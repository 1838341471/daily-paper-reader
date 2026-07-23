---
title: Mitigating Error Accumulation in Continuous Navigation via Memory-Augmented Kalman Filtering
title_zh: 通过记忆增强卡尔曼滤波减轻连续导航中的误差累积
authors: "Yin Tang, Jiawei Ma, Jinrui Zhang, Alex Jinpeng Wang, Deyu Zhang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/711857fd38004509b173ac1ca4148cf32ab031d1.pdf"
tags: ["query:av-pnc"]
score: 5.0
evidence: 记忆增强卡尔曼滤波用于连续导航，可应用于自动驾驶轨迹规划
tldr: 无人机视觉语言导航中，逐步预测导致位置误差累积，即状态漂移问题。本文借鉴控制理论，将连续预测形式化为递归贝叶斯估计，提出记忆增强卡尔曼滤波方法进行误差校正。实验证明该方法能显著减轻状态漂移，提高轨迹预测准确性，对自动驾驶的连续导航具有借鉴意义。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有视觉语言导航模型采用航位推算，导致状态漂移和轨迹预测不准。
method: 将连续预测建模为递归贝叶斯状态估计，使用记忆增强卡尔曼滤波修正误差。
result: 实验表明该方法有效纠正状态漂移，提升连续导航的轨迹精度。
conclusion: 为无人机及自动驾驶的连续轨迹优化提供了误差累积缓解的新思路。
---

## Abstract
Continuous prediction in complex environments is critical for Unmanned Aerial Vehicle (UAV). However, the existing Vision-Language Navigation (VLN) models follows the dead-reckoning, which iteratively predicts the next waypoint and updates its position, thereby constructing the complete trajectory. Then, such stepwise manner will inevitably lead to accumulated errors of position over time, resulting in misalignment between internal belief and objective coordinates, which is known as ``state drift'' and ultimately compromises the subsequent trajectory prediction. Drawing inspiration from classical control theory, we propose to correct for errors by formulating the continuous prediction as a recursive Bayesian state estimation problem. In this paper, we design NeuroKalman, a novel framework that decouples navigation into two complementary processes: a Prior Prediction, based on motion dynamic,s and a Likelihood Correction, from historical observation. We first mathematically associate Kernel Density Estimation of the measurement likelihood with the attention-based retrieval mechanism, which then allows the system to rectify the latent representation using retrieved historical anchors without gradient updates. Comprehensive experiments on TravelUAV benchmark demonstrate that, with only 10\% of the full training data fine-tuning, our method clearly outperforms strong baselines and regulates drift accumulation.

---

## 论文详细总结（自动生成）

# 论文总结：通过记忆增强卡尔曼滤波减轻连续导航中的误差累积

## 1. 核心问题与整体含义
- **研究动机**：无人机（UAV）在复杂环境下的连续预测是自动驾驶和机器人领域的核心难题。现有视觉语言导航（VLN）模型普遍采用“航位推算”（dead-reckoning）策略——逐步预测下一个航点并更新位置，从而构建完整轨迹。
- **核心问题**：这种逐步预测方式会无可避免地导致位置误差随时间累积，形成所谓的**状态漂移**（state drift），即系统内部信念与客观坐标之间产生偏离，最终破坏后续轨迹预测的准确性。
- **整体含义**：该研究将连续导航问题转化为递归贝叶斯状态估计问题，借鉴经典控制理论中的卡尔曼滤波思想，提出一种**记忆增强的校正机制**，在不依赖在线梯度更新的前提下，利用历史观测信息修正误差累积，从而提升轨迹预测的鲁棒性和精度。

## 2. 方法论
- **核心思想**：将连续预测解耦为两个互补的过程——基于运动动力学的**先验预测**（Prior Prediction）与基于历史观测的**似然校正**（Likelihood Correction），形成递归贝叶斯估计框架。
- **模型框架：NeuroKalman**
    - **先验预测**：依据运动动力学模型，从当前状态推测下一时刻的状态（类似卡尔曼滤波的状态转移）。
    - **似然校正**：利用历史观测数据，通过**核密度估计**（KDE）对测量似然进行建模；将这种估计与注意力机制的检索过程建立数学关联，使系统能够通过检索到的历史锚点（anchors）直接修正隐层表示，而**无需梯度更新**。
- **关键算法流程**：
    1. 系统基于运动模型生成一个先验状态。
    2. 利用可学习的检索机制，从存储的历史经验中获取与当前情形相似的“历史锚点”。
    3. 将这些锚点作为观测信息的替代，计算测量似然，对先验状态进行校正，得到后验状态。
    4. 校正后的状态用于后续决策，整个过程不涉及反向传播，仅需要通过少量的训练数据进行微调来设置检索先验。

## 3. 实验设计
- **数据集与基准**：实验在 **TravelUAV** 基准数据集上进行，该基准专为无人机连续导航任务设计。
- **对比方法**：文中提到与多个“强基线”（strong baselines）进行对比，但摘要未列出具体模型名称。从元数据可知，该方法与已有的VLN模型进行对比，突出其对误差累积的缓解效果。
- **训练策略**：特别强调仅使用 **10% 的全量训练数据**进行微调，即可取得优于基线的效果，体现极高的数据效率。

## 4. 资源与算力
- 论文摘要及提供的元数据中**未明确说明**所使用的GPU型号、数量或训练时长。关于算力开销的具体信息需要查阅正文才能获得。

## 5. 实验数量与充分性
- 根据摘要描述，实验被认为是**综合性的**，至少包含以下维度：
    - 与多个强基准的横向对比实验。
    - 不同数据使用比例下的性能测试（如10%微调）。
    - 很可能包含消融实验，以验证先验预测与似然校正各模块的贡献，但摘要未展开细节。
- 实验设计从声明上看是**客观、公平**的，使用了公开基准TravelUAV，并采用有限微调设置突出方法的泛化潜力。由于仅根据摘要无法得知消融实验的具体数量，尚不能完全判断其全面性，但会议接收信号表明评审认可其实验充分性。

## 6. 主要结论与发现
- **误差补偿有效**：NeuroKalman 框架能够有效地纠正连续预测过程中的状态漂移问题。
- **数据效率高**：仅用10%的训练数据微调，即可显著提升轨迹预测精度，胜过常规基线。
- **方法普适性**：基于卡尔曼滤波的记忆增强方案为无人机及更广泛的自动驾驶连续导航提供了一条缓解误差累积的新思路。

## 7. 优点
- **新颖的跨领域结合**：将经典控制理论（卡尔曼滤波）与现代注意力检索机制融合，理论根基扎实。
- **计算与数据高效**：校正过程无需在线梯度计算，且微调所需数据量极少，降低了部署成本。
- **模块化解耦设计**：先验预测和似然校正分离清晰，易于扩展和调试。
- **直接修复隐状态**：通过检索历史锚点直接修正表示，避免误差在循环迭代中传播。

## 8. 不足与局限
- **评测场景单一**：仅在TravelUAV一个基准上进行了验证，其在真实环境、其他导航任务（如地面自动驾驶）或更大规模多变场景下的泛化能力尚待检验。
- **依赖历史存储**：需要维护和检索历史锚点集合，长期运行时的内存管理以及检索效率可能成为瓶颈。
- **动力学假设**：先验预测依赖于运动动力学模型，当运动模式剧烈变化或模型不精确时，先验的可靠性可能下降。
- **实验细节缺失**：摘要未提供对比方法的具体名称、消融实验的详细结果以及统计显著性分析，难以判断部分宣称的绝对优势程度。

（完）
