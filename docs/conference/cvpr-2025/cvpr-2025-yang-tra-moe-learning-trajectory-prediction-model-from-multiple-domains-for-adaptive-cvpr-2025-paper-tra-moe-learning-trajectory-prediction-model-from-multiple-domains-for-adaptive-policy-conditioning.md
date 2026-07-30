---
title: "Tra-MoE: Learning Trajectory Prediction Model from Multiple Domains for Adaptive Policy Conditioning"
title_zh: Tra-MoE：从多域学习轨迹预测模型实现自适应策略调节
authors: "Yang, Jiange, Zhu, Haoyi, Wang, Yating, Wu, Gangshan, He, Tong, Wang, Limin"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Yang_Tra-MoE_Learning_Trajectory_Prediction_Model_from_Multiple_Domains_for_Adaptive_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 4.0
evidence: 使用MoE进行多域轨迹预测，可应用于自动驾驶场景
tldr: 机器人系统的轨迹预测常受限于单一域数据，泛化能力不足。本文提出Tra-MoE，采用稀疏门控专家混合（Top-1）架构，从多域数据学习轨迹预测模型。该模型能预测指令驱动的任意点轨迹，为策略学习提供详细控制指导。实验表明在多个跨域任务上泛化性能提升。该方法可扩展至自动驾驶中的轨迹预测。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yang-tra-moe-learning-trajectory-prediction-model-from-multiple-domains-for-adaptive-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 696, \"height\": 615, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yang-tra-moe-learning-trajectory-prediction-model-from-multiple-domains-for-adaptive-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 851, \"height\": 492, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yang-tra-moe-learning-trajectory-prediction-model-from-multiple-domains-for-adaptive-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1522, \"height\": 940, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yang-tra-moe-learning-trajectory-prediction-model-from-multiple-domains-for-adaptive-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1513, \"height\": 578, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yang-tra-moe-learning-trajectory-prediction-model-from-multiple-domains-for-adaptive-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 774, \"height\": 263, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yang-tra-moe-learning-trajectory-prediction-model-from-multiple-domains-for-adaptive-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 797, \"height\": 260, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yang-tra-moe-learning-trajectory-prediction-model-from-multiple-domains-for-adaptive-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 789, \"height\": 216, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yang-tra-moe-learning-trajectory-prediction-model-from-multiple-domains-for-adaptive-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 880, \"height\": 257, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yang-tra-moe-learning-trajectory-prediction-model-from-multiple-domains-for-adaptive-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 831, \"height\": 177, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yang-tra-moe-learning-trajectory-prediction-model-from-multiple-domains-for-adaptive-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 783, \"height\": 221, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yang-tra-moe-learning-trajectory-prediction-model-from-multiple-domains-for-adaptive-cvpr-2025-paper/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1653, \"height\": 258, \"label\": \"Table\"}]"
motivation: 单域训练的轨迹预测模型泛化能力差，难以适应多样化的驾驶场景。
method: 使用稀疏门控MoE（Top-1策略）架构处理多域数据分布，实现参数合作与特化的平衡。
result: 在多个跨域数据集上，Tra-MoE的轨迹预测精度和泛化性均优于单域模型。
conclusion: 多域学习结合MoE能有效提升轨迹预测模型的适应能力。
---

