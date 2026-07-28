---
title: "READ: End-to-End Autonomous Driving Made Safer with Efficient Reinforcement Learning"
title_zh: READ：通过高效强化学习使端到端自动驾驶更安全
authors: "Zhewen Yang, Yuanhui Huang, Wenzhao Zheng, Yunpeng Zhang, Dalong Du, Jie Zhou, Jiwen Lu"
date: 2025-09-13
pdf: "https://openreview.net/pdf?id=UOYkiemcUP"
tags: ["query:av-pnc"]
score: 8.0
evidence: READ利用强化学习优化端到端驾驶中的决策策略
tldr: 端到端模型通过模仿学习训练后行为多样性不足，且存在分布偏差。本文提出READ框架，使用轻量级强化学习微调预训练模型的动作概率分布，使其偏向最优而非单纯模仿。实验表明READ有效提升了闭环安全性、效率和多样性。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 模仿学习导致策略行为多样性差，且存在分布不匹配问题。
method: 提出结构化策略精炼的RL微调框架，重新校准预训练模型的输出动作空间概率分布。
result: 轻量级RL更新即可显著提升策略的安全性和效率，且不改变模型结构。
conclusion: 强化学习微调是提升模仿学习策略泛化性和安全性的有效手段。
---

## Abstract
Autonomous driving planning requires synthesizing perceptual cues into safe and efficient trajectories, yet current end-to-end models trained solely by imitation learning often suffer from limited behavioral diversity and distributional mismatch.
To this end,we introduce READ, a reinforcement learning-based fine-tuning framework that significantly enhances pre-trained end-to-end driving models through structured policy refinement. 
Our approach is grounded in the observation that although certain models already support diverse trajectory generation, their output action-space-probability-distributions are biased toward imitation rather than optimality.
READ efficiently recalibrates these distributions using lightweight RL updates, avoiding catastrophic forgetting while promoting high-reward behaviors. 
Our approach also incorporates a novel reward decomposition strategy,designed to resolve the inefficiency of training with a composite reward signal.
Such signals obscure which behaviors lead to success, making it difficult for the policy to discern and reinforce high-reward patterns. 
Our method decomposes the reward into semantically clear components, each providing a well-defined optimization objective, enabling the policy to independently learn and balance distinct objectives. 
This leads to more efficient exploration, better credit assignment, and significantly improved convergence compared to using a single comprehensive reward.
Evaluated on the NavSim benchmark with DiffusionDrive as the baseline, READ significantly enhances driving performance with only minimal fine-tuning: it raises the PDMScore from 87.7 to 88.8 after only 2  epochs of training with a learning rate of $4.5 \times 10^{-5}$, compared to the original 100 training epochs at a rate of $6.4 \times 10^{-4}$.
Further open-loop evaluations of our method on nuScenes dataset show that READ reduces the collision rate of original DiffusionDrive-nusc branch baseline model by over 60\% (from 0.088\% to 0.031\%) while maintaining comparable L2 error (58.56 vs 58.32) after the same brief training of 1 epoch(about just 20 minutes), demonstrating its capacity to surpass expert demonstrations and learn safer driving policies. 
READ provides an efficient and effective pathway for reinforcement learning-based optimization in safety-critical autonomous driving systems.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：当前端到端自动驾驶模型通常完全依赖模仿学习（Imitation Learning, IL）进行训练，导致两个关键缺陷：  
  - **行为多样性不足**：模型倾向于复现专家轨迹，缺乏探索不同驾驶策略的能力。  
  - **分布不匹配（Distributional Mismatch）**：训练数据来自专家演示，但部署时遇到未见过的状态（OOD）容易产生错误。
- **研究动机**：为了提高自动驾驶的安全性、效率和泛化性，需要引入能够优化策略而非简单模仿的机制。强化学习（RL）天然适合探索高回报行为，但直接从头训练RL代价高且易遗忘预训练知识。
- **整体含义**：本文提出**READ（Reinforcement Learning-based Fine-tuning for Autonomous Driving）**框架，通过轻量级RL微调预训练的端到端模型，在保持原有结构的同时，显著提升策略的安全性和效率，解决模仿学习的内在局限性。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 核心思想
- 观察到预训练模型的输出动作空间概率分布偏向于“模仿”而非“最优”，因此通过轻量级RL更新重新校准该分布，使其偏向高回报行为，同时利用奖励分解提高训练效率和收敛速度。

### 关键技术细节
- **结构化策略精炼**：在预训练模型（如DiffusionDrive）上附加RL微调层，仅更新少量参数（或以低学习率微调全部参数），避免灾难性遗忘。
- **奖励分解策略（Reward Decomposition）**：  
  - 复合奖励信号（如安全性+效率的加权和）会模糊行为与结果的关联，导致策略难以判别哪些行为真正带来高回报。  
  - **分解方法**：将复合奖励拆解为语义清晰的独立分量（例如：碰撞避免奖励、车道保持奖励、速度效率奖励等），每个分量提供明确的优化目标，使策略能够独立学习并平衡不同目标。
- **算法流程**（文字描述）：  
  1. 使用预训练模型（如DiffusionDrive）初始化策略网络。  
  2. 在仿真环境中（NavSim）或真实数据集（nuScenes）上运行策略，收集轨迹。  
  3. 对每条轨迹计算分解后的奖励分量，然后分别进行信用分配（Credit Assignment）。  
  4. 通过策略梯度方法（如PPO）更新策略参数，最大化总奖励（各分量之和或加权和）。  
  5. 仅需少量epoch（例如2个epoch或1个epoch）即可收敛，且学习率远低于原始训练（如4.5×10⁻⁵ vs 6.4×10⁻⁴）。

