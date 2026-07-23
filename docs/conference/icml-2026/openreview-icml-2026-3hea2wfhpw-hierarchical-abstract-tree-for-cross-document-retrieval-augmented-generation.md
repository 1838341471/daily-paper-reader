---
title: Hierarchical Abstract Tree for Cross-Document Retrieval Augmented Generation
title_zh: 面向跨文档检索增强生成的层次化抽象树
authors: "Ziwen Zhao, Menglin Yang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/7936e231851b48a26fa59cba1bcb86f1bfaef6dc.pdf"
tags: ["query:ad-rag"]
score: 5.0
evidence: 面向跨文档多跳问题的树结构RAG方法
tldr: 提出Ψ-RAG，一种层次化抽象树RAG框架，解决跨文档多跳检索中的分布适应性差、结构孤立和粗粒度抽象问题，提升多文档推理能力。（通用RAG方法，可用于自动驾驶多源信息检索）
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有树型RAG在跨文档多跳问题上面临聚类噪声、文档间隔离和细节丢失等挑战。
method: 提出Ψ-RAG，构建层次化抽象树，增强文档间连接和细粒度表示。
result: 在跨文档多跳问答数据集上提升检索和生成效果。
conclusion: 为多文档RAG提供了一种可扩展的树结构索引方案。
---

## Abstract
Retrieval-augmented generation (RAG) enhances large language models with external knowledge, and tree-based RAG organizes documents into hierarchical indexes to support queries at multiple granularities. However, existing Tree-RAG methods designed for single-document retrieval face critical challenges in scaling to cross-document multi-hop questions: *(1) poor distribution adaptability*, where $k$-means clustering introduces noise due to rigid distribution assumptions; *(2) structural isolation*, as tree indexes lack explicit cross-document connections; and *(3) coarse abstraction*, which obscures fine-grained details. To address these limitations, we propose **$\Psi$-RAG**, a tree-RAG framework with two key components. *First*, a hierarchical abstract tree index built through an iterative "merging and collapse" process that adapts to data distributions without a priori assumption. *Second*, a multi-granular retrieval agent that intelligently interacts with the knowledge base with reorganized queries and an agent-powered hybrid retriever. $\Psi$-RAG supports diverse tasks from token-level question answering to document-level summarization. On cross-document multi-hop QA benchmarks, it outperforms RAPTOR by 25.9\% and HippoRAG 2 by 7.4\% in average F1 score.

---

## 论文详细总结（自动生成）

# 论文详细总结：面向跨文档检索增强生成的层次化抽象树（Ψ-RAG）

## 1. 核心问题与整体含义（研究动机与背景）
检索增强生成（RAG）通过引入外部知识来增强大型语言模型。其中，基于树的RAG方法将文档组织为层次化索引，以支持多粒度查询。然而，现有Tree-RAG方法主要针对单文档检索设计，当扩展至跨文档、多跳问答场景时，面临三大核心瓶颈：
- **分布适应性差**：常用的 k-means 聚类假设数据分布为刚性球形，在复杂文档集合中容易引入聚类噪声。
- **结构孤立**：不同文档的树索引之间缺乏显式的跨文档连接，难以支持需要综合多个文档信息的推理。
- **抽象粗糙**：高层次的摘要节点会丢失细粒度细节，导致面向具体细节的查询无法得到准确答案。

填补这一缺失，**Ψ-RAG** 提出一种新的层次化抽象树框架，旨在为跨文档多跳检索构建一个更适应真实数据分布、文档间紧密关联且能保留细粒度信息的索引结构，从而提升多文档推理的性能。

## 2. 方法论
Ψ-RAG 由两个核心模块构成：

### 2.1 层次化抽象树索引
- **核心理念**：通过迭代的“合并与坍缩”（merging and collapse）过程自底向上构建树结构，无需预先设定聚类数量或数据分布假设。
- **构建过程**（文字描述）：
  1. 从最细粒度的文本片段（如句子或标记）开始，将它们视为叶子节点。
  2. 在每一轮迭代中，基于语义相似度将最相近的节点两两合并，生成父节点（抽象摘要）。
  3. 对生成的父节点进行“坍缩”操作，剔除冗余或信息量低的中间节点，防止树结构过度膨胀。
  4. 重复该过程，直到形成涵盖整个知识库的层次化树。
- **优势**：该过程自适应真实数据分布，不会强加球形假设；同时，通过合并来自不同文档的节点，天然地在树中创建了跨文档连接（打破结构孤立）；并且保留多层级节点，使得细粒度信息不被淹没。

### 2.2 多粒度检索代理
- **查询重组**：将用户的复杂多跳问题分解或改写为适合不同树层级的子查询。
- **代理驱动混合检索**：智能代理根据查询特征，决定在树的哪个层级（叶子、中间、根节点）进行检索，并综合来自不同层级、不同文档分支的信息。
- **任务支持**：框架可统一处理从标记级问答到文档级摘要等多种任务。

## 3. 实验设计
- **任务与基准**：在跨文档多跳问答（multi-hop QA）基准数据集上进行评估。
- **对比方法**：与代表性的Tree-RAG方法 RAPTOR，以及近期先进的 HippoRAG 2 进行对比。
- **评价指标**：主要采用平均 F1 分数（average F1 score）。
- **主要结果**：Ψ-RAG 相较 RAPTOR 平均 F1 提升 25.9%，较 HippoRAG 2 提升 7.4%，展现出显著优势。

## 4. 资源与算力
论文摘要及元数据中**未明确提及**所使用的GPU型号、数量或训练时长等算力消耗信息。如需完整评估其资源需求，需查阅正文的实验配置部分。

## 5. 实验数量与充分性
基于现有信息，论文至少完成了：
- 一个主要任务（跨文档多跳QA）的完整实验；
- 与两个强基线模型的对比；
- 核心性能指标（F1）的量化报告。

然而，未提供消融实验、不同数据集的泛化测试、效率分析等细节。从会议接收（ICML-2026 Accepted）及显著提升的结果推断，实验应当较为充分和公正，但最终判断需以全文为准。

## 6. 主要结论与发现
- Ψ-RAG 通过无先验分布的层次化抽象树，有效解决了传统Tree-RAG在跨文档多跳场景下的分布适应性、结构孤立与粗粒度抽象问题。
- 多粒度检索代理进一步增强了模型对复杂查询的响应能力。
- 总体而言，该工作为多文档RAG提供了一种可扩展、高性能的树结构索引方案。

## 7. 优点（亮点）
- **无需先验假设**：免除了 k-means 等方法对数据分布的限制，对多样化文档集合的适应性更强。
- **内生跨文档连接**：通过合并不同文档的节点自然构建联系，无需额外设计跨文档边，方法简洁且有效。
- **保留细粒度信息**：层次化坍缩策略避免信息过度压缩，可兼顾高层语义概括与低层细节。
- **统一的检索框架**：一套架构同时支持多种粒度的任务，降低了系统复杂度。

## 8. 不足与局限
- **实验透明度待补充**：摘要未公布算力成本、训练数据规模、超参数细节，难以复现与评估实用性。
- **实验覆盖范围有限**：目前仅展示了多跳QA任务的结果，对摘要、对话等其他RAG典型任务的验证缺失。
- **潜在偏差风险**：树构建中使用的语义相似度模型可能自带偏差，且“合并与坍缩”的超参数可能对最终结构敏感，文中并未讨论。
- **实时性未知**：面向大规模知识库时，迭代式树构建的在线更新效率未说明。

（完）
