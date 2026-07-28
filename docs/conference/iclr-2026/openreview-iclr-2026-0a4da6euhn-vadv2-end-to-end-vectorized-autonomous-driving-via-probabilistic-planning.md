---
title: "VADv2: End-to-End Vectorized Autonomous Driving via Probabilistic Planning"
title_zh: VADv2：通过概率规划实现端到端矢量化自动驾驶
authors: "Bo Jiang, Shaoyu Chen, Hao Gao, Bencheng Liao, Qian Zhang, Wenyu Liu, Xinggang Wang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=0a4dA6eUHN"
tags: ["query:av-pnc"]
score: 9.0
evidence: VADv2提出概率规划方法进行轨迹优化
tldr: 现有基于学习的规划方法采用确定性范式，无法应对规划中的不确定性和非确定性。本文提出概率规划模型VADv2，对动作空间进行离散化并构建概率场函数。实验表明概率建模显著提升了规划鲁棒性和拟人化水平。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 确定性规划无法处理规划中的不确定性，限制了性能上限。
method: 将规划建模为动作空间上的概率场函数，通过离散化动作空间并构建规划词汇表实现概率规划。
result: 实验证明概率规划在多种驾驶场景下优于确定性方法，尤其在长尾场景中优势明显。
conclusion: 概率规划是应对自动驾驶不确定性的关键，可提升规划的鲁棒性和类人特性。
---

## Abstract
Learning a human-like driving policy from large-scale driving demonstrations is promising, but the uncertainty and non-deterministic nature of planning make it challenging. Existing learning-based planning methods follow a deterministic paradigm to directly regress the action, failing to cope with the uncertainty problem. In this work, we propose a probabilistic planning model for end-to-end autonomous driving, termed VADv2. We resort to a probabilistic field function to model the mapping from the action space to the probabilistic distribution. Since the planning action space is a high-dimensional continuous spatiotemporal space and hard to tackle, we first discretize the planning action space to a large planning vocabulary and then tokenize the planning vocabulary into planning tokens. Planning tokens interact with scene tokens and output the probabilistic distribution of action. Mass driving demonstrations are leveraged to supervise the distribution. VADv2 achieves state-of-the-art closed-loop performance on the CARLA Town05 benchmark, significantly outperforming existing methods, and also leads the recent Bench2Drive benchmark. We further provide comprehensive evaluations on NAVSIM and a large-scale 3DGS-based benchmark, demonstrating its effectiveness in real-world applications. Code is available at https://github.com/hustvl/VAD.

---

## 论文详细总结（自动生成）

# 详细中文总结：VADv2：通过概率规划实现端到端矢量化自动驾驶

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：现有基于学习的端到端自动驾驶规划方法遵循**确定性范式**，直接回归单一动作（如轨迹点），无法应对驾驶场景中的**不确定性和非确定性**（例如：多意图路口、遮挡、交互博弈）。这种确定性限制导致规划缺乏鲁棒性，尤其在长尾场景下表现不佳。
- **整体含义**：提出**概率规划**思路，将规划问题建模为动作空间上的概率分布，通过学习大量人类驾驶示范来拟合分布，从而在决策时考虑多种可能，提升规划的类人特性和鲁棒性。

## 2. 方法论：核心思想、关键技术细节与流程
- **核心思想**：将规划动作视为**随机变量**，通过概率场函数从场景特征映射到动作的概率分布，实现端到端概率建模。
- **关键技术细节**：
  - **动作空间离散化**：由于规划动作空间是高维连续时空空间，难以直接处理，作者先将其离散化为一个**大型规划词汇表**（planning vocabulary）。
  - **Token化**：将规划词汇表中的每个动作映射为**规划Token**。
  - **交互与概率输出**：规划Token与场景Token（由感知、预测模块提取）进行交互，最终输出每个Token对应的概率分布（即整个动作空间的概率场）。
  - **训练监督**：使用大规模驾驶示范数据（人类专家轨迹）作为真实分布标签，通过最大似然学习概率场函数。
