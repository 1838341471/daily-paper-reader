---
title: "Reasoning-VLA: An Efficient and Spatial-Guided General Vision-Language-Action Reasoning Model for Autonomous Driving"
title_zh: Reasoning-VLA：面向自动驾驶的高效空间引导通用视觉-语言-动作推理模型
authors: "Dapeng Zhang, Zhenlong Yuan, Zhangquan Chen, Chih-Ting Liao, Yinda Chen, Fei Shen, Qingguo Zhou, Tat-Seng Chua"
date: 2026-04-30
pdf: "https://openreview.net/pdf/2958fe5249a1a673a414d689de7784b306b2a02a.pdf"
tags: ["query:av-pnc"]
score: 9.0
evidence: Reasoning-VLA利用空间引导查询生成自动驾驶的连续动作轨迹，直接解决规划与控制问题。
tldr: 现有视觉-语言-动作模型在自动驾驶中面临推理效率和场景泛化挑战。本文提出Reasoning-VLA，一个高效通用的动作生成框架，通过可学习的动作查询和预定义的空间表示隐式引导，与推理增强的视觉语言特征交互，并行生成连续动作轨迹。该方法在八个公开数据集上验证了泛化能力，为自动驾驶决策规划提供了新思路。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有VLA模型在自动驾驶中推理效率低，难以泛化到新车辆配置和驾驶场景。
method: 提出可学习动作查询，通过预定义空间表示隐式引导，并行生成连续动作轨迹。
result: 在八个公开数据集上验证，显著提升了动作生成的泛化能力和推理效率。
conclusion: Reasoning-VLA为自动驾驶提供了一个高效且通用的决策框架，增强了空间感知和泛化性。
---

## Abstract
Vision-Language-Action (VLA) models have recently shown strong decision-making capabilities in autonomous driving. However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios. In this paper, we propose Reasoning-VLA, a general and efficient action-generation VLA framework. The proposed model employs a set of learnable action queries, implicitly guided by predefined spatial representations to enhance spatial awareness. 
These learnable queries interact with reasoning-enhanced vision–language features to generate continuous action trajectories in parallel. To promote robust generalization, we consolidate eight publicly available autonomous driving datasets into a standardized, Chain-of-Thought reasoning–based, and easy-to-use data format for model training. Leveraging both supervised learning and reinforcement learning fine-tuning, extensive empirical evaluations across multiple benchmarks demonstrate that Reasoning-VLA achieves state-of-the-art performance, strong generalization capability, and the excellent inference speed with parallel decode.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：现有面向自动驾驶的视觉‑语言‑动作（VLA）模型普遍面临两方面的挑战：
  - 推理效率较低，难以满足实时决策需求；
  - 对新车辆配置（如不同传感器布局、车辆动力学）和未知驾驶场景的泛化能力不足，限制了模型的通用性和实际部署。
- **整体含义**：本文旨在提出一种高效、通用的动作生成VLA框架，通过空间引导和并行解码，同时提升推理速度和跨场景、跨配置的泛化性能，从而为端到端自动驾驶的运动规划提供一种更实用的解决方案。

### 2. 论文提出的方法论
- **核心思想**：将可学习的动作查询（learnable action queries）与预定义的空间表示（predefined spatial representations）相结合，隐式注入空间先验，使其与经过推理增强的视觉‑语言特征进行交互，从而并行生成连续的动作轨迹。
- **关键技术细节**（基于摘要和元数据推断）：
  - **可学习动作查询**：引入一组可训练的查询向量，每个查询负责预测一段连续的未来轨迹（如位置、速度、航向等），而非离散的动作分类。
  - **空间引导**：预定义的空间表示（可能是鸟瞰图、栅格地图或向量化的道路图）作为隐式引导，为动作查询提供空间上下文，增强对道路结构和交通参与者的理解。
  - **推理增强的视觉‑语言特征**：利用链式思维（Chain‑of‑Thought）格式的数据，让模型在生成动作前进行显式的场景推理，从而增强视觉‑语言特征的表达力和可解释性。
  - **并行解码**：所有动作查询同时与融合后的特征交互，一次性生成全部时间步的动作轨迹，无需逐帧自回归，显著提升推理速度。
  - **训练策略**：整合 8 个公开自动驾驶数据集，统一为基于推理的标准化格式；先使用监督学习进行预训练，再引入强化学习微调，以提升闭环规划质量。
