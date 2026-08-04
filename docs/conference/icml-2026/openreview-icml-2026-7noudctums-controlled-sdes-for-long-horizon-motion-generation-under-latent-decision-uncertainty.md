---
title: Controlled SDEs for Long-Horizon Motion Generation under Latent Decision Uncertainty
title_zh: 受控随机微分方程：潜决策不确定下的长时程运动生成
authors: "Han Zhang, Nenggan Zheng"
date: 2026-04-30
pdf: "https://openreview.net/pdf/7e0b1673a3abdaddb9eac9fb647ddeae198a3d73.pdf"
tags: ["query:traj-pred"]
score: 8.0
evidence: 利用受控随机微分方程进行潜决策不确定下的长时程运动生成，属于生成式运动轨迹建模。
tldr: 长时程运动预测常因内在决策状态不可观测且随机演化而困难，生物体尤其如此。该文提出CogSDE，用受控随机微分方程刻画指令驱动的潜决策动态，漂移项通过双通道控制调制外部指令，扩散项采用状态依赖算子表达随机性。模型在长时程运动生成任务上优于既有方法，能够在外界命令影响下生成合理连续的轨迹。该框架为理解决策与运动生成的关系提供了数学化视角。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 生物体长时程运动生成面临不可观测的潜决策状态随机演化的挑战，常规方法难以建模。
method: 提出受控随机微分方程CogSDE，用漂移项双通道控制调制外部指令，用状态依赖扩散项刻画随机性。
result: 实验验证其在长时程指令驱动运动生成上的有效性，生成的轨迹更合理且符合低层运动学约束。
conclusion: 为长期运动生成与潜决策不确定性建模提供统一的受控SDE范式。
---

## Abstract
Long-horizon motion prediction under external commands is challenged by latent decision uncertainty, where the internal states governing future behavior are unobservable and evolve stochastically over time. This issue is particularly pronounced in biological agents, whose motion trajectories reflect decision-making processes rooted in underlying cognitive states. To address these challenges, we propose CogSDE, a formulation of a controlled stochastic differential equation (SDE) for modeling instruction-driven latent decision dynamics. The drift term in the SDE incorporates a dual-channel control modulation mechanism, enabling external commands to modulate the evolution of latent states. The diffusion term employs a state-dependent operator to model intrinsic uncertainty in latent decision dynamics. Furthermore, we establish dissipativity-based mean-square boundedness for the latent decision dynamics. Experiments demonstrate that CogSDE consistently improves predictive accuracy in long-horizon motion generation. Importantly, predicted trajectories remain well aligned with control commands over extended horizons, a property widely recognized as challenging in long-horizon motion prediction.

---

## 论文详细总结（自动生成）

# 中文总结：受控随机微分方程用于潜决策不确定下的长时程运动生成

## 1. 核心问题与研究动机
- 研究聚焦**长时程运动预测/生成**问题，尤其是当外部指令存在、智能体需要长时间生成符合指令的运动轨迹时。
- 核心难点是**潜决策不确定性（latent decision uncertainty）**：决定未来行为的内部状态不可观测，且随时间的演化具有随机性。
- 在生物体场景中尤为突出：运动轨迹往往反映认知状态驱动的决策过程，但认知状态本身无法直接测量。
- 既有方法难以同时解决“不可观测潜状态”和“随机演化”两大挑战，因此在长时程预测中容易出现轨迹漂移、偏离控制指令的问题。

## 2. 提出的方法论：CogSDE
- 核心思想：将**隐式决策动态**建模为**受控随机微分方程（controlled SDE）**，用 SDE 描述指令驱动下的潜状态演化。
- 模型名称：**CogSDE**。
- 关键技术细节：
  - **漂移项（drift term）**：采用**双通道控制调制机制**，将外部命令输入同时通过两条路径调制潜状态的确定性演化，从而实现对指令的适应。
  - **扩散项（diffusion term）**：使用**状态依赖算子**，刻画潜决策动态中的内在随机性，而非简单的高斯噪声。
  - **理论性质**：建立了基于**耗散性（dissipativity）的均方有界性**，为潜决策动态的长时间稳定性提供数学保证。
- 整体流程可理解为：外部命令 → 双通道控制调制潜状态漂移；状态依赖扩散引入随机性；在受控 SDE 框架下进行长时程运动轨迹生成。

## 3. 实验设计
- 根据现有文本（主要为摘要和元数据），论文实验聚焦**长时程指令驱动运动生成**任务。
- 领域标签属于**轨迹预测（query:traj-pred）**，来源为 ICML-2026 接收论文。
- 具体使用的数据集、场景与基准（benchmark）在提供内容中**未明确列出**。
- 对比方法也未在摘要中逐一说明，仅称“优于既有方法（consistently improves predictive accuracy）”。
- 摘要强调一项重要评价维度：**预测轨迹在长时间范围内与外部控制命令保持对齐**，这是长时程运动预测公认的难点。

## 4. 资源与算力
- 提供的文本中**未提及任何算力信息**，包括 GPU 型号、数量、训练时长等。
- 若需了解训练资源，必须查阅论文正文或附录；当前材料无法给出具体数值。

## 5. 实验数量与充分性
- 仅从摘要和元数据来看，无法判断具体实验数量、数据集个数或消融实验设置。
- 摘要显示模型在长时程生成上具有一致提升，并专门验证了指令对齐性，说明实验设计至少覆盖了**核心主张的两个方面**。
- 但缺少：
  - 可视化示例数量；
  - 消融实验（双通道控制、状态依赖扩散等组件的重要性验证）；
  - 不同运动类型、不同指令密度、不同噪声条件下的鲁棒性分析。
- 因此，基于现有材料**不能充分评估实验的公平性与完备性**，需要阅读论文全文。

## 6. 主要结论
- CogSDE 能有效建模外部指令驱动的潜决策动态，在长时程运动生成上显著提升预测精度。
- 生成的轨迹能够长时间保持与外部控制命令的一致性，克服了长时程运动预测中的常见难题。
- 该工作为“认知决策 → 运动生成”的关系提供了一个统一的受控 SDE 数学化视角。

## 7. 优点
- **建模角度新颖**：将运动生成中的不可观测决策状态显式建模为随机微分方程，比纯判别式或自回归方法更具可解释性。
- **控制器设计合理**：双通道控制调制使外部指令能够灵活地影响潜状态演化，避免指令信息丢失。
- **随机性建模精细**：状态依赖扩散算子比固定噪声更贴合决策不确定性随状态变化的真实特性。
- **理论支撑充分**：用耗散性推导均方有界性，为长时程预测的稳定性给出数学保障。
- **问题定位清晰**：针对“长时程指令对齐”这一公认难点进行专门验证，具有实际意义。

## 8. 不足与局限
- **细节缺失**：当前可用材料只有摘要，无法评估方法的完整实现、训练目标、推理方式等关键信息。
- **实验验证有限**：未见数据集列表、多种场景对比和消融实验，暂时难以判断方法的通用性和稳健性。
- **适用范围可能受限**：模型隐式假设运动生成由可建模的潜决策过程控制，对非认知驱动或纯物理驱动型运动可能不适用。
- **计算复杂度未知**：受控 SDE 的数值求解与长时程采样可能带来较高计算开销，论文中未给出相关效率分析。
- **需要更多实证支撑**：是否在真实生物运动数据、多智能体交互或复杂指令场景中有效，仍有待进一步验证。

（完）
