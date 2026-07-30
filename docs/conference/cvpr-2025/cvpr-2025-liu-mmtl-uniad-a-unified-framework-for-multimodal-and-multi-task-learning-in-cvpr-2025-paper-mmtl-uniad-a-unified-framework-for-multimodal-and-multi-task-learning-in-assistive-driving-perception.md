---
title: "MMTL-UniAD: A Unified Framework for Multimodal and Multi-Task Learning in Assistive Driving Perception"
title_zh: MMTL-UniAD：辅助驾驶感知中多模态多任务学习的统一框架
authors: "Liu, Wenzhuo, Wang, Wenshuo, Qiao, Yicheng, Guo, Qiannan, Zhu, Jiayin, Li, Pengfei, Chen, Zilong, Yang, Huiming, Li, Zhiwei, Wang, Lening, Tan, Tiao, Liu, Huaping"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Liu_MMTL-UniAD_A_Unified_Framework_for_Multimodal_and_Multi-Task_Learning_in_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 4.0
evidence: 驾驶员行为识别，与驾驶员行为轨迹预测相关
tldr: 现有辅助驾驶系统通常忽略不同感知任务之间的联合学习潜力。本文提出MMTL-UniAD统一多模态多任务学习框架，同时识别驾驶员行为（如环顾）、驾驶员情绪、车辆行为和交通上下文。通过引入多轴区域模块和任务特定适配器缓解负迁移问题。实验表明联合训练提升了各任务表现，为理解驾驶场景提供了更全面的感知基础。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-liu-mmtl-uniad-a-unified-framework-for-multimodal-and-multi-task-learning-in-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 829, \"height\": 457, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-liu-mmtl-uniad-a-unified-framework-for-multimodal-and-multi-task-learning-in-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 876, \"height\": 448, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-liu-mmtl-uniad-a-unified-framework-for-multimodal-and-multi-task-learning-in-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 874, \"height\": 301, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-liu-mmtl-uniad-a-unified-framework-for-multimodal-and-multi-task-learning-in-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1707, \"height\": 516, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-liu-mmtl-uniad-a-unified-framework-for-multimodal-and-multi-task-learning-in-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 865, \"height\": 724, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liu-mmtl-uniad-a-unified-framework-for-multimodal-and-multi-task-learning-in-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1811, \"height\": 1204, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liu-mmtl-uniad-a-unified-framework-for-multimodal-and-multi-task-learning-in-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 870, \"height\": 255, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liu-mmtl-uniad-a-unified-framework-for-multimodal-and-multi-task-learning-in-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 871, \"height\": 462, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liu-mmtl-uniad-a-unified-framework-for-multimodal-and-multi-task-learning-in-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 868, \"height\": 246, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liu-mmtl-uniad-a-unified-framework-for-multimodal-and-multi-task-learning-in-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 869, \"height\": 260, \"label\": \"Table\"}]"
motivation: 现有辅助驾驶系统忽视多任务联合学习的潜力，缺乏统一的感知框架。
method: 构建多模态多任务学习框架，设计多轴区域模块和任务适配器以缓解负迁移。
result: 联合学习提升驾驶员行为、情绪、车辆行为及交通上下文识别性能。
conclusion: 统一的多任务学习框架有效增强辅助驾驶场景的全面感知能力。
---

