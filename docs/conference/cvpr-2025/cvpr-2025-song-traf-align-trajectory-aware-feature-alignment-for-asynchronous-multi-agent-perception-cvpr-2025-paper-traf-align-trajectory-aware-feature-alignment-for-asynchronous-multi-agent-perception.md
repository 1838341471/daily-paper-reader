---
title: "TraF-Align: Trajectory-aware Feature Alignment for Asynchronous Multi-agent Perception"
title_zh: TraF-Align：面向异步多车感知的轨迹感知特征对齐
authors: "Song, Zhiying, Yang, Lei, Wen, Fuxi, Li, Jun"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Song_TraF-Align_Trajectory-aware_Feature_Alignment_for_Asynchronous_Multi-agent_Perception_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 4.0
evidence: 利用轨迹预测实现自动驾驶协同感知中的特征对齐
tldr: 协同感知中多车间的通信延迟导致空间和语义特征错位。本文提出TraF-Align，通过预测特征级轨迹，生成时序有序采样点，引导当前查询与历史特征对齐。实验证明该方法在延迟条件下显著提升了感知融合精度。该工作将轨迹预测用于感知增强，为自动驾驶多车协同提供了新思路。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-song-traf-align-trajectory-aware-feature-alignment-for-asynchronous-multi-agent-perception-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 832, \"height\": 572, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-song-traf-align-trajectory-aware-feature-alignment-for-asynchronous-multi-agent-perception-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1766, \"height\": 796, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-song-traf-align-trajectory-aware-feature-alignment-for-asynchronous-multi-agent-perception-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 842, \"height\": 715, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-song-traf-align-trajectory-aware-feature-alignment-for-asynchronous-multi-agent-perception-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 840, \"height\": 941, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-song-traf-align-trajectory-aware-feature-alignment-for-asynchronous-multi-agent-perception-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 837, \"height\": 1018, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-song-traf-align-trajectory-aware-feature-alignment-for-asynchronous-multi-agent-perception-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 801, \"height\": 653, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-song-traf-align-trajectory-aware-feature-alignment-for-asynchronous-multi-agent-perception-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1775, \"height\": 566, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-traf-align-trajectory-aware-feature-alignment-for-asynchronous-multi-agent-perception-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1796, \"height\": 491, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-traf-align-trajectory-aware-feature-alignment-for-asynchronous-multi-agent-perception-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 870, \"height\": 516, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-traf-align-trajectory-aware-feature-alignment-for-asynchronous-multi-agent-perception-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 861, \"height\": 514, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-traf-align-trajectory-aware-feature-alignment-for-asynchronous-multi-agent-perception-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 856, \"height\": 346, \"label\": \"Table\"}]"
motivation: 多车感知中的延迟导致特征错位，影响融合效果。
method: 预测特征级轨迹并生成采样点，通过注意力机制对齐历史特征与当前查询。
result: 在模拟和真实延迟场景下，TraF-Align的感知精度优于现有方法。
conclusion: 轨迹感知的特征对齐能有效克服异步多车感知中的延迟挑战。
---

## Abstract
Cooperative perception presents significant potential for enhancing the sensing capabilities of individual vehicles, however, inter-agent latency remains a critical challenge. Latencies cause misalignments in both spatial and semantic features, complicating the fusion of real-time observations from the ego vehicle with delayed data from others. To address these issues, we propose TraF-Align, a novel framework that learns the flow path of features by predicting the feature-level trajectory of objects from past observations up to the ego vehicle's current time. By generating temporally ordered sampling points along these paths, TraF-Align directs attention from the current-time query to relevant historical features along each trajectory, supporting the reconstruction of current-time features and promoting semantic interaction across multiple frames. This approach corrects spatial misalignment and ensures semantic consistency across agents, effectively compensating for motion and achieving coherent feature fusion. Experiments on two real-world datasets, V2V4Real and DAIR-V2X-Seq, show that TraF-Align sets a new benchmark for asynchronous cooperative perception.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：在车联网（V2X）协同感知中，不同智能体（车辆或路侧设备）之间的通信延迟会导致多帧点云/特征在空间和时间上错位，具体表现为：
  - **空间错位**：由于其他智能体的观测时间早于自车当前时刻，物体位置发生移动，导致其发送的特征与当前真实空间位置不匹配。
  - **语义错位**：自车和其他智能体虽然观测同一物体，但由于延迟，无法识别这些特征属于同一实体，导致融合后出现误检或漏检。
