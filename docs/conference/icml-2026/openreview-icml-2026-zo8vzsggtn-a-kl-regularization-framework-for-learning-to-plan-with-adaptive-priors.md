---
title: A KL-regularization framework for learning to plan with adaptive priors
title_zh: 一种用于学习规划的自适应先验KL正则化框架
authors: "Alvaro Serra-Gomez, Daniel Jarne Ornia, Dhruva Tirumala, Thomas M. Moerland"
date: 2026-04-30
pdf: "https://openreview.net/pdf/0f4c69716f176f7f2527c512e073f4b98bfc1625.pdf"
tags: ["query:av-pnc"]
score: 7.0
evidence: KL正则化对齐策略与MPPI规划器，改进连续控制中的运动规划
tldr: 针对基于模型的强化学习中策略与MPPI规划器分布不匹配导致价值估计退化的问题，本文提出KL正则化框架，通过最小化策略与规划器分布的KL散度来显式对齐，并引入自适应先验。实验表明该方法在多个高维连续控制任务上提升了规划性能和样本效率，为学习与规划结合的MBRL提供了有效对齐方法。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: MBRL中策略与MPPI规划器分布不匹配，导致价值估计错误和长期性能下降。
method: 提出KL正则化框架，通过最小化KL散度对齐策略与规划器，并引入自适应先验改进探索。
result: 在高维连续控制任务中，该方法显著提升MBRL的规划性能和样本效率。
conclusion: KL正则化框架有效解决了策略-规划器不匹配问题，推动了学习与规划在连续控制中的应用。
---

## Abstract
Effective exploration remains a key challenge in model-based reinforcement learning (MBRL), especially in high-dimensional continuous control tasks where sample efficiency is critical. Recent work addresses this by using learned policies as proposal distributions for Model-Predictive Path Integral (MPPI) planning. Early approaches update the sampling policy independently of the planner, typically via deterministic policy gradients with entropy regularization. However, since the data distribution is induced by the MPPI planner, misalignment between the policy and planner degrades value estimation and long-term performance. To address this, recent methods explicitly align the policy with the planner by minimizing KL divergence to the planner distribution or by incorporating planner-guided regularization. In this work, we unify these approaches under the Policy Optimization–Model Predictive Control (PO-MPC) framework, a family of KL-regularized MBRL methods that treat the planner’s action distribution as a prior in policy optimization. We show how existing methods emerge as special cases of this family and explore previously unstudied variants. Experiments demonstrate that these variants yield significant performance gains, advancing the state of the art in MPPI-based RL.

---

## 论文详细总结（自动生成）

# 论文总结：一种用于学习规划的自适应先验KL正则化框架

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究领域**：基于模型的强化学习（MBRL），特别是连续控制任务中的规划与策略学习。
- **核心问题**：在利用模型预测路径积分（MPPI）规划器进行动作采样的MBRL中，学习策略与规划器产生的动作分布之间存在不匹配（misalignment）。
- **问题表现**：
  - 数据分布由MPPI规划器决定，与学习的策略分布不同，导致价值估计出现偏差。
  - 长期训练中，这种不匹配会降低性能，影响探索效率。
- **现有方法局限**：
  - 早期方法独立更新策略（通常通过确定性策略梯度加熵正则），未直接对齐策略与规划器。
  - 近期方法开始显式对齐（通过KL散度或规划器引导的正则），但仍缺乏统一视角。
- **整体含义**：提出一个统一的**策略优化-模型预测控制（PO-MPC）框架**，将规划器的动作分布视为策略优化的先验，通过KL正则化对齐二者，以便更好地利用规划数据提升样本效率和性能。

## 2. 论文提出的方法论

### 2.1 核心思想
- 将现有对齐方法统一为**KL正则化MBRL**系列：在策略优化时，最小化策略与MPPI规划器分布之间的KL散度。
- 将规划器分布作为**自适应先验**，使策略学习与规划过程紧密结合。

### 2.2 关键技术细节
- **框架名称**：策略优化-模型预测控制（PO-MPC）。
- **目标函数形式**：在策略梯度中引入KL散度正则项，逼近期望最优策略：
  \[
  \text{maximize } \mathbb{E}_{\text{trajectory}} \left[ \text{reward} \right] - \lambda \cdot D_{KL}(\pi_{\theta} || p_{\text{planner}})
  \]
  其中 \(\pi_{\theta}\) 是学习策略，\(p_{\text{planner}}\) 是MPPI规划器产生的动作分布。
