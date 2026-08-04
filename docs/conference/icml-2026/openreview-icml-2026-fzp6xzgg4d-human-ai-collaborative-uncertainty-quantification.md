---
title: Human-AI Collaborative Uncertainty Quantification
title_zh: 人机协同不确定性量化
authors: "Sima Noorani, Shayan Kiyani, George J. Pappas, Hamed Hassani"
date: 2026-04-30
pdf: "https://openreview.net/pdf/f80bfe87eeb994f88c8ee04109a5cb333a5f6516.pdf"
tags: ["query:traj-pred"]
score: 6.0
evidence: 通用不确定性量化框架，可迁移用于轨迹预测的不确定性评估
tldr: 在高风险决策中，AI预测系统需要与人类判断协同以应对不确定性。论文提出人机协同不确定性量化框架，让AI在’反事实伤害‘和’互补性‘约束下优化人类专家给出的预测集，并从理论上证明最优协同预测集具有双阈值结构。该方法为提高预测不确定性评估的可靠性与人机互补性提供了新思路，可迁移至轨迹预测等多模态预测场景。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 高风险决策需要结合人类判断与AI预测，现有不确定性量化方法未充分协同人类能力。
method: 提出人机协同不确定性量化框架，AI遵循反事实伤害与互补性原则优化人类预测集。
result: 理论上显示最优协同预测集具有简单的双阈值结构，为实际构建提供依据。
conclusion: 为AI与人类协同决策中的不确定性建模提供了通用框架，可应用于轨迹预测评估。
---

## Abstract
AI predictive systems increasingly support high-stakes decision making, yet robust decisions under uncertainty often rely on human capabilities beyond AI alone. This motivates collaborative approaches that combine human judgment with AI predictions. We study this problem through the lens of uncertainty quantification and introduce **Human-AI Collaborative Uncertainty Quantification**, a framework in which an AI system refines a human expert’s proposed prediction set subject to two principles: **counterfactual harm**, requiring that the AI not degrade correct human judgments, and **complementarity**, requiring recovery of correct outcomes the human missed. At the population level, we show that the optimal collaborative prediction set has a simple two-threshold structure over a single score function, governing pruning and augmentation relative to the human proposal. Building on this characterization, we develop offline and online calibration algorithms with **distribution-free** finite-sample guarantees. The online algorithm adapts to arbitrary distribution shifts, including settings where human behavior evolves through interaction with the AI. Empirically, we show that collaborative prediction sets outperform human-only and AI-only baselines, achieving improved coverage--efficiency tradeoffs across image classification, regression, and text-based medical decision making.

---

## 论文详细总结（自动生成）

根据提供的论文页面信息（摘要及元数据），以下是详细中文总结：

## 1. 核心问题与整体含义

- **背景与动机**：AI预测系统越来越多地支持高风险决策（如医疗、金融等），但面对不确定性，仅靠AI难以做出稳健决策，往往还需要依赖人类独有的判断能力。现有不确定性量化（UQ）方法主要聚焦于纯AI或纯人类视角，未能充分发挥人与AI的互补优势。
- **核心问题**：如何形式化并构建一种**人机协同**的不确定性量化框架，使AI系统在尊重并增强人类判断的前提下，输出覆盖更好、效率更高的预测集，从而支撑更可靠的决策。
- **整体含义**：该工作为“人与AI如何协同应对决策不确定性”提供了一个通用理论框架，明确了协同预测集的最优结构，并给出可操作的校准算法。该框架天然可迁移至轨迹预测等需要多模态不确定性评估的预测任务中，用于衡量和改进AI预测与人类预期的对齐程度。

## 2. 方法论

- **核心思想**：AI系统不独立生成预测集，而是以人类专家提出的预测集为基础，对其进行“精炼”（refine），使其在满足两个关键原则的前提下变得更优：
  - **反事实伤害（Counterfactual Harm）**：要求AI不得破坏人类原本正确的判断（即不能因加入AI的修正而让原本正确的预测失效）；
  - **互补性（Complementarity）**：要求AI必须尽力找回人类漏掉的正确结果，实现真正的人机互补，而不仅是重复人类的预测。
