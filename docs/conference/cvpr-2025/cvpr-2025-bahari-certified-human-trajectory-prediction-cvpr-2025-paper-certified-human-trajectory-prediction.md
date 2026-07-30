---
title: Certified Human Trajectory Prediction
title_zh: 认证人类轨迹预测
authors: "Bahari, Mohammadhossein, Saadatnejad, Saeed, Farsangi, Amirhossein Askari, Moosavi-Dezfooli, Seyed-Mohsen, Alahi, Alexandre"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Bahari_Certified_Human_Trajectory_Prediction_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 8.0
evidence: 自动驾驶中行人轨迹预测的鲁棒性认证
tldr: 当前轨迹预测模型对噪声输入缺乏鲁棒性。本文提出针对轨迹预测的认证方法，结合扩散模型去噪器，在保证鲁棒性的同时缓解性能下降。实验证明该方法能有效抵御对抗攻击，提高自动驾驶安全性。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bahari-certified-human-trajectory-prediction-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 862, \"height\": 513, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bahari-certified-human-trajectory-prediction-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1735, \"height\": 375, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bahari-certified-human-trajectory-prediction-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1751, \"height\": 738, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bahari-certified-human-trajectory-prediction-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1701, \"height\": 407, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bahari-certified-human-trajectory-prediction-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1177, \"height\": 509, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bahari-certified-human-trajectory-prediction-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 812, \"height\": 301, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bahari-certified-human-trajectory-prediction-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 628, \"height\": 183, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bahari-certified-human-trajectory-prediction-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 684, \"height\": 184, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bahari-certified-human-trajectory-prediction-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 446, \"height\": 185, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bahari-certified-human-trajectory-prediction-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 768, \"height\": 222, \"label\": \"Table\"}]"
motivation: 现有方法缺乏对噪声输入的鲁棒性保证。
method: 设计轨迹预测专用认证流程，集成扩散模型去噪器以提升认证下的性能。
result: 在多个数据集上验证了鲁棒性保证，且性能损失较小。
conclusion: 认证方法为安全关键应用提供了可靠的轨迹预测。
---

## Abstract
Predicting human trajectories is essential for the safe operation of autonomous vehicles, yet current data-driven models often lack robustness in case of noisy inputs such as adversarial examples or imperfect observations. Although some trajectory prediction methods have been developed to provide empirical robustness, these methods are heuristic and do not offer guaranteed robustness. In this work, we propose a certification approach tailored for trajectory prediction that provides guaranteed robustness. To this end, we address the unique challenges associated with trajectory prediction, such as unbounded outputs and multi-modality. To mitigate the inherent performance drop through certification, we propose a diffusion-based trajectory denoiser and integrate it into our method. Moreover, we introduce new certified performance metrics to reliably measure the trajectory prediction performance. Through comprehensive experiments, we demonstrate the accuracy and robustness of the certified predictors and highlight their advantages over the non-certified ones. The code is available online: https://s-attack.github.io/

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义

本文针对自动驾驶等安全关键场景中人类轨迹预测模型在面临噪声输入（如对抗攻击、感知系统误差）时缺乏鲁棒性保证的问题。现有方法多为启发式防御，无法提供确定的输出边界。论文首次将随机平滑认证框架引入轨迹预测任务，旨在为预测结果提供可证明的鲁棒性保证，确保在输入扰动有界时，输出始终落在认证区间内，从而提升系统的可靠性。

### 2. 论文提出的方法论

- **核心思想**：基于随机平滑（Randomized Smoothing）技术，通过对原始预测模型进行平滑变换，得到具有认证鲁棒性的新模型。具体地，对输入添加高斯噪声获得多个样本，经（可选）去噪器预处理后输入原预测模型，再对多个输出进行聚合（均值或中位数），得到最终预测并计算认证边界。
- **关键技术细节**：
  - **自适应裁剪**：针对轨迹预测输出无界的特点，通过训练数据确定每个坐标的最大/最小值，将预测结果裁剪到该范围内，使均值平滑公式可应用。
  - **中位数平滑**：更适用于回归任务，无需预设输出范围，且对异常值更鲁棒，实验证明优于均值平滑。
  - **扩散去噪器**：提出无条件的扩散模型作为输入预处理模块，在平滑前抑制噪声，从而收紧认证边界，缓解随机平滑带来的性能下降。
  - **多模态处理**：将多模态预测视为多输出映射，对所有模态进行认证，并根据最小认证FDE选择最佳模式。
- **算法流程**（文字说明）：  
  ① 给定原始输入X，生成n个蒙特卡洛样本 X_i = X + ϵ_i，其中 ϵ_i ~ N(0, σ²I)。  
  ② 将X_i通过扩散去噪器h得到去噪后的输入。  
  ③ 将去噪后的输入送入轨迹预测模型g，得到输出Y_i = g(h(X_i))。  
  ④ 对Y_i应用聚合函数A（中位数或均值）得到最终预测Ŷ，并利用随机平滑理论（公式(1)或(2)）计算每个预测坐标的上下界（LB, UB）。