- **研究动机**：现有方法如直接预测高维特征（FFNet）或实例级ROI跟踪（CoBEVFlow）难以处理较大延迟，且缺乏端到端能力；同时语义错位问题尚未被充分研究。因此需要一种能同时解决空间和语义错位的异步协同感知框架。
- **整体含义**：提出TraF-Align，通过预测低维轨迹场来引导高维特征的流向与交互，实现多帧特征的时空对齐与语义共识，从而鲁棒地处理延迟。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：不直接预测高维特征的运动，而是学习低维的物体**轨迹特征**（位置场和方向场），利用该轨迹场生成时序有序的**采样点**，然后通过**交叉注意力**机制使当前查询（query）沿着轨迹关注历史相关特征，实现当前时刻特征的重建与跨智能体语义一致性。
- **关键技术细节**：
  1. **特征提取与缓存**：使用PointPillars+PillarNext骨架提取BEV特征，并加入时间编码（正弦/余弦位置编码）以支持多帧重用。
  2. **轨迹场预测（Field Predictor）**：基于U-Net变体，为每个智能体预测一个轨迹场，包含：
     - **位置场**：物体沿轨迹的占位热度图。
     - **方向场**：轨迹的流向（反正切方向）。
     轨迹场的地面真值由各智能体局部坐标系下的历史边界框中心连接生成，并投影到同一当前时刻。
  3. **偏移生成器（Offset Generator）**：对每个查询位置，生成一组注意力位置（n=18），这些位置满足三个条件：位于位置场响应区域、与查询属于同一轨迹、时间上早于查询。通过简单卷积+PReLU生成偏移量。
  4. **轨迹感知注意力（Trajectory-aware Attention）**：将每个查询与生成的响应集合中的特征做多头注意力（类似Transformer），实现特征沿轨迹传递与交互，重建当前时刻特征并达成语义对齐。
  5. **损失函数**：包括检测损失（PointPillars标准）、场损失（位置场用Focal Loss，方向场用L1 Loss）、偏移损失（通过Sinkhorn算法匹配预测偏移与真实偏移后计算L1距离）。总损失权重α=β=0.05。
  6. **融合与检测**：将各智能体对齐后的特征简单拼接后通过卷积融合，再用锚点检测头输出3D框。

### 3. 实验设计：数据集、基准、对比方法

- **数据集**：
  - **V2V4Real**：真实场景V2V协同感知数据集，城市环境。
  - **DAIR-V2X-Seq**：真实场景V2I（车-路）协同感知数据集，路口环境。
- **基准与对比方法**：
  - 单智能体感知（Ego only）。
  - 8种SOTA中间特征融合方法：F-Cooper、V2VNet、Where2comm、AttFuse、V2X-ViT、CoBEVT、MRCNet、ERMVP。
- **评估指标**：Average Precision (AP) 在IoU 0.5 (AP50) 和0.7 (AP70)。
- **延迟设置**：对非自车智能体（cooperative vehicle或infrastructure）分别施加0、100、200、300、400 ms的延迟，报告各延迟下的AP。
- **训练细节**：统一代码框架，训练60 epochs，使用one-cycle学习率策略和AdamW优化器。数据增强包括随机翻转、缩放、旋转、平移。多帧方法使用随机延迟增强（0-400ms均匀分布）。TraF-Align在V2V4Real上使用自车2帧+协作车4帧，DAIR-V2X-Seq上各4帧。

### 4. 资源与算力

