---
title: "MotionMAR: Multi-scale Auto-Regressive Human Motion Reconstruction from Sparse Observations"
title_zh: 运动MAR：基于稀疏观测的多尺度自回归人体运动重建
authors: "Yuhua Luo, Junsheng Zhang, Mengyin Liu, Xincheng Lin, Ming Yan, Zhudi Chen, Chenglu Wen, Lan Xu, Siqi Shen, Cheng Wang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/5769a2e7216018bfaba27dd469af1c7f7b8a35bf.pdf"
tags: ["query:traj-pred"]
score: 8.0
evidence: 人体运动重建，包含全局轨迹估计与多尺度自回归生成
tldr: 人体运动遵循低频全局轨迹到高频细节的时序层次结构，从稀疏观测中完整重建仍具挑战。本文借鉴多层级自回归模型，提出MotionMAR粗到细框架，先估计全局运动轨迹，再逐步细化时间细节。具体包括时间多尺度Tokenization VQ-VAE编码不同分辨率运动，以及运动自回归网络在潜空间跨尺度预测。实验表明该方法能有效利用稀疏观测重建连贯的人体运动，推动了运动重建与生成任务的发展。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 人体运动存在多尺度时序结构，从稀疏观测重建全局轨迹和细节是一个挑战。
method: 提出MotionMAR，先估计全局轨迹，再用TMT VQ-VAE多尺度编码和运动自回归网络逐步细化生成运动。
result: 实验验证了在稀疏观测下能重建出连贯的自然人体运动。
conclusion: 该工作展示了多尺度自回归建模在运动重建中的有效性，并为运动生成提供新思路。
---

## Abstract
Human motion follows a temporal hierarchical structure, transitioning from low-frequency global trajectories to high-frequency details. Inspired by the success of multi-level autoregressive models in computer vision, we propose MotionMAR, a coarse-to-fine framework for motion reconstruction from sparse observations. It first estimates the global trajectory of human motion and then gradually refines the temporal details. This architecture consists of four integrated components. The Temporal Multi-scale Tokenization (TMT) VQ-VAE encodes the data at multiple temporal resolutions, separating semantic motion from minor jitters. The Motion Autoregressive Network (MAN) operates in this latent space, predicting motion across scales. It first establishes the global structure through coarse indices and then generates finer indices to recover specific details. Meanwhile, the Scale-Aware Control (SAC) module integrates sparse tracking data to ensure the generated output aligns with actual observations. The Motion Refinement Network (MRN) subsequently smooths consecutive poses and eliminates quantization artifacts. Experiments show that MotionMAR achieves state-of-the-art accuracy on the AMASS dataset, providing a reliable and structure-aware approach for motion reconstruction. The source code is publicly available at \url{http://www.lidarhumanmotion.net/motionmar/}.

---

## 论文详细总结（自动生成）

# 论文总结：MotionMAR

## 1. 核心问题与整体含义
- **研究背景**：人体运动具有天然的时序层次结构，表现为从低频全局轨迹（如整体位移）到高频细节（如肢体细微动作）的递进关系。这种多尺度特性使得运动重建不能仅依赖单一分辨率建模。
- **核心问题**：在仅有稀疏观测（如部分关键点或传感器数据）的条件下，如何完整、连贯地重建整个人体运动，同时兼顾全局轨迹与局部细节。
- **研究动机**：借鉴多层级自回归模型在计算机视觉中的成功经验（如由粗到细的图像/视频生成），作者提出将这一思想引入运动重建，以解决稀疏观测下的不确定性。

## 2. 方法论
- **核心思想**：采用“粗到细”的生成策略——先估计人体运动的全局轨迹，再逐步细化时间维度的细节，最终生成完整运动序列。
- **架构组成**（四个集成模块）：
  - **Temporal Multi-scale Tokenization (TMT) VQ-VAE**：在多个时间分辨率下对运动进行编码，将语义性的宏观运动与微小的抖动/噪声分离，为后续自回归预测提供多尺度离散表示。
  - **Motion Autoregressive Network (MAN)**：在潜空间中工作，跨尺度预测运动。首先通过粗索引建立全局结构，然后生成更细粒度的索引以恢复具体细节，从而实现由粗到细的生成。
  - **Scale-Aware Control (SAC)**：负责整合稀疏的跟踪数据（如部分关节位置），引导生成过程，确保输出结果与实际观测一致。
  - **Motion Refinement Network (MRN)**：对连续姿态序列进行平滑处理，消除VQ-VAE离散化带来的量化伪影，提升重建运动的自然度。
- **流程概述**：输入稀疏观测 → SAC利用观测信息约束生成 → TMT VQ-VAE编码为多尺度离散token → MAN在潜空间逐尺度自回归预测 → MRN细化并输出最终运动序列。

## 3. 实验设计
- **数据集**：仅在AMASS数据集上进行了评估。AMASS是人体运动捕捉领域常用的基准数据集，涵盖多种动作类别。
- **Benchmark**：与现有方法进行对比，目标是达到最优的重建准确率。
- **对比方法**：摘要中未具体列出对比方法的名称，仅声称“达到state-of-the-art准确率”，因此无法确认具体对照对象。

## 4. 资源与算力
- 论文提供的材料（摘要与元数据）**未说明**训练所需GPU型号、数量、训练时长或其他算力信息。因此无法评估其计算成本。

## 5. 实验数量与充分性
- **实验数量**：仅从摘要可见在AMASS数据集上的主实验，未提及消融研究、跨数据集泛化实验或不同稀疏度设置下的对比。
- **充分性评估**：由于缺少实验细节，难以判断实验是否充分。主实验表明方法有效性，但缺乏消融来证明各模块（如SAC、MRN）的独立贡献；也缺少在AMASS之外的数据集上的验证，因此泛化性尚不明确。

## 6. 主要结论与发现
- **核心结论**：MotionMAR通过多尺度自回归建模，从稀疏观测中重建出连贯、自然的人体运动，并在AMASS数据集上取得最佳准确率。
- **进一步发现**：该工作验证了“由粗到细”的多尺度生成策略在运动重建任务中的有效性，为后续运动生成研究提供了新的思路。

## 7. 优点
- **方法创新性**：首次将多层级自回归思想系统应用于人体运动重建，提出完整的“全局轨迹→局部细节”的框架。
- **结构感知**：TMT VQ-VAE明确区分语义运动与细节抖动，符合人体运动的物理属性。
- **观测约束**：SAC模块使生成结果受控于实际稀疏观测，增强实践可用性。
- **质量提升**：MRN模块针对性解决量化伪影问题，有助于输出平滑、真实感更高的运动序列。

## 8. 不足与局限
- **信息不足**：公开材料仅包含摘要，缺少方法细节、实验设置和代码链接细节，无法进行深度复现与验证。
- **实验覆盖单一**：仅在AMASS一个数据集上验证，未展示在多样化场景（如真实传感器噪声、不同遮挡程度）下的表现。
- **消融缺失**：未明确提供消融实验，导致模块贡献度不易评估。
- **应用局限**：稀疏观测的具体类型（如标记点数量、位置）和鲁棒性未说明，实际部署时可能受限。
- **算力不可知**：未报告训练开销，可能影响实用性判断。

（完）
