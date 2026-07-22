---
title: "TodoEvolve: Learning to Architect Agent Planning Systems"
title_zh: TodoEvolve：学习构建智能体规划系统
authors: "Jiaxi Liu, Guibin Zhang, Yanzuo Jiang, Zihan Zhang, Heng Chang, Zhenfei Yin, Qibing Ren, Junchi Yan"
date: 2026-04-30
pdf: "https://openreview.net/pdf/edc35abd0a8ed76f34162fb5481ab1759eaebc3f.pdf"
tags: ["query:av-pnc"]
score: 5.0
evidence: 智能体系统的元规划方法，动态修订规划架构，可潜在应用于自动驾驶规划
tldr: 针对固定规划结构难以适应开放性问题多样性的局限，本文提出TodoEvolve元规划范式，通过构建标准化规划元件库PlanFactory并收集高质量规划数据，训练元规划器自动合成与动态修订任务特定规划架构。实验表明该方法在多种复杂任务中优于固定基线，为智能体系统提供了自适应规划能力。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有智能体规划依赖手工设计的固定结构，缺乏对任务多样性的自适应能力。
method: 构建PlanFactory模块化设计空间，并基于此学习元规划器以自动合成和修订任务规划架构。
result: 在多种长时域任务上，TodoEvolve显著优于固定结构规划器，展现出更强的泛化性。
conclusion: TodoEvolve为构建自适应智能体规划系统提供了通用元学习框架。
---

## Abstract
Planning has become a central capability for contemporary agent systems in navigating complex, long-horizon tasks, yet existing approaches predominantly rely on fixed, hand-crafted planning structures that lack the flexibility to adapt to the structural diversity of open-ended problems. To address this limitation, we introduce TodoEvolve, a meta-planning paradigm that autonomously synthesizes and dynamically revises task-specific planning architectures. Specifically, we first construct PlanFactory, a modular design space that standardizes diverse planning paradigms within a unified codebase encompassing topology, initialization, adaptation, and navigation, thereby providing a common interface for heterogeneous planning patterns. Leveraging PlanFactory, we collect high-quality planning trajectories and train Todo-14B via Impedance-Guided Preference Optimization (IGPO), a multi-objective reinforcement learning objective that encourages the generation of planning systems that are performant, stable, and token-efficient across arbitrary tasks and agent backbones. Empirical evaluations on five agentic benchmarks demonstrate that TodoEvolve consistently surpasses carefully engineered planning modules while maintaining economical API costs and runtime overhead. Our codes are available at \url{https://github.com/EcthelionLiu/TodoEvolve}.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
- 当前智能体系统在执行复杂、长时域任务时，规划能力已成为核心瓶颈。
- 现有主流方法严重依赖固定、手工设计的规划结构（如固定的推理链、子任务分解方式），这种“一刀切”的设计难以适应开放世界中任务结构的极大多样性，导致在面对不同场景时缺乏必要的灵活性和自适应能力。
- 本文提出一种**元规划范式 TodoEvolve**，其核心思想是让智能体学会自动合成并动态修订针对具体任务的规划架构，从而突破固定模板的限制，实现更通用的任务解决能力。

### 2. 论文提出的方法论
- **核心思想**：将规划本身视为一个可学习、可优化的元过程，不再使用单一不变的规划拓扑结构。
- **关键模块 PlanFactory（规划工厂）**：
  - 构建了一个模块化设计空间，将各种异质的规划范式（如拓扑结构、初始化策略、自适应机制、导航方式等）标准化在一个统一的代码库中。
  - 提供了一套通用接口，使得不同的规划模式可以像搭积木一样被组合、表示和复用，为后续自动合成任务特定架构奠定基础。
- **训练数据与元训练目标**：
  - 利用 PlanFactory 收集大量高质量的规划轨迹数据。
  - 训练一个名为 **Todo-14B** 的元规划模型。
- **优化算法：阻抗引导偏好优化（Impedance-Guided Preference Optimization，IGPO）**：
  - IGPO 是一种多目标强化学习目标函数，旨在同时优化三个维度的特性：
    - **性能（Performance）**：生成的规划系统能够高效完成任务。
    - **稳定性（Stability）**：生成的规划序列在不同任务和智能体主干网络中表现可靠。
    - **令牌效率（Token-efficiency）**：生成的规划架构本身消耗的语言令牌少，从而控制 API 成本和运行时开销。

### 3. 实验设计
- **评估场景**：在 **5 个不同的智能体测评基准（agentic benchmarks）** 上进行了实验，具体基准名称在摘要中未列出，但属于长时域、复杂任务场景。
- **对比方法**：与一系列经过人工精心设计的规划模块进行了对比（摘要中称为“carefully engineered planning modules”）。
- **评估维度**：除了任务成功率等性能指标外，还重点考察了 **API 成本** 和 **运行时开销**，以验证其实际应用的性价比。

### 4. 资源与算力
- **所用模型**：训练了参数规模为 **14B** 的语言模型作为元规划器（Todo-14B），训练中使用了强化学习阶段的 IGPO 目标。
- **硬件细节**：**摘要及所提供文本中未明确说明** 所使用的 GPU 型号、卡数或具体的训练时长。通常 14B 模型的 RL 训练需要大规模算力，但原论文是否详述有待完整版本确认。

### 5. 实验数量与充分性
- **实验组数**：至少覆盖 5 个测评基准，加上与一系列人工设计基线的对比实验。摘要未提及详细的消融研究（如各模块贡献度、不同目标权重的分析），但从行文看，论文很可能包含对 PlanFactory 组件、IGPO 目标中各子项的消融实验（这在深度学习方法中是标配，但此处无法定论）。
- **充分性与公平性**：在多种任务上一致超越固定结构基线，并额外关注成本和延迟指标，实验设计较为全面。对比对象是人工设计的强基线，具有一定的公平性。但摘要信息有限，无法判断是否对所有基准都做到了严格的可复现性保障。

### 6. 论文的主要结论与发现
- TodoEvolve 能够超越固定的手工规划模块，在不同智能体基准上取得更优的性能。
- 同时，该方法能够维持较低的 API 使用成本和极小的时间开销，兼顾了性能和效率。
- 验证了“学习如何规划”这一元学习思想在智能体系统中的可行性与优越性，为构建高度自适应的智能体提供了通用框架。

### 7. 优点
- **范式创新**：首次将模块化设计空间与元规划学习结合，将“规划架构”本身视为需动态生成的产物，思路新颖。
- **实用性强**：通过 IGPO 同时优化性能、稳定性和令牌效率，直击现实部署中对成本和鲁棒性的要求。
- **可扩展性**：PlanFactory 统一了多种规划范式，便于未来整合新出现的规划策略，开源有利于社区跟进。
- **模型无关性**：声称可跨任意任务和智能体主干网络工作，具有一定的通用性。

### 8. 不足与局限
- **细节缺失**：摘要未提供 5 个基准的具体名称，也未描述收集规划轨迹的数据规模和质量控制，方法的普适性边界尚不明确。
- **任务复杂性上限**：虽然强调了“长时域任务”，但未给出任务的最大步数或逻辑深度，面对极端复杂的现实任务（如开放式科学研究）可能仍显不足。
- **训练成本隐晦**：14B 模型的 IGPO 训练通常需要可观的计算资源，但摘要未披露算力消耗，这对想要复现的团队不够友好。
- **泛化风险**：依赖 PlanFactory 中手工抽象出的规划原语，若遇到原库不支持的全新规划模式，系统能否无缝扩展存疑。

（完）
