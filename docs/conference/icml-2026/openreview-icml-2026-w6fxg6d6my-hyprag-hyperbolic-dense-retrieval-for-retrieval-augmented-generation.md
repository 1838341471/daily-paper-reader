---
title: "HypRAG: Hyperbolic Dense Retrieval for Retrieval Augmented Generation"
title_zh: HypRAG：用于检索增强生成的双曲密集检索
authors: "Hiren Madhu, Ngoc Bui, Ali Maatouk, Leandros Tassiulas, Smita Krishnaswamy, Menglin Yang, Sukanta Ganguly, Kiran Srinivasan, Rex Ying"
date: 2026-04-30
pdf: "https://openreview.net/pdf/861a9062f09a3b3fd1a76fd2a0b76289ba995aac.pdf"
tags: ["query:ad-rag"]
score: 4.0
evidence: 双曲密集检索用于RAG，非自动驾驶专用
tldr: 本文针对RAG密集检索局限于欧几里得空间、无法保留层次语义的问题，引入双曲密集检索。在洛伦兹空间构建全双曲变换器和混合架构，捕获文本层次结构。实验表明检索质量优于欧几里得基线，降低幻觉风险，但未在自动驾驶场景验证。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有密集检索器局限于欧几里得空间，无法捕获自然语言层次结构，导致语义相似文档被错误关联。
method: 引入双曲密集检索，在洛伦兹空间构建全双曲变换器HyTE-FH和混合架构HyTE-H。
result: 在多个基准上检索质量优于欧几里得基线，降低幻觉风险。
conclusion: 双曲几何为RAG检索提供了更适合层次化语义的表示空间。
---

## Abstract
Embedding geometry plays a fundamental role in retrieval quality, yet dense retrievers for retrieval-augmented generation (RAG) remain largely confined to Euclidean space. However, natural language exhibits hierarchical structure from broad topics to specific entities that Euclidean embeddings fail to preserve, causing semantically distant documents to appear spuriously similar and increasing hallucination risk. To address these limitations, we introduce hyperbolic dense retrieval, developing two model variants in the Lorentz model of hyperbolic space: HyTE-FH, a fully hyperbolic transformer, and HyTE-H, a hybrid architecture projecting pre-trained Euclidean embeddings into hyperbolic space. To prevent representational collapse during sequence aggregation, we introduce the Outward Einstein Midpoint, a geometry-aware pooling operator that provably preserves hierarchical structure. On MTEB, HyTE-FH outperforms equivalent Euclidean baselines, while on RAGBench, HyTE-H achieves up to 29\% gains over Euclidean baselines in context relevance and answer relevance using substantially smaller models than current state-of-the-art retrievers. Our analysis also reveals that hyperbolic representations encode document specificity through norm-based separation—with over 20\% radial increase from general to specific concepts—a property absent in Euclidean embeddings, underscoring the critical role of geometric inductive bias in faithful RAG systems. The code is available at: https://github.com/Graph-and-Geometric-Learning/HypRAG

---

## 论文详细总结（自动生成）

# HypRAG: 用于检索增强生成的双曲密集检索 论文总结

## 1. 核心问题与整体含义

- **研究背景**：在检索增强生成（RAG）中，嵌入空间的几何性质对检索质量至关重要。目前主流的密集检索器几乎全部在欧几里得空间中构建嵌入表示。
- **核心问题**：自然语言具有天然的层次结构（从宽泛主题到具体实体），而欧几里得嵌入无法有效保持这种层次语义，导致原本语义距离较远的文档被错误地拉近，进而增大生成幻觉的风险。
- **整体含义**：本文提出将密集检索从欧几里得空间迁移到双曲空间（洛伦兹模型），利用双曲几何对层次结构的天然表达能力，提升语义检索的保真度，从而构建更可信的 RAG 系统。

## 2. 方法论

- **核心思想**：将文本的层次化语义编码到双曲空间，使概念的泛化-特化关系通过嵌入的“径向范数”自然分离开来。
- **双曲空间选择**：采用洛伦兹模型作为双曲几何的实现载体。
- **两种模型架构**：
  - **HyTE‑FH（全双曲 Transformer）**：在洛伦兹空间中完全重新设计 Transformer 组件，使所有运算都具有双曲几何保真性。
  - **HyTE‑H（混合架构）**：将预训练的欧几里得嵌入投影到双曲空间，在不完全抛弃成熟预训练模型的前提下融入双曲归纳偏置。
- **关键算子：Outward Einstein Midpoint（外推爱因斯坦中点）**
  - **问题**：序列聚合时，若直接使用常规中点或平均池化，容易导致表示坍缩，破坏层次结构。
  - **创新**：提出具有几何感应的池化算子，在洛伦兹空间中向外推定中点，从理论上证明能够保持层次化的结构信息，避免表示退化。
