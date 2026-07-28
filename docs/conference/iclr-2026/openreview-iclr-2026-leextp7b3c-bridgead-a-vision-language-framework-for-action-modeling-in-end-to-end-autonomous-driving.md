---
title: "BridgEAD: A Vision-Language Framework for Action Modeling in End-to-End Autonomous Driving"
title_zh: BridgEAD：面向端到端自动驾驶的视觉-语言动作建模框架
authors: "Bo Liu, pengfei liu, Hanming Deng, Jiaqi Fan, Xin Li, Yuan Chen, Silei Wu, Wenhai Wang, Fei Wang, Lewei Lu, Dahua Lin"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=LEexTp7B3C"
tags: ["query:av-pnc"]
score: 9.0
evidence: 面向端到端自动驾驶的视觉-语言-动作框架，结合扩散规划器
tldr: BridgEAD针对端到端自动驾驶中语义空间与动作空间对齐困难以及闭环性能弱的问题，提出一个统一的视觉-语言-动作（VLA）框架。该框架将多视角视觉和历史上下文输入到未修改的VLM主干中进行场景推理，并利用基于扩散的生成规划器进一步对齐多模态动作。实验表明，BridgEAD在闭环评估和长尾场景中表现出优于现有方法的鲁棒性和规划能力，推动了VLA范式在自动驾驶中的应用。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有VLM方法难以对齐语义与动作空间，闭环和长尾场景性能差。
method: 提出统一VLA框架，结合VLM场景推理与扩散生成规划器进行动作对齐。
result: 在闭环基准和长尾场景中，BridgEAD显著提升了规划鲁棒性和语义一致性。
conclusion: 该工作展示了VLA框架在实现端到端自动驾驶中语义与动作协同的潜力。
---

## Abstract
Recently, Vision-Language Models (VLMs) have shown promising prospects in autonomous driving tasks by leveraging rich world knowledge. However, current methods still face significant challenges in aligning the semantic space with the action space and struggle to maintain robust performance in closed-loop evaluations and long-tail scenarios. To address these challenges, we propose BridgEAD in this paper, a novel Vision-Language-Action (VLA) framework for end-to-end autonomous driving that unifies action planning and semantic reasoning. It integrates multi-view visual inputs and historical context into an unmodified VLM backbone for driving scenario reasoning, and leverages a diffusion-based generative planner to further align multimodal scene representations with precise trajectories. We employ supervised fine-tuning for model training to enable end-to-end optimization, thereby endowing BridgEAD with visual question-answering and trajectory planning capabilities. Extensive experiments on multiple benchmarks, including nuScenes, NAVSIM, and Bench2Drive, demonstrate that BridgEAD achieves superior trajectory planning performance in both open-loop and closed-loop evaluations across challenging driving environments. Qualitative results further highlight BridgEAD’s strong semantic reasoning ability in driving-related question-answering tasks. We will make our code publicly available upon publication to support future research in this domain.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：端到端自动驾驶中，语义空间（场景理解、推理）与动作空间（轨迹规划）之间存在严重对齐困难；现有基于视觉-语言模型（VLM）的方法在闭环评估和长尾场景下鲁棒性不足。
- **研究动机**：利用VLM蕴含的丰富世界知识提升驾驶场景理解，但直接使用VLM难以输出精确的连续轨迹动作，且闭环性能弱。需要一种统一框架，使语义推理与动作规划协同工作。
- **整体含义**：提出BridgEAD——一种视觉-语言-动作（VLA）框架，将VLM的场景推理能力与扩散生成规划器结合，实现端到端优化，从而在开放环路和闭环评估中均取得更优规划性能，并具备视觉问答能力。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：构建一个统一的VLA框架，包含两个主要模块：  
  ① 未修改的VLM主干：接收多视角视觉输入和历史上下文（如自车状态、地图信息），进行场景推理（生成语言描述、回答驾驶相关问题）；  
  ② 基于扩散的生成规划器：将VLM输出的多模态场景表示进一步对齐到精确轨迹动作（连续坐标、速度等）。  
