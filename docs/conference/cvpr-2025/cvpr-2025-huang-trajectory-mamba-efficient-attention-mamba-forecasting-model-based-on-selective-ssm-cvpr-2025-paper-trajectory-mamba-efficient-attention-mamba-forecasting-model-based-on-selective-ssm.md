---
title: "Trajectory Mamba: Efficient Attention-Mamba Forecasting Model Based on Selective SSM"
title_zh: 轨迹Mamba：基于选择状态空间模型的高效注意力-曼巴预测模型
authors: "Huang, Yizhou, Cheng, Yihua, Wang, Kezhi"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Huang_Trajectory_Mamba_Efficient_Attention-Mamba_Forecasting_Model_Based_on_Selective_SSM_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 9.0
evidence: 高效的自动驾驶轨迹预测模型
tldr: 传统注意力模型计算量随目标数平方增长，难以用于动态环境。本文提出Trajectory Mamba，基于选择状态空间模型（SSM）重构编码器-解码器注意力，实现线性复杂度。实验表明在保持高精度的同时显著提升效率，适用于实时自动驾驶。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-huang-trajectory-mamba-efficient-attention-mamba-forecasting-model-based-on-selective-ssm-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 855, \"height\": 530, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-huang-trajectory-mamba-efficient-attention-mamba-forecasting-model-based-on-selective-ssm-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 864, \"height\": 538, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-huang-trajectory-mamba-efficient-attention-mamba-forecasting-model-based-on-selective-ssm-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1784, \"height\": 479, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-huang-trajectory-mamba-efficient-attention-mamba-forecasting-model-based-on-selective-ssm-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1795, \"height\": 810, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-huang-trajectory-mamba-efficient-attention-mamba-forecasting-model-based-on-selective-ssm-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1315, \"height\": 467, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-huang-trajectory-mamba-efficient-attention-mamba-forecasting-model-based-on-selective-ssm-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1779, \"height\": 423, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-huang-trajectory-mamba-efficient-attention-mamba-forecasting-model-based-on-selective-ssm-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1536, \"height\": 247, \"label\": \"Table\"}]"
motivation: 注意力模型计算开销大，限制在动态环境中的应用。
method: 利用选择状态空间模型替代自注意力，实现线性时间复杂度的编码器-解码器架构。
result: 在多个基准上达到与注意力模型相当的精度，但计算效率大幅提升。
conclusion: SSM可作为注意力机制的高效替代，用于实时轨迹预测。
---

## Abstract
Motion prediction is crucial for autonomous driving, as it enables accurate forecasting of future vehicle trajectories based on historical inputs. This paper introduces Trajectory Mamba, a novel efficient trajectory prediction framework based on the selective state-space model (SSM). Conventional attention-based models face the challenge of computational costs that grow quadratically with the number of targets, hindering their application in highly dynamic environments. In response, we leverage the SSM to redesign the self-attention mechanism in the encoder-decoder architecture, thereby achieving linear time complexity. To address the potential reduction in prediction accuracy resulting from modifications to the attention mechanism, we propose a joint polyline encoding strategy to better capture the associations between static and dynamic contexts, ultimately enhancing prediction accuracy. Additionally, to balance prediction accuracy and inference speed, we adopted the decoder that differs entirely from the encoder. Through cross-state space attention, all target agents share the scene context, allowing the SSM to interact with the shared scene representation during decoding, thus inferring different trajectories over the next prediction steps. Our model achieves state-of-the-art results in terms of inference speed and parameter efficiency on both the Argoverse 1 and Argoverse 2 datasets. It demonstrates a four-fold reduction in FLOPs compared to existing methods and reduces parameter count by over 40% while surpassing the performance of the vast majority of previous methods. These findings validate the effectiveness of Trajectory Mamba in trajectory prediction tasks.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：在自动驾驶场景中，基于注意力的轨迹预测模型（如Transformer）虽然精度高，但其计算复杂度随目标数量呈二次增长（O(N²)），难以满足高动态环境下实时性要求。同时，传统方法在处理静态场景（如车道线）与动态智能体（如车辆、行人）的异构数据融合时，往往采用水平统一的编码方式，未能充分捕捉不同元素间的深层关联，导致预测精度受限。
- **研究动机**：探索一种既能保持高精度又能实现线性复杂度的轨迹预测框架，以平衡效率与精度。选择状态空间模型（SSM）因其处理长序列时的线性复杂度和高效记忆特性，成为替代自注意力机制的潜力方案。
- **整体含义**：本文提出Trajectory Mamba（Tamba），首次将选择性SSM（即Mamba）引入自动驾驶轨迹预测，通过重新设计编码器-解码器中的自注意力机制，实现线性时间复杂度，同时通过联合折线编码策略增强异构数据融合，最终在Argoverse 1和2数据集上达到SOTA水平的效率与精度平衡。