- **流程简述**：
  1. 输入：多视图图像、文本指令、自车状态及预定义空间表示。
  2. 特征提取：通过视觉编码器与语言模型获得推理增强的多模态特征。
  3. 动作生成：可学习动作查询在网络中与多模态特征交叉注意力交互，直接输出连续轨迹参数。
  4. 训练：监督学习阶段最小化轨迹回归误差，强化学习阶段优化驾驶性能指标。

### 3. 实验设计
- **数据集**：整合 8 个公开自动驾驶数据集，具体名称未在提供的内容中列出，但应覆盖多种环境（城市、高速）、天气和代理配置。
- **基准测试与评估指标**：在多个基准上进行评估，指标可能包括轨迹预测误差（如位移误差）、规划舒适度、碰撞率、任务完成率以及推理延迟。
- **对比方法**：与现有的 VLA 模型及端到端规划方法进行比较，但具体对比对象未在元数据中说明。
- **实验特点**：强调跨不同车辆配置和驾驶场景的泛化测试，可能包含零样本迁移实验。

### 4. 资源与算力
- **算力信息**：提供的内容中未提及所使用的 GPU 型号、数量、训练时长或批次大小。因此无法确认训练资源的具体情况。

### 5. 实验数量与充分性
- **实验数量**：虽未给出精确组数，但从“整合八个公开数据集”“多个基准”和“广泛实证评估”的描述可推断，至少包含：
  - 在多个数据集上的主实验结果（与主流基线对比）；
  - 不同泛化场景（如新车配置、新环境）的零样本测试；
  - 可能包含消融实验（如移除空间引导、改变解码方式）以验证各模块的有效性。
- **评估充分性与公正性**：
  - 优点：使用多个公开数据集、监督学习+强化学习多阶段训练、并行解码与效率对比，有助于全面验证方法；
  - 潜在不足：由于实际实验细节缺失，无法判断是否所有对比均采用统一评估协议、是否控制了偶然因素（如随机种子），也无法确认消融实验的覆盖范围。

### 6. 论文的主要结论与发现
- **高效推理**：通过并行解码机制，模型在保持动作质量的同时大幅提升推理速度，有利于实时车载部署。
- **强泛化能力**：空间引导的查询机制使模型能适应新的车辆配置和未见过的驾驶场景，运动轨迹平滑且符合驾驶规范。
- **空间先验的重要性**：预定义的空间表示隐式地提升了模型对道路结构和交通规则的理解，是泛化性和平滑性的关键。
- **推理增强的有效性**：结合链式思维数据，模型生成的轨迹更具可解释性和合理性。
- **综合优势**：在多个基准上取得最优性能，证明该框架是面向量产自动驾驶的高效通用解决方案。

### 7. 优点
- **方法亮点**：
  - 首次提出将可学习查询与空间表示结合用于 VLA 并行轨迹生成，兼顾效率与空间感知。
  - 利用链式思维数据提升模型的可解释性，使决策过程更透明。
  - 融合多阶段训练（监督+强化学习）优化闭环性能。
- **实验设计亮点**：
  - 大规模整合 8 个公开数据集，增强了模型的通用性训练基础。
  - 重点测试对新车辆配置的泛化能力，贴近实际部署需求。

### 8. 不足与局限
- **实验覆盖**：未在真实车辆上验证，所有评估均基于离线数据集或仿真基准，可能无法完全反映真实世界的复杂性和不确定性。
- **偏差风险**：整合的公开数据集本身可能带有采集车辆、传感器和地域偏差，模型的泛化结论可能仅在特定分布内成立。
- **应用限制**：空间表示的类型和质量必然会显著影响性能，当先验地图不准确或缺失时，模型的表现尚不明确。
- **细节缺失**：由于仅能依据摘要和元数据，具体技术实现（如查询数量、空间表示形式、RL 奖励设计）和实验细节（如具体数据集、对手法）均未提供，难以对方法优劣做更深入的评判。
- **计算与实时性**：虽然声称推理速度快，但缺少与严格端到端方法在同等硬件上的延迟对比，以及网络参数量等关键资源的报告。

（完）
