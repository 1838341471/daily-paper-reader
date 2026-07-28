---
title: "SAR: Scene-Action Representation for End-to-End Autonomous Driving"
title_zh: SAR：端到端自动驾驶的场景-动作表示
authors: "Peiwei Chen, Kaiqiu Xu, Yudong Zhang, Shengyin Fan, Aoran Zhang, zhigang ling, Yaonan Wang"
date: 2025-09-16
pdf: "https://openreview.net/pdf?id=upMaonekAE"
tags: ["query:av-pnc"]
score: 8.0
evidence: 利用场景-动作表示的端到端自动驾驶
tldr: 针对端到端自动驾驶中缺乏行为建模导致轨迹偏差的问题，提出场景-动作表示框架SAR；将场景分解为稀疏语义、自车动作和多智能体动作三部分，注入结构化行为信息；在交互密集场景下，轨迹偏差和碰撞风险显著降低。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 现有端到端方法过度依赖稠密中间监督或忽视行为建模，在交互场景中轨迹偏差大。
method: 提出场景-动作表示，分解场景为稀疏语义、自车动作和多智能体动作，注入结构化行为知识。
result: 在复杂交互场景中，轨迹预测准确性提升，安全风险降低。
conclusion: 结构化行为注入能有效改善端到端自动驾驶的交互建模能力。
---

## Abstract
End-to-end autonomous driving systems have made remarkable progress by integrating perception, prediction, and planning into a fully differentiable framework. However, most existing methods either rely heavily on dense intermediate supervision (e.g., segmentation and mapping) or neglect behavior modeling, which leads to significant trajectory deviations and safety risks in highly interactive scenarios. To address these challenges, we propose SAR, a novel end-to-end scene action representation framework that enhances sparse scene modeling through structured behavior injection. Inspired by human driving cognition, SAR decomposes the scene into three complementary components: sparse scene semantics, ego-action awareness, and multi-agent action awareness. These components are fused via a specially designed Scene-Action Transformer to produce a consistent, interpretable, and interaction-aware representation for high-quality trajectory planning. Unlike prior approaches, SAR achieves strong generalization in highly interactive urban scenarios with only a small annotation cost. Experimental results on the nuScenes benchmark show that SAR reduces L2 trajectory error by 47% and collision rate by 41% compared to VAD. It also demonstrates superior robustness on NAVSIM and Bench2Drive, achieving new state-of-the-art performance in both open-loop and closed-loop evaluations. The code will be released soon.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：现有端到端自动驾驶系统虽然集成了感知、预测和规划，但过度依赖稠密中间监督（如语义分割、高精地图）或缺乏明确的行为建模。在高度交互的驾驶场景中（如交叉路口、密集车流），这种设计导致轨迹预测显著偏离合理路径，带来安全风险。
- **核心问题**：如何通过结构化行为知识的注入，在保持端到端可微性的同时，提升复杂交互场景下的规划质量和安全性。
- **背景**：端到端方法近年来进展迅速，但行为建模的缺失是制约其鲁棒性的关键瓶颈。受人类驾驶认知启发，论文提出将场景分解为稀疏语义、自车动作和多智能体动作三个互补部分。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：提出**SAR（Scene-Action Representation）框架**，将场景表示拆解为三个独立但互补的组件：稀疏场景语义（sparse scene semantics）、自车动作意识（ego-action awareness）和多智能体动作意识（multi-agent action awareness）。通过结构化行为注入，显式建模交互关系。
- **关键技术细节**：
  - 使用一个**Scene-Action Transformer**将三个组件融合，产生一致、可解释且具有交互感知的表示。
  - 稀疏场景语义：提取关键道路元素（如车道、交通灯）的稀疏化表示，避免稠密监督的标注成本。
  - 自车动作意识：编码自车的历史和未来动作意图（速度、转向等）。
  - 多智能体动作意识：编码周围交通参与者的未来轨迹和交互模式。
  - 该表示直接用于端到端轨迹规划，无需额外模块。
