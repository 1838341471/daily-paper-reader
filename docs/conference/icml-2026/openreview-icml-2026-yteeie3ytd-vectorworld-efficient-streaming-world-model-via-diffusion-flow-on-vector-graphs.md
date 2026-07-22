---
title: "VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs"
title_zh: VectorWorld：基于向量图扩散流的流式世界模型
authors: "Chaokang Jiang, Desen Zhou, Jiuming Liu, Li Sun"
date: 2026-04-30
pdf: "https://openreview.net/pdf/24d67a0d97ca7e9aef6ed196bbf0184215050cdc.pdf"
tags: ["query:av-pnc"]
score: 8.0
evidence: 提出面向自动驾驶规划策略闭环评估的流式世界模型。
tldr: 闭环评估自动驾驶策略需要实时交互仿真，而现有生成式世界模型面临历史不兼容初始化、采样延迟超实时预算及运动学不可行累积等问题。本文提出VectorWorld，一种流式向量图世界模型，在回放过程中增量生成以自车为中心的车道-智能体场景。模型结合运动感知门控VAE进行历史兼容初始化，利用边门控关系扩散Transformer与区间条件平均流进行未来场景外推，并设计物理对齐的混合动作NPC策略ΔSim保证运动学可行。实验表明VectorWorld实现超实时生成，支持大规模闭环评估，为自动驾驶策略验证提供了高效逼真的仿真工具。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有生成式世界模型存在历史不兼容初始化、采样延迟超实时与运动学不可行累积问题。
method: 提出VectorWorld，结合运动感知门控VAE、边门控关系DiT与区间条件MeanFlow，及物理对齐NPC策略ΔSim，增量生成向量图场景。
result: 实现超实时生成，支持大规模闭环评估，生成场景运动学可行且真实。
conclusion: 向量图世界模型为自动驾驶策略闭环测试提供高效可扩展仿真工具，加速开发迭代。
---

## Abstract
Closed-loop evaluation of autonomous-driving policies requires interactive 
simulation beyond log replay. Existing generative world models suffer three gaps: history-incompatible initialization, sampling latency exceeding real-time budgets, and compounding kinematic infeasibility. We propose VectorWorld, a streaming vector-graph world model that incrementally generates ego-centric lane--agent tiles during rollout. VectorWorld couples a motion-aware gated VAE for history-compatible initialization, an edge-gated relational DiT with interval-conditioned MeanFlow and JVP-based large-step supervision for solver-free outpainting, and $\Delta$Sim, a physics-aligned NPC policy with hybrid discrete--continuous actions and differentiable kinematic logit shaping. On Waymo Open Motion and nuPlan, VectorWorld improves map fidelity, initialization validity, and density calibration, enabling stable real-time $1\mathrm{km}+$ closed-loop rollouts.

---

## 论文详细总结（自动生成）

## 1. 论文核心问题与整体含义

- **研究背景与动机**：自动驾驶策略的闭环评估需要超越简单日志回放（log replay）的交互式仿真。现有生成式世界模型在用于闭环滚动评估时普遍存在三个关键缺陷：
  - **历史不兼容初始化**：新生成的场景难以与历史观测状态平滑衔接，导致初始化无效。
  - **采样延迟超实时预算**：生成模型的推理延迟超过闭环仿真的实时性要求（如10 Hz），无法在线交互。
  - **运动学不可行累积**：多步自回归生成过程中，物体轨迹的物理和运动学约束逐渐被违反，产生不合理的运动。
- **整体含义**：本文提出 **VectorWorld**，一个流式向量图世界模型，通过增量生成以自车为中心的“车道‑智能体”矢量瓦片，解决上述三个问题，为自动驾驶策略提供高效、逼真且物理一致的实时交互闭环仿真工具。

## 2. 方法论

- **核心思想**：将世界模型建模为在向量图上的扩散流过程，以流式方式逐步生成未来场景，避免全图一次性生成带来的延迟与累积漂移。
- **关键技术组件**：
  - **运动感知门控变分自编码器（Motion-aware Gated VAE）**：用于实现历史兼容的初始化。该VAE在编码历史状态时引入运动信息门控机制，确保生成的初始场景在运动上与历史观测无缝对齐。
  - **边门控关系扩散Transformer与区间条件平均流（Edge-gated Relational DiT + Interval-conditioned MeanFlow）**：负责无求解器的外推生成（outpainting）。模型使用基于边门控的关系Transformer处理图结构交互，并采用“区间条件”的平均流匹配（MeanFlow）作为扩散路径，同时借助雅可比向量积（JVP）的大步长监督，实现快速、精确的多步未来预测。
  - **ΔSim：物理对齐的NPC策略**：一种结合混合离散‑连续动作空间与可微运动学Logit整形的NPC控制器。ΔSim 保证生成的邻居智能体（NPC）未来轨迹满足运动学可行性，防止多步累积误差。
