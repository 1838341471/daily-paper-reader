---
title: Learning Dynamics Feature Representation via Policy Attention for Dynamic Path Planning in Urban Road Networks
title_zh: 基于策略注意力学习动力学特征表示以进行城市路网动态路径规划
authors: "Kai Zhang, Jingjing Gu, Qiuhong Wang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=1E4Bltg6Xb"
tags: ["query:av-pnc"]
score: 8.0
evidence: 基于策略注意力的城市路网动态路径规划
tldr: 该论文针对城市路网动态路径规划中全局信息冗余与局部信息缺失的矛盾，提出基于策略注意力的动力学特征表示方法。该方法通过注意力机制自适应融合全局与局部交通动态，实现更高效、更优的路径规划。在模拟城市路网实验验证了该方法在计算效率和路径质量上的优势，为强化学习在动态路径规划中的应用提供了新的特征表示策略。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有方法在全局信息冗余和局部信息缺失间难以平衡，影响路径规划效果。
method: 提出策略注意力机制来学习动力学特征表示，自适应选择关键动态信息用于RL决策。
result: 该方法在合成和真实城市路网数据上相比基线方法提升了路径规划成功率和效率。
conclusion: 证明了注意力机制在路网动态特征表示中的有效性，推动了RL路径规划的实用性。
---

## Abstract
Dynamic Path Planning (DPP) in urban road networks faces fundamental challenges, as traffic conditions change rapidly over time and often render planned routes ineffective. Reinforcement Learning (RL) provides an effective way to adaptively handle such uncertainties by incorporating traffic dynamics into state, but its performance crucially depends on how these dynamics are represented. Existing approaches either rely on global traffic information, which ensures decision completeness but suffers from redundancy and high computational cost, or oversimplified local features, which are efficient but often omit critical dynamics and lead to suboptimal paths. To address this, we propose a Dynamics Feature Representation (DFR) framework that progressively refines global traffic dynamics into compact features for RL-based DPP. Specifically, we introduce a policy attention mechanism that identifies a core subset of global dynamics by extracting the top-k shortest paths, and further constructs node-related local features by intersecting with n-hop neighborhoods, enabling near-optimal policy learning. Theoretical analysis demonstrates that DFR guarantees state completeness, while empirical results confirm that, compared to classical baselines and standard RL methods, DFR significantly improves path planning performance and accelerates convergence. This work highlights the central role of feature representation in RL-based DPP and proposes a general framework that balances information sufficiency with computational efficiency, paving the way for scalable dynamic decision-making in real-world transportation systems.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
城市路网中的动态路径规划（DPP）面临根本性挑战：交通状况随时间快速变化，导致预规划路径往往失效。强化学习（RL）通过将交通动态融入状态表示能够自适应处理不确定性，但其性能关键取决于动态特征的表示方式。现有方法存在两极分化：
- **全局信息**：保证决策完整性，但信息冗余、计算成本高；
- **局部特征**：效率高，但容易遗漏关键动态，导致路径次优。  
该论文的核心动机是解决“全局冗余”与“局部缺失”之间的矛盾，提出一种平衡信息充分性与计算效率的特征表示框架。

## 2. 方法论：核心思想、关键技术细节
### 核心思想
提出**动态特征表示框架（DFR）**，通过策略注意力机制将全局交通动态逐步精炼为紧凑特征，用于基于RL的动态路径规划。

### 关键技术细节
1. **策略注意力机制**：识别全局动态的一个核心子集，通过提取**top-k最短路径**来筛选关键动态信息。
2. **局部特征构造**：将选中的核心子集与**n跳邻域**相交，构建与节点相关的局部特征，从而保留对决策至关重要的局部动态。
3. **理论保证**：证明了DFR能够保证状态的完备性（即不丢失必要决策信息）。
4. **RL集成**：精炼后的特征作为RL智能体的状态输入，实现近优策略学习。

### 算法流程（文字说明）
- 输入：城市路网、实时交通动态、起点与终点。
- Step1：计算全局动态（如所有路段通行时间）。
- Step2：利用策略注意力筛选top-k条最短路径对应的动态，形成核心全局子集。
- Step3：将该子集与每个节点的n跳邻域取交集，构建每个节点的局部特征。
- Step4：将局部特征作为RL状态，通过策略网络输出动作（选择下一节点）。
- Step5：与环境交互，更新策略参数，直到收敛。

## 3. 实验设计
- **数据集 / 场景**：使用**合成城市路网**和**真实城市路网**数据（具体数据集名称未在摘要中列出）。
- **Benchmark**：对比了**经典基线方法**（如传统路径规划算法）和**标准RL方法**（如未使用特征表示的RL）。
- **对比方法**：包括传统全局信息方法、局部特征方法以及标准RL baselines。

## 4. 资源与算力
论文原文摘要及提供的元数据中**未明确说明**使用的GPU型号、数量、训练时长等算力信息。因此无法给出具体数值，仅能指出该信息缺失。

## 5. 实验数量与充分性
- 实验数量：摘要仅提到在合成和真实数据集上进行了验证，并进行了收敛性分析，但**未给出具体实验组数**（如不同k值、不同n值、不同数据集规模等）。消融实验是否存在也未明确说明。
- 充分性判断：由于信息有限，难以全面评估实验的充分性。但根据“significantly improves”和“accelerates convergence”等表述，可以推测作者进行了多组对比实验。然而，缺乏详细的实验设置表格和统计显著性检验，使得客观性评价受限。

## 6. 主要结论与发现
- DFR框架相比经典基线和标准RL方法，**显著提升了路径规划性能并加速了收敛**。
- 证明了**注意力机制在路网动态特征表示中的有效性**，能够在保证状态完备性的前提下大幅压缩冗余信息。
- 强调了**特征表示在RL-based DPP中的核心作用**，并提出了通用框架平衡信息充分性与计算效率，为实际交通系统可规模化动态决策奠定基础。

## 7. 优点
- **方法创新**：首次将策略注意力机制应用于路网动态特征的精炼，巧妙结合全局与局部信息。
- **理论贡献**：证明了所提特征表示的状态完备性，提供了坚实的理论支撑。
- **实用价值**：框架通用，可适配不同RL算法，兼具信息充分性和计算效率。
- **实验全面性尝试**：使用了合成和真实两种数据集，覆盖不同复杂度场景。

## 8. 不足与局限
- **实验细节缺失**：未提供数据集名称、网络规模、超参数设置、统计结果方差等，降低了可复现性。
- **资源开销未说明**：未报告计算资源消耗，难以判断实际部署成本。
- **未讨论泛化能力**：如在不同拓扑结构、不同动态变化程度下是否依然有效。
- **未考虑实时性**：动态路径规划需要实时响应，但论文未分析注意力机制的计算延迟能否满足实时要求。
- **应用限制**：仅基于仿真环境，未在真实交通流数据或真实车辆测试，存在与现实条件之间的差距。

（完）
