---
title: "ADDI: A Simplified E2E Autonomous Driving Model with Distinct Experts and Implicit Interactions"
title_zh: ADDI：具有不同专家和隐式交互的简化端到端自动驾驶模型
authors: "Dapeng Zhang, Zhenlong Yuan, Chenyang Li, Yinda Chen, Shiyue Zhao, Hongtao Nie, Rui Zhou, Qingguo Zhou"
date: 2025-09-05
pdf: "https://openreview.net/pdf?id=LnbMSnQpXb"
tags: ["query:av-pnc"]
score: 8.0
evidence: 简化的端到端自动驾驶模型
tldr: 针对传统模块化自动驾驶破坏任务连贯性的问题，提出ADDI：将检测-建图、预测和规划集成到统一框架，通过隐式交互取代显式连接；实验表明在规划效率与性能上超越分治方法，实现更紧凑的端到端系统。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 模块化方法分解感知、预测、规划导致子任务间不连贯，效率低下。
method: 设计统一检测模块整合跟踪与建图，并利用隐式交互连接预测与规划。
result: 规划性能提升，系统计算效率更高。
conclusion: 隐式交互和统一模型能简化端到端自动驾驶并提升效果。
---

## Abstract
End-to-end autonomous driving has emerged as a promising research trend aimed at achieving autonomy from a human-like driving perspective. Traditional solutions often divide the task into four sub-tasks—tracking-by-detection, online mapping, prediction, and planning—with several interactions to polish planning. However, this modular approach disrupts the cohesion of autonomous driving by ecomposing these processes and then linking them through interactions, leading to suboptimal and inefficient practical applications. To address this limitation, we propose ADDI, a simple and efficient end-to-end autonomous driving method. First, ADDI integrates tracking-by-detection and online mapping through a unified detection module paired with distinct expert designs, enabling simultaneous output of detection and mapping elements. Second, ADDI employs a unified motion planning model with distinct experts to jointly predict agent trajectories and ego planning trajectories. With this unified model structure, most interactions required by previous methods are rendered unnecessary. ADDI implements two implicit (resource-free) and two explicit interactions to associate the different components. Experimental results demonstrate that ADDI achieves state-of-the-art performance on both open-loop and closed-loop benchmarks while running significantly faster than prior end-to-end methods.

---

## 论文详细总结（自动生成）

# 论文总结：ADDI：具有不同专家和隐式交互的简化端到端自动驾驶模型

## 1. 核心问题与整体含义（研究动机和背景）
- **传统模块化自动驾驶**将任务分解为四个子任务：检测跟踪、在线建图、预测和规划，并通过多次显式交互来优化规划结果。这种分解方式破坏了自动驾驶任务的连贯性，导致子任务间信息传递不充分、效率低下，实际应用效果欠佳。
- **论文目标**：提出一种简化的端到端自动驾驶模型 ADDI，通过统一不同模块、引入隐式交互，在保持高性能的同时显著提升系统计算效率。

## 2. 方法论：核心思想与关键技术细节
- **核心思想**：将“检测-建图”、“预测”和“规划”整合到一个统一的框架中，使用**不同专家（Distinct Experts）** 处理各自子任务，并通过**隐式交互（Implicit Interactions）** 替代传统方法中大量的显式交互，减少不必要的连接，简化系统结构。
- **关键技术细节**：
  - **统一检测模块**：将目标的检测跟踪（tracking-by-detection）与在线建图（online mapping）合并为一个统一的检测模块，并配以不同的专家设计，同时输出检测结果和地图元素。
  - **统一运动规划模型**：采用带不同专家的统一运动规划模型，同时预测其他智能体的轨迹（agent trajectories）和自车的规划轨迹（ego planning trajectories）。
  - **交互方式**：使用两种**隐式交互（无计算开销）** 和两种显式交互来关联不同组件。隐式交互的引入使得之前方法所需的许多显式交互变得不再必要。
- **公式/算法流程**（文本描述）：
  1. 输入多模态传感器数据（摄像头、激光雷达等，原文未明确但属于常规端到端流程）。
  2. 通过统一检测模块同时输出目标检测框、跟踪信息及地图元素。
  3. 将检测结果与地图信息输入统一运动规划模型，该模型内部由不同专家分别处理预测和规划，并通过隐式/显式交互进行信息传递。
  4. 输出自车规划轨迹（用于控制），同时输出其他智能体的预测轨迹（可选用于评估或监督）。

## 3. 实验设计
- **数据集/场景**：论文在**开环（open-loop）和闭环（closed-loop）基准**上进行了评估。具体数据集名称未在摘要中明确，但根据端到端自动驾驶领域常见基准（如nuScenes、CARLA等），推测使用了相关数据集（需要原文进一步确认）。
- **对比方法**：与先前最先进的端到端自动驾驶方法进行了对比，重点报告了运行速度（显著快于先前方法）和性能（达到SOTA）。
- **指标**：未在摘要中详细列出，但通常包括规划成功率、碰撞率、舒适性、效率等（需参考原文）。

## 4. 资源与算力
- **论文未明确说明**使用的GPU型号、数量及训练时长等算力信息。根据领域惯例，此类端到端模型通常需要多张高端GPU（如NVIDIA A100或RTX 3090）进行数天训练，但基于现有摘要和元数据无法给出具体数值。

## 5. 实验数量与充分性
- **实验数量**：摘要仅提到在开环和闭环两类基准上进行了实验，并对比了多种先前方法，但未列出具体消融实验（如是否对隐式交互数量、专家设计等进行消融）或不同场景下的详细结果。元数据中的tldr也仅概括性能提升和计算效率，未提供实验组数。
- **充分性评估**：虽然达到了SOTA，但缺乏对消融实验、不同隐式交互设计的效果分析、以及在不同困难场景下的鲁棒性测试。因此目前展示的实验证据**不够充分**，需参考完整论文来确认其公平性和全面性。例如，是否与多种基线方法在同一条件下公平比较（相同数据集、相同后处理步骤等）尚未说明。

## 6. 主要结论与发现
- 提出的ADDI模型在**开环和闭环基准上均达到最先进的规划性能**。
- 同时，ADDI的**运行速度显著快于之前的端到端方法**，验证了通过隐式交互和统一模型简化结构能够有效提升效率。
- 隐式交互能够替代大量显式交互，降低系统复杂度而不牺牲性能。

## 7. 优点
- **结构简洁**：将检测、建图、预测、规划集成到统一框架，减少了模块间显式连接的冗余。
- **效率高**：隐式交互设计无额外计算开销，使得整个推理速度更快。
- **性能优异**：在主流基准测试上达到SOTA，表明简化策略并未损害规划质量。
- **创新性**：提出“不同专家+隐式交互”的范式，为端到端自动驾驶设计提供了新思路。

## 8. 不足与局限
- **实验覆盖有限**：仅基于开环和闭环基准，未提及在真实世界部署、多种天气/光照条件下的验证；消融实验不足，难以判断每个设计的贡献。
- **隐式交互的通用性**：是否对所有场景都能保持鲁棒？在极端交互情况下（如密集交通流、道路参与者故意违规）是否可能失效？论文未讨论。
- **训练复杂度**：虽然推理快，但统一模型训练时可能需要更复杂的多任务损失平衡策略，且训练成本可能依然较高（未说明）。
- **应用限制**：依赖于传感器数据质量和同步性，对于缺乏高保真传感器输入的车辆可能效果下降。此外，未提供与模块化方法在故障诊断、可解释性等方面的对比。

（完）