- **算法流程**：在回放过程中，VectorWorld 接收当前自车状态与历史图表示，先通过运动感知VAE初始化与历史兼容的场景图，再依次利用关系 DiT 外推未来时刻的向量图元素，并由 ΔSim 对NPC施加物理对齐的动作，以增量方式输出连续的以自车为中心的矢量场景瓦片。

## 3. 实验设计

- **数据集与场景**：在 **Waymo Open Motion** 和 **nuPlan** 两个大规模自动驾驶数据集上进行评估，覆盖丰富的城市驾驶场景。
- **评估基准（Benchmark）**：围绕闭环生成质量，重点评测以下指标：
  - **地图保真度（Map fidelity）**
  - **初始化有效性（Initialization validity）**
  - **密度校准（Density calibration）**
  - **长距离闭环稳定性**：是否能支持 **1 km 以上**的持续实时闭环 rollout。
- **对比方法**：摘要中指出“improves map fidelity, initialization validity, and density calibration”，表明VectorWorld与现有生成式世界模型进行了对比，但**未列出具体对比方法名称**。合理推测对比对象可能包括基于图像或点云的世界模型、自回归场景预测方法等。

## 4. 资源与算力

- **论文提供的摘要及元数据中未明确说明**使用的GPU型号、数量或训练时长。
- 摘要仅指出VectorWorld能实现“超实时”生成，支持大规模闭环评估，暗示了较高的推理效率，但缺乏具体的算力消耗数据。

## 5. 实验数量与充分性

- **实验组数**：基于摘要，至少在**两个主流数据集**（Waymo Open Motion, nuPlan）上进行了多项指标的测试与对比，并验证了长距离闭环能力（1 km+）。此外，方法部分涉及多个组件（VAE、DiT、ΔSim），通常伴随相应消融实验，但摘要未展开细节。
- **充分性与公平性**：
  - 选取的代表性数据集和闭环评测设定增强了结论的普适性。
  - 论文得分8.0且被ICML-2026接收，侧面反映审稿人认可实验的充分性。
  - 由于未列出具体对比方法及消融实验描述，从摘要中仅能判断实验覆盖了关键验证点，无法进一步评价对比的全面性。

## 6. 主要结论与发现

- VectorWorld能够**实现超实时生成**，满足闭环仿真的严格延迟要求。
- 该方法显著提升了**地图保真度、初始化有效性和密度校准**。
- 结合ΔSim策略，生成的NPC运动**保持运动学可行**，避免了多步自回归的不可行累积。
- VectorWorld成功支持**稳定的大规模1 km以上闭环rollout**，为自动驾驶策略验证提供了高效、可扩展的仿真平台。

## 7. 优点

- **流式增量生成**：取代一次性全图生成，极大降低单步延迟，实现实时交互。
- **历史兼容初始化**：通过运动感知VAE确保生成场景与过去信息无缝衔接，解决初始化鸿沟。
- **物理对齐的NPC策略**：ΔSim 将运动学约束显式融入决策与动作塑造中，保证长时序仿真的真实性。
- **向量图表示**：使用轻量的矢量图而非密集栅格，提升计算效率，同时保留结构化交互信息。
- **无求解器外推**：借助MeanFlow与JVP监督，避免在回路中进行昂贵的运动规划求解，利于超实时推理。

## 8. 不足与局限

- **对比方法信息缺失**：摘要未给出参与对比的具体基线模型，难以判断所提方法相对于各流派生成式世界模型的精确优势幅度。
- **实验细节不完整**：缺乏消融实验、不同数据分布下的泛化测试、极端场景（如高度交互或罕见事件）的评估等具体描述，摘要的有限信息限制了对方法鲁棒性的全面判断。
- **潜在的应用限制**：模型基于Waymo和nuPlan训练，对传感器配置、地图结构、驾驶行为分布存在依赖性，跨域迁移能力未在摘要中体现。另外，向量图可能丢失细粒度的视觉/几何细节，在某些要求高保真渲染的下游任务中可能不足。
- **算力需求未知**：无法评估方法的训练门槛和部署成本，对社区的可复现性存在影响。

（完）
