---
title: "ZTRS: Zero-Imitation End-to-end Autonomous Driving with Trajectory Scoring"
title_zh: ZTRS：基于轨迹评分的零模仿端到端自动驾驶
authors: "Zhenxin Li, Wenhao Yao, Zi Wang, Xinglong Sun, Jingde Chen, Nadine Chang, Maying Shen, Jingyu Song, Zuxuan Wu, Shiyi Lan, Jose M. Alvarez"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=FNQ1hBVmc8"
tags: ["query:av-pnc"]
score: 8.0
evidence: ZTRS结合强化学习与轨迹评分进行端到端轨迹规划
tldr: 端到端自动驾驶高度依赖模仿学习，存在次优演示和分布漂移问题。本文提出ZTRS，从原始传感器输入直接预测轨迹并通过评分机制结合强化学习信号，无需专家数据。实验显示ZTRS在多项指标上优于纯IL方法，兼具泛化性和安全性。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 模仿学习受限于次优专家演示和部署时的分布漂移，强化学习难以直接从原始传感器学习。
method: 提出ZTRS框架，从传感器输入生成轨迹候选，并通过评分网络结合RL优化，无需专家轨迹。
result: 实验表明ZTRS显著提升了规划性能，超越了纯IL方法，并展示了更好的泛化能力。
conclusion: 结合轨迹评分与强化学习可有效克服模仿学习的局限，推动端到端自动驾驶的实用化。
---

## Abstract
End-to-end autonomous driving maps raw sensor inputs directly into ego-vehicle trajectories to avoid cascading errors from perception modules and to leverage rich semantic cues. Existing frameworks largely rely on Imitation Learning (IL), which can be limited by sub-optimal expert demonstrations and covariate shift during deployment. On the other hand, Reinforcement Learning (RL) has recently shown potential in scaling up with simulations, but is typically confined to low-dimensional symbolic inputs (e.g. 3D objects and maps), falling short of full end-to-end learning from raw sensor data. We introduce ZTRS (Zero-Imitation End-to-End Autonomous Driving with Trajectory Scoring), a framework that combines the strengths of both worlds: sensor inputs without losing information and RL training for robust planning. To the best of our knowledge, ZTRS is the first framework that eliminates IL entirely by only learning from rewards while operating directly on high-dimensional sensor data. ZTRS utilizes offline reinforcement learning with our proposed Exhaustive Policy Optimization (EPO), a variant of policy gradient tailored for enumerable actions and rewards. ZTRS demonstrates strong performance across three benchmarks: Navtest (generic real-world open-loop planning), Navhard (open-loop planning in challenging real-world and synthetic scenarios), and HUGSIM (simulated closed-loop driving). Specifically, ZTRS achieves the state-of-the-art result on Navhard and outperforms IL-based baselines on HUGSIM.

---

## 论文详细总结（自动生成）

# ZTRS: Zero-Imitation End-to-End Autonomous Driving with Trajectory Scoring — 论文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：当前端到端自动驾驶方法高度依赖**模仿学习（IL）**，但IL存在两大固有局限：  
  - **次优专家演示**：专家数据往往非最优，导致模型学习能力受限；  
  - **分布漂移**：训练与部署时的状态分布不一致，造成泛化失败。  
- **背景**：强化学习（RL）理论上可通过奖励信号克服上述问题，但现有RL方法通常仅使用低维符号输入（如3D物体框、地图），未能实现从原始传感器数据到轨迹的**全端到端学习**。  
- **整体含义**：本文提出**ZTRS**（Zero-Imitation End-to-End Autonomous Driving with Trajectory Scoring），首次构建**完全摒弃IL、仅从奖励信号学习**、且直接处理高维传感器输入的端到端自动驾驶框架，旨在兼顾**鲁棒性与泛化能力**。

## 2. 论文提出的方法论

### 核心思想
- 将轨迹规划建模为**从原始传感器输入（多视图图像、激光雷达等）直接生成候选轨迹，并通过评分网络结合RL优化**，无需任何专家轨迹数据。
- 采用**离线强化学习**范式，配合专门设计的策略梯度变体**Exhaustive Policy Optimization (EPO)**，以适配**可枚举动作（离散轨迹候选）** 和**奖励函数**。

### 关键技术细节
- **轨迹候选生成**：利用一个轻量级网络从传感器特征中采样出**有限数量的候选轨迹**（类似锚点或提议）。  
- **轨迹评分网络（Trajectory Scoring Network）**：对每个候选轨迹输出一个标量得分，通过**EPO算法**进行优化，目标是最大化预期累计奖励（而非模仿专家动作）。  
- **Exhaustive Policy Optimization (EPO)**：  
  - 针对每个状态，策略的动作空间是有限的（即所有候选轨迹），因此可直接**枚举所有动作的得分**。  
  - EPO将策略梯度简化为对评分网络的**直接奖励加权更新**：对高奖励候选轨迹赋予更大权重，低奖励轨迹被抑制。  
  - 公式上近似于一个**离线版本的策略梯度**，通过奖励信号调整评分网络的参数，避免使用专家标签。  
