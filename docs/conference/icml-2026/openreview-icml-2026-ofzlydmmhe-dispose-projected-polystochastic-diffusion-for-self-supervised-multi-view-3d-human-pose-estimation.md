---
title: "DisPOSE: Projected Polystochastic Diffusion for Self-Supervised Multi-View 3D Human Pose Estimation"
title_zh: DisPOSE：投影多随机扩散用于自监督多视角3D人体姿态估计
authors: "Tony Danjun Wang, Tolga Birdal, Nassir Navab, Lennart Bastian"
date: 2026-04-30
pdf: "https://openreview.net/pdf/e418774588dadff270a2304f25735c660c868590.pdf"
tags: ["query:traj-pred"]
score: 4.0
evidence: 生成扩散用于人体姿态估计，多视角分配与Sinkhorn投影
tldr: 该论文针对自监督多视角3D人体姿态估计中依赖合成目录导致真实场景泛化差的问题，提出DisPOSE框架。DisPOSE将多视角人员分配问题近似为多随机张量空间上的生成扩散过程，在去噪过程中使用可微Sinkhorn投影引导解向可行分配，并结合2D图像先验恢复完整3D骨架。实验表明，DisPOSE在公共真实数据集上的精度与泛化性均超过现有自监督方法，为多视角人体姿态估计提供了一种生成式解决路径。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 自监督多视角3D人体姿态估计依赖合成姿态目录，真实场景泛化能力不足。
method: 提出DisPOSE，将多视角人员分配近似为多随机张量上的生成扩散过程，并利用Sinkhorn投影约束。
result: 在真实场景数据上，DisPOSE的姿态估计精度和泛化性优于现有自监督方法。
conclusion: 生成式扩散赋能为多视角姿态估计提供了一种鲁棒的自监督解决方案。
---

## Abstract
Recovering 3D human poses for multiple individuals from different camera views is a fundamental bottleneck for analyzing interacting behaviors. Existing self-supervised approaches leverage synthetic catalogues of 3D poses; however, this leads to poor generalization in real-world scenarios due to distribution shifts. We therefore introduce DisPOSE, a self-supervised framework that approximates the inherently discrete multi-view person-assignment problem as a generative diffusion process over the space of polystochastic tensors. By employing differentiable Sinkhorn projections during denoising, our model learns to guide solutions toward valid and feasible assignments based on 2D image priors. The complete 3D skeletons of localized individuals are then regressed using a Hypergraph-Convolutional Decoder that explicitly models relational structures and articulated joints across multiple views. The proposed approach outperforms current state-of-the-art self-supervised methods on standard datasets and demonstrates strong performance on a newly proposed benchmark featuring highly occluded scenes from surgical operating rooms. Our diffusion-based localization demonstrates high label efficiency, retaining 99\% of its performance with only 10\% of the pseudo-labels. Notably, disentangling the assignment and root regression components while maintaining differentiability makes DisPOSE nearly agnostic to different camera arrangements.

---

## 论文详细总结（自动生成）

# DisPOSE：投影多随机扩散用于自监督多视角3D人体姿态估计 —— 论文总结

## 1. 论文的核心问题与整体含义

- **研究背景**：从多个摄像机视角恢复多个个体的3D人体姿态，是分析人际交互行为的核心瓶颈，在医疗手术室监控、人机交互、运动分析等场景中具有重要应用价值。
- **核心问题**：现有自监督方法严重依赖**合成3D姿态目录**（synthetic catalogues of 3D poses）作为先验，导致在真实场景中因**分布偏移**（distribution shift）而泛化能力严重不足。
- **整体含义**：本文旨在摆脱对合成数据的依赖，提出一种**完全自监督、无需标注**的多视角3D人体姿态估计框架，能够在真实世界中（尤其是高度遮挡场景下）准确恢复多人姿态，并且对相机布局具有鲁棒性。

## 2. 论文提出的方法论

### 核心思想
- 将多视角人员分配问题——一个本质上**离散的组合优化问题**——重新表述为**多随机张量空间上的生成扩散过程**（generative diffusion process over polystochastic tensors）。
- 利用扩散模型的生成能力，在去噪过程中逐步引导解走向**可行且有效的分配**，从而将2D图像先验自然地融入分配求解。

### 关键技术细节

1. **多随机张量表达**：将多视角之间的对应关系表示为多随机张量（polystochastic tensor），将离散分配问题连续化，便于梯度传播和生成式建模。

2. **可微Sinkhorn投影**：在去噪过程中的每一步，使用**可微的Sinkhorn投影**（differentiable Sinkhorn projections）将扩散模型的中间输出约束/引导至满足有效分配条件的解空间，保证生成结果在数学上是合法的多视角匹配。

3. **生成扩散流程**：
   - 前向过程：向真实的分配张量逐步添加噪声。
   - 反向去噪：训练模型从噪声中逐步恢复分配张量，同时以2D图像特征为先验条件（conditioning），在每一步通过Sinkhorn投影维持解的可行性。

