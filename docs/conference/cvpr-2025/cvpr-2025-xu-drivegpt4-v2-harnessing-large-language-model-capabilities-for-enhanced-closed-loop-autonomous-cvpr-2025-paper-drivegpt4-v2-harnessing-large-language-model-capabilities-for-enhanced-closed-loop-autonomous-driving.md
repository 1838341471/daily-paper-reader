---
title: "DriveGPT4-V2: Harnessing Large Language Model Capabilities for Enhanced Closed-Loop Autonomous Driving"
title_zh: DriveGPT4-V2：利用大型语言模型能力增强闭环自动驾驶
authors: "Xu, Zhenhua, Bai, Yan, Zhang, Yujia, Li, Zhuoling, Xia, Fei, Wong, Kwan-Yee K., Wang, Jianqiang, Zhao, Hengshuang"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Xu_DriveGPT4-V2_Harnessing_Large_Language_Model_Capabilities_for_Enhanced_Closed-Loop_Autonomous_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 8.0
evidence: 闭环自动驾驶控制信号生成
tldr: 现有闭环自动驾驶方法面临感知与规划分离的挑战。本文提出DriveGPT4-V2，利用多模态大语言模型从多视图图像和车辆状态直接生成低层控制信号。所提多视图视觉分词器增强了环境感知范围并保留关键细节。实验表明该方法在闭环驾驶任务中有效提升了控制稳定性和安全性。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xu-drivegpt4-v2-harnessing-large-language-model-capabilities-for-enhanced-closed-loop-autonomous-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 864, \"height\": 624, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xu-drivegpt4-v2-harnessing-large-language-model-capabilities-for-enhanced-closed-loop-autonomous-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1783, \"height\": 992, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xu-drivegpt4-v2-harnessing-large-language-model-capabilities-for-enhanced-closed-loop-autonomous-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 845, \"height\": 624, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xu-drivegpt4-v2-harnessing-large-language-model-capabilities-for-enhanced-closed-loop-autonomous-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 875, \"height\": 373, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xu-drivegpt4-v2-harnessing-large-language-model-capabilities-for-enhanced-closed-loop-autonomous-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 894, \"height\": 761, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xu-drivegpt4-v2-harnessing-large-language-model-capabilities-for-enhanced-closed-loop-autonomous-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 874, \"height\": 224, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xu-drivegpt4-v2-harnessing-large-language-model-capabilities-for-enhanced-closed-loop-autonomous-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1820, \"height\": 534, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xu-drivegpt4-v2-harnessing-large-language-model-capabilities-for-enhanced-closed-loop-autonomous-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 886, \"height\": 223, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xu-drivegpt4-v2-harnessing-large-language-model-capabilities-for-enhanced-closed-loop-autonomous-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 867, \"height\": 302, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xu-drivegpt4-v2-harnessing-large-language-model-capabilities-for-enhanced-closed-loop-autonomous-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 857, \"height\": 241, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xu-drivegpt4-v2-harnessing-large-language-model-capabilities-for-enhanced-closed-loop-autonomous-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 865, \"height\": 201, \"label\": \"Table\"}]"
motivation: 闭环自动驾驶中感知与规划分离导致性能瓶颈，需要统一的端到端方法。
method: 采用多视图视觉分词器处理环视图像，结合车辆状态输入到大语言模型生成控制信号。
result: 在闭环仿真中，DriveGPT4-V2实现了更平稳的控制和更低的碰撞率。
conclusion: MLLM在闭环自动驾驶控制中具有潜力，为端到端驾驶提供新思路。
---

## Abstract
Multimodal large language models (MLLMs) possess the ability to comprehend visual images or videos, and show impressive reasoning ability thanks to the vast amounts of pretrained knowledge, making them highly suitable for autonomous driving applications. Unlike the previous work, DriveGPT4-V1, which focused on open-loop tasks, this study explores the capabilities of LLMs in enhancing closed-loop autonomous driving. DriveGPT4-V2 processes camera images and vehicle states as input to generate low-level control signals for end-to-end vehicle operation. A multi-view visual tokenizer (MV-VT) is employed enabling DriveGPT4-V2 to perceive the environment with an extensive range while maintaining critical details. The model architecture has been refined to improve decision prediction and inference speed. To further enhance the performance, an additional expert LLM is trained for online imitation learning. The expert LLM, sharing a similar structure with DriveGPT4-V2, can access privileged information about surrounding objects for more robust and reliable predictions. Experimental results show that DriveGPT4-V2 outperforms all baselines on the challenging CARLA Longest6 benchmark. The code and data of DriveGPT4-V2 will be publicly available.

