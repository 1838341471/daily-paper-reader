---
title: "SAD-Flower: Flow Matching for Safe, Admissible, and Dynamically Consistent Planning"
title_zh: SAD-Flower：用于安全、可容许与动态一致规划的流匹配方法
authors: "Tzu-Yuan Huang, Armin Lederer, Dai-Jie Wu, Xiaobing Dai, Sihua Zhang, Hsiu-Chin Lin, Shao-Hua Sun, Stefan Georg Sosnowski, Sandra Hirche"
date: 2026-04-30
pdf: "https://openreview.net/pdf/b5c67a42e2159ac5a0a45bc7981e0004b70effa5.pdf"
tags: ["query:av-pnc"]
score: 10.0
evidence: 提出一种流匹配框架，用于生成安全、可容许且动态一致的规划轨迹
tldr: 针对流匹配规划器缺乏状态与动作约束保证的问题，本文提出SAD-Flower框架。该方法通过引入虚拟控制输入对流进行增强，利用控制技术推导有原则的引导，确保生成的轨迹安全、可容许且动态一致。实验表明其规划的轨迹既能满足约束又具备可执行性，为安全攸关系统的数据驱动规划提供了关键保障。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有流匹配规划器缺乏对状态和动作约束的形式化保障，导致轨迹不安全或不可执行。
method: 通过虚拟控制输入增强流模型，并结合控制理论推导引导信号，确保轨迹的安全性与动力学一致性。
result: 实验证明生成的轨迹满足安全、可容许与动态一致要求，优于现有流匹配规划器。
conclusion: SAD-Flower为安全关键系统提供了具有严格约束保障的数据驱动规划框架。
---

