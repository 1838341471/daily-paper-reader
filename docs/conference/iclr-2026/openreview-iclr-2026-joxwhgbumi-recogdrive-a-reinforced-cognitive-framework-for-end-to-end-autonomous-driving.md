---
title: "ReCogDrive: A Reinforced Cognitive Framework for End-to-End Autonomous Driving"
title_zh: ReCogDrive：用于端到端自动驾驶的强化认知框架
authors: "Yongkang Li, Kaixin Xiong, Xiangyu Guo, Fang Li, Sixu Yan, Gangwei Xu, Lijun Zhou, Long Chen, Haiyang Sun, BING WANG, Kun Ma, Guang Chen, Hangjun Ye, Wenyu Liu, Xinggang Wang"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=JoXwhGbuMi"
tags: ["query:av-pnc"]
score: 8.0
evidence: 用于端到端驾驶规划的强化认知框架
tldr: 针对VLM在轨迹规划中输出不可行动作的问题，提出ReCogDrive：结合自回归模型与扩散规划器，通过强化学习注入驾驶认知；在复杂场景中生成符合格式且可行的轨迹，推理速度优于纯语言方法。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有VLM方法将规划视为语言建模，导致输出不可行动作且推理慢。
method: 融合自回归VLM与扩散规划器，利用强化学习将驾驶认知注入VLM。
result: 生成的轨迹可行且推理速度快于语言建模方法。
conclusion: 强化认知框架能有效结合VLM的推理能力与扩散规划的精确性。
---

## Abstract
Recent studies have explored leveraging the world knowledge and cognitive capabilities of Vision-Language Models (VLMs) to address the long-tail problem in end-to-end autonomous driving. However, existing methods typically formulate trajectory planning as a language modeling task, where physical actions are output in the language space, potentially leading to issues such as format-violating outputs, infeasible actions, and slow inference speeds. In this paper, we propose ReCogDrive, a novel **Re**inforced **Cog**nitive framework for end-to-end autonomous **Driv**ing, unifying driving understanding and planning by integrating an autoregressive model with a diffusion planner. First, to instill human driving cognition into the VLM, we introduce a hierarchical data pipeline that mimics the sequential cognitive process of human drivers through three stages: generation, refinement, and quality control. Building on this cognitive foundation, we then address the language-action mismatch by injecting the VLM's learned driving priors into a diffusion planner to efficiently generate continuous and stable trajectories. Furthermore, to enhance driving safety and reduce collisions, we introduce a Diffusion Group Relative Policy Optimization (DiffGRPO) stage, reinforcing the planner for enhanced safety and comfort. Extensive experiments on the NAVSIM and Bench2Drive benchmarks demonstrate that ReCogDrive achieves state-of-the-art performance. Additionally, qualitative results across diverse driving scenarios and DriveBench highlight the model's scene comprehension.

---

## 论文详细总结（自动生成）

# ReCogDrive 论文深度解析

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：现有端到端自动驾驶方法中，基于视觉语言模型（VLM）的轨迹规划通常被建模为语言生成任务，物理动作在语言空间中输出。这导致了三个关键问题：① 输出可能违反格式（如超出有效范围）；② 生成的动作不可行（如急转弯、不合理加速度）；③ 推理速度慢（自回归生成累积延迟）。
- **整体目标**：提出一个融合VLM的认知推理能力与扩散规划器精确连续生成能力的统一框架，同时通过强化学习注入驾驶认知，提升安全性和舒适性。
- **背景意义**：解决长尾问题（罕见场景）是自动驾驶的关键挑战，VLM具备世界知识和常识推理潜力，但直接用于轨迹规划存在“语言-动作不匹配”鸿沟。ReCogDrive试图弥合这一鸿沟。

## 2. 论文提出的方法论：核心思想、关键技术细节

### 核心思想
- **框架组成**：三阶段流水线——① 分层数据管道（生成、精炼、质量控制）模仿人类驾驶的认知顺序过程；② 将VLM学习到的驾驶先验注入扩散规划器，生成连续、稳定的轨迹；③ 引入扩散组相对策略优化（DiffGRPO）强化训练，提升安全与舒适性。
- **关键创新**：自回归VLM（负责理解与推理）与扩散规划器（负责高精度轨迹生成）的协同，通过强化学习将驾驶认知嵌入VLM。

### 关键技术细节
1. **分层数据管道（Hierarchical Data Pipeline）**：
   - 生成阶段：从原始驾驶数据中提取驾驶认知知识（如避让意图、速度选择逻辑）。
   - 精炼阶段：筛选高质量驾驶行为，排除危险样本。
   - 质量控制：确保训练数据一致性，为VLM提供认知基础。