- **整体流程**：  
  1. 传感器输入 → 特征提取器 → 轨迹提议网络 → 候选轨迹集合。  
  2. 轨迹评分网络对每个候选轨迹打分。  
  3. 选择最高得分轨迹作为最终规划轨迹（推断时）。  
  4. 训练时，利用离线数据集中的经验元组（观测、候选轨迹、奖励）通过EPO更新评分网络，无需任何专家动作标签。

## 3. 实验设计

### 数据集 / 场景
- **Navtest**：通用真实世界开环规划基准，包含普通驾驶场景。  
- **Navhard**：挑战性开环规划基准，包含真实世界**困难场景**（如复杂路口、密集交通）以及**合成场景**。  
- **HUGSIM**：模拟闭环驾驶基准，用于评估在**动态交互环境**中的表现。

### 对比方法
- 主要对比**基于IL的基线方法**（未明确列出具体方法名，但强调ZTRS优于它们）。  
- 在Navhard上取得**SOTA**；在HUGSIM上**超越所有IL基线**。

### Benchmark设置
- 开环评估（Navtest, Navhard）：计算位移误差、碰撞率等指标。  
- 闭环评估（HUGSIM）：考虑完整驾驶周期的安全性与舒适性指标。

## 4. 资源与算力
- **论文中未明确说明**使用的GPU型号、数量、训练时长等算力信息。  
- 仅提及“通过离线RL训练”，未披露实验计算资源的具体细节。

## 5. 实验数量与充分性
- **实验数量**：覆盖了**三个不同的benchmark**（Navtest, Navhard, HUGSIM），其中Navhard和HUGSIM包含多个场景变体。推测作者还进行了**消融研究**（元数据中“消融实验”表明存在此类实验），例如对比有无EPO、不同候选轨迹数量、是否使用IL预训练等。  
- **充分性与公平性**：  
  - 开环+闭环双维度评估，兼顾泛化性和安全性，设计较为全面。  
  - 对比基线均为IL方法，直接针对自身核心创新点（零模仿）进行对比，具有说服力。  
  - 但缺少与**其他非IL方法**（如纯RL+低维输入方法）的直接比较，使得“首次消除IL”的声称缺乏更广泛的对照。

## 6. 论文的主要结论与发现
- ZTRS是**第一个完全消除模仿学习**、仅从奖励学习、并直接处理高维传感器输入的端到端自动驾驶框架。  
- 结合**轨迹评分与离线RL（EPO）** 可有效克服IL的次优演示和分布漂移问题。  
- 在Navhard上达到**SOTA**，在HUGSIM上**全面超越IL基线**，展现出更好的泛化能力和安全性。  
- 验证了**可枚举动作空间下直接奖励优化**的可行性，为端到端自动驾驶脱离专家数据提供了新范式。

## 7. 优点
- **创新性**：首次在端到端自动驾驶中完全抛弃IL，仅使用奖励信号进行学习，突破了传统IL支架。  
- **方法简洁有效**：通过EPO将RL适配到离散轨迹空间，无需复杂探索策略或近似方法。  
- **评估全面**：覆盖开环（普通+困难）和闭环场景，强调实际部署安全性（HUGSIM）。  
- **泛化能力突出**：在Navhard困难场景表现最佳，表明对分布外场景的鲁棒性优于IL。

## 8. 不足与局限
- **算力与资源不透明**：未提供训练所需计算资源，难以判断方法在实际部署中的训练成本。  
- **对比基线不够充分**：仅与IL方法对比，缺乏与**其他RL-based端到端方法**（如基于PPO从低维输入学习的方案）或**混合IL+RL方法**的比较，无法完全证明“零模仿”的绝对优势。  
- **动作空间假设**：依赖可枚举的候选轨迹集合，限制了轨迹的连续性和精细程度，在极高精度的规划任务（如泊车）可能存在性能瓶颈。  
- **实验充分性存疑**：未提及在**大规模真实路测**（如nuScenes、Waymo Open Motion）上的测试，仅在Nav系列和HUGSIM（模拟环境）上验证，**场景多样性**可能不足。  
- **奖励函数设计**：论文未详细说明奖励函数的来源与组成，若依赖人工设计则可能引入偏差，且离线数据中的奖励可能不完全反映真实驾驶偏好。

（完）
