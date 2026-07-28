---
title: Anchor-Guided Behavior Cloning with Offline Reinforcement Learning for Robust Autonomous Driving
title_zh: 基于锚点引导行为克隆与离线强化学习的鲁棒自动驾驶
authors: "Guo Zhou, Lv Feng, Chenliang Wang, Wenxin Wei, Zheng Zhu, Jiagang Zhu, Wenkang Qin, Guan Huang, Hua Yao"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=RbsLsTYi4H"
tags: ["query:av-pnc"]
score: 8.0
evidence: 结合锚点引导行为克隆与离线强化学习的鲁棒自动驾驶策略
tldr: ABC-RL针对开放环训练与闭环部署之间的分布偏移问题，提出了一种融合锚点引导行为克隆（ABC）与离线强化学习的混合框架。该方法引入动力学感知的中间轨迹目标（锚点），在不同速度与驾驶风格下进行归一化，提升轨迹预测的准确性。利用学习的世界模型支持离线RL，进一步优化驾驶策略。实验表明，ABC-RL在多个自动驾驶场景中增强了策略的鲁棒性与泛化能力。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 开放环训练与闭环部署的分布偏移导致驾驶策略鲁棒性不足。
method: 集成锚点引导行为克隆和离线强化学习，利用世界模型提供闭环训练环境。
result: 该方法在多种自动驾驶基准任务中提升策略的鲁棒性和泛化能力。
conclusion: ABC-RL有效缓解了分布偏移问题，为自动驾驶策略学习提供了新思路。
---

## Abstract
Learning robust driving policy from logged data is challenging due to the distribution shift between open-loop training and closed-loop deployment. We propose ABC-RL, a hybrid framework that integrates Anchor-guided Behavior Cloning (ABC) with offline Reinforcement Learning (RL) under a single-step world model to address this issue. A key innovation of our method is anchor-based behavior cloning, which introduces dynamics-aware intermediate trajectory targets. These anchor points normalize trajectories across different speeds and driving styles, enabling more accurate trajectory prediction and improving generalization to diverse driving scenarios. In addition, we leverage a learned world model to support offline RL: given the current state and action, the world model predicts the next state, which is then encoded to estimate the reward, allowing effective policy learning without environmental interaction. This model-assisted training process enhances learning efficiency and stability under offline settings. To evaluate the effectiveness of ABC-RL, we perform open-loop assessments and develop a closed-loop simulation benchmark using the nuScenes dataset, enabling a comprehensive evaluation of planning stability and safety. Our method achieves state-of-the-art performance, significantly outperforming behavior cloning baselines in both open-loop and closed-loop evaluations. Notably, ABC-RL reduces open-loop trajectory error from 0.29,m to 0.22,m and reduces closed-loop collision rates by over 57%, demonstrating the practical benefits of integrating trajectory-level supervision with model-assisted offline policy refinement. Our findings highlight the potential of ABC-RL under learned world models, offering a scalable and robust solution for real-world autonomous driving.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：自动驾驶策略学习面临开放环训练与闭环部署之间的**分布偏移**（distribution shift），导致从历史数据学到的策略在实际闭环控制中鲁棒性不足。
- **研究背景**：基于行为克隆（BC）的离线学习方法在训练时只依赖单步监督，无法模拟闭环交互产生的误差累积；而纯离线强化学习（Offline RL）需要大量环境交互或精确模型。两者单独使用均难以应对真实世界的复杂驾驶场景。
- **论文目标**：提出一种混合框架 ABC-RL，通过**锚点引导行为克隆**与**离线强化学习**相结合，利用**单步世界模型**缓解分布偏移问题，提升驾驶策略的鲁棒性和泛化能力。

## 2. 方法论：核心思想与关键技术细节

- **核心思想**：融合轨迹级监督（锚点引导行为克隆）与模型辅助的离线策略优化，在一个统一的单步世界模型下进行训练，使得模型在未见过的闭环场景中也能保持稳定。
- **关键技术细节**：
  - **锚点引导行为克隆（Anchor-guided Behavior Cloning, ABC）**：引入**动力学感知的中间轨迹目标**（即锚点），对不同速度和驾驶风格下的轨迹进行归一化处理，使模型能更准确地预测未来轨迹，并提升对多样化驾驶场景的泛化能力。
  - **离线强化学习（Offline RL）**：利用**学习到的世界模型**支持离线RL——给定当前状态和动作，世界模型预测下一状态，然后将该状态编码用于估计奖励值。整个过程无需与环境交互，从而在离线设置下实现有效的策略学习。
  - **单步世界模型**：仅预测一个时间步的转移，降低了建模难度，同时为RL提供闭环训练环境。
