---
title: "CarPlanner: Consistent Auto-regressive Trajectory Planning for Large-Scale Reinforcement Learning in Autonomous Driving"
title_zh: CarPlanner：面向自动驾驶大规模强化学习的一致性自回归轨迹规划
authors: "Zhang, Dongkun, Liang, Jiaming, Guo, Ke, Lu, Sha, Wang, Qi, Xiong, Rong, Miao, Zhenwei, Wang, Yue"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_CarPlanner_Consistent_Auto-regressive_Trajectory_Planning_for_Large-Scale_Reinforcement_Learning_in_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 9.0
evidence: 一致自回归轨迹规划结合强化学习
tldr: 基于强化学习的轨迹规划器面临训练效率低和难以扩展到大场景的问题。本文提出CarPlanner，采用一致性自回归轨迹规划结构，利用RL生成多模态轨迹。自回归结构支持高效大规模RL训练，一致性约束确保时间步间稳定。在多种复杂驾驶场景中展示了优于现有方法的规划和泛化能力，为大规模RL轨迹规划提供了可行方案。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-carplanner-consistent-auto-regressive-trajectory-planning-for-large-scale-reinforcement-learning-in-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 802, \"height\": 830, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-carplanner-consistent-auto-regressive-trajectory-planning-for-large-scale-reinforcement-learning-in-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1730, \"height\": 489, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-carplanner-consistent-auto-regressive-trajectory-planning-for-large-scale-reinforcement-learning-in-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1774, \"height\": 973, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-carplanner-consistent-auto-regressive-trajectory-planning-for-large-scale-reinforcement-learning-in-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 880, \"height\": 449, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-carplanner-consistent-auto-regressive-trajectory-planning-for-large-scale-reinforcement-learning-in-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 882, \"height\": 314, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-carplanner-consistent-auto-regressive-trajectory-planning-for-large-scale-reinforcement-learning-in-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1779, \"height\": 379, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-carplanner-consistent-auto-regressive-trajectory-planning-for-large-scale-reinforcement-learning-in-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1775, \"height\": 543, \"label\": \"Table\"}]"
motivation: 现有RL轨迹规划器训练效率低，难以处理大规模真实场景。
method: 提出一致自回归轨迹规划器，结合RL生成多模态轨迹。
result: 实现高效大规模训练，在复杂场景中规划和泛化性能优异。
conclusion: CarPlanner推动了大规模RL在轨迹规划中的应用。
---

## Abstract
Trajectory planning is vital for autonomous driving, ensuring safe and efficient navigation in complex environments. While recent learning-based methods, particularly reinforcement learning (RL), have shown promise in specific scenarios, RL planners struggle with training inefficiencies and managing large-scale, real-world driving scenarios.In this paper, we introduce CarPlanner, a Consistent auto-regressive Planner that uses RL to generate multi-modal trajectories. The auto-regressive structure enables efficient large-scale RL training, while the incorporation of consistency ensures stable policy learning by maintaining coherent temporal consistency across time steps. Moreover, CarPlanner employs a generation-selection framework with an expert-guided reward function and an invariant-view module, simplifying RL training and enhancing policy performance.Extensive analysis demonstrates that our proposed RL framework effectively addresses the challenges of training efficiency and performance enhancement, positioning CarPlanner as a promising solution for trajectory planning in autonomous driving.To the best of our knowledge, we are the first to demonstrate that the RL-based planner can surpass both IL- and rule-based state-of-the-arts (SOTAs) on the challenging large-scale real-world dataset nuPlan. Our proposed CarPlanner surpasses RL-, IL-, and rule-based SOTA approaches within this demanding dataset.

---

## 论文详细总结（自动生成）

### 论文详细中文总结

#### 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：基于强化学习（RL）的轨迹规划器在自动驾驶中面临两大挑战：**训练效率低下**（模型无关RL需要CPU模拟器反复rollout策略，耗时巨大）和**性能不足**（现有RL方法在大规模真实场景数据集nuPlan上未能超越模仿学习（IL）或基于规则的SOTA方法）。
- **研究动机**：尽管IL方法存在分布偏移和因果混淆问题，RL可通过奖励函数提供更丰富的监督来缓解这些问题，但直接应用RL到大规模、多模态轨迹生成任务中难以实现高效训练和稳定策略学习。
- **整体含义**：本文提出CarPlanner，首次证明RL-based规划器能够在nuPlan大规模数据集上全面超越IL和规则方法，为大规模RL自动驾驶规划提供了可行方案。

#### 2. 方法论：核心思想、关键技术细节
- **核心思想**：采用**一致自回归（Consistent Auto-regressive）** 结构生成多模态轨迹，将决策过程分解为**模式选择器**和**轨迹生成器**两个部分，并通过**专家引导奖励函数**和**不变视图模块（IVM）** 简化RL训练并提升泛化能力。
- **关键技术细节**：
    - **框架流程（生成-选择框架）**：
        1. **非反应式转移模型**：基于初始状态一次性预测所有交通代理的未来轨迹（使用PointNet和Transformer编码器）。
        2. **模式选择器**：接收初始状态和**纵-横向分解模式**（纵向：平均速度标量；横向：地图搜索的候选路线），输出每个模式的概率得分。模式特征作为Transformer解码器的查询，与地图、代理特征融合。
        3. **轨迹生成器**：以**一致模式c**为条件，自回归解码每个时间步的ego车辆下一时刻位姿（动作a_t）。使用**不变视图模块（IVM）** 预处理状态：KNN筛选邻近元素、将所有坐标转换至当前ego坐标系、时间步相对化，提供时间无关的输入。策略网络输出高斯分布的均值（推理时取均值）和值估计。
        4. **规则增强选择器（仅推理时）**：结合模式选择器得分与基于安全、舒适、进展等规则的分数，选出最优轨迹。
    - **一致性建模**：模式c在整个轨迹生成中保持不变（式4），避免了传统自回归中因随机采样导致的时间步不一致，缩小了RL探索空间。
    - **奖励函数**：通用型，包含**专家引导项**（ego轨迹与真实轨迹的位移误差DE）和**任务导向项**（碰撞或驶离可行驶区域奖励为-1，否则0）。
    - **训练细节**：先预训练非反应式转移模型并冻结；模式分配采用**胜者全得**策略，根据真实轨迹为每个样本动态分配正模式；使用PPO算法训练生成器和选择器；引入模式丢弃（mode dropout）防止过拟合。