4. **超图卷积解码器**（Hypergraph-Convolutional Decoder）：
   - 在完成人员分配后，使用Hypergraph-Convolutional Decoder回归完整3D骨架。
   - 该解码器显式建模**跨视角的关系结构**和**关节间的运动学连接**，从而在聚合多视角信息时保持几何一致性。

5. **模块解耦设计**：将**分配（assignment）**与**根节点回归（root regression）**解耦，同时保持整体流程可微，使得方法几乎不受相机布局变化的影响。

## 3. 实验设计

### 数据集与场景
- **标准公开数据集**：用于与现有SOTA方法进行公平对比。
- **新提出的基准**：构建了一个包含**手术室高遮挡场景**的新基准数据集，用于测试方法在极端遮挡条件下的实际应用能力。

### 对比方法
- 与当前**最先进的自监督方法**（state-of-the-art self-supervised methods）进行对比。
- 论文未具体列出对比方法名称，但从上下文可推断涵盖主流自监督多视角姿态估计方法。

### 评价指标
- 姿态估计精度（3D关键点误差等标准指标）。
- 泛化能力（跨场景、跨数据集的表现）。
- 标签效率（pseudo-label使用比例与性能保持率）。

## 4. 资源与算力

- **论文原文未明确说明**所使用的GPU型号、数量、训练时长等具体的算力资源配置。
- 仅在方法层面提到使用**可微Sinkhorn投影**和**Hypergraph-Convolutional Decoder**，这些模块的计算开销适中，但具体训练成本未披露。
- 这属于论文报告中的信息缺失，读者无法直接复现训练的硬件需求。

## 5. 实验数量与充分性

### 实验组数
根据摘要和元数据可知的实验包括：
- 在标准数据集上的性能对比实验。
- 在新提出的手术室高遮挡基准上的验证实验。
- 标签效率实验（使用10%伪标签仍保留99%性能）。

### 充分性评估
- **优点**：实验覆盖了标准场景和极端遮挡场景两类环境，且包含标签效率分析，视角较全面。
- **不足**：
  - 论文摘要中未提及**消融实验**的具体情况（如Sinkhorn投影的作用、扩散过程必要性、超图解码器贡献等），元数据也未列出消融细节。
  - 未提及与其他方法的**定性可视化对比**。
  - 标准数据集上的对比是否涵盖足够多的基线方法不明确。
  - 总体上实验设计合理且针对性强，但完整性和透明度受限，需阅读全文才能全面评估公平性。

## 6. 论文的主要结论与发现

- DisPOSE在**标准公开数据集**上超越了现有最先进的自监督方法，在姿态估计精度上取得SOTA结果。
- 在**高度遮挡的手术室场景**中表现出强鲁棒性，证明其生成式分配策略能有效应对真实世界的分布偏移问题。
- **标签效率极高**：仅使用10%的伪标签即可保留99%的性能，显著降低了自监督方法对大量伪标签的依赖。
- **相机布局无关性**：通过解耦分配与根节点回归并保持可微性，DisPOSE对不同的相机排列方式几乎不敏感，具备很强的实际部署灵活性。

## 7. 优点

- **问题建模新颖**：将离散分配问题转化为连续的多随机张量上的生成扩散过程，是姿态估计领域的一种新范式。
- **自监督且泛化性强**：不依赖合成姿态目录，从根本上规避了分布偏移问题，真实场景泛化能力显著提升。
- **数学保证与可微性兼具**：Sinkhorn投影在保证解可行性的同时保持全程可微，实现了生成模型与组合优化的优雅结合。
- **架构设计合理**：Hypergraph-Convolutional Decoder能显式建模多视角关节间的复杂关系，有效恢复3D骨架。
- **标签效率突出**：10%伪标签即保留99%性能，对实际应用中的数据成本控制意义重大。
- **相机无关性**：对相机布局的鲁棒性使得方法可迁移至多种部署环境。

## 8. 不足与局限

- **算力信息缺失**：未报告训练所需的GPU资源、时间等关键信息，影响可复现性和实际部署的可行性评估。
- **实验细节不透明**：摘要和元数据中未提供消融实验、基线方法具体列表、误差量化对比等细节，实验的全面性和公平性难以从现有信息中完整判断。
- **新基准的地域局限性**：新提出的手术室基准来自特定手术场景，虽然具有实际意义，但其普遍适用性有待更多领域验证。
- **方法复杂度**：生成扩散+多随机张量+Sinkhorn投影+超图卷积的组合在工程实现上较为复杂，训练与推理的稳定性、收敛速度等未在提供信息中讨论。
- **已定位个体后的3D骨架回归**依赖Hypergraph-Convolutional Decoder，该模块在多视角特征融合时的具体鲁棒性（如相机数量变化、极端视角差异）未在摘要中充分说明。
- **潜在偏差风险**：如果伪标签本身存在系统性偏差，自监督训练可能继承这些偏差，论文未提及对此的分析或校正策略。

---

（完）
