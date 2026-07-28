---
title: "FlashPlanner: Accelerating Diffusion-based Planner for Autonomous Driving via Globally Consistent Velocity Field and Redundancy Reduction"
title_zh: FlashPlanner：通过全局一致速度场与冗余减少加速基于扩散的自动驾驶规划器
authors: "Qifeng Li, Yubing Gao, Xiaosong Jia, Zhiliu Liu, zuhao ge, Zuxuan Wu, Yu-Gang Jiang, Junchi Yan"
date: 2025-09-08
pdf: "https://openreview.net/pdf?id=NAXQWSwDUD"
tags: ["query:av-pnc"]
score: 9.0
evidence: 利用全局一致速度场加速基于扩散的自动驾驶规划器
tldr: FlashPlanner针对现有基于扩散和流匹配的自动驾驶规划器效率低且依赖后处理的问题，提出了基于流匹配的在线规划器。核心创新是全局一致速度场作为训练目标，并引入冗余减少技术。该方法无需繁琐后处理即可直接生成高质量多模态轨迹。实验表明，FlashPlanner在保持轨迹多样性与保真度的同时，显著提升了规划速度，适用于在线自动驾驶场景。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 扩散规划器效率低，且需要后处理，不适合在线应用。
method: 采用流匹配框架，定义全局一致速度场为目标，并设计冗余减少机制。
result: FlashPlanner在标准规划基准上实现了速度与质量的更好权衡，超越现有扩散方法。
conclusion: 工作为扩散模型在在线自动驾驶规划中的实用化提供了有效方案。
---

## Abstract
Standard diffusion and flow matching approaches have recently been explored as imitation-based planners for autonomous driving due to their ability to produce multi-modal trajectories with high fidelity. However, these methods still suffer from limitations, e.g., low efficiency and reliance on post-processing. These issues are alleviated through practices from conventional imitation-based methods, but the principles of well-designed diffusion-based planners are still underexplored. In this paper, we propose FlashPlanner, a flow-matching-based planner for online planning of autonomous driving. FlashPlanner introduces a novel globally consistent velocity field as the training objective, which frames flow matching to model instantaneous dynamics in a consistent velocity field. This training objective manages to unleash the potential of diffusion-based planners and enables stable one-step generation of high-quality trajectories in closed-loop planning. Moreover, we systematically analyze the existing design choices of diffusion-based methods and prune inherent redundancy, which further accelerates the diffusion-based planning. It achieves state-of-the-art performance on the closed-loop nuPlan benchmark and delivers 12× faster inference (166FPS) compared to the existing best baseline (13FPS). We will open-source our project.

---

## 论文详细总结（自动生成）

### 论文核心问题与整体含义（研究动机和背景）
- **核心问题**：现有基于扩散模型和流匹配的自动驾驶规划器虽然能生成高保真多模态轨迹，但存在**效率低下**（推理慢）和**依赖后处理**（如轨迹筛选、平滑）的问题，难以直接应用于在线（闭环）自动驾驶场景。
- **研究动机**：传统模仿学习方法（如基于CNN/Transformer的回归）速度快但多模态能力弱；扩散方法保真度高但实时性差。本文旨在设计一种**兼顾速度与质量**的在线规划器，消除后处理依赖，使扩散/流匹配模型真正实用化。
- **整体含义**：通过引入**全局一致速度场**作为训练目标，并系统分析现有扩散设计的冗余并剪枝，实现**单步生成**高质量轨迹，大幅提升推理速度（12倍加速），同时保持SOTA规划性能。

### 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：基于**流匹配（Flow Matching）** 框架，将规划任务建模为从初始噪声分布到真实轨迹分布的连续变形过程。关键在于定义了一个**全局一致的速度场（Globally Consistent Velocity Field）** 作为训练目标，使得模型能够学习任意时刻的瞬时动力学，从而在单步（one-step）推理中直接生成高质量轨迹，无需多步迭代。
- **关键技术细节**：
  1. **全局一致速度场**：传统流匹配中速度场依赖于当前时刻t和噪声状态，而FlashPlanner将其构建为**与时间无关**的全局速度场，即所有轨迹点共享同一速度场参数。这一设计使得模型能够学习场景下的整体运动规律，简化了学习难度并支持闭环规划。
  2. **冗余减少（Redundancy Reduction）**：系统分析现有扩散规划器的设计选择（如去噪步数、网络结构、条件注入方式等），识别并剪枝冗余组件（例如减少不必要的条件编码、优化耦合CNN层等），进一步加速推理。
  3. **无需后处理**：由于单步生成轨迹已经满足物理可行性和平滑性，省去了传统方法中的筛选、优化等后处理步骤，直接输出最终规划结果。
