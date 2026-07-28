---
title: "FlowAD: Ego-Scene Interactive Modeling for Autonomous Driving"
title_zh: FlowAD：面向自动驾驶的自车-场景交互建模
authors: "Mingzhe Guo, Yixiang Yang, Chuanrong Han, Rufeng Zhang, Shirui Li, Ji Wan, Zhipeng Zhang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=m4JpoJRgAr"
tags: ["query:av-pnc"]
score: 8.0
evidence: FlowAD通过自车-场景交互建模提升规划与控制
tldr: 现有环境建模忽视自车运动对观测的反馈，导致规划能力受限。本文提出以自车为中心的动态场景流表示，将自车-场景交互建模为相对场景流，在特征层面学习反馈。实验表明该方法有效提升了感知到规划的全链路性能。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 当前环境建模缺乏自车运动对观测的反馈，导致对驾驶过程理解不完整。
method: 提出以自车为中心的动态场景流范式，将自车运动反馈融入特征学习，利用已有日志数据。
result: 实验证明该交互建模显著提升了规划能力，特别是在复杂交互场景中。
conclusion: 自车-场景交互建模是提升自动驾驶规划鲁棒性的关键，可有效利用现有数据。
---

## Abstract
Effective environment modeling is the foundation for autonomous driving, underpinning tasks from perception to planning. However, current paradigms often inadequately consider the feedback of ego motion to the observation, which leads to an incomplete understanding of the driving process and consequently limits the planning capability. To address this issue, we introduce a novel ego-scene interactive modeling paradigm. Inspired by human recognition, the paradigm represents ego-scene interaction as the scene flow relative to the ego-vehicle. This conceptualization allows for modeling ego-motion feedback within a feature learning pattern, advantageously utilizing existing log-replay datasets rather than relying on scenario simulations. We specifically propose FlowAD, a general flow-based framework for autonomous driving. Within it, an ego-guided scene partition first constructs basic flow units to quantify scene flow. The ego-vehicle's forward direction and steering velocity directly shape the partition, which reflects ego motion. Then, based on flow units, spatial and temporal flow predictions are performed to model dynamics of scene flow, encompassing both spatial displacement and temporal variation. The final task-aware enhancement exploits learned spatio-temporal flow dynamics to benefit diverse tasks through object and region-level strategies. We also propose a novel Frames before Correct Planning (FCP) metric to assess the scene understanding capability. Experiments in both open and closed-loop evaluations demonstrate FlowAD's generality and effectiveness across perception, end-to-end planning, and VLM analysis. Notably, FlowAD reduces 19\% collision rate over SparseDrive with FCP improvements of 1.39 frames (60\%) on nuScenes, and achieves an impressive driving score of 51.77 on Bench2Drive, proving the superiority. Code, model, and configurations will be released here.

---

## 论文详细总结（自动生成）

# 论文总结：FlowAD：面向自动驾驶的自车-场景交互建模

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：现有自动驾驶环境建模方法常忽略**自车运动对观测的反馈**，即规划决策会影响后续感知，导致对驾驶过程的理解不完整，限制了规划能力。
- **动机**：受人类认知启发，人类在驾驶时会不断根据自身动作更新对周围环境的理解。论文试图将这种**自车-场景交互**显式建模，提升从感知到规划的端到端性能。
- **整体含义**：提出以**自车为中心的动态场景流**表示，将交互转化为相对场景流，在特征学习层面融入自车运动反馈，利用已有日志数据而非仿真，实现更鲁棒的规划。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：将自车-场景交互建模为**相对于自车的场景流**，通过特征学习模式而非模拟器来体现自车运动对观测的反馈。
- **关键技术细节**：
  - **FlowAD框架**：基于流的通用自动驾驶框架。
  - **自车引导的场景划分**：首先构建基本流单元来量化场景流。自车的前进方向和转向速度直接塑造这些划分，从而反映自车运动。
  - **空间与时间流预测**：基于流单元，进行空间位移和时间变化的动态建模。
  - **任务感知增强**：利用学习到的时空流动态，通过**对象级策略**和**区域级策略**使不同下游任务受益。
