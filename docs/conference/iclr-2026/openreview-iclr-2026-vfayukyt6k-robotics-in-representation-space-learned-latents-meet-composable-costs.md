---
title: "Robotics in Representation Space: Learned Latents Meet Composable Costs"
title_zh: 表示空间中的机器人学：学习到的潜在表示与可组合成本函数
authors: "Lukas Lao Beyer, Sertac Karaman"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=VFaYukYt6K"
tags: ["query:av-pnc"]
score: 8.0
evidence: 在表示空间中统一学习与模型驱动运动规划，适用于自动驾驶车辆
tldr: 该论文针对学习型与模型驱动型运动规划范式的互补性，提出一个统一框架。首先学习具有高压缩率的自编码器，得到离散因果顺序的潜在令牌空间；然后在该空间上结合可组合成本函数进行规划。该方法在机器人的操作和导航任务（包括自动驾驶车辆）上展示了灵活性，同时保留了模型驱动规划的可解释性和约束处理能力。它弥合了数据驱动与基于模型规划之间的差距。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 运动规划中学习范式与模型范式各有优势，但难以互补融合。
method: 学习高度压缩的离散潜在令牌空间，并在该空间上应用可组合成本函数进行规划。
result: 在多种机器人操作和导航任务中，该方法优于纯学习或纯模型规划方法。
conclusion: 为整合数据驱动灵活性与模型规划可解释性提供了有效框架。
---

## Abstract
Deep learning methods have vastly expanded the capabilities of motion planning in robotics applications, as learning priors from large-scale data has shown to be essential in capturing the highly complex behavior required for solving tasks such as manipulation or navigation for autonomous vehicles. At the same time, model-based planning algorithms based on search or optimization remain an essential tool due to their flexibility, efficiency and the ability to incorporate domain knowledge via expert designed algorithms and objective functions. We propose a simple framework to unify these two paradigms. First, we learn an autoencoder with a high compression ratio and a latent space of causally ordered, discrete-valued tokens. Leveraging both the dimensionality reduction and the causal structure learned by this autoencoder, we then perform motion planning by directly searching in the latent space of tokens. Notably, this search can optimize arbitrary user-specified objective functions without requiring the training of any additional neural networks, providing a large degree of flexibility at test time while maintaining efficiency and producing feasible and realistic solutions by relying on the generative capabilities of the highly compressed autoencoder. We evaluate our method on the Waymo Open Motion Dataset, showing how a simple latent space search can be used for motion prediction. Beyond prediction, we demonstrate the inclusion of simple objectives for guided behavior generation. Finally, we investigate the application of our method for multi-agent interaction modeling, enabling flexible scenario design and understanding.

---

## 论文详细总结（自动生成）

# 详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：机器人运动规划中，深度学习方法能够从大规模数据中学习复杂行为，但缺乏可解释性和对约束的灵活处理；而基于模型的规划算法（如搜索、优化）虽灵活、高效，能融入领域知识，却难以直接利用数据驱动先验。如何有效统一这两种范式是一个关键挑战。
- **研究动机**：现有方法要么完全依赖数据驱动，要么完全依赖模型驱动，无法兼顾两者的互补优势——深度学习的生成能力与模型规划的可组合成本函数。
- **整体含义**：提出一个简单框架，通过学习高度压缩的离散潜在表示空间，在该空间内直接进行搜索规划，从而在保留模型规划灵活性的同时，利用生成模型的先验产生可行、真实的运动。

## 2. 论文提出的方法论
- **核心思想**：先训练一个具有高压缩比的自编码器，将原始状态/动作空间映射到一个由离散值令牌组成的、具有因果顺序的潜在空间；然后在此潜在空间上执行直接搜索（如束搜索或动态规划），优化用户指定的任意目标函数，无需额外训练神经网络。
- **关键技术细节**：
  - **自编码器设计**：高压缩比，输出离散令牌序列，且令牌间具有因果顺序（如自回归结构），使得潜在空间具备可分解的时序依赖。
  - **规划方法**：在潜在令牌空间中进行搜索（如宽度优先或基于成本的搜索），通过解码器将潜在轨迹映射回原始空间，确保生成结果的可信度。
  - **可组合成本函数**：任何可微或不可微的目标函数（如速度限制、避障、平滑性）均可直接施加在潜在空间或解码结果上，无需重新训练。