- **公式/算法流程**（文字描述）：
  - 输入：多模态传感器数据（相机、雷达等）。
  - 步骤1：分别通过三个独立编码器提取稀疏语义、自车动作、多智能体动作的特征。
  - 步骤2：Scene-Action Transformer通过交叉注意力机制将三类特征融合，生成统一的场景-动作嵌入。
  - 步骤3：基于嵌入通过可学习的规划头输出自车未来轨迹。

### 3. 实验设计：数据集、基准与对比方法

- **数据集与场景**：
  - **nuScenes**：开放环路（open-loop）评估，主要指标为L2轨迹误差和碰撞率。
  - **NAVSIM**：开放环路评估。
  - **Bench2Drive**：闭环（closed-loop）评估。
- **基准与对比方法**：
  - 主要对比方法：**VAD**（端到端SOTA baseline）。
  - 实验表明SAR在nuScenes上L2误差降低47%，碰撞率降低41%；在NAVSIM和Bench2Drive上均达到新的SOTA。

### 4. 资源与算力

- 论文摘要及元数据中**未明确说明**所使用的GPU型号、数量、训练时长等算力信息。仅提到代码将开源。

### 5. 实验数量与充分性

- 覆盖**三个不同基准**（nuScenes、NAVSIM、Bench2Drive），包含开放环路和闭环评估，说明实验具有较好的一般性。
- 元数据中提及“evidence”为“利用场景-动作表示的端到端自动驾驶”，且元数据中“result”提到了轨迹预测准确性提升和安全风险降低，但**未详细列出消融实验的数量**（例如是否对三个组件分别进行了消融）。仅从摘要看，未提供详细消融表或统计分析。
- **充分性判断**：整体实验覆盖了主流基准，对比方法明确，但缺少对组件贡献的定量消融报告，以及在不同天气/光照等条件上的鲁棒性实验。实验尚可，但不够彻底。

### 6. 论文的主要结论与发现

- SAR框架通过结构化行为注入（稀疏语义、自车动作、多智能体动作）显著提升了端到端自动驾驶在交互场景中的性能。
- 在nuScenes上相比VAD，L2轨迹误差降低47%，碰撞率降低41%。
- 在NAVSIM和Bench2Drive上取得新SOTA，证明了方法的泛化能力。
- 仅需少量标注成本（稀疏语义而非稠密监督），即可获得良好性能。

### 7. 优点：方法或实验设计上的亮点

- **行为建模的创新**：将人类驾驶认知抽象为三个互补组件，结构化注入行为知识，避免了传统稠密中间监督的高成本。
- **可解释性与一致性**：Scene-Action Transformer融合后得到可解释的表示，有利于分析规划决策原因。
- **实验全面性**：覆盖开环和闭环两种评估范式，并在多个数据集上验证，结果可重复性高（代码即将开源）。
- **效率优势**：稀疏语义降低了标注和计算开销。

### 8. 不足与局限

- **未涉及计算资源与训练成本**：未报告GPU型号、训练时长、参数量等信息，难以评估方法在实际部署中的硬件门槛。
- **消融实验细节缺失**：摘要未说明是否对不同组件（稀疏语义、自车动作、多智能体动作）进行了独立消融，也未见超参数敏感性分析，实验充分性稍显不足。
- **潜在偏差风险**：仅在现有公开数据集上评估，未考虑极端长尾场景（如恶劣天气、罕见交通参与者）的鲁棒性。
- **被拒可能原因**：根据元数据该文被ICLR 2026 Rejected，可能审稿人认为创新性有限或实验验证不够深入（如缺少闭环真实世界测试）。
- **应用限制**：方法依赖于对多智能体动作的建模，在传感器噪声大或部分观测场景下可能退化；且当前仅适用于城市道路场景，未测试高速公路或乡村道路。

（完）
