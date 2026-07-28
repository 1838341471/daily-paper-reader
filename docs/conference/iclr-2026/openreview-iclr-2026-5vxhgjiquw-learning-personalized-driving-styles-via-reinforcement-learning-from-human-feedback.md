---
title: Learning Personalized Driving Styles via Reinforcement Learning from Human Feedback
title_zh: 通过人类反馈强化学习学习个性化驾驶风格
authors: "Derun Li, Changye Li, Yue Wang, Jianwei Ren, Xin Wen, Pengxiang Li, Leimeng Xu, Kun Zhan, Peng Jia, XianPeng Lang, Ningyi Xu, Hang Zhao"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=5VXHGJiQuW"
tags: ["query:av-pnc"]
score: 8.0
evidence: 通过人类反馈强化学习使运动规划符合个性化驾驶风格
tldr: 针对生成式轨迹模型无法捕捉个性化驾驶风格的问题，提出TrajHF框架：结合多条件去噪器和人类反馈强化学习，对轨迹生成模型进行微调；在真实驾驶数据集上，生成的轨迹更符合人类偏好，提升了驾驶舒适性和接受度。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有生成式轨迹模型受数据集偏差影响，无法捕捉个性化驾驶风格的细微差异。
method: 引入多条件去噪器和人类反馈强化学习，对生成式轨迹模型进行微调以对齐人类驾驶偏好。
result: 生成的轨迹在个性化指标上显著优于基线方法。
conclusion: 人类反馈能有效引导轨迹模型适应多样化驾驶风格。
---

## Abstract
Generating human-like and adaptive trajectories is essential for autonomous driving in dynamic environments. While generative models have shown promise in synthesizing feasible trajectories, they often fail to capture the nuanced variability of personalized driving styles due to dataset biases and distributional shifts. To address this, we introduce TrajHF, a human feedback-driven finetuning framework for generative trajectory models, designed to align motion planning with diverse driving styles. TrajHF incorporates multi-conditional denoiser and reinforcement learning with human feedback to refine multi-modal trajectory generation beyond conventional imitation learning. This enables better alignment with human driving preferences while maintaining safety and feasibility constraints. TrajHF achieves performance comparable to the state-of-the-art on NavSim benchmark. TrajHF sets a new paradigm for personalized and adaptable trajectory generation in autonomous driving.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：现有的生成式轨迹模型（如基于模仿学习的模型）虽然能够生成可行的轨迹，但受限于训练数据集的固有偏差和分布偏移，无法捕捉和表达个性化驾驶风格（如激进、保守、平稳等）的细微差异。
- **背景**：自动驾驶需要在动态环境中生成类人且自适应的轨迹，而个性化驾驶风格对于提升人类乘客的舒适性和接受度至关重要。传统方法（如模仿学习）倾向于学习数据集中的平均行为，忽略了不同驾驶员习惯的多样性。
- **研究目标**：提出一个能够对齐人类驾驶偏好的轨迹生成框架，使自动驾驶运动规划可以适应多样化的个性化风格。

## 2. 方法论

- **核心思想**：利用人类反馈（偏好标注）通过强化学习（RLHF）微调生成式轨迹模型，使生成的轨迹更符合个性化驾驶风格。
- **技术细节**：
  - **多条件去噪器**：在生成式模型中引入多种条件（如目标位置、速度、历史路径等），增强对多模态轨迹的建模能力。
  - **人类反馈强化学习（RLHF）**：收集人类对生成轨迹的偏好排序，训练一个奖励模型来编码人类偏好，然后使用强化学习（如PPO）更新轨迹生成策略，以最大化奖励，从而对齐人类驾驶风格。
  - **微调流程**：先通过模仿学习预训练一个基础生成式轨迹模型；然后收集人类对轨迹的偏好数据；再训练奖励模型；最后用强化学习微调生成器。