- 文中明确说明：使用 **九块 RTX 3090 GPU** 训练模型，共训练 **60个epoch**。但未提及具体训练时长（如小时数）。论文未提供推理速度或参数量信息。

### 5. 实验数量与充分性

- **主要对比实验**：在两个数据集上，对每种延迟条件（0/100/200/300/400ms）各报告一次结果（共10个场景），充分展示了与8种SOTA方法的对比，覆盖同步和异步情况。
- **消融实验**（表2-4）：
  - 核心组件消融（场预测器、偏移生成器、注意力层）——在DAIR-V2X-Seq上针对基础设施延迟和车辆延迟分别测试。
  - 损失消融（场损失、偏移损失）——同样在DAIR-V2X-Seq上。
  - 帧数消融（自车/协作车LiDAR帧数）——在V2V4Real上测试。
- **定性分析**：可视化检测结果、轨迹场、注意力分布，对比了V2VNet、COBEVT、V2X-ViT等。
- **Precision-Recall曲线**（图5）：展示了ERMVP与TraF-Align在不同延迟下的PR曲线。
- **充分性评价**：实验较为充分，覆盖两个大规模真实数据集、多种延迟、多种SOTA方法、详细的消融（组件、损失、帧数）。但未涉及：
  - 压缩通信带宽的影响（文中特意去掉了压缩操作）。
  - 不同噪声水平（如定位误差、通信丢包）下的鲁棒性。
  - 实际部署延迟分布（仅测试规律间隔的固定延迟）。
  - 未在合成数据集或仿真中评测。

### 6. 论文的主要结论与发现

- **主要结论**：TraF-Align在同步和异步场景下均大幅超越现有SOTA方法。例如在V2V4Real上，400ms延迟时AP50/AP70分别达到69.41%/38.49%，比ERMVP（57.26%/29.31%）高出12%以上；在DAIR-V2X-Seq上同样显著领先。
- **鲁棒性**：延迟从0增加到400ms，TraF-Align的AP下降幅度远小于其他方法，表明其有效解决了空间和语义错位。
- **组件有效性**：消融证明场预测器、偏移生成器、注意力层、场损失和偏移损失均对性能有正向贡献。
- **帧数影响**：增加协作车帧数提升AP及延迟鲁棒性；自车帧数过多可能引入运动模糊，最佳的帧数组合需平衡。

### 7. 优点

- **方法创新**：
  - 首次提出利用低维轨迹场引导高维特征的对齐，避免了直接预测高维特征的不可控性。
  - 端到端可训练，无需两阶段ROI生成和跟踪。
  - 同时解决了空间错位和语义错位，且能处理较大延迟（400ms）。
- **实验设计**：
  - 在两种真实数据集（V2V和V2I）上验证，场景多样。
  - 消融实验全面，包括组件、损失、帧数，证实各模块必要性。
  - 提供了PR曲线深入分析延迟对召回和精度的影响。
- **性能优势**：在同步场景也显著优于已有方法，说明轨迹感知注意力不仅处理延迟，还增强了特征表达能力。

### 8. 不足与局限

- **实验覆盖不足**：
  - 延迟设置仅为规则间隔（100ms整数倍），未测试服从真实网络延迟分布（如对数正态、随机抖动）的情况。
  - 未评估通信带宽限制下特征压缩对性能的影响（论文特意省略了压缩操作）。
  - 未考虑定位误差、数据包丢失等现实噪声。
  - 训练数据和测试数据均来自同一数据集，未进行跨域泛化测试。
- **方法局限**：
  - 依赖多帧LiDAR输入，增加计算和存储成本，且自车帧数过多可能引入运动模糊。
  - 轨迹场预测依赖历史边界框标注，对未标注物体或非刚性物体（如行人）可能效果不佳。
  - 需精确的智能体间姿态对齐和时间同步，误差会降低性能（论文提及但未实验验证）。
  - 仅针对LiDAR点云，未扩展至相机或雷达模态。
- **可复现性**：代码已开源，但训练时长和推理速度未报告，不利于公平对比。

（完）
