---
title: "ReconDreamer: Crafting World Models for Driving Scene Reconstruction via Online Restoration"
title_zh: ReconDreamer：通过在线恢复构建驾驶场景重建的世界模型
authors: "Ni, Chaojun, Zhao, Guosheng, Wang, Xiaofeng, Zhu, Zheng, Qin, Wenkang, Huang, Guan, Liu, Chen, Chen, Yuyin, Wang, Yida, Zhang, Xueyang, Zhan, Yifei, Zhan, Kun, Jia, Peng, Lang, Xianpeng, Wang, Xingang, Mei, Wenjun"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Ni_ReconDreamer_Crafting_World_Models_for_Driving_Scene_Reconstruction_via_Online_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 4.0
evidence: 世界模型驱动驾驶场景重建支持新轨迹渲染
tldr: 现有神经渲染方法在渲染新驾驶轨迹（如变道）时效果不佳。本文提出ReconDreamer，通过渐进式整合世界模型知识来增强场景重建，使仿真系统能够渲染更大机动动作。该方法将世界模型在线恢复与NeRF/3DGS结合。实验证明在重建质量和新视图合成上优于先前方法，对于自动驾驶闭环仿真有重要价值。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1727, \"height\": 1073, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1705, \"height\": 1075, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 803, \"height\": 662, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 885, \"height\": 618, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 819, \"height\": 581, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1672, \"height\": 1692, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 875, \"height\": 600, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1806, \"height\": 309, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 868, \"height\": 248, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 868, \"height\": 257, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1811, \"height\": 591, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 869, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1804, \"height\": 236, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-recondreamer-crafting-world-models-for-driving-scene-reconstruction-via-online-cvpr-2025-paper/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1804, \"height\": 300, \"label\": \"Table\"}]"
motivation: 现有场景重建方法难以渲染新颖轨迹，限制了闭环仿真的真实感。
method: 采用在线恢复策略，将世界模型知识逐步注入NeRF/3DGS重建流程。
result: 在Waymo等数据集上，ReconDreamer渲染多车道变换等新轨迹的质量显著提升。
conclusion: 整合世界模型知识可有效增强驾驶场景重建，支持更逼真的闭环仿真。
---

## Abstract
Closed-loop simulation is crucial for end-to-end autonomous driving. Existing sensor simulation methods (e.g., NeRF and 3DGS) reconstruct driving scenes based on conditions that closely mirror training data distributions. However, these methods struggle with rendering novel trajectories, such as lane changes. Recent work, DriveDreamer4D, has demonstrated that integrating world model knowledge alleviates these issues. Although the training-free integration approach is efficient, it still struggles to render larger maneuvers, such as multi-lane shifts.Therefore, we introduce ReconDreamer, which enhances driving scene reconstruction through incremental integration of world model knowledge. Specifically, based on the world model, DriveRestorer is proposed to mitigate ghosting artifacts via online restoration. Additionally, we propose the progressive data update strategy to ensure high-quality rendering for larger maneuvers. Notably, ReconDreamer is the first method to effectively render in large maneuvers (e.g., across multiple lanes, spanning up to 6 meters). Additionally, experimental results demonstrate that ReconDreamer outperforms Street Gaussians in the NTA-IoU, NTL-IoU, and FID, with a relative improvement by 24.87%, 6.72%, and 29.97%. Furthermore, ReconDreamer surpasses DriveDreamer4D with PVG during large maneuver rendering, as verified by a relative improvement of 195.87% in the NTA-IoU metric and a comprehensive user study.

---

## 论文详细总结（自动生成）

# ReconDreamer 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **背景**：端到端自动驾驶中的闭环仿真至关重要，需要能够渲染新轨迹（如变道）的高质量动态场景重建。现有基于 NeRF 和 3DGS 的方法严重依赖训练数据分布，无法良好处理新视角，尤其是大幅度的驾驶机动（如跨多车道偏移达 6 米）。
- **问题**：尽管 DriveDreamer4D 通过无训练地利用预训练世界模型改善了部分情况，但在更大机动场景下（如多车道切换）仍存在严重重影伪影和时空不一致。
- **目标**：提出 ReconDreamer，通过**在线恢复**（Online Restoration）的方式逐步整合世界模型知识，首次实现大规模机动下的高质量场景重建，提升闭环仿真真实感。

