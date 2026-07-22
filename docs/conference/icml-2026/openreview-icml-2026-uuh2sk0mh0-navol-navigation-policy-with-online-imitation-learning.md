---
title: "NavOL: Navigation Policy with Online Imitation Learning"
title_zh: NavOL：基于在线模仿学习的导航策略
authors: "Xiaofei Wei, Chun Gu, Li Zhang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/c0087257172019e2ed8e011dffcb3ec2d79bcca9.pdf"
tags: ["query:av-pnc"]
score: 8.0
evidence: 在线模仿学习导航策略将观测映射到路径点，直接用于自动驾驶路径规划
tldr: 针对离线模仿学习在机器人导航中因分布偏移和复合误差导致性能下降的问题，本文提出NavOL在线模仿学习范式。NavOL在仿真器中交互运行，利用全局规划器提供的专家路径作为标签在线更新扩散导航策略，形成“执行-更新”循环。实验表明该方法显著提升了导航策略的鲁棒性和成功率，为机器人导航提供了一种高效的学习框架。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 离线模仿学习在导航任务中面临分布偏移和复合误差，导致策略性能不佳。
method: 提出NavOL，通过在线交互与仿真器，查询全局规划器获得最优路径段作为标签，迭代更新扩散策略。
result: 在导航任务中，NavOL相比离线方法显著提高成功率，有效缓解分布偏移问题。
conclusion: NavOL展示了在线模仿学习在导航策略学习中的有效性，可推广至其他机器人任务。
---

## Abstract
Learning robust navigation policies remains a core challenge in robotics. Offline imitation learning suffers from distribution shift and compounding errors at rollout, while reinforcement learning requires reward engineering and learns inefficiently. In this paper, we propose NavOL, an online imitation learning paradigm that interacts with a simulator and updates itself using expert demonstrations gathered online. Built upon a pretrained navigation diffusion policy that maps local observations to future waypoints, NavOL trains in a rollout–update loop: during rollout, the policy acts in the simulator and queries a global planner which has privileged access to the global environment for the optimal path segment as ground truth trajectory labels; during update, the policy is trained on the online collected observation–trajectory pairs. This online imitation loop removes the need for reward design, improves learning efficiency, and mitigates distribution shift by training on the policy’s own explored rollouts. Built on IsaacLab with fast, high-fidelity parallel rendering and domain randomization of camera pose and start-goal pairs, our system scales across 50 scenes on 8 RTX 4090 GPUs, collecting over 2,000 new trajectories per hour, each averaging more than 400 steps. We also introduce an indoor visual navigation benchmark with predefined start and goal positions for zero-shot generalization. Extensive evaluations on simulation benchmarks, including the NavDP benchmark and our proposed benchmark, as well as carefully designed real-world experiments, demonstrate the effectiveness of NavOL, showing consistent performance gains in online imitation learning.

---

## 论文详细总结（自动生成）

由于提供的 PDF 提取文本仅包含验证页面，未能获取论文正文。以下总结将基于给定的论文元数据（标题、摘要、元信息）进行整合，严格遵循要求的八个要点展开。

### 1. 论文的核心问题与整体含义
*   **核心问题**：在机器人导航任务中，离线模仿学习（Behavior Cloning）常因训练与测试时的分布偏移（distribution shift）和长序列推演时的复合误差（compounding errors）而导致性能崩溃；强化学习虽能自主探索，却需要精细的奖励函数设计（reward engineering）且样本效率低下。
*   **整体含义**：本文提出一种在线模仿学习范式 NavOL，旨在通过让策略在仿真器中在线交互，并实时获取专家最优轨迹作为标签来进行自更新，从而同时规避离线学习的分布偏移问题和强化学习的奖励设计难题，实现高效、鲁棒的视觉导航策略学习。

