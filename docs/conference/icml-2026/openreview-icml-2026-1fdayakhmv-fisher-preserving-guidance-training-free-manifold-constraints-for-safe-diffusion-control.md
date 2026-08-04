---
title: "Fisher-Preserving Guidance: Training-Free Manifold Constraints for Safe Diffusion Control"
title_zh: 保Fisher引导：面向安全扩散控制的免训练流形约束
authors: "Hao Ren, Zetong Bi, Yiming Zeng, Le Zheng, Zhi Li, Zhaoliang Wan, Lu Qi, Hui Cheng"
date: 2026-04-30
pdf: "https://openreview.net/pdf/4c2cfbcdb554c973e7ad59b0d05a451090534f90.pdf"
tags: ["query:av-pnc"]
score: 6.0
evidence: 免训练扩散引导用于安全轨迹生成与不确定性感知融合
tldr: 这项工作针对扩散模型在测试时引导易偏离训练流形的问题，提出保Fisher引导方法，利用外积跨度投影避免Fisher漂移，通过低秩雅可比分解实现每次仅需一次反向传播的实时推理。同时引入截断Fisher去噪敏感性作为不确定性信号，用于多采样动作融合。在视觉导航等任务上生成更可靠、高效的轨迹，对自动驾驶的安全规划具有借鉴价值。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 标准扩散模型在测试时引导易偏离训练流形，产生不可靠或低效的轨迹。
method: 提出保Fisher引导与截断Fisher去噪敏感性，通过低秩雅可比分解实现单步回传的在线约束优化。
result: 在视觉导航中生成满足目标且保持在流形上的可靠轨迹，支持多样本混合。
conclusion: 免训练流形约束提升扩散控制的安全性与实时性，可用于路径规划与自动驾驶。
---

## Abstract
Diffusion models are effective for waypoint prediction in visual navigation, but standard sampling and test time guidance can produce unreliable or inefficient trajectories when updates drift off the training manifold. We propose Fisher Preserving Guidance with Outer Product Span Projection, a training-free inference method that avoids large Fisher drift associated with off-distribution actions while optimizing a task objective. Our method computes the Fisher-preserving update via a low-rank Jacobian factorization, requiring only a single backward pass per step and enabling real-time use. We further introduce Truncated Fisher Denoising Sensitivity as an uncertainty signal and use it for robust multi-sample action blending. Experiments on toy and realistic navigation benchmarks, including Maze2D with TSDF-based guidance, PushT with official Diffusion Policy weights, and visual navigation in simulation and on real robots, demonstrate consistent improvements in performance over strong diffusion-policy baselines without additional training.

---

## 论文详细总结（自动生成）

# 论文总结：Fisher保持引导——用于安全扩散控制的免训练流形约束

## 1. 核心问题与整体含义
- **研究动机**：扩散模型在视觉导航的路点预测中展现出有效性，但其标准采样和测试时引导容易使生成的动作偏离训练数据的分布（流形），从而产生不可靠甚至不安全的轨迹。
- **整体含义**：本文旨在解决扩散策略在推理阶段因偏离训练流形而引入的安全隐患，提出一种无需重新训练的推理时干预方法，使扩散模型的采样过程始终保持在训练流形内，从而提升导航轨迹的可靠性与效率。该方法的思想可推广至自动驾驶等对安全要求极高的轨迹规划任务。

## 2. 方法论
- **核心思想**：通过约束采样更新方向，避免引入较大的 Fisher 信息漂移，从而防止生成掉出训练流形的“分布外”动作。
- **关键技术细节**：
    - **Fisher保持引导与外积跨度投影**：计算 Fisher 信息矩阵的低秩近似（通过雅可比矩阵的外积分解），将任务目标的梯度投影到训练流形的切空间上，在优化任务表现的同时最小化 Fisher 漂移。
    - **计算高效性**：仅需在每次去噪步骤中执行一次反向传播，即可获得所需的投影方向，无需迭代优化或预训练组件，满足实时性要求。
    - **截断 Fisher 去噪敏感性**：提出一种基于 Fisher 信息的不确定性度量，用于评估当前采样状态偏离流形的程度，并将其作为信号进行鲁棒的多采样动作融合（即将多个采样结果按敏感性加权平均）。
- **算法流程概览（文字描述）**：在扩散去噪的每一步，首先利用当前状态和预训练扩散模型计算雅可比矩阵，通过外积构造低秩投影算子；接着计算任务目标梯度，使用投影算子将其修正为 Fisher 保持更新；然后结合截断敏感性对多个候选采样进行加权融合，得到最终的安全动作。

## 3. 实验设计
- **数据集/场景**：
    - **Maze2D**：带 TSDF 代价引导的迷宫环境。
    - **PushT**：使用官方扩散策略权重（Diffusion Policy）的物体推送任务。
    - **仿真视觉导航**：基于视觉的导航仿真环境。
    - **真实机器人**：在真实机器人平台上进行的视觉导航实验。
- **对比基准**：以强扩散策略基线（strong diffusion-policy baselines）作为主要对比对象，包括标准采样和常规测试时引导方法。

## 4. 资源与算力
- 文中**未明确说明**具体的 GPU 型号、数量或推理时长数据。仅指出方法只需单次反向传播，计算开销小，可实时运行，但未提供硬件配置或耗时对比的量化信息。

## 5. 实验数量与充分性
- **实验覆盖范围**：涉及 4 种不同的任务设定（玩具 Maze2D、标准 PushT、仿真导航、真实机器人），覆盖从简单仿真到现实场景的递进。
- **对比充分性**：与扩散策略基线进行了对比，并在多个环境中展示了一致的提升；但其具体消融实验（如各组件贡献、不同超参数影响）的细节在摘要和元数据中**未予披露**。
- **客观性**：采用了官方发布的预训练权重（PushT），避免了自行训练带来的偏差，比较方式相对公平。但由于缺乏详尽的实验表格和量化消融结果，无法评估实验结论的统计稳健性。

## 6. 主要结论与发现
- 提出的 Fisher 保持引导能够在不经过额外训练的情况下，显著改善扩散策略生成轨迹的**可靠性**和**效率**。
- 截断 Fisher 去噪敏感性能够有效作为不确定性信号，实现更鲁棒的多采样动作融合。
- 该方法计算高效，仅需一次反向传播，可部署于实时系统。
- 其安全约束思想具有可推广性，能够为自动驾驶车辆的轨迹规划提供新的解决方案。

## 7. 优点
- **免训练**：完全在推理阶段工作，无需修改或微调原有的扩散模型，部署成本极低。
- **实时性**：通过低秩分解和单次反向传播实现了高效计算，适合在线导航。
- **理论基础清晰**：从 Fisher 信息和流形约束的角度给出了安全的解释，并提供了具体的不确定性度量。
- **实验覆盖面较广**：从仿真玩具环境延伸到真实机器人，验证了方法的实际适用性。

## 8. 不足与局限
- **实验细节缺失**：所提供材料未包含具体的定量结果表格、消融研究设计和统计指标，难以评估性能提升的显著性和泛化能力。
- **场景局限**：当前实验主要集中在导航和简单操作任务，对于高动态、多智能体或复杂物理交互环境的表现未知。
- **未讨论失效情况**：当任务目标引导与流形保持引导冲突剧烈时，方法的妥协策略可能牺牲任务性能，这点未展开分析。
- **资源开销不透明**：尽管声称高效，但未提供推理延迟或显存占用的具体数据，实际部署的硬件要求不明确。
- **依赖流形假设**：方法建立在预训练扩散模型能合理覆盖安全流形的基础上，若原有模型存在系统偏差，该方法无法修正。

（完）