- **公式说明（文字）**：将轨迹规划建模为MDP，动作定义为下一时刻的ego位姿。通过引入模式c，将状态序列概率分解为积分形式，实现了模式选择与条件生成解耦。

#### 3. 实验设计
- **数据集**：**nuPlan**（超过1500小时、4个城市的真实驾驶数据，包含多种复杂场景）。
- **Benchmark**：
    - **Test14-Random**（261个场景，由PlanTF提供）
    - **Reduced-Val14**（318个场景，由PDM提供）
- **评价指标**：**封闭环分数（CLS）**，细分为**CLS-NR**（非反应性交通代理）和**CLS-R**（反应性交通代理），并包含安全（S-CR, S-TTC）、可行驶区域（S-Area）、进展（S-PR）、舒适性等子指标。
- **对比方法**：
    - **规则方法**：IDM, PDM-Closed
    - **IL方法**：RasterModel, UrbanDriver, GC-PGP, PDM-Open, GameFormer, PlanTF, PEP, PLUTO
    - **RL方法**：Gen-Drive（预训练+微调）
- **结果**：
    - 在Test14-Random非反应性设置中，CarPlanner的CLS-NR=94.07，超越PDM-Closed（90.05）和PLUTO（91.92）。
    - 在Reduced-Val14非反应性设置中，CLS-NR=91.45，进展S-PR=95.37，显著优于PDM-Closed（92.68）和Gen-Drive（89.94）。
    - 反应性设置中略逊于PDM-Closed（91.1 vs 91.64），原因在于模型仅在非反应性环境中训练。

#### 4. 资源与算力
- 文中明确提及：使用 **2块NVIDIA 3090 GPU**，batch size为64 per GPU，训练**50个epochs**。优化器为AdamW（初始学习率1e-4，带衰减策略）。
- **未明确说明**训练总时长，但指出其训练时间成本与IL方法相当（得益于模型基方法在GPU上高效运行）。

#### 5. 实验数量与充分性
- **实验数量**：
    - 主实验2个benchmark（Tab1, Tab2），对比12种以上方法。
    - 消融实验3组（Tab3：奖励项、IVM的坐标变换与KNN；Tab4：IL与RL中模式丢弃、侧任务、历史丢弃、骨干共享等设计的对比）。
    - 定性案例1个（行人场景对比PDM-Closed和IL/RL变体）。
- **充分性评价**：实验设计较为全面，覆盖了多种SOTA方法，并进行了细致的消融分析。消融实验不仅验证了RL各组件的有效性，还揭示了IL与RL在设计偏好上的差异（如历史丢弃对RL有害、骨干共享不利于RL）。**不足**：仅在nuPlan上评估，未在其他数据集（如Waymo）上验证泛化性，可能存在过拟合风险。此外，反应性场景结果较弱，但文中给出了合理原因。

#### 6. 主要结论与发现
- RL-based规划器首次在nuPlan大规模数据集上超越所有IL和规则SOTA，证明了RL在复杂真实场景中的潜力。
- 一致自回归结构有效解决了多模态轨迹生成中的时间不一致问题，提升了训练效率和策略稳定性。
- RL自然缓解了IL中的因果混淆问题（通过奖励信号而非历史掩码），而历史掩码在RL中反而有害。
- 专家引导的奖励结合质量奖励（碰撞/区域）可平衡安全与进展，IVM显著提升泛化性能。
- 骨干共享策略在IL中有益，但在RL中因梯度冲突会降低性能。

#### 7. 优点
- **方法创新**：首次提出一致自回归结构用于RL轨迹规划，创新性地将模式信息作为条件保持时间一致性。
- **训练高效**：模型基方法（非反应式转移模型）使得RL训练可充分利用GPU并行加速，时间成本与IL相当。
- **通用性**：设计的奖励函数无需特定场景设计，IVM使得输入时间无关，提升了泛化能力。
- **实验充分**：在多个维度进行消融，且对比了RL与IL的设计差异，提供了宝贵经验。
- **性能优越**：在非反应性场景中大幅领先，进展和安全指标均优异。

#### 8. 不足与局限
- **实验覆盖有限**：仅在nuPlan上验证，未在Waymo等大规模数据集上测试，泛化性存疑。
- **反应性场景表现**：在反应性交通代理环境中略逊于PDM-Closed，未进行混合环境训练，可能对真实动态场景鲁棒性不足。
- **依赖专家引导**：奖励函数包含位移误差项，可能限制RL探索超越人类驾驶的策略，未能充分释放RL的潜力。
- **过拟合风险**：RL易过拟合训练环境，文中也指出未来需要开发更鲁棒的算法以应对未见场景。
- **算力细节不完整**：未报告训练总耗时，影响复现和效率比较。
- **框架复杂性**：需要多阶段训练（先训练转移模型，再训练策略），且需要设计纵向/横向模式数量等超参数。

（完）
