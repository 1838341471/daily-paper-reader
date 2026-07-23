---
title: "RAG without Forgetting: Continual Query-Infused Key Memory"
title_zh: RAG不遗忘：持续查询注入的关键记忆
authors: "Yuntong Hu, Sha Li, Naren Ramakrishnan, Liang Zhao"
date: 2026-04-30
pdf: "https://openreview.net/pdf/014da7f78f2559372ce20ed814ed82657f6013d2.pdf"
tags: ["query:ad-rag"]
score: 4.0
evidence: RAG持续检索记忆，非驾驶专用
tldr: 本文针对RAG中查询适应状态无关、无法累积学习的问题，提出演化检索记忆框架ERM。将查询时增益转化为持久索引更新，通过反馈信号对齐任务效用。实验显示在多个任务上实现持续改进，但未涉及自动驾驶场景。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: RAG中的查询时适应（如查询扩展）是状态无关的，无法累积学习，且索引侧更新易引入噪声。
method: 提出演化检索记忆框架，将查询时增益转化为持久索引更新。
result: 在多个任务上实现持久检索改进，且无显著额外成本。
conclusion: ERM实现了RAG系统的持续自我优化。
---

## Abstract
Retrieval-augmented generation (RAG) systems commonly improve robustness via query-time adaptations such as query expansion and iterative retrieval. While effective, these approaches are inherently stateless: adaptations are recomputed for each query and discarded thereafter, precluding cumulative learning and repeatedly incurring inference-time cost. Index-side approaches like key expansion introduce persistence but rely on offline preprocessing or heuristic updates that are weakly aligned with downstream task utility, leading to semantic drift and noise accumulation. We propose Evolving Retrieval Memory (ERM), a training-free framework that transforms transient query-time gains into persistent retrieval improvements. ERM updates the retrieval index through correctness-gated feedback, selectively attributes atomic expansion signals to the document keys they benefit, and progressively evolves keys via stable, norm-bounded updates. We show that query and key expansion are theoretically equivalent under standard similarity functions and prove convergence of ERM’s selective updates, amortizing optimal query expansion into a stable index with zero inference-time overhead. Experiments on BEIR and BRIGHT across 13 domains demonstrate consistent gains in retrieval and generation, particularly on reasoning-intensive tasks, at native retrieval speed.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义
- **核心问题**：现有 RAG 系统的查询时适应（如查询扩展、迭代检索）是无状态的，每次查询重新计算、用完即弃，无法累积学习，导致重复的推理成本；而索引侧更新（如键扩展）虽能持久化，但依赖离线预处理或启发式更新，与下游任务效用对齐弱，容易引入语义漂移和噪声累积。
- **整体含义**：旨在将查询时的瞬时增益转化为持久的索引改进，使 RAG 系统能够像人类记忆一样持续优化自身，同时不增加推理时的额外开销，实现“不遗忘”的持续学习。

### 2. 论文提出的方法论
- **核心思想**：提出 **演化检索记忆（Evolving Retrieval Memory, ERM）**，一个免训练的框架，通过正确性门控反馈将查询时的原子扩展信号选择性归因到有帮助的文档键上，并利用稳定、范数有界的更新渐进地演化键向量，最终将最优查询扩展摊分到固定索引中。
- **关键技术细节**：
  - **正确性门控反馈**：仅当生成结果正确时，才触发对相关文档键的更新，避免错误信号污染。
  - **原子扩展信号归因**：将查询扩展拆解为原子单元，并只归因到那些从该扩展中受益的文档键，实现细粒度的选择性更新。
  - **稳定更新**：采用范数有界的更新规则，保证键向量在演化过程中不偏离语义太远，维持索引稳定性。
- **理论等价性与收敛性**：证明了在标准相似度函数下，查询扩展与键扩展在理论上是等价的，并证明了 ERM 的选择性更新能够收敛，将最优查询扩展摊分到稳定的索引中，实现零推理开销。

### 3. 实验设计
- **数据集与场景**：使用 **BEIR** 和 **BRIGHT** 两个基准，覆盖 **13 个领域**，包括多种检索与生成任务，特别关注推理密集型任务的表现。
- **对比方法**：摘要中未详列具体对比方法名称，但强调与查询时适应方案（状态无关型）和索引侧启发式更新方案（易引入噪声型）进行对比。
- **测评指标**：以检索性能和下游生成质量为主要评价指标，关注增益的一致性与推理速度。

### 4. 资源与算力
- 论文的摘要及提供的元数据中 **未明确说明** 使用的 GPU 型号、数量、训练时长等算力信息。文中提到 ERM 是“免训练”框架，可能不涉及大规模模型训练，但索引更新过程所需的计算资源未提及。

### 5. 实验数量与充分性
- 从摘要推断，实验覆盖 BEIR 和 BRIGHT 中的 **13 个领域**，构成了较大规模的跨域验证。但由于未能获取全文，具体的实验细节（如每个领域的任务数量、消融实验设计、统计检验等）未知。
- 从现有信息看，实验在领域多样性上具备一定充分性，但对消融因素（如门控策略、更新步长、归因粒度的影响）的分析是否完备，在无全文情况下无法客观判断。

### 6. 论文的主要结论与发现
- ERM 能够在多个领域实现 **持续的检索与生成增益**，尤其在推理密集型任务上提升明显。
- 方法保留了 **原生检索速度**，无推理时额外开销，实现了 RAG 系统在不遗忘前提下的持续自我优化。
- 通过理论证明和实验验证，将查询时增益转化为持久索引改进是可行且高效的。

### 7. 优点
- **方法创新性**：提出将瞬时查询适应转换为持久索引记忆的免训练框架，兼具在线学习和离线高效推理的优点。
- **理论支撑**：给出了查询/键扩展等价性证明和收敛性保证，增强了方法的可信度。
- **实用性强**：零推理开销保证了部署可行性，持续改进特性对动态知识场景有吸引力。
- **实验广泛**：跨 13 个领域、两个标准基准的验证体现了方法的泛化潜力。

### 8. 不足与局限
- **信息缺失**：由于只提供了摘要与元数据，无法评估方法细节、实验参数、消融实验的完整性以及结论的稳固性。
- **算力未知**：即使免训练，索引更新的计算成本未披露，对大规模索引的扩展性存疑。
- **应用限制**：论文可能集中于文本检索与生成，未涉及自动驾驶等特殊场景（元数据中 evidence 也注明“非驾驶专用”）；对于实时性要求极高或索引极度庞大的系统，选择性更新和归因的复杂度可能成为瓶颈。
- **偏差风险**：无全文无法判断对比方法的选择是否公平，以及是否存在数据泄漏或评估偏差。

（完）
