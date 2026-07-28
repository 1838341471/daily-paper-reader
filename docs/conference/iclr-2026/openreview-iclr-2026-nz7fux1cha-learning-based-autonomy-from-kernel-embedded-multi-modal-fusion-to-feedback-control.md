---
title: Learning-Based Autonomy from Kernel-Embedded Multi-modal Fusion to Feedback Control
title_zh: 从核嵌入多模态融合到反馈控制的学习型自主驾驶
authors: Lakshman Mahto
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=nZ7fUX1cHa"
tags: ["query:av-pnc"]
score: 8.0
evidence: 基于核嵌入的多模态融合与反馈控制用于自动驾驶
tldr: 提出一个端到端自主驾驶循环，将核嵌入的多模态融合与数据驱动动力学学习及反馈控制相结合。使用再现核希尔伯特空间嵌入异构传感器流，通过核岭回归或贝叶斯神经网络学习动力学，并利用动态规划或强化学习综合策略。给出了闭式估计和有限样本复杂度分析。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有自主驾驶系统在多模态融合与控制之间缺乏统一的理论框架。
method: 利用核嵌入实现多模态融合，结合数据驱动动力学学习与反馈控制优化策略。
result: 在仿真中验证了方法的有效性，并提供了理论保证。
conclusion: 核方法为端到端自主驾驶提供了可解释且高效的理论基础。
---

## Abstract
In this work, we develop an end-to-end autonomy loop that couples \emph{kernel-embedded} multi-modal fusion with data-driven dynamics learning and feedback control. Heterogeneous sensor streams are embedded into a joint Reproducing Kernel Hilbert Space (RKHS) via additive/product kernels and conditional mean embeddings; dynamics are learned with kernel ridge regression (KRR), Deep Kernel Learning (DKL), or Bayesian deep neural networks (BDNNs); and policies are synthesized via dynamic programming (discrete and continuous-time HJB) or reinforcement learning with RKHS value functions. We present closed-form estimators, finite-sample and iteration-complexity characterizations, risk-sensitive planning with uncertainty, and safety via control barrier functions. We provide deployable algorithms, results and experiment in simulated robotics and precision irrigation.

---

## 论文详细总结（自动生成）

### 1. 核心问题与整体含义（研究动机和背景）

- 现有自主驾驶（或更广泛的自主系统）在多模态传感器融合与控制策略设计之间缺乏统一的理论框架，通常将感知、预测、规划和控制模块化分离，难以保证端到端的可解释性和理论最优性。
- 本文旨在构建一个端到端自主循环，将**核嵌入的多模态融合**、**数据驱动动力学学习**与**反馈控制**有机结合，形成一个可理论分析且可部署的闭环系统。

### 2. 方法论：核心思想、关键技术细节

- **核心思想**：利用再生核希尔伯特空间（RKHS）作为统一表示空间，对异构传感器流（如相机、激光雷达、IMU）进行嵌入融合，再在该空间内进行动力学学习和控制策略综合。
- **关键技术细节**：
  - **多模态融合**：通过加性核（additive kernels）、乘积核（product kernels）和条件均值嵌入（conditional mean embeddings）将不同传感器数据映射到联合RKHS。
  - **动力学学习**：采用核岭回归（KRR）、深度核学习（DKL）或贝叶斯深度神经网络（BDNN）从嵌入数据中学习系统动态。
  - **策略合成**：使用动态规划（离散时间或连续时间HJB方程）或强化学习（RKHS值函数）求解最优控制策略。
  - **理论性质**：给出了闭式估计、有限样本复杂度分析、风险敏感规划（处理不确定性）以及通过控制屏障函数（CBF）保证安全的方法。
- **算法流程（文字描述）**：  
  ① 传感器数据通过核嵌入融合为RKHS中的特征表示；  
  ② 利用KRR/DKL/BDNN学习系统的转移模型或动力方程；  
  ③ 基于学习到的动力学，利用HJB或RL求解价值函数并得到反馈控制律；  
  ④ 引入风险敏感项和安全屏障约束，在线调整控制输出。

### 3. 实验设计

- **使用场景**：仿真环境中的机器人操作任务和精准灌溉（precision irrigation）场景。
- **Benchmark**：文中未明确提及具体的标准benchmark数据集或对比方法。
- **对比方法**：未列出与其他基线方法的定量比较，主要展示自身框架的可行性。

### 4. 资源与算力

- 论文未明确说明所使用的GPU型号、数量、训练时长等算力细节。

### 5. 实验数量与充分性

- 文中仅提及“在仿真中验证了方法的有效性”，未报告具体的实验组数、消融实验、超参数敏感性分析或统计显著性测试。
- **充分性评价**：实验覆盖范围较窄，缺乏真实世界数据和与现有方法的直接对比，不足以充分验证方法的泛化能力和实际优势。

### 6. 主要结论与发现

- 核嵌入方法为端到端自主驾驶提供了一个可解释且高效的理论基础。
- 所提出的融合-学习-控制循环能够在仿真任务中成功运行，并能结合理论保证（如有限样本复杂度、安全屏障）。

### 7. 优点

- **统一理论框架**：首次将核方法贯穿多模态融合、动力学学习和反馈控制全过程，具有闭式解和复杂度分析。
- **可解释性**：RKHS中的操作（如内积、核函数）提供了数学透明性。
- **灵活性**：支持多种学习器（KRR/DKL/BDNN）和控制范式（DP/RL），可通过风险敏感和CBF融入安全约束。

### 8. 不足与局限

- **实验不足**：仅进行了仿真验证，缺乏真实机器人或实车实验；未与现有方法（如LSTM-based融合、MPC、ILQR等）做定量对比。
- **偏差风险**：仿真环境可能过于理想，未考虑传感器噪声、延迟、缺失等实际问题。
- **应用限制**：核嵌入在高维或大规模数据下可能面临计算效率问题；CBF对模型准确性要求较高，学习误差可能破坏安全保证。
- **可复现性**：未提供代码或详细的数据集描述，实验结果难以复现。

（完）
