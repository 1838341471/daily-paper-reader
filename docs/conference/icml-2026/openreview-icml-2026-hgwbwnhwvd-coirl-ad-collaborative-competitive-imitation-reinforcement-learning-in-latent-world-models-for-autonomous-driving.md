---
title: "CoIRL-AD: Collaborative-Competitive Imitation-Reinforcement Learning in Latent World Models for Autonomous Driving"
title_zh: CoIRL-AD：自动驾驶中潜世界模型下的协同-竞争模仿强化学习
authors: "Xiaoji Zheng, Ziyuan Yang, Yanhao Chen, Yuhang Peng, Yuanrong Tang, Gengyuan Liu, Bokui Chen, Jiangtao Gong"
date: 2026-04-30
pdf: "https://openreview.net/pdf/31d868560d11c7698e65a19c30821e6d9d9866c5.pdf"
tags: ["query:av-pnc"]
score: 10.0
evidence: 面向自动驾驶的协同-竞争模仿强化学习
tldr: 端到端自动驾驶模型在模仿学习下泛化能力差，尤其在专家示范稀疏的长尾场景中。本文提出CoIRL-AD，一种协同-竞争双策略框架，在离线训练范式下解耦模仿学习与强化学习奖励优化，利用潜世界模型进行想象推演，增强行为多样性。实验表明该方法有效缓解了目标冲突，提升了在罕见场景下的决策性能，为离线强化学习在自动驾驶中的应用提供了新方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 模仿学习训练的自动驾驶模型在长尾场景泛化差，离线强化学习面临行为多样性不足的挑战。
method: 提出CoIRL-AD框架，解耦模仿与奖励优化为双策略，利用想象推演和竞争训练。
result: 实验证明该方法在离线设置下有效提升长尾场景的决策性能。
conclusion: 为自动驾驶中的离线强化学习提供了新的训练范式。
---

## Abstract
End-to-end autonomous driving models trained with imitation learning (IL) often generalize poorly, particularly in long-tail scenarios where expert demonstrations are sparse. Reinforcement learning (RL) can provide complementary task-level supervision, but applying RL to real-world autonomous driving is challenging in offline settings without interactive simulators, where datasets are dominated by expert actions and provide limited behavioral diversity. We propose CoIRL-AD, a competitive dual-policy framework that integrates IL and RL under a unified offline training regime. CoIRL-AD decouples imitation and reward optimization into separate actors to alleviate objective conflicts, uses imagined future rollouts for long-horizon reward estimation, and introduces a competition mechanism that selectively transfers beneficial behaviors while keeping RL anchored to expert-like driving. Experiments on the nuScenes benchmark show that CoIRL-AD consistently improves robustness over strong IL-based baselines, with especially large gains in cross-city generalization and long-tail scenarios. Code is available at: https://github.com/SEU-zxj/CoIRL-AD.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：端到端自动驾驶模型若仅依靠模仿学习（Imitation Learning, IL）训练，容易在专家示范稀疏的**长尾场景**（long-tail scenarios）中泛化性能急剧下降；而强化学习（Reinforcement Learning, RL）虽然能提供任务级别的监督信号，但其在**离线设定**下（无交互式仿真器，数据集主要由专家动作主导）面临行为多样性不足、离线分布漂移等挑战。
- **研究动机**：将 IL 和 RL 有机结合以互补优势，但二者存在**目标冲突**——IL 追求像专家一样的绝对模仿，RL 追求最大化累计奖励，直接在同一个策略中混合容易导致训练不稳定或策略退化。因此，需要一种新的训练范式，在离线数据下实现 IL 与 RL 高效、稳定的协同。
- **整体含义**：论文提出 CoIRL-AD 框架，通过**协同‑竞争双策略解耦**、**潜世界模型想象推演**和**竞争机制**，为离线自动驾驶提供一种将模仿学习与强化学习深度融合的新方案，旨在提升模型在罕见、复杂场景下的鲁棒性与泛化能力。

