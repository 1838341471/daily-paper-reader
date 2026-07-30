---
title: "SocialMOIF: Multi-Order Intention Fusion for Pedestrian Trajectory Prediction"
title_zh: SocialMOIF：面向行人轨迹预测的多阶意图融合
authors: "Chen, Kai, Zhao, Xiaodong, Huang, Yujie, Fang, Guoyu, Song, Xiao, Wang, Ruiping, Wang, Ziyuan"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_SocialMOIF_Multi-Order_Intention_Fusion_for_Pedestrian_Trajectory_Prediction_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 7.0
evidence: 行人轨迹预测中的意图融合
tldr: 行人轨迹预测面临意图不确定性及高阶社会交互建模难题。本文提出SocialMOIF，通过融合一阶和多阶意图交互来提升预测精度。模型有效捕捉群组内复杂影响，在ETH/UCY等数据集上取得最新最优结果。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-socialmoif-multi-order-intention-fusion-for-pedestrian-trajectory-prediction-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 822, \"height\": 711, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-socialmoif-multi-order-intention-fusion-for-pedestrian-trajectory-prediction-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1801, \"height\": 980, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-socialmoif-multi-order-intention-fusion-for-pedestrian-trajectory-prediction-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 859, \"height\": 778, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-socialmoif-multi-order-intention-fusion-for-pedestrian-trajectory-prediction-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1359, \"height\": 829, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-socialmoif-multi-order-intention-fusion-for-pedestrian-trajectory-prediction-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1425, \"height\": 621, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-socialmoif-multi-order-intention-fusion-for-pedestrian-trajectory-prediction-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 788, \"height\": 458, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-socialmoif-multi-order-intention-fusion-for-pedestrian-trajectory-prediction-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1813, \"height\": 501, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-socialmoif-multi-order-intention-fusion-for-pedestrian-trajectory-prediction-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1546, \"height\": 311, \"label\": \"Table\"}]"
motivation: 现有方法忽略高阶邻域意图交互，预测精度受限。
method: 构建多阶意图融合模块，同时强化一阶与高阶邻居的意图影响。
result: 在公开行人轨迹数据集上达到最优性能。
conclusion: 多阶意图融合能有效捕捉群体交互，提升预测准确性。
---

## Abstract
The analysis and prediction of agent trajectories are crucial for decision-making processes in intelligent systems, with precise short-term trajectory forecasting being highly significant across a range of applications. Agents and their social interactions have been quantified and modeled by researchers from various perspectives; however, substantial limitations exist in the current work due to the inherent high uncertainty of agent intentions and the complex higher-order influences among neighboring groups. SocialMOIF is proposed to tackle these challenges, concentrating on the higher-order intention interactions among neighboring groups while reinforcing the primary role of first-order intention interactions between neighbors and the target agent. This method develops a multi-order intention fusion model to achieve a more comprehensive understanding of both direct and indirect intention information. Within SocialMOIF, a trajectory distribution approximator is designed to guide the trajectories toward values that align more closely with the actual data, thereby enhancing model interpretability. Furthermore, a global trajectory optimizer is introduced to enable more accurate and efficient parallel predictions. By incorporating a novel loss function that accounts for distance and direction during training, experimental results demonstrate that the model outperforms previous state-of-the-art baselines across multiple metrics in both dynamic and static datasets.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：行人轨迹预测中，现有方法主要关注目标智能体与邻居之间的直接（一阶）交互，忽略了邻居群组内部复杂的高阶意图传播对目标智能体的间接影响；同时，未来轨迹信息的利用缺乏显式指导，导致可解释性差；此外，多数方法在解码阶段顺序生成轨迹，误差累积且效率低下。
- **整体含义**：为解决上述问题，该文提出**SocialMOIF**框架，通过**多阶意图融合**、**轨迹分布逼近**、**全局轨迹优化**和**方向-距离融合损失**四个关键设计，更全面地捕捉社会交互中的直接与间接意图，提升预测精度和可解释性，并实现高效的并行预测。

## 2. 论文提出的方法论

- **核心思想**：将邻居对目标智能体的意图影响分解为**一阶（直接）** 和**高阶（间接）** 两部分，通过融合两者获得综合意图表示；利用先验（历史意图）和后验（未来真实轨迹）指导隐变量分布；引入KANs进行全局并行优化；设计同时考虑距离和方向的新损失函数。
- **关键技术细节**：
  - **多阶意图融合模型（MOIF）**：  
    - 高阶层：通过多头自注意力机制计算邻居之间的意图系数矩阵 \(W^{m}_{U}\)，捕获群组内部交互。  
    - 一阶层：计算目标与邻居之间的意图系数矩阵 \(W_{S}\)，强调直接主导影响。  
    - 融合：\(A_i = \sum_{m=1}^{M} \eta_m W^{m}_{U} + W_S\)，并通过跳跃连接和全连接层得到融合意图 \(I_i\)。
  - **轨迹分布逼近器**：借鉴夹逼定理，将历史意图 \(I_i\) 作为下界，未来真实轨迹特征 \(B_i\) 作为上界，显式近似隐变量分布 \(z^{t}_{i\phi} \sim \mathcal{N}(u^{t}_{i\phi}, \sigma^{t}_{i\phi})\)，并在训练中通过RNN更新 \(I_i\)，实现显式监督。
  - **全局轨迹优化器**：首次引入KANs（Kolmogorov-Arnold Networks），将解码出的轨迹沿时间维度聚合为 \(\Gamma^0 \in \mathbb{R}^{2T_F}\)，通过多层KAN进行全局非线性变换，一次输出完整预测轨迹，实现并行优化。
  - **损失函数**：融合距离损失 \(L_{dis}\) 和方向损失 \(L_{angle}\)（预测方向向量与真实方向向量的夹角），并加入KL散度项约束隐变量分布；最终损失形式为：

