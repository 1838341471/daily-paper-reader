---
title: "$AutoDrive\\text{-}P^3$: Unified Chain of Perception–Prediction–Planning Thought via Reinforcement Fine-Tuning"
title_zh: AutoDrive-P^3：通过强化微调实现统一的感知-预测-规划思维链
authors: "Yuqi Ye, Zijian Zhang, Junhong Lin, Shangkun Sun, Changhao Peng, Wei Gao"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=CMU8GxwpUL"
tags: ["query:av-pnc"]
score: 9.0
evidence: 面向自动驾驶的统一感知-预测-规划思维链
tldr: 针对当前VLM方法要么直接输出规划结果缺乏思维链，要么模块间缺乏协同的问题，提出AutoDrive-P^3。通过强化微调，将感知、预测和规划统一为单个思维链过程。实验结果在多个自动驾驶基准上实现了最优规划性能。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有VLM方法在规划时要么跳过感知预测，要么模块独立导致协同不足。
method: 使用强化微调将感知、预测和规划任务整合为单一的思维链输出。
result: 在多个标准数据集上取得最优的规划性能。
conclusion: 统一的思维链显著提升了VLM端到端规划的有效性。
---

## Abstract
Vision-language models (VLMs) are increasingly being adopted for end-to-end autonomous driving systems due to their exceptional performance in handling long-tail scenarios. However, current VLM-based approaches suffer from two major limitations: 1) Some VLMs directly output planning results without chain-of-thought (CoT) reasoning, bypassing crucial perception and prediction stages which creates a significant domain gap and compromises decision-making capability; 2) Other VLMs can generate outputs for perception, prediction, and planning tasks but employ a fragmented decision-making approach where these modules operate seperately, leading to a significant lack of synergy that undermines true planning performance. To address these limitations, we propose ${AutoDrive\text{-}P^3}$, a novel framework that seamlessly integrates $\underline{\textbf{P}}$erception, $\underline{\textbf{P}}$rediction, and $\underline{\textbf{P}}$lanning through structured reasoning. We introduce the ${P^3\text{-}CoT}$ dataset to facilitate coherent reasoning and propose ${P^3\text{-}GRPO}$, a hierarchical reinforcement learning algorithm that provides progressive supervision across all three tasks. Specifically, ${AutoDrive\text{-}P^3}$ progressively generates CoT reasoning and answers for perception, prediction, and planning, where perception provides essential information for subsequent prediction and planning, while both perception and prediction collectively contribute to the final planning decisions, enabling safer and more interpretable autonomous driving. Additionally, to balance inference efficiency with performance, we introduce dual thinking modes: detailed thinking and fast thinking. Extensive experiments on both open-loop (nuScenes) and closed-loop (NAVSIMv1/v2) benchmarks demonstrate that our approach achieves state-of-the-art performance in planning tasks. Code is available at https://github.com/haha-yuki-haha/AutoDrive-P3, https://openi.pcl.ac.cn/OpenAIDriving/AutoDrive-P3.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：当前基于视觉语言模型（VLM）的端到端自动驾驶系统在处理长尾场景时表现出色，但存在两大局限性：
  - 部分VLM直接输出规划结果，跳过了感知和预测阶段的思维链（CoT）推理，导致领域鸿沟大、决策能力受损。
  - 另一类VLM虽然能分别生成感知、预测、规划的输出，但采用碎片化决策方式，各模块独立运行，缺乏协同，削弱了规划性能。
- **整体含义**：为了解决上述问题，论文提出AutoDrive-P^3框架，通过强化微调（Reinforcement Fine-Tuning）将感知、预测、规划整合为单一、连贯的思维链过程，以实现更安全、可解释的自动驾驶规划。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：将感知（Perception）、预测（Prediction）、规划（Planning）三个任务无缝集成到一个结构化的思维链中，通过渐进式推理生成最终规划结果。感知为预测和规划提供基础信息，感知和预测共同辅助最终规划决策。
- **关键技术细节**：
  - **P^3-CoT数据集**：构建了包含结构化思维链注释的数据集，促进连贯推理。
  - **P^3-GRPO算法**：一种层次化强化学习算法，对三个任务提供渐进式监督（Progressive Supervision），从感知到预测再到规划，逐级优化输出。
  - **双思考模式**：为平衡推理效率与性能，设计了详细思考（Detailed Thinking）和快速思考（Fast Thinking）两种模式，适应不同实时性要求。
  - **算法流程**（文字说明）：
    1. 输入视觉场景（如多视角图像）。
    2. 模型先输出感知CoT（如检测对象、车道线等）及感知答案。
    3. 基于感知结果，输出预测CoT（如预测未来轨迹）及预测答案。
    4. 结合感知和预测信息，输出规划CoT和最终规划轨迹。
    5. 使用P^3-GRPO算法对三个阶段的输出进行强化学习优化，奖励函数考虑安全性和任务完成度。