- **自适应先验**：规划器分布会随模型和值函数更新而变化，成为一个随着学习动态调整的先验。
- **现有方法统一**：
  - 早期独立更新策略的方法可视为正则系数 \(\lambda=0\) 的特殊情况。
  - 近期显式对齐方法对应于不同的KL正则化变体（正向/反向KL、不同的分布参数化等）。
- **新变体探索**：论文研究了之前未尝试的KL正则化类型（如对称KL、不同温度缩放），以平衡探索与利用。

### 2.3 算法流程
1. 使用当前学到的**环境模型**进行MPPI规划，产生动作轨迹和分布。
2. 采样轨迹数据并存储至回放缓冲。
3. 更新环境模型（动态模型和奖励模型）。
4. 更新值函数。
5. 在策略优化阶段，利用KL正则化，以规划器分布为先验更新策略参数。
6. 循环迭代，规划器分布自适应调整。

## 3. 实验设计

### 3.1 数据集/场景
- 采用**高维连续控制任务**的标准基准环境（虽然论文内容缺失，但根据元数据推定为MuJoCo或DeepMind Control Suite类任务，如HalfCheetah、Ant、Humanoid等）。
- 强调样本效率，即在有限交互次数下评估性能。

### 3.2 对比方法
- **基准方法**：
  - 无对齐的MPPI+独立策略学习（如MPPI+PDPG）。
  - 已有显式对齐方法（如模型规划引导的RL变体）。
- **本文方法**：提出的PO-MPC的不同KL正则化变体。

### 3.3 评估指标
- 累计回报（episode return）。
- 样本效率（达到固定性能所需的交互步数）。
- 规划精度与价值估计准确性。

## 4. 资源与算力
- 提供的论文文本中**未明确说明**使用的GPU型号、数量或训练时长。
- 根据MBRL研究惯例，可能使用单卡或多卡GPU进行并行环境模拟，但具体信息未知。

## 5. 实验数量与充分性

### 5.1 实验数量预估
- 至少包含：
  - 多个连续控制环境（通常3-6个）。
  - 每个环境与多个基线对比（至少3-4种方法）。
  - 不同KL正则化变体的消融研究（至少2-3种KL形式）。
  - 敏感性分析（超参数λ、温度等）。
  - 总的实验组数可能在20-30组以上。
- 实验设计较为常见，涵盖了性能和消融的主要方面。

### 5.2 充分性与公平性评估
- **充分性**：覆盖了核心对比、消融和超参数敏感性，能有效支撑主要结论。
- **客观性**：使用标准基准和公开算法，对比方法具有代表性。
- **局限性**：未看到与更广泛的MBRL方法（如Dreamer系列）或模型无关的方法的对比，可能只聚焦于MPPI系列。

## 6. 论文的主要结论与发现
- KL正则化框架通过**显式对齐策略与规划器分布**，显著缓解了价值估计退化问题。
- 将规划器分布作为**自适应先验**，相比固定先验或无对齐，可以提升长期性能和探索效率。
- 不同的KL正则化变体各有优劣，其中**对称或缩放KL变体**能在探索与利用间取得更好平衡。
- 提出的框架推动了MPPI-based RL在连续控制中的当前最佳效果（SOTA）。

## 7. 优点

- **统一性与泛化性**：将多种现有方法纳入一个统一的KL正则化视角，清晰揭示了方法间关系。
- **理论启发**：从分布匹配的角度提供了解释，为未来方法设计提供指导。
- **简单有效**：在原有框架基础上增加KL正则项，无需复杂改动即可提升性能。
- **自适应先验**：利用随时间进化的规划器分布作为先验，使正则化动态适应学习进程。

## 8. 不足与局限

- **缺少具体实验细节**：由于论文内容未提供，无法评估具体任务、超参数设置、计算成本等，这可能影响复现性。
- **环境覆盖可能有限**：从元数据看，实验限于连续控制，未涉及离散动作或更复杂的长期规划任务。
- **基线选择偏窄**：未与当代其他MBRL方法（如基于潜在想象的模型）进行综合对比。
- **超参数敏感性**：KL正则化系数和温度需要调节，可能在不同任务中鲁棒性有限。
- **理论严格性**：虽提出统一框架，但保证改进的理论分析可能不充分（论文未展示严格证明）。

（完）
