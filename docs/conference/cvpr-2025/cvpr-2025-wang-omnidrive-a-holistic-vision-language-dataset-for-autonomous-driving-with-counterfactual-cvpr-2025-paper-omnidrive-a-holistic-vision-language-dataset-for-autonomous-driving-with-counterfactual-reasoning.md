---
title: "OmniDrive: A Holistic Vision-Language Dataset for Autonomous Driving with Counterfactual Reasoning"
title_zh: OmniDrive：面向自动驾驶的全景视觉语言数据集与反事实推理
authors: "Wang, Shihao, Yu, Zhiding, Jiang, Xiaohui, Lan, Shiyi, Shi, Min, Chang, Nadine, Kautz, Jan, Li, Ying, Alvarez, Jose M."
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_OmniDrive_A_Holistic_Vision-Language_Dataset_for_Autonomous_Driving_with_Counterfactual_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 5.0
evidence: 通过反事实推理支持自动驾驶决策与规划
tldr: 将视觉语言模型从2D扩展到3D理解是自动驾驶推理的关键挑战。本文提出OmniDrive，一个包含反事实推理的全景视觉语言数据集，通过评估潜在场景结果增强决策能力。采用反事实合成数据标注生成大规模高质量数据，为规划模块提供更密集的监督信号。该方法在规划任务上展现出优越性能。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-omnidrive-a-holistic-vision-language-dataset-for-autonomous-driving-with-counterfactual-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1792, \"height\": 583, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-omnidrive-a-holistic-vision-language-dataset-for-autonomous-driving-with-counterfactual-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1739, \"height\": 475, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-omnidrive-a-holistic-vision-language-dataset-for-autonomous-driving-with-counterfactual-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1148, \"height\": 391, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-omnidrive-a-holistic-vision-language-dataset-for-autonomous-driving-with-counterfactual-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1370, \"height\": 1181, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-wang-omnidrive-a-holistic-vision-language-dataset-for-autonomous-driving-with-counterfactual-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1251, \"height\": 494, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wang-omnidrive-a-holistic-vision-language-dataset-for-autonomous-driving-with-counterfactual-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1753, \"height\": 660, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wang-omnidrive-a-holistic-vision-language-dataset-for-autonomous-driving-with-counterfactual-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 864, \"height\": 258, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wang-omnidrive-a-holistic-vision-language-dataset-for-autonomous-driving-with-counterfactual-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1501, \"height\": 371, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-wang-omnidrive-a-holistic-vision-language-dataset-for-autonomous-driving-with-counterfactual-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1586, \"height\": 374, \"label\": \"Table\"}]"
motivation: 现有VLM缺乏3D理解能力，难以直接支持自动驾驶规划决策。
method: 构建反事实推理数据集，通过合成场景生成多样化的规划监督信号。
result: 在3D驾驶任务上，反事实推理显著提升规划决策的准确性。
conclusion: 反事实推理数据集有效弥合了2D推理与3D规划之间的鸿沟。
---

## Abstract
The advances in vision-language models (VLMs) have led to a growing interest in autonomous driving to leverage their strong reasoning capabilities. However, extending these capabilities from 2D to full 3D understanding is crucial for real-world applications. To address this challenge, we propose OmniDrive, a holistic vision-language dataset that aligns agent models with 3D driving tasks through counterfactual reasoning. This approach enhances decision-making by evaluating potential scenarios and their outcomes, similar to human drivers considering alternative actions. Our counterfactual-based synthetic data annotation process generates large-scale, high-quality datasets, providing denser supervision signals that bridge planning trajectories and language-based reasoning. Futher, we explore two advanced OmniDrive-Agent frameworks, namely Omni-L and Omni-Q, to assess the importance of vision-language alignment versus 3D perception, revealing critical insights into designing effective LLM-agents. Significant improvements on the DriveLM Q&A benchmark and nuScenes open-loop planning demonstrate the effectiveness of our dataset and methods.

---

## 论文详细总结（自动生成）

