---
title: "Rethinking Instruction Drift as a Sampling Error: SNR-Aware Power Distributions for Long-Horizon Robotic Planning"
title_zh: 将指令漂移重新理解为采样误差：面向长时程机器人规划的SNR感知幂分布
authors: "Kewei Chen, Yayu Long, Mingsheng Shang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/a53475ef3452dd06c41a4cc9ab1384c3fca9eb16.pdf"
tags: ["query:av-pnc"]
score: 5.0
evidence: 面向长时程机器人规划的推理期采样框架，提升全局轨迹概率，可迁移至轨迹规划
tldr: 视觉-语言-动作模型在长时程任务中常出现指令漂移。本文将这种漂移归因于局部贪心采样坠入负向枢轴窗口的系统性采样误差。为此提出上下文感知幂采样CAPS，利用幂分布锐化全局轨迹概率，在条件生成轨迹上实现前瞻搜索。该方法是免训练的推理期计算框架，可有效提升长时程机器人规划的稳定性。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 长时程任务中局部贪心采样导致指令漂移和不可逆错误。
method: 提出CAPS，基于信噪比感知的幂分布锐化全局轨迹概率并执行前瞻搜索。
result: 在长时程规划中缓解了指令漂移，提升了全局成功率。
conclusion: 将指令漂移建模为采样误差，为长时程规划提供了免训练改进方案。
---

## Abstract
Despite rapid progress in Vision-Language-Action (VLA) models for robotic control, instruction drift remains a persistent failure mode in long-horizon tasks. This paper reconceptualizes this phenomenon, positing that instruction drift is fundamentally a systematic sampling error: local greedy sampling is prone to collapsing into “Negative Pivotal Windows”—irreversible local optima with high local probability that sever global success pathways. To address this, we propose Context-Aware Power Sampling (CAPS), a training-free inference-time computation framework. CAPS leverages power distributions to sharpen global trajectory probabilities, enabling lookahead search over the model's conditional generative trajectory distribution. Furthermore, we introduce a metacognitive control mechanism based on Signal-to-Noise Ratio (SNR). This mechanism triggers adaptive MCMC search solely when drift risk is detected, enabling a dynamic transition from “intuitive fast thinking” to “rational slow search.” Experiments on RoboTwin, Simpler-WindowX, and Libero-long benchmarks show that CAPS achieves substantial improvements over strong baselines, including OpenVLA and TACO, without parameter updates. These results support the effectiveness of adaptive inference-time computation for improving long-horizon robustness in embodied control.

---

## 论文详细总结（自动生成）

# 中文总结

## 1. 核心问题与整体含义

- **背景**：视觉-语言-动作（VLA）模型在机器人控制领域发展迅速，但在**长时程任务**中仍存在一个顽固的失败模式——**指令漂移（instruction drift）**，即机器人随着任务推进逐渐偏离原始指令。
- **问题重定义**：本文提出将指令漂移**不是**视为简单的上下文丢失或模型遗忘，而是从根本上重新理解为一种**系统性采样误差（systematic sampling error）**。
- **具体机制**：局部贪心采样容易坠入“**负向枢轴窗口（Negative Pivotal Windows）**”——即局部概率很高但不可逆的局部最优状态，这些状态会切断通向全局成功的轨迹路径。
- **整体含义**：该视角将长时程规划的失败归因于采样策略的局限，而非纯粹模型能力不足，从而为**推理期计算**（inference-time computation）提供新的改进空间。

## 2. 方法论

- **核心思想**：提出 **Context-Aware Power Sampling (CAPS)**，即“上下文感知幂采样”，这是一个**免训练（training-free）** 的推理期计算框架。
- **关键技术细节**：
  - **幂分布锐化**：CAPS 利用幂分布（power distributions）来锐化全局轨迹概率，而非直接使用模型原始输出的分布进行采样。这种锐化有助于将采样权重向高全局价值轨迹偏移，避免落入局部最优窗口。
  - **前瞻搜索**：CAPS 在模型的条件生成轨迹分布之上执行**前瞻搜索（lookahead search）**，相当于在生成过程中模拟未来多步，从而评估当前动作的全局影响。
  - **SNR 元认知控制**：引入基于**信噪比（Signal-to-Noise Ratio, SNR）** 的元认知机制，用于判断当前生成过程是否存在漂移风险。只有当风险被检测到时，才触发**自适应 MCMC 搜索**（马尔可夫链蒙特卡洛），使系统从“直觉快速思考”动态切换到“理性慢速搜索”。
