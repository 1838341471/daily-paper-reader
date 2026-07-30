---
title: "S4-Driver: Scalable Self-Supervised Driving Multimodal Large Language Model with Spatio-Temporal Visual Representation"
title_zh: S4-Driver：可扩展的自监督驾驶多模态大语言模型与时空视觉表示
authors: "Xie, Yichen, Xu, Runsheng, He, Tong, Hwang, Jyh-Jing, Luo, Katie, Ji, Jingwei, Lin, Hubert, Chen, Letian, Lu, Yiren, Leng, Zhaoqi, Anguelov, Dragomir, Tan, Mingxing"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Xie_S4-Driver_Scalable_Self-Supervised_Driving_Multimodal_Large_Language_Model_with_Spatio-Temporal_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 8.0
evidence: 基于时空视觉表示的MLLM端到端运动规划
tldr: 端到端运动规划常依赖人工标注，且MLLM预训练在2D空间，与自动驾驶的3D规划不匹配。本文提出S4-Driver，采用自监督方式直接学习传感器输入到规划轨迹，并引入3D时空视觉表示。该方法无需人工标注即可生成规划轨迹。实验结果显示其性能优于现有自监督方法，接近有监督方法。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 848, \"height\": 513, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1692, \"height\": 780, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 764, \"height\": 775, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 770, \"height\": 247, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 862, \"height\": 270, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 848, \"height\": 529, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 848, \"height\": 391, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 865, \"height\": 164, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1576, \"height\": 808, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1589, \"height\": 400, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 865, \"height\": 146, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 791, \"height\": 311, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xie-s4-driver-scalable-self-supervised-driving-multimodal-large-language-model-with-spatio-temporal-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 711, \"height\": 231, \"label\": \"Table\"}]"
motivation: 现有MLLM端到端方法在2D空间预训练，与3D规划不匹配，且依赖标注。
method: 设计自监督框架，使用3D时空视觉表示的大语言模型从传感器输入直接输出规划轨迹。
result: 在nuScenes等数据集上，S4-Driver在无标注情况下达到了与有监督方法可比的性能。
conclusion: 自监督MLLM方法可有效降低标注需求，推动端到端驾驶实用化。
---

## Abstract
The latest advancements in multi-modal large language models (MLLMs) have spurred a strong renewed interest in end-to-end motion planning approaches for autonomous driving. Many end-to-end approaches rely on human annotations to learn intermediate perception and prediction tasks, while purely self-supervised approaches--which directly learn from sensor inputs to generate planning trajectories without human annotations--often underperform the state of the art. We observe a key gap in the input representation space: end-to-end approaches built on MLLMs are often pretrained with reasoning tasks in 2D image space rather than the native 3D space in which autonomous vehicles plan. To this end, we propose S4-Driver, a scalable self-supervised motion planning algorithm with spatio-temporal visual representation, based on the popular PaLI multimodal large language model. S4-Driver uses a novel sparse volume strategy to seamlessly transform the strong visual representation of MLLMs from perspective view to 3D space without the need to finetune the vision encoder. This representation aggregates multi-view and multi-frame visual inputs and enables better prediction of planning trajectories in 3D space. To validate our method, we run experiments on both nuScenes and Waymo Open Motion Dataset (with in-house camera data). Results show that S4-Driver performs favorably against existing supervised multi-task approaches while requiring no human annotations. It also demonstrates great scalability when pretrained on large volumes of unannotated driving logs.

---

## 论文详细总结（自动生成）

# S4-Driver: 可扩展的自监督驾驶多模态大语言模型与时空视觉表示

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：端到端自动驾驶运动规划方法常依赖人工标注的中间任务（感知、预测），而纯自监督方法性能不足。关键问题在于：现有MLLM的视觉预训练在2D图像空间中进行，与自动驾驶所需的3D空间规划不匹配，导致模型难以在3D场景中进行有效推理。
- **背景意义**：多模态大语言模型（MLLM）在通用视觉理解上表现出色，但直接用于3D运动规划效果不佳。现有方案通过多任务学习或链式思维推理来弥补，但依赖昂贵的人工标注。S4-Driver旨在实现纯自监督的端到端运动规划，仅需原始传感器数据和自车轨迹，无需任何人工标注，且能利用大规模未标注驾驶数据进行拓展。

