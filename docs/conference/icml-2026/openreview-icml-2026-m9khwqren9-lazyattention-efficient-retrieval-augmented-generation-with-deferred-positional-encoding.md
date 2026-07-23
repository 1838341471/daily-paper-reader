---
title: "LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding"
title_zh: LazyAttention：利用延迟位置编码的高效检索增强生成
authors: "Haocheng Xia, Mihir Pamnani, Hanxi Fang, Supawit Chockchowwat, Yongjoo Park"
date: 2026-04-30
pdf: "https://openreview.net/pdf/c4d825d653070733092c564642dc66ac6db18eb5.pdf"
tags: ["query:ad-rag"]
score: 4.0
evidence: 通过延迟位置编码实现RAG的高效KV缓存
tldr: 本文针对RAG长上下文推理中KV缓存位置编码限制重用的问题，提出LazyAttention。通过核化延迟位置编码实现位置无关的零拷贝KV复用，在在线重编码下提高效率。实验表明在长上下文场景中显著降低内存和计算开销，但未在自动驾驶领域测试。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有KV缓存嵌入位置信息，限制了在RAG中的重用，导致效率低下。
method: 提出LazyAttention注意力机制，通过核化延迟位置编码实现在线重编码和零拷贝复用。
result: 在长上下文推理中显著提高效率，降低内存开销。
conclusion: 该方法为非固定位置场景下的高效RAG推理提供了新途径。
---

## Abstract
Key-value (KV) caching accelerates inference of large language models (LLMs) by reusing past computations for generated tokens. Its importance becomes even greater in long-context applications such as retrieval-augmented generation (RAG) and in-context learning (ICL). However, conventional KV caching embeds positional information directly into the cache, limiting its reusability. Existing solutions either restrict reuse to prefixes or require expensive memory materialization for positional re-encoding. We introduce LazyAttention, a novel attention mechanism that kernelizes deferred positional encoding to enable zero-copy, position-agnostic KV reuse. By adjusting positional encoding within attention kernels on-the-fly, LazyAttention resolves the materialization bottleneck, allowing a single physical KV copy to serve multiple logical requests at arbitrary positions. Leveraging attention kernels tailored for prefilling and decoding, our system achieves significant efficiency improvements: under skewed document distributions, it reduces time-to-first-token (TTFT) by 1.37× and increases inference throughput by 1.40× compared to the state-of-the-art Block-Attention, while maintaining comparable output quality.

---

## 论文详细总结（自动生成）

# 论文总结：LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding（利用延迟位置编码的高效检索增强生成）

## 1. 核心问题与整体含义
- **研究背景**：KV（Key-Value）缓存通过重用已生成 token 的中间计算结果来加速大语言模型（LLM）推理，在检索增强生成（RAG）、上下文学习（ICL）等长上下文场景中尤为重要。
- **现有瓶颈**：传统 KV 缓存将位置编码直接嵌入缓存内容，导致缓存的**可重用性受限**。已有方案要么只能重用前缀部分，要么需要为位置重新编码而产生昂贵的显存物化（materialization）开销。
- **论文目标**：提出一种新型注意力机制 **LazyAttention**，实现位置无关、零拷贝的 KV 复用，从而在非固定位置的 RAG 推理中大幅提升效率。

## 2. 方法论
- **核心思想**：将位置编码“延迟”到注意力计算的内核中动态调整（deferred positional encoding），使同一份物理 KV 缓存可被多个不同位置的逻辑请求共享，无需复制或重新物化。
- **关键技术细节**：
  - 对延迟位置编码进行**核化（kernelize）**，将位置修正融合进注意力核（attention kernel）内部，在计算注意力分数时**在线（on-the-fly）**完成位置调整。
  - 实现**零拷贝（zero-copy）**与**位置无关（position-agnostic）**的 KV 复用：一份物理 KV 副本可以同时服务任意位置的多个请求，消除显存物化瓶颈。
  - 针对预填充（prefilling）和解码（decoding）阶段分别设计定制的注意力核，以进一步提升端到端效率。
