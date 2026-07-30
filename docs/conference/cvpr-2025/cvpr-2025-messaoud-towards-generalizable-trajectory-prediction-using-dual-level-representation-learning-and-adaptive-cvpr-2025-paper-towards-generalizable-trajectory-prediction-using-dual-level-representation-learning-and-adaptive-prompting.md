---
title: Towards Generalizable Trajectory Prediction using Dual-Level Representation Learning and Adaptive Prompting
title_zh: 迈向泛化轨迹预测：双级表示学习与自适应提示
authors: "Messaoud, Kaouther, Cord, Matthieu, Alahi, Alexandre"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Messaoud_Towards_Generalizable_Trajectory_Prediction_using_Dual-Level_Representation_Learning_and_Adaptive_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 9.0
evidence: 直接针对车辆轨迹预测框架
tldr: 现有车辆轨迹预测模型泛化性差且难以处理复杂交互。本文提出PerReg+框架，通过自蒸馏和掩码重建实现双级表示学习，并引入自适应提示以增强泛化能力。实验表明该方法在多种数据集上显著提升预测精度，为自动驾驶安全决策提供有力支持。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-messaoud-towards-generalizable-trajectory-prediction-using-dual-level-representation-learning-and-adaptive-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 862, \"height\": 830, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-messaoud-towards-generalizable-trajectory-prediction-using-dual-level-representation-learning-and-adaptive-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1773, \"height\": 1004, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-messaoud-towards-generalizable-trajectory-prediction-using-dual-level-representation-learning-and-adaptive-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1475, \"height\": 424, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-messaoud-towards-generalizable-trajectory-prediction-using-dual-level-representation-learning-and-adaptive-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 713, \"height\": 404, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-messaoud-towards-generalizable-trajectory-prediction-using-dual-level-representation-learning-and-adaptive-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1778, \"height\": 827, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-messaoud-towards-generalizable-trajectory-prediction-using-dual-level-representation-learning-and-adaptive-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 874, \"height\": 310, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-messaoud-towards-generalizable-trajectory-prediction-using-dual-level-representation-learning-and-adaptive-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 872, \"height\": 456, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-messaoud-towards-generalizable-trajectory-prediction-using-dual-level-representation-learning-and-adaptive-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 874, \"height\": 297, \"label\": \"Table\"}]"
motivation: 现有模型针对特定数据集定制，泛化性差且无法有效处理多模态预测。
method: 提出PerReg+，结合自蒸馏与掩码重建的双级表示学习，以及自适应提示机制。
result: 在多个自动驾驶数据集上超越现有方法，预测精度和泛化能力显著提升。
conclusion: 双级学习与自适应提示有效提升了轨迹预测的泛化性和准确性。
---

## Abstract
Existing vehicle trajectory prediction models struggle with generalizability, prediction uncertainties, and handling complex interactions. It is often due to limitations like complex architectures customized for a specific dataset and inefficient multimodal handling. We propose Perceiver with Register queries (PerReg+), a novel trajectory prediction framework that introduces: (1) Dual-Level Representation Learning via Self-Distillation (SD) and Masked Reconstruction (MR), capturing global context and fine-grained details. Additionally, our approach of reconstructing segment-level trajectories and lane segments from masked inputs with query drop, enables effective use of contextual information and improves generalization; (2) Enhanced Multimodality using register-based queries and pretraining, eliminating the need for clustering and suppression; and (3) Adaptive Prompt Tuning during fine-tuning, freezing the main architecture and optimizing a small number of prompts for efficient adaptation. PerReg+ sets a new state-of-the-art performance on nuScenes, Argoverse 2, and Waymo Open Motion Dataset (WOMD). Remarkable, our pretrained model reduces the error by 6.8% on smaller datasets, and multi-dataset training enhances generalization. In cross-domain tests, PerReg+ reduces B-FDE by 11.8% compared to its non-pretrained variant.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：现有车辆轨迹预测模型在泛化性、预测不确定性和复杂交互处理方面表现不足。主要原因是架构过于复杂且针对特定数据集定制，多模态处理效率低下（如依赖聚类、非极大值抑制等）。
- **研究动机**：自动驾驶需要对动态多智能体环境进行准确轨迹预测，但现有方法难以适应不同场景和数据集。自监督学习（SSL）和感知器架构（Perceiver）虽有潜力，但尚未被有效结合。
- **整体含义**：本文提出**PerReg+**框架，通过双级表示学习（自蒸馏SD + 掩码重建MR）和自适应提示调优（Adaptive Prompt Tuning），显著提升轨迹预测的泛化能力和准确性，为自动驾驶安全决策提供更可靠的预测基础。

## 2. 方法论：核心思想、关键技术细节、公式或算法流程

### 核心思想
- 结合**自蒸馏（Self-Distillation, SD）** 和**掩码重建（Masked Reconstruction, MR）**，分别捕捉全局场景上下文和细粒度细节。
- 在感知器IO架构（Perceiver IO）中引入**寄存器查询（Register Queries）** 和**模式查询（Mode Queries）**，实现高效多模态预测，无需聚类或抑制。
- 采用**自适应提示调优（Adaptive Prompt Tuning）**，在微调阶段冻结主架构，仅优化少量提示（prompts），实现高效适应新场景。