# OmniDrive 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：现有视觉语言模型（VLM）在2D任务上展现出强大的推理能力，但扩展到自动驾驶领域时，缺乏对3D几何和空间语义的深层理解。传统自动驾驶数据集仅提供专家轨迹作为稀疏监督信号，无法反映复杂的决策推理过程，导致模型难以有效学习规划策略。
- **研究动机**：模仿人类驾驶员在决策时考虑多种可能情景（反事实推理）的能力，提升自动驾驶系统的安全性和可解释性。同时，需要设计能够融合3D感知与语言推理的LLM-Agent框架。
- **整体含义**：提出一个从数据集到模型框架的完整方案——OmniDrive，通过反事实合成数据生成高质量的3D驾驶问答对，并探索两种Agent架构（Omni-L和Omni-Q），旨在弥合2D VLM与3D自动驾驶规划之间的鸿沟。

## 2. 方法论：核心思想、关键技术细节、算法流程

### 核心思想
- **反事实推理**：模拟多种替代驾驶轨迹（如加速左转、减速直行等），通过规则检查其合规性（碰撞、红灯、驶出可行驶区域等），生成“如果…会怎样”的问答对，为模型提供比单一专家轨迹更密集的监督信号。
- **人机协同数据生成**：利用GPT-4结合结构化场景描述和反事实检查表，自动生成高质量Q&A，再通过人工验证迭代。

### 关键技术细节
1. **关键帧选择**：先用CLIP提取前视图嵌入进行语义聚类（K-means，选取20%中心），再对轨迹进行行为聚类（8类，选取200个中心），确保覆盖多样场景。
2. **反事实检查表设计**：基于nuScenes、OpenLane-v2的3D标注（物体、车道线、信号灯），用规则判断模拟轨迹是否违规；同时让GPT-4对图像进行高层决策分析，弥补纯规则不足。
3. **Q&A生成类型**：包括场景描述、注意力元素定位、反事实推理、决策规划、通用对话（计数、颜色、OCR等）。
4. **Agent架构**：
   - **Omni-L**：基于LLaVA的MLP投影器，直接对齐多视图图像特征与语言，加入3D位置编码（初始化为零）。
   - **Omni-Q**：基于StreamPETR的BEV感知架构，采用Q-Former设计，使用检测查询（Query）和载体查询（Carrier Query），载体查询用于语言生成，检测查询用于3D感知监督。

### 算法流程（文字说明）
- 数据生成：输入多视图图像→提取CLIP特征聚类关键帧→从nuScenes轨迹库中采样8类模拟轨迹→对每条轨迹执行规则检查（碰撞、红灯等）→将结构化场景信息（物体位置、轨迹、标签）和图像一起输入GPT-4→GPT-4生成符合检查结果的Q&A→人工验证。
- 模型训练：两阶段训练。第一阶段在2D图像任务上预训练投影器/Q-Former；第二阶段在OmniDrive和DriveLM数据上微调整个模型（视觉编码器、投影器、LLM），学习率采用cosine衰减。

## 3. 实验设计

### 数据集与场景
- **OmniDrive**：基于nuScenes，通过反事实生成大规模Q&A，覆盖感知、推理、规划。
- **DriveLM**：696个场景，0.3M图像-问题对，用于评测VLM的端到端驾驶能力。
- **nuScenes开放环规划**：使用真实日志回放，评估L2误差、碰撞率、交叉率。

### Benchmark
- **DriveLM**：综合指标（GPT Score 0.4 + 语言分数0.2 + 匹配分数0.2 + 准确率0.2）。
- **nuScenes开放环规划**：1s/2s/3s的L2距离、碰撞率、道路边界交叉率。
- **反事实推理**：用GPT-3.5提取关键词（安全、碰撞、红灯、驶出区域），计算精确率和召回率。

### 对比方法
- 规划对比：BEV-Planner、UniAD、VAD、ST-P3、Ego-MLP等。
- VLM对比：仅在DriveLM上训练的Omni-L vs 添加OmniDrive预训练 vs 添加LLaVA665K预训练。
- 架构对比：Omni-L（2D VLM对齐）、Omni-Q（3D感知集成）、BEV-MLP（LSS+MLP）。

