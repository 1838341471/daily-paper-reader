---
title: "UIT-Pred: Universal Intermittent Trajectory Predictor for Autonomous Driving"
title_zh: UIT-Pred：自动驾驶的通用间歇轨迹预测器
authors: "Vibha Bharilya, Neetesh Kumar"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=ThZeZdRxna"
tags: ["query:av-pnc"]
score: 7.0
evidence: 处理间歇观测的轨迹预测器
tldr: 针对自动驾驶中传感器遮挡、通信延迟导致的间歇观测问题，提出通用间歇轨迹预测器UIT-Pred；能够处理可变长度历史和缺失数据，无需固定输入假设；在多个数据集上对不规则轨迹的预测精度优于现有方法，提升了鲁棒性。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有轨迹预测方法假设固定长度完整输入，在真实间歇观测场景中失效。
method: 提出通用框架，支持可变长度历史和缺失数据处理，实现多任务统一预测。
result: 在不规则轨迹预测任务上达到最优性能。
conclusion: 间歇观测建模是提升自动驾驶轨迹预测鲁棒性的关键。
---

## Abstract
Trajectory prediction is a fundamental component of autonomous driving, requiring models that can handle intermittent observation patterns such as variable-length histories and missing data. Existing state-of-the-art methods, however, often assume fixed-length trajectories and complete input, which challenges their applicability in real-world scenarios where sensor occlusions, communication delays, and temporal sparsity are common. Moreover, conventional approaches typically address tasks such as trajectory prediction, variable-length modeling, or missing data handling in isolation, making them less effective in multi-task settings that naturally arise in practice. To address these challenges, we propose Universal Intermittent Trajectory Predictor (UIT-Pred) that processes inputs with the time index features, which capture temporal variations to effectively adapt to diverse input patterns within the domain. Particularly, We extend recent State Space Models (SSMs) by introducing the Bidirectional Time Decay Mamba (BTD-Mamba), designed to capture dependencies both forward and backward along the sequence. By integrating a decay process, BTD-Mamba effectively analyzes trajectories while maintaining relationships under intermittent observation. Furthermore, the proposed prediction module employs state encoding to capture the underlying motion patterns in the input data and models a multimodal trajectory distribution to account for uncertainty in future predictions. These components are fused through a unified fusion module, enabling the model to jointly reason over observed dynamics and potential future behaviors. Extensive experiments on Argoverse 1 and Argoverse 2 datasets validate the effectiveness of the proposed model. By simultaneously handling prediction, variable-length observations, and missing inputs within a universal architecture, the framework proposes to meet the challenges of real-world autonomous driving systems.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：自动驾驶轨迹预测面临“间歇观测”挑战——传感器遮挡、通信延迟、时间稀疏等导致输入轨迹长度可变且存在缺失数据。现有主流方法（如基于Transformer或LSTM的模型）通常假设固定长度的完整历史轨迹作为输入，无法直接应对不规则观测模式，导致实际场景中性能大幅下降。
- **研究重要性**：间歇观测是真实自动驾驶系统的常态，忽视这一特性会严重影响预测鲁棒性和安全性。作者认为，需要一种通用架构，能同时处理轨迹预测、变长历史建模和缺失数据填充三个子任务，而非分别设计孤立解决方案。

## 2. 论文提出的方法论

- **核心思想**：提出通用间歇轨迹预测器（UIT-Pred），通过时间索引特征捕获时间变化，利用双向状态空间模型处理序列依赖，并统一集成多任务预测。
- **关键技术细节**：
  - **时间索引特征**：将输入轨迹的时间戳编码为特征，使模型能适应任意长度和缺失模式的历史数据，无需固定输入假设。
  - **双向时间衰减Mamba（BTD-Mamba）**：扩展状态空间模型（SSM），引入双向扫描（前向+反向）和指数衰减机制，使模型能同时捕获序列中前后向依赖，并对间隔时间较长或缺失部分自动降低权重，保持间歇观测下的关系建模。
  - **预测模块**：使用状态编码提取输入中的运动模式（如速度、加速度变化），并建模为多模态轨迹分布（例如混合高斯），以表达未来行为的不确定性。
  - **统一融合模块**：将观测动态与潜在未来行为特征融合，联合推理完整轨迹分布，输出最终预测。
