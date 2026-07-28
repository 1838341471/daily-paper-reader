---
title: "AlignDrive: Aligned Lateral-Longitudinal Planning for End-to-End Autonomous Driving"
title_zh: AlignDrive：面向端到端自动驾驶的对齐横向-纵向规划
authors: "Yanhao Wu, Haoyang Zhang, Fei He, Rui Wu, Congpei Qiu, Liang Gao, Wei Ke, Tong Zhang"
date: 2025-09-08
pdf: "https://openreview.net/pdf?id=vhrovHIeE4"
tags: ["query:av-pnc"]
score: 9.0
evidence: 提出AlignDrive实现横向-纵向协调的路径规划
tldr: 现有端到端模型将横向与纵向规划解耦并行执行，导致路径与速度不协调。本文提出级联框架，将纵向规划显式依赖于规划路径，实现协调的横向-纵向规划。实验表明该方法有效减少了碰撞风险，提升了规划安全性。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 并行横向-纵向规划存在协调失败问题，且未充分利用路径作为纵向先验。
method: 提出级联规划框架，将纵向规划条件化于已规划的路径上，实现路径-速度协调。
result: 实验结果显示该方法在协调性、安全性和规划质量上均优于并行方案。
conclusion: 路径条件化纵向规划是一种简单有效的协调机制，可提升端到端规划的安全性。
---

## Abstract
End-to-end autonomous driving has rapidly progressed, enabling joint perception and planning in complex environments. In the planning stage, state-of-the-art (SOTA) end-to-end autonomous driving models decouple planning into parallel lateral and longitudinal predictions. While effective, this parallel design can lead to i) coordination failures between the planned path and speed, and ii) underutilization of the drive path as a prior for longitudinal planning, thus redundantly encoding static information.
To address this, we propose a novel cascaded framework that explicitly conditions longitudinal planning on the drive path, enabling coordinated and collision-aware lateral and longitudinal planning. Specifically, we introduce a path-conditioned formulation that explicitly incorporates the drive path into longitudinal planning. Building on this, the model predicts longitudinal displacements along the drive path rather than full 2D trajectory waypoints. This design simplifies longitudinal reasoning and more tightly couples it with lateral planning. Additionally, we introduce a planning-oriented data augmentation strategy that simulates rare safety-critical events, such as vehicle cut-ins, by adding agents and relabeling longitudinal targets to avoid collision. Evaluated on the challenging Bench2Drive benchmark, our method sets a new SOTA, achieving a driving score of 89.07 and a success rate of 73.18\%, demonstrating significantly improved coordination and safety.

---

## 论文详细总结（自动生成）

# AlignDrive：面向端到端自动驾驶的对齐横向-纵向规划

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：当前最先进的端到端自动驾驶模型在规划阶段将横向（路径）和纵向（速度）规划解耦并并行执行。这种并行设计导致两个关键缺陷：一是规划的路径与速度之间容易产生协调失败（如路径突然转向但速度未调整），二是纵向规划未充分利用已规划的路径作为先验信息，冗余编码了静态场景信息，增加了计算负担。
- **意义**：实现安全、协调的横向-纵向规划是端到端自动驾驶实用化的关键瓶颈。本文旨在通过级联框架显式利用路径指导纵向规划，从而提升规划的安全性和协调性。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：提出**级联规划框架**，将纵向规划显式条件化于已规划的路径上，实现路径-速度的协同预测。
- **关键技术细节**：
  - **路径条件化纵向规划**：模型先预测一条驱动路径（lateral planning），然后在此路径上预测纵向位移（longitudinal displacement），而非直接预测完整的2D轨迹点。这使得纵向推理更简单、与横向规划更紧密耦合。
  - **公式/算法**：将纵向规划问题转化为沿路径的一维位移预测，同时引入路径条件概率建模，确保速度与路径一致。
  - **规划导向的数据增强**：模拟罕见的安全关键事件（如车辆切入），通过添加虚拟障碍物并重新标注纵向目标（避免碰撞），提升模型在危险场景下的鲁棒性。
- **整体流程**：输入感知特征 → 路径规划（lateral）→ 基于路径的纵向规划（longitudinal）→ 输出协调轨迹。

## 3. 实验设计
- **数据集/场景**：使用 **Bench2Drive** 基准，该基准包含多类复杂驾驶场景（城市、高速等），侧重评估规划安全性和协调性。
- **对比方法**：与当前SOTA端到端模型（如UniAD、VAD、ST-P3等）进行对比，同时进行自身的消融研究。
- **评价指标**：驾驶得分（Driving Score）、成功率（Success Rate）等。在Bench2Drive上，AlignDrive达到驾驶得分89.07、成功率73.18%，超越所有对比方法。

## 4. 资源与算力
- **未明确说明**：论文正文及摘要中未提及具体使用的GPU型号、数量、训练时长等算力信息。仅提到在Bench2Drive上进行评测，但训练细节缺失。

## 5. 实验数量与充分性
- **实验组数**：至少包括：主实验（与多个SOTA对比）、消融实验（验证路径条件化、数据增强等各组件的有效性）；可能还包含不同场景下的子集分析。但论文中未列出完整消融表，仅给出最终指标。
- **充分性评估**：
  - **充分**：主实验对比方法全面（涵盖主流端到端模型），结果显著提升。
  - **不足**：缺乏在多个不同数据集（如nuScenes、Waymo）上的泛化验证；消融细节和统计显著性未充分展示；对失败案例的分析较少，可能高估了方法的鲁棒性。

## 6. 主要结论与发现
- 级联的路径条件化纵向规划框架能有效消除并行规划中的协调失败问题，显著减少碰撞风险。
- 将纵向规划简化为沿路径的一维位移预测，不仅降低了复杂度，还提升了推理效率与准确性。
- 规划导向的数据增强有助于提升模型在长尾安全场景下的表现。
- 在Bench2Drive上取得新SOTA，验证了方法的有效性与先进性。

## 7. 优点
- **方法简洁有效**：级联思路直观，修改量小，但带来显著改善。
- **数据增强独特**：针对规划安全的仿真增强，填补了现有方法对罕见事件覆盖的空白。
- **实验验证扎实**：在公认的复杂基准Bench2Drive上达到最高分数，对比公平。
- **可解释性**：路径条件化使得规划过程更可解释（速度随路径变化）。

## 8. 不足与局限
- **实验覆盖有限**：仅在Bench2Drive单一数据集上评测，未在nuScenes、Waymo等经典基准上验证，结论的泛化性存疑。
- **算力资源不明**：未提供训练成本，难以评估实际部署门槛。
- **消融不充分**：缺乏对不同组件贡献的定量分析，例如单独去掉数据增强或路径条件化的性能变化未详细列出。
- **潜在偏差**：数据增强可能引入仿真与实际分布不一致的风险；模型在极端动态场景（如多车同时切入）的表现未考察。
- **应用限制**：当前框架假定路径规划足够准确，若路径本身有误则纵向规划会继承错误；未考虑横向-纵向双向协调（只单向依赖）。

（完）