## 2. 方法论：核心思想、关键技术细节、算法流程

- **核心思想**：在MLLM（基于PaLI）基础上，提出**稀疏体积表示（Sparse Volume Representation）**，将多视角、多帧图像特征从透视视图转换到3D空间，增强模型的3D时空推理能力，直接输出自车未来轨迹。
- **关键技术细节**：
  - **基线与改进**：使用PaLI模型作为基础规划器，输入多视角图像、历史自车状态、高层行为命令，输出轨迹。在此基础上逐步添加：
    - **层次化规划与元决策**：先预测高层行为（保持静止、保持速度、加速、减速），再预测具体数值轨迹，无需额外标注（通过启发式规则生成标签）。
    - **3D视觉表示（稠密体积）**：对每个体素，将其3D坐标投影到各视角，双线性采样特征并取平均，加上位置编码构建3D体积特征。
    - **稀疏体积表示**：通过一个小型MLP计算每个体素的“门控值”，选择门控值最大的M个体素（M远小于总体素数），结合可学习的空体素特征，聚焦重要区域，提升效率。
    - **局部特征聚合**：在自注意力中引入基于3D相对位置偏置（沿xyz轴分箱的可学习偏置），增强局部信息融合。
    - **多帧时间融合**：利用历史T帧（间隔0.5s），对每帧分别构建门控体积特征，经自车运动补偿后拼接，再通过FC层融合为含时间信息的稀疏体积特征。
    - **多解码投票**：使用核采样生成K个轨迹，简单平均得到最终结果，缓解模型偏向简单行为（如静止）的问题。
  - **无需微调视觉编码器**：稀疏体积策略仅基于冻结的ViT输出特征，不修改视觉编码器，保持预训练知识。
- **算法流程**（文字描述）：
  1. 输入：多帧多视角图像、历史自车状态（位置、速度、加速度）、高层行为命令。
  2. 视觉编码器（冻结）提取各帧各视图2D特征。
  3. 对每帧计算降维后的门控特征，构建3D门控体积，获得每个体素的门控值。
  4. 选取M个门控值最大的体素作为稀疏体积，从各帧特征中采样语义特征，与空体素特征加权融合，加上位置编码。
  5. 将稀疏体积特征与文本令牌（历史状态、命令等）拼接，输入多模态编码器（含3D相对位置偏置的自注意力）。
  6. 解码器先预测元决策，再基于元决策预测数值轨迹。
  7. 通过核采样生成K个轨迹，取平均作为最终规划结果。

## 3. 实验设计：数据集、基准、对比方法

- **数据集**：
  - **WOMD-Planning-ADE**（基于Waymo Open Motion Dataset）：约103k序列（574小时），10Hz频率，5s规划视野，含多视角相机图像、自车轨迹、高层行为命令。比nuScenes大100倍。
  - **nuScenes**：标准端到端规划基准（1k序列，5.5小时，2Hz，3s规划）。
- **基准（WOMD-Planning-ADE）**：提出行为级指标（bADE），对7种行为（6种高层命令+停歇）分别计算ADE再取平均，弥补样本级指标（如整体ADE）对罕见行为的忽视。
- **对比方法**：
  - 在nuScenes上对比：多任务方法（UniAD, VAD, PARA-Drive）、MLLM方法（GPT-Driver, DriveVLM, OmniDrive）、自监督方法（DriveVLM w/o CoT）。
  - 在WOMD-Planning-ADE上对比：Vanilla PaLI基线、MotionLM（利用高质量物体/轨迹/道路图作为输入）。
  - 额外对比不同MLLM（PaLI2-3B vs PaLI3-5B）、不同数据规模、不同稀疏体积分辨率等消融实验。

## 4. 资源与算力

- 文中明确提到：**使用128个Google Cloud TPU v4**，batch size 256，学习率3e-3，微调整个WOMD-Planning-ADE数据集约需**2.5天**。视觉编码器ViT-G（2B参数）冻结，仅微调插入模块和多模态编码器-解码器（3B参数）。未提供能源消耗或成本细节。

