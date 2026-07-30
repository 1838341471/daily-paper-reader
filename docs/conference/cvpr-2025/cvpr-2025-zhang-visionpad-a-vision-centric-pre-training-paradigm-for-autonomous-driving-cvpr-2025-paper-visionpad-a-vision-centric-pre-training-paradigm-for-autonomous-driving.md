---
title: "VisionPAD: A Vision-Centric Pre-training Paradigm for Autonomous Driving"
title_zh: VisionPAD：面向自动驾驶的视觉中心预训练范式
authors: "Zhang, Haiming, Zhou, Wending, Zhu, Yiyao, Yan, Xu, Gao, Jiantao, Bai, Dongfeng, Cai, Yingjie, Liu, Bingbing, Cui, Shuguang, Li, Zhen"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_VisionPAD_A_Vision-Centric_Pre-training_Paradigm_for_Autonomous_Driving_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 6.0
evidence: 面向视觉自动驾驶的自监督预训练，学习运动线索以支持轨迹预测
tldr: 视觉自动驾驶的预训练通常需要显式深度监督。本文提出VisionPAD，利用3D高斯泼溅仅从图像进行多视图重建，并引入自监督体素速度估计和帧间光度一致性约束。预训练的视觉骨干在轨迹预测、目标检测等下游任务上显著提升性能，证明了无监督运动学习对自动驾驶感知的有效性。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-visionpad-a-vision-centric-pre-training-paradigm-for-autonomous-driving-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 780, \"height\": 228, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-visionpad-a-vision-centric-pre-training-paradigm-for-autonomous-driving-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 804, \"height\": 393, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-visionpad-a-vision-centric-pre-training-paradigm-for-autonomous-driving-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1782, \"height\": 440, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-visionpad-a-vision-centric-pre-training-paradigm-for-autonomous-driving-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 839, \"height\": 451, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-visionpad-a-vision-centric-pre-training-paradigm-for-autonomous-driving-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 865, \"height\": 866, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-visionpad-a-vision-centric-pre-training-paradigm-for-autonomous-driving-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1790, \"height\": 1361, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-visionpad-a-vision-centric-pre-training-paradigm-for-autonomous-driving-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 860, \"height\": 938, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-visionpad-a-vision-centric-pre-training-paradigm-for-autonomous-driving-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1653, \"height\": 797, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-visionpad-a-vision-centric-pre-training-paradigm-for-autonomous-driving-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 848, \"height\": 239, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-visionpad-a-vision-centric-pre-training-paradigm-for-autonomous-driving-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1813, \"height\": 601, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-visionpad-a-vision-centric-pre-training-paradigm-for-autonomous-driving-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1752, \"height\": 426, \"label\": \"Table\"}]"
motivation: 现有预训练依赖深度标注，且缺乏对运动线索的学习。
method: 采用3D高斯泼溅重建多视图表示，自监督估计体素速度并施加光度一致性损失。
result: 预训练模型在多个自动驾驶下游任务上取得优异性能，尤其轨迹预测。
conclusion: 以运动学习为核心的自监督预训练是提升视觉自动驾驶的有效途径。
---

## Abstract
This paper introduces VisionPAD, a novel self-supervised pre-training paradigm designed for vision-centric algorithms in autonomous driving. In contrast to previous approaches that employ neural rendering with explicit depth supervision, VisionPAD utilizes more efficient 3D Gaussian Splatting to reconstruct multi-view representations using only images as supervision. Specifically, we introduce a self-supervised method for voxel velocity estimation. By warping voxels to adjacent frames and supervising the rendered outputs, the model effectively learns motion cues in the sequential data. Furthermore, we adopt a multi-frame photometric consistency approach to enhance geometric perception. It projects adjacent frames to the current frame based on rendered depths and relative poses, boosting the 3D geometric representation through pure image supervision. Extensive experiments on autonomous driving datasets demonstrate that VisionPAD significantly improves performance in 3D object detection, occupancy prediction and map segmentation, surpassing state-of-the-art pre-training strategies by a considerable margin.

---

## 论文详细总结（自动生成）

