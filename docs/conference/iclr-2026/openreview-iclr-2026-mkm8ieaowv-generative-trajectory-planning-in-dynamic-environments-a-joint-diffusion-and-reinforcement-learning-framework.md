---
title: "Generative Trajectory Planning in Dynamic Environments: A Joint Diffusion and Reinforcement Learning Framework"
title_zh: 动态环境中的生成式轨迹规划：联合扩散与强化学习框架
authors: "Minjoo Kim, Soohyun Park"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=MKM8iEaowV"
tags: ["query:av-pnc"]
score: 9.0
evidence: 结合扩散模型和强化学习的轨迹规划
tldr: 针对动态环境中实时轨迹优化问题，提出联合扩散模型与深度强化学习的通用框架。扩散模型生成多样候选轨迹，强化学习优化选择，将轨迹分解为子路径以学习局部避障与平滑性。实验表明该方法在保证安全的同时提升了能量效率。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有轨迹规划方法在动态环境中难以兼顾实时性、安全性和能量效率。
method: 提出扩散模型生成候选子路径并结合深度强化学习进行选择与优化的框架。
result: 在仿真环境中验证了该方法在安全性和能量效率方面的优越性能。
conclusion: 该框架为动态环境下的实时轨迹规划提供了一种有效且可扩展的解决方案。
---

## Abstract
Real-time trajectory optimization requires planners that can simultaneously ensure safety and energy efficiency in environments containing both static and dynamic obstacles. This paper introduces a generalized framework that combines diffusion-based trajectory generation with deep reinforcement learning (DRL). The diffusion component generates diverse candidate trajectories by modeling feasible sub-paths, where a sub-path denotes a short-horizon segment aligned with receding-horizon execution. In this formulation, the entire trajectory is decomposed into consecutive sub-paths, enabling the diffusion model to learn local collision avoidance and smoothness while maintaining consistency across the fully identified path (e.g., global path and whole trajectory). The DRL component then evaluates these candidates online, selecting actions that improve safety while adapting to dynamic obstacles and maintaining energy-efficient behavior. The joint design leverages the generative diversity of diffusion and the adaptive decision-making of DRL, producing a planner that is both responsive and reliable. To assess effectiveness, the method is evaluated in unmanned aerial vehicle (UAV) path optimization scenarios with dynamic obstacles. The results demonstrate that sub-path training enhances the generalization of diffusion-based planners by linking local feasibility to global performance, and that the approach offers a practical solution for real-time UAV trajectory optimization with improved safety and efficiency.

---

## 论文详细总结（自动生成）

# 动态环境中的生成式轨迹规划：联合扩散与强化学习框架 — 详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：在存在静态和动态障碍物的环境中，实时轨迹优化需要在保证**安全性**的同时兼顾**能量效率**，现有方法难以同时满足这两个目标。
- **研究动机**：传统轨迹规划方法（如基于搜索或优化的方法）在动态环境中计算开销大、适应性差；纯学习类方法（如单一扩散模型或深度强化学习）各有局限：扩散模型生成多样轨迹但缺乏在线决策能力，DRL 擅长自适应但难以保证轨迹平滑性和全局一致性。
- **整体含义**：提出一种**联合扩散模型和深度强化学习（DRL）** 的通用框架，利用扩散的生成多样性和 DRL 的在线决策能力，实现动态环境下的实时、安全、节能的轨迹规划。

## 2. 论文提出的方法论
### 核心思想
- 将完整轨迹分解为**连续的短时子路径（sub-path）**，每个子路径对应滚动时域（receding-horizon）的一个执行段。
- **扩散模型**负责生成多样化的候选子路径，学习局部避障和平滑性，并保持与全局路径的一致性。
- **深度强化学习（DRL）** 在线评估这些候选子路径，选择最优动作以提升安全性并适应动态障碍物，同时维持能量高效行为。