## 2. 论文提出的方法论：核心思想、关键技术细节与流程

- **核心思想**：**解耦模仿优化与奖励优化为两个独立的策略网络**，让二者分工协作而非互相干扰；同时引入潜世界模型在隐空间中生成想象的未来轨迹，以进行高效的长时域奖励估计；额外设计竞争机制权衡并选择性迁移有益行为，防止 RL 策略偏离专家驾驶风格。
  
- **关键技术细节**：
  - **竞争双策略框架（Competitive Dual‑Policy）**：一个**IL 策略**专注于模仿专家示范，一个**RL 策略**专注于最大化累积奖励。二者共享视觉主干和部分特征，但拥有独立的输出头，避免梯度冲突。
  - **潜世界模型（Latent World Model）**：构建在隐空间中的动态模型，可以基于当前隐状态和动作预测下一时刻的隐状态，进而实现“想象推演”（imagined future rollouts）。在不依赖在线仿真器的情况下，为 RL 策略提供多步奖励估计，缓解离线 RL 中的值函数外推误差。
  - **协同‑竞争机制**：训练时，IL 策略作为“锚点”，RL 策略在探索过程中受到与 IL 策略的距离约束；同时引入 **行为迁移门控**，当 RL 动作的潜在回报显著优于 IL 且未偏离安全范围时，才允许 RL 的行为监督被纳入训练，实现竞争中的协同。
  - **统一离线训练流程**：整个框架以离线数据集为基础，交替优化各模块：1）训练潜世界模型以学习环境的动态转移；2）在潜空间中用 IL 策略生成演示轨迹，用 RL 策略进行值函数学习与策略提升；3）通过竞争机制融合两条路径的梯度，更新共享编码器和各自策略头。

- **公式或算法流程（文字说明）**：
  - 从传感器输入编码为隐状态 \(s_t\)。
  - IL 策略输出动作分布 \(\pi_{\text{IL}}(a_t|s_t)\)，并通过行为克隆损失 \(\mathcal{L}_{\text{IL}}\) 进行监督。
  - RL 策略 \(\pi_{\text{RL}}\) 基于潜世界模型做 \(H\) 步想象推演，估计 \(Q(s_t, a_t)\)，利用 TD 误差优化 Critic，并通过策略梯度优化 Actor，同时加入与 \(\pi_{\text{IL}}\) 的 KL 散度正则项。
  - 竞争模块根据 \(Q\) 值优势比动态调整来自 RL 的分段损失权重，仅当 \(\Delta Q\) 超过阈值时才强化 RL 行为，否则退化为纯 IL 监督。
  - 整体损失为 \(\mathcal{L} = \mathcal{L}_{\text{IL}} + \lambda_1 \mathcal{L}_{\text{RL}} + \lambda_2 \mathcal{L}_{\text{world model}}\)，并动态调节 \(\lambda_1\)。

## 3. 实验设计：数据集、场景、Benchmark 与对比方法

- **数据集与 Benchmark**：使用**nuScenes** 数据集，大规模真实世界自动驾驶多模态数据集，包含多种城市、天气和交通场景。实验聚焦于规划层面的端到端驾驶任务，评估长尾场景和跨城市泛化能力。
- **对比方法**：包括多种基于 IL 的强基线，例如：
  - 纯行为克隆（BC）模型；
  - 俯视图（Bird’s‑Eye‑View, BEV）表征下的 IL 方法（如 ST‑P3、UniAD 等业界主流框架）；
  - 其他离线 RL 或 IL+RL 混合方法（如 TD3+BC、IQL 等经典离线 RL 算法在自动驾驶上的适配版本）。
- **评估指标**：位移误差、碰撞率、驾驶分数以及在长尾场景子集中的成功率和舒适度指标。

## 4. 资源与算力

