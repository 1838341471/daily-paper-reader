---
title: "From Language to Driving: A Dual-Loop SLM-Enhanced Framework for Multi-Planner Scheduling via a Domain-Specific Language"
title_zh: 从语言到驾驶：基于领域专用语言的双环SLM增强多规划器调度框架
authors: "Jiawei Liu, Xun Gong, Muli Yang, Xingrui Yu, Fen Fang, Xulei Yang, Ivor Tsang, Yunfeng Hu, Hong Chen, Qing Guo"
date: 2026-07-01
pdf: "https://aclanthology.org/2026.acl-long.1381.pdf"
tags: ["query:av-pnc"]
score: 9.0
evidence: 通过多运动规划器调度将自然语言指令转化为车辆控制
tldr: 针对自动驾驶中执行乘员自然语言指令的问题，提出一种双环SLM增强框架，外层用小语言模型进行低频语义推理与多运动规划器调度，内层实现高频执行与车辆控制，通过领域专用语言和滚动时域调度补偿模型容量限制，实现了从语言指令到安全驾驶的透明决策链。
source: ACL-2026-Long
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 608, \"height\": 604, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1596, \"height\": 844, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1586, \"height\": 343, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 798, \"height\": 539, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 800, \"height\": 867, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1587, \"height\": 320, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1584, \"height\": 315, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1585, \"height\": 321, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1596, \"height\": 1093, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-010.webp\", \"caption\": \"\", \"page\": 0, \"index\": 10, \"width\": 1601, \"height\": 1063, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-011.webp\", \"caption\": \"\", \"page\": 0, \"index\": 11, \"width\": 1599, \"height\": 728, \"label\": \"Figure\"}, {\"url\": \"assets/figures/acl-2026-long/anthology-2026acl-long1381/fig-012.webp\", \"caption\": \"\", \"page\": 0, \"index\": 12, \"width\": 1598, \"height\": 679, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1381/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1595, \"height\": 509, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1381/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 801, \"height\": 200, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1381/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 497, \"height\": 251, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1381/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1439, \"height\": 865, \"label\": \"Table\"}, {\"url\": \"assets/tables/acl-2026-long/anthology-2026acl-long1381/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 495, \"height\": 249, \"label\": \"Table\"}]"
motivation: 实现从乘员自然语言指令到安全驾驶的协同自主性，需要透明、可靠的多规划器调度。
method: 提出双环框架：外环SLM进行高层语义推理与滚动时域调度，内环执行控制指令。
result: 框架有效桥接语言指令与车辆控制，证明小语言模型在驾驶调度中的可行性。
conclusion: 该工作推进了人车协同自主性，为语言指令驱动的自动驾驶规划提供了新范式。
---

## Abstract
Advancing from usable to collaborative autonomy requires driving systems to execute passenger instructions safely and reliably. This work formulates instruction realization as scheduling across multiple motion planners and presents a dual-loop framework that provides a transparent decision chain from natural language to vehicle control. The outer loop uses a small language model (SLM) for high-level, low-frequency semantic reasoning and schedule generation, while the inner loop performs low-level, high-frequency schedule execution and vehicle control. To compensate for the SLM’s limited capacity, the framework integrates receding-horizon scheduling to segment long-horizon instruction tasks, a domain-specific language (DSL) that restricts SLM outputs to a scheduling-oriented subspace, and reinforcement learning in high-fidelity urban traffic to refine the SLM’s DSL proficiency and scheduling performance. Experiments show that the framework improves instruction-completion rates while maintaining high safety and compliance relative to multiple baselines.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **核心问题**：在协作式自动驾驶场景中，如何将乘员发出的自然语言指令（如“开到路边停车”或“超过前面那辆慢车”）安全、可靠地转化为车辆可执行的运动规划与底层控制动作。此过程涉及在多个专用运动规划器（换道、跟车、泊车等）之间进行合理调度。
- **整体含义**：该工作将指令执行问题形式化为**多运动规划器的调度问题**，旨在建立一条从自然语言到车辆控制的**透明决策链**，推动自动驾驶系统从“可用”走向“协同自主”，使人、车能够以语言为接口高效协作。

### 2. 论文提出的方法论
核心思想是构建一个**双环架构**，通过分离低频推理与高频执行，并引入领域约束来弥补小语言模型（SLM）的容量限制。关键技术细节如下：
- **外层低频语义环（Outer Loop）**
  - **角色**：负责高层次语义理解、情景推理与调度计划生成，运行频率低。
  - **调度器**：使用一个**小语言模型（SLM）** 作为核心推理单元，将感知模块输出的场景描述与乘客指令转化为可执行的调度序列（如“执行变道规划器→执行跟车规划器”）。
  - **滚动时域调度（Receding-Horizon Scheduling）**：将长时域指令任务切分为一系列短时域调度段，逐步推进，从而补偿 SLM 处理长上下文和长期规划能力的不足。
  - **领域专用语言（Domain-Specific Language, DSL）**：定义了一套受限的语法与词汇空间，将 SLM 的输出严格约束在调度相关的子空间内，避免生成无意义或不可执行的结果，并增强输出的可解释性。
  - **强化学习精调（RL Fine-tuning）**：在高保真城市交通仿真环境中，利用强化学习对 SLM 进行训练，使其在遵循 DSL 约束的前提下，优化调度策略，提升指令完成率和安全性。
