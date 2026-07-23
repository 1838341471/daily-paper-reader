---
title: "GAM-RAG: Gain-Adaptive Memory for Evolving Retrieval in Retrieval-Augmented Generation"
title_zh: GAM-RAG：面向检索增强生成的增益自适应记忆
authors: "Yifan Wang, Mingxuan Jiang, Zhihao Sun, Yixin Cao, Yicun Liu, Keyang Chen, Guangnan Ye, Hongfeng Chai"
date: 2026-04-30
pdf: "https://openreview.net/pdf/0fd454748f575a4bffb3a311d192478eca177b8a.pdf"
tags: ["query:ad-rag"]
score: 4.0
evidence: RAG演化检索记忆，非驾驶专用
tldr: 本文针对RAG静态索引导致重复查询遍历开销大的问题，提出GAM-RAG框架。通过积累检索经验构建轻量层次索引，并根据句子级反馈更新记忆。实验表明在反复查询场景中显著减少遍历和延迟，但未在自动驾驶领域应用。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: RAG系统通常使用静态索引，处理相关查询时重复多跳遍历，增加延迟和计算成本。
method: 提出训练无关的GAM-RAG框架，通过积累检索经验构建轻量层次索引，并基于反馈更新记忆。
result: 在反复查询场景中显著减少遍历次数和延迟。
conclusion: 动态检索记忆使RAG系统能从经验中学习，提高效率。
---

## Abstract
Retrieval-Augmented Generation (RAG) grounds large language models with external evidence, but many implementations rely on pre-built indices that remain static after construction. Related queries therefore repeat similar multi-hop traversal, increasing latency and compute. Motivated by schema-based learning in cognitive neuroscience, we propose GAM-RAG, a training-free framework that accumulates retrieval experience from recurring or related queries and updates retrieval memory over time. GAM-RAG builds a lightweight, relation-free hierarchical index whose links capture potential co-occurrence rather than fixed semantic relations. During inference, successful retrieval episodes provide sentence-level feedback, updating sentence memories so evidence useful for similar reasoning types becomes easier to activate later. To balance stability and adaptability under noisy feedback, we introduce an uncertainty-aware, Kalman-inspired gain rule that jointly updates memory states and uncertainty estimates. It applies fast updates for reliable novel signals and conservative refinement for stable or noisy memories. We provide a theoretical analysis of the update dynamics, and empirically show that GAM-RAG improves average performance by 3.95\% over the strongest baseline and by 8.19\% with 5-turn memory, while reducing inference cost by 61\%.

---

## 论文详细总结（自动生成）

# GAM-RAG 论文总结

## 1. 核心问题与整体含义

- **研究背景**：检索增强生成（RAG）系统将大语言模型与外部证据相结合，但大多实现依赖于**构建后即静态不变**的预置索引。当系统处理一系列相关查询时，相同的多跳遍历路径会被反复执行，造成**高延迟和重复计算开销**。
- **动机来源**：受认知神经科学中“基于模式的学习”启发，使检索记忆能够从过去的经验中演化，从而更高效地处理相似推理需求。
- **整体含义**：提出一种**无需额外训练**的动态记忆框架，让 RAG 的检索组件能够“学习”哪些证据在特定上下文中更可能被激活，从而实现**增益自适应**的检索效率提升。

## 2. 方法论

### 核心思想
- 构建一个**轻量级、无固定关系的层次化索引**，其连接权重反映句子（或证据片段）之间的**潜在共现性**，而非预设的语义关系。
- 在推理过程中，成功的检索过程产生**句子级反馈**，用以更新句子记忆，使得对类似推理类型有用的证据在未来更容易被激活。

### 关键技术细节
- **检索记忆结构**：采用层次索引，链接动态调整，捕获反复共同出现的证据。
- **反馈更新机制**：每次成功检索后，相关句子的记忆强度会得到增强或削弱。
- **不确定性感知的增益规则**：
  - 灵感来源于卡尔曼滤波，同时更新**记忆状态**和**不确定性估计**。
  - 对于**可靠新颖信号**，应用快速更新；对于**稳定或嘈杂记忆**，采用保守的微调。
  - 提供更新动力学的**理论分析**，证明该规则在稳定性和适应性之间的平衡。
