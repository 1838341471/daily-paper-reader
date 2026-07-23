---
title: "Retriever Portfolios: A Principled Approach to Adaptive RAG"
title_zh: 检索器投资组合：面向自适应RAG的原则性方法
authors: "Miltiadis Stouras, Vincent Cohen-Addad, Silvio Lattanzi, Ola Svensson"
date: 2026-04-30
pdf: "https://openreview.net/pdf/fca390c3d22e4bfe5d97590506e68b7db1c0559f.pdf"
tags: ["query:ad-rag"]
score: 4.0
evidence: RAG自适应多检索器选择，非驾驶专用
tldr: 本文针对RAG单一检索器难以应对异质查询的问题，提出基于预期收益目标的检索器组合选择算法。学习多样化子集并训练路由模型，实现自适应检索。在QA基准上超越基线，但未在自动驾驶RAG中验证。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: RAG系统通常使用单一检索器，难以应对从简单到复杂的异质查询。
method: 提出基于预期最优k收益目标的检索器组合选择算法，并学习路由模型。
result: 在多项QA基准上超越单一检索器和简单多检索器组合。
conclusion: 自适应检索器组合能显著提升RAG系统性能，为最优检索策略学习提供理论保证。
---

## Abstract
Retrieval-augmented generation (RAG) systems typically rely on a single
retriever and a single set of hyperparameters, despite facing highly
heterogeneous queries that range from simple factoid questions to complex
multi-hop reasoning. We propose a method that automatically selects a small, 
diverse subset of retrievers (a portfolio) from a large pool of candidates, to cover 
different regions of the target query distribution.
We formalize this setting via an expected best-of-$k$ objective over 
the query distribution and show that it admits an efficient portfolio construction 
algorithm with near-optimal guarantees. Across multiple QA benchmarks, our learned
portfolios and router pipeline consistently outperform
single-retriever and naive multi-retriever baselines on both retrieval metrics and answer quality. 
In addition, compared to inference-time hyperparameter tuning approaches, fixed portfolios 
enable parallel retrieval and LLM calls, achieving comparable (and sometimes better) accuracy 
with substantially lower latency and token cost.

---

## 论文详细总结（自动生成）

# 论文总结：检索器投资组合：面向自适应RAG的原则性方法

## 1. 论文的核心问题与整体含义

- **核心问题**：检索增强生成（RAG）系统通常依赖单一的检索器及一组固定的超参数，而实际查询的异质性极强（从简单的事实性问题到复杂的多跳推理）。单一检索器难以在所有查询类型上均表现良好。
- **整体含义**：提出一种原则性方法，从大量候选检索器中自动构建一个“检索器投资组合”（即一个多样化的检索器子集），并训练一个路由模型将每个查询动态分配给组合中最合适的检索器，从而实现自适应RAG，同时兼顾检索精度、答案质量与系统效率。

## 2. 论文提出的方法论

- **核心思想**：
  - 将检索器选择形式化为一个在查询分布上的“期望最优$k$收益”优化问题（expected best-of-$k$ objective）。
  - 不是为每个查询单独选择检索器，而是预先构造一个固定的小型检索器组合，使该组合整体在查询分布上覆盖不同的“能力区域”。
- **关键技术细节**（基于摘要及元数据提炼）：
  - **组合构建算法**：针对期望最优$k$目标，设计了一种高效的组合选择算法，能够从大规模候选池中挑选出小规模、多样化的检索器子集，并具有近似最优的理论保证。
  - **路由模型**：学习一个路由器（router），将每个输入查询动态映射到组合中最合适的检索器，实现自适应调度。
  - **推理并行化**：因组合固定，可并行调用多个检索器（及后续的LLM），相比于推理时动态调优的方法，显著降低延迟与token消耗。
- **算法流程**（文字概括）：
  1. 定义查询分布与候选检索器集合。
  2. 优化期望最优$k$收益目标，输出一个包含$k$个检索器的投资组合。
  3. 利用标注数据或代理信号训练一个查询-检索器路由模型。
  4. 推理时，新查询经过路由模型分派至一个或多个检索器，并行执行检索。

## 3. 实验设计

- **数据集/场景**：多项问答（QA）基准（具体数据集名称未在摘要中公开，根据常见RAG评估可能包含Natural Questions、HotpotQA等，但原文未明确说明）。
- **对比方法**：
  - 单一检索器基线。
  - 朴素的（naive）多检索器组合方法。
  - 推理时超参数调优方法（如每个查询实时选择最佳检索器或配置）。
- **评估指标**：检索指标（如召回率、精确率）与答案质量（如生成答案的准确性）。

## 4. 资源与算力

- 论文摘要及提供的元数据中**未提及**任何关于GPU型号、数量、训练时长或算力消耗的信息。本次分析无法提供相关细节。

## 5. 实验数量与充分性

- **实验组数**：摘要中仅提及“多项QA基准”，未说明具体数据集数量、消融实验设置等。从“consistently outperform”等用语推断至少覆盖了多个主流数据集和多种变体，但无法精确统计。
- **充分性与客观性**：
  - 对比了单一检索器、朴素多检索器组合以及推理时调优方法，基线较为全面。
  - 在检索指标和答案质量两个层面进行评估，考虑维度较完整。
  - 缺乏特定领域（如自动驾驶RAG、法律、医疗等）的验证，通用性边界尚未探明。
  - 补充性分析（如组合大小$k$的影响、路由模型精度、消融研究）是否完备，原文无法确认。

## 6. 论文的主要结论与发现

- 学习到的检索器投资组合搭配路由模型，能够在检索指标和生成答案质量上稳定超越单一检索器及简单的多检索器方案。
- 固定组合支持并行检索和LLM调用，相比推理时动态超参数调优方法，能在取得相当（甚至更优）精度的同时，大幅降低延迟和token成本。
- 所提出的组合选择算法具有近似最优的理论保证，为检索策略的自动化学习提供了坚实的数学基础。

## 7. 优点

- **原则性**：将多检索器选择建模为带有理论保障的优化问题，而非启发式拼凑。
- **效率与性能兼顾**：通过固定组合与并行机制，实现高精度与低延迟的平衡，具有实际部署价值。
- **自适应性**：通过路由模型使系统自动适应查询的异质性，规避了手工设计规则或单检索器力不能及的缺陷。
- **清晰的实验设计**：与强基线（含推理时调优）比较，验证了方法的优势。

## 8. 不足与局限

- **实验覆盖有限**：未在非QA类RAG任务（如摘要、对话、代码生成）或专门领域（如自动驾驶、科学文献）中验证，可用性范围尚不明确。
- **偏差风险**：候选检索器池的构建方式、训练数据分布可能影响组合的泛化能力；路由模型的训练也可能引入额外偏差。
- **实现复杂度**：需要维护多个检索器并训练路由模型，与极简的单检索器系统相比，首次搭建成本更高。
- **理论假设的适用性**：期望最优$k$目标依赖于对查询分布的准确建模，分布漂移或非平稳场景下的鲁棒性未提及。
- **资源信息缺失**：未报告训练和推理的算力成本，不便进行成本效益评估。

（完）
