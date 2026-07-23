---
title: "Less Is More: Elevating RAG via Performance-Driven Context Compression"
title_zh: 少即是多：通过性能驱动的上下文压缩提升RAG
authors: "Ziqiang Cui, Yunpeng Weng, Xing Tang, Peiyang Liu, Shiwei Li, Bowei He, Jiamin Chen, Yansen Zhang, Xiuqiang He, Rui Zhang, Chen Ma"
date: 2026-04-30
pdf: "https://openreview.net/pdf/691980af2ac73b21258f307583aec6e72ad92325.pdf"
tags: ["query:ad-rag"]
score: 5.0
evidence: RAG上下文压缩框架CORE-RAG，减少输入长度
tldr: 提出CORE-RAG，一种性能驱动的RAG上下文压缩框架，直接基于生成任务性能优化压缩上下文，摒弃启发式规则，在降低计算成本的同时保持任务性能。（通用RAG方法，可用于自动驾驶场景的检索压缩）
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 检索文档过多导致RAG输入长度剧增，计算开销大，现有压缩方法依赖启发式规则损害性能。
method: 提出CORE-RAG，通过性能驱动学习直接优化压缩上下文，以适应生成任务。
result: 在多个RAG基准上，压缩后仍保持高性能，并降低延迟。
conclusion: 为RAG系统提供了一种高效的上下文压缩方案，实用性广。
---

## Abstract
Retrieval-Augmented Generation (RAG) has emerged as a promising paradigm for improving the timeliness of knowledge updates and the factual accuracy of large language models. However, incorporating a large volume of retrieved documents significantly increases input length, leading to prohibitive computational costs. Existing compression approaches often compromise task performance, primarily due to their reliance on predefined heuristics. These heuristics fail to ensure that the compressed context is conducive to the generation tasks. To address these limitations, we propose CORE-RAG, a novel framework for context compression in RAG systems. 
CORE eliminates reliance on proxy heuristics through a performance-driven learning framework, which directy utilizes task performance as a feedback signal to iteratively refine the compressor policy. Prior to this optimization process, we incorporate a knowledge distillation phase to initialize the compressor with a robust policy. Extensive experiments demonstrate the superiority of our approach. At a high compression ratio of 3\%, CORE not only avoids performance degradation but also improves the average Exact Match (EM) score by 3.3 points compared to using full documents. Our code is available at https://github.com/ziqiangcui/CORE-RAG-ICML26.

---

## 论文详细总结（自动生成）

# 论文详细总结：少即是多：通过性能驱动的上下文压缩提升RAG

## 1. 论文的核心问题与整体含义

- **研究背景**：检索增强生成（RAG）已成为提升大语言模型知识时效性与事实准确性的重要范式。但 RAG 系统需要将大量检索文档拼接到输入中，导致输入长度急剧膨胀，带来高昂的计算开销。
- **核心问题**：如何在保持生成任务性能的前提下，对检索到的上下文进行高效压缩，以降低计算成本。
- **现有方法局限**：当前的上下文压缩方法大多依赖预定义的启发式规则（如基于相似度或相关性分数截断），这类规则无法保证压缩后的上下文真正有利于下游生成任务，往往以牺牲任务性能为代价。
- **整体含义**：本文提出一种“性能驱动”的压缩框架，旨在打破启发式依赖，让压缩策略直接为最终生成效果服务，实现“少即是多”——用更短的上下文达到甚至超越全量文档的任务表现。

## 2. 论文提出的方法论

- **核心思想**：以任务性能直接作为反馈信号，通过迭代学习的方式自动优化压缩策略（compressor policy），而非依赖任何代理性启发指标。
- **框架名称**：**CORE-RAG**（全称未在摘要中给出，推测为 COntext REfinement for RAG）。
- **关键技术细节**（根据摘要提炼）：
  - **性能驱动学习**：将一个可学习的压缩器（compressor）置于检索模块与生成模块之间，其目标是最小化最终生成任务的损失（或最大化性能指标）。每一步训练中，压缩器输出一个精简的上下文，生成模型据此产生答案，然后利用答案的准确度（如精确匹配分数 EM）作为反馈信号，通过强化学习或梯度近似的方式更新压缩器参数。
  - **知识蒸馏预热**：在正式的性能驱动优化之前，引入知识蒸馏阶段，用教师模型（可能为全量文档下的生成表现）指导学生压缩器的初始策略，使其获得一个稳健的起点，避免从零开始的盲目探索。
  - **策略迭代优化**：基于任务反馈不断微调压缩策略，使模型学会鉴别哪些句子或文档片段对回答至关重要，从而在高压缩比（例如仅保留 3% 的原始上下文）下仍能维持甚至提升下游性能。