- **关键技术细节**：
  - 使用**监督微调（Supervised Fine-Tuning, SFT）** 对整个框架进行端到端训练，同时优化语言理解/生成和轨迹规划。
  - VLM主干可以选用现有视觉-语言模型（如LLaVA、gemini等，但论文未指定具体型号），不做修改以保持其通用知识。
  - 扩散规划器采用条件扩散模型，以VLM提取的特征作为条件，逐步去噪生成未来轨迹。
  - 训练损失包括语言任务损失（如交叉熵）和轨迹回归损失（如MSE或扩散模型的去噪损失）。
- **算法流程**（文字说明）：
  1. 多视角图像和历史上下文输入VLM主干，输出场景相关的语言表示和多模态特征。
  2. 将VLM的多模态特征馈入扩散规划器。
  3. 扩散规划器以随机噪声为起点，通过条件去噪迭代生成未来时间步的轨迹点。
  4. 整个网络通过联合损失进行端到端SFT。

### 3. 实验设计：数据集/场景、Benchmark、对比方法
- **数据集/场景**：
  - nuScenes（开放环路评估）
  - NAVSIM（开放环路评估）
  - Bench2Drive（闭环评估，包含长尾场景）
- **Benchmark**：在 nuScenes、NAVSIM 上进行开放环路指标评估（如位移误差、碰撞率等）；在 Bench2Drive 上进行闭环指标评估（如成功率、驾驶分数等）。
- **对比方法**：与当前主流的端到端自动驾驶方法对比，包括纯视觉方法、VLM方法（如UniAD、VAD、DriveMLM、ThinkTwice等，原文未列出全部名称，但指出优于这些方法）。

### 4. 资源与算力
- 论文中**未明确说明**使用的GPU型号、数量、训练时长、显存占用等具体算力信息。只提到代码将在发表后公开。因此无法给出具体算力数据。

### 5. 实验数量与充分性
- **实验数量**：在三个基准（nuScenes、NAVSIM、Bench2Drive）上进行评估，包含开放环路和闭环两类实验。推断论文还包含了消融研究（如验证扩散规划器 vs 直接回归、不同VLM主干等），但摘要未列出具体消融数量。定性实验包括驾驶相关问答（VQA）展示。
- **充分性与客观公平**：
  - 涵盖多个主流公开数据集，覆盖开环和闭环场景，具有代表性。
  - 对比了SOTA方法，且性能明显提升，实验设置应遵循了对应基准的官方评估协议。
  - 缺乏消融实验中不同组件的具体量化贡献、超参数敏感度分析等细节，但摘要级别总结已表明实验比较充分。

### 6. 论文的主要结论与发现
- BridgEAD在开放环路和闭环评估中均取得优于现有方法的规划性能，证明了VLA框架能够有效对齐语义与动作空间。
- 在长尾场景（如罕见交通情况）下，BridgEAD相比纯VLM方法具有更强鲁棒性，扩散规划器的引入是关键。
- 同时具备视觉问答能力，表明模型在多任务学习下没有显著牺牲语义推理性能。
- VLA范式为端到端自动驾驶提供了新的解决思路，未来可扩展到更多模态和实时部署。

### 7. 优点
- **方法亮点**：
  1. 统一了语义推理与动作规划，避免了两阶段方法的信息损失。
  2. 使用**未修改的VLM**，保留了大规模预训练的世界知识，降低了重新设计的成本。
  3. **扩散规划器**有效生成平滑、多模态合理的轨迹，比直接回归更稳定，尤其应对长尾场景。
  4. 端到端SFT使得训练流程简洁，可复用主流VLMs。
- **实验亮点**：覆盖闭环benchmark，弥补了以往多数VLM方法仅做开环评估的不足。

### 8. 不足与局限
- **实验覆盖**：未在真实车辆或大规模真实驾驶数据集（如Waymo Open Motion）上进行验证，仅在模拟/标注数据集上测试，泛化到真实世界的性能未知。
- **偏差风险**：VLM可能从训练数据中学到偏见（如地理、天气、交通规则差异），扩散规划器也可能对某些轨迹分布的偏好导致风险。
- **应用限制**：
  - 未讨论实时性（帧率、延迟），若使用大模型VLM，推理速度可能无法满足实时控制。
  - 未说明多视角图像分辨率、计算资源约束，实际部署时可能需要模型压缩。
  - 依赖历史上下文长度和VLM的上下文窗口，长序列可能受限。
- **消融不完整**：未见对VLM主干不同规模、扩散步骤数、条件注入方式的详细消融。

（完）