# 论文中文总结：VisionPAD: 面向自动驾驶的视觉中心预训练范式

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：现有自动驾驶视觉中心算法（如 BEV、占用网络）依赖大量3D标注（点云、边界框），标注成本极高。预训练是降低标注依赖的关键策略，但主流预训练方法（如对比学习、MAE、神经渲染）要么需显式深度监督（LiDAR），要么难以同时捕捉语义、几何和时序动态。
- **目标**：提出一种仅依赖多帧多视角图像的自监督预训练范式，让模型从纯视觉数据中学习几何、运动（速度）和时序一致性，从而提升下游任务性能。
- **整体含义**：VisionPAD 是首个将 3D 高斯泼溅（3D-GS）用于驾驶预训练的工作，通过自监督体素速度估计和光度一致性约束，在无需任何深度标注的条件下，显著超越依赖显式深度监督的 SOTA 方法（如 UniPAD）。

## 2. 方法论：核心思想、关键技术细节
### 2.1 核心思想
- 以多帧多视图图像为输入，通过视觉 backbone 提取 2D 特征，经视图变换得到体素特征。
- 采用**锚点式 3D 高斯泼溅（3D-GS）解码器**将体素特征转化为一组 3D 高斯原语，高效渲染多视图图像和深度。
- 引入**自监督体素速度估计**：预测每个体素的运动速度，通过时间差将体素扭曲到相邻帧，再借助 3D-GS 解码器渲染相邻帧图像并与真实图像计算损失，从而学习运动线索。
- 采用**多帧光度一致性损失**：基于渲染的深度图和已知相对位姿，将相邻帧重投影到当前帧，施加重建损失，强化几何表征。

### 2.2 关键技术细节
1. **体素构建**：输入 M 个历史多视图图像，共享图像骨干提取 2D 特征，经视图变换（如 LSS）得到 3D 体素特征 V ∈ R^(X×Y×Z×C)。
2. **3D-GS 解码器**：
   - 以每个体素中心为锚点，使用 MLP 预测多个高斯原语的属性（偏移量、旋转、尺度、不透明度、球谐系数）。
   - 通过可微分光栅化（alpha-blending）渲染多视图图像和深度图。
   - 对低不透明度高斯进行过滤（tanh 激活后 opacity < 0 的丢弃）以降低计算量。
3. **自监督体素速度估计**：
   - 增加一个辅助速度头，回归每个体素在世界坐标系中的速度向量。
   - 利用帧间时间差 Δt 计算体素流向：flow = v·Δt，通过 GridSample 将当前帧体素特征扭曲到相邻帧。
   - 对扭曲后的体素特征使用 3D-GS 解码器渲染相邻帧图像，与真实图像计算 L1 损失，且梯度仅回传到速度头。