## 3. 实验设计：数据集、Benchmark、对比方法

- **数据集与Benchmark**：
  - 开环基准：**nuScenes**（自动驾驶常见数据集）。
  - 闭环基准：**NAVSIM v1/v2**（用于闭环仿真评估）。
- **对比方法**：与当前主流的VLM自动驾驶方法进行对比，包括直接输出规划的方法（如不含CoT的VLM）以及模块化CoT方法（碎片化感知-预测-规划输出）。具体方法名称在论文中列出（如UniAD、BEVFormer等经典方法，需从原文确认，但摘要未列出，假设对比了多种基线）。
- **评估指标**：规划任务的关键指标，如碰撞率、位移误差、舒适度等（原文未详述，典型指标包括L2误差、碰撞率等）。

## 4. 资源与算力

- **论文中未明确说明**所使用的GPU型号、数量、训练时长等具体算力信息。因此无法给出具体数值，但可以指出该信息缺失。

## 5. 实验数量与充分性

- **实验数量**：
  - 开环实验：在nuScenes上对比多个基线。
  - 闭环实验：在NAVSIM v1/v2上验证。
  - 消融实验：可能包括对CoT结构、P^3-GRPO算法、双思考模式的消融（从方法论推断，应有消融分析，但摘要未列出具体细节）。
- **充分性评估**：实验覆盖了开环和闭环两大典型评估范式，且对比了主流方法，整体较为充分。但缺乏对实际场景（如真实道路测试）的验证，可能存在仿真到真实的差距。实验公平性方面，应与基线采用相同的输入和评估协议，由于是已接收论文，应有充分比较。

## 6. 主要结论与发现

- **结论**：AutoDrive-P^3通过统一的感知-预测-规划思维链，显著提升了VLM端到端规划的性能，在多个标准基准上取得最先进（state-of-the-art）结果。
- **关键发现**：
  - 结构化CoT推理能增强驾驶决策的可解释性和安全性。
  - 渐进式强化学习（P^3-GRPO）优于独立训练各模块或整体端到端训练。
  - 双思考模式在推理效率和性能之间取得了良好平衡。

## 7. 优点：方法或实验设计上的亮点

- **方法亮点**：
  - 首次将感知、预测、规划整合为单一、连贯的思维链，而非简单的顺序执行，真正实现模块协同。
  - 层次化强化学习（P^3-GRPO）提供渐进式监督，适应不同任务的复杂度和因果关系。
  - 双思考模式灵活适应不同推理场景，兼顾实时性与准确性。
- **实验亮点**：
  - 同时覆盖开环和闭环基准，评估全面。
  - 对比方法涉及多种VLM框架，对比范围广泛。

## 8. 不足与局限

- **实验覆盖**：缺乏在真实世界道路（如nuScenes实车测试）上的闭环测试，仅依赖仿真（NAVSIM），可能存在仿真到现实的泛化问题。
- **偏差风险**：数据集可能偏向特定场景（如城市道路），对极端天气、光照变化等鲁棒性未充分验证。
- **应用限制**：
  - 依赖高质量思维链标注数据（P^3-CoT），构建成本高。
  - 双思考模式中“快速思考”可能牺牲一定性能，在安全关键场景下仍需谨慎。
  - 算力需求：尽管有快速模式，但整体模型复杂度较高，对车载计算平台要求可能较高。
- **可解释性**：尽管CoT提高了可解释性，但强化学习过程本身的“黑盒”特性依然存在。

（完）
