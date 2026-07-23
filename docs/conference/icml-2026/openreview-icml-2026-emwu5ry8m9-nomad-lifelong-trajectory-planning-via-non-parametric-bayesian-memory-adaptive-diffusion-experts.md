---
title: "NOMAD: Lifelong Trajectory Planning via Non-Parametric Bayesian Memory-Adaptive Diffusion Experts"
title_zh: NOMAD：基于非参数贝叶斯记忆自适应扩散专家的终身轨迹规划
authors: "Yixian Chen, Rufan Bai, Jiangbin Zheng, Yimin Wang, Tiantian CHEN, Wei Wang, Yuhuan Lu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/d1c1fb8aca1386b5f851fe8cd9d097c39695e998.pdf"
tags: ["query:av-pnc"]
score: 10.0
evidence: 利用非参数贝叶斯记忆与扩散模型的自动驾驶车辆终身轨迹规划
tldr: 针对自动驾驶车辆在开放世界中需持续适应稀有场景并保留已有技能的问题，本文提出NOMAD框架，结合非参数贝叶斯记忆与扩散模型动态生成轨迹，通过高斯过程专家不断扩展记忆，避免灾难性遗忘。实验证明该方法能有效应对复杂交通动态，提升终身学习能力，为自动驾驶持续适应提供新方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有轨迹规划方法无法在开放世界中持续适应长尾场景，且存在稳定性-可塑性权衡问题。
method: 提出NOMAD，集成非参数贝叶斯记忆与扩散轨迹生成，动态映射场景上下文至高斯过程专家。
result: 实验表明该方法能持续适应罕见场景，避免灾难性遗忘，保持规划性能。
conclusion: NOMAD为自动驾驶终身轨迹规划提供了一种平衡新旧技能的有效方案。
---

## Abstract
Autonomous vehicles operating in open-world environments must continually adapt to rare long-tail scenarios while preserving previously acquired driving skills. However, existing trajectory planning approaches struggle with this stability--plasticity trade-off, as they rely on static models or rigid rule-based controllers that cannot robustly handle evolving and complex traffic dynamics. Against this background, we propose **NOMAD**, a lifelong trajectory planning framework that integrates non-parametric Bayesian memory with diffusion-based trajectory generation, enabling continuous adaptation to long-tail scenarios without catastrophic forgetting. Our method maps growing scene contexts to a dynamically growing set of discrete memory clusters, which guide a conditional diffusion model to function as a mixture of experts specialized for diverse driving behaviors. To retain past knowledge during incremental learning, we introduce a generative replay mechanism that synthesizes pseudo-experiences from previously learned memory clusters. Extensive closed-loop evaluations on the nuPlan benchmark demonstrate that our approach achieves state-of-the-art performance on long-tail scenarios, improving the interPlan score by **9.4%** over the strongest baseline, while maintaining competitive performance on regular driving benchmarks. Moreover, our method exhibits robust continual learning capability, achieving the highest average closed-loop score with positive backward transfer when adapting to sequentially introduced long-tail scenarios.

---

## 论文详细总结（自动生成）

由于提供的论文 PDF 提取文本仅为 OpenReview 验证页面，未能获得全文内容，以下总结完全基于所提供的论文 Markdown 元数据（摘要、动机、方法、结果、结论等）进行提炼，可能缺失部分技术细节与实验数据。总结将严格依照要求展开。

## 1. 论文的核心问题与整体含义
- **核心问题**：自动驾驶车辆在开放世界环境中面临“终身学习”的挑战，即既要持续适应罕见的长尾场景（可塑性），又要保持已有的正常驾驶技能（稳定性）。现有方法（静态模型、固定规则控制器）难以在稳定性与可塑性之间取得平衡，无法稳健应对不断演化的复杂交通动态。
- **整体含义**：论文提出了一种面向终身轨迹规划的框架，通过结合非参数贝叶斯记忆与扩散模型，使得自动驾驶系统能够在不断遇到新场景时动态扩展知识，既学习新行为又不遗忘旧技能，从而提升长期安全性与适应性。

