---
title: Leveraging SD Map to Augment HD Map-based Trajectory Prediction
title_zh: 利用SD地图增强基于HD地图的轨迹预测
authors: "Dong, Zhiwei, Ding, Ran, Li, Wei, Zhang, Peng, Tang, Guobin, Guo, Jia"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Dong_Leveraging_SD_Map_to_Augment_HD_Map-based_Trajectory_Prediction_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 9.0
evidence: 利用SD地图增强轨迹预测
tldr: 基于HD地图的轨迹预测模型受感知误差和特征冗余影响。本文提出SATP框架，利用SD地图增强HD地图轨迹预测。首先设计SD-HD融合方法，使SD地图兼容多种预测模型；其次提出AlignNet对齐两种地图。在多个基准上显著提升了轨迹预测精度，尤其在感知错误场景下更具鲁棒性。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 862, \"height\": 502, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 832, \"height\": 234, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1783, \"height\": 686, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1781, \"height\": 384, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1807, \"height\": 498, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 809, \"height\": 580, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1806, \"height\": 514, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 869, \"height\": 339, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 886, \"height\": 334, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 868, \"height\": 343, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 871, \"height\": 204, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-dong-leveraging-sd-map-to-augment-hd-map-based-trajectory-prediction-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 859, \"height\": 251, \"label\": \"Table\"}]"
motivation: 在线HD地图存在感知误差和特征冗余，影响轨迹预测性能。
method: 提出SD地图与HD地图融合方法，并设计AlignNet对齐特征。
result: 在多个数据集上提升轨迹预测精度，对感知错误鲁棒。
conclusion: SATP证明了SD地图可作为HD地图的有效补充，提升轨迹预测可靠性。
---

## Abstract
Latest trajectory prediction models in real-world autonomous driving systems often rely on online High-Definition (HD) maps to understand the road environment.However, online HD maps suffer from perception errors and feature redundancy, which hinder the performance of HD map-based trajectory prediction models.To address these issues, we introduce a framework, termed SD map-Augmented Trajectory Prediction (SATP), which leverages Standard-Definition (SD) maps to enhance HD map-based trajectory prediction models.First, we propose an SD-HD fusion approach to leverage SD maps across the diverse range of HD map-based trajectory prediction models. Second, we design a novel AlignNet to align the SD map with the HD map, further improving the effectiveness of SD maps. Experiments on real-world autonomous driving benchmarks demonstrate that SATP not only improves the performance of HD map-based trajectory prediction up to 25% in real-world scenarios using online HD maps but also brings benefits in ideal scenarios with ground-truth HD maps.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究背景**：轨迹预测是自动驾驶的关键任务之一，现有主流方法依赖高精度（HD）地图来理解道路环境。HD 地图包含车道、人行横道等精细信息，但其构建和维护成本极高。
- **实际问题**：在实际部署中，多数系统使用在线 HD 地图（由车载传感器实时构建），这引入了两个主要问题：
  - **感知误差**：传感器限制或遮挡导致地图元素错误或缺失。
  - **特征冗余**：HD 地图包含过多细节，缺乏紧凑描述，降低模型学习效率。
