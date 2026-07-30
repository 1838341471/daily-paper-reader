---
title: "Bridging Past and Future: End-to-End Autonomous Driving with Historical Prediction and Planning"
title_zh: 连接过去与未来：基于历史预测与规划的端到端自动驾驶
authors: "Zhang, Bozhou, Song, Nan, Jin, Xin, Zhang, Li"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhang_Bridging_Past_and_Future_End-to-End_Autonomous_Driving_with_Historical_Prediction_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 9.0
evidence: 端到端历史预测与规划统一
tldr: "端到端自动驾驶方法常忽略多步历史预测与规划的对齐。本文提出BridgeAD，将运动查询和规划查询重新设计为多步查询，实现历史预测与规划的深度融合。该方法遵循'未来是过去的延续'理念，在规划中充分利用历史信息。实验表明在多个基准上提升了规划和预测性能，为端到端驾驶提供了一种统一框架。"
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 855, \"height\": 711, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1789, \"height\": 981, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 855, \"height\": 707, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1680, \"height\": 1295, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 874, \"height\": 452, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 876, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1548, \"height\": 540, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 674, \"height\": 304, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 863, \"height\": 272, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 873, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 874, \"height\": 236, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 871, \"height\": 326, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhang-bridging-past-and-future-end-to-end-autonomous-driving-with-historical-prediction-cvpr-2025-paper/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 1762, \"height\": 280, \"label\": \"Table\"}]"
motivation: 现有端到端方法未能有效对齐多步历史预测与规划。
method: 提出多步查询机制，统一历史预测和规划的解码过程。
result: 在标准测试集上提升规划和预测精度，验证了历史信息的重要性。
conclusion: BridgeAD实现了预测与规划的协同优化，为端到端自动驾驶提供了新范式。
---

## Abstract
End-to-end autonomous driving unifies tasks in a differentiable framework, enabling planning-oriented optimization and attracting growing attention.Current methods aggregate historical information either through dense historical bird's-eye-view (BEV) features or by querying a sparse memory bank, following paradigms inherited from detection.However, we argue that these paradigms either omit historical information in motion planning or fail to align with its multi-step nature, which requires predicting or planning multiple future time steps. In line with the philosophy of "future is a continuation of past", we propose **BridgeAD**, which reformulates motion and planning queries as multi-step queries to differentiate the queries for each future time step. This design enables the effective use of historical prediction and planning by applying them to the appropriate parts of the end-to-end system based on the time steps, which improves both perception and motion planning. Specifically, historical queries for the current frame are combined with perception, while queries for future frames are integrated with motion planning. In this way, we bridge the gap between past and future by aggregating historical insights at every time step, enhancing the overall coherence and accuracy of the end-to-end autonomous driving pipeline. Extensive experiments on the nuScenes dataset in both open-loop and closed-loop settings demonstrate that BridgeAD achieves state-of-the-art performance. We will make our code and models publicly available.

---

## 论文详细总结（自动生成）

# 论文详细总结：BridgeAD

## 1. 论文的核心问题与整体含义（研究动机和背景）

现有的端到端自动驾驶方法在利用历史信息时存在两个主要缺陷：
- **密集方法**（如聚合历史 BEV 特征）仅在感知模块使用历史信息，完全忽略了运动规划中的历史线索；
- **稀疏方法**（如查询记忆库）虽然考虑了历史规划查询，但每个查询对应一个轨迹实例，未能对齐运动规划的多步本质（需要预测或规划多个未来时间步）。

论文提出“未来是过去的延续”这一核心思想，旨在**弥合过去与未来之间的鸿沟**，将历史预测和规划信息按时间步精确地注入到感知和运动规划模块中，从而提升整个端到端管路的连贯性和准确性。

## 2. 论文提出的方法论

### 核心思想
将运动查询和规划查询重新设计为**多步查询**（multi‑step queries），即分别增加时间步维度：  
- 运动查询：`Q_mot ∈ R^(Na × Mmot × Tmot × C)`  
- 规划查询：`Q_plan ∈ R^(Mplan × Tplan × C)`  
从而在每个时间步上都能与历史信息进行步级交互。

### 关键技术细节
1. **历史查询缓存队列**（FIFO）：缓存过去 K=3 帧的运动和规划查询。
2. **History‑Enhanced Perception**：  
   - 从缓存中提取当前帧时间步的历史运动查询 `Q_m2d`，与目标查询 `Q_obj` 做交叉注意力（Historical Mot2Det Fusion）。  
   - 之后进行标准的检测、跟踪、在线构图。
3. **History‑Enhanced Motion Prediction**：  
   - 从缓存中提取未来 `Tm2m=6` 步的历史运动查询 `Q_m2m`，与当前多步运动查询 `Q_mot` 做交叉注意力、步级自注意力、模式级自注意力。
4. **History‑Enhanced Planning**：  
   - 类似地，从缓存中提取未来 `Tp2p=3` 步的历史规划查询 `Q_p2p`，与当前多步规划查询 `Q_plan` 做三注意力。
5. **Step‑Level Mot2Plan Interaction**：  
   - 选择运动查询中最高概率的模式，与对应时间步的规划查询做交叉注意力，确保预测与规划的一致性。
6. **损失函数**：包含检测、地图、运动预测、规划四个任务的回归（L1）与分类（Focal loss），并采用 winner‑takes‑all 策略。