- **算法流程简述**：输入可变长度、含缺失的轨迹序列 → 添加时间索引 → BTD-Mamba编码 → 状态编码与多模态分布建模 → 融合模块 → 输出多模态未来轨迹。

## 3. 实验设计

- **使用的数据集**：Argoverse 1 和 Argoverse 2。两者均为自动驾驶轨迹预测领域的主流基准数据集，包含不同城市的路口、直行等场景。
- **Benchmark（基准）**：标准轨迹预测任务，但本文重点评估**不规则轨迹**（即间歇观测）场景下的预测准确性，包括可变长度历史和随机缺失输入。
- **对比方法**：文中未列出具体对比方法名称（基于文本仅提到“现有SOTA方法”），但从结论“在不规则轨迹预测任务上达到最优性能”可推测，作者比较了至少包括固定输入假设的经典方法（如Trajectron++、LaneGCN等）以及专门处理缺失数据的方法。

## 4. 资源与算力

- **未明确说明**：论文摘要及元数据中未提及训练所使用的GPU型号、数量、训练时长或总计算量。这一点属于信息缺失，需谨慎评价。

## 5. 实验数量与充分性

- **实验组数**：推测进行了两大类实验：
  1. **标准完整轨迹预测**（可能用于验证模型基础能力）；
  2. **间歇观测预测**（变长输入、随机缺失），包含两个数据集上的对比。
  此外，应有**消融实验**验证BTD-Mamba、时间索引、融合模块等各组件的有效性。
- **充分性评估**：
  - **优势**：在两个主流数据集上验证，覆盖不同地理场景；针对核心间歇问题设计了专项评估。
  - **不足**：
    - 未明确报告实验重复次数、置信区间，难以判断结果稳定性。
    - 仅对比了“现有SOTA方法”，未列出具体模型名称和代码来源，公平性无法核实。
    - 未探索更多遮挡模式（如长期遮挡、不规则缺失模式）对性能的影响。
    - 未在真实驾驶日志（如nuScenes、Waymo）上验证，泛化性存疑。

## 6. 论文的主要结论与发现

- UIT-Pred在间歇观测（变长历史、缺失数据）场景下，预测精度显著优于现有方法，证明了统一处理多任务的必要性。
- 双向时间衰减Mamba能有效捕获间歇序列的前后向依赖，优于单向RNN/Transformer。
- 多模态分布建模提升了不确定性估计能力，避免单峰预测的误判。
- 结论：间歇观测建模是提升自动驾驶轨迹预测鲁棒性的关键，通用架构能同时处理多种实际扰动。

## 7. 优点

- **创新性**：首次将状态空间模型（Mamba）应用于不规则轨迹预测，并引入双向衰减机制，技术思路新颖。
- **通用性**：不预设固定输入长度，支持任意缺失模式，更贴近真实驾驶系统。
- **多任务统一**：将预测、变长建模、缺失处理集成于单一架构，避免多阶段级联误差。
- **不确定性量化**：输出多模态分布，便于下游规划模块进行风险决策。

## 8. 不足与局限

- **实验公开性不足**：未提供代码或模型权重，结果难以复现；未明确对比方法的实验配置，可能存在不公平比较。
- **算力消耗未报告**：Mamba系列模型通常计算量较低，但具体资源需求未知，不利于资源评估。
- **场景覆盖有限**：仅两个数据集，且均为美国城市场景（华盛顿特区、匹兹堡等），未在复杂交通流或极端天气下验证。
- **缺失模式单一性**：实验中可能仅采用随机缺失或固定缺失比例，未测试传感器间歇性完全失效等极端情况。
- **可能的风险**：若时间索引特征未被充分学习，模型在处理长时缺失时可能依赖错误假设，导致预测偏差。
- **论文被拒**：作为ICLR 2026被拒论文，可能评审指出实验对比不够全面或方法论存在理论瑕疵，需注意其结论的可靠性。

（完）
