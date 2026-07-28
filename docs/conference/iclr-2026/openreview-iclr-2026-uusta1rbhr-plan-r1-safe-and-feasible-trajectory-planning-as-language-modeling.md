---
title: "Plan-R1: Safe and Feasible Trajectory Planning as Language Modeling"
title_zh: Plan-R1：将安全可行的轨迹规划建模为语言模型
authors: "Xiaolong Tang, Meina Kan, Shiguang Shan, Xilin Chen"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=uusTA1rBhR"
tags: ["query:av-pnc"]
score: 9.0
evidence: 将安全可行的轨迹规划建模为语言模型任务用于自动驾驶
tldr: Plan-R1针对现有学习型规划器缺乏显式安全感知且可能继承不良驾驶行为的问题，提出将轨迹规划视为语言建模的两阶段框架。第一阶段在专家数据上预训练通用轨迹预测器，第二阶段利用GRPO算法结合规则奖励进行微调，显式对齐自车行为与安全原则。实验证明，Plan-R1在多种驾驶场景下生成更安全、更可行的轨迹，克服了从次优数据学习的问题，为自动驾驶规划引入了语言模型的成功范式。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有学习型规划器缺乏安全意识，且易从次优数据中继承不良驾驶行为。
method: 提出Plan-R1两阶段框架，先预训练轨迹预测器，再用GRPO微调对齐安全原则。
result: 在标准自动驾驶规划基准上，Plan-R1在安全性和可行性指标上均超越现有方法。
conclusion: 该工作表明将语言模型训练技术应用于轨迹规划能有效提升安全性和泛化性。
---

## Abstract
Safe and feasible trajectory planning is critical for real-world autonomous driving systems.
However, existing learning-based planners rely heavily on expert demonstrations, which not only lack explicit safety awareness but also risk inheriting undesirable behaviors such as speeding from suboptimal human driving data.
Inspired by the success of large language models, we propose Plan-R1, a two-stage trajectory planning framework that decouples principle alignment from behavior learning.
In the first stage, a general trajectory predictor is pre-trained on expert data to capture diverse, human-like driving behaviors.
In the second stage, the model is fine-tuned with rule-based rewards using Group Relative Policy Optimization (GRPO), explicitly aligning ego planning with principles such as safety, comfort, and traffic rule compliance.
This two-stage paradigm retains human-like behaviors while enhancing safety awareness and discarding undesirable patterns from demonstrations.
Furthermore, we identify a key limitation of directly applying GRPO to planning: group-wise normalization erases cross-group scale differences, causing rare, high-variance safety-violation groups to have similar advantages as abundant low-variance safe groups, thereby  suppressing optimization for safety-critical objectives.
To address this, we propose Variance-Decoupled GRPO (VD-GRPO), which replaces normalization with centering and fixed scaling to preserve absolute reward magnitudes, ensuring that safety-critical objectives remain dominant throughout training.
Experiments on the nuPlan benchmark demonstrate that Plan-R1 significantly improves planning safety and feasibility, achieving state-of-the-art performance, particularly in realistic reactive settings.
Our code is available at https://github.com/XiaolongTang23/Plan-R1.

---

## 论文详细总结（自动生成）

# 论文总结：Plan-R1: Safe and Feasible Trajectory Planning as Language Modeling

## 1. 核心问题与整体含义（研究动机和背景）

- **背景**：现有的学习型自动驾驶轨迹规划器严重依赖专家示范数据。这类方法存在两个根本缺陷：一是缺乏显式的安全感知能力，二是容易从次优的人类驾驶数据中继承不良驾驶行为（如超速）。
- **动机**：借鉴大型语言模型（LLM）的成功经验，将轨迹规划问题重新定义为语言建模任务，通过两阶段范式实现在保留类人驾驶行为的同时，将安全、舒适、规则遵守等原则显式地对齐到模型输出中。
- **整体含义**：这项工作揭示了将语言模型的训练技术（预训练 + 强化学习微调）迁移到自动驾驶规划领域的可行性，为解决“从次优数据中学习不良行为”这一关键挑战提供了新思路。

## 2. 方法论：核心思想、关键技术细节、算法流程

