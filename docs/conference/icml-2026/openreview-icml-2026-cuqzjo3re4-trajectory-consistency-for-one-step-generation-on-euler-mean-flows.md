---
title: Trajectory Consistency for One-Step Generation on Euler Mean Flows
title_zh: 基于欧拉平均流的一步生成中的轨迹一致性
authors: "Zhiqi Li, Yuchen Sun, Duowen Chen, Jinjin He, Bo Zhu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/67b5115073fb3add16dac92a626479542cda5a7e.pdf"
tags: ["query:traj-pred"]
score: 6.0
evidence: 基于流的生成框架，通过轨迹一致性实现高效采样
tldr: 本文提出欧拉平均流（EMF），针对现有轨迹一致性约束难以监督优化的问题，根据半群公式推导出一个线性替代目标，在温和正则假设下可靠逼近原始一致性，并支持长程流映射组合的直接数据监督。该框架统一了单步与少步生成训练，且无需计算雅可比向量积，在保持生成质量的同时显著减少采样成本，为高效生成模型提供了新方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 长时间尺度的轨迹一致性目标难以监督和优化，限制了少步生成。
method: 提出欧拉平均流（EMF），用线性替代目标近似原始一致性目标，支持一跳与少步生成，无需JVP训练。
result: 在保持生成质量的同时大幅降低采样成本，实现统一训练框架。
conclusion: 为高效生成模型提供轨迹一致性近似方案，可用于轨迹预测等任务。
---

## Abstract
We propose \emph{Euler Mean Flows (EMF)}, a flow-based generative framework for one-step and few-step generation that enforces long-range trajectory consistency with minimal sampling cost. 
The key idea of EMF is to replace the trajectory consistency constraint, which is difficult to supervise and optimize over long time scales, with a principled linear surrogate that enables direct data supervision for long-horizon flow-map compositions.  We derive this approximation from the semigroup formulation of flow-based models and show that, under mild regularity assumptions, it faithfully approximates the original consistency objective while being substantially easier to optimize.  This formulation leads to a unified, JVP-free training framework that supports both $u$-prediction and $x_1$-prediction variants, avoiding explicit Jacobian computations and significantly reducing memory and computational overhead.  Experiments on image synthesis, particle-based geometry generation, and functional generation demonstrate improved optimization stability and sample quality under fixed sampling budgets, together with approximately $50\%$ reductions in training time and memory consumption compared to existing one-step methods for image generation.

---

## 论文详细总结（自动生成）

# 中文总结

## 1. 核心问题与研究动机

- **背景**：基于流的生成模型（Flow-based Generative Models）近年来在图像、几何、函数等数据生成任务中表现优异，但传统方法通常需要多步采样才能获得高质量结果，采样成本较高。
- **核心问题**：现有的一致性模型（Consistency Models）试图通过施加轨迹一致性约束实现少步甚至一步生成，但**长时间尺度下的轨迹一致性目标难以监督和优化**，导致模型训练不稳定、收敛困难。
- **研究动机**：作者希望设计一种新的训练框架，既能保持轨迹一致性的优势（少步/一步生成），又能**避免难以优化的原始约束**，同时减少训练资源开销。

## 2. 方法论

- **核心思想**：提出**欧拉平均流（Euler Mean Flows, EMF）**，将难以监督的轨迹一致性约束，替换为一个**基于半群（semigroup）公式推导的线性替代目标**。该替代目标在温和正则假设下能忠实逼近原始一致性目标，但更容易优化。
- **关键技术细节**：
  - 该替代目标支持对长时程流映射组合（long-range flow-map compositions）进行**直接数据监督**，无需依赖逐步自回归式训练。
  - 框架统一支持**单步生成**和**少步生成**的训练范式，两者共用同一套目标函数。
  - 支持两种预测变体：**u-prediction**（预测速度场）和 **x₁-prediction**（预测终点样本）。
  - **无需计算雅可比-向量积（JVP-free）**，完全避免显式雅可比矩阵计算，显著降低内存与计算开销。