- 论文提供的公开信息中**未明确注明所使用的 GPU 型号、数量及训练总时长**。通常此类端到端自动驾驶工作会使用若干块 NVIDIA A100 或 RTX 3090/4090 训练数天，但具体算力配置需查阅代码仓库或正式版本原文确认。本文此处暂无法给出精确算力数据。

## 5. 实验数量与充分性

- **主要实验组数**：
  - **主实验**：在 nuScenes 标准验证集上对比多个基线，考察常规场景和多种长尾场景（如无保护左转、狭窄道路、异形路口、暴雨/夜晚等）的性能。
  - **跨城市泛化实验**：测试模型在未见城市（如从波士顿迁移到新加坡）的迁移性能。
  - **消融实验**：至少包含以下模块的消融：① 移除竞争机制（变为简单多任务 IL+RL）② 移除潜世界模型想象推演（仅使用单步奖励）③ 移除 IL 锚定（纯 RL 训练）④ 不同 λ 权重与阈值敏感性分析。
  - **定性分析**：可视化规划轨迹、注意力图和想象推演示例。
- **充分性与公平性评价**：
  - 实验涵盖标准基准、长尾细分、跨域泛化和消融，设计较为全面。
  - 对比方法选取了当时主流的 IL 和离线 RL 方案，比较基准较公平。
  - 但所有实验均基于离线数据，未在真实车或闭环仿真中验证，结论的**外推到真实在线交互环境仍需谨慎**。
  - 长尾场景的划分依赖于数据集本身分布，可能存在分类主观性；消融虽然较细，但未报告不同随机种子下的方差。

## 6. 论文的主要结论与发现

- CoIRL‑AD 在离线设定下**稳定地将 RL 的奖励优化与 IL 的专家约束相结合**，有效缓解了模仿学习在长尾场景的泛化瓶颈。
- 竞争机制能够**自适应地权衡 IL 与 RL 的贡献**，防止 RL 策略过分偏离安全驾驶行为，同时保留探索高收益行为的能力。
- 潜世界模型的想象推演为离线 RL 提供了准确的长时域价值估计，是提升跨城泛化能力的关键因素。
- 综合而言，该框架在 nuScenes 的长尾场景和跨城市泛化指标上均取得显著提升，证明了解耦与协同竞争设计在离线自动驾驶中具有实际价值。

## 7. 优点：方法或实验设计上的亮点

- **问题针对性强**：直面离线自动驾驶中 IL 泛化差、RL 行为多样性不足的双重困境。
- **解耦设计新颖**：双策略竞争架构清晰地分离了模仿目标和奖励最大化目标，避免了梯度的恶意干扰。
- **世界模型赋能离线 RL**：利用隐空间想象推演进行长时域信用分配，减少对在线交互的依赖，思路在自动驾驶中较为前沿。
- **安全机制融入**：通过 IL 锚定和选择性迁移，天然内嵌了安全约束，对实车应用有潜在意义。
- **实验覆盖面广**：包含长尾场景细分与跨城泛化，贴近真实部署痛点，增强了结论的可信度。

## 8. 不足与局限

- **未报告算力与可复现细节**：GPU 型号、训练时间等缺失，可能影响他人复现时的资源评估。
- **离线‑真车间隙**：完全在离线数据集上训练和评估，未在闭环仿真器或真实车辆中验证安全性与实时性，应用部署风险尚存。
- **长尾场景依赖数据标注**：实验中的长尾子集依赖人工规则或标签定义，泛化到其他数据集时可能需要重新划分。
- **超参数敏感性**：竞争阈值、KL 权重等调节可能较为繁琐，虽有消融，但未探讨自动化超参调节策略。
- **世界模型的可解释性**：潜空间想象可能产生不符合物理规则的轨迹，论文未深入探讨世界模型的鲁棒性边界。
- **对比方法有限**：未与基于模型预测控制（MPC）或更先进离线 RL（如 CQL 重实现）在规划层面进行充分对比，可能高估自身相对优势。

（完）
