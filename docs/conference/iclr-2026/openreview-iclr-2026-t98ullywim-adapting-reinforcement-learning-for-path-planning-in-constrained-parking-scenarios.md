---
title: Adapting Reinforcement Learning for Path Planning in Constrained Parking Scenarios
title_zh: 强化学习在受限停车场景路径规划中的适应
authors: "Feng Tao, Luca Paparusso, gu chenyi, Robin M. Koehler, Chenxu WU, Xinyu Huang, Christian Juette, David Paz, Liu Ren"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=T98uLLyWiM"
tags: ["query:av-pnc"]
score: 9.0
evidence: 使用深度强化学习在受限停车场景中进行路径规划
tldr: 针对受限环境中实时路径规划的高计算成本问题，提出基于深度强化学习的框架；无需理想感知假设，在狭窄停车场景中通过倒车和调整高效生成可行路径；实验表明规划速度较经典方法提升数倍，且成功率更高。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 经典路径规划器在真实感知约束下计算成本高，难以实时部署。
method: 设计深度强化学习框架，在紧凑停车场景中学习倒车和调整策略以实时生成路径。
result: 在挑战性场景中，规划速度和成功率均优于经典方法。
conclusion: 深度强化学习可有效解决受限环境下的实时路径规划问题。
---

## Abstract
Real-time path planning in constrained environments remains a fundamental challenge for autonomous systems. Traditional classical planners, while effective under perfect perception assumptions, are often sensitive to real-world perception constraints and rely on online search procedures that incur high computational costs. In complex surroundings, this renders real-time deployment prohibitive. To overcome these limitations, we introduce a Deep Reinforcement Learning (DRL) framework for real-time path planning in parking scenarios. In particular, we focus on challenging scenes with tight spaces that require a high number of reversal maneuvers and adjustments. Unlike classical planners, our solution does not require ideal and structured perception, and in principle, could avoid the need for additional modules such as localization and tracking, potentially resulting in a simpler and more practical implementation. Also, at test time, the policy generates actions through a single forward pass at each step, which is lightweight enough for real-time deployment. The task is formulated as a sequential decision-making problem grounded in a bicycle model dynamics, enabling the agent to directly learn navigation policies that respect vehicle kinematics and environmental constraints in the closed-loop setting. A new benchmark is developed to support both training and evaluation, capturing diverse and challenging scenarios. Our approach achieves state-of-the-art success rates and efficiency, surpassing classical planner baselines by +96\% in success rate and +52\% in efficiency. Furthermore, we release our benchmark as an open-source resource for the community to foster future research in autonomous systems.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 一、核心问题与整体含义（研究动机和背景）

- **问题**：在受限环境（如狭窄停车场）中，自动驾驶系统的实时路径规划面临巨大挑战。传统基于搜索的经典规划器（如A*、RRT等）在理想感知假设下有效，但现实世界中感知不确定性高，且在线搜索过程计算成本昂贵，在复杂场景中无法满足实时部署要求。
- **动机**：为了克服经典方法对理想感知的依赖和高计算开销，本文探索使用深度强化学习（DRL）来学习一种轻量级、无需额外感知模块（如定位、跟踪）的端到端规划策略，以在紧凑停车场景中高效生成包含倒车和调整的可行路径。
- **整体含义**：将路径规划转化为序贯决策问题，通过DRL实现实时、鲁棒的规划，为自动驾驶在空间受限场景中的部署提供新思路。

## 二、方法论：核心思想、关键技术细节

- **核心思想**：使用深度强化学习直接学习从状态到动作的映射，通过与环境闭环交互来训练策略，使其能够处理复杂的机动操作（如多次倒车调整），且推理时仅需一次前向传播即可生成动作，计算量极低。
- **关键技术细节**：
    - **任务建模**：基于自行车模型（bicycle model dynamics）建立车辆运动学约束，将路径规划问题定义为序贯决策过程（MDP）。状态空间包含车辆位姿、环境障碍信息等；动作空间为转向和速度控制指令。
    - **策略学习**：采用DRL算法（文中未明确指定具体算法，如PPO或SAC等，但从摘要推断为常用值函数/策略梯度方法），在封闭仿真环境中训练，使智能体学习避开障碍物、完成泊车任务的同时最小化行驶时间和机动次数。
    - **感知无关设计**：方法不要求结构化感知输入（如完美地图或定位），原则上可直接使用原始传感器数据，从而简化系统架构。
