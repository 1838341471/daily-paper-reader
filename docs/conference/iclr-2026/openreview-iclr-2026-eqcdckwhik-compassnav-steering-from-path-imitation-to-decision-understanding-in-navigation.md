---
title: "CompassNav: Steering From Path Imitation to Decision Understanding In Navigation"
title_zh: CompassNav：从路径模仿转向决策理解的导航
authors: "LinFeng Li, Jian Zhao, Yuan Xie, Xin Tan, Xuelong Li"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=eqcDckWHik"
tags: ["query:av-pnc"]
score: 4.0
evidence: CompassNav关注导航中的决策理解，与行为规划相关
tldr: 当前导航训练依赖模仿专家轨迹，限制了探索和泛化能力。本文转向决策理解范式，提出Compass-Data-22k数据集和强化微调子集，提供决策全景。实验显示该方法在未见环境中表现出更强的决策鲁棒性。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 模仿学习使导航代理缺乏真正的决策理解能力，泛化性差。
method: 提出决策理解范式，构建含22k轨迹的数据集，并通过强化微调提供决策全景视角。
result: 实验表明该范式在未见场景中决策鲁棒性显著优于传统模仿方法。
conclusion: 从路径模仿到决策理解的转变是提升导航代理泛化能力的关键。
---

## Abstract
The dominant paradigm for training Large Vision-Language Models (LVLMs) in navigation relies on imitating expert trajectories. This approach reduces the complex navigation task to a sequence-to-sequence replication of a single correct path, fundamentally limiting the agent's ability to explore and generalize. In this work, we argue for and introduce a new paradigm: a shift from Path Imitation to Decision Understanding. The goal of this paradigm is to build agents that do not just follow, but truly understand how to navigate. We materialize this through two core contributions: first, we introduce Compass-Data-22k, a novel 22k-trajectory dataset.Its Reinforcement Fine-Tuning (RFT) subset provides a panoramic view of the decision landscape by annotating all feasible actions with A* geodesic distances. Second, we design a novel gap-aware hybrid reward function that dynamically adapts its feedback to decision certainty, shifting between decisive signals for optimal actions and nuanced scores to encourage exploration. Integrated into an SFT-then-RFT recipe, our CompassNav agent is trained not to memorize static routes, but to develop an internal ``compass'' that constantly intuits the direction to the goal by evaluating the relative quality of all possible moves. This approach enables our 7B agent to set a new state-of-the-art on Goal navigation benchmarks, outperforming even larger proprietary models, and achieve robust real-world goal navigation on a physical robot.

---

## 论文详细总结（自动生成）

# 论文总结：CompassNav：从路径模仿转向决策理解的导航

## 1. 核心问题与整体含义（研究动机和背景）
- **研究动机**：当前主流导航训练范式依赖**模仿学习**（如模仿专家轨迹），将复杂导航任务简化为对单条“正确”路径的序列到序列复制，严重限制了智能体的**探索能力**与**泛化能力**，导致其在**未见环境**中决策鲁棒性不足。
- **整体含义**：论文提出从“路径模仿”转向“决策理解”的新范式，旨在构建**真正理解导航逻辑**的智能体，而非仅仅复现固定路线。这一转变对于提升大型视觉-语言模型（LVLMs）在机器人导航等领域的实用性和适应能力至关重要。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：通过提供**全景决策视角**（panoramic view of decision landscape），让模型学习评估所有可行动作的相对优劣，而非记忆单一最优路径，从而发展出内在的“指南针”（compass）——能够直观判断朝向目标的正确方向。
- **关键技术细节**：
  - **数据集构建**：提出 **Compass-Data-22k** 数据集，包含22k条轨迹。其中**强化微调（RFT）子集**为每条轨迹的所有可行动作标注了 **A* 测地线距离**（geodesic distance），从而提供决策空间的“全景”视图。
  - **奖励函数设计**：提出一种**差距感知混合奖励函数**（gap-aware hybrid reward function），能够根据**决策确定性**动态调整反馈：对于最优动作提供明确（decisive）信号，对于其他动作则给出细致（nuanced）分数以鼓励探索。
  - **训练流程**：采用 **SFT（监督微调）→ RFT（强化微调）** 的先后顺序。先通过模仿学习建立基础能力，再通过RFT（结合上述奖励函数）强化决策理解，使其不记忆静态路线，而是学会对所有可能动作进行相对质量评估。
  - **算法流程描述**：并未给出显式公式或伪代码，但整体可概括为：①预训练LVLM → ②SFT阶段：在Compass-Data-22k的标准轨迹上模仿学习 → ③RFT阶段：输入状态→模型输出动作概率分布→根据A*距离标签和混合奖励计算回报→强化学习更新参数。

