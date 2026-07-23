---
title: "DeepSight: Long-Horizon World Modeling via Latent States Prediction for End-to-End Autonomous Driving"
title_zh: DeepSight：通过潜在状态预测实现长时域世界建模的端到端自动驾驶
authors: "Lingjun Zhang, Changjie Wu, Linzhe Shi, Jiangyang Li, Jiaxin Liu, Lei Yang, Hang Zhang, Mu Xu, Hong Wang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/48be22be2762cc64031302f430b73cab3cdbdf9d.pdf"
tags: ["query:av-pnc"]
score: 7.0
evidence: 预测潜在未来状态的驾驶世界模型，用于长时域自动驾驶
tldr: 针对自动驾驶中VLM架构的视觉推理模块缺乏场景定制问题，本文提出DeepSight驾驶世界模型，在鸟瞰图空间并行预测连续帧的潜在语义特征，实现长时域未来状态建模，并引入自适应文本推理。实验表明该模型能提升决策鲁棒性和准确性，为自动驾驶长时域规划提供更丰富的前瞻世界理解。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有端到端驾驶的VLM推理机制缺乏针对自动驾驶场景的深入探索，尤其视觉推理。
method: 提出DeepSight，在BEV空间预测未来帧的潜在语义特征，并采用自适应文本推理增强。
result: 实验显示长时域世界建模提升了驾驶决策的鲁棒性和准确性。
conclusion: DeepSight通过潜在状态预测增强了自动驾驶的世界理解与前瞻能力。
---

## Abstract
End-to-end autonomous driving systems are increasingly integrating Vision-Language Model (VLM) architectures, incorporating text reasoning or visual reasoning to enhance the robustness and accuracy of driving decisions.
However, the reasoning mechanisms employed in most methods are direct adaptations from general domains, lacking in-depth exploration tailored to autonomous driving scenarios, particularly within visual reasoning modules. In this paper, we propose a driving world model that performs parallel prediction of latent semantic features for consecutive future frames in the bird’s-eye-view (BEV) space, thereby enabling long-horizon modeling of future world states. We also introduce an efficient and adaptive text reasoning mechanism that utilizes additional social knowledge and reasoning capabilities to further improve driving performance in challenging long-tail scenarios. We present a novel, efficient, and effective approach that achieves state-of-the-art (SOTA) results on the closed-loop Bench2drive benchmark. Codes are available at: https://github.com/hotdogcheesewhite/DeepSight.

---

## 论文详细总结（自动生成）

好的，以下是根据提供的论文元数据与摘要内容，整理的结构化中文总结。

## 1. 论文的核心问题与整体含义

*   **核心问题**：当前端到端自动驾驶系统在融合视觉语言模型（VLM）时，其推理机制大多直接照搬通用领域的做法，缺乏针对自动驾驶场景的深度定制，尤其是在视觉推理模块上探索不足。
*   **整体含义**：本文旨在为端到端自动驾驶构建一个**专用的驾驶世界模型**，通过在鸟瞰视图空间中预测未来帧的潜在语义特征，实现长时域的状态建模；同时引入高效的自适应文本推理，以进一步提升在复杂长尾场景下的决策性能。

## 2. 论文提出的方法论

*   **核心思想**：构建一个能在 **鸟瞰视图（BEV）空间**中对未来连续帧的潜在语义特征进行并行预测的世界模型，使模型能“预见”未来世界状态，从而为决策提供更长期的上下文。
*   **关键技术细节**：
    *   **驾驶世界模型（DeepSight）**：在 BEV 空间中，对连续未来帧执行潜在语义特征的并行预测，专门针对驾驶场景进行视觉推理建模。
    *   **长时域状态预测**：不直接预测原始像素或显式目标轨迹，而是预测抽象的潜在特征，从而支持对未来世界状态的长期、稳定建模。
    *   **自适应文本推理机制**：额外集成一个高效且自适应的文本推理模块，利用社会知识和常识推理能力，辅助模型处理具有挑战性的长尾场景。
*   **整体流程**：输入多模态感知信息 → BEV 特征提取 → 世界模型并行预测未来潜在状态 → 结合自适应文本推理 → 输出端到端规划决策。

## 3. 实验设计

*   **使用的数据集/场景**：在闭环驾驶基准 **Bench2drive** 上进行验证。该基准覆盖多种日常及挑战性驾驶场景，能够全面评估端到端方法的闭环性能。
*   **Benchmark**：以 Bench2drive 闭环评估指标作为主要衡量标准。
*   **对比方法**：与已有端到端自动驾驶方法进行对比（摘要未列出具体对比模型名称，但指出在 Bench2drive 上取得了 State‑of‑the‑art (SOTA) 结果）。

## 4. 资源与算力

*   提供的摘要和元数据中**未明确提及**训练所用的 GPU 型号、数量以及具体训练时长。该信息需要查阅正文和实验配置文件方可确认。

## 5. 实验数量与充分性

*   **实验组数**：摘要未给出具体实验组数，但根据常规 SOTA 论文推断，通常包含：
    *   主实验：与现有方法在 Bench2drive 基准上的性能对比。
    *   消融实验：移除世界模型或文本推理模块，以验证各组件贡献。
    *   定性分析：可能包含长时域规划的可视化或长尾场景案例。
*   **充分性与公平性评价**：由于在业内认可的闭环基准上实现 SOTA，且公开了代码，可以认为实验具备一定说服力。闭环评估本身较开环更具挑战和现实意义，整体实验设计为证明方法的有效性提供了支撑。但消融实验的具体细节与统计检验需查阅原文。

## 6. 论文的主要结论与发现

*   DeepSight 提出的专用驾驶世界模型，能够有效对 BEV 空间下的未来潜在状态进行长时域建模。
*   将长时域视觉预测与自适应文本推理相结合，可显著提升端到端自动驾驶规划的性能与鲁棒性。
*   方法在 Bench2drive 闭环基准上取得了当前最优（SOTA）结果，证明了其技术路径的有效性。

## 7. 优点

*   **针对性强**：一改通用推理的简单移植，专门为驾驶场景设计视觉世界模型，解决了领域适配不足的问题。
*   **建模方式创新**：直接在 BEV 空间预测潜在语义特征，而非传统像素或框轨迹，兼顾效率与长期推理能力。
*   **架构互补**：视觉世界模型与自适应文本推理机制形成互补，兼顾场景预测与社会常识推理。
*   **验证充分且公开**：在权威闭环基准上取得 SOTA 并提供代码，增强了工作的可信度和可复现性。

## 8. 不足与局限

*   **信息不全**：由于仅凭摘要与元数据进行总结，论文的详细实验设计、消融结果对比、超参数敏感性、计算开销细节、失败案例等关键信息均未获知。
*   **长尾依赖**：自适应文本推理模块很可能依赖外部知识或大语言模型，其实时性与部署成本在真实车载环境中的可行性未经详细论证。
*   **泛化性**：仅在 Bench2drive 一个基准上进行 SOTA 声明，其对不同地域、天气或罕见交通场景的泛化能力仍有待验证。
*   **偏差风险**：世界模型的训练数据分布若存在偏差，可能导致预测的未来状态产生系统性错误，进而引发安全风险，该风险未在摘要中讨论。

（完）