## 2. 方法论：核心思想、关键技术细节、算法流程

### 核心思想
- 将预训练的世界模型作为数据生成器，但不是直接生成新轨迹视图，而是**在线修复**由稀疏数据导致的伪影，并**渐进式**地扩展训练数据，逐步适应更大视角偏移。
- 关键组件：**DriveRestorer**（用于伪影消除的在线恢复网络）和**渐进式数据更新策略**（Progressive Data Update Strategy, PDUS）。

### 关键技术细节
1. **DriveRestorer**：
   - 基于世界模型（如 DriveDreamer-2）微调，将渲染出的低质量新轨迹视频作为输入，结合结构条件（3D 框、HDMap）和掩码（重点恢复远处和天空边界），通过扩散去噪过程恢复高质量视频。
   - 训练数据构建：使用未完全训练的 3DGS 模型沿原始轨迹渲染出带有重影伪影的视频，与真实视频配对；并从不同训练阶段采样以增加多样性。
   - 损失函数：扩散损失 \( L_R = E_{z,\epsilon,t} \|\epsilon_t - \epsilon_\theta(z_t, t, c)\|_2^2 \)，其中条件 c 包含掩码后的退化视频、3D 框、HDMap。

2. **渐进式数据更新策略（PDUS）**：
   - 逐步增大新轨迹的偏移距离（从较小偏移开始，如 1.5m，3m，6m），每次使用 DriveRestorer 修复当前偏移的视频，并按照采样概率 \( w = k / \sum_{j=1}^k j \) 更新混合训练数据集。
   - 混合数据集由原始轨迹数据（50%）和修复后的新轨迹数据（50%）组成，同时优化场景重建模型，以保留历史有用信息并逐步适应更大机动。
   - 训练损失：原始轨迹使用 RGB/深度/SSIM 损失，新轨迹使用 RGB/SSIM 损失（避免深度噪声）。

### 算法流程（文字说明）
1. 初始化场景重建模型 G（如 Street Gaussians）和空的新轨迹数据集 \( D_{novel} \)。
2. 在每次更新步 S 中，将当前偏移距离扩大到 \( k\Delta y \)（\(\Delta y=1.5m\)），渲染新轨迹视频 \( \hat{V}_{novel} \)。
3. DriveRestorer 修复得到 \( V_{novel} \)。
4. 按公式 \( D_{novel} = (1-w) \cdot D_{novel} \cup w \cdot V_{novel} \) 更新数据集。
5. 用混合数据集 \( D = 0.5D_{ori} \cup 0.5D_{novel} \) 继续训练 G。
6. 重复直到最大偏移距离达到目标（如 6m）且模型收敛。

## 3. 实验设计：数据集、Benchmark、对比方法

### 数据集
- **Waymo**：8 个复杂场景（多车辆、多车道），用于主要定量对比。
- **nuScenes**：8 个包含动态对象和复杂车道结构的场景，用于泛化性验证。
- **PandaSet**：10 个场景（同 UniSim 设置），用于公平比较。

### Benchmark
- 评估新轨迹视图：**横向偏移 3m**、**横向偏移 6m**（大机动）、**车道变换**（换到平行车道）。
- 指标：NTA-IoU（新轨迹前景车辆 IoU）、NTL-IoU（新轨迹车道线 IoU）、FID，外加用户调研。

### 对比方法
- 场景重建基线：PVG、S3Gaussian、Deformable-GS、Street Gaussians。
- 世界模型增强方法：DriveDreamer4D（分别与 PVG、S3Gaussian、Deformable-GS 结合）。
- 消融实验：比较不同 DriveRestorer backbone（Stable Diffusion、Stable Video Diffusion、DriveDreamer-2 带/不带掩码）；不同 PDUS 步长（0.5m、1m、1.5m、3m、6m）。

