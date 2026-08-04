---
title: "FunPhase: A Periodic Functional Autoencoder for Motion Generation via Phase Manifolds"
title_zh: FunPhase：基于相位流形的周期性函数自编码器用于运动生成
authors: "Marco Pegoraro, Evan Atherton, Bruno Roy, Aliasghar Khani, Arianna Rampini"
date: 2026-04-30
pdf: "https://openreview.net/pdf/234ff91a4c02dcfb1fb5a0321e0736de6888cb07.pdf"
tags: ["query:traj-pred"]
score: 8.0
evidence: 基于相位流形的运动生成与预测统一框架，支持任意时间分辨率平滑轨迹
tldr: 人体运动生成受空间几何与时间动力学强耦合的限制，现有相位流形方法多绑定固定骨架和窄分布。本文提出FunPhase，将周期相位流形嵌入函数空间，用函数域解码取代离散时间解码，从而支持任意时间分辨率采样平滑轨迹。FunPhase在统一的可解释相位流形中同时完成运动预测与生成。实验验证了其在多样运动分布上的泛化能力，为运动表征与生成提供新范式。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有运动生成受固定骨架与窄分布限制，难以处理空间时间耦合。
method: 提出功能周期自编码器FunPhase，学习相位流形，用函数空间解码控制运动轨迹。
result: 在统一的相位流形中实现运动预测与生成，并支持任意时间分辨率采样。
conclusion: 函数空间的相位流形为自然运动建模提供了灵活的统一框架。
---

## Abstract
Learning natural body motion remains challenging due to the strong coupling between spatial geometry and temporal dynamics.
Embedding motion in phase manifolds, latent spaces that capture local periodicity, has proven effective for motion prediction; however, existing approaches are tied to fixed skeletons and narrow motion distributions, limiting their applicability across diverse settings.
We introduce FunPhase, a functional periodic autoencoder that learns a phase manifold for motion and replaces discrete temporal decoding with a function-space formulation, enabling smooth trajectories that can be sampled at arbitrary temporal resolutions.
FunPhase unifies motion prediction and generation within a single interpretable phase manifold, enabling motion generation via latent diffusion, generalizes across skeletons and datasets, and supports downstream tasks such as motion super-resolution and partial-body completion.
Our model achieves substantially lower reconstruction error than prior periodic autoencoder baselines, achieving uniform improvements of at least 45% across all metrics, while enabling a broader range of applications and performing on par with state-of-the-art motion generation methods.

---

## 论文详细总结（自动生成）

# 中文总结：FunPhase

## 1. 论文的核心问题与整体含义

- **研究动机**：人体运动建模的核心难点在于空间几何与时间动力学的强耦合。传统方法难以同时捕捉运动的空间结构（如骨骼姿态）与时间节奏（如周期性的步态、手势）。
- **现有方法的局限**：已有的将运动嵌入“相位流形”（phase manifold）的方法虽能捕捉局部周期性，但通常**绑定固定骨架**、仅适用于**窄分布的运动数据**，难以推广到多样化的骨骼结构和多数据集场景。
- **整体意义**：本文提出 FunPhase，通过将周期性相位流形嵌入函数空间，统一运动预测与生成，并支持任意时间分辨率采样，为运动表征与生成提供了一种更灵活、通用的新范式。

## 2. 论文提出的方法论

- **核心思想**：利用**函数式周期性自编码器**学习一个可解释的相位流形，用函数空间中的解码替代传统的离散时间解码。
- **关键技术细节**：
  - 相位流形：用于捕获运动序列中的局部周期性结构，使运动表征更具解释性。
  - 函数空间解码：不再在固定时间步上输出离散姿态，而是学习一个连续时间函数，从而可以**以任意时间分辨率**生成平滑轨迹。
  - 统一框架：将运动预测与生成放在同一相位流形中，通过**潜在扩散模型（latent diffusion）**实现运动生成。
- **算法流程（文字说明）**：
  1. 输入运动序列 → 编码器映射到相位流形上的潜变量；
  2. 潜变量通过函数解码器生成连续运动函数；
  3. 根据需求在任意时间点采样，得到平滑姿态序列；
  4. 对于生成任务，在潜空间上运行扩散模型采样，再解码为运动。
- **额外能力**：支持运动超分辨率（motion super-resolution）、部分身体完成（partial-body completion）等下游任务。

## 3. 实验设计

- **数据集/场景**：由于原文摘要未列出具体数据集名称，但从“跨骨架、跨数据集泛化”的描述推断，应涉及**多种不同骨架定义的运动数据集**（如 HumanML3D、AMASS、BABEL 或类似常见基准），并用于**运动预测、运动生成、超分辨率、部分补全**等任务。
- **Benchmark**：以“周期性自编码器”为基线，并与现有最先进的运动生成方法进行对比。
- **对比方法**：
  - 周期性自编码器基线（prior periodic autoencoder baselines）；
  - 当前最先进的运动生成方法（state-of-the-art motion generation methods）。

## 4. 资源与算力

- 原文摘要中**未明确提及**使用的 GPU 型号、数量、训练时长等算力信息。
- 仅能确认实验涉及较复杂的模型训练与多个下游任务评估，但无法量化资源消耗。

## 5. 实验数量与充分性

- 实验范围较广：至少覆盖了**重建精度对比、运动生成质量对比、跨骨架/跨数据集泛化、运动超分辨率、部分身体完成**等多类实验。
- 充分性评价：
  - **积极方面**：实验设计覆盖了模型的多个能力维度，且与两类基线（周期性自编码器与最新生成方法）进行对比，能较好展示方法的优势。
  - **客观性存疑**：摘要仅给出“至少45%的指标统一提升”这一突出结果，但未提供具体数值、可视化结果或用户研究；也未说明消融实验（例如相位流形维度、函数解码器结构的影响）是否开展。
  - 对于跨数据集泛化，未提及是否在完全未见过的骨骼类型上进行评估，公平性细节不足。

## 6. 论文的主要结论与发现

- FunPhase 在重建误差上相比以往周期性自编码器基线获得**至少 45% 的全面改进**（所有指标均提升）。
- 在运动生成方面，与最先进方法相比**性能持平（on par）**，但额外支持更多应用场景（超分辨率、部分补全）。
- 结论：函数空间的相位流形为自然运动建模提供了灵活统一的框架，有效解决了固定骨架和窄分布限制。

## 7. 优点

- **统一性强**：一个框架同时支持预测、生成、超分辨率、部分补全，无需多个专用模型。
- **灵活采样**：函数空间解码实现了任意时间分辨率输出，优于离散时间解码。
- **可解释性**：相位流形本身具有物理可解释性（周期性），有助于理解运动结构。
- **泛化能力**：宣称可跨骨架、跨数据集使用，相比此前方法适用范围更广。
- **性能突出**：相比专门的周期性自编码器基线，重建性能大幅提升。

## 8. 不足与局限

- **信息缺失**：摘要未披露具体数据集、实验设置细节、消融实验和可视化结果，难以从现有文本完全评估实验严谨性。
- **对比公平性**：与“最先进的运动生成方法”对比时仅提到“性能持平”，未说明是否在相同骨架、相同数据集、相同评估协议下比较。
- **潜在偏差**：宣称的“至少45%改进”可能只针对特定基线集合，未必能泛化到所有周期性自编码器变体。
- **应用限制**：对于非周期性动作（如一次性复杂交互）可能不适用，相位流形的假设偏向周期运动；跨骨架泛化在极端骨架（如非人形）情况下可能失效。
- **算力未报告**：缺乏训练成本信息，不利于其他研究者复现或评估实际效率。

（完）
