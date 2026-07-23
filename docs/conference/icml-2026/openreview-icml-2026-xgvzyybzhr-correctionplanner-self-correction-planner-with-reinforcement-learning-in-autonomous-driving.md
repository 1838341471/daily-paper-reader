---
title: "CorrectionPlanner: Self-Correction Planner with Reinforcement Learning in Autonomous Driving"
title_zh: CorrectionPlanner：基于强化学习的自动驾驶自校正规划器
authors: "Yihong Guo, Dongqiangzi Ye, Sijia Chen, Anqi Liu, Xianming Liu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/543172d90bfd7a09d534e91c22b5059750bf2736.pdf"
tags: ["query:av-pnc"]
score: 10.0
evidence: 自动驾驶安全运动规划的自校正规划器
tldr: 本文针对自动驾驶中学习型规划器缺乏自校正能力的问题，提出CorrectionPlanner，一种具有提议、评估、校正循环的自回归规划器。通过碰撞批评家预测碰撞并基于校正轨迹生成新动作，迭代提升安全性。实验表明该方法能有效减少碰撞，为安全规划提供了新思路。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有学习型规划器一旦提出不安全动作，缺乏显式校正机制，威胁自动驾驶安全。
method: 提出包含提议、评估、校正循环的自回归规划器，利用碰撞批评家和历史不安全动作序列生成校正动作。
result: 实验证明该方法能有效减少碰撞，提高规划安全性。
conclusion: 自校正机制显著提升了自动驾驶规划器的安全性和鲁棒性。
---

## Abstract
Autonomous driving requires safe planning, but most learning-based planners lack explicit self-correction ability: once an unsafe action is proposed, there is no mechanism to correct it. Thus, we propose CorrectionPlanner, an autoregressive planner with self-correction that contains a propose, evaluate, and correct loop in the motion-token generation process. At each planning step, the policy proposes an action, namely a motion token, and a learned collision critic predicts whether it will induce a collision within a short horizon. If the critic predicts a collision, we retain the sequence of historical unsafe motion tokens as a self-correction trace, generate the next motion token conditioned on it, and repeat this process until the safe motion token is proposed or the safety criterion is met. This self-correction trace, consisting of all the unsafe motion tokens, represents the planner’s correction process in motion-token space. We train the planner with imitation learning followed by model-based reinforcement learning using rollouts from a pretrained world model that realistically models agents' reactive behaviors. Closed-loop evaluations show that CorrectionPlanner reduces the collision rate by over $20\%$ on Waymax and obtains state-of-the-art planning scores on nuPlan.

---

## 论文详细总结（自动生成）

# CorrectionPlanner 论文总结

## 1. 核心问题与研究动机

- 自动驾驶运动规划对**安全性**要求极高，一旦产生不安全动作可能引发事故。
- 大多数基于学习的规划器（如模仿学习、强化学习）是**开环生成**的：它们直接输出动作序列，缺乏**显式的自纠正能力**。如果生成了不安全动作，系统无法在规划内部进行修正，只能依赖外部控制器或重新规划。
- 本研究旨在解决**学习型规划器“提出动作后无法自我修正”的问题**，通过引入“提出‑评估‑纠正”闭环机制，使规划器能够在生成过程中主动识别并纠正不安全候选动作。

## 2. 方法论

### 核心思想
- 将规划过程建模为**自回归运动令牌生成**，并在生成过程中嵌入**自纠正循环**：策略**提出**一个运动令牌 → 碰撞评判模型**评估**短期碰撞风险 → 如果预测到碰撞，则**保留历史不安全令牌**作为纠正痕迹，**重新生成**下一个令牌，直到提出安全令牌或满足安全终止条件。

### 关键技术细节
- **运动令牌生成**：使用自回归策略逐令牌生成未来运动序列。
- **碰撞评判模型（collision critic）** ：一个学习的模型，接收当前提出的运动令牌和场景上下文，预测在**短时间窗内是否会发生碰撞**。
- **自纠正轨迹（self-correction trace）**：所有被碰撞评价器判定为不安全的运动令牌序列，被显式保留并作为条件输入，用于指导后续令牌的重新生成。该轨迹本身就是规划器在运动令牌空间中的纠正过程。
- **训练流程**：
    1. **模仿学习阶段**：使用专家驾驶数据对策略和碰撞评判模型进行行为克隆预训练。
    2. **基于模型的强化学习阶段**：利用预训练的世界模型（能够真实建模其他交通参与者的反应行为）进行纵向推演（rollouts），对策略进行强化学习微调，进一步优化安全性和驾驶质量。

## 3. 实验设计

- **数据集与仿真平台**：
  - **Waymax**：用于闭环评估，验证碰撞避免能力。
  - **nuPlan**：大规模自动驾驶规划基准，评估综合规划性能。
- **主要评估指标**：
  - 碰撞率（Waymax上降低超过20%）。
  - nuPlan综合规划得分（达到最先进水平）。
- **对比方法**：原文未在摘要中具体列出对比的基准方法名称，但提及“大多数学习型规划器”以及“state-of-the-art planning scores on nuPlan”，暗示与现有的学习型规划器（可能包含模仿学习、强化学习基线）进行了对比。

## 4. 资源与算力

- 摘要和元数据中**未提供**关于GPU型号、数量、训练时长等算力细节，无法给出具体信息。

## 5. 实验数量与充分性

- 根据现有信息，论文至少包含以下实验组：
  - 闭环碰撞避免实验（Waymax平台）
  - 开放环路规划质量实验（nuPlan平台）
- 未提及消融实验（如移除自纠正机制、不同评判模型架构等）、不同场景类型分解或与更多基线的详细对比，**无法判断实验的全面性和数据充分性**。
- 封闭式摘要未透露实验设置细节，难以评估是否公平（如感知输入、仿真参数、评价协议是否一致）。

## 6. 主要结论与发现

- CorrectionPlanner通过内置的“提出‑评估‑纠正”循环，**显著提高了自动驾驶规划的安全性**。
- 在Waymax闭环测试中，碰撞率**降低超过20%**；在nuPlan规划基准上，取得了**最先进的规划分数**。
- 该自纠正机制不依赖外部黑名单或后处理规则，而是学习在训练过程中内化安全修正能力，为安全关键应用提供了可靠基础。

## 7. 优点

- **显式自纠正机制**：首次在自回归规划中将碰撞评判与历史不安全轨迹相结合，实现动态修正，弥补了传统学习型规划器的关键短板。
- **训练框架务实**：模仿学习+基于模型的RL，利用世界模型建模多智能体交互，平衡了样本效率和闭环安全性。
- **闭环评估验证**：在Waymax上进行真实闭环碰撞测试，而非仅依赖开环轨迹误差，更有实际说服力。
- **可解释的纠正过程**：以运动令牌序列形式保留不安全尝试，便于分析和调试。

## 8. 不足与局限

- **实验报告非常有限**：仅给出两个平台的总体提升，缺乏对比方法列表、消融分析、失败案例剖析，可复现性和公平性存疑。
- **依赖世界模型**：基于模型的RL训练效果受世界模型精度制约，若世界模型不能真实模拟他车反应，安全纠正可能在现实中失效。
- **计算代价未知**：每一步生成循环可能需要多次评判与重生成，推理延迟和计算量未说明，可能不适合极低延迟需求。
- **纠正范围受限**：碰撞评判仅看短期视野，可能无法避免长时序下的危险情况；且只纠正碰撞，不涵盖其他约束（如交通规则、舒适性）。
- **数据与场景覆盖**：未明确使用的场景类型分布（城市/高速/交叉口），泛化能力有待进一步验证。

（完）