4. **光度一致性**：
   - 利用当前帧渲染的深度图 D_t、相对位姿 T_(t→t‘) 和相机内参 K，将源帧 I_t’ 重投影到当前视角得到 I_(t‘→t)。
   - 损失函数：L_pc = α·(1-SSIM(I_t, I_{t'→t})) + (1-α)·||I_t - I_{t'→t}||_1（α=0.85）。
5. **预训练总损失**：L = ω1·L_img + ω2·L_vel + ω3·L_pc，其中 ω1=0.5, ω2=1, ω3=1。

## 3. 实验设计
- **数据集**：nuScenes（700/150/150 场景，6 摄像头环视），采用标准 nuScenes Detection Score (NDS) 和 mAP 评估 3D 检测；语义占用预测用 Occ3D 的 mIoU；地图分割用车道线 IoU。
- **基准方法**：
  - 3D 检测：UVTR、BEVFormer、PETR、UniPAD 等。
  - 语义占用：BEVFormer、TPVFormer、FB-Occ、RenderOcc、SparseOcc、OPUS 等。
  - 地图分割：UniAD 地图解码器。
- **对比结果**：
  - 3D 检测（表1）：UVTR 基线 NDS=45.0, mAP=37.5；VisionPAD 达到 NDS=46.7, mAP=41.0（+1.7 NDS, +3.8 mAP）；若加 LiDAR 深度，NDS=50.4, mAP=43.1。
  - 语义占用（表2）：UVTR 基线 mIoU=30.1%；VisionPAD 提升到 35.4%（+5.3%），且超过某些检测预训练的方法。
  - 地图分割（表3）：UVTR 基线 IoU=15.0%；VisionPAD 提升到 20.4%（+5.4%）。
  - 数据效率（图4）：使用 25% 标注数据时，VisionPAD 比 UniPAD 高出约 6 mAP 和 5 NDS。
- **消融实验**（表4）：逐步验证 3D-GS 解码器（+0.6 NDS）、高斯过滤（+0.8 NDS）、体素速度估计（+1.2 mAP）、光度一致性（+2.4 NDS, +4.4 mAP），完整模型相对基线提升 +4.5 NDS, +7.1 mAP。

## 4. 资源与算力
- 论文中未明确说明使用的 GPU 型号和数量。
- 提及预训练总 batch size = 4，学习率 2×10⁻⁴，AdamW 优化器，训练 12 epochs。
- 消融实验采用了较轻量的设置（体素 0.8m 分辨率、128×128×5、通道 128）以节省时间。
- 总体算力需求未详细披露，属于论文未说明部分。

## 5. 实验数量与充分性
- **实验数量**：涵盖 3 个主要下游任务（检测、占用、地图分割）各一组实验；数据效率实验（4 种标注比例）；系统消融（6 组逐步组件比较）；额外实验（不同 anchor 数量、渲染质量可视化）。
- **充分性与公平性**：
  - 与 UniPAD 在同一骨干 (ConvNeXt-S)、相同数据增强、相同下游微调配置下对比，确保公平。
  - 消融实验完整，贡献归因清晰。
  - 数据效率实验验证了小样本场景下的优越性。
  - 但缺失与 Masked Autoencoder 类方法（如 BEV-MAE）、对比学习方法的直接对比，也未在 nuScenes 之外的数据集（如 Waymo）上验证泛化性。
- **偏差风险**：所有实验仅在 nuScenes 上进行，场景单一（城市环境）；速度估计依赖已知相对位姿（可能来自 CAN/IMU），若位姿噪声大可能导致偏差。

## 6. 主要结论与发现
1. VisionPAD 是首个仅用图像监督在自动驾驶预训练中超越依赖深度监督方法的工作，证明了纯视觉中心预训练的可行性。
2. 3D-GS 解码器相比 NeRF 体渲染能提供更高分辨率重建和更优的几何学习，且计算成本对分辨率不敏感。
3. 自监督体素速度估计能有效捕获运动线索，分离动静态体素，提升下游时序感知任务。
4. 光度一致性损失显著增强了 3D 几何表征，尤其在密集占用预测上提升巨大。
5. 预训练后在下游数据有限时（如 25% 标注）优势更突出，展现了数据高效率性。

## 7. 优点
- **方法创新**：首次将 3D-GS 引入驾驶预训练，利用其高效可微渲染替代传统体渲染；自监督速度估计无需任何标注，仅凭图像时序信息即可学习运动；光度一致性损失从自监督深度估计迁移到预训练中，强化几何。
- **完全视觉中心**：无需 LiDAR、深度图或任何 3D 标注，降低了数据采集成本，易于扩展到纯视觉系统。
- **高效的渲染机制**：3D-GS 的基于光栅化的渲染比 NeRF 的逐射线采样快得多，可一次渲染全图。
- **强实验验证**：在三个任务上均大幅超过 SOTA，且消融实验设计严谨，贡献分解清晰。

## 8. 不足与局限
- **实验范围局限**：仅在 nuScenes 单一数据集上评估，缺乏跨数据集（如 Waymo、KITTI）的泛化验证，无法确认方法的领域适应性。
- **缺失与非渲染方法的对比**：未与 MAE、对比学习等更广泛的自监督方法比较，无法确定相比其他范式的优势程度。
- **算力信息缺失**：未报告预训练的总 GPU 小时数，影响可复现性和成本评估。
- **速度估计的依赖**：速度监督仅通过渲染损失反传，可能对快速运动或严重遮挡的物体估计不准确；且假设相对位姿已知，实际系统中位姿噪声可能影响光度一致性效果。
- **潜在偏差风险**：预训练仅使用 nuScenes 的固定环视相机配置，对不同的相机布局 (如车辆前后视角不一致) 可能不兼容。
- **其他**：论文未讨论失败案例或场景（如恶劣天气 / 夜间），也未提供速度估计的定量评估（如速度误差）。

（完）
