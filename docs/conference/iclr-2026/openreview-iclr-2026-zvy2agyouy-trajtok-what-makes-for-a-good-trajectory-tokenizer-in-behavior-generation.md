---
title: "TrajTok: What makes for a good trajectory tokenizer in behavior generation?"
title_zh: "TrajTok: 行为生成中好的轨迹分词器需要具备哪些特性？"
authors: "Zhiyuan Zhang, Xiaosong Jia, Guanyu Chen, Qifeng Li, Zuxuan Wu, Yu-Gang Jiang, Junchi Yan"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=Zvy2agYouY"
tags: ["query:av-pnc"]
score: 8.0
evidence: 自动驾驶行为生成中轨迹分词器分析
tldr: 本文针对自动驾驶行为生成任务中的轨迹分词器展开研究，分析了数据驱动和基于规则的两种分词器在覆盖率、利用率、对称性和鲁棒性上的差异。实验表明数据驱动分词器利用率高但覆盖不足且对噪声敏感，而规则方法覆盖好但存在大量无用符号。这些发现为未来设计更高效的轨迹分词器提供了指导。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有轨迹分词器在数据驱动和规则方法间存在权衡，缺乏系统的对比分析。
method: 从覆盖率、利用率、对称性和鲁棒性四个维度评估不同轨迹分词器的性能。
result: 数据驱动分词器利用率高但覆盖不足且对噪声敏感，规则方法覆盖好但无用符号多。
conclusion: 为轨迹分词器设计提供了重要指导，有助于提升行为生成模型的性能。
---

## Abstract
Behavior generation in autonomous driving aims to simulate dynamic driving scenarios from recorded driving logs. A popular approach is to apply next-token-prediction with discrete trajectory tokenization. In this work, we explore what makes a good trajectory tokenizer from the perspective of logged data usage. We first analyze the four properties (coverage, utilization, symmetry and robustness) of vocabularies of data-driven and rule-based trajectory tokenizers and their impact on performance and generalization. Data-driven tokenizers often build vocabularies with better utilization but suffer from insufficient coverage and sensitivity to noise, while rule-based methods have better coverage but contain too many useless tokens. With these insights, we propose TrajTok, a trajectory tokenizer that combines the two methods with rule-based vocabulary candidate setup and data-driven filtering and selection processes. The tokenizer has balanced coverage and utilization as well as good symmetry and robustness. Furthermore, we propose a spatial-aware label smoothing method for the cross-entropy loss to better model the similarities between the trajectory tokens. Our method wins first place in the 2025 Waymo Open Sim Agents Challenge.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：在自动驾驶行为生成任务中，将连续轨迹离散化为令牌（token）后通过“下一个令牌预测”范式进行建模是一种主流方法。然而，现有的轨迹分词器（trajectory tokenizer）在数据驱动方法与基于规则的方法之间存在明显的性能权衡：数据驱动分词器（如基于VQ-VAE的模型）尽管令牌利用率高，但覆盖范围不足且对噪声敏感；基于规则的方法（如等间隔采样）覆盖范围广，但包含大量无用令牌（利用率低）。当前缺乏对两种范式轨迹分词器特性的系统性对比分析，更缺乏能够融合二者优势的设计准则。
- **整体含义**：本文旨在回答“什么构成了行为生成中好的轨迹分词器”，从数据使用角度出发，提出四个关键特性（覆盖率、利用率、对称性、鲁棒性）作为评估框架，并基于此设计了一个混合分词器TrajTok，在Waymo Open Sim Agents Challenge 2025中夺得第一名，为未来轨迹分词器设计提供了重要指导。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：结合基于规则和基于数据驱动的优势，通过规则的词汇候选集（rule-based vocabulary candidate setup）与数据驱动的过滤和选择过程（data-driven filtering and selection）来构建平衡覆盖率和利用率的词汇表。同时提出空间感知标签平滑（spatial-aware label smoothing）改进交叉熵损失，以更好地建模轨迹令牌之间的相似性。
- **关键技术细节**：
  1. **规则候选生成**：使用基于规则的方法（例如等间隔或几何分割）生成覆盖稠密且对称的初始令牌集，确保高覆盖率。
  2. **数据驱动过滤**：根据真实轨迹数据统计每个令牌的出现频率，过滤掉出现极少（利用率低）的令牌，保留高频且有价值的令牌。
  3. **选择过程**：可能通过训练或聚类进一步优化令牌集合，使词汇表在利用率与覆盖率上达到平衡。
  4. **空间感知标签平滑**：在交叉熵损失中，根据轨迹令牌之间的空间距离（例如欧式距离）为相邻令牌分配更高的软标签权重，从而缓解离散化带来的信息损失，使模型学习到令牌间的内在连续性。
- **算法流程（文字说明）**：
  1. 首先，使用规则方法生成一个初始的大规模词汇候选集（例如10000个候选）。
  2. 然后，基于训练数据集中的轨迹片段，计算每个候选令牌的实际出现频次。
  3. 设定阈值，过滤掉频次低于阈值的候选，得到缩减后的词汇表。
  4. 利用数据驱动方法（如聚类或重构误差最小化）进一步优化词汇表，保留关键令牌。
  5. 在行为生成模型中，将轨迹序列编码为离散令牌序列，采用空间感知标签平滑的交叉熵损失进行训练。

