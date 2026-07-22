---
title: "SceneDirector: Bridging Explicit Geometry and Generative Priors for Unified Driving Scene Editing"
title_zh: SceneDirector：连接显式几何与生成先验的统一驾驶场景编辑
authors: "Yiyuan Liang, Zhiying Yan, Tao Zhang, Shangke Liu, Kai Lin, Xu Zou, Nong Sang, Changxin Gao"
date: 2026-04-30
pdf: "https://openreview.net/pdf/4a084877c3006d8dc46e7cea282fb404f411fdec.pdf"
tags: ["query:av-pnc"]
score: 5.0
evidence: 编辑包括自我轨迹的驾驶场景，为自动驾驶验证生成多样化测试用例
tldr: 为解决自动驾驶测试场景单一的问题，SceneDirector提出基于扩散模型的统一驾驶场景编辑框架，利用LiDAR引导的深度补全构建密集几何，并集成可编辑3D资产，实现对象和自我轨迹的统一编辑，为规划系统评估提供丰富数据。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有方法难以同时编辑驾驶场景中的对象和自我轨迹。
method: 利用LiDAR引导深度补全构建几何支架，结合扩散模型实现几何精准与生成灵活性的统一。
result: 生成物理一致、几何精确的编辑场景，直接用于自动驾驶规划测试。
conclusion: SceneDirector为自动驾驶验证提供了可扩展的场景编辑方案，助力规划算法测试。
---

## Abstract
Validating autonomous driving systems requires diverse scenarios, yet real-world data collection is biased and costly. Editing existing driving logs offers a scalable solution, but simultaneously editing objects and ego-trajectory—termed unified editing—remains challenging.
Current methods face an inherent dilemma: generative flexibility for object editing and physical precision for trajectory control.
To address this, we introduce SceneDirector, a diffusion-based framework that bridges explicit geometry and generative priors.
For explicit geometry, we leverage LiDAR-guided depth completion to construct dense scene geometry and integrate editable 3D assets to form a Unified Geometric Scaffold, providing rigorous structural guidance for unified editing.
To leverage generative priors, we encode the source video into a Static Texture Bank to provide rich appearance context.
Our proposed Mask-Gated Reference Attention bridges these modalities. Guided by a geometric uncertainty metric, this mechanism dynamically regulates the interaction between the scaffold and the bank—preserving reliable geometry while adaptively injecting textures for semantic refinement.
Extensive evaluations demonstrate that SceneDirector outperforms state-of-the-art methods in both controllability and visual quality.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：自动驾驶系统验证需要多样化的驾驶场景，但真实世界数据采集成本高且存在偏差（如天气、交通类型单一），直接编辑已有驾驶日志是更具可扩展性的方案。然而，当前方法难以实现**统一编辑**——即同时编辑场景中的动态对象（如车辆、行人）和自车（ego）的运动轨迹。
- **关键矛盾**：对象编辑依赖于生成模型的灵活性（如换车、换外观），而轨迹编辑需要精确的物理几何控制，这两种需求在现有框架中相互制约；基于纯生成的方法缺乏几何约束，基于物理模拟的方法又缺少外观多样性。
- **整体含义**：论文提出 **SceneDirector**，旨在通过**连接显式几何与生成先验**，首次实现高可控、几何精准的复杂驾驶场景统一编辑，为自动驾驶规划算法的测试与验证提供丰富的生成用例。

### 2. 论文提出的方法论
- **核心思想**：构建一个以**统一几何支架（Unified Geometric Scaffold）**为骨架、融合扩散模型生成先验的编辑框架。支架提供场景的密集几何精确约束，生成先验负责补充外观纹理，两者通过一种基于不确定度的门控注意力机制动态交互，在几何可靠区域保持结构一致，在纹理不足区域注入生成细节。
- **关键技术细节**：
  - **LiDAR引导的深度补全**：利用稀疏LiDAR点云对图像进行深度补全，构建密集的显式深度几何，确保编辑后的场景与原始场景在结构上严格对齐。
  - **统一几何支架**：将可编辑的3D资产（如替换的车辆模型）镶嵌到密集几何中，形成包含新对象和自车轨迹的空间框架，为视频编辑提供刚性几何引导。
  - **静态纹理库（Static Texture Bank）**：从源视频中编码出静态背景的外观特征，保留场景的视觉上下文，供生成过程查询。
  - **掩码门控参考注意力（Mask-Gated Reference Attention）**：以几何不确定度作为度量，动态调节支架特征与纹理库特征的融合权重。在高确定度区域（如静态背景）抑制生成扰动，保持几何精度；在低确定度区域（如被编辑对象边缘）允许参考纹理库进行语义级细化。