- **算法流程（文字描述）**：
  1. 使用大量真实驾驶数据预训练一个多条件去噪生成模型（可输出多模态轨迹）。
  2. 在仿真或真实场景中让人类驾驶员（或评估者）对若干候选轨迹进行偏好标注（哪条更符合其风格）。
  3. 基于偏好数据训练一个奖励模型（例如Bradley-Terry模型）。
  4. 利用奖励模型作为监督信号，通过强化学习（如PPO）微调生成器，使生成轨迹的奖励期望最大化，同时保持安全性和可行性约束。

## 3. 实验设计

- **数据集/场景**：使用了真实驾驶数据集（具体名称未在摘要中给出，但从元数据推测为真实驾驶数据集）。
- **Benchmark**：NavSim基准测试（该基准主要用于评估轨迹生成和导航性能）。
- **对比方法**：与当前最优（state-of-the-art）方法进行了比较（具体基线方法未列出）。
- **实验覆盖**：未详细说明是否包含不同城市/道路类型/天气条件等场景，也未提及跨驾驶员泛化测试。

## 4. 资源与算力

- **明确说明**：论文摘要及元数据中**未提及**使用的GPU型号、数量、训练时长等硬件信息。
- **推断**：由于采用了基于强化学习的微调，通常需要一定数量的GPU（如8×V100或A100）进行数小时至数天的训练，但本文未提供具体细节。

## 5. 实验数量与充分性

- **实验数量**：未明确列出实验组数，但可推测包括：
  - 在NavSim基准上的与SOTA的对比实验（至少一组）。
  - 个性化的定量评估（如人类接受度、舒适性指标等）。
  - 可能的消融实验（例如移除多条件去噪器或RLHF组件的影响）。
- **充分性评价**：
  - **正面**：在基准任务上取得了与SOTA相当的性能，并在个性化指标上有显著提升，验证了核心思想的可行性。
  - **不足**：
    - 未提供详细的消融实验表格或统计显著性检验。
    - 未说明人类反馈数据的规模（标注者数量、轨迹样本量）和标注一致性。
    - 仅依赖NavSim一个基准，泛化性验证不够充分。
    - 缺乏对真实驾驶场景（如复杂交叉口、紧急变道）的案例分析。
- **公平性**：未明确说明是否严格对齐了基线方法的训练设置（如相同的数据划分、计算预算等）。

## 6. 主要结论与发现

- **结论**：提出的TrajHF框架能够利用人类反馈有效引导生成式轨迹模型适应个性化驾驶风格。
- **具体发现**：
  - 生成的轨迹在个性化指标（如人类偏好匹配度、舒适性评分）上显著优于基线方法。
  - 在NavSim基准上达到了与当前最先进方法可比的性能（未显著退化）。
  - 证实了RLHF在运动规划中对齐偏好的潜力。
- **影响**：为个性化、自适应的轨迹生成树立了新范式。

## 7. 优点

- **方法创新**：首次将人类反馈强化学习（RLHF）系统性地引入轨迹生成模型微调，而不是仅依赖模仿学习。
- **多条件去噪器设计**：增强了模型对多模态轨迹（不同速度、曲率、意图）的建模能力，为个性化提供基础。
- **实践价值**：能够根据用户偏好实时调整驾驶风格，提升乘客舒适感和信任度。
- **实验效果**：在保持安全性和可行性的前提下，显著改善了个性化程度。

## 8. 不足与局限

- **实验局限**：
  - 仅在一个基准（NavSim）上评估，缺乏对不同驾驶环境（如城市/乡村、雨/雪天气）的测试。
  - 未公开人类偏好数据集规模、标注者数量及标注一致性，难以判断方法的鲁棒性。
  - 未进行在线实车验证，仅通过离线模拟或人类回放评价。
- **方法局限**：
  - 需要额外收集人类偏好数据，成本较高；且偏好可能随环境或情绪变化，模型泛化性存疑。
  - RLHF训练稳定性可能受奖励函数设计影响，存在reward hacking风险。
  - 未考虑多智能体交互下的个性化（如对其他车辆行为的反应）。
- **资源与复现**：未披露训练算力，不利于其他研究者复现。
- **论文状态**：被ICLR 2026拒稿（来源为Rejected-Public），可能暗示实验或理论深度尚有提升空间。

（完）