---

## 论文详细总结（自动生成）

# DriveGPT4-V2 论文详细中文总结

## 1. 论文的核心问题与整体含义

- **研究动机**：现有闭环自动驾驶系统多依赖基于规则的决策模块，灵活性差，难以应对复杂多变的真实场景。端到端方法虽能简化系统，但仅靠行为克隆（Behavior Cloning）会导致误差累积和漂移问题。多模态大语言模型（MLLM）具备强大推理和预训练知识，有潜力提升闭环驾驶性能，但此前工作（如DriveGPT4-V1）主要局限于开环任务。
- **核心问题**：如何利用MLLM实现高效、鲁棒的闭环端到端自动驾驶，并解决行为克隆带来的误差累积问题。
- **整体含义**：本文提出DriveGPT4-V2，通过将多视图图像和车辆状态输入MLLM，直接生成低层控制信号，并引入在线模仿学习（DAgger）增强鲁棒性，在CARLA Longest6基准上达到SOTA。

## 2. 论文提出的方法论

### 核心思想
- 基于MLLM（如Qwen-0.5B、TinyLLaMA）构建端到端驾驶系统，输入多视图图像（前左、前、前右）和车辆状态（速度、目标点），输出高层决策变量（目标速度、目标角度、路径点、路线点），再经PID控制器转为底层控制信号（油门、刹车、转向）。
- 引入一个额外的“专家LLM”，其结构与DriveGPT4-V2相似，但能访问周围物体的真实信息（特权信息）。专家模型在训练中提供在线策略监督，帮助代理模型处理异常状态。

### 关键技术细节
1. **多视图视觉分词器（MV-VT）**：三个前视角图像（384×384）分别经预训练视觉编码器（SigLIP）提取特征，再通过投影层映射到文本空间，实现大感知范围且保留细节。
2. **决策头（DeciHeads）**：用四个MLP头分别预测目标速度、目标角度、路径点（8个未来位置）和路线点（10个沿线采样点），每个头对应一个LLM输出token，大幅提升推理速度（仅需4个token）。
3. **在线模仿学习（DAgger）**：
   - 第一阶段：使用规则自动驾驶仪收集数据，对DriveGPT4-V2和专家LLM进行行为克隆训练。
   - 第二阶段：DriveGPT4-V2在训练场景中运行，专家LLM实时比较预测差异；若差异超过阈值，专家接管车辆并记录当前样本，形成聚合数据集，用于微调DriveGPT4-V2。
4. **损失函数**：L1损失，四项决策变量（目标速度、目标角度、路径点、路线点）之和。

### 算法流程（文字说明）
- 输入 → MV-VT提取图像特征 → 与文本状态拼接 → LLM生成4个token → 各经决策头输出数值 → PID控制器生成底层控制。

## 3. 实验设计

### 数据集与场景
- **训练数据**：采用CARLA模拟器，遵循Transfuser++的数据准备方式。
  - 阶段1：规则自动驾驶仪收集350K样本，过滤后300K，涵盖多个城镇（1-8, 10）和不同天气/光照。
  - 阶段2：DriveGPT4-V2在选定的训练路线上运行，专家提供在线监督，收集约150K样本，与原始数据集合并。
- **基准**：CARLA Longest6基准，包含36条长路线，评估闭环驾驶的综合能力。

### 对比方法
- WOR (ICCV 2021)、LAV v1/v2 (CVPR 2022)、Transfuser (TPAMI 2022)、PlanT (CoRL 2022)、InterFuser (CoRL 2023)、Transfuser++ (ICCV 2023)、LMDrive (CVPR 2024)。

### 评估指标
- Driving Score (DS)、Route Completion (RC)、Infraction Score (IS)，以及具体违规率（碰撞、闯红灯、偏离路线等）。

