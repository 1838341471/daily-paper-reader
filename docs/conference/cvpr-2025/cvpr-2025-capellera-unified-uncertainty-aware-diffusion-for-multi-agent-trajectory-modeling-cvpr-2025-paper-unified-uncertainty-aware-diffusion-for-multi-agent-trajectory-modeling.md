---
title: Unified Uncertainty-Aware Diffusion for Multi-Agent Trajectory Modeling
title_zh: 统一不确定性感知扩散用于多智能体轨迹建模
authors: "Capellera, Guillem, Rubio, Antonio, Ferraz, Luis, Agudo, Antonio"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Capellera_Unified_Uncertainty-Aware_Diffusion_for_Multi-Agent_Trajectory_Modeling_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 9.0
evidence: 多智能体轨迹建模，不确定性感知扩散，支持轨迹完成与预测
tldr: 多智能体轨迹建模通常只关注预测，忽略了轨迹完成等任务，且缺乏不确定性估计。本文提出U2Diff，一个统一的扩散模型，可同时处理轨迹完成和预测，并输出每个状态的不确定性。通过修改去噪过程，模型能估计预测误差的概率。在多个轨迹数据集上，U2Diff在完成和预测任务中均达到最优，其不确定性估计有助于排序和拒绝不可靠预测。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-capellera-unified-uncertainty-aware-diffusion-for-multi-agent-trajectory-modeling-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1797, \"height\": 391, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-capellera-unified-uncertainty-aware-diffusion-for-multi-agent-trajectory-modeling-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 758, \"height\": 575, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-capellera-unified-uncertainty-aware-diffusion-for-multi-agent-trajectory-modeling-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 800, \"height\": 364, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-capellera-unified-uncertainty-aware-diffusion-for-multi-agent-trajectory-modeling-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 842, \"height\": 522, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-capellera-unified-uncertainty-aware-diffusion-for-multi-agent-trajectory-modeling-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1795, \"height\": 573, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-capellera-unified-uncertainty-aware-diffusion-for-multi-agent-trajectory-modeling-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 861, \"height\": 473, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-capellera-unified-uncertainty-aware-diffusion-for-multi-agent-trajectory-modeling-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 806, \"height\": 367, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-capellera-unified-uncertainty-aware-diffusion-for-multi-agent-trajectory-modeling-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 806, \"height\": 170, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-capellera-unified-uncertainty-aware-diffusion-for-multi-agent-trajectory-modeling-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 862, \"height\": 315, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-capellera-unified-uncertainty-aware-diffusion-for-multi-agent-trajectory-modeling-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 717, \"height\": 326, \"label\": \"Table\"}]"
motivation: 现有轨迹模型任务单一，缺乏状态级不确定性度量，难以评估预测可靠性。
method: 设计增强去噪扩散模型，联合学习轨迹生成与不确定度，支持多任务。
result: 在轨迹完成和预测基准上，U2Diff性能领先，不确定性估计与实际误差相关性强。
conclusion: 统一不确定性扩散框架为实际轨迹建模提供了更可信的解决方案。
---

## Abstract
Multi-agent trajectory modeling has primarily focused on forecasting future states, often overlooking broader tasks like trajectory completion, which are crucial for real-world applications such as correcting tracking data. Existing methods also generally predict agents' states without offering any state-wise measure of uncertainty. Moreover, popular multi-modal sampling methods lack any error probability estimates for each generated scene under the same prior observations, making it difficult to rank the predictions during inference time. We introduce U2Diff, a unified diffusion model designed to handle trajectory completion while providing state-wise uncertainty estimates jointly. This uncertainty estimation is achieved by augmenting the simple denoising loss with the negative log-likelihood of the predicted noise and propagating latent space uncertainty to the real state space. Additionally, we incorporate a Rank Neural Network in post-processing to enable error probability estimation for each generated mode, demonstrating a strong correlation with the error relative to ground truth. Our method outperforms the state-of-the-art solutions in trajectory completion and forecasting across four challenging sports datasets (NBA, Basketball-U, Football-U, Soccer-U), highlighting the effectiveness of uncertainty and error probability estimation.

---

## 论文详细总结（自动生成）

### 论文的核心问题与整体含义（研究动机和背景）

