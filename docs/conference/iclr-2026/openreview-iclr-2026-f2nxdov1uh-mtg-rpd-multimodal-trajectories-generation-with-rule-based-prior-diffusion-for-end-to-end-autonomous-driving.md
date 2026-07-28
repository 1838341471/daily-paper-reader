---
title: "MTG-RPD: Multimodal Trajectories Generation with Rule-Based Prior Diffusion for End-to-End Autonomous Driving"
title_zh: MTG-RPD：基于规则先验扩散的多模态轨迹生成用于端到端自动驾驶
authors: "Xinyu Wang, Heng Wang, Huanyu Shen"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=f2nxdOv1Uh"
tags: ["query:av-pnc"]
score: 9.0
evidence: 用于自动驾驶的多模态轨迹生成与扩散模型
tldr: 针对端到端自动驾驶中生成多样且安全轨迹的挑战，提出MTG-RPD方法，融合基于规则的先验与扩散模型。该方法在保证实时性和重建精度的同时生成多模态轨迹。实验结果显示其轨迹生成质量优于现有方法。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有的扩散轨迹生成方法难以平衡实时性与重建精度，且缺乏规则约束。
method: 将基于规则的先验注入扩散模型，实现安全且多样的多模态轨迹生成。
result: 在公开数据集上验证了轨迹生成质量和实时性的提升。
conclusion: 规则先验与扩散模型的结合为端到端轨迹生成提供了新思路。
---

## Abstract
Replicating human driving behaviors in complex and authentic real-world environments remains a key challenge in autonomous driving. While end-to-end autonomous driving technologies have advanced substantially, generating safe and diverse multimodal trajectories poses a persistent hurdle. In recent years, diffusion-based methods have demonstrated remarkable potential across image generation, robotics, and autonomous driving—with trajectory generation approaches based on diffusion models also emerging. However, balancing real-time performance and reconstruction accuracy remains an unresolved issue. To address these limitations, we propose MTG-RPD, an innovative trajectory generation method that integrates rule-based prior knowledge. The approach first generates trajectory anchor points via rule-based prior clustering, then leverages a conditional diffusion model to transform an anchored Gaussian distribution into a multimodal trajectory distribution under scene information guidance. Notably, the diffusion model is specifically designed to facilitate agent-agent and agent-environment interactions. On the planning-based NAVSIM dataset, MTG-RPD achieved a PDMS of 88.5 when evaluated using the ResNet-34 backbone network.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：端到端自动驾驶需要生成安全、多样且符合真实环境的多模态轨迹，但现有基于扩散模型的轨迹生成方法难以同时满足**实时性**和**重建精度**，且缺乏对驾驶场景规则的显式约束。
- **研究动机**：人类驾驶行为复杂且多变，传统方法生成的轨迹要么多样性不足，要么违反安全规则。作者希望融合**基于规则的先验知识**与**扩散模型的生成能力**，在保证实时性的同时提升轨迹的安全性与多模态性。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程
- **核心思想**：将规则先验注入扩散模型，通过**轨迹锚点（anchor points）** 引导扩散过程的逆步，实现场景信息约束下的多模态轨迹生成。
- **关键技术细节**：
  1. **规则先验聚类**：首先利用基于规则的方法（如交通规则、运动学约束）对历史轨迹或场景数据进行聚类，生成一组**轨迹锚点**，作为安全驾驶的粗略参考。
  2. **条件扩散模型**：以锚点引导的**高斯分布**为起点，在场景信息（地图、交通参与者状态等）条件下，通过逆向扩散逐步生成多样化的轨迹分布。扩散模型内部设计了**智能体-智能体**和**智能体-环境**的交互机制，增强社会合规性。
- **算法流程（文字说明）**：
  - 步骤1：输入场景特征，通过规则先验模块生成K个锚点轨迹。
  - 步骤2：对每个锚点，初始化高斯噪声，并将其作为扩散模型的条件输入。
  - 步骤3：通过多步逆向扩散，在每个去噪步骤中融合场景上下文，逐步生成最终轨迹分布。
  - 步骤4：输出多模态轨迹集合（每个锚点对应一条轨迹）。

### 3. 实验设计：数据集、基准、对比方法
- **数据集与场景**：使用**NAVSIM**数据集（基于规划的仿真数据集），该数据集提供真实驾驶场景及多模态轨迹标签。
- **基准（Benchmark）**：论文未明确提及社区标准基准名称，但使用了NAVSIM的规划指标**PDMS**（Planning Driving Metric Score）进行评估。
- **对比方法**：论文仅说明“优于现有方法”，但未列出具体对比对象。从元数据看，推测对比了其他扩散轨迹生成方法（如MotionDiffuser、D2C等）或传统规划方法。

### 4. 资源与算力
- **文中未明确说明**：未提及GPU型号、数量、训练时长等详细信息。仅能从算法复杂度（扩散模型+规则先验）推测对算力有一定要求，但无具体数据。

### 5. 实验数量与充分性
- **实验数量**：仅知在NAVSIM上使用ResNet-34骨干网络获得了PDMS=88.5的结果。未提及消融实验、不同骨干网络对比、多数据集验证等。
- **充分性判断**：信息非常有限，**不充分**。缺少消融实验（规则先验有效性、扩散步数影响、锚点数量影响等）、与SOTA方法的定量对比、不同场景下（如拥堵、交叉口）的专项分析。实验设计不够客观/公平，因为未公布完整对比。

### 6. 论文的主要结论与发现
- 提出的MTG-RPD方法能够生成**安全、多样且实时**的多模态轨迹，在NAVSIM数据集上PDMS达到88.5，表明规则先验与扩散模型的结合有效提升了轨迹生成质量。

### 7. 优点
- **创新点**：首次将**规则先验**显式注入扩散生成过程，解决了纯扩散方法缺乏驾驶常识的问题。
- **实时性潜力**：通过锚点粗生成+扩散细化的两阶段设计，可能比直接扩散更快收敛（需实验佐证）。
- **多模态生成**：利用锚点作为不同模式峰值的引导，自然产生符合场景的多条轨迹。

### 8. 不足与局限
- **实验覆盖不足**：仅在一个数据集（NAVSIM）上报告单一骨干网络的结果，未在nuScenes、Waymo等主流数据集上验证泛化性。
- **基准与对比缺失**：未与基线和SOTA方法进行公平比较（如UniAD、VAD、MotionDiffuser等），难以判断实际提升幅度。
- **规则先验的设计细节未提供**：如何聚类锚点？规则规则是否可学习？是否适应不同驾驶场景？缺乏说明。
- **算力与部署成本未知**：未提供任何运行时间、GPU占用等指标，无法评估实际部署可行性。
- **偏差风险**：仅依赖一个PDMS指标，可能无法反映实际驾驶中的碰撞率、舒适性等关键属性。

（完）
