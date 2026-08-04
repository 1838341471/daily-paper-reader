---
title: "CooT: Learning to Coordinate In-Context with Coordination Transformers"
title_zh: CooT：用协调Transformer实现上下文中的协作学习
authors: "Huai-Chih Wang, Hsiang-Chun Chuang, Hsi-Chun Cheng, Dai-Jie Wu, Shao-Hua Sun"
date: 2026-04-30
pdf: "https://openreview.net/pdf/41ec9d7578f44a4227ccfcbe515f7fb3145138bc.pdf"
tags: ["query:traj-pred"]
score: 4.0
evidence: 多智能体协调与轨迹学习，可迁移至社会交互建模
tldr: 多智能体系统中陌生伙伴的有效协调充满挑战，现有方法依赖群体多样性但难以适应分布外情况，微调又需要大量交互。本文提出协调变换器（CooT），利用上下文学习对行为偏好智能体的轨迹进行训练，从而在不微调的情况下实时适应多样化伙伴行为。该方法为建模智能体间交互提供了新思路，或可借鉴到行人轨迹预测中的社会交互建模。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有多智能体协调方法缺乏分布外适应能力，微调可行性低，难以在少样本下适应新伙伴。
method: 提出协调Transformer，利用上下文学习在行为偏好智能体的轨迹上训练，实现在线伙伴适应。
result: 初步实验表明该方法能够有效适应多样化的伙伴行为，无需大量微调。
conclusion: 为多智能体协调提供了一种无需微调的上下文学习机制，也为社会交互建模提供了参考。
---

## Abstract
Effective coordination among unfamiliar partners remains a major challenge in multi-agent systems. Existing approaches, such as population-based methods, improve robustness through diversity but often lack mechanisms for efficient adaptation beyond the training distribution. Fine-tuning is also impractical for few-shot learning because it requires a large number of interactions for meaningful improvement. 
To address these limitations, we propose Coordination Transformers (CooT), a framework that leverages in-context learning (ICL) for real-time partner adaptation. Unlike prior ICL approaches that focus on task generalization, CooT is designed to generalize across diverse partner behaviors. Trained on trajectories from behavior-preferring agents, it learns to align actions with partner intentions purely through observation. We evaluate CooT on two challenging multi-agent benchmarks: Overcooked and Google Research Football.
Results show that CooT consistently outperforms population-based methods, gradient-based fine-tuning, and Meta-RL baselines, achieving stable and rapid adaptation without parameter updates. Human evaluations also identify CooT as a preferred collaborator, and our ablations confirm its ability to adapt quickly to new partners and remain stable under sudden partner changes, making it reliable for real-world human-AI collaboration.

---

## 论文详细总结（自动生成）

# 论文中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- 多智能体系统中，智能体与陌生伙伴进行有效协作是一个核心挑战。
- 现有方法（如基于群体多样性的种群方法）虽然能提升鲁棒性，但难以在训练分布之外高效适应新伙伴；梯度微调方法则需要大量交互样本，不适合少样本适应场景。
- 本文旨在解决“如何在无需参数更新、仅依靠少量观察的情况下，实时适应多样化伙伴行为”的问题，为多智能体协调提供了一种基于上下文学习（In-Context Learning, ICL）的新框架。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **方法名称**：Coordination Transformers（CooT，协调Transformer）。
- **核心思想**：利用上下文学习（ICL）实现实时伙伴适应，而非任务泛化。模型通过观察伙伴的历史轨迹，推断其行为偏好，并动态调整自身动作以与之协调。
- **关键技术细节**：
  - 训练数据来自“行为偏好智能体”（behavior-preferring agents）的轨迹，使模型学会仅通过观察来对齐伙伴意图。
  - 模型不进行任何参数更新（即无需微调），完全依赖上下文中的轨迹信息进行在线适应。
- **算法流程（文字说明）**：
  1. 输入当前智能体与伙伴的联合历史轨迹（上下文）；
  2. 通过Transformer编码轨迹序列，提取伙伴行为模式；
  3. 解码生成当前智能体应采取的协调动作；
  4. 在新交互中，通过更新上下文窗口（加入最新观察），实现持续适应。
- 论文未给出具体公式（如注意力机制变体、损失函数形式），仅描述了整体框架思路。

## 3. 实验设计：数据集 / 场景 / Benchmark / 对比方法

- **基准场景**：两个多智能体协调基准任务：
  - **Overcooked**（烹饪协作游戏，要求紧密配合）。
  - **Google Research Football**（谷歌研究足球，多智能体团队对抗）。
- **对比方法**：
  - 种群方法（Population-based methods）
  - 梯度微调（Gradient-based fine-tuning）
  - Meta-RL 基线（Meta Reinforcement Learning baselines）
- **人类评估**：额外进行了人类参与者的协作评估，衡量人类对 CooT 作为协作伙伴的偏好。

## 4. 资源与算力

- 论文中**未明确说明**所使用的 GPU 型号、数量、训练时长、显存占用等计算资源信息。
- 仅能从“Transformer 架构”和“多智能体 benchmark”推断需要一定的计算资源，但具体细节缺失。

## 5. 实验数量与充分性

- **实验组数**：包括两大基准任务上的对比实验、人类评估、以及消融实验（ablations）。消融实验验证了快速适应新伙伴的能力以及在伙伴突然变化时的稳定性。
- **充分性与公平性评估**：
  - 对比了多类主流基线（种群、微调、Meta-RL），覆盖较全面。
  - 加入了人类评估，增强了结果的说服力。
  - 消融实验针对关键能力（快速适应、稳定性）进行了验证。
  - 但论文摘要未提供具体的性能数值、统计显著性、误差棒或多次随机种子结果，因此无法完全判断实验的统计充分性和公平性。此外，仅有两个基准场景，泛化性证据有限。

## 6. 论文的主要结论与发现

- CooT 在 Overcooked 和 Google Research Football 上**持续优于**种群方法、梯度微调和 Meta-RL 基线。
- 能够在**不进行参数更新**的情况下实现稳定且快速的伙伴适应。
- 人类评估显示，人类参与者更倾向于选择 CooT 作为协作对象。
- 消融实验证实 CooT 能快速适应新伙伴，并在伙伴突然变化时保持稳定，适合真实世界中的人机协作场景。

## 7. 优点

- **创新性强**：将上下文学习从任务泛化延伸到“伙伴泛化”，开辟了多智能体协调的新思路。
- **实用性高**：无需微调即可实时适应，避免了大量交互成本，适合动态、开放的真实环境。
- **方法简洁**：仅依赖轨迹观察，无需显式推断模型或复杂元学习。
- **实验设计较全面**：包含多任务对比、人类评估和消融实验，验证了方法的有效性与稳定性。

## 8. 不足与局限

- **公式细节缺失**：论文未展示模型的具体网络结构、损失函数、训练算法细节，难以完全复现。
- **计算资源未报告**：缺少 GPU 型号、训练时间等资源信息，影响可复现性和成本评估。
- **基准数量有限**：仅两个多智能体任务，缺乏更广泛（如连续控制、混合协作-竞争）场景的验证。
- **统计严谨性不明**：未提供性能数值、方差、显著性检验等信息，无法确认性能差异的统计可靠性。
- **“行为偏好智能体”定义不明确**：训练数据的具体生成方式、偏好类型覆盖范围未详细说明，可能带来偏差。
- **人类评估细节缺失**：参与人数、评估协议、主观指标等未介绍，主观偏好结果的可信度受限。

（完）
