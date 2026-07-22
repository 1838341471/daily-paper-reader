---
title: "DriveWorld-VLA: Unified Latent-Space World Modeling with Vision–Language–Action for Autonomous Driving"
title_zh: DriveWorld-VLA：面向自动驾驶的统一潜空间世界建模与视觉-语言-行动
authors: "Feiyang Jia, Lin Liu, Ziying Song, Caiyan Jia, Hangjun Ye, Xiaoshuai Hao, Long Chen"
date: 2026-04-30
pdf: "https://openreview.net/pdf/4d7c2b743fd3940159e57db8dbf92bc64d1dbdd8.pdf"
tags: ["query:av-pnc"]
score: 10.0
evidence: 端到端自动驾驶中统一潜空间世界建模与规划
tldr: 现有端到端自动驾驶方法未能有效统一未来场景演变与行动规划，限制了视觉想象力对决策的影响。本文提出DriveWorld-VLA框架，通过在潜空间深度整合视觉-语言-动作与世界模型，让规划器直接利用整体场景演变建模，提升决策与前瞻能力。实验证明该方法增强了自动驾驶在复杂场景下的行为合理性和安全性，推动了统一架构下的端到端自动驾驶发展。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有端到端自动驾驶方法无法有效统一场景演变与行动规划，限制了决策的提升。
method: 提出DriveWorld-VLA框架，在潜空间紧密整合VLA与世界模型，共享表示。
result: 实验表明该方法能增强复杂场景下的决策合理性与安全性。
conclusion: 为统一架构下的端到端自动驾驶提供了新的范式。
---

## Abstract
End-to-end (E2E) autonomous driving has recently attracted increasing interest in unifying Vision–Language–Action (VLA) with World Models to enhance decision-making and forward-looking imagination. However, existing methods fail to effectively unify future scene evolution and action planning within a single architecture due to inadequate sharing of latent states, limiting the impact of visual imagination on action decisions. To address this limitation, we propose DriveWorld-VLA, a novel framework that unifies world modeling and planning within a latent space by tightly integrating VLA and world models at the representation level, which enables the VLA planner to benefit directly from holistic scene-evolution modeling and reducing reliance on dense annotated supervision. Additionally, DriveWorld-VLA incorporates the latent states of the world model as core decision-making states for the VLA planner, facilitating the planner to assess how candidate actions impact future scene evolution. By conducting world modeling entirely in the latent space, DriveWorld-VLA supports controllable, action-conditioned imagination at the feature level, avoiding expensive pixel-level rollouts. Extensive open-loop and closed-loop evaluations demonstrate the effectiveness of DriveWorld-VLA, which achieves state-of-the-art performance with 91.3 PDMS on NAVSIMv1, 86.8 EPDMS on NAVSIMv2, and 0.16 3-second average collision rate on nuScenes. Code and models are released at https://github.com/liulin815/DriveWorld-VLA.

---

## 论文详细总结（自动生成）

# DriveWorld-VLA 论文总结

## 1. 核心问题与整体含义

- **研究动机**：端到端自动驾驶正尝试统一视觉–语言–行动（VLA）与世界模型，以增强决策的前瞻性与想象能力。然而现有工作未能有效地将未来的场景演变与行动规划统一在单一架构中，原因在于潜状态共享不足，导致视觉想象对行动决策的支撑力有限。
- **整体含义**：论文提出在潜空间中深度整合世界建模与行动规划，使未来场景的演变直接服务于规划器决策，从而提升复杂场景下的行为合理性与安全性，推动统一架构的端到端自动驾驶范式发展。

## 2. 方法论

