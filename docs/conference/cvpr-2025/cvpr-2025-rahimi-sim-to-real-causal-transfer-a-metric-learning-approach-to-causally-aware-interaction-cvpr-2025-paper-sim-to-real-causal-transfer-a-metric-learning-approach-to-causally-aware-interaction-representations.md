---
title: "Sim-to-Real Causal Transfer: A Metric Learning Approach to Causally-Aware Interaction Representations"
title_zh: Sim-to-Real因果迁移：一种面向因果感知交互表示的度量学习方法
authors: "Rahimi, Ahmad, Luan, Po-Chien, Liu, Yuejiang, Rajič, Frano, Alahi, Alexandre"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Rahimi_Sim-to-Real_Causal_Transfer_A_Metric_Learning_Approach_to_Causally-Aware_Interaction_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 8.0
evidence: 用于运动预测的因果感知交互表示，直接相关交互感知轨迹预测
tldr: 多智能体交互模型的因果鲁棒性尚不明确。本文深入分析了现有表示对非因果扰动的部分鲁棒性，发现中介因果效应建模仍是挑战。提出一种度量学习方法增强表示的因果意识，在运动预测基准上提升了跨场景的泛化能力。该工作为构建更可靠的交互感知轨迹预测模型提供了理论基础。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-rahimi-sim-to-real-causal-transfer-a-metric-learning-approach-to-causally-aware-interaction-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 874, \"height\": 154, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-rahimi-sim-to-real-causal-transfer-a-metric-learning-approach-to-causally-aware-interaction-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 583, \"height\": 230, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-rahimi-sim-to-real-causal-transfer-a-metric-learning-approach-to-causally-aware-interaction-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 485, \"height\": 344, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-rahimi-sim-to-real-causal-transfer-a-metric-learning-approach-to-causally-aware-interaction-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1440, \"height\": 473, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-rahimi-sim-to-real-causal-transfer-a-metric-learning-approach-to-causally-aware-interaction-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 852, \"height\": 421, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-rahimi-sim-to-real-causal-transfer-a-metric-learning-approach-to-causally-aware-interaction-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1770, \"height\": 493, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-rahimi-sim-to-real-causal-transfer-a-metric-learning-approach-to-causally-aware-interaction-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1631, \"height\": 467, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-rahimi-sim-to-real-causal-transfer-a-metric-learning-approach-to-causally-aware-interaction-cvpr-2025-paper/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 1608, \"height\": 471, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-rahimi-sim-to-real-causal-transfer-a-metric-learning-approach-to-causally-aware-interaction-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1304, \"height\": 341, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-rahimi-sim-to-real-causal-transfer-a-metric-learning-approach-to-causally-aware-interaction-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 551, \"height\": 322, \"label\": \"Table\"}]"
motivation: 现有交互表示难以捕捉真实因果关系，影响运动预测的鲁棒性。
method: 通过度量学习优化交互表示，增强对非因果扰动的鲁棒性并建模间接因果效应。
result: 在CausalAgents基准上验证了因果感知改进，提升了运动预测的跨场景迁移性能。
conclusion: 因果感知度量学习是构建更可信交互预测模型的关键方向。
---

## Abstract
Modeling spatial-temporal interactions among neighboring agents is at the heart of multi-agent problems such as motion forecasting and crowd navigation. Despite notable progress, it remains unclear to which extent modern representations can capture the causal relationships behind agent interactions. In this work, we take an in-depth look at the causal awareness of these representations, from computational formalism to real-world practice. First, we revisit the notion of non-causal robustness studied in the recent CausalAgents benchmark. We show that existing representations are already partially resilient to perturbations of non-causal agents, and yet modeling indirect causal effects involving mediator agents remains challenging. To address this challenge, we introduce a metric learning approach that regularizes latent representations with causal annotations. Our controlled experiments show that this approach not only leads to higher degrees of causal awareness but also yields stronger out-of-distribution robustness. To further operationalize it in practice, we propose a sim-to-real causal transfer method via cross-domain multi-task learning. Experiments on trajectory prediction datasets show that our method can significantly boost generalization, even in the absence of real-world causal annotations, where we acquire higher prediction accuracy by only using 25% of real-world data. We hope our work provides a new perspective on the challenges and potential pathways toward causally-aware representations of multi-agent interactions. Our code is available in supplementary materials. Our code is available at https://github.com/vita-epfl/CausalSim2Real.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

多智能体交互建模（如运动预测、人群导航）中，现有深度表示主要依赖训练数据中的统计相关性，难以捕捉代理之间真正的因果关系，导致在分布变化（如代理密度增加、场景迁移）时性能显著下降。近期CausalAgents基准通过标注因果/非因果代理来评估鲁棒性，但本文指出该基准存在两大缺陷：标注忽略间接因果效应（通过中介代理传递的因果链），评估协议简单移除一组非因果代理可能高估模型的鲁棒性。因此，本文旨在深入分析现有表示对因果关系的感知能力，并提出提升因果鲁棒性的方法。

## 2. 论文提出的方法论

### 核心思想
- 利用反事实模拟生成带因果效应标注的合成数据，通过度量学习正则化潜在表示，使其嵌入空间中反事实场景与事实场景的距离与真实因果效应一致。

### 关键技术细节
1. **因果效应定义**：移除代理集合 \(R\) 后，ego轨迹的差异 \(E_R = \|y^{\text{orig}} - y^R\|_2\)。
2. **正则化框架**：
   - 编码器 \(f\) 提取特征 \(z\)，经非线性头 \(h\) 得到嵌入 \(p\)。
   - 距离度量：余弦相似度 \(d_i = 1 - \text{sim}(p^{\text{orig}}, p^i)\)。