## 5. 实验数量与充分性

- **实验组数**：涵盖多个维度：
  - 主结果（nuScenes Tab.2，WOMD-Planning-ADE Tab.3）。
  - 逐步增强的消融（图3：逐步加入元决策、稠密体积、稀疏体积、局部偏置、时间融合、多解码、大规模预训练）。
  - 输入消融（Tab.5：有无历史状态、有无图像、有无MLLM预训练）。
  - 模型与数据规模（Tab.4：PaLI2 vs PaLI3，20k vs 400k数据）。
  - 稀疏体积分辨率（Tab.6：不同xyz网格大小）。
  - 元决策可靠性分析（图7：各行为准确率）。
  - 稀疏体积分布可视化（图8）。
  - 定性结果（图6多种场景）。
- **公平性与充分性**：对比方法覆盖主流范式（多任务、MLLM、自监督），在nuScenes上S4-Driver使用完全相同的数据（无额外标注），在WOMD-Planning-ADE上对比的MotionLM使用了更丰富的输入（物体/轨迹），但S4-Driver仍表现更好，说明具有竞争力。消融实验系统分析了每个模块的贡献。数据集规模大（WOMD-Planning-ADE），避免小数据集过拟合。总体实验充分、客观。

## 6. 主要结论与发现

- S4-Driver在nuScenes上超越所有现有自监督方法，且与使用监督信号的多任务方法性能相当甚至更优（L2误差0.31m@3s，比OmniDrive的0.29m稍高，但OmniDrive使用了标注数据；S4-Driver预训练后达到0.31m）。
- 在WOMD-Planning-ADE上，S4-Driver在行为级指标（bADE）上显著优于Vanilla PaLI，且优于使用额外输入的MotionLM（bADE@5s: 0.830 vs 0.978）。
- 大规模无标注数据预训练可显著提升性能（图1a、Tab.3中带*版本）。
- 各模块（元决策、稀疏体积、局部偏置、时间融合、多解码）均有正向贡献（图3）。
- 稀疏体积分布符合驾驶经验（聚焦前方近处，左右覆盖但中间为主）。
- 元决策预测准确率高，可简化数值轨迹预测。

## 7. 优点

- **自监督与可扩展性**：完全无需人工标注，可直接利用海量未标注驾驶日志进行规模扩展，降低数据成本。
- **有效的3D时空表示**：稀疏体积策略轻量、无需微调视觉编码器，通过门控机制聚焦重要区域，结合3D相对位置偏置实现局部信息聚合，增强了MLLM的3D推理能力。
- **层次化规划与无额外标注的元决策**：将语义粗决策与数值细轨迹分离，且元决策标签可通过启发式规则自动生成。
- **行为级评估指标**：提出bADE，更公平评价算法在稀疏但关键行为（如转弯）上的表现。
- **强基线性能**：在多个基准上达到SOTA或可比性能，验证了自监督MLLM规划路线的潜力。

## 8. 不足与局限

- **实验覆盖有限**：仅在nuScenes和Waymo内部数据集上验证，未在CARLA等闭环仿真器或真实道路闭环测试中评估。闭环性能未知。
- **偏差风险**：元决策的“停歇”行为标签可能泄露未来信息（文中已说明未将其作为高层命令输入）。行为级指标虽好，但仅基于7种行为，未覆盖更细粒度场景。
- **应用限制**：
  - 需自车历史状态作为输入，若状态噪声大可能影响性能。
  - 稀疏体积分辨率选择对性能有影响（Tab.6），需调参。
  - 模型规模大（5B参数），推理成本高，实时部署可能困难。
  - 方法仅在PaLI系列上验证，对其他MLLM（如GPT-4V）的兼容性未证明。
- **消融实验细节不足**：仅报告了部分模块组合结果，未深入分析每种技术的交互作用（如多解码与稀疏体积的叠加效果）。
- **对比公平性**：在WOMD-Planning-ADE上，MotionLM使用高精度离线标注的物体/轨迹/地图，而S4-Driver仅用原始图像，但性能更优——这虽体现优势，但未进行严格的公平对照（如给MotionLM相同输入）。

（完）
