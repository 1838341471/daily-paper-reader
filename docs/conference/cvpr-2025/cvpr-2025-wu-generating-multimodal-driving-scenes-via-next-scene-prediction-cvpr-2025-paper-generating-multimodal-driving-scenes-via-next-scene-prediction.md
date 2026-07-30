---
title: Generating Multimodal Driving Scenes via Next-Scene Prediction
title_zh: 生成多模态驾驶场景：通过下一场景预测
authors: "Wu, Yanhao, Zhang, Haoyang, Lin, Tianwei, Huang, Lichao, Luo, Shujie, Wu, Rui, Qiu, Congpei, Ke, Wei, Zhang, Tong"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Wu_Generating_Multimodal_Driving_Scenes_via_Next-Scene_Prediction_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 6.0
evidence: 为轨迹预测生成训练场景
tldr: 现有自动驾驶场景生成方法覆盖模态有限，无法全面评估系统。本文提出多模态场景生成框架，基于自回归下一场景预测，包含地图等四种模态。通过时序自回归（TAR）和有序自回归（OAR）组件分别建模帧间动态和模态内对齐。生成的多样场景可用于训练和测试轨迹预测模型，提升鲁棒性。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wu-generating-multimodal-driving-scenes-via-next-scene-prediction-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1747, \"height\": 1152, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wu-generating-multimodal-driving-scenes-via-next-scene-prediction-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1784, \"height\": 768, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wu-generating-multimodal-driving-scenes-via-next-scene-prediction-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1799, \"height\": 1036, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wu-generating-multimodal-driving-scenes-via-next-scene-prediction-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1805, \"height\": 874, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wu-generating-multimodal-driving-scenes-via-next-scene-prediction-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 849, \"height\": 985, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wu-generating-multimodal-driving-scenes-via-next-scene-prediction-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 847, \"height\": 288, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wu-generating-multimodal-driving-scenes-via-next-scene-prediction-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 847, \"height\": 526, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wu-generating-multimodal-driving-scenes-via-next-scene-prediction-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 848, \"height\": 322, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wu-generating-multimodal-driving-scenes-via-next-scene-prediction-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 898, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wu-generating-multimodal-driving-scenes-via-next-scene-prediction-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 875, \"height\": 157, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wu-generating-multimodal-driving-scenes-via-next-scene-prediction-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 864, \"height\": 200, \"label\": \"Table\"}]"
motivation: 现有场景生成方法覆盖模态有限，无法充分评估自动驾驶系统。
method: 提出包含地图模态的多模态场景序列生成框架，采用时序自回归和有序自回归组件。
result: 生成的多模态场景可用于训练和评估，提升轨迹预测等任务性能。
conclusion: 多模态场景生成为轨迹预测提供更丰富的训练数据，有助于提高模型泛化能力。
---

## Abstract
Generative models in Autonomous Driving (AD) enable diverse scenario creation, yet existing methods fall short by only capturing a limited range of modalities, restricting the capability of generating controllable scenes for comprehensive evaluation of AD systems. In this paper, we introduce a multimodal generation framework that incorporates four major data modalities, including a novel addition of the map modality. With tokenized modalities, our scene sequence generation framework autoregressively predicts each scene while managing computational demands through a two-stage approach. The Temporal AutoRegressive (TAR) component captures inter-frame dynamics for each modality, while the Ordered AutoRegressive (OAR) component aligns modalities within each scene by sequentially predicting tokens in a fixed order. To maintain coherence between map and ego-action modalities, we introduce the Action-aware Map Alignment (AMA) module, which applies a transformation based on the ego-action to maintain coherence between these two modalities. Our framework effectively generates complex, realistic driving scenes over extended sequences, ensuring multimodal consistency and offering fine-grained control over scene elements. Project page: https://yanhaowu.github.io/UMGen/

---

## 论文详细总结（自动生成）

## 论文总结：Generating Multimodal Driving Scenes via Next-Scene Prediction

### 1. 核心问题与整体含义（研究动机和背景）
- **研究动机**：现有自动驾驶场景生成方法仅覆盖有限模态（如仅生成轨迹或图像），缺乏对地图（map）模态的动态建模，导致无法生成用户可控、多模态一致的复杂场景，难以全面评估自动驾驶系统。
- **核心问题**：如何实现包含**自车动作、地图、交通参与者、图像**四种模态的**逐帧自回归生成**，并确保跨模态一致性和时间连续性。
- **整体含义**：提出统一多模态生成框架UMGen，能够生成长达60秒的多样化、可交互驾驶场景，为自动驾驶提供闭环仿真和系统测试的基石。