### 公式/算法流程（文字说明）
- 未给出具体公式，但可推断采用标准RL更新：\[ \theta_{new} = \arg\max_{\theta} \mathbb{E}_{\tau \sim \pi_{\theta}} [\sum_t r_t] \]，其中 \( r_t \) 是分解奖励的加权和。

## 3. 实验设计：数据集、基准、对比方法

- **基准（Benchmark）**：NavSim，一个闭环仿真评测平台（包含多种驾驶场景和指标如PDMScore）。
- **基线模型**：DiffusionDrive（扩散模型驱动的端到端驾驶模型）。
- **对比设置**：  
  - **闭环实验**：在NavSim上对比原始DiffusionDrive（训练100 epochs，学习率6.4×10⁻⁴）与READ微调版（仅2 epochs，学习率4.5×10⁻⁵），主要指标为PDMScore（从87.7提升至88.8）。  
  - **开环实验**：在nuScenes数据集上对原始DiffusionDrive-nusc分支进行1 epoch微调（约20分钟），对比碰撞率（从0.088%降至0.031%）和L2误差（58.56 vs 58.32，基本持平）。
- **数据集**：  
  - NavSim仿真环境（用于闭环评估）。  
  - nuScenes真实数据集（用于开环评估）。
- **消融实验**：文中未明确列出，但提到了奖励分解策略的有效性（通过对比使用复合奖励 vs 分解奖励的收敛效率）。

## 4. 资源与算力（明确信息或缺省说明）

- **未明确说明**：论文摘要和元数据中未提及所使用的GPU型号、数量、训练时长等具体算力信息。仅提到nuScenes开环微调仅需约20分钟（1 epoch），但未说明硬件配置。  
- **推测**：鉴于模型为扩散模型且微调非常轻量，可能使用单卡或双卡GPU（如A100或RTX 3090），但无法确认。

## 5. 实验数量与充分性分析

- **实验数量**：主要呈现两组核心实验结果（闭环NavSim和开环nuScenes），每组均包含与基线的对比。缺少多场景、多基线模型的横向对比（如对比其他RL微调方法或不同预训练模型）。
- **充分性**：  
  - **正面**：提供了闭环和开环两种评价方式，且指标覆盖安全性（碰撞率）、效率（PDMScore）和精度（L2误差），具有一定说服力。  
  - **不足**：  
    - 未进行多种预训练模型（如UniAD、ST-P3等）的泛化实验。  
    - 未提供在nuScenes上闭环评测结果（仅开环）。  
    - 消融实验未详细展开，例如缺少“无奖励分解”的对比或不同分解方式的对比。  
    - 统计显著性、多随机种子重复实验未提及。
- **客观公平性**：对比均基于相同基线且微调后性能提升，但微调epoch数远少于原始训练，可能存在原始训练不充分导致的“苹果与橘子”比较风险。

## 6. 论文的主要结论与发现

- **主要结论**：强化学习微调是提升模仿学习策略泛化性和安全性的高效手段。READ框架通过轻量级RL更新和奖励分解，可以：
  - 显著降低碰撞率（开环降低60%以上）。
  - 在保持或略微提升精度（L2误差）的同时提高闭环综合得分（PDMScore）。
  - 仅需极少训练成本（1~2 epochs）即可超越专家演示，学习更安全的驾驶策略。
- **关键发现**：预训练模型的输出概率分布偏向于模仿而非最优，RL微调可有效重新校准该分布；复合奖励信号会阻碍策略学习，分解后能大幅提升训练效率和收敛性能。

## 7. 优点：方法或实验设计亮点

- **方法亮点**：
  - **轻量级微调**：避免从头训练RL，计算开销极小（20分钟或2 epochs），适合实际部署。
  - **奖励分解**：巧妙解决了复合奖励下信用分配困难的问题，增强了探索和收敛能力。
  - **结构不变性**：不改变预训练模型架构，便于集成到现有端到端系统中。
- **实验设计亮点**：
  - 同时评估闭环和开环性能，覆盖仿真和真实数据集。
  - 展示了微调后策略不仅更安全（碰撞率下降），且未牺牲路径精度（L2误差持平）。

## 8. 不足与局限

- **实验覆盖不足**：  
  - 仅测试了一个基线模型（DiffusionDrive），未验证对其他端到端模型（如Transfuser、LAV等）的泛化性。  
  - 缺乏在多样化天气、光照、交通密度等挑战性场景下的鲁棒性分析。  
  - 未进行真实车辆闭环测试，仅停留在仿真和开环。
- **偏差风险**：  
  - 原始训练可能并未充分收敛（100 epochs vs 2 epochs），导致提升部分来自于欠拟合。  
  - 开环碰撞率极低（0.088%→0.031%），可能由于nuScenes数据集本身碰撞样本极少，微调后过拟合到安全动作。
- **应用限制**：  
  - 奖励分解需要手动设计语义分量，泛化到新任务时需重新设计。  
  - 未讨论模拟到现实（Sim-to-Real）的迁移问题，仿真环境中的奖励设计可能不匹配真实动态。
  - 缺乏关于算力和推理效率的详细说明，难以评估实际部署成本。

（完）