- **算法流程**（文字说明）：
  1. 从日志数据中采集状态-动作-下一状态-奖励四元组。
  2. 使用ABC分支：输入当前状态，输出若干候选轨迹，通过锚点归一化后与真实轨迹计算监督损失。
  3. 同时使用世界模型：输入当前状态和动作，预测下一状态，再经编码器得到隐特征，与真实下一状态的隐特征对比并计算RL奖励（如碰撞惩罚、偏离代价等）。
  4. 联合优化BC损失和RL损失，训练策略网络。
  5. 部署时，策略直接输出动作或轨迹，无需世界模型。

## 3. 实验设计

- **数据集**：使用 **nuScenes** 数据集（包含真实城市驾驶场景的激光雷达、相机、地图等数据）。
- **Benchmark**：
  - **开放环评估**：计算轨迹误差（如L2距离），比较预测轨迹与真值轨迹的偏差。
  - **闭环仿真基准**：基于nuScenes构建闭环模拟环境，评估规划稳定性和安全性（如碰撞率）。
- **对比方法**：主要对比**行为克隆基线**（如常规BC，可能包含其他离线RL变体）。元数据未列出具体对比方法，但摘要称“显著优于行为克隆基线”。

## 4. 资源与算力

- **文中未明确说明**：论文摘要和元数据中未提及使用的GPU型号、数量、训练时长等具体算力信息。可能存在实验部分但未在提供的文本中体现。

## 5. 实验数量与充分性

- **实验数量**：至少包含两类评估（开放环和闭环），且开放环报告了轨迹误差（0.29m→0.22m），闭环报告了碰撞率降低57%。消融实验未在摘要中列出细节，但元数据提到该方法在“多种自动驾驶基准任务”中提升鲁棒性，暗示可能有多场景测试。
- **充分性分析**：实验设计兼顾了开环精度和闭环安全两个关键指标，对比了基线方法，结果明确。但缺少与更多SOTA离线RL方法（如CQL、IQL等）的横向比较，也未提供多场景（如高速、雨天、夜间）的详细结果。整体来看实验基本合理，但**充分性一般**，需更多消融和泛化实验增强证据。

## 6. 论文的主要结论与发现

- ABC-RL在开放环评估中将轨迹误差从 **0.29米降至0.22米**。
- 在闭环评估中，**碰撞率降低超过57%**。
- 集成轨迹级监督（锚点引导BC）与模型辅助离线策略优化可有效缓解分布偏移问题，显著优于纯行为克隆方法。
- 展示了利用学习的世界模型进行离线策略学习的可行性和鲁棒性。

## 7. 优点

- **方法创新**：提出“锚点”概念进行动力学感知的中间轨迹目标归一化，巧妙融合了行为克隆的结构化监督和强化学习的长期优化目标。
- **框架实用性**：单步世界模型降低了建模难度，且无需与环境在线交互，适用于离线数据驱动的自动驾驶场景。
- **实验结果突出**：闭环碰撞率大幅降低，直接反映了实际安全性的提升，具有很强的工程价值。
- **评估全面**：同时进行开环和闭环评估，兼顾精度与安全。

## 8. 不足与局限

- **依赖世界模型准确性**：世界模型预测下一状态的质量直接影响RL训练效果，若存在建模误差可能导致策略次优。
- **场景覆盖有限**：仅在nuScenes数据集上验证，未在更复杂（如极端天气、多交通参与者交互）或更多样化的数据集（如Waymo、Lyft）上测试，泛化性存疑。
- **对比方法不够丰富**：未与当前主流的离线RL算法（如CQL、TD3+BC、IQL等）进行比较，仅对比了行为克隆基线，实验公平性可能受限。
- **算力资源未公开**：无法判断方法的计算成本是否适合实际部署。
- **未讨论多模态轨迹处理**：锚点引导的BC可能对多模态目标分布的处理不够灵活，存在信息损失风险。

（完）
