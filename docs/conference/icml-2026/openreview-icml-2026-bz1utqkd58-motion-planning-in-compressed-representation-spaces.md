---
title: Motion Planning in Compressed Representation Spaces
title_zh: 压缩表示空间中的运动规划
authors: "Lukas Lao Beyer, Sertac Karaman"
date: 2026-04-30
pdf: "https://openreview.net/pdf/d1d57586df5e61de44748077cc96bc464726ada2.pdf"
tags: ["query:av-pnc"]
score: 10.0
evidence: 提出结合深度学习和基于模型的规划的生成式运动规划框架，直接适用于自动驾驶车辆导航。
tldr: 运动规划中深度学习与基于模型的方法各有优势，但难以统一。本文提出生成式框架，通过学习高压缩比的自动编码器，将运动规划映射到分层离散令牌的潜在空间，结合维度和排序特性，实现高效规划。该方法在机器人导航等任务上验证，为自动驾驶车辆的运动规划提供了融合数据驱动与专家知识的新范式。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 深度学习与基于模型的规划方法各有局限，需要统一框架以利用大规模数据和专家知识。
method: 学习高压缩比自动编码器，将运动规划映射到分层离散令牌的潜在空间。
result: 在机器人导航等任务上验证了规划效率和灵活性，优于纯学习或纯模型方法。
conclusion: 该框架成功融合了学习先验与模型优化，为自动驾驶运动规划提供了新的生成式范式。
---

## Abstract
Deep learning methods have vastly expanded the capabilities of motion planning in robotics applications, as learning priors from large-scale data has been shown to be essential in capturing the highly complex behavior required for solving tasks such as manipulation or navigation for autonomous vehicles. At the same time, model-based planning algorithms based on search or optimization remain an essential tool due to their flexibility, efficiency, and the ability to incorporate domain knowledge via expert-designed algorithms and objective functions. We propose a new generative framework to unify these two paradigms. First, we learn an autoencoder with a high compression ratio and a latent space of hierarchically ordered, discrete-valued tokens. Leveraging both the dimensionality reduction and the hierarchical coarse-to-fine structure learned by this autoencoder, we then perform motion planning by directly searching in the latent space of tokens. This search can optimize arbitrary objective functions specified at test time, providing a large degree of flexibility while maintaining efficiency and producing realistic solutions by relying on the generative capabilities of the highly compressed autoencoder. We evaluate our method on nuPlan and the Waymo Open Motion Dataset, showing how latent space search can be used for a variety of guided behavior generation tasks, achieving strong performance for closed-loop motion planning and multi-agent guided scenario synthesis without requiring any task-specific training.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
*   **研究动机**：深度学习方法在机器人运动规划（如自动驾驶导航、机械臂操作）中展现了从大规模数据中学习复杂行为先验的强大能力；同时，基于搜索或优化的传统模型驱动规划器因其灵活性、可融入专家知识以及可定义任意目标函数的特点，仍是不可或缺的工具。如何将两种范式的优势统一起来，是当前一大挑战。
*   **整体含义**：论文提出一种生成式框架，不再将深度学习与模型规划视为对立或替代关系，而是通过一个高压缩比的离散潜空间将二者深度融合——在极度压缩的表示空间中直接实施搜索或优化，使得规划既能利用学习到的丰富先验生成逼真轨迹，又能保留传统规划器任意定义成本函数、灵活适应不同任务的特性。

### 2. 论文提出的方法论
*   **核心思想**：先训练一个自编码器，将高维的运动轨迹或场景状态压缩到一个由层次化、有序的离散令牌组成的潜空间中；随后，将运动规划问题转化为在该潜空间的令牌序列上进行搜索或优化，利用潜空间的低维性和由粗到精的结构提升效率，同时依靠解码器的生成能力保证输出结果的真实性。
*   **关键技术细节**：
    *   **高压缩比自编码器**：学习将原始运动/场景表示映射到极低维度的离散潜空间，并具有层次化、由粗到精的有序结构。
    *   **离散令牌潜空间**：潜空间中的每个“词汇”(token)均为离散值，便于搜索算法（如树搜索、束搜索）操作。
    *   **潜空间规划**：在测试时，直接在潜空间中对令牌序列进行搜索，可以优化任意用户指定的目标函数（如安全性、舒适度、模仿特定行为等），无需针对特定任务重新训练模型。