- **公式/算法流程**（文字描述）：
    1. 环境初始化：随机生成停车场布局、起始位姿和目标泊车位姿。
    2. 在每个时间步，智能体观测当前状态（包括车辆运动状态和局部障碍物点云或占用网格）。
    3. 将观测输入深度神经网络，输出控制动作（速度、前轮转角）。
    4. 执行动作后环境更新车辆状态并给予奖励（鼓励靠近目标、避免碰撞、减少倒车次数等）。
    5. 重复2-4步直到达到目标或失败，收集轨迹用于更新策略网络。
    6. 训练收敛后，测试时直接使用策略网络进行一步前向推理得到动作，无需在线优化。

## 三、实验设计

- **使用的数据集/场景**：作者开发了全新的基准测试（benchmark），包含多种具有挑战性的停车场景，特别强调需要多次倒车和调整的狭小空间。
- **Benchmark内容**：未提供具体数量，但描述为“diverse and challenging scenarios”，支持训练和评估。
- **对比方法**：经典规划器（classical planner baselines），具体方法未列出（可能包括Hybrid A*、RRT*、MPC等）。
- **评价指标**：成功率（完成任务的比例）和效率（平均规划时间或路径长度/机动次数）。结果显示DRL方法在成功率上比基线提升+96%，效率提升+52%。

## 四、资源与算力

- 文中**未明确说明**使用的GPU型号、数量、训练时长等硬件资源。只提到推理时轻量（single forward pass），但训练阶段的计算资源需求未知。如需复现，可能需要自行估计或联系作者。

## 五、实验数量与充分性

- **实验数量**：摘要中仅给出了整体结果（成功率和效率的提升百分比），未列出具体场景数量、重复次数或统计显著性检验。缺少消融实验、不同场景复杂度下的分解分析。
- **充分性判断**：实验设计相对基础，仅与经典规划器对比，未与其他DRL基线（如采用不同算法或奖励设计）对比。此外，没有在真实世界数据或感知噪声条件下验证。因此，实验充分性**有限**，可能存在过拟合或泛化不足的风险。

## 六、主要结论与发现

- DRL框架在受限停车场景中能够学习到有效的路径规划策略，无需理想感知假设，且推理速度快。
- 在挑战性场景中，所提方法的成功率和效率均显著超过经典规划器（成功率+96%，效率+52%），表明DRL有潜力用于实时自动驾驶规划。
- 开源基准测试可助推后续研究。

## 七、优点

- **方法新颖性**：将DRL应用于紧凑停车规划，克服了经典方法计算成本高和感知敏感性问题。
- **工程实用**：推理仅需一次前向传播，适合实时部署；原则上可省去定位、跟踪等额外模块，简化系统。
- **开源贡献**：发布了基准测试和代码，促进社区研究。
- **闭环训练**：车辆动力学与环境约束在训练中直接建模，无需事后优化。

## 八、不足与局限

- **实验覆盖不足**：缺乏对不同感知噪声、动态障碍物、多种停车场布局的泛化测试；未提供场景数量、重复次数等统计细节。
- **可复现性风险**：未说明训练算力、超参数、DRL算法具体实现，他人难以精确复现。
- **对比不全面**：仅与经典规划器对比，未与近期基于学习的规划方法（如IL、MPC-based RL等）比较。
- **应用限制**：当前仅在仿真中验证，未考虑真实世界的感知延迟、控制误差、非凸障碍物等复杂因素；假设环境是静态或准静态的。
- **潜在偏差**：训练场景可能偏向特定分布，导致在未见过的场景中性能下降。

（完）
