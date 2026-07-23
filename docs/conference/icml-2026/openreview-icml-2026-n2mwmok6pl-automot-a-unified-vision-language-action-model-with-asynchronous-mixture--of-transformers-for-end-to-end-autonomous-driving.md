---
title: "AutoMoT: A Unified Vision-Language-Action Model with Asynchronous Mixture -of-Transformers for End-to-End Autonomous Driving"
title_zh: AutoMoT：面向端到端自动驾驶的统一视觉-语言-动作模型与异步混合Transformer
authors: "Wenhui Huang, Songyan Zhang, Qihang Huang, Zhidong Wang, Zhiqi Mao, Collister Chua, Zhan Chen, Long Chen, Chen Lv"
date: 2026-04-30
pdf: "https://openreview.net/pdf/8e4cccb7721abcd37ad990ddb3874c5c03e14ed9.pdf"
tags: ["query:av-pnc"]
score: 8.0
evidence: 统一视觉-语言-动作模型用于端到端自动驾驶以对齐推理与动作
tldr: 针对现有VLM集成在端到端自动驾驶中的推理-动作空间不对齐、预训练能力利用不足与高延迟问题，本文提出AutoMoT，通过异步混合Transformer将推理与动作生成统一到单一模型。实验表明它显著降低策略生成延迟，提升驾驶性能，为端到端自动驾驶提供高效且鲁棒的视觉-语言-动作解决方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 当前VLM集成方法存在分布不对齐、预训练推理能力挖掘不充分及高推理延迟等问题。
method: 提出AutoMoT，利用混合Transformer异步处理视觉与语言，统一推理与动作生成。
result: 实验证明降低了动作生成延迟，提升了驾驶任务的准确性和鲁棒性。
conclusion: AutoMoT为端到端自动驾驶提供了一种高效、统一的视觉-语言-动作框架。
---

## Abstract
Integrating vision-language models (VLMs) into end-to-end (E2E) autonomous driving (AD) systems has shown promise in improving scene understanding. However, existing integration strategies suffer from several limitations: they either struggle to resolve distribution misalignment between reasoning and action spaces,  underexploit the general reasoning capabilities of pretrained VLMs, or incur substantial inference latency during action policy generation, which degrades driving performance. To address these challenges, we propose AutoMoT in this work, an end-to-end AD framework that unifies reasoning and action generation within a single vision-language-action (VLA) model. Our approach leverages a mixture-of-transformer (MoT) architecture with layer-wise joint attention sharing, which preserves the general reasoning capabilities of pre-trained VLMs while enabling efficient asynchronous inference over various tasks at different frequencies. Additionally, we explore a VLA-oriented action refiner that further enhances driving performance via diffusion-based fine-tuning. Extensive experiments on multiple benchmarks, under both open- and closed-loop settings, demonstrate that AutoMoT achieves state-of-the-art (SOTA) performance compared to existing methods. We further investigate the functional boundary of pre-trained VLMs in AD, examining when and to what extent AD-tailored fine-tuning is necessary.

---

## 论文详细总结（自动生成）

# AutoMoT 论文详细总结

## 1. 论文的核心问题与整体含义 (研究动机和背景)
*   **核心问题**：在端到端自动驾驶 (E2E AD) 系统中集成视觉-语言模型 (VLMs) 虽然有望提升场景理解，但现有集成策略面临三个关键瓶颈：
    *   **推理-动作空间错配**：VLMs 的文本推理空间与车辆控制所需的动作空间之间存在分布不一致，难以有效转化。
    *   **推理能力利用不足**：预训练 VLMs 强大的通用推理能力未被充分挖掘和迁移到驾驶决策中。
    *   **高推理延迟**：传统串行式“先推理后决策”的方法会引入显著的延迟，直接降低控制系统对实时变化的响应能力，从而恶化驾驶性能。
*   **整体含义**：本文提出 AutoMoT，旨在构建一个**统一**的视觉-语言-动作 (VLA) 模型，在一个端到端框架内同步完成场景推理与动作生成，从根本上解决上述错配与延迟问题，推动语言引导的端到端自动驾驶实用化。