3. **两种正则化变体**：
   - **因果对比正则化**（利用二值标注）：将移除因果代理的场景作为正样本（距离大），移除非因果代理的场景作为负样本（距离小），使用对比损失。
   - **因果排序正则化**（利用连续因果效应值）：对场景内所有代理按因果效应排序，配对采样，使用边际排序损失 \(\max(0, d_i - d_j + m)\)，其中 \(E_i < E_j\)。
4. **Sim-to-Real因果迁移**：联合训练真实域的主预测任务（重建损失）和合成域的因果正则化任务，即使真实域没有因果标注，也能通过合成数据传递因果知识。

### 公式/算法流程
- 对比损失：\(L_{\text{contrast}} = -\log \frac{\exp(d^+/\tau)}{\exp(d^+/\tau) + \sum_k \exp(d^k/\tau)}\)（\(d^+\)对应因果代理的移除距离）
- 排序损失：\(L_{\text{ranking}} = \max(0, d_i - d_j + m)\)
- 总损失：\(L = L_{\text{pred}}^{\text{real}} + \lambda L_{\text{causal}}^{\text{syn}}\)

## 3. 实验设计

### 数据集/场景
- **合成诊断数据集**：使用ORCA模拟器生成反事实场景，包含三类代理（非因果、直接因果、间接因果），并生成两个OOD测试集：**Density OOD**（增加代理密度）和**Context OOD**（改变场景布局为狭窄街道）。
- **真实数据集**：
  - ETH-UCY（行人轨迹预测）
  - NBA rebound数据集（篮球运动员运动预测）

### Benchmark与对比方法
- 基线模型：D-LSTM, S-LSTM, Trajectron++, STGCNN, Multi-TransMotion, AutoBots（最强基线）。
- 对比方法：
  - Vanilla sim-to-real（直接合并合成与真实数据训练）
  - 非因果数据增强（移除非因果代理并保持标签不变，来自CausalAgents）
  - 本文的对比正则化和排序正则化。

### 评价指标
- ADE（平均位移误差）、FDE（最终位移误差）
- ACE（平均因果误差）及其按类别的子指标（ACE-NC, ACE-DC, ACE-IC）

## 4. 资源与算力

论文正文未明确提及使用的GPU型号、数量或训练时长。仅在附录或实验设置中可能提及，但基于提供的文本未找到相关说明。因此，本文**未报告具体的计算资源**。

## 5. 实验数量与充分性

### 实验组数
- 5.1节：在合成诊断数据集上评估6种基线模型，计算4类因果误差（表1）。
- 5.2节：以AutoBots为骨干，对比本方法（对比/排序）与基线、数据增强，在ID和两个OOD测试集上分别评估ACE和ADE/FDE（图6、图7），并给出定性可视化。
- 5.3节：在ETH-UCY上评估不同真实数据比例（25%、50%、100%）下的因果迁移效果（图8）；在NBA数据集上评估完整数据下的ADE/FDE（表2）。
- 所有实验结果均基于**5个随机种子**重复，并报告均值。

### 客观性与公平性
- 对比方法包括最近基准（CausalAgents）和多种SOTA模型。
- 消融实验：对比正则化 vs. 排序正则化，验证细粒度标注的优势。
- 设置OOD测试集检验泛化性。
- 在真实数据集上未使用真实因果标注，仅用合成数据，体现了方法的实用价值。

**充分性判断**：实验覆盖了合成数据和两个不同真实域（行人、篮球），并考察了低数据场景，总体上较为充分。但缺少在更复杂驾驶场景（如Waymo）上的验证。

## 6. 主要结论与发现

1. **现有表示已部分鲁棒于非因果扰动**：ACE-NC远小于ACE-DC/IC，说明模型对非因果代理的移除不敏感，主要问题在于低估因果效应，尤其是间接因果代理。
2. **排序正则化优于对比正则化**：利用连续因果效应值可更精细地建模表示距离，显著降低ACE并提升OOD泛化。
3. **因果感知与OOD鲁棒性正相关**：ACE降低的模型在密度和上下文OOD上预测误差也更低。
4. **Sim-to-Real因果迁移有效**：即使合成与真实域存在较大差异，联合训练仍能提升真实数据上的预测精度，在仅用25%真实数据时即超越基线，50%数据时超越所有对比方法。

## 7. 优点

- **理论贡献**：清晰指出现有基准的标注和评估缺陷，并构建基于反事实的合成诊断数据集，提供更精确的因果标注。
- **方法简洁有效**：度量学习正则化直接匹配反事实距离与因果效应，无需复杂结构归纳偏置。
- **实用性强**：Sim-to-Real框架解决了真实因果标注稀缺的问题，在低数据场景下表现优异。
- **实验全面**：覆盖多个代表性模型、两个真实域、不同数据比例和多种分布偏移，结果稳健。

## 8. 不足与局限

- **实验覆盖有限**：仅在行人（ETH-UCY）和篮球（NBA）数据集上验证，未涉及自动驾驶常用数据集（如Waymo、nuScenes），限制了在驾驶场景下的通用性。
- **依赖模拟器质量**：ORCA模拟器行为相对简单，可能无法反映真实世界中复杂的交互模式（如意图不明、群体性行为），导致迁移效果受限于模拟-真实差距。
- **未报告计算成本**：缺乏训练时间、GPU型号等信息，影响可复现性和效率评估。
- **标注粒度受限**：间接因果效应在真实世界中难以定义和获取，本文仅依赖合成数据，可能无法覆盖所有真实因果链。
- **因果推理能力有限**：即使使用排序正则化，ACE仍有一定残留误差，说明监督信息不足以完全解决高阶因果推理（如长链因果）。

（完）