- **算法流程（概要）**：
  1. 输入文本经编码器获得中间表示；
  2. 对于 HyTE‑FH，全程在洛伦兹空间进行计算；对于 HyTE‑H，先将欧氏嵌入按指数映射投影到洛伦兹空间；
  3. 使用 Outward Einstein Midpoint 对序列维度进行聚合，得到文档/查询的最终双曲嵌入；
  4. 在双曲空间中利用双曲距离度量进行相似度排序，完成检索。

## 3. 实验设计

- **数据集与 Benchmark**：
  - **MTEB**（Massive Text Embedding Benchmark）：用于评估通用文本嵌入的检索质量。
  - **RAGBench**：专为 RAG 场景设计的基准，涵盖上下文相关性和答案相关性等维度。
- **对比方法**：
  - 等价的欧几里得基线模型（相同参数量级、相同架构的欧氏密集检索器）。
  - 当前最先进的检索器（SOTA retrievers），且 HyTE‑H 在模型规模明显更小的情况下进行对比。
- **评估指标**：检索质量、上下文相关性、答案相关性，以及抗幻觉能力的间接衡量。

## 4. 资源与算力

- 论文摘要及元数据中**未明确提及**具体的 GPU 型号、数量或训练时长。
- 仅能从描述中推断，HyTE‑H 使用的模型规模比 SOTA 检索器“显著更小”，说明其计算开销相对可控，但精确算力数据需查阅原文完整版本。

## 5. 实验数量与充分性

- **实验组数**：
  - 在 MTEB 上比较 HyTE‑FH 与欧几里得基线。
  - 在 RAGBench 上比较 HyTE‑H 与欧几里得基线及多组 SOTA 方法。
  - 额外进行了分析性实验：验证双曲嵌入中“径向范数”与概念特异性之间的对应关系（声称有超过20%的径向增长从一般概念到具体概念）。
- **充分性与客观性**：
  - 覆盖了通用文本检索与 RAG 特定检索两类主流基准，评估维度较全面。
  - 对比了等量级的欧氏模型和更大型的外部 SOTA 模型，考虑了对规模公平性的控制。
  - 消融/分析实验验证了层次结构保留的几何解释，增强了方法论的说服力。
  - 总体实验体系较为充分，但未披露训练稳定性、对超参的敏感度等更细粒度的消融。

## 6. 主要结论与发现

- HyTE‑FH 在 MTEB 上的检索性能优于同规模的欧几里得基线，证明全双曲编码器在通用检索任务上的竞争力。
- HyTE‑H 在 RAGBench 上取得大幅提升，上下文相关性和答案相关性指标最多超过欧几里得基线 29%，且模型规模远小于 SOTA 检索器。
- 双曲嵌入通过范数实现了对文档特异性的自然编码：从一般性概念到具体概念，径向距离增加超过20%，这是欧氏嵌入所不具备的特性。
- 几何归纳偏置（双曲空间的层次保持性质）对于减少幻觉、增强 RAG 系统的可信度具有关键作用。

## 7. 优点

- **几何创新**：首次将双曲空间密集检索系统性地引入 RAG 场景，并提出两种互补的架构，兼顾几何一致性与工程可行性。
- **理论支撑**：Outward Einstein Midpoint 具备可证明的层次保持性质，为双曲池化提供了扎实的理论基础。
- **效果显著**：在 RAGBench 上相对于欧氏基线的提升幅度大（最高29%），且模型更轻量，实用性突出。
- **可解释性强**：通过径向范数分析，直观展示了双曲嵌入如何自然建模文本的层级特异性，增强了方法的透明性。

## 8. 不足与局限

- **算力信息缺失**：未公开具体的训练资源需求和耗时，复现与成本评估存在困难。
- **未在自动驾驶或其他垂直领域验证**：论文聚焦文本检索，虽然出自自动驾驶相关检索，但未在自动驾驶的实际 RAG 场景中测试，泛化性有待进一步检验。
- **混合架构的依赖**：HyTE‑H 仍依赖欧氏预训练模型，其最终表示的双曲结构可能受预训练质量的制约，全双曲版本 HyTE‑FH 的训练稳定性和可扩展性尚未充分展示。
- **实验覆盖可能不足**：虽然基准较权威，但缺乏对超长文档、多语言、实时流式场景的评估，也未讨论双曲空间计算带来的推理延迟。
- **偏差风险**：未提及用于训练或评估的数据集是否存在特定领域的偏差，也未分析双曲嵌入对边缘群体或低资源语言的公平性。

（完）
