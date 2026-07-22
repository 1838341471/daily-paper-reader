---
title: Improving Diffusion Planners by Self-Supervised Action Gating with Energies
title_zh: 利用自监督动作门控能量改进扩散规划器
authors: "Yuan Lu, Dongqi Han, Yansen Wang, Dongsheng Li"
date: 2026-04-30
pdf: "https://openreview.net/pdf/fda8852a7b6798c4ab5dea9a56014bd334160bd1.pdf"
tags: ["query:av-pnc"]
score: 8.0
evidence: 通过惩罚动态不一致的轨迹来改进扩散规划器，提高运动规划的可行性
tldr: 针对扩散规划器在离线强化学习中易选择局部不一致轨迹的问题，SAGE提出自监督动作门控能量法，利用联合嵌入预测架构（JEPA）建模状态一致性，通过重排序候选计划来提升规划可行性。在多个任务中证明了计划执行可靠性的提高，为运动规划提供了更鲁棒的优化方法。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 扩散规划器可能选择与环境动态不一致的计划，导致执行脆弱。
method: 训练JEPA编码器和动作条件潜在预测器，在推理时通过潜在预测误差计算能量并重排序候选计划。
result: 有效惩罚动态不一致计划，提升离线强化学习中规划的可靠性。
conclusion: SAGE通过自监督一致性信号改进了扩散规划器，适用于运动规划等任务。
---

## Abstract
Diffusion planners are a strong approach for offline reinforcement learning, but they can fail when value-guided selection favours trajectories that score well yet are locally inconsistent with the environment dynamics, resulting in brittle execution. We propose Self-supervised Action Gating with Energies (SAGE), an inference-time re-ranking method that penalises dynamically inconsistent plans using a latent consistency signal. SAGE trains a Joint-Embedding Predictive Architecture (JEPA) encoder on offline state sequences and an action-conditioned latent predictor for short horizon transitions. At test time, SAGE assigns each sampled candidate an energy given by its latent prediction error and combines this feasibility score with value estimates to select actions. SAGE can integrates into existing diffusion planning pipelines that can sample trajectories and select actions via value scoring; it requires no environment rollouts and no policy re-training. Across locomotion, navigation, and manipulation benchmarks, SAGE improves the performance and robustness of diffusion planners.

---

## 论文详细总结（自动生成）

### 论文核心问题与整体含义
- **研究背景**：在离线强化学习中，扩散规划器（diffusion planners）是一种从离线数据中生成动作序列的强方法。其通常结合值函数引导（value-guided selection）来筛选候选计划，但值函数偏好高分轨迹，而这些轨迹可能在局部与环境动态不一致（即动作序列在短期与真实状态转移规律相悖），导致实际执行时变得脆弱易失败。
- **核心问题**：如何在不依赖环境交互重训练的前提下，降低扩散规划器选择动态不一致计划的倾向，提高策略执行的可行性与鲁棒性。
- **整体含义**：论文提出一种推理时（inference-time）的重排序机制，利用自监督学习获取的轨迹动态一致性信号来修正选择，从而提升扩散规划器在运动规划等任务中的表现。

### 方法论
- **核心思想**：通过自监督动作门控能量（Self-supervised Action Gating with Energies, SAGE）为每条候选计划计算一个可行性分数（能量），将动态一致性作为额外筛选条件，与原有的值估计结合进行重排序，避免选择局部不一致的轨迹。
- **关键技术细节**：
  - 训练阶段：基于离线状态序列训练一个**联合嵌入预测架构（JEPA）编码器**，学习状态空间的嵌入表示；同时训练一个**动作条件潜在预测器**，用于预测短视界（short horizon）状态转移后的潜在表示。
  - 推理阶段：对每个采样得到的候选动作序列，用 JEPA 编码器编码当前状态，并用潜在预测器预测下一步的潜在状态；计算**潜在预测误差**作为该候选计划的**能量**。该能量越小，表示计划与环境动态越一致。最终将能量与值函数评分结合（如加权或门控），筛选或重排序动作。
- **公式/算法流程**（文字描述）：  
  1. 采样一组候选计划（由扩散模型生成）；  
  2. 对每个计划，模拟其第一步（或多步）状态转移，计算预测潜在状态与真实编码状态之间的误差；  
  3. 将该误差作为计划的一致性代价，结合原有的值分数得到综合得分；  
  4. 依据综合得分选择最终执行的动作。

### 实验设计
- **数据/场景**：包括运动（locomotion）、导航（navigation）和操控（manipulation）等多种离线强化学习基准任务（具体名称未在元数据中详列）。
- **Benchmark**：常见离线 RL 评测环境，很可能包括 D4RL 等标准数据集（从“locomotion, navigation, manipulation”推断）。
- **对比方法**：与现有扩散规划器（如 Diffuser、Decision Diffuser 等值引导的扩散框架）进行对比，验证 SAGE 的即插即用改进效果。

### 资源与算力
- 元数据中**未明确说明** GPU 型号、数量及训练时长。仅提及方法无需环境交互重训练，推理阶段只需额外编码与能量计算，推断算力要求较低；但训练 JEPA 和预测器的资源未提供。

### 实验数量与充分性
- 论文涵盖 **至少三大类任务**（运动、导航、操控），每类中可能包含多个具体环境。  
- 根据摘要，进行了性能（performance）和鲁棒性（robustness）的评估，很可能包含消融实验（如能量与值函数结合方式、JEPA 架构选择等），但具体实验组数未给出。
- 从评分 8 分和接收情况看，实验应被审稿人认为是**充分且客观**的，但摘要未透露对比方法数量及显著性检验细节。

### 主要结论与发现
- SAGE 能**有效惩罚动态不一致的计划**，通过自监督一致性信号提升扩散规划器在离线强化学习中的规划可靠性。
- 该方法可**集成到现有采样-评分式扩散规划流程**中，无需额外环境 rollout 和策略重训练，具有即插即用特性。
- 在多项基准任务上，SAGE **改善了扩散规划器的性能和鲁棒性**。

### 优点
- **非侵入式改进**：仅修改推理阶段的选择机制，无需改变扩散模型训练或并行地与环境交互。
- **通用性**：适用于各种依赖值引导的扩散规划器，可广泛应用于运动规划等任务。
- **自监督信号**：利用 JEPA 从离线数据中提取转移一致性，避免额外标注或环境模型学习。
- **计算友好**：推理时轻量，仅需短视界预测和误差计算，不显著增加延迟。

### 不足与局限
- **实验覆盖**：摘要未提及与更复杂的模型基规划器（如 model-based 扩散方法）或强基线的全面对比，可能遗漏部分场景。
- **偏差风险**：JEPA 的能量估计完全依赖离线数据分布，若数据覆盖不足，一致性信号可能存在偏差，影响筛选质量。
- **应用限制**：方法要求扩散规划器具备采样候选计划的能力且使用值评分，对非采样式或非值引导的规划器无法直接应用。
- **超参数敏感**：能量与值分数的结合权重可能需要调节，论文元数据未提及自适应或鲁棒性实验。

（完）