## 2. 论文提出的方法论
- **核心思想**：构建一个名为 **NOMAD** (Non‑parametric Bayesian Memory‑Adaptive Diffusion experts) 的框架。它利用非参数贝叶斯方法维护一个可动态增长的离散记忆簇，每个簇对应一种驾驶行为模式，并以此引导一个条件扩散模型，使其成为多个专家（mixture of experts）的集成。
- **关键技术细节**：
  - **非参数贝叶斯记忆**：将不断增长的场景上下文映射到一组可动态扩充的离散记忆簇，自动决定何时创建新簇以表示新出现的场景类型。
  - **扩散轨迹生成**：使用条件扩散模型生成轨迹，记忆簇作为条件输入，使模型针对不同驾驶行为（如不同场景簇）表现出专业化。
  - **增量学习与防遗忘**：引入生成式重放机制，从先前学习到的记忆簇中合成伪经验，在增量训练时回放，以保留过去的知识，抑制灾难性遗忘。
- **算法流程说明**：模型接收当前场景上下文，通过非参数贝叶斯推断分配到某个记忆簇（或创建新簇），然后以该簇的表示作为条件，通过扩散过程生成符合该场景类型的轨迹。在新场景学习时，模型扩展记忆簇并训练对应的扩散专家，同时回放伪样本防止对旧簇的遗忘。

## 3. 实验设计
- **数据集/场景**：基于 **nuPlan** 基准进行封闭循环评估，包含常规驾驶场景与长尾场景。
- **Benchmark**：主要评估指标为 **interPlan score**（来自 nuPlan 的综合评分），并考察封闭循环得分（closed‑loop score）以及向后迁移（backward transfer）指标。
- **对比方法**：文中提到“最强基线”（strongest baseline），但未从元数据中列出具体对比方法名称；可以推测对比了现有的静态模型或规则式控制器。

## 4. 资源与算力
- 所提供的元数据与摘要中 **未提及** GPU 型号、数量、训练时长等算力信息。因此无法从已有内容总结算力消耗。

## 5. 实验数量与充分性
- 摘要提及进行了 **广泛的封闭循环评估**，并且在持续学习能力方面设计了 **序列化引入长尾场景** 的实验，考察平均封闭循环得分和向后迁移。此外，据“result”部分提到，在长尾场景上相比最强基线 interPlan 分数提升 **9.4%**，同时还维持了常规场景的竞争性表现。
- 考虑到元数据有限，可推断至少包含以下实验组：
  - 与基线方法的总体性能对比；
  - 长尾场景专项评估；
  - 连续学习场景下的知识保持与迁移实验。
- 是否充分、客观、公平：因缺少详细实验设置、对比方法列表与统计检验信息，无法做出确凿判断，但从描述看实验设计覆盖了核心诉求。

## 6. 论文的主要结论与发现
- NOMAD 能有效实现终身轨迹规划，在长尾场景上取得了最先进的性能，相较最强基线 interPlan 得分提升 9.4%；
- 在常规驾驶基准上保持了具有竞争力的表现，未因适应长尾场景而牺牲基本能力；
- 在连续引入长尾场景的学习过程中，展现了稳健的持续学习能力，获得了最高的平均封闭循环得分和正向向后迁移，验证了方法能避免灾难性遗忘。

## 7. 优点
- **方法创新**：将非参数贝叶斯动态记忆与扩散生成模型有机融合，解决了终身学习中的稳定性‑可塑性困境。
- **记忆机制**：记忆簇的数量随场景动态增长，无需预先定义固定类别，具有自适应性和可扩展性。
- **防遗忘设计**：生成式重放为增量式持续学习提供了有效保障。
- **实验证据**：在公认的 nuPlan 基准上取得了可量化的显著提升，并验证了持续学习能力。

## 8. 不足与局限
- **信息缺失风险**：因未能获取完整论文，技术细节（如贝叶斯非参数模型的具体形式、扩散模型架构、训练策略、损失函数）、实验设置与对比方法的完整列表、算力消耗等均不明确，无法进行深入判断。
- **可能的应用限制**：动态扩充记忆簇可能在极长运行时间下面临记忆规模不断增长的问题，文中的生成式重放机制可能随着记忆量增大而增加计算成本；摘要未提及对此类扩展性的讨论。
- **对比公平性未知**：未看到与基于规则、基于学习或其它持续学习方法的详细比较，无法评估实验的全面性。
- **安全性验证**：封闭循环评估虽较真实，但nuPlan模拟与实际驾驶仍有差距，真实世界的鲁棒性有待验证。

（完）