### 关键技术细节
- **输入表示**：将历史轨迹（H）和道路图（R）通过线性层映射为统一嵌入，加入时间和空间位置编码后拼接为混合输入 X_mixed。
- **Perceiver IO编码器**：先通过交叉注意力将X_mixed映射到固定大小潜空间 Z_latent，再经过多层自注意力增强交互。
- **掩码自蒸馏（Masked SD）**：
  - 教师编码器处理未掩码输入（含未来轨迹），学生编码器处理掩码输入。
  - 通过指数移动平均（EMA）更新教师权重，学生输出与教师输出通过交叉熵损失对齐（公式5）。
- **掩码重建（MR）**：
  - **细粒度掩码**：对历史轨迹点、未来轨迹点和车道折线点进行随机掩码（掩码率分别为90%、97%、75%）。
  - **段级重建查询**：使用两组查询（Q_agents, Q_road）分别重建智能体轨迹（过去和未来）和车道段，并随机丢弃部分查询（丢弃率40%）以增强鲁棒性。
- **多模态预测**：
  - 设定固定数量的**模式查询**（M个），每个查询输出一个预测轨迹及其概率（通过GMM建模）。
  - **寄存器查询**：作为解码器的结构化记忆，保留中间场景表示，有助于微调。
- **损失函数**（公式8）：总损失 = w_distill·L_distill + w_GMM·L_GMM + w_recon·L_recon，并通过动态权重分配（DWA）平衡各任务。
- **自适应提示调优**：
  - 保留预训练的解码器（包括模式查询和寄存器查询），冻结主架构。
  - 利用预训练的场景聚类头（MLP）将输入聚类到K个簇，每个簇对应一个可学习的提示（prompt）。
  - 微调时仅优化提示池和预测头，其他参数冻结。输出为：Ŷ = f_frozen(X, p_k)。

## 3. 实验设计：数据集、Benchmark、对比方法

- **数据集**：nuScenes（32k样本）、Argoverse 2（AV2，180k样本）、Waymo Open Motion Dataset（WOMD，1.8M样本）。均基于UniTraj框架处理，地图范围100米半径，历史2秒、未来6秒。
- **Benchmark**：采用UniTraj基准指标：brier-minFDE、minADE、minFDE、Miss Rate（MR），多模态预测数设为6。
- **对比方法**：AutoBot、MTR、Forecast-MAE（含预训练变体），以及PerReg无预训练变体。

## 4. 资源与算力

- **文中未明确说明使用的GPU型号、数量、训练时长等具体算力信息**。仅提到模型实现基于UniTraj框架，使用Perceiver架构，训练超参数包括AdamW优化器、初始学习率2e-4、批大小128。实际算力需求需参考UniTraj或感知器架构的常见配置，但本文未给出具体数字。

## 5. 实验数量与充分性

- **实验组数**：主要包括：
  - 单数据集训练与多数据集训练对比（表1，覆盖3个数据集×2种训练模式×多种方法）。
  - 域外泛化实验（表2：在WOMD训练，在nuScenes测试）。
  - 消融实验（表3：逐步加入注册查询、段级重建、解码器保留、多模态预测、掩码SD、提示调优）。
  - 掩码率和查询丢弃率影响实验（表4、图4）。
  - 定性可视化（图3、图5）。
- **充分性与公平性**：实验覆盖多个主流数据集、多种训练策略，对比了最新的SOTA方法，消融实验完整分析每个组件的贡献。结果客观，但未提供统计显著性检验，且部分基线（如MTR、AutoBot）在部分数据集上表现较弱。

## 6. 主要结论与发现

- PerReg+在nuScenes、AV2、WOMD上均达到SOTA，尤其在较小数据集（nuScenes、AV2）上预训练带来显著提升（B-FDE降低11%~13%）。
- 多数据集训练进一步改善泛化，在WOMD上PerReg+优于AutoBot和MTR。
- 域外泛化测试中，PerReg+相对于非预训练变体B-FDE降低11.8%，优于Forecast-MAE（仅降0.6%），得益于提示调优保留预训练知识。
- 消融实验表明：注册查询贡献最大（B-FDE降低11%），其次为多模态预测（5.0%）、掩码SD（6.4%）、提示调优（0.8%）。
- 最佳掩码率：智能体0.9，车道0.75；最佳查询丢弃率40%。

## 7. 优点

- **方法创新**：首次将自蒸馏与掩码重建结合到感知器架构中，实现双级表示学习；段级重建和查询丢弃增强了鲁棒性；寄存器查询有效替代传统聚类/抑制。
- **高效微调**：自适应提示调优使得模型在少量参数下快速适应新场景，适合资源受限场景。
- **泛化能力强**：在跨数据集和域外测试中表现突出，验证了预训练和提示调优的有效性。
- **实验全面**：覆盖三大数据集、多种训练模式、消融等，结果可信。

## 8. 不足与局限

- **算力资源未报告**：无法直接评估训练成本或推理效率，不利于实际部署参考。
- **实验覆盖局限**：仅针对车辆轨迹预测，未验证对行人、自行车等其他交通参与者的泛化性；仅使用三个数据集，未在更多样化场景（如不同国家/天气）测试。
- **风险偏差**：模型依赖感知器架构，其固定大小潜空间可能限制对极端复杂场景的建模能力；提示调优依赖聚类质量，若聚类不准确可能影响适应效果。
- **方法复杂度**：虽然微调参数少，但整体架构（教师-学生双编码器、多查询、动态权重）设计相对复杂，实现和调参成本较高。
- **论文未讨论失败案例**：无对错误预测的深入分析，缺乏对模型局限性（如长尾场景、极端交互）的讨论。

（完）
