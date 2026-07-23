---
title: Information Flow Reveals When to Trust Language Models
title_zh: 信息流揭示何时信任语言模型
authors: "Rui Xu, Yi Chen, Jiujiu Chen, Sihong Xie"
date: 2026-04-30
pdf: "https://openreview.net/pdf/9e5c51b770ffeed01e47c4d228504b941d795e0f.pdf"
tags: ["query:ad-rag"]
score: 5.0
evidence: 通过信息流分析上下文基础来量化RAG不确定性
tldr: 利用信息流构建逐层上下文中token贡献的追踪，为RAG系统中的上下文基础提供可解释的不确定性估计，帮助判断何时信任语言模型输出。（通用RAG方法，可提高自动驾驶RAG系统的可信度）
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: RAG中模型可能未利用相关证据而生成错误回答，需要评估上下文基础的可靠性。
method: 提出基于信息流的逐层追踪方法，量化每个上下文token对输出的贡献。
result: 提供可解释的不确定性估计，有效判断生成答案是否基于检索内容。
conclusion: 为RAG系统的可信度评估提供了新视角，有助于检测错误答案。
---

## Abstract
In retrieval-augmented generation, language models can generate incorrect responses if they fail to utilize query-relevant content from the retrieved evidence. This shifts the focus of uncertainty quantification (UQ) toward assessing contextual grounding, i.e., whether predictions are supported by query-relevant tokens. Recent UQ methods unpack language models to characterize how inputs are processed. Nevertheless, these methods focus on a few layers and overlook the whole progressive propagation within the model, thereby failing to fully capture the grounding dynamics essential for reliable uncertainty estimation. We use information flow to build a layer-wise trace that reveals each context token’s contribution to the output, providing an interpretable basis for assessing reliability. From this analysis, we introduce two measures to calibrate prediction confidence. The first, \textit{simulatability}, posits that a prediction is more likely to be correct when context token contributions align closely with their true relevance. The second, \textit{concentration}, asserts that a response is more likely to be correct when it is derived from a narrow, focused subset of tokens. Experiments show that our method achieves an average AUROC of 0.709, exceeding the runner-up performance of 0.676, while maintaining moderate computational cost.

---

## 论文详细总结（自动生成）

很抱歉，您提供的“论文 PDF 提取文本”仅包含一个浏览器验证页面的提示信息（如“Complete the check below to continue to OpenReview”），并未包含论文的真实内容。因此，无法基于该内容生成所需的结构化中文总结。建议您重新提取或提供完整的论文文本，以便进行后续分析。

（完）