## 3. 实验设计：数据集、基准、对比方法
- **数据集**：使用自建的 **Compass-Data-22k** 数据集（包含22k条轨迹及其RFT子集）。此外在评估阶段使用了**Goal Navigation benchmarks**（具体名称未提及，但为公开基准），并部署在**实体机器人**上进行真实世界目标导航。
- **基准**：Goal Navigation benchmark（如可能是Habitat、Matterport3D等环境中的PointGoal或ObjectGoal任务）。
- **对比方法**：对比了更大规模的**专有模型**（proprietary models），以及可能包括标准的模仿学习方法（如Behavior Cloning）。未明确列出所有对比方法，但声称7B参数模型超过了更大专有模型，暗示其SOTA地位。

## 4. 资源与算力
- 论文摘要及元数据中**未明确说明**使用的GPU型号、数量、训练时长等具体算力信息。仅有模型大小（7B参数）提及，但未说明训练该7B模型所需资源。因此需要指出这一点缺失。

## 5. 实验数量与充分性
- **实验数量**：文中提及在Goal Navigation benchmark上评估（可能包含多个子任务），并进行了**实体机器人验证**。此外，通过构建RFT子集并与SFT对比，隐含了**消融实验**（比较SFT vs. SFT+RFT）。但未详细列出分组实验数量（如不同场景、不同泛化测试的组数）。
- **充分性与客观性**：基准测试+真实机器人验证增加了说服力；但缺少对多个环境、多种干扰条件、大规模消融的详细描述，也缺少与更多基线方法的全面对比。整体实验设计具有一定说服力，但**充分性有待完善**（例如未报告标准差、统计显著性等）。

## 6. 主要结论与发现
- **性能领先**：7B参数的CompassNav代理在Goal Navigation benchmark上取得了**新SOTA**，性能超越更大尺寸的专有模型。
- **泛化能力提升**：在**未见环境**（包括真实机器人场景）中表现出更强的**决策鲁棒性**，而传统模仿方法则表现退化。
- **范式转变有效**：从模仿路径到决策理解的转变是提升导航代理泛化能力的关键，所提出的数据集、奖励函数和训练流程构成了一套可行方案。

## 7. 优点：方法或实验设计上的亮点
- **问题切入深刻**：直接挑战当前导航模仿学习的根本局限，提出认识论上的范式换新。
- **数据集创新**：Compass-Data-22k的RFT子集通过A*测地距离为所有可行动作提供质量标签，使得决策理解训练成为可能，具有很好的数据表征价值。
- **奖励函数动态性**：gap-aware hybrid reward能平衡确定性奖励与探索鼓励，避免训练崩溃。
- **双阶段训练**：SFT-then-RFT以模仿为起点、强化为进阶，渐进式培养决策理解。
- **实体验证**：在真实机器人上部署，验证方法实用性，增加了工程价值。

## 8. 不足与局限
- **实验覆盖有限**：仅提及一个benchmark（Goal Navigation），未在多个导航环境（如室内、室外、动态障碍）上测试；RFT子集规模22k可能仍不足以保证极端泛化。
- **对比方法不够全面**：未详细列出与当前主流导航LVLM（如CoW, NavGPT等）的全面对比，且缺乏对纯强化学习方法（如RL without imitation）的对比。
- **资源与复现信息缺失**：未给出训练所需算力、超参数等细节，增加了复现难度。
- **可能偏差风险**：RFT子集基于A*距离，但A*作为全局规划器可能不适合部分动态环境，导致训练数据存在间接偏差；奖励函数的“gap-aware”设计可能对超参数敏感，未做充分鲁棒性分析。
- **应用限制**：目前仅聚焦于目标导航（goal navigation），未探索更复杂任务（如指令跟随、动态避障等）；7B模型部署在实体机器人上可能对计算资源有较高要求。

（完）