- **问题背景**：多智能体轨迹建模传统上聚焦于预测未来状态（forecasting），忽视了轨迹补全（trajectory completion）等更广泛的任务（例如在体育追踪数据中校正缺失轨迹）。现有方法通常仅输出位置，不提供每个状态的**不确定性度量**，并且多模态采样方法（如扩散模型）无法为同一先验下的多个生成场景提供**误差概率估计**，导致推理时难以对预测结果进行排序。
- **研究动机**：为了弥补上述空白，本文希望构建一个统一的模型，既能完成多种轨迹补全任务（预测、插补、推断完全未观测的智能体），又能联合输出每个状态的**逐点不确定性**（state-wise uncertainty），并在后处理中为每个生成模态提供**误差概率**（error probability），从而提升模型的可解释性和实际部署的可靠性。

### 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：基于条件扩散概率模型（DDPM），设计统一框架 **U2Diff**，将轨迹补全问题建模为条件生成，通过修改损失函数使模型同时预测噪声的均值与标准差，实现不确定性学习；再通过方差传播将潜在空间的不确定性映射到真实状态空间；最后设计**RankNN**后处理网络，从多个生成模态中估计与真实误差高度相关的概率分数。

- **关键技术细节**：
  1. **问题形式化**：给定部分观测轨迹 `X_co` 及其二进制掩码 `M`（1表示可见，0表示缺失），模型学习完整轨迹 `X` 的分布，目标为 `p(X|X_co, M) = N(f_μ(X_co,M), f_σ²(X_co,M))`。
  2. **不确定性感知扩散**：经典DDPM中，反向过程只学习噪声均值（`ϵ_θ`）。本文让网络同时输出噪声的均值 `ϵ_μθ` 和标准差 `ϵ_σθ`，并定义**负对数似然损失**（`L_NLL`）来最大化噪声的对数似然。总损失为 `L_total = L_simple + λ L_NLL`（`L_simple`为经典MSE损失），其中对均值使用stop-gradient，使 `L_NLL` 专注学习标准差。
  3. **方差传播**：在采样时，使用DDIM（带跳跃步长ζ）的确定性更新公式，但额外引入了方差传播规则：`Var(X_{s-ζ}) = (α̂_{s-ζ}/α̂_s)² Var(X_s) + (a_{s-ζ} - √(α̂_{s-ζ}/α̂_s) a_s)² ϵ_σθ²`。方差初始化为零，并发现从较大去噪步 **ŝ=30**（总步数S=50）开始传播方差效果最优。
  4. **网络架构**：借鉴CSDI，但将原始Transformer编码器替换为**双向MambaSSM**（Temporal Mamba）进行时间维度处理，并保留**Social Transformer**处理智能体间交互。输入嵌入为观测融合噪声样本（T×N×4），通过两个残差块（每个块内依次是Temporal Mamba和Social Transformer），输出张量经线性层和sigmoid分别得到噪声均值和标准差。
  5. **RankNN后处理**：输入K个生成模态的均值、方差和掩码，通过Temporal Mamba + Social Transformer + Multi-scene Transformer（跨模态注意力）+ 全连接层 + softmax，输出K个误差概率`e_k`。优化目标为最大化**Spearman秩相关系数**ρ（通过可微分排序实现）在`e_k`与场景平均位移误差（SADE）之间的单调相关性。

### 实验设计

- **数据集**：四个体育轨迹数据集：
  - **Basketball-U**：基于NBA，10球员+球，50帧（8秒），训练/测试：93,490/11,543序列。
  - **Football-U**：基于NFL Big-Data-Bowl，22球员+球，50帧，10,762/2,624序列。
  - **Soccer-U**：基于SoccerTrack，22球员+球，50帧，9,882/2,448序列。
  - **NBA SportVU**：用于预测任务，10球员+球，30帧（6秒），观测2秒预测4秒。

- **任务与基准**：
  - **轨迹补全**：遵循UniTraj提出的五种掩蔽策略，包括预测未来、插补中间状态、推断未观测智能体等。对比方法：UniTraj（SOTA）、SSSD、GC-VRNN、INAM、Naomi、MAT、Transformer、LSTM等。
  - **轨迹预测**：NBA数据集，观测10帧预测20帧。对比方法：LED（扩散模型SOTA）、AutoBots、GroupNet、MID、MemoNet、NPSN等。