- **流程概述**：预存 KV 缓存时不注入绝对位置，而在实际推理时，由 LazyAttention 核心动态向缓存注入相对或正确的绝对位置信息，使得同一缓存仿佛位于目标上下文的不同位置。

## 3. 实验设计
- **场景与数据集**：
  - 主要面向**长上下文 RAG**，实验在**文档分布倾斜（skewed document distributions）**的条件下评估。
  - 论文摘要未明确列出所用的具体数据集名称（如 NaturalQuestions、TriviaQA 等），亦未详细说明 RAG 检索库的构成。
- **基准与对比方法**：
  - 与最先进的方法 **Block-Attention** 进行对比。
  - 可能还涉及其他 KV 复用或位置编码方案，但摘要仅明确提及 Block-Attention。
- **评估指标**：
  - **TTFT（首 token 延迟）**：降低 1.37 倍。
  - **推理吞吐量（throughput）**：提升 1.40 倍。
  - **输出质量（output quality）**：与对比方法保持可比（comparable）。

## 4. 资源与算力
- **文中未提及**：摘要与提供的元数据中均未披露实验所使用的 GPU 型号、数量、训练/推理时的具体算力成本或时长。如需了解硬件开销，需要查阅论文正文。

## 5. 实验数量与充分性
- **已知实验组**：至少包含**长上下文 RAG 场景下与 Block-Attention 的效率对比**（TTFT 和吞吐量），以及**输出质量可比的验证**。
- **未充分展现的内容**：
  - 未说明是否在多种文档分布、多个数据集、不同模型规模下进行实验。
  - 未提供消融实验（例如，是否对比了无位置复用、其他位置编码策略等）。
  - 从摘要判断，实验广度有限，但**效率提升与质量保持的结论有定量支撑**。
- **公平性**：文中明确定义对比对象为当前 state-of-the-art，且在同等条件下测试，**具备基本客观性**。

## 6. 主要结论与发现
- LazyAttention 通过核化延迟位置编码，成功克服了 KV 缓存中位置信息嵌入导致的重用限制。
- 在长上下文 RAG 推理中，该方法**显著降低显存开销**、**提升推理效率**（TTFT 减少 1.37×，吞吐量提高 1.40×），且**输出质量不亚于现有方案**。
- 为“非固定位置”场景下的高效 RAG 推理（如动态插入多个文档片段）提供了**实用新范式**。

## 7. 优点（亮点）
- **方法论创新**：提出位置编码延迟与核化计算，从根本上解决了因位置固化带来的 KV 缓存复用难题。
- **零拷贝设计**：无需为不同位置复制缓存，极大降低显存占用和传输开销。
- **在线重编码**：将位置融合内化至注意力核，避免中间结果的昂贵物化。
- **实际性能提升显著**：在倾斜文档分布等真实 RAG 场景下，端到端效率增益明确。
- **解码与预填充协同优化**：针对性设计内核，兼顾计算与访存效率。

## 8. 不足与局限
- **实验覆盖有限**：
  - 摘要未提及具体数据集，重现性和拓展性存疑；实验可能仅局限于特定 RAG 数据构造。
  - 未展示在非 RAG 任务（如普通长文本生成、ICL 等）上的表现。
- **应用场景偏差风险**：
  - 强调“skewed document distributions”，在均匀分布或缓少许可复用性低的场景下收益可能不明显。
  - 摘要中未在自动驾驶等与 RAG 无关的领域进行测试（符合标签 `query:ad-rag` 暗示的自动驾驶 RAG 方向，但实际未覆盖自动驾驶评测）。
- **对比方法单一**：仅明确对比 Block-Attention，缺少与更多位置复用策略（如 PagedAttention、位置无关缓存等）的全面比较。
- **质量评估细节不明**：输出质量“comparable”缺乏量化指标（如困惑度、任务准确率），无法评估微小的质量折损。
- **系统实现复杂性**：核化延迟编码可能需要特定硬件/算子支持，对部署通用性提出要求，但未讨论。

（完）
