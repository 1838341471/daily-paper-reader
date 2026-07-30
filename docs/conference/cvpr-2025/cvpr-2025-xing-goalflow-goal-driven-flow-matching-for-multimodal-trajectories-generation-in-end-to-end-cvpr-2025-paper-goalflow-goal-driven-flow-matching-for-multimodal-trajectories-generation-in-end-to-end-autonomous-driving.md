---
title: "GoalFlow: Goal-Driven Flow Matching for Multimodal Trajectories Generation in End-to-End Autonomous Driving"
title_zh: GoalFlow：面向端到端自动驾驶多模态轨迹生成的目标驱动流匹配
authors: "Xing, Zebin, Zhang, Xingyu, Hu, Yang, Jiang, Bo, He, Tong, Zhang, Qian, Long, Xiaoxiao, Yin, Wei"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Xing_GoalFlow_Goal-Driven_Flow_Matching_for_Multimodal_Trajectories_Generation_in_End-to-End_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 9.0
evidence: 端到端自动驾驶中多模态轨迹生成
tldr: 端到端自动驾驶中多模态轨迹生成面临轨迹发散和场景指引不一致的问题。本文提出GoalFlow，采用目标驱动的流匹配方法，有效约束生成过程产生高质量多模态轨迹。通过引入目标引导，解决了扩散方法中的轨迹发散问题。在多个数据集上展示了生成轨迹的质量和多样性，提升了端到端驾驶的轨迹生成能力。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xing-goalflow-goal-driven-flow-matching-for-multimodal-trajectories-generation-in-end-to-end-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 835, \"height\": 666, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xing-goalflow-goal-driven-flow-matching-for-multimodal-trajectories-generation-in-end-to-end-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1794, \"height\": 683, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xing-goalflow-goal-driven-flow-matching-for-multimodal-trajectories-generation-in-end-to-end-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1775, \"height\": 707, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-xing-goalflow-goal-driven-flow-matching-for-multimodal-trajectories-generation-in-end-to-end-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 902, \"height\": 507, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xing-goalflow-goal-driven-flow-matching-for-multimodal-trajectories-generation-in-end-to-end-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1801, \"height\": 517, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xing-goalflow-goal-driven-flow-matching-for-multimodal-trajectories-generation-in-end-to-end-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1496, \"height\": 342, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xing-goalflow-goal-driven-flow-matching-for-multimodal-trajectories-generation-in-end-to-end-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 862, \"height\": 198, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xing-goalflow-goal-driven-flow-matching-for-multimodal-trajectories-generation-in-end-to-end-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 861, \"height\": 232, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-xing-goalflow-goal-driven-flow-matching-for-multimodal-trajectories-generation-in-end-to-end-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 865, \"height\": 265, \"label\": \"Table\"}]"
motivation: 现有扩散方法生成多模态轨迹时存在轨迹发散和质量下降问题。
method: 提出目标驱动流匹配方法，用目标约束生成过程。
result: 生成轨迹质量高且多样，优于现有扩散方法。
conclusion: GoalFlow为端到端自动驾驶提供了一种高质量多模态轨迹生成方案。
---

## Abstract
We propose GoalFlow, an end-to-end autonomous driving method for generating high-quality multimodal trajectories. In autonomous driving scenarios, there is rarely a single suitable trajectory. Recent methods have increasingly focused on modeling multimodal trajectory distributions. However, they suffer from trajectory selection complexity and reduced trajectory quality due to high trajectory divergence and inconsistencies between guidance and scene information. To address these issues, we introduce GoalFlow, a novel method that effectively constrains the generative process to produce high-quality, multimodal trajectories. To resolve the trajectory divergence problem inherent in diffusion-based methods, GoalFlow constrains the generated trajectories by introducing a goal point. GoalFlow establishes a novel scoring mechanism that selects the most appropriate goal point from the candidate points based on scene information. Furthermore, GoalFlow employs an efficient generative method, Flow Matching, to generate multimodal trajectories, and incorporates a refined scoring mechanism to select the optimal trajectory from the candidates. Our experimental results, validated on the Navsim, demonstrate that GoalFlow achieves state-of-the-art performance, delivering robust multimodal trajectories for autonomous driving. GoalFlow achieved PDMS of 90.3, significantly surpassing other methods. Compared with other diffusion-policy-based methods, our approach requires only a single denoising step to obtain excellent performance. The code is available at https://github.com/YvanYin/GoalFlow.

---

## 论文详细总结（自动生成）

# GoalFlow 论文详细总结