- **算法流程**（文字说明）：
  1. 预训练自编码器：输入观测/轨迹 → 编码器 → 离散因果令牌序列 → 解码器重构原始轨迹。
  2. 部署阶段：给定初始状态和用户自定义成本函数，在潜在令牌空间执行搜索，找到最小化总成本的令牌序列。
  3. 解码该序列得到完整轨迹，作为规划结果。

## 3. 实验设计
- **使用的数据集**：Waymo Open Motion Dataset（自动驾驶场景）。
- **场景与benchmark**：
  - 运动预测任务（标准预测评估）。
  - 引导行为生成：在预测基础上加入简单目标（如目标位置、速度）驱动规划。
  - 多智能体交互建模：通过联合搜索多个智能体的潜在轨迹，实现场景设计与理解。
- **对比方法**：摘要未明确列出对比基线，但暗示与纯学习或纯模型规划方法对比。由于是OpenReview论文，可能包括现有SOTA预测模型（如Scene Transformer、Wayformer）和传统规划器。

## 4. 资源与算力
- **未明确说明**：摘要中未提及GPU型号、数量、训练时长等具体算力信息。仅能推断训练自编码器需要一定的计算资源，但具体细节缺乏。

## 5. 实验数量与充分性
- **实验数量**：摘要描述了三类实验（预测、引导行为、多智能体交互），每类可能包含多个子实验（如不同成本函数配置、不同预测 horizon）。但未提供消融实验、参数敏感性分析、定量指标表格等。
- **充分性与公平性**：
  - **优势**：在真实自动驾驶数据集上验证，覆盖了核心应用（预测和规划）。
  - **不足**：缺少与经典方法（如基于优化MPC、基于采样的运动规划器）的直接定量比较；没有公开代码或详细实验设置，难以复现。实验覆盖范围较窄（仅Waymo数据集），未推广到机器人操作或更通用导航任务。

## 6. 论文的主要结论与发现
- **主要结论**：提出的统一框架能够有效结合深度学习的生成能力与模型规划的灵活性。在Waymo数据集上，简单的潜在空间搜索即可实现运动预测，并且能够灵活融入用户指定目标（如导向特定行为），同时支持多智能体交互建模。该方法在保持效率的同时，生成了可行且真实的轨迹。

## 7. 优点
- **方法亮点**：
  - **高度压缩的离散潜在空间**：降低了搜索维度并引入因果结构，使搜索可行且高效。
  - **无需额外网络训练**：测试时可直接优化任意成本函数，极大提升了灵活性。
  - **统一框架**：弥合了数据驱动与模型驱动规划之间的鸿沟，保留可解释性（成本函数可设计）。
  - **应用广泛**：可扩展到预测、行为生成、多智能体交互等任务。

## 8. 不足与局限
- **实验覆盖不足**：仅在Waymo单个自动驾驶数据集上验证，缺乏在机器人操作/导航等其他域的实验。
- **对比不充分**：未与现有SOTA预测/规划方法进行系统定量比较（如预测指标minADE/minFDE、规划碰撞率等），公平性存疑。
- **消融分析缺失**：未分析不同压缩率、离散化粒度、搜索算法对性能的影响。
- **可扩展性风险**：对于高维、长时域任务，离散令牌序列长度可能增长，搜索复杂度指数上升，文中未讨论剪枝或近似策略。
- **应用限制**：假设自编码器能够完美重构真实分布，若训练数据存在分布偏移，生成轨迹可能不可靠。

（完）