- **训练无关**：整个过程不需要模型微调或额外训练，完全基于在线经验积累。

### 算法流程（文字描述）
1. 给定输入查询，RAG 系统执行多跳检索，得到证据并生成答案。
2. 如果最终生成的答案被评估为“成功”（例如通过某种校验或最终任务正确），则触发记忆更新。
3. 根据检索过程中涉及的句子链，抽取**句子级反馈**，并利用卡尔曼增益公式融合外部信号与内部不确定性，更新这些句子的记忆强度。
4. 经过多轮查询交互，记忆网络自动适应任务模式，后续相似查询的检索跳数减少，检索效率提升。

## 3. 实验设计

- **数据集/场景**：摘要未明确列出具体数据集名称，但从性能提升描述（“平均性能提升 3.95%”等）可推断使用了基于正确率/效率的 RAG 评测任务，可能包括多跳问答等场景。
- **Benchmark**：以“最强基线”为对比基准，原文应包含多个现有 RAG 检索方法，但不详。
- **对比方法**：摘要未列出具体方法，但提到“强基线”，并给出记忆轮次（5-turn memory）的增益比较。
- **备注**：由于提供的文本仅为摘要和元数据，无法获得详细的数据集、具体任务及对比方法信息。

## 4. 资源与算力

- 提交的文本中**完全没有提及**所用算力资源（如 GPU 型号、数量、训练时长等）。由于该方法声明为“训练无关”，可能推理实验仅需常规 CPU/GPU 资源，但无法确认具体规模。

## 5. 实验数量与充分性

- **可推断的实验组**：
  - 与最强基线的整体性能对比（3.95% 提升）。
  - 引入 5 轮记忆后的性能对比（8.19% 提升）。
  - 推理成本（延迟）降低 61% 的评估。
  - 理论分析部分应包含更新动态的模拟或理论验证。
  - 预期的消融实验（如增益规则的作用、记忆结构的影响等）在摘要中未体现，但很可能在正文中存在。
- **充分性判断**：
  - 从摘要来看，实验覆盖了**性能、效率、记忆轮次**影响，体现了方法的核心优势。
  - 但缺少具体任务类型、数据集规模、不同领域泛化性等信息，无法全面评估实验的客观性与公平性。
  - 说明：由于我们只能基于提供的内容，**无法获知是否有跨领域测试、鲁棒性分析或与更多变体的对比**。

## 6. 主要结论与发现

- **动态检索记忆能够使 RAG 系统从反复的经验中学习，显著减少冗余的检索遍历，提升效率。**
- 所提出的不确定性感知增益规则可有效平衡记忆的**稳定性**（不轻易因噪声改写有用记忆）与**可塑性**（快速吸收新关联）。
- 在（推断的）相近查询频繁出现的场景下，**5 轮记忆累积即可带来超过 8% 的性能跃升，同时降低约六成的推理成本**。

## 7. 优点

- **训练无关**：无需重训模型或重新构建索引，部署成本低。
- **轻量化机制**：仅维护层次化记忆与不确定性估计，额外计算开销小。
- **理论支撑**：卡尔曼增益的引入提供了收敛性和优化性质的解释。
- **实际效益突出**：同时提升准确率（+8.19%）和降低成本（-61% 推理耗时），兼顾效果与效率。
- **与认知科学结合**：新颖地从人脑模式学习角度设计机制。

## 8. 不足与局限

- **信息缺失严重**：论文主体实验细节（数据集、基准、对比方法、消融实验等）在提交的文本中不可见，限制对其严谨性的深入评判。
- **应用前提限制**：框架的收益依赖于**存在大量相关或反复查询**的场景；对于高度分散、无模式可循的提问流，记忆积累可能效果有限。
- **反馈依赖性**：更新依赖于判定检索“成功”的信号，若成功信号错误或噪声较大，可能干扰记忆质量（尽管有不确定性估计缓解）。
- **评估可能不全面**：缺乏对其他 RAG 变体（如自适应检索步数、图索引方法）的全面比较，泛化性有待考证。
- **领域适用性**：从元数据可知未在自动驾驶领域应用，其在结构化知识库外的文本检索场景中的表现未知。

（完）