- **核心动机**：标准定义（SD）地图（如 OpenStreetMap）虽然仅提供道路级骨架，但由人工离线制作，精度可靠且全局覆盖免费；其简洁的道路骨架能纠正 HD 地图的感知误差，并提供紧凑的环境线索。因此，本文提出利用 SD 地图增强 HD 地图轨迹预测。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：将 SD 地图信息以与基线模型利用 HD 地图相同的方式整合进轨迹预测流程，实现 SD-HD 融合，并设计对齐网络解决地图间错位问题。
- **整体框架 (SATP)**：包含两个主要组件：
  1. **SD-HD 融合 (SD-HD Fusion)**：
     - 分析主流 HD 地图轨迹预测模型（如 HiVT、DenseTNT、QCNet）共有的两步流程：HD 地图编码 → HD 特征提取。
     - 对基线模型的对应模块进行“模型缩小”（减少层数和通道数），构建 SD 地图编码和 SD 特征提取模块，保证特征兼容性并减少参数量。
     - 通过可学习的自适应加权融合两类查询（Q_H 和 Q_S），得到融合特征用于最终轨迹预测。公式：  
       \( w_i = \text{Sigmoid}(\text{MLP}(\text{Concat}(Q_H^i, Q_S^i))) \)  
       \( Q_F^i = (1 - w_i) \cdot Q_H^i + w_i \cdot Q_S^i \)
     - 在三个代表性基线模型上给出具体实现：
       - **HiVT**：缩小 Agent-Lane Interaction 模块为 Agent-SD Interaction。
       - **DenseTNT**：缩小 Context Encoder 和 Dense Goal Encoder。
       - **QCNet**：缩小 Agent-Lane Encoder 和 Mode-Map Cross-Attention。
  2. **AlignNet（对齐网络）**：
     - 解决 SD 地图与 HD 地图之间的错位（由车辆定位误差或 SD 地图精度不足引起）。
     - 对 HD 和 SD 地图采样稀疏关键点（5m 间隔 + 拐点），用轻量 2D Point Transformer 提取局部结构特征，通过全局平均池化得到全局特征；拼接后经 MLP 预测相对旋转角 θ 和平移 t。
     - 不直接监督 θ 和 t，而是通过最终轨迹预测损失进行端到端优化（因在线 HD 地图有感知误差，无法获得精确真值姿态）。
     - 使用 sigmoid 激活限制 θ 在 [-π, π] 范围，简化学习。

## 3. 实验设计

- **数据集**：
  - **nuScenes**：1000 个场景，每个 20 秒，采样频率提升后用于预测 2 秒历史→3 秒未来轨迹。HD 地图结构来自数据集的离线真值 HD 地图。
  - **Argoverse2**：25 万个场景，6 个城市，5 秒历史→6 秒未来轨迹。
- **评测指标**：minADE₆、minFDE₆、MR₆（FDE>2m 为 Miss），简化表示为 ADE、FDE、MR。
- **对比方法**：
  - 在线 HD 地图构建模型：MapTRv2、HRMapNet。
  - 轨迹预测基线模型：HiVT、DenseTNT、QCNet。
  - 消融对标：不带 AlignNet、CNN 对齐、顺序融合（SD→HD 和 HD→SD）。
  - 额外对比：使用 SD 增强在线 HD 地图构建的方法（P-MapNet 融合到 MapTRv2）。
  - 端到端自动驾驶：VAD-tiny。
- **实验设置**：
  - 先训练在线 HD 地图构建模型，生成在线 HD 地图，再训练轨迹预测模型（使用生成的地图作为输入）。
  - 在 nuScenes 上测试三组轨迹预测基线配合不同在线 HD 地图输入（MapTRv2、HRMapNet）以及真值 HD 地图。
  - 在 Argoverse2 中无 RGB/激光雷达数据，故对真值 HD 地图加噪声并随机删除元素模拟在线地图误差。
  - 端到端实验在 nuScenes 验证集上进行。

## 4. 资源与算力

- **文中明确说明**：所有轨迹预测模型均在单张 V100 GPU 上进行训练和测试。
- 未给出训练时长和具体 GPU 数量（仅提及单卡）。所有训练配置（包括在线 HD 地图模型和轨迹预测模型）均与官方实现一致。

## 5. 实验数量与充分性

- **实验组数**：
  - 主表 (Table 1)：nuScenes 上 3 种基线 × 5 种地图输入（SD、MapTRv2、MapTRv2+SATP、MapTRv2+SATP+[8]、HRMapNet、HRMapNet+SATP、HRMapNet+SATP+[8]、GT HD、GT HD+SATP）→ 约 24 组结果。
  - Argoverse2 实验 (Table 2)：5 种条件（SD、GT+Noise、GT+Noise+SATP、GT、GT+SATP）。
  - 消融实验 (Table 3)：6 种变体（HiVT+MapTRv2 基线、+SATP、无 AlignNet、CNN 对齐、顺序融合两种）。
  - 效率实验 (Table 4)：3 种基线 vs 3 种+SATP。
  - 端到端实验 (Table 5)：VAD-tiny vs VAD-tiny+SATP。
  - 与 SD 增强 HD 地图对比 (Table 6)：4 组。