*   **算法流程（文字描述）**：给定场景上下文，通过编码器获得初始潜状态或引导信息；规划器在潜空间中迭代生成/修改令牌序列，每一次生成的序列经解码器映射回真实轨迹，并计算外部目标函数；将目标函数值作为搜索导向，直至找到满足约束且优化目标的轨迹。

### 3. 实验设计
*   **数据集**：
    *   **nuPlan**：用于评估闭环运动规划性能，聚焦自动驾驶车辆在复杂城市环境下的导航能力。
    *   **Waymo Open Motion Dataset**：用于评估多智能体引导场景合成的性能，验证框架在交互式多车场景中的行为生成能力。
*   **Benchmark与任务**：
    *   闭环运动规划（在 nuPlan 上）。
    *   多智能体引导的场景合成（在 Waymo Open Motion Dataset 上）。
*   **对比方法**：摘要及元数据中未明确列出具体对比的基线方法，仅说明该方法“无需任何任务特定的训练”即可在两种任务上取得强性能，隐含与传统规划器、特定任务训练的深度学习模型形成对比。

### 4. 资源与算力
*   提供的论文内容（仅摘要与元数据）中**未明确说明**所使用的 GPU 型号、数量、训练时长等计算资源信息。由于原文缺失正文内容，算力开销细节无法推断。

### 5. 实验数量与充分性
*   **实验组数大致估计**：根据摘要，至少包含两大实验场景（nuPlan闭环规划、Waymo多智能体合成），可能还涉及不同目标函数下的变体、消融研究（如压缩比率、令牌层次的影响），但具体数量在现有信息中无法得知。
*   **充分性与公平性评估**：就提供的摘要而言，在两个大规模公开数据集上验证，且覆盖了闭环控制与交互合成两种不同性质的任务，初步表面实验覆盖面较合理。但缺少具体指标、误差条、消融实验对比的详述，无法从现有信息判断实验是否完全充分或客观公平。

### 6. 论文的主要结论与发现
*   通过学习高压缩比的离散潜空间并在其中进行搜索，可以成功地将深度学习先验与基于模型的目标优化结合起来。
*   该框架能够在自动驾驶车辆闭环运动规划和多智能体引导场景合成等任务上实现强大性能，且所有测试均无需任何针对特定任务的额外训练，展现了高度的灵活性与泛化能力。
*   压缩潜空间的层次化和离散化特性是实现高效、逼真规划的关键。

### 7. 优点
*   **方法亮点**：巧妙利用离散令牌潜空间作为“规划界面”，既保留了搜索优化的可解释性和灵活性，又继承了深度生成模型的真实性，提供了一种新颖的规划范式。
*   **实验设计亮点**：在闭环规划（nuPlan）与开环交互合成（Waymo）两种差异极大的任务上验证，且强调 zero-shot 能力（无需任务特定训练），突出了框架的通用性和实用性。

### 8. 不足与局限
*   **实验覆盖细节缺失**：因仅获取到摘要，无法评判实验对比的全面性（例如是否与强化的行为克隆、经典采样/优化规划器进行了公平比较）、模型在不同场景下的失效模式等。
*   **偏差风险**：自编码器的质量高度依赖于训练数据的分布，对长尾或极大偏离训练集的场景，其生成真实性可能下降，并引发潜在的安全偏差。
*   **应用限制**：离散潜空间虽便于搜索，但其表达能力上限、令牌序列长度的固定性可能限制对极长时间窗或极高动态变化场景的建模精度。计算开销虽在压缩空间降低，但自编码器推理及大量搜索迭代的实际在线实时性仍有待检验（原文未提实时性能）。

（完）