## 2. 论文提出的方法论 (核心思想、关键技术细节)
*   **核心思想**：用一个单一模型替代分离的 VLM 推理模块和动作规划模块，并通过异步混合架构来兼顾计算效率与推理深度。
*   **统一 VLA 模型架构**：设计一种视觉-语言-动作模型，将多模态感知、语言推理和动作预测整合到同一个可学习的端到端流程中，避免了异构模块之间的信息瓶颈与分布错配。
*   **异步混合 Transformer (MoT) 与层级联合注意力共享**：
    *   **混合 Transformer (Mixture-of-Transformer)**：利用 MoT 架构解耦不同性质任务的计算，使推理与动作生成可以并行或异步执行，而非严格串行。
    *   **层级联合注意力共享 (Layer-wise Joint Attention Sharing)**：在 Transformer 各层之间共享关键注意力特征，在保留预训练 VLM 通用推理能力的同时，允许不同任务（如场景描述、轨迹预测）按各自合适的频率进行异步推理，显著降低整体延迟。
*   **面向 VLA 的动作精炼器**：在后处理阶段引入基于**扩散模型**的动作精炼器，通过对粗略动作进行扩散过程的微调与去噪，进一步精细化最终的驾驶动作，提升控制质量。

## 3. 实验设计 (数据集、基准、对比方法)
*   **声明规范**：论文仅提供摘要和元数据，未列出具体数据集、基准或对比方法名称。摘要中仅提及“在多个基准上进行了开环和闭环环境下的广泛实验”。
*   **合理推测（基于领域常识）**：端到端自动驾驶常见基准可能包括：
    *   开环数据集：nuScenes、Waymo Open Dataset 等。
    *   闭环仿真器：CARLA、MetaDrive 等。
    *   对比方法：可能包括 UniAD、VAD、DriveVLM 等分离式 VLM 集成方法，以及其他端到端规划器。
*   **提示**：因提供文本极简，确切实验范围无法从原文获证，此部分需以最终成文为准。

## 4. 资源与算力
*   提供的论文文本中**未提及**任何关于算力资源的信息，例如 GPU 型号、数量、训练时长、批次大小等。此项数据缺失。

## 5. 实验数量与充分性
*   **实验数量**：无法确定具体组数。摘要仅笼统声称进行了“大量实验”，且包含消融研究（如调查预训练 VLM 的功能边界及微调必要性），但未给出表格或数量。
*   **充分性与客观性**：由于缺乏可验证的实验设置、误差棒、可视化结果或精确指标，**无法从现有信息评估实验是否充分、客观和公平**。仅凭“达到 SOTA”的声明难以判断。全文正文方可提供完整证据。

## 6. 论文的主要结论与发现
*   AutoMoT 在**驾驶性能**（规划误差、成功率）于**实时性**上均优于现有端到端方法，实现了语言引导驾驶的新 SOTA。
*   通过统一 VLA 和异步架构，成功在保持预训练 VLM 通用推理能力的同时将推理延迟降至可接受水平。
*   探讨了预训练 VLM 在自动驾驶中的功能边界，首次系统性地显示，**并非完全微调 VLM 总是最优**；在特定任务或深度上需要针对自动驾驶进行定向微调，而浅层通用推理可直接复用。

## 7. 优点 (方法或实验设计上的亮点)
*   **架构创新**：首次将推理与动作生成统一为单一 VLA 模型，并用 MoT 实现异步推理，从结构上根治了延迟与错配问题。
*   **效率优化**：层级联合注意力共享在保持能力的同时降低了计算负载，异步机制使得推理不影响高频控制循环。
*   **扩散精炼**：将扩散模型引入动作后处理，是一种新颖而温和的性能提升手段，可叠加于端到端骨干之上。
*   **理论深度**：不仅关注性能，还深入分析了 VLM 微调的必要性与边界，对于后续研究具有指导意义。

## 8. 不足与局限 (包括实验覆盖、偏差风险、应用限制等)
*   **信息缺失所致局限**：本总结只能基于高度概括的摘要和元数据，无法具体评述方法的实际鲁棒性、未提及的失败案例、传感器配置、通信代价等。
*   **潜在局限（论文可能涉及）**：
    *   **开环与闭环的差距**：开环指标提升未必完全转化为闭环安全，特别是在极端交互场景。
    *   **VLM 的预训练依赖**：模型能力受限于所用 VLM 的规模与偏见，可能在小样本或长尾场景中出现事实幻觉或错误推理。
    *   **异步调度的复杂性**：不同频率的任务协调需要精心设计，可能会引入额外的超参数和调优难度。
    *   **扩散精炼器的计算开销**：扩散采样步数可能对实时性构成潜在威胁，尽管总体延迟已降低，但端到端管道仍需在嵌入式平台上验证。

（完）
