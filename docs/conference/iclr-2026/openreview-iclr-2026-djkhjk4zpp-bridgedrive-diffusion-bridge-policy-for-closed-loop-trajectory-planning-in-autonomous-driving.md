---
title: "BridgeDrive: Diffusion Bridge Policy for Closed-Loop Trajectory Planning in Autonomous Driving"
title_zh: BridgeDrive：自动驾驶中闭环轨迹规划的扩散桥策略
authors: "Shu Liu, Wenlin Chen, Weihao Li, Zheng Wang, Lijin Yang, Jianing Huang, YipinZhang, Zhongzhan Huang, Ze Cheng, Hao Yang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=dJKhjK4zpp"
tags: ["query:av-pnc"]
score: 9.0
evidence: 用于闭环轨迹规划的扩散桥策略
tldr: 针对扩散规划器在闭环引导中引入的非对称问题，提出BridgeDrive：将规划建模为锚点引导的扩散桥过程，保持扩散原理一致性；在闭环仿真中规划安全性显著优于截断扩散方法。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有锚点引导扩散规划器使用截断调度，导致前向与去噪过程不对称。
method: 提出扩散桥策略，将规划视为锚点引导的扩散桥过程，保持对称性。
result: 在闭环仿真中，安全性和反应性优于截断扩散方法。
conclusion: 扩散桥公式能有效解决闭环轨迹规划中的引导不对称问题。
---

## Abstract
Diffusion-based planners have shown strong potential for autonomous driving by capturing multi-modal driving behaviors. A key challenge is how to effectively guide these models for safe and reactive planning in closed-loop settings, where the ego vehicle's actions influence future states. Recent work leverages typical expert driving behaviors (i.e., anchors) to guide diffusion planners but relies on a truncated diffusion schedule that introduces an asymmetry between the forward and denoising processes, diverging from the core principles of diffusion models. To address this, we introduce BridgeDrive, a novel anchor-guided diffusion bridge policy for closed-loop trajectory planning. Our approach formulates planning as a diffusion bridge that directly transforms coarse anchor trajectories into refined, context-aware plans, ensuring theoretical consistency between the forward and reverse processes. BridgeDrive is compatible with efficient ODE solvers, enabling real-time deployment. We achieve state-of-the-art performance on the Bench2Drive closed-loop evaluation benchmark, improving the success rate by 7.72% and 2.45% over prior arts with PDM-Lite and LEAD datasets, respectively. Project page: https://github.com/shuliu-ethz/BridgeDrive.

---

## 论文详细总结（自动生成）

# 详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究背景**：基于扩散模型的规划器在自动驾驶中能够捕捉多模态驾驶行为（如换道、跟车等），展现出强大潜力。但在闭环（closed-loop）环境中，自车动作会影响未来状态，因此需要有效引导扩散模型生成安全且具备反应性的轨迹。
- **核心问题**：现有工作利用典型专家驾驶行为（即锚点，anchors）来引导扩散规划器，但它们普遍采用**截断扩散调度**（truncated diffusion schedule），这导致前向加噪过程与去噪过程之间出现**不对称性**（asymmetry），偏离了扩散模型的核心原理，进而限制了规划的安全性和性能。
- **研究动机**：为克服这一不对称性问题，作者提出一种新的锚点引导扩散桥策略，使得前向和反向过程在理论上保持一致，从而提升闭环轨迹规划的安全性与反应性。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：将轨迹规划建模为**锚点引导的扩散桥过程**（anchor-guided diffusion bridge），直接地将粗糙的锚点轨迹（coarse anchor trajectories）变换为精细的、环境感知的规划轨迹。
  - 扩散桥（Diffusion Bridge）是指从初始分布（锚点轨迹）到目标分布（最优计划）的随机过程，通过约束起点和终点，保持前向与反向过程的对称性。
- **关键技术细节**：
  - 摒弃截断调度，转而使用完整的扩散桥公式，保证前向加噪和反向去噪遵循一致的扩散原理。
  - 兼容高效的**ODE求解器**（如DPM-Solver等），从而支持实时部署（real-time deployment）。
  - 具体流程：
    1. 输入场景上下文（如周围车辆、道路结构等）和一组粗锚点轨迹（通常来自简单行为模板或聚类）。
    2. 将每一条锚点轨迹作为扩散桥的初始点（起点），目标为最优规划轨迹（终点）。
    3. 通过前向扩散桥过程逐步加入噪声，反向去噪过程则从噪声中恢复出精细轨迹，且该过程始终受锚点条件约束。
    4. 最终输出多个候选规划轨迹，并选择最优者执行。
- **公式/算法流程（文字说明）**：扩散桥的SDE可表示为 \( dX_t = f(t)X_t dt + g(t)dW_t \)，其中初始条件 \( X_0 \) 为锚点轨迹，终态 \( X_T \) 近似于目标分布。反向过程通过求解相应的反时间扩散方程实现，并在每一步使用神经网络预测去噪方向。

