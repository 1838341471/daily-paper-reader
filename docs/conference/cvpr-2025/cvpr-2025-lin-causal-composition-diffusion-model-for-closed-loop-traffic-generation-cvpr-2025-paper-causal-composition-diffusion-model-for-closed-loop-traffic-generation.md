---
title: Causal Composition Diffusion Model for Closed-loop Traffic Generation
title_zh: 因果组合扩散模型：用于闭环交通生成
authors: "Lin, Haohong, Huang, Xin, Phan, Tung, Hayden, David, Zhang, Huan, Zhao, Ding, Srinivasa, Siddhartha, Wolff, Eric, Chen, Hongge"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Lin_Causal_Composition_Diffusion_Model_for_Closed-loop_Traffic_Generation_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 6.0
evidence: 可控交通生成为规划提供测试场景
tldr: 自动驾驶仿真需要真实且可控的交通场景，但现有生成模型在安全关键场景中难以兼顾可控性和真实性。本文提出因果组合扩散模型CCDiff，将可控闭环仿真视为约束优化问题，使用结构引导扩散框架。在最大化可控性的同时保持场景真实性。生成的场景可用于评估轨迹规划算法应对长尾情况的能力。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lin-causal-composition-diffusion-model-for-closed-loop-traffic-generation-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 852, \"height\": 568, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lin-causal-composition-diffusion-model-for-closed-loop-traffic-generation-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1800, \"height\": 445, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lin-causal-composition-diffusion-model-for-closed-loop-traffic-generation-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 860, \"height\": 616, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-lin-causal-composition-diffusion-model-for-closed-loop-traffic-generation-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1700, \"height\": 693, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-causal-composition-diffusion-model-for-closed-loop-traffic-generation-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 877, \"height\": 549, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-causal-composition-diffusion-model-for-closed-loop-traffic-generation-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 862, \"height\": 607, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-causal-composition-diffusion-model-for-closed-loop-traffic-generation-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 862, \"height\": 672, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-lin-causal-composition-diffusion-model-for-closed-loop-traffic-generation-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 863, \"height\": 796, \"label\": \"Table\"}]"
motivation: 现有交通生成模型难以同时实现可控性和真实性。
method: 提出因果组合扩散模型，将约束优化与结构引导扩散结合。
result: 在保持真实性的前提下实现了更高的用户可控性。
conclusion: CCDiff为评估规划算法提供了更有效的仿真场景。
---

## Abstract
Simulation is critical for safety evaluation in autonomous driving, particularly in capturing complex interactive behaviors. However, generating **realistic** and **controllable** traffic scenarios in long-tail situations remains a significant challenge. Existing generative models suffer from the conflicting objective between user-defined controllability and realism constraints, which is amplified in safety-critical contexts. In this work, we introduce the **C**ausal **C**ompositional **Diff**usion Model (***CCDiff***), a structure-guided diffusion framework to address these challenges. We first formulate the learning of controllable and realistic closed-loop simulation as a constrained optimization problem. Then, CCDiff maximizes controllability while adhering to realism by automatically identifying and injecting causal structures directly into the diffusion process, providing structured guidance to enhance both realism and controllability. Through rigorous evaluations on benchmark datasets and in a closed-loop simulator, CCDiff demonstrates substantial gains over state-of-the-art approaches in generating realistic and user-preferred trajectories. Our results show CCDiff's effectiveness in extracting and leveraging causal structures, showing improved closed-loop performance based on key metrics such as collision rate, off-road rate, FDE, and comfort. For more details, welcome to check our project website: https://sites.google.com/view/ccdiff/.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：自动驾驶安全评估需要**真实且可控**的闭环交通仿真，但在安全关键的长尾场景中，现有方法无法平衡**用户定义的可控性**与**现实约束**。数据驱动方法（如基于深度生成模型）难以生成稀有的碰撞/近碰撞事件，且闭环仿真中的误差累积导致分布偏移；规则驱动方法（如基于手写规则）虽可精确控制，但缺乏真实感和适应性。
- **动机**：驾驶场景中智能体间的交互遵循内在的**因果结构**（每个智能体的行动主要依赖附近子集智能体的状态）。利用这一结构有望解决可控性与真实性之间的冲突。
- **整体目标**：提出一种结构引导的扩散框架 **CCDiff**，将闭环交通仿真建模为约束优化问题，通过自动识别并注入因果结构到扩散过程，同时最大化可控性和保证真实性。

## 2. 方法论：核心思想、关键技术细节、公式与算法流程

### 核心思想
- 将闭环仿真建模为 **Constrained Factored MDP (CFMDP)**，状态和动作空间被因子化以利用因果结构。
- 引入 **Decision Causal Graph (DCG)** 表示每个智能体决策时的因果依赖关系（条件独立性）。
- 利用扩散模型进行序列建模，通过**结构性指导**（interventional classifier-free guidance + masked classifier-based guidance）解决可控性与真实性的梯度冲突。

### 关键技术细节
1. **Causal Composition Scene Encoder**  
   - 包含时域注意力（编码智能体历史）、空间交叉注意力（融合相对特征如位置、速度、TTC）和**因果发现模块**。  
   - 通过基于TTC的硬掩码（\(M_{ij} = 1\) if \(f_{TTC} \le C_{ttc}\)）和softmax注意力权重计算DCG：  
     \[
     G_{ij} = M_{ij} \cdot \text{softmax}\left( \frac{(q W_q h_i)^T (k W_k h_{ij})}{\sqrt{d_k}} \right)
     \]