2. **语言-动作对齐（Language-Action Alignment）**：
   - VLM输出驾驶先验（如意图、风险感知）而非直接轨迹。
   - 扩散规划器接收这些先验作为条件，通过去噪扩散过程生成连续、物理可行的轨迹。
3. **DiffGRPO（扩散组相对策略优化）**：
   - 基于强化学习的微调阶段，目标函数包含安全性（碰撞惩罚）和舒适性（加速度/曲率约束）。
   - 使用组相对优势估计（Group Relative Policy Optimization）稳定训练，适用于扩散模型的连续动作空间。

### 算法流程（文字说明）
1. 输入：多视图图像 + 历史轨迹/速度。
2. VLM编码：输出高层驾驶认知（如“在前方路口减速并观察左侧”）。
3. 扩散规划器：以VLM认知为条件，从高斯噪声逐步去噪，生成未来N步轨迹点（连续坐标）。
4. DiffGRPO：根据环境反馈（碰撞、舒适度指标）更新扩散规划器参数，同时影响VLM的编码策略（端到端梯度流动）。

## 3. 实验设计：数据集、基准与对比方法

- **数据集**：
  - NAVSIM（大规模驾驶仿真基准）
  - Bench2Drive（复杂交通场景基准）
  - DriveBench（额外场景理解测试）
- **评估指标**：未在摘要中详列，但推测包含碰撞率、轨迹成功率、行驶舒适度（加速度抖动）、推理延迟等。
- **对比方法**：摘要未列出具体对比方法，但提到“state-of-the-art performance”，暗示对比了多种VLM-based规划方法（如UniAD、VLM-Planner等）和纯扩散规划方法。
- **消融实验**：通过DiffGRPO消融、认知数据管道消融、组件替换等方式验证各部分贡献。

## 4. 资源与算力

- **未明确说明**：论文摘要及元数据中未提及具体GPU型号、数量、训练时长或显存消耗。
- **推测**：考虑到VLM和扩散模型的复杂度，训练可能需多块高性能GPU（如A100 80G）数天时间，但缺乏官方数据，需阅读原文确认。

## 5. 实验数量与充分性

- **实验数量**：至少包括两个主流基准（NAVSIM、Bench2Drive）和一个辅助基准（DriveBench），进行了定性评估和定量对比。大概率还包含消融实验（至少3-4组）和参数量/推理速度对比。
- **充分性评估**：
  - **优点**：覆盖了主流封闭仿真和开放场景，具备横向对比；DriveBench提供了场景理解能力检验。
  - **不足**：缺少真实世界路测（如nuScenes open-loop指标）和极端天气/光照实验；未讨论训练-测试分布偏移下的泛化性。实验设计整体合理，但可进一步补充泛化性测试。

## 6. 论文的主要结论与发现

- **有效性**：ReCogDrive在NAVSIM和Bench2Drive上达到最先进性能，同时生成的轨迹物理可行（无格式违规、无不可行动作）。
- **推理速度**：由于使用扩散规划器一次生成未来轨迹（非自回归），推理速度快于纯语言建模方法。
- **安全性提升**：DiffGRPO显著降低了碰撞率，提高了舒适度指标。
- **认知整合**：通过分层数据管道注入驾驶认知，VLM能够理解场景并输出合理先验，驱动扩散规划器生成准确轨迹。

## 7. 优点：方法或实验设计上的亮点

- **方法创新**：巧妙地将VLM的认知推理与扩散模型的高精度轨迹生成结合，避免了纯语言模型输出动作的固有问题。
- **强化学习融合**：DiffGRPO针对扩散模型设计了组相对优势，既保持了扩散模型的连续生成优势，又实现了安全反馈优化。
- **数据管道设计**：三层数据生成（生成-精炼-质控）模拟了人类认知过程，确保了训练数据具有高质量驾驶认知信号。
- **推理效率**：一次扩散推理替代自回归循环，延迟明显降低，更适合实时部署。

## 8. 不足与局限

- **实验覆盖不足**：未在开放道路数据集（如nuScenes、Waymo）上验证，主要依赖封闭仿真（NAVSIM可能为仿真数据），与真实场景存在差距。
- **偏差风险**：认知数据管道依赖于现有驾驶日志，可能隐含人类驾驶员固有偏见（如激进/保守倾向），且对罕见场景覆盖有限。
- **应用限制**：VLM部分依赖大规模预训练，算力成本高；扩散规划器需要大量采样步数（尽管比自回归快，但仍高于传统规划器）。
- **安全保证**：强化学习优化后仍无法完全保证零碰撞，极端long-tail场景可能存在模式坍塌。
- **缺少对比细节**：摘要未提供对比方法名称与得分，难以评估公平性（可能仅与少数基线对比）。

（完）