### 主要实验结果
- DriveGPT4-V2以DS=70、RC=91、IS=0.77全面超越所有基线，尤其比SOTA基线Transfuser++（DS=65）提升5分。
- 仅使用摄像头（C）输入，优于多数使用摄像头+激光雷达（C&L）的方法。

## 4. 资源与算力

- **训练配置**：使用16块A800 GPU，FP16精度，训练约75小时（60个epoch，学习率2e-5，余弦退火）。
- **推理**：单块A800 GPU，FP16精度。
- **模型规模**：采用0.5B参数LLM（如Qwen-0.5B），以平衡性能与效率。实验表明，使用7B LLM仅提升少量指标（DS从63到65），但训练时间增加近6倍，推理帧率从8.1降至0.4。

## 5. 实验数量与充分性

- **性能对比实验**：在CARLA Longest6上与7种基线方法（含不同变体）对比，结果全面领先。
- **消融实验**：共进行4组关键消融（含子实验）：
  - LLM视觉预训练：去掉预训练后DS从56降至47。
  - 多视图分词器（单图vs多视图）：DS从60降至47。
  - 路径点/路线点监督：移除后DS从63降至60。
  - 专家在线监督：移除后DS从70降至63。
  - PID控制器设计：对比直接基于路径点/路线点控制，证明预测目标速度/角度更优。
  - 决策头设计：对比更多token输出，证明4 token设计在精度不变下效率更高（FPS 8.1 vs 1.4）。
- **效率分析**：对比不同规模LLM（0.5B、1.5B、8B）的训练和推理性能，共3组。
- **公平性**：与基线比较时，部分方法采用官方报告结果，部分用开源代码复现（标注*），并特别注意数据量一致（Transfuser++有翻三倍数据版本与单倍数据版本对比）。消融实验控制变量清晰。

**充分性评价**：实验覆盖了性能对比、结构消融、效率分析、控制器设计等多个维度，数量充足，分析客观。但仅使用单一模拟器（CARLA）和单一基准，未在真实世界或其他模拟器中验证，存在一定局限性。

## 6. 论文的主要结论与发现

- MLLM凭借预训练知识和推理能力，能够有效应用于闭环端到端自动驾驶，以纯视觉输入超越融合激光雷达的基线方法。
- 多视图视觉分词器确保感知范围与细节保留，决策头设计显著提升推理效率。
- 在线模仿学习（专家LLM提供DAgger监督）是解决行为克隆误差累积的关键，带来明显性能提升。
- 模型规模并非越大越好：0.5B LLM在精度与效率间取得最佳平衡，过大模型（7B）收益有限而代价高昂。

## 7. 优点

- **方法创新**：首次将MLLM成功用于闭环自动驾驶闭环控制，并创新性地引入特权专家LLM实现在线模仿学习。
- **工程优化**：多视图分词器、决策头、PID控制器等设计兼顾感知、精度与实时性，推理速度达8.1 FPS，具备实际部署潜力。
- **实验扎实**：与多种SOTA方法对比，消融实验完整，分析逻辑严密，结论可信。
- **开源承诺**：代码和数据将公开，有利于社区复现和后续研究。

## 8. 不足与局限

- **实验场景局限**：仅在CARLA模拟器上进行，缺乏真实世界测试，鲁棒性和泛化性尚未验证。
- **特权信息依赖**：专家模型需访问模拟器提供的真实信息，在真实场景中难以获取，限制了DAgger阶段的应用。
- **基准单一**：仅使用CARLA Longest6一个基准，未在其他常见基准（如nuScenes、Waymo）上验证。
- **安全分析不足**：虽然报告了违规率，但未对极端危险情况（如紧急避撞）进行专门分析或保障机制。
- **模型通用性**：当前仅针对CARLA环境设计，需调整适配其他模拟器或真实车辆（如不同摄像头视角、动态范围等）。
- **训练成本较高**：虽相比大模型已优化，但75小时16卡训练仍有门槛。
- **未讨论故障模式**：未分析模型失败案例或统计显著差异（如城市内vs郊区、白天vs夜晚性能差异）。

（完）
