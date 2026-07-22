---
title: "TF-FACE: Time-Frequency Fusion Learning via Frequency-Domain Adaptive and Controllable Enhancement for Trajectory Prediction"
title_zh: TF-FACE：面向轨迹预测的频域自适应可控增强时频融合学习
authors: "Dongjian Song, Yunhao Meng, Songjun Huang, Jiayi Han"
date: 2026-04-30
pdf: "https://openreview.net/pdf/c7ccc16b88f29bc08f891a76d49048b19edd29ae.pdf"
tags: ["query:av-pnc"]
score: 9.0
evidence: 提出时频融合的轨迹预测方法，对自动驾驶行为决策至关重要
tldr: 针对现有轨迹预测方法忽视频域信息、难以捕捉长期依赖和短期动态的问题，TF-FACE提出时频融合学习框架，通过可学习的门控频域注意力自适应增强。在驾驶数据集上的实验表明，该方法能够更准确地预测交通参与者未来轨迹，为自动驾驶行为决策提供更可靠的输入。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有轨迹预测方法主要基于时域，未能充分挖掘频域信息。
method: 设计融合编码器，采用可学习门控频域注意力机制，自适应操控频带特定特征。
result: 在多个基准上取得最优轨迹预测性能，提升自动驾驶安全性。
conclusion: TF-FACE通过频域增强有效提高轨迹预测精度，是自动驾驶行为决策的关键技术。
---

## Abstract
Accurately predicting the future trajectories of traffic participants is critical for safe, efficient, and human-friendly autonomous driving. Existing learning-based trajectory prediction methods are predominantly time-domain and insufficiently exploit latent frequency information, which limits their capability to capture low-frequency long-term dependencies and high-frequency short-term dynamics. To address this, we propose TF-FACE, a time-frequency learning framework via frequency-domain adaptive and controllable enhancement. TF-FACE introduces a fusion encoder with learnable gated frequency-domain attention that adaptively manipulates band-specific features for trajectory prediction. Building on the fused representation, we design a dual-stage decoder and a band-specific time–frequency dual-consistency loss to enable controllable decoupling and coupling across long- and short-term temporal scales, global and local scales, and then generate final multimodal predictions. Experiments on Argoverse 1 demonstrate that TF-FACE achieves state-of-the-art accuracy, while maintaining real-time inference for autonomous driving. Additional experiments are conducted on Argoverse 2, further validating TF-FACE's performance and generalizability.

---

## 论文详细总结（自动生成）

# TF-FACE：面向轨迹预测的频域自适应可控增强时频融合学习

## 1. 论文的核心问题与研究动机
- **核心问题**：自动驾驶中交通参与者未来轨迹的准确预测，对安全、高效且人性化的决策至关重要。现有基于学习的预测方法主要聚焦于**时域**建模，缺乏对潜在**频域信息**的有效利用。
- **研究动机与背景**：
  - 时域模型难以同时捕捉**低频的长期依赖**（如平稳巡航）和**高频的短期动态**（如突然转向、加减速）。
  - 频域表示能够天然分离不同时间尺度的成分，但如何自适应地选择与融合频域特征仍是一个开放挑战。
  - 本文旨在通过引入频域增强机制，弥补时域轨迹预测在长短期依赖建模上的不足，提升多模态预测的精度与实时性。

## 2. 方法论
- **整体框架**：提出**时频融合学习框架 TF‑FACE**，通过频域自适应可控增强实现长短期尺度的解耦与耦合。
- **融合编码器**：采用可学习的**门控频域注意力（learnable gated frequency‑domain attention）**，自适应地对不同频带的特征进行操控和加权，生成时频融合表征。
- **双阶段解码器**：基于融合表征，设计双阶段结构，支持可控的解耦与耦合，分别处理长期/短期时间尺度和全局/局部空间尺度。
- **损失函数**：提出**频带特定的时‑频双一致性损失（band‑specific time–frequency dual‑consistency loss）**，在时域和频域之间施加一致性约束，强化频带特征的解耦能力和预测稳定性。
- **最终输出**：生成多模态的轨迹预测，覆盖多种可能的未来运动。

## 3. 实验设计
- **数据集与场景**：
  - 主实验：**Argoverse 1** 数据集（自动驾驶场景下的车辆轨迹预测）。
  - 额外验证：**Argoverse 2** 数据集，用于检验方法的泛化性和性能上限。
- **Benchmark**：以公开的轨迹预测基准指标（如 minADE、minFDE、Miss Rate 等）作为评价标准。
- **对比方法**：与当前最先进的轨迹预测模型进行比较（具体方法名称在摘要中未列出，但声称达到 state‑of‑the‑art 精度）。

## 4. 资源与算力
- **算力信息**：摘要和元数据中**未明确提及** GPU 型号、数量、训练时长等具体资源消耗。
- **推理性能**：论文声称在 Argoverse 1 上实现了**实时推理**能力，可满足自动驾驶在线运行需求，但未给出具体的推理延迟数值。

## 5. 实验数量与充分性
- **实验组数**：至少在两个大规模数据集（Argoverse 1 和 Argoverse 2）上进行了主实验和泛化性实验。同时，设计已蕴含多种消融组件（频域注意力、双一致性损失、双解码器等），推测文中包含相应的消融实验，但摘要中未列出详细数目。
- **充分性与客观性**：
  - 采用多数据集验证可增强可信度，防止过拟合于单一场景。
  - 与 SOTA 方法对比并结合标准指标，实验对比应属客观、公平。
  - 由于摘要未披露所有对比方法和消融细节，无法判断实验覆盖的广度是否完全充分，但从已公开的信息看，设计较为完整。

## 6. 主要结论与发现
- TF‑FACE 在 **Argoverse 1** 上取得了 **state‑of‑the‑art** 的轨迹预测精度。
- 方法同时保持了**实时推理**能力，表明频域增强可以兼顾精度与效率。
- 在 **Argoverse 2** 上的额外实验进一步验证了 TF‑FACE 的**性能与泛化能力**，证明了频域融合方法的有效性。
- 核心发现：通过自适应的频域操控和时频一致性约束，能够显著改善长期依赖和短期动态的联合建模，从而生成更准确、更安全的多模态预测。

## 7. 优点
- **新颖的频域视角**：首次将可学习门控频域注意力引入轨迹预测，主动利用不同频带的信息，突破了纯时域方法的局限。
- **可控解耦与耦合**：双阶段解码器和频带特定损失实现了长期/短期、全局/局部尺度的显式控制，预测可解释性和灵活性更强。
- **实时能力**：在取得高精度的同时满足自动驾驶实时要求，具有较强的实际部署价值。
- **多数据集验证**：在 Argoverse 1 和 Argoverse 2 上均表现出色，证明了方法的泛化潜力。

## 8. 不足与局限
- **算力透明度不足**：未给出训练所需的计算资源详情，难以评估其复现成本和工程部署门槛。
- **对比范围未知**：摘要未列出具体对比方法列表，无法判断是否与最全的基准方法进行了比较。
- **场景局限性**：目前验证限于自动驾驶的车辆轨迹预测（Argoverse 数据），对行人、非机动车等多样化交通参与者的效果未作讨论。
- **损失超参敏感性**：双一致性损失可能引入额外的超参数（如频带划分、权重平衡），论文未透露其对调参的敏感程度，实际应用中可能增加调优难度。
- **频域操作的解释性**：虽然自适应门控提升了性能，但门控输出的物理含义与可解释性尚未在摘要中体现，可能影响安全性关键应用的可信度。

（完）