### 2. 论文提出的方法论
*   **核心思想**：NavOL 是一个“推演-更新”循环。策略在仿真器里运行时，就地查询一个拥有全局地图信息的特权规划器，获取当前时刻的最佳路径段作为真值，立即用于策略的在线监督学习，使训练数据始终匹配策略自身的状态分布。
*   **关键技术细节**：
    *   **基础策略**：采用预训练的扩散策略（diffusion policy），其功能是将局部观测（如深度图、里程计）映射为未来一系列的路径点（waypoints）。
    *   **在线推演**：策略在基于 IsaacLab 的并行高速渲染仿真器中执行导航任务。
    *   **专家标签获取**：在每一步，系统调用全局规划器（具有完整环境信息的特权专家）为当前位姿计算最优路径段，作为该观测的真值标签。
    *   **在线更新**：将在线收集的（局部观测，最优路径段）对实时加入训练集，对扩散策略进行持续微调。通过训练策略亲自探索产生的数据，直接从源头缓解分布偏移。
    *   **域随机化**：对相机安装姿态以及每次任务的起点-终点对进行广泛的域随机化，增强策略泛化性。

### 3. 实验设计
*   **使用的数据集/场景**：
    *   在 NVIDIA IsaacLab 仿真器中搭建，覆盖 50 个不同的室内场景。
    *   域随机化覆盖相机姿态和起点-终点对的多样性。
*   **Benchmark**：
    *   现有的 NavDP 导航基准（NavDP benchmark）。
    *   本文专门提出的室内视觉导航基准，其特点是预定义了严格的起点和终点位置，用于专门测试模型的零样本泛化（zero-shot generalization）能力。
*   **对比方法**：
    *   虽未在摘要中详尽列出，但核心对比基线应该是离线模仿学习的方法（如标准行为克隆）。文章旨在展示在线学习相对离线方法的稳步性能提升。

### 4. 资源与算力
*   **算力配置**：明确使用 8 张 NVIDIA RTX 4090 GPU 进行并行仿真渲染和策略更新。
*   **训练吞吐**：系统每小时可采集超过 2000 条新轨迹，且每条轨迹平均超过 400 步，表明其交互与更新循环具有极高的数据通量。
*   **训练时长**：未在元数据中明确说明总训练时长。

### 5. 实验数量与充分性
*   **实验规模**：从摘要推断，至少包含三组大规模评估：标准仿真基准（NavDP）、自定义强泛化基准以及真实世界实验。50 个场景的扩展、极高的数据收集速率，都表明实验具有一定的深度。
*   **充分性与客观性**：实验覆盖了仿真标准化比较、严苛的零样本泛化测试，并最终落地到真实世界，链条较为完整。通过在自有基准和开放基准上的共同验证，增强了结果的客观性和说服力。但摘要未详细介绍消融实验（如各部件的贡献度）、对比算法的具体数量及其调参公平性，这部分完整性无法从元数据确认。

### 6. 论文的主要结论与发现
*   NavOL 通过在线模仿学习管道，成功地在导航任务中提供了稳定的性能增益。
*   该方法有效缓解了离线模仿学习中固有的分布偏移和复合误差问题。
*   整个框架无需人工设计奖励函数，学习效率高，且具备在复杂仿真环境和真实世界中部署的潜力。

### 7. 优点
*   **范式创新**：将“在线交互并查询特权规划器”与模仿学习巧妙结合，实现无奖励的在线策略提升，思路简洁而有效。
*   **工程实现扎实**：基于 IsaacLab 的 8 卡并行渲染实现了极高的数据收集效率（每小时 2000+ 轨迹），支撑了在线学习的快速迭代。
*   **评估全面**：不仅涵盖了已有的 NavDP 基准，还自行构建了侧重泛化能力的基准，并最终进行真实世界验证，实用性强。

### 8. 不足与局限
*   **对特权专家的依赖**：在线更新强依赖于一个能够访问全局地图的规划器来提供最优路径标签，当无法获得此类完美专家（如未知的真实场景）时，方法如何适用未得到讨论。
*   **仿真与真实的迁移**：虽然在真实世界中做了验证，但训练过程完全依赖仿真交互，对于复杂动态环境及传感器噪声更极端的场景，其泛化极限未被深入探讨。
*   **方法单一性分析**：摘要未提及与在线强化学习方法的直接性能对比，无法量化在线模仿学习与在线强化学习在最终性能或样本效率上的具体差异。
*   **成本约束**：极高吞吐率（8卡4090）的在线训练范式，对单次部署的算力门槛和能耗成本提出了较高要求，限制了低资源研究者的复现与改进。

（完）
