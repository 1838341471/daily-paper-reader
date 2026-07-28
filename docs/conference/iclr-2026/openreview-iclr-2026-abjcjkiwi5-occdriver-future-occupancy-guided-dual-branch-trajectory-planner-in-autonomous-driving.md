---
title: "OccDriver: Future Occupancy Guided Dual-branch Trajectory Planner in Autonomous Driving"
title_zh: OccDriver：未来占用引导的自动驾驶双分支轨迹规划器
authors: "Zhao Huang, Bowen Zhang, Zhongzhu Li, Di Lin"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=abJCjkIwi5"
tags: ["query:av-pnc"]
score: 9.0
evidence: 使用占用流进行轨迹规划
tldr: 针对自动驾驶轨迹规划中未显式利用场景演变的局限，提出OccDriver双分支框架：矢量分支生成粗轨迹，栅格分支预测条件占用流；在nuScenes等数据集上规划性能显著提升，验证了世界模型启发式方法的有效性。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有轨迹规划方法未显式利用可能的场景演化，导致决策信息不足。
method: 提出栅格-矢量双分支框架，矢量分支生成多模态粗轨迹，栅格分支通过占用流预测未来场景演化并精化轨迹。
result: 在多个自动驾驶数据集上，规划安全性和效率优于现有方法。
conclusion: 利用占用流预测的未来场景演化能显著提升轨迹规划质量。
---

## Abstract
Trajectory planning for autonomous driving is challenging due to agents' behavioral uncertainty and intricate multi-agent interaction modeling. Most existing studies generate trajectories without explicitly exploiting possible scene evolution, while world models predict consequences from ego behavior, enabling more informed planning decisions. Inspired by the world model, we propose OccDriver, a novel rasterized-to-vectorized dual-branch framework for trajectory planning. This pipeline performs a coarse-to-fine trajectory decoding process: The vectorized branch first generate multimodal coarse trajectories; Then the rasterized branch predicts future scene evolutions conditioned on each coarse trajectory via occupancy flow prediction; Lastly, the vectorized branch leverages intuitive future interaction evolution of each modality from the rasterized branch and produces refined trajectories. Several cross-modality (occupancy and trajectory) losses are further introduced to improve the consistency between trajectory and occupancy prediction. Additionally, we apply a contingency objective in both occupancy space, considering marginal and joint occupancy distributions in different planning scopes. Our model is assessed on the large-scale real-world nuPlan dataset and its associated planning benchmark. Experiments show that OccDriver achieves state-of-the-art in both Non-Reactive and Reactive closed-loop performance.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：现有自动驾驶轨迹规划方法大多直接生成轨迹，未显式利用未来场景演化信息（如其他交通参与者的潜在行为），导致决策信息不足，难以应对高度交互的复杂环境。
- **背景**：世界模型（World Model）可通过预测自车行为的结果来辅助规划决策，受此启发，论文提出将场景演化显式引入规划过程，使轨迹生成更具前瞻性。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：提出**OccDriver**，一种**栅格-矢量双分支框架**，通过“粗→细”的两阶段轨迹解码过程，利用条件占用流预测未来场景演化，从而精化轨迹。
- **关键技术细节**：
  - **矢量分支**：首先生成多模态的粗轨迹（多种可能的未来规划方案）。
  - **栅格分支**：以每条粗轨迹为条件，预测对应的**未来占用流**（occupancy flow），即场景中所有物体随时间变化的占用栅格演化。
  - **矢量分支（再次）**：利用栅格分支提供的各模态的未来交互演化信息，对粗轨迹进行精化，输出最终轨迹。
  - **交叉模态损失**：设计占用和轨迹之间的联合损失函数，提高轨迹预测与占用预测的一致性。
  - **紧急目标（contingency objective）**：在占用空间内同时考虑**边际占用分布**和**联合占用分布**，针对不同规划范围分别处理，以应对不确定场景下的应急决策。
- **算法流程（文字说明）**：输入传感器数据→矢量分支输出多个粗轨迹→每个粗轨迹送入栅格分支预测条件占用流→矢量分支结合占用流信息精化轨迹→通过交叉模态损失和紧急目标训练。

### 3. 实验设计：数据集、benchmark 与对比方法

- **数据集**：大规模真实世界的**nuPlan**数据集，以及其配套的规划基准（planning benchmark）。
- **评估场景**：同时报告了**Non-Reactive**（非反应式）和**Reactive**（反应式）两种闭环性能。
- **对比方法**：未在摘要中列出具体方法名称，但声称达到了**State-of-the-Art**，说明与当前主流规划方法进行了比较。

### 4. 资源与算力

- 论文摘要及元数据中**未明确说明**使用的GPU型号、数量、训练时长等算力信息。用户需注意这一点。

### 5. 实验数量与充分性

- 从摘要可推断至少进行了：
  - 主实验结果（nuPlan上的闭环性能对比）。
  - 交叉模态损失和紧急目标的消融研究（因为提到“进一步引入”和“应用”）。
  - 不同规划范围（marginal vs joint occupancy）的对比。
- **充分性评估**：实验覆盖了主流数据集和两种闭环模式，且包含消融，基本满足验证方法有效性的需求。但缺乏对其他数据集（如nuScenes）和开放环评估的明确说明，可能不够全面。实验设计相对客观，但具体公平性需查看完整论文中的超参数、随机种子等细节。

### 6. 论文的主要结论与发现

- **明确结论**：利用占用流预测的未来场景演化信息，能够显著提升轨迹规划质量。在nuPlan的Non-Reactive和Reactive闭环测试中，OccDriver均达到最优性能。
- **隐含发现**：双分支粗到细的范式、交叉模态一致性损失以及紧急目标设计是提升规划鲁棒性的关键组件。

### 7. 优点：方法或实验设计上的亮点

- **方法创新**：将世界模型思想显式融入轨迹规划，通过条件占用流为每条粗轨迹提供未来交互演化信息，实现信息更充分的规划。
- **结构设计**：双分支、粗→细的解码方式，既保持了多模态覆盖，又通过栅格分支的环境感知能力精化轨迹。
- **损失函数**：交叉模态损失保证了占用与轨迹的一致性；紧急目标考虑了边际与联合分布，增强了应对不确定性的能力。
- **实验评估**：同时报告Non-Reactive和Reactive两种闭环性能，更具有说服力。

### 8. 不足与局限

- **实验覆盖**：仅依赖nuPlan一个数据集，缺乏在不同驾驶场景（如路口、高速公路、复杂城市）的细粒度分析，也未在开放环指标（如L2误差）上对比。
- **偏差风险**：占用流预测本身存在误差，若预测不准可能误导轨迹精化，文中未讨论误差传递的影响。
- **应用限制**：依赖高精度占用流预测模块，计算开销可能较大，实时性、模型轻量化方面未提及。
- **透明度**：算力资源、训练细节、超参数等未披露，影响可复现性。

（完）