## Abstract
Learning from multiple domains is a primary factor that influences the generalization of a single unified robot system. In this paper, we aim to learn the trajectory prediction model by using broad out-of-domain data to improve its performance and generalization ability. Trajectory model is designed to predict any-point trajectories in the current frame given an instruction and can provide detailed control guidance for robotic policy learning. To handle the diverse out-of-domain data distribution, we propose a sparsely-gated MoE (Top-1 gating strategy) architecture for trajectory model, coined as Tra-MoE. The sparse activation design enables good balance between parameter cooperation and specialization, effectively benefiting from large-scale out-of-domain data while maintaining constant FLOPs per token. In addition, we further introduce an adaptive policy conditioning technique by learning 2D mask representations for predicted trajectories, which is explicitly aligned with image observations to guide action prediction more flexibly. We perform extensive experiments on both simulation and real-world scenarios to verify the effectiveness of Tra-MoE and adaptive policy conditioning technique. We also conduct a comprehensive empirical study to train Tra-MoE, demonstrating that our Tra-MoE consistently exhibits superior performance compared to the dense baseline model, even when the latter is scaled to match Tra-MoE's parameter count.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义（研究动机与背景）
- **研究动机**：在机器人学习中，轨迹预测模型通常仅使用单一领域（in-domain）的数据进行训练，导致其在新环境、新物体、新技能或新形态（embodiment）数据上泛化能力不足。虽然大规模、跨域（out-of-domain）视频数据（如人类操作视频、不同物理引擎的仿真数据）具有丰富信息，但直接与域内数据混合训练会导致优化冲突，甚至造成域内性能下降（图1显示性能从57.6%降至52.0%）。
- **核心目标**：设计一个能够从多域数据中有效学习，并在域内任务上保持甚至提升性能的轨迹预测模型，同时保持计算高效性，并改善策略调节（policy conditioning）方式。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：采用稀疏门控混合专家（Sparsely-gated Mixture-of-Experts, MoE）架构扩展轨迹预测模型，实现参数合作与特化的平衡；并设计自适应的策略调节技术，将2D轨迹显式对齐到图像观测空间。
- **关键技术细节**：
  - **Tra-MoE 架构**：在原始 Transformer 中替换部分前馈网络（FFN）为 MoE 块，每个 MoE 块包含多个专家（Expert），采用 Top-1 门控策略（Top-1 gating）激活最相关的专家，使得每个 token 的计算量（FLOPs）与基线模型保持一致，从而在模型容量扩大的同时维持计算效率。
  - **门控网络**：门控函数 G(x;Θ) 通过线性-softmax 网络对 token 序列 x 进行评分，仅保留 top-1 专家对应的 logit，其余置为 -∞，保证稀疏激活。
  - **辅助损失**：使用 router z-loss 提高训练稳定性，并尝试负载平衡损失（load-balancing loss）和门控噪声，但实验发现仅 z-loss 有效，负载平衡和噪声反而导致性能下降。
  - **自适应策略调节技术**：构造一个额外的 2D 轨迹掩膜（mask）模态，将预测的轨迹点（起点、终点等）以可学习嵌入的形式填充到该掩膜中，然后沿通道维度与图像观测拼接（得到 H×W×4 张量），实现 2D 轨迹与图像的空间显式对齐，使策略模型能更灵活地捕捉轨迹特征（起点侧重局部运动，终点侧重全局趋势）。
- **算法流程**：两阶段训练——阶段一：联合使用域内（小规模、含动作标签）和域外（大规模、无动作标签）视频数据预训练 Tra-MoE 轨迹模型；阶段二：冻结轨迹模型，仅使用域内含动作标签的演示数据训练轨迹引导策略（行为克隆，MSE 损失）。

## 3. 实验设计
- **数据集/场景**：
  - **仿真环境**：LIBERO 基准（分为 Spatial、Object、Goal、Long 以及 LIBERO-90 共 5 个子集）。域内数据 Din 从 4 个子集（各 10 任务）中选择 40 个任务，每个任务 10 条带动作标签演示；域外数据 Dood 从 LIBERO-90 中选择 90 个任务，每个任务 20 条无动作视频。此外还引入 RLBench（CoppeliaSim 物理引擎）数据，92 个任务各 5 个视频，进一步扩大域差异。
  - **真实世界**：使用低成本双臂机器人评估 5 个任务（单臂：倒水、推蔬菜；双臂：抽纸巾、叠毛巾、抓取并传递物体），每个任务收集 50 条机器人演示和 50 条人类操作视频（跨形态）。
- **基准方法**：以 ATM（Any-point Trajectory Modeling）为基线稠密模型，对比 Tra-MoE 以及将稠密模型按宽度或深度扩展至相同参数量的变体。
- **对比方法**：对比是否使用 MoE、是否使用域外数据、是否使用自适应掩膜等消融实验；在策略调节部分对比“手绘掩膜”（类似 RT-Trajectory）和“自适应掩膜”。
- **评价指标**：下游操纵任务的平均成功率（Average Success Rate），因为论文指出成功率和轨迹预测质量正相关。

## 4. 资源与算力
- **文中未明确说明**使用的 GPU 型号、数量及训练时长。仅在实现细节中提到基于 ATM 构建模型，未提供具体硬件规格或训练时间。