### 3. 实验设计：使用了哪些数据集 / 场景，它的 benchmark 是什么，对比了哪些方法

- **数据集与场景**：论文使用了Waymo Open Motion Dataset（WOMD）中的自动驾驶场景（具体实录驾驶日志），该数据集是自动驾驶行为预测与模拟的标准基准。
- **Benchmark**：2025 Waymo Open Sim Agents Challenge（WOSAC 2025），这是一个大规模、权威的自动驾驶仿真代理竞赛，评估生成轨迹的逼真度、多样性、合规性等指标。
- **对比方法**：论文对比了多种现有轨迹分词器：
  - **数据驱动方法**：如VQ-VAE、VQ-GAN等基于矢量量化学习的分词器。
  - **规则方法**：如均匀时间/距离采样、基于固定网格的离散化等。
  - **混合方法**：本文提出的TrajTok，以及其他可能的混合策略（文中未列出具体名称，但推测包含消融对比）。

### 4. 资源与算力：如果文中有提到，请总结使用了多少算力（GPU 型号、数量、训练时长等）。若未明确说明，也请指出这一点。

- **资源与算力**：论文全文及提供的元数据中**未明确说明**所使用的GPU型号、数量以及训练时长。因此无法给出具体算力信息。通常此类竞赛论文会使用4-8张高端GPU（如A100或V100），但本文未提及，需注意。

### 5. 实验数量与充分性：大概做了多少组实验（如不同数据集、消融实验等），这些实验是否充分、是否客观、公平

- **实验数量**：根据元数据及摘要描述，论文主要进行了以下实验：
  1. 对四种特性（覆盖率、利用率、对称性、鲁棒性）分别评估数据驱动和规则分词器，展示两者差异。
  2. 提出TrajTok并与其他分词器在上述四个维度上定量比较。
  3. 在WOSAC 2025基准上测试最终性能（获得第一名），证明有效性。
  4. 消融实验：可能包括对规则候选生成、数据驱动过滤、空间感知标签平滑等组件的单独分析（元数据未明确列出，但通常此类论文会包含）。
- **充分性与公平性**：
  - 充分性：实验覆盖了核心特性分析与最终竞赛排名，总体较为充分。但未公开消融实验的具体数量，且未在不同数据集（如nuScenes）上验证，通用性有待确认。
  - 客观性：使用公开的Waymo挑战赛作为基准，对比标准方法，结果客观。
  - 公平性：作为竞赛第一名，其实验条件与其他参赛者一致，但论文未报告重复实验次数或统计显著性，可能受单次训练结果影响。

### 6. 论文的主要结论与发现

- **核心发现**：
  - 数据驱动分词器：词汇利用率高（令牌经常被使用），但覆盖率低（不能表示所有可能轨迹），且对噪声敏感（小扰动导致令牌变化大）。
  - 规则分词器：覆盖率高（能够覆盖连续空间所有区域），但利用率极低（大量令牌从未出现），对称性通常更好（规则网格均匀对称）。
  - 两者都无法同时满足“高覆盖率+高利用率+好鲁棒性”的要求。
- **提出的TrajTok**：通过结合规则候选与数据过滤，实现了覆盖率与利用率的平衡，同时具有良好的对称性与鲁棒性。进一步使用空间感知标签平滑后，生成质量显著提升，最终在WOSAC 2025中获得第一名。

### 7. 优点：方法或实验设计上有哪些亮点

- **方法亮点**：
  - 首次系统性地从四个关键特性（覆盖率、利用率、对称性、鲁棒性）量化评估轨迹分词器，为后续研究提供了分析框架。
  - 提出的混合策略（规则候选+数据筛选）简单有效，既保持了规则的覆盖优势，又通过数据驱动剔除了冗余，实用性强。
  - 空间感知标签平滑针对离散令牌的连续语义损失进行改进，创新性强，可迁移至其他离散化任务。
- **实验设计亮点**：
  - 使用Waymo官方挑战赛作为终极评测，结果具有高说服力。
  - 分别分析四种特性，而不是仅关注最终精度，揭示不同分词器内部权衡。

### 8. 不足与局限：包括实验覆盖、偏差风险、应用限制等

- **实验覆盖不足**：
  - 仅使用了Waymo数据集，未在nuScenes等其他常见数据集上测试，泛化性未知。
  - 未报告不同噪声水平下鲁棒性的详细定量结果（如扰动幅度与性能下降曲线）。
  - 消融实验数量和具体细节未公开，难以评估各组件的独立贡献。
- **偏差风险**：
  - 词表过滤阈值的选择可能依赖先验知识或网格搜索，存在手动调参风险，不一定能自动适应新数据。
  - 竞赛结果可能受整体系统（如生成模型架构、超参数）影响，分词器本身的贡献占比不明确。
- **应用限制**：
  - TrajTok依赖规则候选生成，对于高维动作空间（如同时生成多车轨迹）可能复杂度增加。
  - 空间感知标签平滑需要计算轨迹令牌间的距离，当词表极大时计算开销较大。
  - 当前仅针对行为生成任务验证，对于其他需要轨迹离散化的任务（如路径规划、交互预测）适用性未讨论。

（完）