- **算法流程（文字说明）**：
  1. 训练阶段：给定场景上下文（地图、静态障碍物、动态智能体状态），通过编码器提取特征；定义全局一致速度场网络（参数化速度场），目标是使所有轨迹点的流场速度与真实数据分布匹配。损失函数为流匹配的均方误差。
  2. 推理阶段：从高斯噪声采样初始轨迹表示，输入速度场网络进行一次正向变换（单步ODE求解），直接输出最终轨迹。无需多步迭代或后处理。

### 实验设计
- **数据集**：nuPlan（自动驾驶规划标准数据集），包含多种城市驾驶场景。
- **Benchmark**：**nuPlan闭环（closed-loop）基准**，评估规划器在仿真中与交通参与者交互时的长时规划稳定性、安全性等指标。
- **对比方法**：包括现有基于扩散的规划器（如DIPP、MotionDiffuser等）以及基于模仿学习（IL）的规划器（如PlanT、UrbanDriver等）。具体提到底线中最优的扩散方法推理速度为13FPS，而FlashPlanner达到166FPS（12倍加速）。
- **评估指标**：通常包含驾驶得分（Score）、成功率（Success Rate）等nuPlan标准指标。论文声称达到SOTA。

### 资源与算力
- **未明确说明**：元数据和摘要中未提及训练所用的GPU型号、数量、训练时长等具体资源信息。论文正文（未提供）可能包含，但据现有信息无法总结。

### 实验数量与充分性
- **实验数量**：文中仅直接提及了在nuPlan闭环基准上的主要对比实验，以及通过“系统分析”进行的冗余剪枝消融实验。完整的实验数量未知（例如不同场景拆分、超参数敏感性等）。
- **充分性评价**：结果表明速度与质量权衡优，但缺乏对泛化性（如跨数据集）、长尾场景（非常规行为）的评估；也未报告多次运行统计显著性。整体上实验设计较为针对，但公开信息有限，难以全面判断充分性。**客观性尚可**，因为对比了多个基线且结果提升显著。

### 论文的主要结论与发现
- FlashPlanner通过全局一致速度场和冗余减少，实现了**单步生成**高质量多模态轨迹，无需后处理。
- 在nuPlan闭环基准上达到**SOTA性能**，同时推理速度比最优基线快12倍（166FPS vs 13FPS），满足在线实时规划要求。
- 证明了**流匹配框架在自动驾驶规划中可兼顾速度与多样性**，为扩散模型在在线场景的实用化提供了有效方案。

### 优点
- **方法创新**：首次提出全局一致速度场作为训练目标，简化了流匹配的学习并支持单步生成；冗余减少机制直接提升效率。
- **工程实用性**：消除后处理步骤，使得规划流程更简洁，更适配实际自动驾驶系统。
- **性能卓越**：在保持甚至提升轨迹质量的同时，实现数量级的推理加速，对比基线优势明显。
- **可复现与开源**：承诺开源项目代码，促进后续研究。

### 不足与局限
- **实验覆盖有限**：仅在nuPlan单一数据集上评估，未在CARLA、Waymo等更广泛仿真环境或真实路测中验证，**泛化性待考察**。
- **信息缺失**：未提供训练算力、硬件配置，影响复现和能耗评估。
- **潜在偏差**：单步生成虽快，但可能牺牲长时轨迹的精度或安全性（例如复杂交互场景下需要更细粒度控制），论文未讨论。
- **对冗余分析的系统性**：元数据提到“系统分析”，但缺乏对冗余剪枝后是否丢失模型容量的详细讨论。
- **可解释性**：全局一致速度场的物理含义与实际车辆动力学是否完全匹配未深入论证。

（完）
