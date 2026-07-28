---
title: "Less is More: Lean yet Powerful Vision-Language Model for Autonomous Driving"
title_zh: Less is More：用于自动驾驶的简洁而强大的视觉语言模型
authors: "Sheng Yang, Tong Zhan, Guancheng Chen, Yanfeng Lu, Jian Wang"
date: 2025-09-04
pdf: "https://openreview.net/pdf?id=8viZQgKVWT"
tags: ["query:av-pnc"]
score: 8.0
evidence: 通过视觉语言模型将轨迹规划建模为下一个路点预测
tldr: 将自动驾驶重新构想为广义语言任务，把轨迹规划转化为下一个路点预测。提出Max-V1框架，利用视觉语言模型的生成能力直接从前视相机输入进行端到端轨迹预测。基于统计建模的原理性监督策略使模型能够学习复杂驾驶策略。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有端到端驾驶方法复杂且缺乏统一的序列生成范式。
method: 将轨迹规划视为下一个路点预测，使用单阶段VLM直接生成轨迹。
result: 在多个基准上验证了框架的有效性和计算效率。
conclusion: 简洁的序列化预测范式能高效学习复杂驾驶策略。
---

## Abstract
In this work, we reconceptualize autonomous driving as a generalized language and formulate the trajectory planning task as next waypoint prediction. We introduce Max-V1, a novel framework for one-stage end-to-end autonomous driving. Our framework presents a single-pass generation paradigm that aligns with the inherent sequentiality of driving. This approach leverages the generative capacity of the VLM (Vision-Language Model) to enable end-to-end trajectory prediction directly from front-view camera input. The efficacy of this method is underpinned by a principled supervision strategy derived from statistical modeling. This provides a well-defined learning objective, which makes the framework highly amenable to master complex driving policies through imitation learning from large-scale expert demonstrations. Empirically, our method achieves the state-of-the-art performance on the nuScenes dataset, delivers an overall improvement of over 30% compared to prior baselines. Furthermore, it exhibits superior generalization performance on cross-domain datasets acquired from diverse vehicles, demonstrating notable potential for cross-vehicle robustness and adaptability. Due to these empirical strengths, this work introduces a model enabling fundamental driving behaviors, laying the foundation for the development of more capable self-driving agents. Code will be available upon publication.

---

## 论文详细总结（自动生成）

以下是对论文《Less is More: Lean yet Powerful Vision-Language Model for Autonomous Driving》的详细中文总结，内容基于提供的摘要和元数据。

### 1. 核心问题与整体含义（研究动机和背景）
- **研究背景**：现有端到端自动驾驶方法往往结构复杂，缺乏统一的序列生成范式，难以高效学习复杂驾驶策略。
- **核心问题**：如何将自动驾驶任务简化为一种统一的、序列化的预测问题，从而利用视觉语言模型（VLM）的生成能力实现端到端轨迹规划。
- **整体含义**：作者将自动驾驶重新构想为广义语言任务，将轨迹规划转化为“下一个路点预测”，并提出Max-V1框架，旨在实现简洁而强大的驾驶策略学习。

### 2. 方法论
- **核心思想**：采用单阶段端到端生成范式，将驾驶决策建模为序列化的路点预测，与驾驶的固有顺序性对齐。
- **关键技术细节**：
  - 框架名为 **Max-V1**，直接从前视相机输入出发，利用视觉语言模型（VLM）的生成能力一次性输出未来轨迹（路点序列）。
  - 监督策略基于**统计建模**（statistical modeling），即通过大规模专家演示进行模仿学习，使模型能掌握复杂驾驶策略。
  - 整个流程为**单次前向生成**，避免了多阶段模块的级联误差。
- **公式或算法流程（文字说明）**：
  1. 输入：单目前视图像 + 可选的导航/自车状态信息（文中未详述）。
  2. 编码：VLM对图像进行视觉编码，并融合语言指令（若有）。
  3. 生成：模型以自回归（或并行）方式预测后续的多个路点坐标（作为文本或连续token）。
  4. 损失：使用基于统计的监督信号（如负对数似然）优化模型参数。

### 3. 实验设计
- **数据集**：
  - **nuScenes**：主要测试数据集，用于评估性能。
  - **跨域数据集**：从不同车辆采集的数据，用于验证跨车辆鲁棒性和适应性。
- **基准（Benchmark）**：在nuScenes上对比先前基线方法（具体方法名未列出）。
- **对比方法**：文献提到“整体提升超过30%”，表明与先前端到端方法进行了对比。
- **未明确说明**：是否包含CARLA等模拟环境或开环/闭环评估具体指标（如L2误差、碰撞率等）。

### 4. 资源与算力
- 论文摘要和元数据中**未明确说明**所使用的GPU型号、数量、训练时长、显存等算力信息。仅知代码将在发表后开源。

### 5. 实验数量与充分性
- **数量**：摘要仅提及在nuScenes上的主要结果和跨域泛化实验，未列出消融实验的具体数量。可能包含一定量的消融（如模型大小、监督策略等），但文中未详述。
- **充分性与公平性**：
  - 在nuScenes上达到SOTA且提升>30%，结果较为显著。
  - 跨域实验验证了泛化性，增强了结论的可信度。
  - 但缺少详细实验配置（如训练/验证划分、随机种子、统计显著性检验）和失败案例分析，整体充分性**中等偏上**，但公开信息有限。

### 6. 主要结论与发现
- **简洁的序列化预测范式能高效学习复杂驾驶策略**，通过单阶段VLM生成方法即可实现基础驾驶行为。
- 在nuScenes数据集上达到当前最优（SOTA），总体性能相比先前基线提升超30%。
- 跨车辆场景下表现出良好的泛化与鲁棒性，显示出跨车辆适应的潜力。

### 7. 优点
- **方法简洁**：将复杂规划任务统一为下一个路点预测，降低了系统复杂度。
- **端到端单阶段**：避免多阶段模块设计和手工规则。
- **计算效率高**：与一些两阶段或模块化方法相比，单次推理更高效。
- **通用性强**：跨域数据集验证了可迁移性，表明框架对不同车辆平台有一定适应性。
- **理论基础清晰**：基于统计建模的监督策略为学习提供明确目标。

### 8. 不足与局限
- **实验覆盖有限**：仅测试了nuScenes和跨域数据集，缺乏在复杂交互场景（多车博弈、城市复杂路口）或长尾事件上的详细评估。
- **缺失算力与训练细节**：未报告资源消耗，读者难以复现或比较效率。
- **可解释性**：作为VLM生成方法，模型内部推理过程不透明，难以进行安全性验证。
- **依赖大规模专家数据**：需要大量高质量驾驶演示，且模仿学习可能无法处理分布外情况。
- **未讨论隐私与安全性**：例如对抗攻击、感知失效下的行为。

（完）