- **评价指标**：
  - 智能体级：minADE_K、minFDE_K
  - 场景级：minSADE_K、minSFDE_K
  - 不确定性质量：AccRate（95%置信区间内真实状态占比）、NLL
  - 排序相关性：Spearman相关系数ρ

### 资源与算力

- **文中未明确说明使用的GPU型号、数量及训练时长**。仅提及批次大小、训练步数等细节（可能在其他补充材料中）。因此无法给出具体算力信息。

### 实验数量与充分性

- **实验组数较多且充分**：
  1. 轨迹补全任务：在三个数据集上对比多个基线，报告minADE_20和minSADE_20。
  2. 轨迹预测任务：在NBA上对比多种SOTA，报告agent-wise和scene-level指标。
  3. 消融实验（表1和表2）：比较有无`L_NLL`（λ=0 vs λ>0）的影响。
  4. 不确定性质量评估（表3）：计算AccRate和NLL，并比较三种采样策略（Mean、Top-1 e、Top-1 SADE）。
  5. 排序相关性实验（表4、图5）：对比AvgUcty（全局平均方差）与RankNN的ρ，并展示分布；还比较了不同ŝ设置；与AutoBots的排序能力对比。
  6. Top-k选择实验（表5）：在NBA上，用不同排序方法（Random、AvgUcty、e）选择Top-k模态计算minSADE_k，并与LED和AutoBots对比。

- **公平性**：对比方法均使用官方代码、重新训练或直接采用已发布模型；所有指标统一。消融设计合理，验证各组件贡献。

### 论文的主要结论与发现

- **性能领先**：U2Diff在轨迹补全任务中大幅超越UniTraj（如Football-U上minADE_20降低31%，Soccer-U降低42%）；在预测任务中场景级指标超越LED等SOTA约9%。
- **不确定性有效**：通过损失增强和方差传播，模型估计的逐点不确定性具有高AccRate（>90%），且与真实误差呈正相关（Spearman ρ中位数0.25~0.35）。
- **RankNN提升排序**：RankNN输出的误差概率与SADE的Spearman相关性显著提高（中位数0.58~0.78），优于简单的AvgUcty，并能有效选出更优的Top-k模态（表5）。
- **通用性与灵活性**：模型不受固定时间步长和智能体数量限制，可同时处理补全和预测任务。

### 优点

1. **统一框架**：首次将扩散模型扩展到通用的轨迹补全（含预测、插补、未观测智能体推断）与不确定性联合估计。
2. **实用性不确定性**：提供逐状态方差，且能通过简单的方差传播从隐空间映射至实际空间，无需复杂后处理。
3. **RankNN创新**：监督式后处理网络，无需固定模态数量，直接优化排序相关性，具有实际部署价值（如选择最可靠预测）。
4. **架构改进**：采用双向MambaSSM替代Transformer进行时间建模，去除位置编码，提升时序处理能力。
5. **实验充分**：在四个真实体育数据集上，涵盖补全和预测任务，与多个SOTA对比，并进行了详细的消融和排序分析。

### 不足与局限

1. **计算资源未公开**：论文未提供训练所需的GPU型号、数量及时间，使得复现和成本评估困难。
2. **领域局限**：仅在体育数据集上验证，未在行人、自动驾驶等常见多智能体轨迹预测基准（如ETH/UCY、nuScenes）上进行测试，泛化能力待证实。
3. **方差传播的启发式选择**：最佳起始去噪步ŝ=30是通过实验确定，缺乏理论解释，可能对噪声调度敏感。
4. **RankNN训练依赖标注**：需要使用真实轨迹计算SADE作为监督，在无标注场景下无法训练，且与U2Diff耦合（冻结U2Diff权重生成模式），可能带来数据偏差。
5. **实验覆盖不足**：
   - 未进行消融实验分析Mamba vs Transformer单独贡献。
   - 未在多样性指标（如minADE/FDE的方差）上对比，只关注平均误差。
   - 未与其他不确定性方法（如贝叶斯方法）对比AccRate或NLL。
6. **潜在偏差风险**：数据来自特定体育项目，球员运动模式可能导致模型对类似运动模式过度拟合；掩蔽策略固定（遵循UniTraj），实际应用中的缺失模式未知。

（完）