## 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：利用选择性SSM替代传统多头自注意力，降低计算复杂度；设计联合折线编码策略，将行人轨迹与交通灯信号共享一个嵌入器，以更好地捕捉动态与静态上下文之间的关联；采用与编码器结构不同的交叉Mamba解码器，使所有目标智能体共享统一场景表示，递归生成多种候选轨迹。
- **关键技术细节**：
  1. **Joint Polyline Encoding（联合折线编码）**：将强相关的折线类型（如行人与交通灯）使用共享嵌入器编码，而特征差异大的类型（如车道线、交通标志）使用独立嵌入器。每个嵌入器由MLP和归一化层构成，输出经融合层交互。
  2. **Attention Tamba Encoder（注意力Tamba编码器）**：包含三个并行编码器，分别处理：
     - (I) 时空注意力：每个时间步内所有智能体与场景元素的自注意力；
     - (II) 场景注意力：动态智能体与静态场景元素之间的交叉注意力；
     - (III) 交通注意力：交通控制元素（行人+交通灯）对其他动态智能体的影响。
     编码器核心用SSM替代多头注意力，状态演化公式：h_{t+1}=A(P_t)h_t+B(P_t)u_t，输出y_t=C(P_t)h_t+D(P_t)u_t，实现线性复杂度O(T·n²)。
  3. **Cross Tamba Decoder（交叉Tamba解码器）**：借鉴DETR的查询向量机制，初始化K个查询向量，每个查询通过交叉Mamba模块与编码器输出的键值交互，递归生成K个候选轨迹。解码器中的交叉注意力同样用SSM替代，使所有目标智能体共享场景表示。
  4. **Trajectory Proposal & Refinement（轨迹提议与优化）**：先由解码器生成K个提议轨迹（使用MSE损失L_proposal），然后通过预测权重推理模块（含RNN）计算每个轨迹的置信度，再通过“赢家通吃”策略和混合Laplace分布建模优化最终轨迹。总损失：L_total = L_proposal + L_refine + λ L_cls。

## 3. 实验设计

- **数据集**：Argoverse 1（包含匹兹堡、迈阿密地区，10Hz采样，2秒观察预测3秒，>30,000样本）和Argoverse 2（11秒场景，5秒观察预测6秒，250,000场景，10类物体）。
- **Benchmark**：采用标准评估指标：minADE(K)、minFDE(K)、b-minFDE(K)、MR(K)，其中K=6和1。同时报告参数量（M）和FLOPs（G）衡量效率。
- **对比方法**：包括THOMAS、GoRela、QML、MTR、GANet、BANet、QCNet、LaneGCN、DenseTNT、SceneTransformer、HiVT、Wayformer等SOTA方法。所有对比均为原始方法直接比较，排除集成等工程改进。

## 4. 资源与算力

- **文中明确说明**：使用8块NVIDIA 3090TI GPU，batch size=128，训练50个epoch。优化器为Adam，初始学习率0.001，采用自适应学习率调整策略（验证精度连续5个epoch不提升时学习率降为0.1倍）。
- **未明确信息**：具体训练时长（小时数）未提及，但基于50 epoch和batch size可推断训练时间适中。

## 5. 实验数量与充分性

- **实验数量**：
  - 在Argoverse 2数据集上与9种以上方法对比（表1）。
  - 在Argoverse 1数据集上与6种以上方法对比（表2）。
  - 消融实验（表3）：评估三种编码器变体（Attention、Mamba、Tamba）在有无联合折线编码策略下的性能，覆盖minFDE_6、minADE_6、minFDE_1、minADE_1四个指标。
  - 可视化定性结果（图4）：展示四种不同交通场景下的预测轨迹。
- **充分性评价**：实验较为充分，覆盖多个主流数据集和多种SOTA方法，消融实验验证了关键组件（SSM替换、联合编码）的有效性。但缺少对超参数敏感度、不同SSM状态维度影响的系统分析，且仅在两个数据集上验证，泛化性需进一步检验。
- **客观公平性**：论文明确排除集成等工程改进，确保对比公平。但部分方法（表中标记“-”）因无法复现而空缺，可能引入细微偏差。

## 6. 论文的主要结论与发现

- Tamba在Argoverse 2上b-minFDE_6达1.89（优于QCNet的1.91），minFDE_6达1.24（优于QCNet的1.29），参数量仅4.54M（较QCNet减少40.7%），FLOPs 27.3G（较QCNet 45.3G降低39.7%）。
- 在Argoverse 1上Tamba b-minFDE_6达1.67（优于QCNet的1.69），MR_6仅0.09（优于QCNet的0.11），参数量同样4.54M。
- 消融实验证明Tamba编码器（SSM+注意力分解）显著优于纯Attention或纯Mamba变体，联合折线编码策略进一步提升了1%～2%的指标（minFDE_6从0.955降至0.951等）。
- 结论：SSM可高效替代传统注意力，实现线性复杂度，同时保持甚至提升预测精度，适合实时自动驾驶需求。

## 7. 优点

- **方法创新性**：首次将选择性SSM（Mamba）引入自动驾驶轨迹预测领域，重新设计编码器-解码器的注意力机制，实现线性时间复杂度。
- **效率显著提升**：FLOPs降低近4倍，参数量减少超40%，同时精度达到或超越SOTA。
- **编码策略巧妙**：联合折线编码将行人与交通灯共享嵌入，符合交通规则中行人优先对车辆影响的逻辑，提升了多类别交互建模能力。
- **实验验证充分**：在两大主流数据集上与众多方法对比，消融实验和定性可视化支持了方法的有效性。
- **实用导向**：关注实时性与轻量化，符合自动驾驶部署需求。

## 8. 不足与局限

- **实验覆盖**：仅在Argoverse 1和2上验证，未在nuScenes等其他主流轨迹预测数据集上测试，泛化性存疑。
- **缺乏消融深度**：未系统分析不同SSM状态维度（n）、序列长度L、查询向量数K等超参数对性能与效率的影响。
- **偏差风险**：部分对比方法（如THOMAS、GoRela等）因复现问题未报告完整数据，可能影响比较的完整性。
- **应用限制**：方法依赖高精地图和结构化场景表示，对无地图或开放性环境适应性未讨论；SSM在极长序列（如6秒以上）上的表现未验证。
- **理论深度**：SSM替换注意力的理论基础分析较浅，未对选择性SSM如何保留长程依赖进行量化解释。

（完）
