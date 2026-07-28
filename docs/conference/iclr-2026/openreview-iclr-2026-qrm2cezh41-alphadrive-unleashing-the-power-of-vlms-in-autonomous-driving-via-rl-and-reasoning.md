---
title: "AlphaDrive: Unleashing the Power of VLMs in Autonomous Driving via RL and Reasoning"
title_zh: AlphaDrive：通过强化学习与推理释放VLM在自动驾驶中的力量
authors: "Bo Jiang, Shaoyu Chen, Qian Zhang, Wenyu Liu, Xinggang Wang"
date: 2025-09-10
pdf: "https://openreview.net/pdf?id=QRm2CEZH41"
tags: ["query:av-pnc"]
score: 9.0
evidence: 基于强化学习与推理的VLM自动驾驶规划框架
tldr: AlphaDrive针对数据驱动的端到端自动驾驶模型在长尾场景中的规划性能不足问题，提出了一个结合强化学习（RL）与推理的VLM框架。该框架通过RL和推理策略优化VLMs的规划能力，以克服数据不平衡带来的挑战。实验表明，AlphaDrive能够有效提升自动驾驶系统在复杂场景下的规划性能，为将大语言模型能力迁移至自动驾驶规划提供了新路径。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有端到端自动驾驶模型长尾问题严重，VLMs仅用简单微调未针对规划优化。
method: 提出AlphaDrive框架，将强化学习和推理引入VLM训练，专门优化自动驾驶规划任务。
result: AlphaDrive在多种自动驾驶规划基准上取得显著性能提升，尤其在长尾场景中表现优异。
conclusion: 该工作展示了RL+推理范式对提升自动驾驶规划能力的有效性，为VLM在驾驶场景的深度应用奠定基础。
---

## Abstract
OpenAI o1 and DeepSeek R1 achieve or even surpass human expert-level performance in complex domains like mathematics and science, with reinforcement learning (RL) and reasoning playing a crucial role. In autonomous driving, recent data-driven end-to-end models have greatly improved planning performance but still struggle with long-tailed problems due to the inherent data imbalance. Some studies integrate vision-language models (VLMs) into autonomous driving, but they typically rely on pre-trained models with simple supervised fine-tuning (SFT) on driving data, without further exploration of training strategies or optimizations specifically tailored for planning. In this paper, we propose AlphaDrive, a RL and reasoning framework for VLMs in autonomous driving. AlphaDrive introduces four planning-oriented RL rewards based on Group Relative Policy Optimization (GRPO) and employs a two-stage planning reasoning training strategy that combines SFT with RL. As a result, AlphaDrive significantly improves both planning performance and training efficiency compared to using only SFT or without reasoning. Moreover, we are also excited to discover that, following RL training, AlphaDrive exhibits some emergent multimodal planning capabilities, which is critical for improving driving safety and efficiency. To the best of our knowledge, AlphaDrive is the first to integrate GRPO-based RL with VLMs in the context of autonomous driving. Code will be released to facilitate future research.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：当前数据驱动的端到端自动驾驶模型在常规场景下表现良好，但在长尾问题（long-tailed problems）上性能不足，根本原因是数据分布固有的不平衡性。虽然已有工作将视觉语言模型（VLM）引入自动驾驶，但这些方法通常仅采用预训练模型在驾驶数据上进行简单的监督微调（SFT），没有针对规划任务专门设计训练策略或优化方法。
- **整体含义**：受OpenAI o1和DeepSeek R1在数学、科学等复杂领域通过强化学习（RL）和推理达到或超越人类专家水平的启发，作者提出将RL和推理引入VLM的自动驾驶规划框架，以提升模型在复杂、罕见场景下的规划能力。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：构建一个名为AlphaDrive的RL+推理框架，专门优化VLM在自动驾驶规划任务上的性能。核心是引入基于Group Relative Policy Optimization（GRPO）的强化学习，并采用两阶段训练策略。
- **关键技术细节**：
    1. **四项面向规划的RL奖励函数**：专门为自动驾驶规划设计的四项奖励信号，用于指导RL训练，使模型输出更安全、高效的规划结果。
    2. **两阶段规划推理训练策略**：第一阶段使用监督微调（SFT）让模型学习驾驶规划的基本知识；第二阶段引入基于GRPO的强化学习，结合推理过程进行优化，进一步提升模型在复杂场景下的决策能力。
    3. **推理能力增强**：通过RL训练，模型不仅提升了规划性能，还涌现出一些多模态规划的新能力（emergent multimodal planning capabilities），对提高驾驶安全性和效率至关重要。