- **充分性评价**：实验覆盖全面，包括不同数据集、不同基线、不同地图输入类型（在线 vs 真值）、多种消融、效率分析、端到端任务验证。对比方法包括最新在线 HD 地图构建模型和不确定性建模方法 [8]，且使用标准公开基准。结论具有说服力和可重复性。

## 6. 主要结论与发现

1. **SATP 显著提升在线 HD 地图轨迹预测性能**：在 nuScenes 上最高提升 25%（MR 降低 25%），平均提升 ADE 9%、FDE 13%、MR 17%，使性能接近使用真值 HD 地图的水平。
2. **对真值 HD 地图也能带来改进**：在完美 HD 地图上仍有提升，证明 SD 地图的紧凑道路骨架可缓解 HD 地图的特征冗余问题。
3. **AlignNet 是提升 SD 地图有效性的关键**：无对齐时性能下降明显（接近仅使用在线 HD 地图）。
4. **2D Point Transformer 对齐优于 CNN 对齐**：由于 CNN 对精确坐标定位能力有限。
5. **并行融合优于顺序融合**：避免先后顺序导致信息遗忘。
6. **效率高**：参数量增加 ≤0.4M，推理时间增加 ≤8%。
7. **训练效率提升**：SATP 使模型收敛更快、回归损失更低（Figure 6）。

## 7. 优点

- **方法创新性**：首次系统性地将 SD 地图引入 HD 地图轨迹预测，同时解决感知误差和特征冗余两个问题；提出通用的 SD-HD 融合框架，易适配多种模型；AlignNet 无需显式对齐监督，通过轨迹损失端到端学习。
- **实验严谨性**：
  - 在多个数据集（nuScenes、Argoverse2）和多个先进基线（HiVT、DenseTNT、QCNet）上验证。
  - 包含在线 HD 地图、真值 HD 地图、噪声模拟多种条件。
  - 消融实验拆分了各个组件的影响，并与现有方法（MapTRv2、HRMapNet、P-MapNet、不确定性方法 [8]）对比。
  - 不仅考虑轨迹预测，还扩展到端到端自动驾驶任务（VAD），评估 L2 位移和碰撞率。
- **计算友好**：额外计算开销小（推理时间增 <10%），便于实际部署。
- **实用价值**：SD 地图免费全球覆盖，方法可在缺乏高精度 GPS 或在线 HD 地图存在误差的真实场景中大幅提升性能。

## 8. 不足与局限

- **未考虑 SD 地图的延迟更新错误**：论文仅假设 SD 地图静态准确，未处理道路施工、临时改道等动态变化导致的 SD 地图过期问题。
- **对齐方法的局限性**：AlignNet 仅预测刚体变换（旋转和平移），无法处理非线性变形（如局部地图扭曲）；且监督信号来自最终预测损失，可能收敛到次优对齐。
- **Argoverse2 实验依赖噪声模拟**：因缺乏传感器数据，使用加噪和删除元素模拟在线 HD 地图误差，可能与真实在线 HD 地图误差分布不完全一致。
- **实验覆盖**：仅测试了三种基线模型，未涵盖更近期的模型（如 Motion Transformer 及其变体），但框架设计具有通用性。
- **依赖车辆定位**：SD 地图的提取依赖 GPS/IMU 定位，虽在实验中加入了模拟噪声，但实际中极端定位误差可能削弱效果。
- **未讨论 SD 地图缺失或覆盖不全的场景**（如无道路区域、室内停车场等），但这类场景在自动驾驶中可能少见。

（完）
