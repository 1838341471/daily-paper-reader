---
title: "Flow for Future: Geometric SE(3)-Equivariant Flow Matching for 3D Trajectory Prediction"
title_zh: 面向未来流动：用于3D轨迹预测的几何SE(3)-等变流匹配
authors: "Junwei Wu, Yihang Liu, Ruixuan Yu, Jian Sun"
date: 2026-04-30
pdf: "https://openreview.net/pdf/b841463fb81506a8b833fbd0bb1a0e07cd61e7c4.pdf"
tags: ["query:traj-pred"]
score: 8.0
evidence: 生成式流匹配用于3D轨迹预测并保持SE(3)等变性
tldr: 3D轨迹预测需要捕获复杂时空依赖并保持物理对称性，而传统生成模型难以同时满足。本文提出GSE-Flow，将流匹配扩展到SE(3)-等变动力学，设计一致序列编码和时间调制嵌入来统一历史与演化流，并通过几何特征张量化机制提升预测精度。在相关基准上，该方法相比现有基线取得了更优的预测性能和对称性保持。这一框架为物理感知的3D轨迹生成提供了通用方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 3D轨迹预测需兼顾复杂时空依赖与物理对称性，现有生成模型难以兼顾。
method: 提出SE(3)-等变流匹配框架，结合序列编码、时间调制嵌入和几何特征张量化。
result: 在3D轨迹预测基准上相较基线显著提升预测精度与等变性。
conclusion: 为物理对称性约束下的生成式轨迹预测提供了可行范式。
---

## Abstract
Predicting 3D geometric  trajectory requires capturing complex spatiotemporal dependencies while  preserving  physical symmetries. While flow matching offers a powerful generative paradigm, extending it to SE(3)-equivariant dynamics is challenging due to the inherent gap between deterministic history and stochastic evolving flows. To address this, we introduce GSE-Flow, an SE(3)-equivariant flow matching framework. We first propose a Coherent Sequence Encoding and Time-Modulated Embedding strategy that unifies historical and evolving streams, incorporating velocity and flow time via equivariant affine transformations to guide continuous evolution. We further design a Geometry-Feature Tensorization mechanism that projects node states into a tensor product space, enabling Context-Flow Fusion to guide trajectory evolution with historical context. GSE-Flow guarantees theoretical SE(3)-equivariance and achieves SOTA accuracy on MD17, MD22, and CMU MoCap benchmarks for geometric trajectory prediction, while demonstrating generality by enhancing deterministic baselines.  Code is available at https://github.com/aegine/GSE-Flow.

---

## 论文详细总结（自动生成）

### 1. 核心问题与整体含义

- **研究动机**：3D 几何轨迹预测（如分子动力学、人体动作捕捉等）需要同时捕捉复杂的时空依赖关系，并保持物理世界中的对称性（尤其是 SE(3) 平移与旋转等变性）。
- **现存挑战**：流匹配（Flow Matching）是一种强大的生成式建模范式，但将其推广到 SE(3)-等变动力学中并不容易；核心难点在于“确定性的历史信息”与“随机演化的流场”之间存在本质鸿沟，难以统一建模。
- **整体意义**：论文提出 GSE-Flow，一个 SE(3)-等变流匹配框架，试图在生成式轨迹预测中同时保证物理对称性与高精度，为物理感知的 3D 轨迹生成提供通用方案。

### 2. 方法论

- **核心思想**：通过将历史轨迹与演化流统一到等变流匹配框架中，使得轨迹生成过程满足 SE(3) 等变性，同时利用几何特征增强预测精度。
- **关键技术 1：Coherent Sequence Encoding and Time-Modulated Embedding（一致序列编码与时间调制嵌入）**
  - 统一历史信息流与演化流。
  - 将速度和流时间（flow time）通过等变仿射变换引入模型，以引导轨迹的连续演化。
- **关键技术 2：Geometry-Feature Tensorization（几何特征张量化）**
  - 将节点状态投影到张量积空间（tensor product space）。
  - 在此基础上实现“上下文-流融合”（Context-Flow Fusion），使历史上下文能够持续引导轨迹演化。
- **理论保证**：该方法在理论上保证了 SE(3)-等变性。

### 3. 实验设计

- **使用数据集 / Benchmark**：
  - MD17：分子动力学轨迹预测基准。
  - MD22：涵盖更大/更复杂分子体系的动力学基准。
  - CMU MoCap：人体动作捕捉轨迹预测基准。
- **对比方法**：摘要/元数据中未明确列出具体基线名称，但提到“相较于现有基线取得更优性能”，并额外验证了该方法可以增强确定性基线模型。
- **实验任务**：3D 几何轨迹预测，涉及物理对称性保持与生成式预测质量。

### 4. 资源与算力

- 论文元数据与摘要中**未说明**使用的 GPU 型号、数量、训练时长等具体算力信息。
- 也未提及推理成本、参数量或训练开销。
- 注意：由于当前获取到的内容仅包含摘要和元数据，无法从正文中进一步获取相关细节。

### 5. 实验数量与充分性

- **实验数量**：至少覆盖 3 个主流 benchmark（MD17、MD22、CMU MoCap），并进行了“增强确定性基线”的泛化性验证。
- **充分性评估**：
  - 数据集横跨分子动力学与人体动作捕捉，具有领域多样性，且都是 3D 轨迹预测的常用公开基准，因此实验设置有一定代表性。
  - 但摘要中未给出消融实验、参数敏感性、等变性误差定量分析等细节；也没有列出与具体 SOTA 方法的误差对比数字。
  - 因此，从现有信息看实验设计“初步充分”，但无法完全判断其公平性与客观性，需要阅读完整论文来确认。

### 6. 主要结论与发现

- GSE-Flow 在 MD17、MD22 和 CMU MoCap 上取得了最优（SOTA）预测精度。
- 模型具备理论上的 SE(3)-等变性，能够更好地保持物理对称性。
- 该框架具有通用性，不仅可以单独作为生成模型使用，还能用于增强确定性轨迹预测基线。
- 总体上，为“物理对称性约束下的生成式轨迹预测”提供了一种可行且有效的范式。

### 7. 优点

- **理论性强**：明确保证 SE(3)-等变性，而不仅仅是经验上近似。
- **方法创新**：将流匹配与几何张量化结合，提出统一历史与演化的编码机制。
- **实验覆盖较广**：分子体系和人体运动两类不同领域均验证了有效性。
- **通用性**：可以增强确定性基线，说明其具有即插即用潜力。
- **开源**：提供了代码仓库，便于复现与进一步研究。

### 8. 不足与局限

- **信息受限**：当前可获取内容仅为摘要和元数据，缺少完整方法细节、公式推导、实验设置和对比表格，因此无法对结果进行独立验证。
- **基线不明确**：摘要未列出具体对比方法，难以评估“SOTA”的适用范围和比较公平性。
- **等变性范围有限**：只考虑 SE(3) 对称性，可能未覆盖其他物理对称性（如时间反演、置换对称性等）。
- **应用边界**：实验集中在分子动力学和动作捕捉，未涉及更多 3D 轨迹预测场景（如自动驾驶、机器人操控等）。
- **未报告算力与成本**：没有提供训练/推理资源信息，不利于实际部署评估。

（完）