2. **Causal Ranking**  
   - 基于DCG使用社区检测算法排序智能体对安全关键目标的重要性，选择**top-K**关键智能体作为可控对象。
3. **Causal Composition Guidance**  
   - 对top-K智能体应用**interventional classifier-free guidance**（结合无条件分布和以因果父节点为条件的分布），对其他智能体保持原始真实策略。  
   - 同时使用**masked classifier guidance**，仅对关键智能体施加可微分奖励梯度（如碰撞避免），以消除梯度冲突：  
     \[
     \sum_{j} \nabla_{a^{(I_j)}} R^{(j)}(\tau) \approx \sum_{j} \rho_j(\tau) \cdot \nabla_{a} [R^{(j)}(\tau)]
     \]
4. **算法流程（推理）**  
   - 每个去噪步：  
     - 计算无条件/条件模型输出。  
     - 提取DCG和重要性排名。  
     - 组合指导（classifier-free + classifier-based）。  
     - 应用车辆动力学更新下一状态。

### 公式关键点
- 将综合目标分解为可控性项 \(\prod \exp(R^{(j)})\) 和真实性项 \(\prod \pi^{(i)}(a_t^{(i)}|s_t)\)，通过**Lagrangian乘子**和**结构化投影梯度下降**求解带约束优化（稀疏性约束 \(|G| \le C_{sparsity}\)，可控智能体数量 \(\sum \rho_i \le N_c\)）。

## 3. 实验设计

- **数据集**：nuScenes（训练集训练，验证集随机抽100个场景评估）。  
- **仿真框架**：tbsim (Traffic Behavior Simulation)，闭环生成未来10秒轨迹（初始3秒历史）。  
- **对比方法**：SimNet、TrafficSim、BITS、STRIVE、CTG（均为SOTA）。  
- **评价指标**：  
  - **Controllability Score (CS)**：基于场景碰撞率（SCR）标准化，越高越好。  
  - **Realism Score (RS)**：基于场景离路率（ORR）、最终位移误差（FDE）、舒适度距离（CFD）标准化后取平均，越高越好。  
  - **多目标优化指标**：Generational Distance (GD) 和 Inverted GD (IGD)，衡量与Pareto前沿的距离。

## 4. 资源与算力

- **论文未明确说明**使用的GPU型号、数量、训练时长等硬件信息。仅提及模型在nuScenes训练集上训练，未给出具体训练细节（如batch size、优化器、迭代次数等）。

## 5. 实验数量与充分性

- **实验组数**：  
  - **多智能体生成**：K=2,3,4,5,10,Full（共6组）。  
  - **长时域生成**：T=0.5s,1s,2s,3s,4s,5s（共6组）。  
  - **消融实验**：5种变体（w/o encoder, w/o factored guide, w/ Distance ranking, w/ Human ranking, 完整CCDiff）在K=1~5上的5×5=25个实验点。  
- **充分性**：实验覆盖了可控智能体数量、生成时域、因果模块影响等多个维度；使用标准化分数进行公平比较（所有方法在同一设置下运行）。参数设置（如TTC阈值、稀疏度阈值）未系统调优，但通过消融验证了各贡献。整体而言，实验设计较为全面、客观。

## 6. 主要结论与发现

- CCDiff在**可控制性（CS）和真实性（RS）**指标上均优于所有SOTA，尤其在多智能体和大时域设置下更接近Pareto前沿（更低的GD和IGD）。  
- 在K=5时，CCDiff的CS比最接近的竞争者CTG高约0.2（0.56 vs 0.41），RS也更高（0.88 vs 0.84）。  
- 长时域下，CCDiff在T=4s时CS达到0.89（CTG为0.78），RS为0.54（CTG为0.53）。  
- 消融实验表明：**因果排序（Causal Ranking）**贡献最大（替换为距离或人工排序后碰撞率下降5-10%，FDE增加超1m），因果编码器与分解指导也显著提升性能。

## 7. 优点

- **创新性**：首次将因果结构主动注入扩散过程的闭环仿真中，利用结构化指导解决可控性与真实性的冲突。  
- **方法论清晰**：从约束优化到CFMDP、DCG、扩散生成，逻辑链条完整；算法设计合理（通过掩码和重要性排名避免梯度冲突）。  
- **实验全面**：覆盖多智能体、长时域、消融实验，使用标准化分数和多目标指标进行公平比较。  
- **结果突出**：在多个指标上取得最佳或次佳，且可视化显示生成场景更真实、可控（如图1所示）。

## 8. 不足与局限

- **因果推理依赖超参数**：TTC阈值 \(C_{ttc}\)、稀疏约束 \(C_{sparsity}\)、可控智能体数量 \(N_c\) 等需手动调节，且难以直接评估因果图的正确性。  
- **计算资源未公开**：训练成本、推理速度等缺失，不利于复现和实际部署。  
- **泛化性有限**：仅在nuScenes一个数据集上评估，未在Waymo等更大规模、更多样化数据集上验证。  
- **评估偏差风险**：真实性指标（ORR、FDE、CFD）可能无法完全反映人类对真实性的感知；可控性仅通过碰撞率衡量，未包括如违反交通规则等更细粒度的控制需求。  
- **长时域性能衰减**：尽管优于基线，但随着时域变长（T=5s），RS仍下降至0.49，表明闭环误差累积问题仍未完全解决。

（完）