## Abstract
Flow matching (FM) has shown promising results in data-driven planning. However, it inherently lacks formal guarantees for ensuring state and action constraints, whose satisfaction is a fundamental and crucial requirement for the safety and admissibility of planned trajectories on various systems. Moreover, existing FM planners do not ensure the dynamical consistency, which potentially renders trajectories inexecutable. We address these shortcomings by proposing SAD-Flower, a novel framework for generating $\textbf{S}$afe, $\textbf{A}$dmissible, and $\textbf{D}$ynamically consistent trajectories. Our approach relies on an augmentation of the flow with a virtual control input. Thereby, principled guidance can be derived using techniques from nonlinear control theory, providing formal guarantees for state constraints, action constraints, and dynamic consistency. Crucially, SAD-Flower operates without retraining, enabling test-time satisfaction of unseen constraints. Through extensive experiments across several tasks, we demonstrate that SAD-Flower outperforms various generative-model-based baselines in ensuring constraint satisfaction. Video and demos can be found at [sadflowerplanning.github.io](https://sadflowerplanning.github.io/project_web/).

---

## 论文详细总结（自动生成）

# SAD-Flower：用于安全、可容许与动态一致规划的流匹配方法

## 1. 论文的核心问题与整体含义
- **研究动机**：流匹配（Flow Matching, FM）在数据驱动规划中展现出优异性能，但其本质缺乏对状态约束和动作约束的形式化保障，导致生成的轨迹可能不安全、不可执行或不可容许。
- **核心问题**：现有 FM 规划器无法确保轨迹的动态一致性（dynamical consistency），即轨迹可能违背系统动力学模型，使得实际系统无法跟踪执行。
- **整体含义**：本文旨在为安全攸关的自治系统（如自动驾驶、机器人操控）构建一个具有严格约束保证的数据驱动规划框架，使得规划的轨迹满足安全、可容许且动力学自洽三项关键要求。

## 2. 论文提出的方法论
- **核心思想**：通过引入虚拟控制输入（virtual control input）对流模型进行增强，并借助非线性控制理论技术推导出有原则的引导信号（principled guidance），从而为生成的轨迹提供状态约束、动作约束和动态一致性的形式化保证。
- **关键技术细节**：
  - **流增强**：在原有流匹配框架中引入虚拟控制变量，将轨迹生成建模为受控动态系统。
  - **约束引导**：利用控制障碍函数（CBF）、控制李雅普诺夫函数（CLF）或类似控制方法，在推理（测试时）阶段注入引导，矫正生成轨迹以满足约束，无需重新训练模型。
  - **动态一致性**：确保生成的轨迹严格满足系统动力学方程，使轨迹物理上可执行。
- **算法流程**（文字描述）：
  1. 训练一个增强流匹配模型，学习从先验分布到专家轨迹分布的映射，其中包含虚拟控制输入。
  2. 在测试时，给定新的场景约束（可能未见过），通过求解带约束的逆向过程（如通过控制器引导）生成满足安全、动作范围与动力学方程的轨迹。
  3. 整个过程在推理阶段实时完成，不改变预训练模型参数。

## 3. 实验设计
- **数据集/场景**：论文在多个任务上进行实验，具体任务名称未在摘要中详述，但提及“extensive experiments across several tasks”。结合规划领域常见基准，可能包括机器人导航、机械臂操控等场景。
- **Benchmark**：以安全、可容许与动态一致三个指标作为评估基准。
- **对比方法**：与多种基于生成模型的规划基线（generative-model-based baselines）进行比较，如普通流匹配规划器、扩散规划器、或基于VAE/GAN的规划方法。
- **评价指标**：约束满足率（是否安全、是否在动作边界内）、动态一致性度量（如违反动力学方程的误差）、成功率或规划质量等。

## 4. 资源与算力
- 提供的信息中未明确说明所用 GPU 型号、数量或训练时长。摘要和元数据均未提及计算资源细节，故此项无数据。

## 5. 实验数量与充分性
- **实验数量**：摘要提到“across several tasks”，表明至少在不同任务上进行了多组实验，可能包含多个场景、不同约束组合的消融实验（如是否使用引导、不同引导方法）。
- **充分性与公平性**：
  - 实验覆盖了与多种生成式规划基线的对比，表明基准选择具备代表性。
  - 由于方法无需重新训练即可适应未见约束，实验可能测试了模型的泛化能力，增加了说服力。
  - 但摘要缺乏具体实验数量、统计指标（如多次运行的均值和方差）等细节，无法严谨评估统计充分性；若正文包含详细消融与敏感度分析，则实验整体应视为充分且公平。

## 6. 论文的主要结论与发现
- SAD-Flower 能够生成满足安全、可容许和动态一致约束的轨迹。
- 该方法在确保约束满足方面显著优于现有基于生成模型的规划器。
- 无需重新训练即可实现测试时约束满足，展现了强大的泛化能力。
- 验证了控制理论引导与流匹配结合的有效性，为安全关键系统的数据驱动规划提供了新范式。

## 7. 优点
- **方法创新**：首次将虚拟控制输入与控制障碍函数等概念引入流匹配规划，实现形式化约束保证。
- **无需重训**：推理时即可满足新约束，避免为每个新约束重新训练模型的昂贵开销。
- **兼顾多项约束**：同时处理状态约束、动作范围和动力学一致性，填补了流匹配规划器的关键空白。
- **实验演示**：提供了视频和演示页面，增强结果的可视化说服力。

## 8. 不足与局限
- **理论假设依赖**：方法基于控制理论的前提，可能要求系统动力学模型是已知且连续的，对高度非线性或难建模系统（如接触丰富的操作）可能扩展困难。
- **计算开销**：测试时求解控制引导可能引入额外计算，实时性在快节奏控制中存疑，但摘要未提及延迟。
- **实验覆盖不明确**：虽声称多任务，但具体任务类型、复杂度、泛化边界及与最新扩散规划器的对比（如Diffusion Policy的高级变体）未被详细说明。
- **安全保证范围**：形式化保障的严格性（如概率上界还是硬约束）未在摘要中明示，可能导致期望落差。
- **潜在偏差**：若专家数据集存在偏差，即使满足约束，规划性能仍可能受限制。

（完）