- **内层高频执行环（Inner Loop）**
  - **角色**：负责低层次、高频率的调度计划执行与车辆底层控制（如转向、油门、刹车）。
  - **执行**：接收外环下发的调度指令，激活对应的运动规划器，并执行闭环车辆控制。内环专注于实时响应，保证控制的连续性和稳定性。

### 3. 实验设计
- **数据集与场景**：文中提及使用**高保真城市交通仿真环境**进行训练与评估，但未点出具体仿真器名称（如 CARLA、SUMO 等）或自定义数据集。驾驶场景涵盖多运动规划器协同执行的任务。
- **Benchmark 与对比方法**：摘要指出与**多个基线方法**进行了对比，但未列出基线具体名称。推测可能包含基于规则的手动调度、直接使用 LLM/SLM 无额外约束的方法、无滚动时域或 DSL 的消融变体等。
- **评价指标**：核心指标包含**指令完成率（Instruction-Completion Rate）**、**安全性**与**合规性**（如交通规则遵守情况）。

### 4. 资源与算力
- **算力信息**：所提供摘要与元数据中**未明确说明**使用的 GPU 型号、数量、训练时长等算力细节。由于框架中集成了 SLM 和 RL 训练，推测存在一定算力开销，但具体规模无法从现有信息中得知。

### 5. 实验数量与充分性
- **实验数量**：虽然摘要未列出具体实验表格，但提到与多个基线对比，并验证了指令完成率、安全性与合规性。结合框架复杂度（包含 DSL、滚动时域、RL 精调等模块），很可能包含**主流对比实验**及**各模块的消融实验**，以证明各组件的必要性。
- **充分性与公平性**：从动机和方法设计看，实验应覆盖了控制变量的消融和代表性能对比，一定程度上支撑了结论；但因缺乏对数据集规模、场景多样性的详细说明，其统计意义和外部有效性尚难以独立判断。公平性方面，若能统一感知输入和环境设置，对比基础应是合理的。

### 6. 论文的主要结论与发现
- 所提出的**双环 SLM-增强框架**能够有效桥接自然语言指令与车辆控制，实现从语义理解到安全驾驶的闭环。
- 证明了在 DSL 约束与滚动时域调度辅助下，**小语言模型可以胜任驾驶域下的多规划器调度任务**，而不必依赖参数量巨大的大模型。
- 框架在**提升指令完成率的同时，可维持较高的安全水平与交规合规性**，相较于基线方法有显著优势。
- 该工作为人车协同自主性提供了一种**透明、可解释**的新范式，其决策链受 DSL 限制，便于追溯和审计。

### 7. 优点
- **架构创新**：双环设计将语义推理与实时控制解耦，兼顾了智能决策与高频执行的需求，降低了单一模块负责所有时域任务的负担。
- **算力友好与可部署性**：采用**小语言模型**替代大模型，结合 DSL 约束输出空间，更利于车载边缘设备部署。
- **可靠性增强**：通过 DSL 约束将输出空间限缩在安全调度子集中，从结构上减少了模型幻觉引发危险动作的风险；滚动时域调度增强了长序列任务的执行鲁棒性。
- **透明决策链**：从语言指令、DSL 调度表示到具体规划器的激活，形成可解释的因果链路，有助于调试和信任建立。
- **学习与优化结合**：引入 RL 在仿真中精调 SLM 的调度策略，使模型能够从闭环驾驶效果中自动改进，超越静态模仿学习。

### 8. 不足与局限
- **实验细节透明度不足**：未披露具体数据集、仿真平台、基线方法和详细的量化结果表格，难以精确评估方法的优越性边界和统计显著性。
- **泛化性未知**：主要在高保真仿真器上验证，**未能涵盖真实道路实测**；对多样化、带噪口音或模糊指令的鲁棒性未作说明。
- **SLM 能力瓶颈**：即使有 DSL 与滚动时域补偿，小语言模型对极度复杂、多意图交织或需深层常识推理的指令可能仍处理不佳。
- **安全边界依赖**：整体安全性仍依赖于 DSL 预定义动作空间的完备性，若出现未建模的边缘场景，上层调度可能失效。
- **偏差风险**：RL 训练中奖励函数的设计可能引入未预期的策略偏好，若仿真与现实差异较大，可能会在真实环境中暴露问题。

（完）