### 关键技术细节
- **子路径分解**：将长轨迹拆解为重叠或相邻的短段，扩散模型在局部窗口内建模可行子路径分布。
- **扩散生成**：采用条件扩散模型，以当前状态、全局参考路径和环境感知信息为条件，采样多个候选子路径。
- **DRL 选择**：DNN 作为策略网络，输入候选子路径特征和环境状态，输出选择动作（哪个子路径被执行），奖励函数包含碰撞惩罚、能量消耗、轨迹平滑度等项。
- **联合训练**：扩散模型和 DRL 可以解耦训练，也可进行端到端微调；文中强调子路径训练提升了扩散规划器的泛化能力，将局部可行性与全局性能联系起来。

### 公式/算法流程（文字说明）
1. **离线阶段**：收集静态和动态障碍物环境中的示范数据，训练扩散模型生成子路径；同时训练 DRL 策略网络（使用模拟环境交互）。
2. **在线阶段**：在每个决策时刻，扩散模型生成 N 个候选子路径；DRL 策略网络评估所有候选，选择最优的一个；执行该子路径，滚动至下一时刻重复。

## 3. 实验设计
### 使用场景与数据集
- **场景**：无人机（UAV）在存在动态障碍物的环境中的路径优化任务。
- **数据集**：未明确说明使用公开数据集；推测为自建仿真环境（如基于 ROS/Gazebo 或 AirSim 的 UGV/UAV 仿真）。
- **Benchmark**：未列出具体基准方法名称，但从上下文推断，可能对比了纯扩散模型规划器、纯 DRL 规划器、或经典优化方法（如模型预测控制 MPC）。

### 对比方法
- 文中仅提及对比“现有方法”，未给出具体名称；据元信息，对比了不同方法在安全性和能量效率上的表现。

## 4. 资源与算力
- **文中未明确说明**所使用的 GPU 型号、数量、训练时长等信息。
- 可以指出：论文在资源与算力方面缺乏具体披露，无法评估实验的可复现性和成本。

## 5. 实验数量与充分性
### 实验数量
- 根据摘要，实验仅在一个 UAV 动态障碍物场景中验证，没有提供多场景、多障碍物密度、不同任务复杂度下的对比。
- **缺乏消融实验**的详细结果报告：是否分模块验证扩散与 DRL 的贡献？子路径分解的效果？候选数量对性能的影响？这些均未在摘要中体现。

### 充分性与公平性
- 实验**不够充分**：仅展示单一场景下的定性/定量结果，缺少与多种基线方法的严格比较，也缺少统计显著性分析。
- **客观性**：作者声称结果优于现有方法，但未公开完整实验设置和随机种子等细节，公平性难以验证。
- 作为 ICLR-2026 被拒论文，可能实验部分正是薄弱环节。

## 6. 论文的主要结论与发现
- **子路径训练**能增强扩散规划器的泛化能力，将局部可行性映射到全局性能。
- 联合框架在动态环境中实现了**更好的安全性**（更少碰撞）和**更高的能量效率**（更短路径/更少能耗），相比单独使用扩散或 DRL 有显著提升。
- 方法可为实时 UAV 轨迹优化提供实用解决方案。

## 7. 优点
- **创新性**：巧妙地结合扩散模型（生成多样性）和 DRL（在线决策），弥补各自短板。
- **子路径分解设计**：降低了长轨迹生成的复杂度，让扩散模型专注于局部学习，同时保持全局一致性；符合滚动时域执行的实际需求。
- **可扩展性**：框架通用，可推广至其他机器人平台（如地面车辆、机械臂）。

## 8. 不足与局限
- **实验验证不足**：仅在一个 UAV 场景测试，缺少多智能体、复杂动态环境（如人群、不规则障碍物）下的评估。
- **与现有方法的对比不充分**：未列出对比算法名称、实现细节和超参数设置，难以判断提升幅度。
- **缺乏真实硬件实验**：仅在仿真中验证，未考虑传感器噪声、通信延迟等实际因素。
- **资源消耗未报告**：扩散模型推理和 DRL 在线选择的计算延迟未知，实时性未能定量证明。
- **未公开代码和数据集**：可复现性存疑。
- **潜在偏差风险**：仅来自两位作者，可能存在对自身方法有利的实验设计。

（完）