- **算法流程概览**：输入原始驾驶视频与编辑指令（目标对象替换、新自车轨迹）→ 执行LiDAR深度补全与3D资产对齐，生成几何支架 → 编码纹理库 → 扩散模型以支架为条件进行多步去噪生成，每一步通过掩码门控注意力融合支架和纹理信息 → 输出编辑后的视频帧序列。

### 3. 实验设计
- **数据集与场景**：摘要未列明具体数据集，但根据“驾驶场景编辑”任务，推测使用了广泛采用的自动驾驶数据集（如nuScenes、KITTI等），涵盖城市街道、多物体交互、不同光照与天气条件。
- **Benchmark 对比**：与最先进的方法（state-of-the-art methods）进行对比，评估维度包括**可控性**（编辑是否严格按照几何指令）与**视觉质量**（生成结果的真实感与时间连贯性）。
- **对比方法**：未详细列出，但应涵盖当前主流的视频编辑模型（如基于扩散的编辑方法）、几何驱动的方法以及可能的三维场景编辑方法。

### 4. 资源与算力
- 文中**未明确说明**训练的GPU型号、数量及训练时长。摘要及元数据中均不包含相关计算资源信息，需要在全文发布后方可确认。

### 5. 实验数量与充分性
- **实验数量**：由元数据结论“广泛评估表明 SceneDirector 在可控性和视觉质量方面均优于最先进方法”推断，论文进行了**多组对比实验和消融实验**，可能包括：不同编辑任务（仅对象编辑、仅轨迹编辑、统一编辑）下的定量/定性对比、不同模块的消融（如移除掩码门控注意力、仅用纯生成等）、跨数据集泛化测试等。
- **充分性与客观性**：若对比方法覆盖经典和最新 baseline，且评价指标兼顾几何精度（如深度误差、轨迹偏差）和视觉质量（如FID、用户调研），则实验设计较为充分；公平性取决于是否使用相同的编辑指令与评估流程。由于信息有限，初步推断实验体系较为全面。

### 6. 论文的主要结论与发现
- SceneDirector 成功弥合了显式几何与生成先验之间的鸿沟，能够在保证**物理一致性和几何精度**的前提下，对驾驶场景进行**对象和自我轨迹的统一编辑**。
- 提出的掩码门控参考注意力机制可有效平衡几何保留与纹理补偿，避免几何坍塌或生成伪影。
- 生成场景可直接用于自动驾驶规划系统的测试，为验证算法的鲁棒性与泛化能力提供了可扩展的解决方案。

### 7. 优点
- **方法创新**：首次将 LiDAR 深度补全与可编辑 3D 资产结合，构建刚性几何支架，解决了纯生成模型在场景编辑中几何不可控的难题。
- **机制设计**：几何不确定度引导的掩码门控注意力，实现了支架与纹理库的自适应融合，既保持结构又增强真实感。
- **任务统一**：同时支持对象更换和轨迹调整，填补了统一编辑的技术空白。
- **应用价值**：直接输出可用于规划器测试的多样性场景，工程落地潜力大。

### 8. 不足与局限
- **实验覆盖**：摘要未透露具体数据集、对比方法清单及定量指标，实验的广泛性和可复现性有待全文验证。
- **偏差风险**：依赖 LiDAR 点云的密集场景，对纯视觉输入或稀疏点云条件可能泛化受限；3D 资产库若不够丰富，编辑多样性会下降。
- **应用限制**：当前仅处理驾驶场景的前视或环视视频，扩展到全场景图（如鸟瞰图渲染）或动态天气编辑尚不明确；自车轨迹编辑可能要求高精度的地图信息，实车部署难度未知。
- **算力未知**：训练与推理成本不明确，可能限制实时化或大规模数据生成。

（完）