## 5. 实验数量与充分性
- **实验组数**：包含了大量的消融实验和对比实验，具体如下：
  - 仿真实验表1包含 7 个分表：a) 路由器 z-loss 权重 λz 的 5 种取值；b) 负载平衡损失权重 λlo-ba 的 4 种取值；c) 门控噪声开/关；d) 稠密模型按宽度/深度扩展至同等参数量；e) 不同专家数量（1,2,3,4）；f) MoE 与域外数据的联合消融（4 种设置）；g) 引入 RLBench 域外数据后的对比（2 行）。
  - 仿真实验表2 比较 ATM 与 Tra-MoE 在 RLBench 数据下的表现。
  - 仿真实验表3 消融策略调节技术：基线（ATM）、+手绘掩膜、+自适应掩膜共3种设置。
  - 真实世界实验表4 消融人类数据、MoE、自适应掩膜的 4 种组合。
- **充分性与公平性**：实验设计较为全面，覆盖了关键超参数、架构选择、数据规模、域外数据引入方式以及策略端改进。所有对比均在相同数据划分和训练设置下进行，并报告了每个子类的平均成功率，结论有统计支持。但未提供多次运行的标准差或置信区间，对于随机性影响的评估稍显不足。

## 6. 主要结论与发现
- **结论 1**：稀疏门控 MoE（Top-1）能有效利用大规模域外数据，在域内任务上实现性能提升（从 51.8% 增至 61.4%），而稠密模型在同样条件下性能下降（57.6% → 52.0%）。
- **结论 2**：路由器 z-loss 对训练稳定性和性能有积极影响（λz=1e-4 时最佳），而负载平衡损失和门控噪声会损害性能（因为强制平衡破坏专家特化）。
- **结论 3**：即使是少量专家（如 2 个）也能带来显著提升，更多专家（4 个）通常进一步改善但波动存在。
- **结论 4**：将稠密基线扩展至与 Tra-MoE 同等参数量（宽度或深度扩增）仍无法超越 Tra-MoE，证明稀疏 MoE 结构在处理多域数据时优势明显。
- **结论 5**：自适应策略调节技术（2D 可学习轨迹掩膜）优于手绘掩膜，在所有子类上均提升性能，尤其对 LIBERO-Goal 改善最大（从 58.0% 到 77.0%）。
- **结论 6**：真实世界实验验证了 MoE 和自适应掩膜的组合效果：单独引入人类数据无收益，+MoE 后成功率从 38% 提升至 46%，再加上自适应掩膜达到 56%。

## 7. 优点
- **方法创新**：首次将稀疏 MoE 引入轨迹预测任务，天然地实现多域数据中的参数特化与合作，有效缓解域间冲突。
- **计算高效**：Top-1 门控确保每个 token 计算量与稠密基线相同，实现模型容量扩大而不增加推理 FLOPs。
- **策略调节改进**：自适应 2D 掩膜简单有效，将轨迹与图像在空间上显式对齐，且通过学习区分轨迹点的不同角色，提升了策略的学习效率。
- **消融实验充分**：对关键设计（专家数、辅助损失权重、数据扩展、策略调节方式）逐一进行了系统消融，结论清晰。
- **跨域验证**：从仿真 LIBERO、RLBench 到真实机器人，从同形态到跨形态数据，验证了方法通用性。

## 8. 不足与局限
- **实验覆盖**：仅使用了 LIBERO 和 RLBench 两个仿真平台及一组真实场景，未在更广泛的机器人 benchmark（如 MetaWorld、Franka Kitchen 等）上测试，泛化性有待进一步验证。
- **偏差风险**：域外数据的选择可能影响结果——域外数据与域内数据有较大分布重叠时，MoE 的优势可能缩小。论文未分析不同域间差异程度对性能的影响。
- **统计分析缺失**：未报告多次独立实验的均值和方差，当前结果可能受随机初始化影响，缺少显著性检验。
- **计算资源未公开**：论文未提供训练模型所需的 GPU 型号、数量及时间，不利于其他研究者复现或评估资源成本。
- **策略训练方式**：轨迹引导策略仅采用行为克隆（MSE loss），未探索更先进的方法（如扩散策略、隐式动作模型），可能限制了性能上限。
- **真实任务规模**：真实世界仅 5 个任务，每个任务 50 条演示，规模较小，实验结果的可推广性有限。

（完）