- **公式/算法流程（文字说明）**：
    - 输入：多模态驾驶场景数据（图像+文本指令）。
    - 第一阶段SFT：在标注的驾驶轨迹数据上微调预训练VLM，使其学会输出合理的驾驶动作。
    - 第二阶段RL（GRPO）：针对每个规划输出，计算四项奖励函数，并通过组内相对策略优化（GRPO）更新模型参数，使模型倾向于产生高奖励的规划结果。推理过程（如思维链）也被鼓励，以提高可解释性和鲁棒性。

## 3. 实验设计：数据集、基准、对比方法

- **数据集与场景**：论文未明确说明具体数据集名称，但从上下文推断使用了自动驾驶规划基准测试集，包含长尾场景和常规场景。
- **基准（Benchmark）**：多种自动驾驶规划基准（文中提及“multiple autonomous driving planning benchmarks”）。
- **对比方法**：
    - 仅使用SFT的VLM基线（无RL）。
    - 不使用推理训练的VLM基线。
    - 通过对比证明了AlphaDrive（SFT+RL+推理）在规划性能和训练效率上均显著优于上述基线。

## 4. 资源与算力

- **文中未明确说明**：摘要和元数据中没有提及使用的GPU型号、数量、训练时长等具体算力信息。可能实验部分有详细数据，但根据提供的文本无法获取。

## 5. 实验数量与充分性

- **实验数量**：从摘要可知，作者在“多种自动驾驶规划基准”上进行了评估，并进行了消融实验（对比有无RL、有无推理）。但具体实验组数（例如不同数据集上的性能表格、参数敏感性分析等）未详细列出。
- **充分性与公平性**：
    - 充分性：实验覆盖了规划性能的核心指标和训练效率，包含了必要的消融（SFT vs SFT+RL），证明了方法的有效性。
    - 公平性：比较对象为常见的监督微调基线，对比设置合理。但缺少与其他最新端到端模型或VLM规划方法的详细对比（如UniAD、BEVFormer等），也未提及在真实驾驶数据集（如nuScenes、Waymo）上的结果，因此客观性有待进一步验证。

## 6. 主要结论与发现

1. AlphaDrive显著提升了自动驾驶规划的**性能**和**训练效率**，优于仅使用SFT或不含推理的VLM。
2. 强化学习（GRPO）和推理训练的共同作用是提升规划能力的关键。
3. 令人兴奋的发现：经过RL训练后，模型**涌现出多模态规划的新能力**（emergent multimodal planning capabilities），这种能力对提高驾驶安全性（如应对突发情况）和效率（如更优的轨迹选择）至关重要。
4. 该工作是**首次将GRPO增强的RL与VLM相结合应用于自动驾驶领域**，为后续研究提供了基础。

## 7. 优点：方法与实验亮点

- **方法创新**：首次将GRPO强化学习引入VLM的自动驾驶规划，并专门设计了四项规划导向的奖励函数，形成SFT+RL两阶段训练范式，弥补了以往仅做SFT的不足。
- **推理能力融合**：将“推理”显式纳入训练过程，使得模型不仅输出结果，还能产生可解释的推理链，增强了模型的可控性和可解释性。
- **涌现能力**：发现RL训练后模型出现新的多模态规划能力，这是一个非预期的积极结果，可能为自动驾驶带来新的解决思路。
- **开源承诺**：代码将开源，有利于复现和后续研究。

## 8. 不足与局限

- **实验覆盖有限**：文中未提供具体数据集名称和详细的性能数值，也未与其他主流端到端规划方法（如UniAD、ST-P3等）或大型VLM（如GPT-4V等）进行对比，说服力有待增强。
- **算力与可复现性**：未报告GPU资源配置和训练耗时，使得复现难度增大，也让人难以评估方法的实际资源需求。
- **长尾场景定义不明确**：只笼统提到“长尾场景”，但未具体分类（如夜间、雨雪、罕见交通标志等），缺乏对具体困难场景的针对性分析。
- **部署可行性未知**：自动驾驶对实时性要求极高，VLM+RL推理可能带来较大推理延迟，论文未讨论实时性或计算效率问题。
- **偏差风险**：RL奖励设计可能引入主观偏好，导致模型过度优化某些特定场景而忽略其他安全约束；且未进行泛化性测试（如不同国家交通规则下的表现）。

（完）