- **核心思想**：**在潜空间统一世界模型与规划**，通过表示层面的紧密耦合，让 VLA 规划器直接利用整体的场景演变建模，同时降低对稠密标注监督的依赖。
- **关键技术细节**：
  - 将世界模型的潜状态作为 VLA 规划器的**核心决策状态**，使规划器能够评估候选动作如何影响未来的场景演变。
  - **完全在潜空间进行世界建模**，支持特征级的、动作条件可控的想象力生成，避免昂贵的像素级滚动推演。
  - 统一的框架实现了 VLA 和世界模型的**表示级整合**，共享潜空间表示，而非简单的多模块拼接。
- **公式或算法流程**：摘要未给出具体公式，但可概括为：输入传感器数据 → 编码到统一潜空间 → 潜状态同时用于世界模型（预测未来潜状态）和 VLA 规划器（输出驾驶动作），其中世界模型的演变结果反哺给规划器作为决策依据。

## 3. 实验设计

- **数据集与场景**：使用 `NAVSIMv1`、`NAVSIMv2` 和 `nuScenes` 数据集，覆盖自动驾驶的开环与闭环评测场景。
- **Benchmark 指标**：
  - NAVSIMv1: **PDMS**（Planning Distance Mean Score，得分 91.3）
  - NAVSIMv2: **EPDMS**（Extended PDMS，得分 86.8）
  - nuScenes: **3 秒平均碰撞率**（得分 0.16）
- **对比方法**：摘要未列出具体对比对象，但明确表明达到 state-of-the-art 性能，可推测与当前主流的端到端驾驶模型（如 UniAD、VAD 等）或世界模型方法进行了比较。

## 4. 资源与算力

- 摘要和现有材料中**未提及**训练所用的 GPU 型号、数量及训练时长。完整论文中可能包含这部分信息，但基于当前提供的文本无法确认。

## 5. 实验数量与充分性

- **实验覆盖**：摘要明确指出进行了 **open-loop 和 closed-loop** 评估，并在 **三个不同 benchmark** 上报告了结果，说明实验设计考虑了多维度验证。
- **消融实验**：摘要未提及 ablation study，但从方法论创新性推断，完整论文极有可能包含对潜状态共享、动作条件想象等模块的消融分析，然当前材料无法确认。
- **公平性与客观性**：由于未提供对比方法的详细信息，难以判断实验的横向公平性。但三个公开数据集的使用和主流指标的报告倾向表明具备较高的客观性。

## 6. 主要结论与发现

- 提出的 **DriveWorld-VLA** 框架成功在统一潜空间内整合 VLA 与世界模型，使规划器能够直接利用未来场景演变信息。
- 该方法在多个 benchmark 上取得 **领先性能**，尤其在碰撞率指标上表现优异，显著增强了复杂场景下的决策合理性与安全性。
- 证明了**潜空间世界建模**与规划深度融合的有效性，为端到端自动驾驶提供了新的设计范式。

## 7. 优点

- **架构创新**：首次在表示层深度统一 VLA 与世界模型，超越简单的级联或后处理融合。
- **效率与有效性权衡**：在潜空间进行想象和演变建模，规避像素级重建的开销，同时保持对决策的强支撑。
- **降低标注依赖**：通过世界模型自监督学习，减少对稠密人工标注的依赖，提升实用性。
- **可控想象力**：支持动作条件下的特征级未来演变，赋予规划器“假设推演”能力。

## 8. 不足与局限

- **细节缺失**：由于只提供了摘要，完整模型结构、训练损失、消融设计、超参数等关键方法论和实验细节未知，无法全面评估其可靠性与复现性。
- **数据集与场景覆盖**：虽然使用了三个评价基准，但它们均来自相似的自动驾驶场景，对极端天气、异常事件、跨域泛化能力的验证可能不足。
- **计算成本未知**：缺乏算力消耗和推理延时的数据，影响对实际部署可行性的判断。
- **对比基线缺失**：摘要未列出对比方法，难以评判性能提升的绝对幅度及其相对优势的显著性。
- **多靠视觉想象力**：潜空间世界模型的准确性高度依赖表征学习质量，存在长时演变误差累积的风险，可能影响最终决策的安全性。

（完）