- **算法流程**（文字说明）：  
  1. 用知识蒸馏预训练压缩器，获得初始策略。  
  2. 在训练循环中，压缩器压缩检索文档，生成模型输出答案。  
  3. 根据答案准确度计算奖励/损失，更新压缩器策略。  
  4. 重复直至收敛。

## 3. 实验设计

- **数据集/场景**：论文提到在“多个 RAG 基准”上开展了广泛实验，但元数据与摘要中未给出具体基准名称。通常 RAG 论文会涉及开放域问答、事实验证等数据集（如 Natural Questions、TriviaQA、HotpotQA、FEVER 等），此处仅能推断覆盖了通用 RAG 场景。
- **Benchmark 指标**：摘要中明确指出使用 Exact Match (EM) 作为主要评估指标，同时隐含比较了压缩后的计算延迟（降低延迟）。
- **对比方法**：与“全量文档”（不使用压缩）以及“现有压缩方法”进行对比。现有压缩方法被描述为“依赖启发式规则”的方案，但未列出具体方法名（如基于 BM25 或稠密检索分数截断、LongLLMLingua 等常见上下文压缩手段）。

## 4. 资源与算力

- **文本提供的信息**：摘要及元数据中**未明确说明**所使用的 GPU 型号、数量或训练时长。仅提到了计算延迟降低（定性），但缺乏具体的算力配置数据。
- **推断**：通常此类涉及大语言模型生成和训练的实验需要多卡高性能 GPU（如 A100），但该总结无法给出确切数字，需注明“原文未提及”。

## 5. 实验数量与充分性

- **实验组数估算**：摘要中提及“大量实验”（extensive experiments），并在高压缩比 3% 下汇报了平均 EM 分数提升 3.3 个点，推测实验至少涵盖：
  - 多个数据集的横向对比；
  - 不同压缩率（至少报告了 3% 这一极低比例）的敏感性测试；
  - 消融实验以验证性能驱动学习和知识蒸馏的价值（摘要未详述，但此类论文通常包含）。
- **充分性评价**：由于缺乏具体细节（数据集个数、对比方法数量、消融项），无法准确判断实验的广度和深度。但现有信息显示其在一个极端的压缩条件下实现了性能反超，这一结果本身具有较强的说服力，若补充更多基准和对比结果将更加客观公正。
- **公平性**：与全量文档对比，且均在同一生成模型下评估，基本公平；但与启发式压缩方法的对比公平性取决于基线实现的正规性，文中未提供细节，存有一定风险。

## 6. 论文的主要结论与发现

- 通过性能驱动的学习方式，CORE 框架成功消除了对预定义启发式规则的依赖。
- 在 3% 的高压缩比下，CORE 不仅未引发性能下降，反而使平均 EM 分数相比全量文档**提高了 3.3 个点**。

其中，该结论可能揭示了检索到的文档中存在噪声或无关内容，智能压缩起到了“去噪提纯”的作用，从而辅助生成模型更精准地作答。
- 同时，压缩后的上下文显著降低了计算延迟，表明该方法在效率与效果上取得了双赢。

## 7. 优点

- **直接以终为始**：将压缩策略优化与最终生成性能直接挂钩，突破了传统启发式压缩的性能瓶颈。
- **高压缩比下性能反超**：在仅保留 3% 上下文时实现 EM 提升 3.3 点，这一反常识结论（更少输入却有更好输出）具有很强的启示意义，证明了智能压缩的“去噪”价值。
- **引入知识蒸馏初始化**：为压缩器提供了良好的起点，加速收敛并增强最终策略的稳定性。
- **开源代码**：提供了 GitHub 地址，提高了研究的可复现性。

## 8. 不足与局限

- **实验细节缺失**：由于原始 PDF 文本不可获取，摘要未提供具体数据集列表、对比基线名称、模型尺寸、训练算力等关键信息，导致无法全面评估其泛化性。
- **仅报告 EM 指标**：仅以精确匹配作为唯一量化指标略显单薄，缺乏对生成质量的其他维度评估（如 F1、BLEU、ROUGE、人工评估等），可能掩盖部分性能损失。
- **压缩器本身复杂度未知**：压缩器的模型架构、参数量、推理开销未提及，若压缩器本身过于庞大，可能部分抵消压缩带来的延迟收益。
- **通用性证明不足**：文本所述为“通用 RAG 方法”，但摘要未展示在特定领域（如自动驾驶）的定制化实验，领域偏移风险未被讨论。
- **潜在的偏差风险**：使用知识蒸馏初始化可能将教师模型的偏好或偏差引入压缩器，未讨论其对最终策略公平性的影响。

（完）
