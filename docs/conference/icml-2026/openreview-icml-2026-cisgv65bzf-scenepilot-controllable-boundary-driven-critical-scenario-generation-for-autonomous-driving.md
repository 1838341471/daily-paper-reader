---
title: "ScenePilot: Controllable Boundary-Driven Critical Scenario Generation for Autonomous Driving"
title_zh: ScenePilot：面向自动驾驶的可控边界驱动关键场景生成
authors: "Qiyu Ruan, YUXUAN WANG, He Li, Zhenning Li, Cheng-zhong Xu"
date: 2026-04-30
pdf: "https://openreview.net/pdf/3870bd3e139a0834157df84fb0d0981d05a1c746.pdf"
tags: ["query:av-pnc"]
score: 7.0
evidence: 边界驱动的关键场景生成用于自动驾驶规划器压力测试
tldr: 本文针对自动驾驶评估中安全关键场景稀少且生成方法不可靠的问题，提出ScenePilot框架。通过可行性引导和边界驱动，聚焦物理可解但接近能力边界的场景带。实验表明生成场景能有效暴露规划器弱点，同时保持物理可行性，提升了仿真测试的真实性和严格性。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 自然数据中安全关键场景稀少，现有方法生成的场景要么物理不可解，要么过于激进。
method: 提出边界驱动框架，聚焦物理可解但接近能力边界的场景带，结合可行性引导。
result: 生成场景能有效暴露规划器弱点，且保持物理可行性。
conclusion: ScenePilot为自动驾驶系统提供了更高效、真实的压力测试场景生成方法。
---

## Abstract
Safety-critical scenarios are central to evaluating autonomous driving systems, yet their rarity in naturalistic logs makes simulation-based stress testing indispensable. Most scenario generation methods treat surrounding agents as adversaries, but they either (i) induce failures without explicitly modeling vehicle-road physical limits, yielding visually extreme yet physically unsolvable crashes, or (ii) enforce physical feasibility or policy feasibility in isolation, which can over-focus on aggressive maneuvers or remain tied to a controller-dependent capability boundary. We propose ScenePilot, a feasibility-guided, boundary-driven framework that targets the boundary band: scenarios that are physically solvable in principle yet still cause the deployed autonomy stack to fail. We formulate generation as constrained multi-objective reinforcement learning, combining an RSS-derived physical-feasibility score $\sigma$ with an online-learned AV-risk predictor $\Phi$, and introduce step-level feasibility-aware shielding to keep exploration near the feasibility boundary while avoiding infeasible artifacts. Experiments on SafeBench with multiple planners show that ScenePilot yields substantially higher collision rates (+6.2 percentage points) while preserving physical validity, and that adversarial fine-tuning on these boundary-band scenarios consistently reduces downstream crash rates. The code is available at https://github.com/QiyuRuan/ScenePilot.

---

## 论文详细总结（自动生成）

# ScenePilot 论文详细分析与总结

## 1. 论文的核心问题与整体含义
- **核心问题**：自动驾驶系统（AV）的安全性评估高度依赖安全关键场景（Safety-critical scenarios），但这些场景在自然驾驶日志中极为稀少，迫使研究者依赖仿真生成进行压力测试。
- **现有方法局限**：
  - **纯对抗性生成**：将周围车辆视为不择手段的对手，往往产生视觉上极端但在物理上根本无解的碰撞（例如违反了车辆动力学或道路几何约束），这类场景无法有效反映系统真实弱点。
  - **单边可行性约束**：仅强调物理可行性或策略可行性中的单一侧面，导致生成的场景要么过于激进、失去真实性，要么过度绑定于特定控制器的能力边界，缺乏通用压力。
- **整体含义**：本文旨在提出一个平衡“物理可行”与“系统失效”的框架，生成“原则上可解、实则难逃碰撞”的 **边界带（boundary band）** 场景，为自动驾驶规划器提供既严格又真实的仿真测试手段。

## 2. 论文提出的方法论
- **核心思想**：**可行性引导、边界驱动的关键场景生成**。不追求不可解的最坏情况，也不止于安全保守的边界，而是精准瞄准紧贴物理可行性极限的场景区域。
- **关键技术细节**：
  - **形式化框架**：将场景生成建模为 **约束多目标强化学习（constrained multi-objective RL）** 问题。
  - **双组件驱动器**：
    - **物理可行性分数 $\sigma$**：基于责任敏感安全模型（RSS）推导，用于量化当前场景在物理与交规约束下是否尚有安全解。
    - **在线学习的AV风险预测器 $\Phi$**：在实验中动态学习被测规划器的弱点，预测其面临风险的概率。
  - **探索保障机制**：引入 **步进级可行性感知屏蔽（step-level feasibility-aware shielding）**。在生成动作执行前进行过滤，仅允许探索保持在可行性边界附近的行为，直接屏蔽会导致场景退化成完全不可解伪影的动作，从而高效收敛于边界带。