## 4. 资源与算力

- **文中未明确说明使用的 GPU 型号、数量与训练时长**。仅提及“训练 40000-50000 次迭代，使用 40 帧前视相机数据”。未提供硬件配置信息。（例如，未如某些论文说明“4块 A100 训练 3 天”）。

## 5. 实验数量与充分性

### 实验组数
- **主要定量实验**：表 1、表 2 分别针对不同基线（4 种）和 DriveDreamer4D 组合（3 种）在 3 种新轨迹上报告 NTA-IoU、NTL-IoU、FID，共 7 种对比 × 3 轨迹 × 3 指标。
- **跨数据集验证**：表 3（nuScenes 6m 偏移）、表 4（PandaSet 多种偏移）。
- **消融实验**：表 6（5 种 backbone 配置）、表 7（5 种 stride 设置）。
- **用户研究**：表 5（9 种条件 win rate）。
- **定性示例**：图 6 展示直观对比。

### 充分性评估
- **充分**：覆盖主流动态场景重建方法，包含多数据集和多轨迹难度；消融实验验证了 DriveRestorer 和 PDUS 的关键设计；用户研究提供了主观证据。
- **客观性**：指标选择合理（车辆/车道 IoU + 图像质量 FID），且对比方法均为 SOTA，实验设置一致。
- **公平性**：与 DriveDreamer4D 对比时，均使用相同的底层重建方法（PVG、S3Gaussian、Deformable-GS）；PDUS 的步长调优验证了最佳配置。

## 6. 论文的主要结论与发现

- ReconDreamer 首次实现**高达 6m 的多车道偏移渲染**，在 Waymo 上相较于 Street Gaussians 在 NTA-IoU、NTL-IoU、FID 上分别提升 **24.87%**、6.72%、29.97%。
- 相较于 DriveDreamer4D（基于 PVG），在大机动（6m 偏移）下 NTA-IoU 提升 **195.87%**；用户研究中以 96.88% 胜率优于 DriveDreamer4D。
- DriveRestorer 基于 DriveDreamer-2 加掩码微调效果最佳，且 PDUS 步长设为 1.5m 时性能最优。
- 在 nuScenes 和 PandaSet 上均取得显著改进，验证了泛化性。

## 7. 优点

- **创新性**：首次将**在线恢复**与**渐进式数据更新**引入驾驶场景重建，有效弥合生成数据与真实数据之间的差距，突破了大机动渲染的瓶颈。
- **技术完整性**：从训练数据构建（未训练模型渲染配对）、恢复网络设计、到渐进式训练策略形成闭环，逻辑连贯。
- **实验全面**：涵盖多数据集、多种基线、消融实验及用户调研，结论可靠。
- **可操作性**：方法泛化性强，可基于多种 3DGS 框架（Street Gaussians、PVG、S3Gaussian、Deformable-GS）扩展。
- **应用价值**：直接提升闭环仿真的真实感，对于自动驾驶安全验证具有重要意义。

## 8. 不足与局限

- **算力信息缺失**：未提供 GPU 型号、数量及训练时间，难以评估实际计算成本与可复现性。
- **仅使用前视相机**：文中仅使用前视相机 40 帧序列，未验证多相机（环视）下的效果，限制了在真正封闭仿真中的扩展性。
- **对世界模型依赖**：DriveRestorer 需要高质量的世界模型（如 DriveDreamer-2）作为 backbone，若该模型本身存在偏差或失败场景，可能影响恢复效果。
- **轨迹采样限制**：仅测试横向偏移和单次变道，未评估更复杂的纵向/俯仰/滚动等姿态变化或连续随机轨迹。
- **场景多样性有限**：Waymo/nuScenes/PandaSet 虽具代表性，但多样性仍不及真实开放道路（如雨夜、近距离切割、极端车流等）。
- **指标覆盖性**：NTA-IoU 和 NTL-IoU 依赖预训练的检测/分割模型，可能引入额外噪声；FID 衡量全局分布，对局部伪影敏感性不足。

（完）
