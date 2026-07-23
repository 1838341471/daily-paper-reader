---
title: "SafeDec: Constrained Decoding for Safe Autoregressive Generalist Robot Navigation Policies"
title_zh: SafeDec：自回归通用机器人导航策略的安全约束解码
authors: "Parv kapoor, Akila Ganlath, Michael Clifford, Changliu Liu, Sebastian Scherer, Eunsuk Kang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/6e455d6687e375fb048d677aeb7229056f70d05a.pdf"
tags: ["query:av-pnc"]
score: 7.0
evidence: 安全导航策略的约束解码，可应用于自动驾驶
tldr: 提出SafeDec，一种面向自回归机器人导航策略的约束解码框架，将安全规范表达为信号时序逻辑公式，确保生成的动作序列满足安全要求。该方法可用于自动驾驶车辆的安全规划与控制。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 端到端机器人导航策略缺乏行为正确性的显式保证，存在安全隐患。
method: 提出SafeDec，在解码时将STL安全规范作为约束，强制生成动作符合安全要求。
result: 在多种导航环境中实现安全动作生成，避免碰撞等风险。
conclusion: 为基于学习的导航策略提供了安全保障机制，对自动驾驶安全规划有借鉴意义。
---

## Abstract
Recent advances in end-to-end, multi-task robot policies based on transformer models have demonstrated impressive generalization to real-world embodied navigation tasks. Trained on vast datasets of simulated and real-world trajectories, these policies map multimodal observations directly to action sequences for physical execution. Despite promising real-world capabilities, these models are still data-driven and, therefore, lack explicit notions of behavioral correctness. We address this gap by introducing **SafeDec**, a constrained decoding framework for autoregressive, transformer-based robot navigation policies that enforces safety specifications expressed as Signal Temporal Logic (STL) formulas. Our method ensures that generated actions provably satisfy STL specifications under assumed dynamics at runtime without retraining while remaining agnostic of the underlying policy. 
We evaluate **SafeDec** on tasks from the CHORES benchmark for state-of-the-art embodied navigation policies across hundreds of procedurally generated environments and show that our decoding-time interventions are useful not only for filtering unsafe actions but also for conditional action generation. Videos are available at constrained-robot-fms.github.io.

---

## 论文详细总结（自动生成）

根据提供的论文摘要和元数据，我对 **SafeDec** 这篇论文进行结构化总结如下：

### 1. 论文的核心问题与整体含义
- **核心问题**：基于 Transformer 的端到端多任务机器人导航策略虽在真实世界展现了强大的泛化能力，但其本质仍是数据驱动，缺乏对行为正确性的显式保证，在安全关键场景（如自动驾驶、服务机器人）中存在不可忽视的风险。
- **整体含义**：本文试图在**不重新训练模型**的前提下，为现有自回归导航策略注入形式化安全约束，使动作序列在运行时必然满足给定的安全规范，从而弥合“强泛化”与“弱安全”之间的鸿沟。

### 2. 论文提出的方法论
- **核心思想**：提出 **SafeDec**——一个面向自回归 Transformer 导航策略的**约束解码**框架。它通过实时干涉模型的解码过程，确保每一步生成的动作（或整个动作序列）符合预先定义的安全规范。
- **关键技术细节**：
  - **安全规范形式化**：使用**信号时序逻辑（STL）** 公式表达安全需求（如避障、保持安全距离、速度限制等），将自然语言安全要求转化为可机读的严格逻辑。
  - **约束解码机制**：在策略自回归生成动作 token 序列时，基于假设的系统动力学模型，在线验证候选动作是否会使未来轨迹违反 STL 公式。不符合约束的动作将被直接过滤或修正，仅输出安全可行的动作。
  - **策略无关性**：SafeDec 完全独立于底层导航策略的内部结构与参数，可即插即用地集成到任何预训练的 Transformer 策略上，无需微调或重新训练。
- **算法流程概括**：给定状态与任务输入 → 导航策略自回归预测动作概率分布 → SafeDec 根据当前历史与动力学推测未来状态 → 用 STL 监视器检验候选动作的合规性 → 屏蔽违规动作并重新归一化概率 → 输出安全动作。该过程在每个解码时间步迭代执行。

### 3. 实验设计
- **数据集/场景**：采用了具身导航领域先进的 **CHORES** 基准测试，在**数百个程序化生成的环境**中评估，覆盖多种导航任务与场景布局。
- **对比方法**：文中虽未详细列出基线，但摘要指出展示了 SafeDec 对“最先进具身导航策略”的介入效果；可以推测与**不加约束的原始解码**（即原始策略输出）进行了对比，也可能包含其他基于后处理安全过滤的方法。
- **评估维度**：不仅验证了**过滤不安全动作**的能力，还突出了对**条件动作生成**（如引导策略生成满足特定 STL 约束的行为）的支持。

### 4. 资源与算力
- 提供的摘要和元数据中**未明确提及**训练或实验使用的 GPU 型号、数量及耗时。由于方法本身无需重训练，其计算开销主要来自解码时的在线 STL 验证，但文中未给出推理延迟等具体算力数据。

### 5. 实验数量与充分性
- 实验在 CHORES 基准的**数百个程序生成环境**上展开，任务规模较大，具有一定的统计意义。
- 摘要提及两项重要能力验证（安全过滤与条件生成），说明实验考虑了多个应用维度。
- 但由于仅提供有限文本，无法确认是否包含详尽的**消融实验**（如不同 STL 规范复杂度、不同动力学假设、不同基座策略的比较）、**敏感性分析**或**真实机器人实验**。从当前信息判断，实验覆盖场景丰富，但方法本身的鲁棒性边界尚待更多细节佐证，暂时认为其对安全提升的展示较为充分，而泛化与局限性讨论可能不够全面。

### 6. 论文的主要结论与发现
- SafeDec 能够在不修改预训练策略的前提下，通过在解码时施加 STL 约束，**有效滤除导航策略生成的危险动作**，显著提升行为安全性。
- 该框架支持**条件动作生成**，可根据不同的 STL 公式引导策略产生符合特定安全规范的行为。
- 该方法为安全关键的自主系统（明确包含**自动驾驶车辆运动规划**）提供了一种通用、便捷的安全增强途径。

### 7. 优点
- **即插即用**：无需重新训练或修改模型权重，降低部署门槛与计算成本。
- **形式化安全保证**：基于 STL 提供明确、可审计的安全规范，优于黑盒或启发式安全层。
- **策略无关性**：可适配各种预训练的 Transformer 导航策略，通用性强。
- **实时介入**：在推理过程中动态约束解码，而非事后修正，理论上更安全。

### 8. 不足与局限
- **对动力学模型的依赖**：安全验证建立在“假设的动力学模型”之上，若模型与实际物理系统存在偏差，可能导致安全约束名存实亡。
- **STL 规范设计负担**：需要领域专家预先将安全需求转写成正确的 STL 公式，不完善或错误的公式可能引入新的隐患。
- **实时性开销**：解码时每一步都要进行 STL 可达性检查，计算开销可能较高，但论文未披露推理延迟数据，能否满足高速率实时控制（如高速自动驾驶）存疑。
- **实验环境局限**：仅在仿真基准（CHORES）上验证，未涉及真实世界机器人平台，而仿真到现实的迁移（Sim2Real）是导航安全的关键挑战。
- **自回归框架绑定**：方法特化于自回归策略，对于非自回归或基于扩散模型的新兴策略类型兼容性未知。
- **提供的文本信息量有限**，无法评估其在任务成功率、效率损失、多种安全规范冲突等方面的具体权衡表现。

（完）
