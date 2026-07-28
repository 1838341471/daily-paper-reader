---
title: Combining Auxiliary Losses for Safer and More Robust Trajectory Prediction
title_zh: 结合辅助损失实现更安全、更鲁棒的轨迹预测
authors: "Ahmad Rahimi, Alexandre Alahi"
date: 2025-09-18
pdf: "https://openreview.net/pdf?id=nyO2yx9Fd2"
tags: ["query:av-pnc"]
score: 7.0
evidence: 结合辅助损失实现鲁棒轨迹预测，为规划提供支持
tldr: 轨迹预测模型常产生不遵守地图和交通规则的输出。本文重新审视并增强三种辅助损失，并通过自适应加权方案平衡多任务学习。实验结果表明三者组合能显著提升轨迹的合规性、覆盖率和鲁棒性，对下游规划具有重要价值。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 轨迹预测模型常产生离路或违反交通规则的输出，场景合规性差。
method: 重新设计并组合离路损失、方向一致性损失和多样性损失，并提出轻量级自适应加权方案。
result: 实验证明三者组合能有效提升轨迹的合规性和鲁棒性，优于现有多任务训练策略。
conclusion: 恰当组合辅助损失并自适应加权是提升轨迹预测场景合规性的实用方法。
---

## Abstract
Accurate trajectory prediction is essential for the safety and reliability of autonomous systems. Despite recent progress, models still struggle with scene compliance, often producing off-road or traffic-violating forecasts. We revisit and enhance three intuitive auxiliary objectives—Offroad Loss, Direction Consistency Loss, and Diversity Loss—that enhance map adherence, traffic rule compliance, and trajectory coverage. While each improves a specific aspect, our key finding is that only their combination delivers robust road-compliant predictions. To make this practical, we propose a lightweight adaptive weighting scheme that balances auxiliary losses automatically, succeeding where existing multi-task training strategies fail.
Extensive experiments on nuScenes and Argoverse 2 show consistent gains in safety and robustness without sacrificing accuracy, with 43\% decrease in off-road errors on average. Notably, under the SceneAttack benchmark, which perturbs road geometry to create out-of-distribution driving scenarios, our method reduces off-road errors by 25\%, demonstrating that learned road compliance transfers to unseen environments. Our plug-and-play package can be integrated into any trajectory predictor, and code will be released.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：当前轨迹预测模型虽然精度有所提升，但输出的轨迹常偏离道路或违反交通规则，缺乏场景合规性（scene compliance）。这种不安全预测会直接影响下游规划模块的安全性。
- **研究动机**：希望在不牺牲预测精度的前提下，提升轨迹预测对地图约束和交通规则的遵守能力，从而增强自动驾驶系统的整体可靠性。
- **整体含义**：通过组合并自适应加权三种辅助损失，能够显著减少离路错误，且学到场景合规性可泛化到未见过的道路几何形变中。

### 2. 论文提出的方法论：核心思想、关键技术细节、算法流程

- **核心思想**：重新审视并增强三个直观的辅助目标函数，通过轻量级自适应加权方案平衡多任务学习，使得组合后的损失能协同提升轨迹的合规性、覆盖率和鲁棒性。
- **关键技术细节**：
  - **Offroad Loss（离路损失）**：惩罚预测轨迹点位于可行驶区域外，强制模型学习地图边界。
  - **Direction Consistency Loss（方向一致性损失）**：确保预测方向与交通规则（如车道方向）一致。
  - **Diversity Loss（多样性损失）**：鼓励生成多种可行的轨迹模式，避免坍缩到单一模态，提高覆盖率和鲁棒性。
  - **自适应加权方案（Adaptive Weighting）**：轻量级方法，能自动平衡各辅助损失的权重，优于现有手动调权或固定加权策略。
- **算法流程（文字说明）**：
  1. 基于基础轨迹预测模型输出原始预测（多模态轨迹）。
  2. 分别计算三种辅助损失。
  3. 通过自适应机制动态调整各损失项的权重。
  4. 将加权后的辅助损失与主任务（如负对数似然）结合，联合优化。

### 3. 实验设计：数据集、Benchmark、对比方法

- **数据集**：nuScenes 和 Argoverse 2。
- **Benchmark**：SceneAttack（扰动道路几何以创建分布外驾驶场景的基准），用于评估泛化性。
- **对比方法**：摘要未列出具体方法名称，但提及对比了“现有多种多任务训练策略”（existing multi-task training strategies），可能包括固定加权、不确定性加权、GradNorm等。同时，论文将自己的方法与不加入辅助损失或仅加单个损失的基线对比。

### 4. 资源与算力

- **文中未明确说明**使用的GPU型号、数量或训练时长。摘要仅提到方法是“plug-and-play”，资源消耗轻量。具体算力信息需查阅原文附录或实验部分。

### 5. 实验数量与充分性

- **实验组数**：至少包括：
  - 在两个大规模真实数据集（nuScenes、Argoverse 2）上的主实验。
  - 消融实验：比较单独使用每种辅助损失 vs. 组合使用。
  - 场景攻击测试：在SceneAttack上的鲁棒性评估。
  - 可能还有与不同多任务加权策略的对比实验。
- **充分性评价**：实验覆盖了主流数据集、分布内/外场景、消融分析，能充分验证方法有效性。但缺少对更多基线方法的对比，以及不同预测模型架构的泛化性验证。总体实验设计较为合理。

### 6. 论文的主要结论与发现

- 单独使用任一辅助损失只能提升特定方面（如离路损失减少出界，但可能降低多样性），**只有三者的组合才能实现鲁棒的道路合规预测**。
- 提出的自适应加权方案可以有效平衡多目标任务，优于固定权重或现有复杂平衡策略。
- 在nuScenes和Argoverse 2上，平均离路错误降低43%。
- 在SceneAttack对抗性场景下，离路错误减少25%，表明学到的合规性可以泛化到未见过的道路形变。
- 方法可即插即用，不牺牲预测精度。

### 7. 优点

- **实用性**：提出的辅助损失直观、易实现，自适应加权方案轻量，易于集成到现有轨迹预测器中。
- **安全性提升显著**：离路错误降低43%，直接减少规划风险。
- **泛化性证明**：在分布外场景（道路几何被扰动）下仍有25%的离路错误降幅，说明学到了通用的场景约束。
- **实验设计全面**：包括消融、对抗测试、多数据集验证。

### 8. 不足与局限

- **未提及的具体对比方法**：摘要未给出与SOTA预测模型（如SceneTransformer、HiVT等）的直接对比，难以评估相对性能提升。
- **算力资源未公开**：训练成本不透明，可能影响实际部署评估。
- **实验场景覆盖有限**：仅考虑道路几何扰动，未考虑其他类型分布偏移（如交互行为变化、传感器噪声）。
- **依赖地图信息**：Offroad Loss和Direction Consistency Loss需要高精地图，在无地图场景或地图不准确时可能失效。
- **未讨论对下游规划安全性评估**：虽然声称更安全，但未直接评测规划器最终碰撞率、舒适度等指标。

（完）