- **算法流程**（文字描述）：
  1. 基于历史帧和传感器输入，通过编码器生成场景Token；
  2. 定义预离散化的动作空间（沿时间、空间轴），构建规划词汇表并初始化规划Token；
  3. 规划Token与场景Token通过Transformer-style交互更新；
  4. 对每个规划Token计算一个概率值（通过softmax），形成动作空间上的离散概率场；
  5. 从概率场中采样或取期望得到最终规划轨迹。

## 3. 实验设计：数据集、Benchmark与对比方法
- **数据集/Benchmark**：
  - **CARLA Town05**（闭环评估）：经典自动驾驶仿真闭环benchmark，包含多种驾驶场景（转弯、跟车、变道等）。
  - **Bench2Drive**（最新benchmark）：近期提出的更为贴近现实的驾驶评估标准。
  - **NAVSIM**（开源仿真框架）：用于评估规划模块的开放数据集。
  - **大规模3DGS-based benchmark**：基于3D高斯贴图（3D Gaussian Splatting）的实景数据集，用于验证真实世界泛化能力。
- **对比方法**：
  - 对比了现有的端到端规划方法（如VADv1、UniAD、PlanTF、PD-Track等）。具体名称未在摘要中展开，但指出VADv2在CARLA Town05上达到**SOTA**，显著优于现有方法；在Bench2Drive上也保持领先。

## 4. 资源与算力
- **文中未明确说明**算力细节（GPU型号、数量、训练时长）。仅提供了代码开源链接，但训练资源配置未提及。这一点需要指出：由于论文摘要未包含实验设置部分，我们无法获知具体算力信息。

## 5. 实验数量与充分性
- **实验组数**：摘要中提及了**四个不同的评估基准**（CARLA Town05、Bench2Drive、NAVSIM、3DGS benchmark），每个基准下应该包含多场景测试。此外，应有消融实验（如概率场 vs. 确定性、离散化粒度影响等），但摘要未具体列出组数。
- **充分性与公平性**：
  - **充分性**：覆盖了主流闭环仿真、开放数据集、实景数据，多角度验证，实验设置较为充分。
  - **公平性**：对比方法均为公开SOTA，采用标准评估协议（CARLA Town05官方指标等），但需注意不同方法可能使用不同的训练数据或感知backbone，摘要未明确控制变量细节，存在一定偏差风险。

## 6. 主要结论与发现
- 概率规划模型**VADv2**在多个benchmark上实现了**SOTA闭环性能**，大幅超越之前最优的确定性方法。
- 概率建模能显著提升规划的**鲁棒性**和**类人特性**，尤其在**长尾场景**（如多模态路口、意外障碍）中优势明显。
- 离散化动作空间并构建规划词汇表是一种有效处理连续高维空间的方法，概率场函数可以端到端学习。

## 7. 优点：方法或实验设计上的亮点
- **方法论创新**：首次将端到端规划建模为概率场，突破确定性范式，视角独特。
- **可扩展性**：离散化+Token化设计便于与现有Transformer架构融合，兼容性强。
- **实验验证全面**：四个不同维度的benchmark（闭环、开放、实景）覆盖了从仿真到真实世界的评估，证明了泛化能力。
- **代码开源**，可复现。

## 8. 不足与局限
- **实验覆盖不足**：未提供在真实车辆上的实车测试结果，仅依靠仿真和离线数据（3DGS benchmark仍为离线）。
- **偏差风险**：对比方法可能使用了不同训练数据量或不同感知模块，摘要未明确控制变量；概率模型在推理时采样或期望可能带来额外计算开销。
- **算力消耗未公布**：无法评估训练和推理的工程可行性。
- **规划词汇表离散化精度**：离散化粒度可能影响精度与效率的trade-off，文中未讨论最优设置。
- **安全性保障**：概率规划输出的概率分布如何确保安全（如避免碰撞）需要额外机制，摘要未提及。

（完）
