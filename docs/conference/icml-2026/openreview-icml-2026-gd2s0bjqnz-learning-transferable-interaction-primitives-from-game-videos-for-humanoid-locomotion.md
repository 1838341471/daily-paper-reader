---
title: Learning Transferable Interaction Primitives from Game Videos for Humanoid Locomotion
title_zh: 从游戏视频学习可迁移交互原语用于人形运动
authors: "Xiangming Zhu, Huayu Deng, Haoran Zhao, Yiwei Hao, Yunbo Wang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/cb77deec6df361019a80b3b74359f8e7bebe5fc1.pdf"
tags: ["query:traj-pred"]
score: 4.0
evidence: 人类运动与环境交互原语，但面向运动控制而非轨迹预测。
tldr: 人形机器人运动控制普遍缺乏高质量真机数据，现有方法多将视频作为被动运动先验。该文提出TRIP框架，从无标注游戏视频中提取与场景交互的可迁移动作原语，并构建离散交互原语库对运动与环境依赖建模。实验证明迁移到真实人形运动场景后仍能保持鲁棒性。该工作为从视频学习运动交互提供了新思路，但与轨迹预测任务仍有距离。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 人形运动控制面临真实数据稀缺，视频常被当作被动先验，未利用动态交互信息。
method: 提出TRIP框架，从无标注游戏视频中提取离散交互原语库，显式建模运动与环境依赖并跨域迁移。
result: 实验表明该交互原语能提升人形机器人多种场景下的运动控制鲁棒性。
conclusion: 为从视频学习可迁移人类运动交互提供了新方法，但主要服务控制而非预测。
---

## Abstract
Learning humanoid control from video provides a scalable alternative to the scarcity of high-fidelity robot data. Existing methods, however, often rely on curated datasets and treat video as passive kinematic priors. They fail to capture dynamic humanoid interactions with the environment, which are essential for robust control in complex physical environments. To address this, we propose ***TR**ansferable **I**nteraction **P**rimitives (TRIP)*, a framework designed to extract and ground interactions from unlabeled game videos for locomotion control. TRIP explicitly models dependencies between motion dynamics and environmental context via a discrete library of interaction-based action primitives. To bridge the reality gap, we introduce a shared context latent space that aligns implicit video-domain features with functional target-domain observations, enabling the seamless transfer of video-mined strategies to reinforcement learning policies. Our experiments on complex terrain navigation demonstrate that TRIP achieves significant improvements in task performance, sample efficiency, and robustness.

---

## 论文详细总结（自动生成）

# 论文总结：从游戏视频学习可迁移交互原语用于人形运动

## 1. 核心问题与整体含义

- **研究背景**：人形机器人运动控制长期受限于高质量真机数据稀缺，从视频中学习成为一种可扩展的替代方案。
- **现有方法不足**：已有方法往往依赖精心策划的数据集，且仅将视频视为**被动的运动学先验**，未充分利用其中包含的人类与环境的动态交互信息，而这类交互对复杂物理环境下的鲁棒控制至关重要。
- **研究动机**：如何从**无标注的游戏视频**中提取可迁移的交互信息，并将其用于人形运动控制，是本论文的核心问题。
- **整体含义**：该工作提出了一种从视频学习可迁移运动交互的新框架，为缓解真机数据稀缺、提升复杂地形下运动控制的鲁棒性提供了新思路。

## 2. 方法论：TRIP框架

- **核心思想**：提出 **TRIP（Transferable Interaction Primitives，可迁移交互原语）**，从无标注游戏视频中提取并落地交互信息，用于运动控制。
- **关键技术细节**：
  - **离散交互原语库**：显式建模运动动态与**环境上下文**之间的依赖关系，将交互模式编码为离散的原语集合。
  - **共享上下文潜在空间**：为了弥合视频域与真实目标域之间的**现实差距**，引入一个共享的上下文隐空间，将视频域中的隐式特征与目标域中的功能性观测进行对齐。
  - **策略迁移**：利用对齐后的视频挖掘策略指导强化学习（RL）策略的训练，实现跨域迁移。
- **算法流程（文字说明）**：
  1. 从无标注游戏视频中提取运动与环境交互模式；
  2. 将交互模式构建为离散原语库；
  3. 通过共享上下文潜在空间对齐视频域特征与目标域观测；
  4. 将视频中挖掘的策略迁移至强化学习策略中，用于人形机器人运动控制。

## 3. 实验设计

- **数据集/场景**：文中提及实验在**复杂地形导航**任务上进行，具体数据集名称、来源及预处理方式在提供的文本中**未明确说明**。
- **Benchmark**：未指明使用了哪些标准 benchmark 或基线环境。
- **对比方法**：文本中未列出具体对比方法，仅从表述推断与“依赖策划数据集、将视频视为被动先验”的现有方法进行了比较。

## 4. 资源与算力

- **文中未明确说明**使用的 GPU 型号、数量、训练时长等计算资源信息。
- 因此无法评估其训练成本和可复现性。

## 5. 实验数量与充分性

- **实验数量**：从提供的文本看，仅提及“复杂地形导航”上的实验，**未给出具体的实验组数、消融实验、跨场景迁移实验**等细节。
- **充分性评估**：
  - 由于缺少具体的实验配置、基线和消融细节，**难以充分判断实验的客观性与公平性**。
  - 结论中声称“显著提升任务性能、样本效率和鲁棒性”，但缺乏具体量化指标和对比表格支撑。

## 6. 主要结论与发现

- TRIP 框架能够从无标注游戏视频中有效提取可迁移的交互原语。
- 在复杂地形导航任务中，TRIP 相比现有方法在**任务性能、样本效率和鲁棒性**上均有显著提升。
- 该工作验证了利用游戏视频中的动态交互信息辅助人形运动控制的可行性。

## 7. 优点

- **无需标注**：直接利用无标注游戏视频，降低数据获取成本。
- **显式交互建模**：通过离散交互原语库显式建模运动与环境依赖，优于被动运动先验方法。
- **跨域迁移设计**：共享上下文潜在空间有效弥合视频域与真实域之间的差距。
- **任务价值**：提升样本效率和鲁棒性，对真实人形机器人控制具有潜在实用价值。

## 8. 不足与局限

- **任务范围有限**：主要面向**运动控制**而非轨迹预测，对于轨迹预测类任务适用性存疑（据论文筛选元数据）。
- **实验细节缺失**：未给出具体数据集、基线方法、量化指标和消融实验，实验的客观性和充分性难以评估。
- **算力信息缺失**：未报告训练资源和时间，影响可复现性评估。
- **偏差风险**：游戏视频与真实物理环境仍存在较大差距，跨域迁移的泛化能力有待更多场景验证。
- **应用限制**：目前主要支持运动控制场景，对复杂操作或非结构化环境（如人机交互、精细操作等）未做讨论。

（完）