## 4. 资源与算力

- **文中未明确说明使用的GPU型号、数量及训练时长**。仅提到训练使用AdamW优化器，batch size=16，视觉编码器与LLM学习率2e-5，投影器学习率4e-4，采用cosine退火策略。推断使用了NVIDIA GPU集群（作者单位含NVIDIA），但具体算力未披露。

## 5. 实验数量与充分性

- **主要实验组**：约5组核心实验（表2-5），包括：
  - 开放环规划对比（表2）：9种方法，每种有/无ego状态两种配置，共约18个结果。
  - DriveLM基准测试（表3）：4种数据组合（仅DriveLM、+OmniDrive、+LLaVA665k、+Both）。
  - 反事实推理分析（表4）：3种架构 + 2种感知监督消融，共5组。
  - 综合消融（表5）：架构、感知监督、语言能力与规划指标关联。
- **充分性评价**：实验设计较为全面，覆盖了数据集效果（DriveLM提升3%）、规划性能（与SOTA规划方法比较）、反事实推理能力（精确率/召回率）、架构对比（Omni-L vs Omni-Q）。但仍缺少：闭环仿真评估、更多真实场景的泛化测试、与更大规模VLM（如GPT-4V）的直接对比。整体实验客观，消融实验清晰，但规模不算特别大。

## 6. 主要结论与发现

- **OmniDrive数据集有效**：在DriveLM上预训练提升3%综合分数，与LLaVA665K结合再提升1%。
- **反事实推理提升规划**：仅用轨迹预测任务训练的Omni-L碰撞率3.22%，加入OmniDrive Q&A后降至1.90%（无ego状态），表明反事实数据提供了更丰富的监督。
- **架构对比**：Omni-L（基于2D VLM对齐）在反事实推理（AP 53.7% vs 52.3%）、语言能力（CIDEr 73.2 vs 68.6）、开放环规划（碰撞率1.90% vs 3.79%）上全面优于Omni-Q（集成3D感知）。表明将2D VLM迁移到3D比将3D感知集成到VLM更简单有效。
- **Ego状态过拟合风险**：加入ego状态后所有方法指标提升，但LLM更易过拟合，Omni-Q尤为明显（低L2但高碰撞率）。
- **感知监督价值**：在Omni-Q中，加入物体和车道监督能提升碰撞检测的召回率（从53.2%到72.6%）。

## 7. 优点

- **数据集创新**：首次系统地将反事实推理应用于自动驾驶VLM数据集生成，提供密集监督，超越简单专家轨迹。
- **人机协同流程**：规则检查+GPT-4生成+人工验证，兼顾自动化与质量。
- **架构探索**：对比两种典型范式（2D VLM对齐 vs 3D感知集成），揭示设计经验，对社区有指导意义。
- **实验透明度**：明确指出开放环规划的局限性（Ego状态过拟合），并据此公平对比，分析到位。

## 8. 不足与局限

- **模拟假设**：反事实模拟假设其他交通参与者不反应（静态环境），无法模拟真实动态交互。作者也承认这是局限，计划未来结合闭环仿真。
- **开放环评估固有缺陷**：即使提升了规划指标，开放环评估仍存在偏差，无法全面反映实际驾驶性能。
- **资源算力未公开**：缺乏训练资源细节，不利于可重复性验证。
- **架构对比公平性**：Omni-L和Omni-Q的预训练数据、模型大小可能不完全一致（Omni-L使用LLaVA v1.5预训练，Omni-Q使用2D任务预训练），可能引入不公平因素。
- **泛化性**：仅基于nuScenes，未在Waymo、CARLA等数据集上验证，场景多样性有限。
- **语言能力依赖**：反事实推理依赖GPT-4，可能存在生成偏差；评估时又用GPT-3.5提取关键词，引入额外噪声。

（完）