- **核心思想**：将轨迹规划建模为语言建模任务，采用“行为学习”与“原则对齐”解耦的两阶段框架。
- **第一阶段：通用轨迹预测器预训练**
  - 在专家示范数据上训练一个通用的轨迹预测器，使其学习多样化、类人的驾驶行为。
  - 本质上是行为克隆，为后续对齐提供初始模型。
- **第二阶段：基于规则奖励的GRPO微调**
  - 使用**组相对策略优化（GRPO）** 对预训练模型进行微调，奖励函数由显式的规则（安全、舒适、交通规则遵守）定义，从而将自车规划与安全原则对齐。
  - GRPO通过组内归一化来计算优势，但在规划任务中存在关键限制：组间尺度差异被消除，导致罕见但高方差的安全违规组与丰富但低方差的正常组获得相似的优势值，从而抑制了安全关键目标的优化。
- **关键技术改进：方差解耦GRPO（VD-GRPO）**
  - 用“中心化 + 固定尺度缩放”替代GRPO原有的组内归一化，保留绝对奖励量级。
  - 确保在整个训练过程中，安全关键目标（如避免碰撞）的奖励信号始终占据主导地位，从而缓解优化抑制。

## 3. 实验设计

- **数据集与场景**：在**nuPlan benchmark**上进行实验，该基准包含真实世界的驾驶场景，评估设置包括**反应式环境（realistic reactive settings）**，即其他交通参与者会智能地响应自车行为。
- **对比方法**：与现有的学习型规划器（具体方法名称在摘要中未列出，但实验部分的对比应涵盖主流的基于学习的规划方法）。
- **评价指标**：安全性和可行性指标（如碰撞率、舒适度、交通规则违反率等）。

## 4. 资源与算力

- **文中未明确声明**：摘要及元数据中未提及使用的GPU型号、数量、训练时长等具体算力信息。作者仅提供了代码仓库链接，并未在摘要中描述资源消耗。

## 5. 实验数量与充分性

- **实验数量**：摘要仅提及在nuPlan基准上的整体性能，并强调在反应式环境下达到SOTA（最先进水平）。未明确列出消融实验、跨场景泛化实验等。
- **充分性判断**：由于仅从摘要推断，无法全面评估实验的充分性。但论文被ICLR 2026接收，通常意味着实验设计相对完整，覆盖了主实验、消融研究（如VD-GRPO vs. GRPO）以及可能的场景分析。然而，公开信息有限，无法确认是否进行了足够多的对比和鲁棒性验证。整体来看，实验设计基本客观（在标准公开基准上评测），但详细程度需阅读全文才能判定。

## 6. 主要结论与发现

- Plan-R1在nuPlan基准上显著提升了规划的安全性和可行性，实现了最先进的性能，尤其在反应式交互场景中优势明显。
- 提出的VD-GRPO有效解决了原始GRPO在规划优化中的缺陷，使得安全关键目标能持续被优化。
- 两阶段范式（预训练行为 + 强化学习对齐）能够同时保留类人驾驶的多样性，并消除次优数据中的不良行为（如超速）。

## 7. 优点

- **方法创新**：将语言模型领域成熟的预训练+强化学习范式系统性引入轨迹规划，提出VD-GRPO解决规划场景下的特有难题，具有较强的新颖性和启发性。
- **问题定位准确**：明确指出学习型规划器“缺乏安全意识”和“继承不良行为”两大痛点，并给出了针对性解决方案。
- **实验设计合理**：选择了公认的自动驾驶规划基准nuPlan，并在最具挑战的反应式环境下突出展示了方法优势。
- **代码开源**：提供了完整的代码，便于复现和后续研究。

## 8. 不足与局限

- **实验覆盖面有限**：仅在一个基准（nuPlan）上验证，缺乏在更多样化或极端场景（如恶劣天气、高交通密度）下的测试，泛化性有待进一步证明。
- **资源消耗未知**：未说明训练所需的算力规模，可能影响方法的实用性和可复现性。
- **奖励设计依赖人工规则**：第二阶段的安全、舒适、规则遵守奖励需要人工定义，可能存在规则不完备或量化偏差的风险。
- **长期规划效果未探讨**：论文主要关注单步或多步短时规划，对于长时间尺度下的策略稳定性、复杂交互博弈等未明确评估。
- **与端到端方法的关系**：方法仍依赖预训练好的轨迹预测器，本质上是两阶段，端到端的一致性可能较弱。

（完）