### 2. 方法论：核心思想、关键技术细节
- **核心思想**：将场景生成建模为**下一场景预测**任务，通过两阶段自回归分解降低计算复杂度：**时序自回归（TAR）** 处理帧间依赖，**有序自回归（OAR）** 处理帧内模态对齐。
- **关键技术细节**：
  - **Token化**：自车动作和代理属性离散化，地图和图像使用预训练VQ-GAN编码为离散token；每帧token按固定顺序排列（动作→地图→代理→图像），反映因果依赖。
  - **Token嵌入**：通过可学习码本和位置编码将token映射为统一维度特征。
  - **自车动作预测**：使用两层交叉注意力机制，基于历史动作和当前环境预测下一帧动作，作为其他模态生成的先验。
  - **动作感知地图对齐（AMA）**：将地图特征重塑为空间网格，根据预测的自车动作（旋转、平移）对地图特征进行仿射变换，使地图与自车运动对齐，增强两模态一致性。
  - **时序自回归（TAR）**：对每个token位置，使用因果自注意力仅关注**相同位置**的历史帧token，实现高效并行运算；随后通过双向自注意力进行帧内信息交换，得到粗预测特征。
  - **有序自回归（OAR）**：利用TAR得到的粗预测特征作为时间先验，结合因果自注意力**逐token**自回归解码，并使用Top-k采样生成最终token序列，确保帧内token一致性。
- **损失函数**：对OAR和TAR输出分别计算交叉熵损失，总损失为两者之和。

### 3. 实验设计
- **数据集**：
  - **nuPlan**：用于初始场景生成评估和场景序列生成测试。
  - **Waymo Open Motion Dataset (WOMD)**：用于初始场景生成评估。
- **评估指标**：
  - **MMD（Maximum Mean Discrepancy）**：衡量生成场景与真实场景在代理属性（位置、朝向、尺寸、速度）上的分布差异。
  - **碰撞率（CR, Collision Rate）**：用于评估生成场景中代理间的一致性。
  - **GPU内存使用和推理时间**：对比TAR模块与普通自回归的计算效率。
- **对比方法**：
  - 初始场景生成：TrafficGen, LCTGen, SceneGen, UniGen（在WOMD上对比）；TrafficGen（在nuPlan上对比）。
  - 模态覆盖对比：DriveDreamer, TrafficGen, GAIA-1, GUMP（定性比较表1）。
- **场景类型**：生成自车直行、转弯、变道等普通场景；用户控制的左/右转、减速、右转初速度等；以及指定前车切入等交互场景。

### 4. 资源与算力
- **训练配置**：32块 **NVIDIA RTX 4090 GPU**，训练 **300个epochs**，耗时 **2天**。
- **推理**：在单GPU上进行，未明确说明具体型号。

### 5. 实验数量与充分性
- **实验数量**：
  - 初始场景生成实验：在WOMD上对比5种方法，在nuPlan上对比1种方法（表2、3）。
  - 场景序列生成定性展示：多组视觉结果（图3、4、5），涵盖普通控制、用户控制、代理交互。
  - 消融实验：
    - **TAR vs 普通自回归**：对比GPU内存和推理时间（图6）。
    - **OAR模块**：UMGen与UMGen-T（无OAR）比较MMD和碰撞率（表4）。
    - **AMA模块**：有无AMA的地图生成质量对比（图7）。
- **充分性**：
  - 覆盖了核心模块的有效性验证。
  - 在多个数据集上进行了定量评估，对比方法均为当前主流。
  - 定性结果充分展示了生成场景的多样性和可控性。
- **客观公平性**：
  - 初始场景生成采用与其他方法相同的评估设定和指标。
  - 消融实验控制变量，对比合理。
  - 但未与同期最新（如DRIVEDREAMER-2、GAIA-1等）进行直接定量比较（因后者不生成所有模态），这是可理解的部分。

### 6. 主要结论与发现
- UMGen能够成功生成包含四种模态（动作、地图、代理、图像）的多模态驾驶场景序列，保持时间和模态间一致性。
- TAR模块相比普通自回归显著降低了计算开销，使长序列生成成为可能。
- OAR模块有效降低帧内token冲突（降低碰撞率），提升场景真实性。
- AMA模块确保地图随自车运动正确变换，增强地图-动作一致性。
- 用户能通过控制自车动作或代理动作生成定制场景（如切入、紧急制动），展示了作为闭环仿真器的潜力。

### 7. 优点
- **模态完整性**：首次将动态地图模态纳入驾驶场景生成，增强场景表示能力。
- **计算高效**：TAR将时序建模复杂度从O((TN)²)降为O(T²)，支持长序列生成。
- **强可控性**：支持自车和代理的细粒度控制，可生成符合特定需求的长序列场景。
- **交互模拟**：代理能根据自车动作作出合理反应（如刹车、变道），表现出基本交互能力。
- **代码开源**：提供项目页面和代码，便于复现和后续研究。

### 8. 不足与局限
- **图像生成质量**：图像由VQ-GAN tokenizer生成，分辨率有限；论文只提及可通过扩散模型进一步提升，但未提供充分实验验证。
- **场景多样性**：代理类型仅包括车辆、行人、自行车，缺乏更丰富的交通参与者（如动物、施工人员）。
- **控制粒度**：代理动作控制仅通过速度设定实现，未支持更高级指令（如“变道到左车道”），与基于语言的控制相比灵活性受限。
- **长序列稳定性**：虽然展示了60秒序列，但未量化长序列下模态一致性的衰减程度。
- **评测对比**：未能与生成图像或完整场景的最新方法（如GAIA-1、DRIVEDREAMER-2）在生成质量上进行直接定量对比，部分对比为定性或依赖不同设置。
- **应用限制**：仅基于nuPlan和WOMD，数据集覆盖有限；真实道路复杂度（如天气、光照、不规则路况）未涵盖。

（完）