## 1. 核心问题与整体含义（研究动机和背景）
- **研究动机**：在端到端自动驾驶中，单一真值轨迹不足以覆盖复杂场景中的多模态行为，因此需要生成高质量的多模态轨迹候选。现有方法主要分为两类：一是基于离散命令或预定义目标点引导的回归模型，当引导信息与真值偏差较大时会产生低质轨迹；二是基于扩散模型的生成方法，虽然能建模多模态分布，但存在严重的轨迹发散问题，且需要较多推断步数，难以满足实时要求。
- **核心问题**：如何在端到端环境中高效生成高保真、可驾驶的多模态轨迹，同时确保轨迹受约束（不偏离可行驶区域）且多样性充分。
- **整体含义**：本文提出 GoalFlow，通过引入“目标点（goal point）”对生成过程施加强约束，采用 Flow Matching（具体为 Rectified Flow）实现单步或少步高效生成，同时以场景信息驱动目标点选择，最终生成并选优高质量多模态轨迹。

## 2. 方法论
### 2.1 核心思想
将传统“直接生成整条轨迹”的任务分解为两个子任务：
1. **目标点预测**：从离散的目标点词汇表中，基于场景信息选择最合适的未来位置（位置+朝向）。
2. **目标引导轨迹生成**：以选定目标点为强条件，利用 Flow Matching 将噪声分布映射到轨迹分布，生成候选轨迹。
这种分解有效缓解了轨迹发散，并提升了轨迹对可行驶区域的服从性。

### 2.2 关键技术细节
- **感知模块**：采用 TransFuser 架构，融合多视角图像（拼接为 I ∈ R³×H₁×W₁）和 LiDAR 点云（L ∈ Rᴷˣ³），通过多层 Transformer 融合得到 BEV 特征 F_bev，并添加 HD map 和 3D 检测辅助损失。
- **目标点构建模块**：
  - **目标点词汇表 V**：对训练数据中轨迹的终点（位置 x,y 和朝向 θ）进行聚类，生成 N 个聚类中心（通常 N=4096 或 8192）。
  - **目标点评分器**：对每个候选目标点 gi，计算两个分数：
    - 距离分数 δ_dis^hat：基于 softmax 归一化的欧氏距离，衡量与真值终点的接近度。
    - 可行驶区域合规分数 δ_dac^hat：二元值，判断放置假想车辆（shadow vehicle）后四个角是否都在可行驶区域内。
    - 最终分数 = w₁ log δ_dis^hat + w₂ log δ_dac^hat（文中 w₁、w₂ 未给定具体值，但训练损失设置 w₄=1.0, w₅=0.005，可类比）。
  - **网络结构**：Transformer-based Scorer Decoder，以 F_v（词汇编码）+ F_ego 为 query，F_bev 为 key/value，输出两个 MLP 头的分数分布。
- **轨迹规划模块**：
  - **生成模型**：采用 Rectified Flow（Flow Matching 的特例），定义从噪声 x₀~N(0, σ²I) 到归一化真值轨迹 τ_norm 的线性路径 x_t = (1-t)x₀ + tτ_norm，网络 v_θ 预测方向 (τ_norm - x₀)。条件包括：BEV 特征、目标点、时间步、当前噪声轨迹。
  - **推理**：多步（亦可单步）沿 v_θ 方向积分得到 τ_norm，经反归一化得最终轨迹 τ̂。
  - **轨迹选择**：使用一个轻量轨迹评分器，权衡轨迹终点与目标点的 L2 距离和轨迹进度（progress），公式 f(τ̂_i) = -λ₁ Φ(f_dis(τ̂_i)) + λ₂ Φ(f_pg(τ̂_i))，其中 Φ 为 min-max 归一化。另引入“影子轨迹”（无目标点引导的生成），若与主轨迹偏差大则使用影子轨迹以缓解目标点误差。
- **训练损失**：
  - 感知损失 L_perception = w₁ L_HD + w₂ L_bbox + w₃ L_loc（w₁=10, w₂=1, w₃=10）
  - 目标点损失 L_goal = w₄ L_dis + w₅ L_dac（w₄=1, w₅=0.005），其中 L_dis 为交叉熵，L_dac 为二分类交叉熵。
  - 规划损失 L_planner = L1(v_t - v̂_t)

## 3. 实验设计
### 3.1 数据集与 benchmark
- **数据集**：OpenScene 数据集（120 小时自动驾驶数据），其端到端仿真环境 **Navsim** 用于评估，包含 trainval 1192 个场景、test 136 个场景，总计超过 10 万样本（2Hz 采样）。每个样本包含 8 个视角的相机图像、5 个 LiDAR 融合数据、自车状态、地图和物体标注。
- **benchmark 指标**（PDM-score 框架）：
  - SNC（无责任碰撞率）、SDAC（可行驶区域合规率）、STTC（碰撞时间达标率）、SCF（舒适性）、SEP（自车进度）
  - 总分 SPDM = SNC × SDAC × STTC × (5×SEP + 5×SCF + 2×SDDC)/12，实际中 SDDC 被省略。