- **理论刻画**：在总体（population）层面，作者证明最优协同预测集可以表示为**单一得分函数上的双阈值结构**——一个阈值控制相对于人类预测集的“剪枝”（pruning，删去人类提出的不必要结果），另一个阈值控制“增广”（augmentation，补充人类遗漏的结果）。这一简单的结构为后续算法设计与实际部署提供了理论基础。
- **算法流程**：
  - **离线校准算法**：基于有限样本，以**分布无关（distribution-free）**的方式校准两个阈值，保证预测集覆盖性质（有限样本保证）。
  - **在线校准算法**：适应任意分布漂移，包括人类行为在与AI交互过程中动态演化的场景，同样具有分布无关的有限样本保证。

## 3. 实验设计

- **数据集 / 场景**：涵盖三类典型任务：
  - 图像分类（image classification）；
  - 回归任务（regression）；
  - 基于文本的医疗决策制定（text-based medical decision making）。
- **Benchmark / 对比方法**：以**人类单独决策（human-only）**和**AI单独决策（AI-only）**作为基线，对比所提协同预测集的性能。
- **评估指标**：主要考察预测集的**覆盖率-效率权衡（coverage–efficiency tradeoff）**，即协同预测集在保持目标覆盖率的同时，是否显著减小了预测集大小（不确定性区间宽度）。

## 4. 资源与算力

- 提供的论文页面内容中**未**提及任何关于训练资源的信息——未说明使用的GPU型号、数量、训练时长或总计算量等。
- 需要说明的是，该工作理论性较强，涉及的校准算法相对轻量，可能仅需较少算力；但由于原文PDF未完整获取，无法给出确切信息。

## 5. 实验数量与充分性

- **实验组数**：从摘要可知，实验覆盖了**3个不同领域**（图像分类、回归、医疗决策），且对比了两种基线（human-only与AI-only）。
- **充分性评估**：
  - 就覆盖场景多样性而言，3个任务代表了分类、连续回归和语义/文本理解，广度尚可，且兼具非结构与语言类数据，一定程度体现了框架的通用性。
  - 但由于本文提供的文本仅为摘要级内容，**未展开具体实验组数、消融实验、数据集规模、人类受试者数量等细节**，因此难以全面判断实验的充分性与统计严谨性。
  - 论文来自ICML 2026录用，通常评审要求下实验设计应较为严谨；但在缺少Figure、Table与详细设置的情况下，不宜过度断言其完全充分或存在偏向。

## 6. 主要结论与发现

- **理论发现**：在总体层面，最优的人机协同预测集具有**简洁的双阈值结构**，这对实际构建协同预测系统提供了清晰指导。
- **算法有效性与事实性结论**：
  - 所提出的离线与在线校准算法均具有**分布无关的有限样本保证**，在线算法还能适应任意分布漂移及人类行为随交互演化的情况（人类行为会随学习/交互而变化）。
  - 实验表明，协同预测集在覆盖率-效率权衡上**持续优于人类单独与AI单独基线**，说明“人机协同 > 各自为战”的核心主张在多个领域均得到验证。

## 7. 优点

- **问题立意新颖**：将人工智能系统从“提供最终预测”定位为“精炼人类判断”，以不确定性量化为切入点，视角独特、实用性强。
- **理论基础扎实**：将协同预测集的最优解刻画为双阈值的封闭形式，极大地降低了部署复杂度（只需在单一得分上设定两个阈值）。
- **保障强**：离线与在线校准均提供分布无关的有限样本保证，尤其在线算法允许人类行为动态演化，接近真实交互场景。
- **应用面广**：框架不依赖具体领域，可直接迁移到轨迹预测等任务的不确定性评估与交互式决策场景中。

## 8. 不足与局限

- **实验细节缺失**（基于当前材料）：无法获知各数据集的具体规模、人类专家数量、任务实例数、消融分析、参数敏感性等，无法独立检验其统计显著性和不同设置下的鲁棒性。
- **场景覆盖有限**：三个场景虽具代表性，但仍属于常见基准任务，尚未涉及真实高风险领域（如实际临床部署、自动驾驶决策、轨迹预测）中的复杂交互噪声与长尾不确定性。
- **人类行为建模的简化**：摘要中未说明人类专家具体如何提出预测集（是有序概率分布还是直接输出集合），实际人群异质性（专家能力差异、人为系统性偏差）对双阈值结构的影响有待进一步分析。
- **理论假设适用性**：总体层面的最优结构证明依赖特定假设条件，缺少对假设违反（如非平稳误差、恶意/损坏的人类反馈）时的行为分析。
- **无资源披露**：未报告计算资源或部署延迟，在实时决策或大规模在线场景中可行性尚难评估。

（完）
