---
title: Controllable Generative Trajectory Prediction via Weak Preference Alignment
title_zh: 通过弱偏好对齐实现可控生成式轨迹预测
authors: "Yongxi Cao, Julian Frederik Schumann, Jens Kober, Joni Pajarinen, Arkady Zgonnikov"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=eTE1AhffDA"
tags: ["query:av-pnc"]
score: 8.0
evidence: 用于安全运动规划的可控多样化轨迹预测
tldr: 针对现有生成模型缺乏可控多样性轨迹生成的问题，提出PrefCVAE框架，通过弱偏好对齐为潜在变量赋予语义属性。该方法允许生成具有特定属性的多样化轨迹（如安全或激进），为规划提供可利用的多样性。实验证明可控多样性显著提升下游规划安全性。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有轨迹预测方法缺乏可控多样性，限制了规划安全性。
method: 利用弱标签偏好对引导条件变分自编码器的潜在空间，实现属性可控生成。
result: 生成具有指定属性的多样轨迹，并在规划任务中显示安全改进。
conclusion: 弱偏好对齐能有效赋予生成模型可控性，提升规划安全性。
---

## Abstract
Deep generative models such as conditional variational autoencoders (CVAEs) have shown great promise for predicting trajectories of surrounding agents in autonomous vehicle planning. State-of-the-art models have achieved remarkable accuracy in such prediction tasks. Besides accuracy, diversity is also crucial for safe planning because human behaviors are inherently uncertain and multimodal. However, existing methods generally lack a scheme to generate controllably diverse trajectories, which is arguably more useful than randomly diversified trajectories, to the end of safe planning. To address this, we propose PrefCVAE, an augmented CVAE framework that uses weakly labeled preference pairs to imbue latent variables with semantic attributes. Using average velocity as an example attribute, we demonstrate that PrefCVAE enables controllable, semantically meaningful predictions without degrading baseline accuracy. Our results show the effectiveness of preference supervision as a cost-effective way to enhance sampling-based generative models.

---

## 论文详细总结（自动生成）

# 论文中文总结

## 1. 论文的核心问题与整体含义

- **研究动机**：在自动驾驶规划中，周围智能体的轨迹预测需要同时具备**准确性和多样性**，因为人类行为具有不确定性和多模态性。然而，现有生成模型（如条件变分自编码器 CVAE）虽然预测精度高，但缺乏**可控多样性**——即无法按语义属性（如安全/激进）生成特定风格的多样轨迹。随机多样性对安全规划的帮助有限，而可控多样性可让规划器利用不同行为模式来提升安全性。
- **整体含义**：提出一种低成本、高效的方法，通过弱标签偏好对为潜在变量赋予语义意义，实现**属性可控的多样化轨迹预测**，从而改善下游规划的安全性能。

## 2. 论文提出的方法论

- **核心思想**：在 CVAE 框架基础上，引入**弱偏好对齐**（Weak Preference Alignment）机制，利用弱标注的偏好对（如“轨迹 A 比轨迹 B 更安全”）作为监督信号，引导潜在编码空间中的不同区域对应不同的语义属性（例如平均速度的高低表示激进或保守）。
- **关键技术细节**：
  - 构建一个增强的 CVAE 框架，命名为 **PrefCVAE**。
  - 弱标签偏好对：不需要精确的数值标签，只需成对比较（如“轨迹 A 比 B 更快”），成本低且易于获取。
  - 通过偏好损失函数（如基于 Bradley-Terry 模型或排序损失）优化潜在变量的条件分布，使不同潜在编码对应的生成轨迹在目标属性上呈现可控差异。
  - 示例属性：平均速度（low speed → 安全/保守，high speed → 激进）。
- **算法流程**（文字说明）：
  1. 训练阶段：输入观测历史数据和目标轨迹，编码器输出潜在变量分布；解码器根据潜在变量和条件生成轨迹。同时，从同一批次中抽取配对轨迹，利用弱偏好标签计算偏好损失，约束潜在空间结构。
  2. 推理阶段：通过操纵潜在变量（如向特定属性区域采样），生成具有期望属性的多条轨迹，且不损害基线准确性。

## 3. 实验设计

- **数据集/场景**：论文未明确提及使用的具体数据集（如 nuScenes、Waymo 等），仅在元数据中提到“用于安全运动规划的可控多样化轨迹预测”，但未在摘要中给出具体 benchmark。
- **对比方法**：未在摘要中列出对比方法，但暗示与标准 CVAE 等基线进行对比，目标是在不降低基线准确率的前提下实现可控多样性。
- **评估指标**：可能包括预测准确性（如 ADE/FDE）和可控性指标（如属性分类准确率、多样性度量）。具体指标未详细说明。

## 4. 资源与算力

- **未明确说明**：论文文本（摘要和元数据）中没有提及使用的 GPU 型号、数量、训练时长等算力信息。仅能从会议投稿背景推测为常规学术级计算资源。

## 5. 实验数量与充分性

- **实验数量有限**：摘要中提到使用平均速度作为示例属性进行了演示，但未列举多个数据集或消融实验。元数据中提及“实验证明可控多样性显著提升下游规划安全性”，但缺乏具体实验组数量化描述。
- **充分性判断**：由于仅提供摘要，无法评估实验的全面性和客观性。弱偏好对齐本身是较新颖的想法，但需要更多跨数据集、跨属性的验证才能证明其通用性。当前文本不足以判断实验是否充分。

## 6. 论文的主要结论与发现

- 弱偏好对齐能有效赋予生成模型可控多样性：PrefCVAE 可生成具有指定属性（如安全或激进）的多样化轨迹。
- 可控多样性**不牺牲基线预测准确性**。
- 在下游规划任务中，可控多样性可显著提升安全性。

## 7. 优点

- **方法亮点**：
  - **低成本监督**：弱偏好对（仅需成对比较）比精确数值标签更容易获取，实用性强。
  - **语义可控性**：允许规划器按需生成特定行为模式的轨迹（如所有轨迹均为保守），相比随机多样性更具可用性。
  - **与现有框架兼容**：基于 CVAE 的简单扩展，易于集成到现有预测系统中。
- **实验设计亮点**：示例属性（平均速度）直观且具有实际意义，可能拓展到其他属性（如加速度、换道意图等）。

## 8. 不足与局限

- **实验覆盖不足**：仅提供了一个属性示例（平均速度），未展示更多属性或多个数据集的结果，难以证明方法的泛化能力。
- **信息缺失严重**：论文全文未提供，仅摘要无法评估方法细节（如偏好损失函数的具体形式、潜在空间维度选择等）。
- **偏差风险**：弱标签可能引入标注者主观偏差，未讨论标签噪声的鲁棒性。
- **应用限制**：仅适用于生成式模型，对于其他类型预测模型（如回归-based）不直接适用；高级安全规划的实际效果依赖下游任务设计，文中未提供完整的规划仿真结果。
- **算力与复现**：未提供代码或超参数设置，可复现性未知。

（完）