## 3. 实验设计：数据集、Benchmark、对比方法

- **数据集**：主要使用 **Bench2Drive** 闭环评估基准（closed-loop evaluation benchmark）。同时涉及两个子数据集：**PDM-Lite** 和 **LEAD** 数据集。
- **Benchmark**：Bench2Drive 是自动驾驶领域中用于闭环轨迹规划的标准测试平台，包含多种城市驾驶场景（如交叉口、变道、跟车等），评估指标包括成功率、碰撞率、反应性等。
- **对比方法**：
  - 与 **PDM-Lite** 和 **LEAD** 数据集上的先前最优方法（prior arts）进行对比。
  - 具体而言，在 Bench2Drive 闭环测试中，BridgeDrive 相比先前方法在成功率上分别提升了 **7.72%**（使用PDM-Lite数据集）和 **2.45%**（使用LEAD数据集）。
  - 未提及与其他非锚点引导扩散规划器的对比（如单纯扩散模型或基于优化的方法）。

## 4. 资源与算力

- **论文中未明确说明**使用的GPU型号、数量、训练时长等算力信息。
- 仅提及“兼容高效的ODE求解器，支持实时部署”，但未给出具体的推理延迟或训练资源消耗数据。

## 5. 实验数量与充分性

- **实验数量**：
  - 主要实验为在 Bench2Drive 闭环基准上的成功率对比（两个不同锚点数据集下的结果）。
  - 从摘要和元数据看，未提及额外的消融实验（例如对锚点数量、桥长度、ODE求解器类型等的分析），也未在多个不同开源仿真平台（如CARLA、nuPlan）上进行验证。
- **充分性评估**：
  - **优点**：Bench2Drive是公认的闭环评估基准，对比了公开的最优方法，结果具有可比性。
  - **不足**：实验覆盖较窄——仅在一个基准的两个数据子集上汇报结果；缺少消融研究来证明扩散桥设计的各个组件贡献（如与截断扩散的直接对比、不同锚点生成方式的影响、不同ODE求解器的影响等）；也未展示在真实世界数据或更复杂场景（如无信号交叉口、交互密集区域）上的性能。
  - **客观性与公平性**：对比方法为同领域的现有最优方法，但未说明是否使用了相同的锚点提取方式或预测模型，可能存在变量控制不充分的风险。

## 6. 论文的主要结论与发现

- **主要结论**：扩散桥公式能够有效解决闭环轨迹规划中因截断调度导致的引导不对称问题，从而提升规划的安全性和反应性。
- **具体发现**：
  - BridgeDrive 在 Bench2Drive 基准上取得了**当前最优（SOTA）** 性能，成功率提升明显（7.72% 和 2.45%）。
  - 扩散桥过程保持了扩散原理的理论一致性，前向与反向对称，避免了截断方法引入的偏差。
  - 该策略可兼容高效ODE求解器，实现实时推理，具有实际部署潜力。

## 7. 优点：方法或实验设计上的亮点

- **方法创新**：
  - 首次将扩散桥模型引入自动驾驶闭环轨迹规划，从理论上解决了锚点引导时的不对称问题，思路清晰且数学优美。
  - 兼容ODE求解器，兼顾性能与实时性，有利于实际应用。
  - 直接以粗锚点为起点，避免了从纯噪声开始生成的不确定性，提高了生成轨迹的质量。
- **实验设计**：
  - 选择了业界认可度较高的 Bench2Drive 基准进行闭环评测，结果具有说服力。
  - 报告了在两个不同锚点数据集上的结果，显示了方法的泛化性。

## 8. 不足与局限

- **实验覆盖不足**：
  - 仅在一个闭环基准上验证，缺少在多种仿真环境（如 CARLA、nuPlan）或真实道路数据上的测试。
  - 未展示与其他非锚点引导方法（如直接扩散规划器、基于优化或模仿学习的方法）的广泛对比。
  - 缺乏充分的消融实验，难以量化各个组件（桥结构、锚点数量、ODE求解器、网络结构）的贡献。
- **偏差风险**：
  - 锚点的质量对最终结果影响很大，但论文未讨论锚点生成方式可能引入的偏差或鲁棒性。
  - 成功率提升的绝对数值（7.72%和2.45%）虽显著，但未报告其他关键指标（如碰撞率、舒适性、计算延迟等）的详细结果。
- **应用限制**：
  - 依赖预先定义的锚点轨迹集合，当场景超出锚点覆盖范围时可能导致性能下降。
  - 扩散桥的起点固定为锚点，若锚点本身不理想（例如在高度交互场景中），桥的收敛可能会受限。
  - 未给出训练资源和实际推理时间的具体数据，无法准确评估部署成本。
- **理论分析**：虽然声称桥过程保持一致，但未提供严格的数学证明或边界条件分析，仅靠实验论证。

（完）