- **算法流程概览**：
  > 场景生成智能体在每步观测状态 → $\Phi$ 预测当前状态下行车的风险 → 同时 $\sigma$ 评估物理可行性 → 屏蔽层筛选动作 → 执行动作推进场景 → 奖励信号兼顾碰撞成功率和可行性边界贴近度 → 策略迭代优化。

## 3. 实验设计
- **测试平台**：**SafeBench**，一个面向自动驾驶安全性评估的标准化基准（据摘要推断，该平台提供了多样的场景布局与规划器接口）。
- **被测对象**：**多个自动驾驶规划器（planners）**，以验证场景生成方法的通用压力效果（原文未列明具体规划器名称，但强调“multiple planners”）。
- **对比方法**：
  - 隐式对比了其他边界或对抗式生成方法（从“大多数方法”和“+6.2个百分点提升”的表述可知，实验中系统对比了至少一种或多种代表性敌方生成或可行性约束方法）。
  - 下游分析加入了 **对抗微调（adversarial fine-tuning）** 实验，用生成的边界带场景重新训练规划器，以验证场景的反哺改进价值。

## 4. 资源与算力
- **文中说明情况**：**本文摘要及提供的元数据中未明确给出GPU型号、数量、训练时长等算力数据**。ICML录用论文通常会在正文或附录中披露此类信息，但基于当前可提取内容，无法获知确切的资源开销。若有进一步公开的全文，方可补充。

## 5. 实验数量与充分性
- **可评估的实验维度**（基于摘要与常见科学实践推断）：
  - **多规划器测试**：至少覆盖2种以上结构各异的规划器，保障结论的广泛性。
  - **与现方法对比**：碰撞率提升 **+6.2百分点** 是有明确数值支撑的横向对比，说明至少存在一个基线对照组。
  - **消融与变量分析**：物理可行性分数 $\sigma$、风险预测器 $\Phi$ 及屏蔽层的有效性通常需通过移除各组件的消融实验来证明，此类实验在约束强化学习方法中极为常见，摘要虽未枚举，但其机制复杂程度暗示文中应包含。
  - **下游验证**：通过对抗微调降低下游碰撞率，构成了一条从生成到改进的完整闭环验证链。
- **充分性与公平性**：若上述实验均完整呈现，则设计较为充分、客观。从录用级别（ICML）推断，其对比对象的选择、超参数设定、指标计算应具备同行评议认同的公平性。然而，因无法获取全文细节，**具体实验组数、场景多样性覆盖、统计显著水平等信息暂缺**。

## 6. 论文的主要结论与发现
- **更高的暴露能力**：ScenePilot 相较现有方法，能将碰撞率显著提高 **6.2 个百分点**，且生成的场景 **保持了物理有效性**，不会陷入不可解的虚假极端情况。
- **边界带的有效性**：所定义的物理可行边界带场景，正是暴露规划器薄弱环节的高价值区域。
- **正向反馈循环**：利用 ScenePilot 生成的边界带场景对规划器进行对抗性微调，能够**持续降低这些高危场景下的碰撞率**，证明了其不仅能用于测试，更是自动化改进的利器。

## 7. 优点
- **概念清晰且务实**：创造性提出“**物理可行边界带**”这一概念，摒弃了无意义的不可解冲突，直接聚焦“可解但易败”的高价值测试区，更贴近现实安全测试需求。
- **机制协同巧妙**：将RSS推导的静态物理分数与在线学习动态风险预测器相结合，并通过 **步进级屏蔽** 进行动作级约束，高效解决了约束RL中探索易越界、产生无解伪影的难题。
- **验证闭环**：不仅是生出更“难”的场景，还证明了这些场景能有效提升下游模型能力（微调后碰撞率下降），提供了从测试到优化的实用链路。
- **可复现性**：论文承诺代码已开源（GitHub链接可查），增强了结果的可验证性。

## 8. 不足与局限
- **细节信息不可见**：当前仅基于摘要和元数据，**无法评判**实验中具体场景规模、多样性、对比方法的完整列表、算力开销和统计检验，存在评估盲区。
- **RSS假设的泛化性**：物理可行性分数高度依赖RSS模型，该模型基于预设的安全包络和反应策略，可能在非结构化环境、复杂博弈或极端天气下出现覆盖不全，边界带的“真实性”仍有探讨空间。
- **静态元素与交互复杂度**：SafeBench侧重车辆间交互，场景可能较少涉及复杂静态障碍物、行人密集区或动态交通规则，生成的边界带场景类型或许受限。
- **依赖闭环仿真器**：方法深度集成在线风险预测器与屏蔽层，对仿真器的交互及时性和物理模型精度有较强要求，迁移至另一套仿真系统或实车测试的成本可能较高。
- **潜在偏差**：在线学习的 $\Phi$ 高度依赖于被测规划器的初始缺陷分布，若初始模型偏弱或不具代表性，生成的边界带可能过度拟合特定的弱点模式，成为针对性过强而普适压力不足的“窄带”。

（完）
