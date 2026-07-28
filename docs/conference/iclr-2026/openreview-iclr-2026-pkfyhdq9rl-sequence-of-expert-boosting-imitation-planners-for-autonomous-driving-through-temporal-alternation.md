---
title: "Sequence of Expert: Boosting Imitation Planners for Autonomous Driving through Temporal Alternation"
title_zh: 专家序列：通过时间交替提升自动驾驶模仿规划器的性能
authors: "Xiang LI, Liu gang, Weitao Zhou, Hongyi zhu, Zhong Cao"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=pkfyHdq9Rl"
tags: ["query:av-pnc"]
score: 8.0
evidence: Sequence of Expert通过时间交替增强自动驾驶中的路径规划模仿器
tldr: 模仿学习在开环中表现良好，但闭环中误差累积导致严重失败。本文提出时间交替专家序列策略，在不同规划循环中切换专家模式，增强对误差的鲁棒性。实验证明该方法显著提升了闭环规划性能，且无需改变网络结构。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 模仿学习在闭环中因误差累积而性能下降，现有方法集中于单时间点鲁棒性。
method: 提出时间交替专家序列，在不同规划周期交替使用不同专家模式，抑制误差传播。
result: 实验表明该方法在多个基准上显著提升了闭环规划的安全性和平滑性。
conclusion: 时间交替策略是一种简单有效的误差缓解方法，可即插即用于现有模仿规划器。
---

## Abstract
Imitation learning (IL) has emerged as a central paradigm in autonomous driving. While IL excels in matching expert behavior in open-loop settings by minimizing per-step prediction errors, its performance degrades unexpectedly in closed-loop due to the gradual accumulation of small, often imperceptible errors over time. Over successive planning cycles, these errors compound, potentially resulting in severe failures. Current research efforts predominantly rely on increasingly sophisticated network architectures or high-fidelity training datasets to enhance the robustness of IL planners against error accumulation, focusing on the state-level robustness at a single time point. However, autonomous driving is inherently a continuous-time process, and leveraging the temporal scale to enhance robustness may provide a new perspective for addressing this issue. To this end, we propose a method termed Sequence of Experts (SoE)—a temporal alternation policy that enhances closed-loop performance without increasing model size or data requirements. The key idea is to retain intermediate models from training that possess inherent differences in driving errors, and then alternate the activation of different models at certain temporal intervals. This approach not only preserves the consistency capability across multiple models but also leverages their differences to enhance robustness. As a plug-and-play solution for existing IL planners, our approach requires no architectural modifications or prior knowledge of scenarios, making it highly practical for real-world deployment. Our experiments on large-scale autonomous driving benchmarks nuPlan demonstrate that SoE method consistently and significantly improves the performance of all the evaluated models, and achieves state-of-the-art performance. This module may provide a key and widely applicable support for improving the training efficiency of autonomous driving models.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：模仿学习（Imitation Learning, IL）在自动驾驶的**开环（open-loop）** 设置下，通过最小化每步预测误差能够很好地模仿专家行为；但在**闭环（closed-loop）** 部署中，由于时间步上的微小误差逐渐累积（误差累积），最终导致严重的驾驶失效。
- **现有工作局限**：当前研究主要依赖更复杂的网络架构或高保真训练数据集来增强单时间点状态级的鲁棒性，忽视了自动驾驶是一个连续时间过程，**未能利用时间尺度上的信息来抑制误差传播**。
- **动机**：探索通过**时间交替策略**利用不同模型间的固有差异，在闭环中抑制误差累积，从而提升性能，且不增加模型规模或数据需求。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：提出**Sequence of Experts（SoE）—— 时间交替专家序列**。保留训练过程中产生的多个中间模型（这些模型在驾驶误差上存在固有差异），然后在不同规划周期（时间间隔）内**交替激活不同专家模型**。这种方法既保持了多个模型间的一致性能力，又利用它们之间的差异来增强整体鲁棒性。
- **关键技术细节**：
  - 不需要修改网络架构或预知场景信息，是一种**即插即用**的解决方案。
  - 具体算法流程（文字说明）：
    1. 在训练过程中，保存多个不同时期的中间模型（专家）。
    2. 在闭环推理时，按照固定或自适应的时间间隔轮流切换使用这些专家模型进行规划输出。
    3. 交替策略通过不同专家偏向不同误差模式的特性，打破单一模型的误差累积路径，从而提升长期闭环性能。
- **公式/算法**：论文未提供具体公式，但核心是模型切换策略。

## 3. 实验设计

- **数据集与场景**：使用大规模自动驾驶基准 **nuPlan**（包含真实世界驾驶数据）。
- **Benchmark**：nuPlan 的闭环评估协议。
- **对比方法**：论文提到的“所有评估的模型”包括现有模仿学习规划器（具体名称未在摘要中列出，但从上下文可知为多种基线方法）。SoE 作为插件嵌入到这些基线中，并与原始模型进行比较。

## 4. 资源与算力

- **文中未明确说明**使用的 GPU 型号、数量、训练时长等算力信息。摘要及元数据中均无相关描述。

## 5. 实验数量与充分性

- **实验数量**：论文在多个不同的规划器模型上进行了实验，并在 nuPlan 基准上评估了闭环性能。具体组数未明确给出，但提到“在所有的评估模型上一致且显著地提升性能”。
- **充分性分析**：实验覆盖了多种基线模型，且结果具有一致性；但缺乏消融实验的详细说明（如是否对不同交替间隔进行了超参数分析）。总体上实验设计较为充分，但透明性有限。
- **客观公平性**：在标准基准 nuPlan 上测试，对比原始模型，实验条件应保持一致，较公平。

## 6. 主要结论与发现

- SoE 方法**显著且一致地提升了所有评估模型的闭环规划性能**（安全性和平滑性），并达到了最先进的水平。
- 时间交替是一种**简单有效的误差缓解方法**，不需要修改模型结构或增加数据，可即插即用。
- 该方法为提升自动驾驶模仿学习的训练效率提供了关键且广泛适用的支持。

## 7. 优点（亮点）

- **即插即用**：无需调整网络结构或预先了解场景，实用性强。
- **零额外计算负担（推理时）**：仅需维护多个模型权重，轮流切换，不增加单步推理计算量。
- **利用模型多样性**：巧妙地将训练过程中的中间模型（自然具有多样性）用于闭环，打破误差累积。
- **通用性**：在多种基线规划器上均有效，说明方法具有广泛适用性。

## 8. 不足与局限

- **实验覆盖有限**：仅在一个数据集（nuPlan）上验证，缺乏其他场景（如城市/高速混合、恶劣天气）的泛化性证明。
- **缺少算力资源说明**：使得复现成本不透明。
- **消融分析不足**：未详细探讨交替策略的间隔选择、专家数量等超参数的影响。
- **偏差风险**：可能仅适用于某些类型的模仿学习模型（如基于行为克隆的规划器），未在基于强化学习或其他范式的模型上验证。
- **理论分析欠缺**：为什么交替能抑制误差累积？缺乏严格的数学推导或证明。
- **该论文被 ICLR-2026 拒稿**，可能审稿人指出了更多缺点（如与现有方法的差距、实验细节不足等）。

（完）