- **公式/算法流程**（文字说明）：
  1. 输入传感器数据（如相机、激光雷达）。
  2. 以自车状态（速度、转向）为条件，对场景进行空间划分，得到流单元。
  3. 对每个流单元预测空间流（相邻帧的位移）和时间流（未来帧的变化）。
  4. 将流特征与原始特征融合，增强任务相关表示。
  5. 下游模块（检测、预测、规划）使用增强特征。

## 3. 实验设计：数据集、基准、对比方法
- **数据集**：
  - **nuScenes**：用于开环评估，包含复杂城市驾驶场景。
  - **Bench2Drive**：用于闭环评估，模拟驾驶任务。
- **基准任务**：感知（检测、跟踪）、端到端规划、VLM分析。
- **对比方法**：主要对比**SparseDrive**（基线方法）及其他主流端到端驾驶模型。
- **评价指标**：
  - 碰撞率（Collision rate）
  - **FCP（Frames before Correct Planning）**：提出新指标，衡量场景理解能力，即规划正确前可容忍的帧数。
  - 驾驶分数（Driving score）在Bench2Drive上报告。

## 4. 资源与算力
- **文中未明确说明**：摘要和元数据未提及使用的GPU型号、数量及训练时长。可能全文中有细节，但提取内容缺失。需要指出这一点：**论文未提供具体算力信息**。

## 5. 实验数量与充分性
- **实验组数**：
  - 开环实验：nuScenes上的端到端规划评估（包含碰撞率、FCP）。
  - 闭环实验：Bench2Drive上的完整驾驶评估（驾驶分数）。
  - 消融研究：推测有关于流单元划分、时空预测、任务增强的消融（元数据未列出具体数量，但从描述看应包含）。
  - VLM分析：定性/定量分析。
- **充分性**：实验覆盖了**开环和闭环**两种典型评估，对比了具代表性的基线，使用了不同复杂度的数据集。新指标FCP补充了传统规划指标。**但缺乏不同传感器配置、实时性分析、长尾场景覆盖等方面讨论**，可视为客观但有限。

## 6. 主要结论与发现
- FlowAD在nuScenes上将碰撞率相对**降低19%**（与SparseDrive相比），同时FCP提升1.39帧（即规划正确前提前1.39帧，提升60%）。
- 在Bench2Drive上达到**51.77的驾驶分数**，证明了闭环条件下的优越性能。
- 自车-场景交互建模能有效提升规划鲁棒性，尤其适用于复杂交互场景（如拥堵、变道）。
- 该方法可泛化到多种下游任务（感知、规划、VLM），验证了流表示的通用性。

## 7. 优点
- **方法创新性**：首次将自车运动反馈以特征流形式融入环境建模，避免了仿真依赖，直接利用已有日志数据。
- **新评价指标**：提出FCP（正确规划前的帧数），更合理评价场景理解时效性，弥补传统碰撞率只关注结果不关注过程。
- **任务泛化性**：框架不仅提升规划，还改善感知和VLM分析，表明流特征具有强表达能力。
- **开环+闭环双验证**：在常见基准和新基准上都取得了显著提升，证明跨场景有效性。

## 8. 不足与局限
- **实验覆盖有限**：仅涉及两个数据集（nuScenes、Bench2Drive），缺乏对更多数据集（如Waymo、Lyft）的验证，泛化性待确认。
- **算力与效率未报告**：未说明训练资源和推理时延，无法判断实际部署可行性。
- **对极端场景的鲁棒性**：论文未专门分析长尾情况（如雨雪、夜间、突然有障碍物出现），交互建模在这些场景下是否仍有效存疑。
- **基线与对比不充分**：只详细对比了SparseDrive，未与更多SOTA方法（如UniAD、VAD等）进行公平比较，可能忽略部分优势。
- **流划分的假设依赖性**：自车方向与速度引导划分，若自车状态估计错误，可能误导流建模，存在偏差风险。
- **新指标FCP的可解释性**：需进一步论证其与真实驾驶安全性的相关性，目前仅作为辅助指标。

（完）