## Abstract
Advanced driver assistance systems require a comprehensive understanding of the driver's mental/physical state and traffic context but existing works often neglect the potential benefits of joint learning between these tasks. This paper proposes MMTL-UniAD, a unified multi-modal multi-task learning framework that simultaneously recognizes driver behavior (e.g., looking around, talking), driver emotion (e.g., anxiety, happiness), vehicle behavior (e.g., parking, turning), and traffic context (e.g., traffic jam, traffic smooth). A key challenge is avoiding negative transfer between tasks, which can impair learning performance. To address this, we introduce two key components into the framework: one is the multi-axis region attention network to extract global context-sensitive features, and the other is the dual-branch multimodal embedding to learn multimodal embeddings from both task-shared and task-specific features. The former uses a multi-attention mechanism to extract task-relevant features, mitigating negative transfer caused by task-unrelated features. The latter employs a dual-branch structure to adaptively adjust task-shared and task-specific parameters, enhancing cross-task knowledge transfer while reducing task conflicts. We assess MMTL-UniAD on the AIDE dataset, using a series of ablation studies, and show that it outperforms state-of-the-art methods across all four tasks. The code is available on https://github.com/Wenzhuo-Liu/MMTL-UniAD.

---

## 论文详细总结（自动生成）

# MMTL-UniAD 论文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：现有高级辅助驾驶系统（ADAS）在感知驾驶员状态（行为、情绪）和交通上下文（车辆行为、交通场景）时，通常将其作为独立任务处理，忽略了这些任务之间的因果关联和联合学习潜力。例如，交通拥堵可能引发驾驶员焦虑，进而影响驾驶行为。此外，现有方法多依赖单一模态输入（仅驾驶场景或仅驾驶员图像），未能充分利用多模态信息（多视角图像、驾驶员面部/身体图像、姿态/手势关节数据）的互补性。
- **整体含义**：本文提出统一框架**MMTL-UniAD**，旨在通过多模态多任务联合学习，同时识别驾驶员行为、驾驶员情绪、车辆行为和交通上下文，增强ADAS对复杂驾驶场景的全面理解，提升安全性和适应性。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：为了避免多任务学习中的负迁移（即弱相关任务间的信息共享导致性能下降），设计两个关键模块：
  - **多轴区域注意力网络（MARNet）**：用于从多视角图像中提取全局上下文敏感且任务相关的特征，抑制无关特征（如路标、车内装饰）带来的干扰。
  - **双分支多模态嵌入（DBME）**：通过软参数共享，自适应地提取任务共享特征和任务特定特征，平衡跨任务知识传递与任务间冲突。
- **关键技术细节**：
  - **MARNet**：由水平-垂直注意力（H-V Attention）和区域注意力（Region Attention）组成。水平-垂直注意力沿水平和垂直方向分别计算自注意力，捕获长程依赖；区域注意力将特征图划分为t×t区域，通过相似性选择k个最相关区域进行注意力计算，聚焦动态目标（如车辆、行人）。
  - **DBME**：含两个分支：
    - **任务特定分支**：对拼接后的多模态特征进行全局平均池化，通过1D卷积和多头自注意力生成通道权重，抑制无关模态信息，输出任务特定特征 \(F_{sp}^j\)。
    - **任务共享分支**：将交通相关特征（前/左/右视图）与驾驶员相关特征（内部视图、面部、身体）通过多尺度卷积融合，再与手势/姿态关节特征进行软参数共享，得到共享特征 \(F_{sh}\)。
    - 最终各任务输出通过动态融合：\(O_j = \sigma(w_j) L_j^1(F_{sh}) + (1-\sigma(w_j)) L_j^2(w_{ca}(F_{sp}^j))\)，其中 \(w_j\) 可学习控制共享/特定特征的比重。
  - **损失函数**：四个任务的交叉熵损失之和。

## 3. 实验设计
- **数据集**：AIDE数据集（2898个样本），包含多视角视频（前、右、左、内景）、驾驶员面部/身体图像、手势/姿态关节数据，标注了四个任务（驾驶员情绪、驾驶员行为、交通上下文、车辆行为）。划分：65%训练、15%验证、20%测试。
- **基准方法**：按照特征提取维度分为三类：
  - **2D**：ResNet、VGG、CPVT、CMT、GroupMixFormer、AbSViT、GLMDriveNet等，结合MLP+SE或ST-GCN进行多模态融合。
  - **2D+Timing**：在上述2D骨干后加入Transformer编码器处理时序信息。
  - **3D**：MobileNet、ShuffleNet、3D-ResNet、C3D、I3D、SlowFast、TimeSFormer、Video Swin Transformer等，结合ST-GCN或3DCNN。