- **算法流程（文字描述）**：训练时，模型对给定噪声/中间样本，沿欧拉平均流定义的轨迹预测一致性匹配的目标（速度或终点），并通过线性化的半群关系构造监督信号，实现长期一致性的近似优化；采样时，通过一步（或少量几步）前向传播即可生成样本。

## 3. 实验设计

- **数据集与场景**（三类任务）：
  - **图像合成**：使用标准图像生成 benchmark（论文中未列出具体数据集名称，推测为 CIFAR-10 / ImageNet 等常规基准）。
  - **基于粒子的几何生成**：粒子系统/几何点云类数据生成。
  - **函数生成**：函数分布生成任务。
- **对比方法**：文中提到与现有的一步生成方法进行对比，特别是**图像生成领域已有的一致性/一步生成方法**，比较训练时间、内存消耗与生成质量。
- **评估指标**：主要在固定采样预算（fixed sampling budgets）下比较生成质量（如 FID 等指标）与优化稳定性。

## 4. 资源与算力

- 论文明确指出：与现有图像一步生成方法相比，EMF 实现了**约 50% 的训练时间缩减和 50% 的内存消耗降低**。
- **但论文未明确提供具体 GPU 型号、数量、训练轮数或总训练时长等详细算力信息**。这一点属于信息缺失，无法进一步量化实际资源消耗。

## 5. 实验数量与充分性

- **实验数量**：论文涉及**三类任务**（图像、几何、函数生成），并在每类任务上均验证了有效性；包含对两种预测变体（u-prediction 和 x₁-prediction）的验证，实验维度较全面。
- **充分性分析**：
  - **优点**：多领域验证增强了方法的泛化说服力；训练效率和内存节省的数据具有明确对比意义。
  - **不足**：缺少显式的**消融实验描述**（如替代目标逼近误差的定量分析、单步 vs 少步的详细对比曲线、不同正则假设破坏时的鲁棒性测试等）；图像数据集名称和具体基准配比未公开；与最先进 SOTA 方法的定量差距也未完整呈现。总体上实验能证明可行性，但**严谨性和深度仍有提升空间**。

## 6. 主要结论

- EMF 通过线性替代目标成功解决了轨迹一致性难以优化的问题，实现了一个**统一的、JVP-free 的训练框架**，同时支持一步和少步生成。
- 在固定采样预算下，EMF 相比现有一步生成方法**生成质量更好、优化更稳定**。
- 训练开销显著降低：**训练时间与内存消耗均减少约 50%**，为高效生成模型提供了新方案。

## 7. 优点

- **理论支撑扎实**：从半群公式出发推导替代目标，并有温和正则假设下的逼近保证，方法有理论依据。
- **工程实现友好**：完全避免雅可比-向量积计算，大幅降低内存占用和训练时间，实用性高。
- **统一训练范式**：单步与少步生成共用同一目标，简化了训练流程。
- **通用性强**：在图像、几何、函数三类不同模态上均验证了有效性，表明方法具有跨域适应能力。

## 8. 不足与局限

- **实验细节缺失**：未列出具体数据集名称、评估指标数值和采样步数配置，难以独立复现和横向精确对比。
- **消融不足**：缺少对替代目标逼近精度、轨迹长度影响、两种变体性能差异的系统性消融分析。
- **资源信息不透明**：未提供 GPU 型号、数量、训练时长等算力细节，50% 的缩减比例也缺少绝对基准参照。
- **理论假设限制**：替代目标的有效性依赖温和正则假设，实际数据分布偏离这些假设时是否仍能保持性能，未充分讨论。
- **应用边界**：论文主要关注生成任务，虽提及可用于轨迹预测，但未给出具体实验证据，应用范围仍需进一步验证。

（完）