- **算法流程（文字描述）**：
  1. 模型接收视觉与语言指令，开始自回归生成动作轨迹；
  2. 在每个决策点估计当前上下文的 SNR（可理解为全局轨迹信号与噪声的相对强度）；
  3. 若 SNR 较高，则保持快速贪心采样，以节省推理开销；
  4. 若 SNR 较低（漂移风险较高），则启动 MCMC 搜索，借助 CAPS 的幂分布重新加权候选轨迹，进行前瞻探索；
  5. 选择跳出负向枢轴窗口的轨迹，继续生成，直至任务结束。

> 注：提供的摘要中未给出具体公式或伪代码，以上流程是根据方法描述的合理转述。

## 3. 实验设计

- **数据集 / 场景**：
  - **RoboTwin**
  - **Simpler-WindowX**
  - **Libero-long**
- **Benchmark 性质**：上述三个基准均面向**长时程机器人规划**任务，涵盖仿真或标准化机器人操作场景，用于评估指令漂移与全局成功率。
- **对比方法**：
  - **OpenVLA**：作为强基线 VLA 模型。
  - **TACO**：作为另一个强基线方法。
- **评价标准**：主要关注长时程任务的全局成功率（global success rate）以及指令漂移的缓解程度。

## 4. 资源与算力

- **未明确说明**：提供的论文摘要与元数据中**没有列出** GPU 型号、数量、训练时长或推理计算开销等具体资源信息。
- **需要注意**：由于 CAPS 是免训练方法，核心开销在推理期的 MCMC 搜索与前瞻计算上，但论文未提供相应的计算成本度量。

## 5. 实验数量与充分性

- **从现有文本看**：只提到在三个基准（RoboTwin、Simpler-WindowX、Libero-long）上进行了评估，并与两个基线（OpenVLA、TACO）进行了对比。
- **缺少细节**：
  - 没有给出具体成功率数值或性能提升幅度；
  - 未提及消融实验（例如幂分布参数影响、SNR 阈值灵敏度、MCMC 搜索步数等）；
  - 未说明多次重复实验的方差与统计显著性；
  - 未讨论不同 VLA 模型上的泛化性。
- **总体评估**：由于可见信息仅来自摘要，无法充分判断实验的客观性与公平性。需要完整论文中的实验设置、超参数、随机种子和置信区间等信息才能综合评估。

## 6. 主要结论与发现

- **CAPS 有效缓解指令漂移**：在三个长时程基准上，CAPS 相比 OpenVLA 和 TACO 取得了**显著提升**，且无需参数更新。
- **指令漂移是采样误差**：将漂移建模为“局部贪心采样坠入负向枢轴窗口”的系统性误差在实验中获得了支持。
- **自适应推理期计算有效**：SNR 门控的元认知控制能够动态切换思考模式，在保证效率的同时提升长时程鲁棒性。
- **免训练迁移性好**：CAPS 可以直接应用于现有 VLA 模型，无需微调，便于实际部署。

## 7. 优点

- **理论创新性**：将指令漂移重新定义为采样误差，提供了新的解释框架，超越了传统的长上下文或记忆增强视角。
- **方法实用性**：免训练、推理期即可用，对已有模型具备即插即用潜力。
- **计算自适应性**：SNR 控制的慢速搜索只在风险出现时触发，避免了全时段的昂贵搜索，兼顾效率与鲁棒性。
- **基准多样性**：使用了三个不同的长时程基准，覆盖了不同的任务分布，增加了一定说服力。
- **对比强基线**：与 OpenVLA 和 TACO 等知名方法比较，能体现方法的竞争力。

## 8. 不足与局限

- **信息不完整**：当前提供的材料仅为摘要与元数据，缺乏实验数值、算法伪代码和实现细节，难以进行深入验证。
- **实验覆盖有限**：
  - 未提及真实物理机器人部署实验；
  - 未说明是否包含多视角或高噪声环境下的压力测试；
  - 缺少消融实验，无法量化幂分布锐化与 MCMC 搜索各自的贡献。
- **计算开销不明**：MCMC 搜索可能在低 SNR 阶段引入显著推理延迟，摘要未给出任何时间成本分析，这可能影响实时机器人控制。
- **潜在偏差风险**：若基准任务集中于特定类型，则结论可能不能泛化到更复杂的开放世界任务；另外，未报告多次运行的统计波动，存在结果偶然性风险。
- **模型依赖**：CAPS 建立在条件生成式 VLA 模型之上，对非生成式或离散动作策略的适用性尚不清楚。

（完）