### 3. 实验设计

- **数据集与场景**：使用ETH、UCY、WildTrack三个公开行人轨迹数据集，统一采用Trajnet++基准进行预处理和划分。输入长度9帧（观察），输出长度12帧（预测），每帧对应0.4秒。
- **对比方法**：
  - 轨迹预测模型：Social-Force（规则法）、D-Pool、AutoBot、EqMotion（均为基于学习的方法）。
  - 去噪方法对比：无去噪器、多项式拟合、滑动平均、维纳滤波、扩散去噪器。
  - 聚合函数：均值平滑 vs. 中位数平滑。
- **主要指标**：
  - 传统指标：ADE、FDE。
  - 新认证指标：平均/最终半直径（ABD/FBD）、认证ADE/FDE、认证碰撞率。
- **实验类型**：
  - 不同σ（0.08~0.4）下的FDE-FBD trade-off曲线。
  - 各模型的认证与非认证指标对比（表1）。
  - 去噪器效果对比（表2、表3）。
  - 单模态 vs. 多模态认证（表4）。
  - 单智能体 vs. 多智能体认证（表5）。
  - 下游任务（机器人导航）验证（表6）。
  - 对抗攻击场景定性分析（图4）。

### 4. 资源与算力

论文未明确说明训练所需的GPU数量及训练时长。仅在局限性部分提到推理时间：使用单张NVIDIA GeForce RTX 3090，预测一条4.8秒轨迹时，原始EqMotion需0.07秒，平滑版（n=100）需0.1秒，约增加42%的计算时间。

### 5. 实验数量与充分性

论文进行了多组实验，覆盖：
- 四种不同复杂度预测模型。
- 两种聚合函数（均值、中位数）。
- 多个σ参数（5个等间距值）。
- 五种去噪方法对比。
- 单/多模态、单/多智能体设置。
- 在下游机器人导航任务上验证。
- 对抗攻击和真实感知噪声案例。

整体实验设计较为全面，消融实验验证了去噪器、聚合函数选择、多模态等模块的有效性。但缺乏在大规模数据集（如nuScenes完整集）上的定量认证指标对比（仅有定性案例），且未对更多攻击类型（如白盒C&W）进行定量实验。此外，碰撞率的新指标定义与真实风险的关系未深入讨论。

### 6. 论文的主要结论与发现

1. **认证框架可行**：随机平滑可成功应用于轨迹预测，中位数平滑比均值平滑更优，能提供更紧的边界。
2. **精度与鲁棒性权衡**：增大σ会收紧边界但降低精度，用户可根据需求调整。
3. **扩散去噪器有效**：显著降低噪声对预测的影响，在相同FDE下使认证边界缩小约30%~40%。
4. **高精度≠高鲁棒性**：实验中EqMotion FDE最低，但认证FDE反而不如D-Pool，说明应考虑鲁棒性指标。
5. **新认证指标的必要性**：传统ADE/FDE无法反映噪声影响，认证指标能更可靠地评估模型在真实场景中的表现。
6. **实际优势**：平滑模型能抵抗对抗攻击和感知噪声，在机器人导航下游任务中降低碰撞率并提高累计奖励。

### 7. 优点

- **首次将认证引入轨迹预测**，填补了该领域可证明鲁棒性的空白。
- **针对轨迹预测特点的适配**：提出自适应裁剪、中位数平滑、多模态认证处理。
- **扩散去噪器**：作为即插即用模块可集成到现有预测器中，有效缓解平滑带来的性能损失。
- **新认证指标**：如认证FDE、认证碰撞率，为安全评估提供了更合理的手段。
- **实验充分**：涵盖多种模型、聚合函数、去噪方法、多模态/多智能体及下游任务，结论有说服力。

### 8. 不足与局限

- **计算开销增加**：n=100时推理时间增加42%，在高实时性要求场景下可能成为瓶颈。
- **边界依赖于训练数据分布**：自适应裁剪的边界基于训练集推导，若测试分布出现极端值，裁剪可能导致预测失真。
- **多模态认证选择策略简单**：基于最低认证FDE选择模式，未考虑模式概率或场景一致性。
- **实验覆盖有限**：仅在行人轨迹数据集上验证，未在车辆轨迹或更复杂交通场景（如Waymo）测试。
- **对抗攻击定量分析缺失**：仅展示了定性案例，缺乏如攻击成功率等定量指标。
- **碰撞率指标定义**：认证碰撞率基于边界与邻域真实轨迹的相对位置，但未考虑预测的不确定性（如模态权重）。

（完）