> 注意：交叉注意力均在对应时间步之间进行，历史信息通过自注意力传播到所有步和模式。

## 3. 实验设计

- **数据集**：nuScenes（1000 个场景，每段 20 秒，标注 2Hz）。
- **Benchmark**：
  - **开放环**：L2 位移误差（1s/2s/3s 及平均）、碰撞率；遵循 VAD 的评估协议。
  - **闭环**：NeuroNCAP 仿真器（基于 nuScenes 的光真实感安全关键场景），评估 NeuroNCAP Score 和 Collision Rate。
- **对比方法**：包括 UniAD、VAD、SparseDrive、ST‑P3、GenAD、OccWorld‑D、Drive‑WM 等，以及其他感知/预测方法（ViP3D、BEVFormer、Sparse4D 等）。大部分对比使用了官方 checkpoint。

## 4. 资源与算力

- **训练**：8 块 NVIDIA RTX A6000 GPU，使用 AdamW 优化器，Cosine Annealing 学习率调度，初始学习率 1e‑4，权重衰减 1e‑3。训练分两阶段（感知预训练 + 端到端训练），具体训练时长未明确说明。
- **推理**：BridgeAD‑S 在单张 RTX 3090 上约 5.0 FPS（157.2 ms/帧），BridgeAD‑B 约 3.9 FPS。效率优于 VAD（4.5 FPS）和 UniAD（1.8 FPS），但略低于 SparseDrive（6.1 FPS）。

## 5. 实验数量与充分性

论文进行了 **6 组主要实验** 和 **4 组消融实验**：
1. 开放环规划结果（表 1）——对比 7 种方法。
2. 闭环规划结果（表 2）——对比 3 种方法，并包含有无后处理两种情况。
3. 感知结果（表 4）——包括 3D 检测（mAP、NDS）和多目标跟踪（AMOTA、AMOTP、IDS）。
4. 运动预测结果（表 3）——对汽车和行人评估 ADE、FDE、MR、EPA。
5. 消融实验：
   - 历史 Mot2Det 融合与历史运动预测模块（表 5）。
   - 历史规划与步级运动‑规划交互模块（表 6）。
   - 步级自注意力与模式级自注意力（表 7）。
   - 历史时间步数的影响（表 8）。
6. 效率分析（FPS 对比）。
此外还提供了定性分析（图 3、4）和补充材料中的更多结果。

**充分性评价**：实验覆盖了开放环和闭环两种主流评价模式，消融设计严谨，逐步验证了每个新增模块的有效性。对比的方法均为近年 SOTA，且尽量使用官方 checkpoint，保证了公平性。但仅在 nuScenes 一个数据集上验证，缺少跨数据集（如 Waymo）或更多场景（夜间、雨雪）的泛化性实验。

## 6. 论文的主要结论与发现

1. **BridgeAD 在开放环和闭环中均达到 SOTA**：  
   - 开放环：平均 L2 误差 0.59 m（BridgeAD‑S），平均碰撞率 0.09%，优于所有对比方法。  
   - 闭环：NeuroNCAP Score 1.52（不可后处理）比 SparseDrive 高 65%，碰撞率降低 12.4%。
2. **历史预测和规划信息对连续驾驶至关重要**：尤其是在闭环安全关键场景中，能够通过感知车辆持续运动并采取合理避让动作，避免碰撞（定性示例图 4）。
3. **多步查询与步级交互的设计是实现历史信息高效利用的关键**：消融实验显示，移除历史规划或步级交互模块会显著降低规划性能。
4. **自注意力（步级和模式级）能有效传播历史信息**，提升所有时间步的准确性与一致性。

## 7. 优点

- **创新性**：首次将历史预测和规划按时间步显式注入端到端管线，解决了以往方法只把历史信息用于感知或粗略交互的问题。
- **技术设计巧妙**：多步查询自然对齐运动规划的多步本质；步级交互同时保证了预测与规划的一致性。
- **实验全面且公平**：同时包含开放环和闭环评价，闭环使用 NeuroNCAP 提供更具挑战性的安全场景；对比方法众多且使用官方 checkpoint。
- **可复现性**：代码和模型将开源，有助于后续研究。
- **效率合理**：BridgeAD‑S 的 5.0 FPS 在实用性与性能之间取得了良好平衡。

## 8. 不足与局限

- **数据集单一**：仅在 nuScenes 上验证，未在 Waymo Open Dataset、Argoverse 2 等更大规模或不同场景的数据集上测试，泛化性未知。
- **实时性需提升**：5.0 FPS 对应 200 ms 推理延迟，对某些实时系统仍显不足（尤其 BridgeAD‑B 仅 3.9 FPS）。
- **未讨论极端环境**：论文未分析雨、雪、夜间等低光照或低可见度场景下的表现。
- **闭环仿真器限制**：NeuroNCAP 基于 nuScenes 构建，虽然逼真，但与真车路测仍有差距；仿真器中的碰撞率改进能否直接迁移到现实世界存在不确定性。
- **训练资源需求较高**：需要 8 块 A6000 GPU，且两阶段训练，对一般实验室的复现成本较高。
- **缺少与更近期方法的对比**：论文中对比的方法停留在 2024 年 SparseDrive，2025 年可能有更多新方法，但论文本身发表于 CVPR 2025，更新时效尚可。

（完）