\[
\mathcal{L} = \sum_{t} \left[ \mathbb{E}_{z^{t}_{i\phi}\sim q_\phi(\cdot|B_i,I^{t-1}_i)} (L_{dis}+L_{angle}) - \text{KL}(q_\phi\|q_\vartheta) \right]
\]

## 3. 实验设计

- **数据集与场景**：使用了五个主流数据集：
  - **ETH/UCY**：约1600条行人轨迹，0.4s间隔标注。
  - **SDD**（Stanford Drone Dataset）：约19000条行人轨迹。
  - **NBA**：2015-2016赛季篮球运动员轨迹，分为“Rebounds”和“Scores”子集，交互复杂。
  - **NuScenes**：自动驾驶多模态数据集，遵循预测挑战分割。
- **Benchmark**：采用**ADE（平均位移误差）**和**FDE（最终位移误差）**作为主要指标，最佳20个预测中选取最优（best-of-20）。
- **对比方法**：包括FLEAM、ST-MR、MTN、MANTRA、Agent-former、BiTrap、MemoNet、EqMotion、V2-Net-SC、E-V2-Net-SC、GroupNet+CVAE、SHENet、MID、Y-Net、NSP-SFM等SOTA模型。

## 4. 资源与算力

- 文中明确提到：“The model was trained on two NVIDIA RTX 4090 GPUs.”  
- 未提及训练时长、总epoch数或模型参数量等具体算力消耗细节。

## 5. 实验数量与充分性

- **实验组数**：
  - 在ETH/UCY、NBA、SDD、NuScenes四个数据集上进行定量比较（表1），共覆盖11个场景（ETH/UCY的5个子场景、NBA的2个子集、SDD、NuScenes）。
  - **消融实验**（表2）：在SDD和NuScenes上设置了7组实验，依次添加：P、V、D、Θ、E、I、B、K、A等组件，验证每个模块的贡献。
  - **定性分析**：展示了多组可视化案例（图3-6），包括历史复杂轨迹、状态保持、多邻居等场景，并与前三方法对比预测分布热力图。
  - 还进行了NLL指标的补充实验及方向损失在其他模型上的迁移验证（见补充材料）。
- **充分性评估**：
  - 数据集多样性高（静态/动态、密集/稀疏、行人/篮球/车辆）；
  - 消融实验逐步添加组件，清晰验证了每个关键设计的必要性；
  - 对比方法均为近年SOTA，实验结果统计可靠；
  - 实验覆盖全面，但缺乏对模型计算复杂度或推理速度的对比分析。

## 6. 论文的主要结论与发现

- SocialMOIF在**ETH/UCY、NBA、SDD、NuScenes**全部数据集上取得了**最优或仅次于最优**的结果：
  - ETH/UCY平均ADE/FDE从E-V2-Net-SC的0.15/0.20降至**0.13/0.18**（降低13.3%/10.0%）。
  - NBA Rebound子集ADE/FDE从0.54/0.79降至**0.34/0.66**（降低37.0%/16.5%）。
  - SDD上ADE/FDE从NSP-SFM的0.21/0.34降至**0.17/0.24**（降低19.0%/29.4%）。
  - NuScenes上ADE从1.04降至**0.92**，FDE略有提升。
- 消融实验表明：每个组件（高阶意图、分布逼近器、全局优化器、方向损失）均有正向贡献；其中全局优化器（KANs）显著降低累积误差。
- 可视化验证：多阶意图融合使模型在复杂社会场景下预测更准确；分布逼近器使预测分布更贴近真实分布，提高了可解释性。

## 7. 优点

- **方法创新性**：
  - 明确区分一阶与高阶意图，并提出融合方案，弥补了现有工作对高阶社会交互的忽视。
  - 首次将KANs用于轨迹全局优化，实现并行预测，避免顺序生成的误差累积。
  - 设计方向-距离融合损失，更全面监督智能体动态变化。
- **实验充分性**：
  - 在四个不同性质的数据集（行人、篮球、无人机、自动驾驶）上验证，泛化能力强。
  - 消融实验逐步添加组件，定量分析了每个模块的贡献。
  - 定性与定量结合，可视化结果清晰展示模型优势。
- **可解释性**：通过分布逼近器显式引导隐变量分布，避免了纯黑箱生成。

## 8. 不足与局限

- **未报告计算效率**：尽管提出了并行优化，但缺乏推理速度或参数量对比，难以评估实际部署成本。
- **数据集覆盖有限**：未在如Waymo、Argoverse等大规模自动驾驶数据集上验证，可能影响在车辆主导场景的适用性。
- **部分场景未达最优**：在ETH/UCY的Eth子场景中，E-V2-Net-SC表现更好（ADE 0.23 vs 0.26），说明模型在平行运动、弱交互场景下仍有提升空间。
- **高阶意图计算复杂度**：式(3)中的多头自注意力计算 \(O(M N_n^2 d)\)，当邻居数量很大时可能存在瓶颈，论文未讨论该问题。
- **异质智能体考虑不足**：仅针对行人/运动员，未涉及车辆、自行车等不同运动学约束的智能体，方法通用性有待进一步检验。
- **公平性风险**：未讨论模型在不同性别、年龄等群体上的表现偏差，但该问题在现有行人轨迹预测文献中也普遍未被关注。

（完）