- **对比方法**：列表详细，共约20+种不同配置。本文方法使用MARNet提取多视角图像特征，3DCNN提取关节数据，DBME进行多任务融合。

## 4. 资源与算力
- **文中明确提及**：所有实验在一块NVIDIA A40 GPU上进行，batch size=24，训练125个epoch，学习率0.1，使用SGD优化器（momentum=0.9，weight decay=0.0001）。
- **未说明**：未提及具体训练时长（小时/天），也未说明是否使用多卡并行或更多算力资源。实验规模中等，A40单卡足够完成。

## 5. 实验数量与充分性
- **主要实验**：
  - **Table 1**：与21种基线方法对比（含多配置），在四个任务上均取得最佳mAcc（82.30%），比第二名（78.16%）提升4.14%。
  - **消融实验**：
    - 多任务学习必要性的两组实验（表2、表3）：对比联合训练、单任务、移除某一任务，验证了正迁移。
    - 关键组件消融（表4）：去除MARNet或DBME，mAcc下降5.34%-12.05%。
    - 多模态数据消融（表5）：仅使用面部+身体、仅关节、仅场景，mAcc分别下降5.39%、26.61%、4.17%，证明多模态的必要性。
- **充分性评估**：实验设计全面，覆盖了模型组件、数据模态、任务组合三个维度，对比基线丰富，A/B测试公平（控制变量）。但仅在单一数据集（AIDE）上验证，缺乏跨数据集泛化实验，存在一定的外部效度风险。

## 6. 主要结论与发现
- 提出的MMTL-UniAD框架在四个感知任务上均超过所有基线方法，mAcc达82.30%，尤其在驾驶员行为（73.61%）和车辆行为（85.00%）上显著领先。
- 多任务联合学习比单任务或部分任务组合能带来显著性能提升（表2、表3），证明驾驶员状态和交通上下文任务之间存在有益的信息互补。
- MARNet通过方向性注意力和区域注意力有效提取任务相关特征，DBME通过双分支结构平衡共享与特定特征，二者协同缓解了负迁移。
- 多模态数据（图像+关节）是达到最优性能的必要条件，单一模态会造成较大性能下降。

## 7. 优点
- **方法创新性**：首次在辅助驾驶感知中提出统一的多模态多任务框架，专门设计了应对负迁移的模块，具有明确的理论动机。
- **设计精巧**：MARNet结合水平-垂直注意力和区域注意力，兼顾全局上下文和局部动态目标；DBME采用软参数共享和动态融合，灵活性高。
- **实验充分、结果坚实**：与多种主流方法（2D/2D+时序/3D）对比，消融实验细致，验证了每个组件和模态的贡献。
- **开源代码**：提供GitHub仓库，便于复现和后续研究。

## 8. 不足与局限
- **数据集局限**：仅在AIDE（约3000样本）上评估，数据规模较小，且场景单一（可能来自模拟或特定采集）。缺乏在更大规模真实驾驶数据集（如Drive&Act、HRI30）上的泛化验证，存在过拟合风险。
- **任务定义**：四个任务均为分类问题，未涉及回归或细粒度预测（如连续情绪值、精确车辆轨迹），实用性受限。
- **计算开销**：未分析模型参数量、推理速度或实时性，作为ADAS感知模块需满足实时性，但文中未评估。
- **偏差风险**：驾驶员情绪和行为样本分布可能不均衡（如正常驾驶情况远多于异常情况），但文中未讨论类别平衡或长尾问题。
- **可扩展性**：当前框架仅支持四个预定义任务，新增任务可能需要重新设计任务特定分支，未探讨在线学习或任务增量方案。

（完）