- **对比方法**：Constant Velocity、Ego Status MLP、LTF、TransFuser、UniAD、PARA-Drive 等 SOTA 端到端方法。

### 3.2 对比结果
- GoalFlow 在 Navsim test 上取得 SPDM=90.3，显著高于第二名 TransFuser（84.0）。尤其在 SDAC（98.3 vs 92.8）和 SEP（85.0 vs 79.2）上提升明显。
- 若使用真值终点代替预测目标点（GoalFlow†），SPDM 提升至 92.1，接近人类表现 94.8。

## 4. 资源与算力
文中明确提及：“All training was conducted on 4 nodes, each equipped with 8 RTX 4090 or RTX 3090 GPUs.” 即使用了 **4 个节点，每节点 8 块 GPU（RTX 4090 或 RTX 3090），共 32 块 GPU**。未说明具体的训练时长（如小时数或迭代次数）。

## 5. 实验数量与充分性
论文包含四组主要实验：
- **表 1**：与 6 种基线方法的 SOTA 对比，涵盖不同传感器输入和架构，结果客观。
- **表 2**：消融实验，从 M0（仅 Rectified Flow，无目标引导）逐步加入距离评分、DAC 评分、轨迹评分器，清晰验证各模块贡献。
- **表 3**：不同推断步数（1, 5, 10, 20）的影响，显示单步仍保持高性能（SPDM 88.9 vs 90.3），体现效率优势。
- **表 4**：不同初始噪声方差 σ 的影响，说明 σ 需谨慎选择（≤0.1 稳定，过大导致质量崩溃）。
- **表 5**：模型缩放实验，改变 Transformer 隐藏维度和图像骨干（ResNet-34 vs V2-99），发现增大维度/模型提升性能。

**充分性评价**：实验设计比较全面，覆盖了消融、超参数敏感性、效率分析和模型复杂度。但仅在一个数据集（Navsim）上验证，缺乏跨数据集（如 nuScenes 或 Waymo）的泛化实验。未报告多次运行的标准差，可能统计稳定性不足。

## 6. 主要结论与发现
1. **目标点引导显著提升轨迹质量**：分解“选目标+生成”两步，比直接生成更可靠。
2. **Flow Matching 优于扩散模型**：仅需 1-5 步推理即可达到甚至超过其他扩散方法（如 Diffusion-ES），适合实时自动驾驶。
3. **可行驶区域合规建模有效**：DAC 评分引入假想车辆检测，使 SDAC 指标大幅领先。
4. **遮挡/误差处理**：影子轨迹机制可缓解目标点预测错误，增强鲁棒性。
5. **整体性能**：在 Navsim 上达到 SOTA，SPDM=90.3，接近人类水平。

## 7. 优点
- **方法创新**：首次将 Flow Matching 与端到端自动驾驶中的目标点引导结合，解决轨迹发散问题。
- **效率突出**：支持单步生成，推理时间仅约 10ms，显著优于传统扩散模型（需多步迭代）。
- **分解策略合理**：将复杂规划任务拆解为更易学习的目标预测和条件生成，降低学习难度。
- **场景理解全面**：通过感知模块融合图像和 LiDAR，目标点评分同时考虑距离和可行驶区域，考虑实际安全。
- **实验设计严谨**：对每个设计组件进行消融，对关键超参数（步数、噪声方差）做敏感度分析，对模型规模做 scaling 实验。

## 8. 不足与局限
- **实验泛化性有限**：仅在一个仿真环境（Navsim）上测试，未验证在真实道路数据（如 nuScenes、Waymo）或其他仿真器中的表现。Navsim 本身基于 OpenScene 数据集，可能存在数据分布偏移。
- **未报告统计波动**：所有性能指标未提供标准差或多次重复结果，无法评估方法的稳定性。
- **目标点词汇表依赖**：聚类数量 N（4096/8192）需手动设定，过大或过小可能影响性能，且聚类可能受数据分布影响。
- **对比基线不完整**：缺少与近期端到端多模态方法（如 VADv2、SparseDrive、GenAD）的直接数值对比（尽管文献中提及 SparseDrive，但表 1 未列出它们的结果）。
- **目标点误差处理有限**：影子轨迹只能缓解极端情况，当目标点偏差但未触发影子条件时，仍可能生成不良轨迹。
- **计算开销**：训练使用 32 块高端 GPU，资源消耗较大，可能限制可复现性。
- **可解释性**：整体系统仍为黑箱，缺乏对极端场景下行为（如遮挡、混合交通流）的深入分析。

（完）
