---
title: "Don't Shake the Wheel: Momentum-Aware Planning in End-to-End Autonomous Driving"
title_zh: 不要晃动方向盘：端到端自动驾驶中的动量感知规划
authors: "Song, Ziying, Jia, Caiyan, Liu, Lin, Pan, Hongyu, Zhang, Yongchang, Wang, Junming, Zhang, Xingyu, Xu, Shaoqing, Yang, Lei, Luo, Yadan"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Song_Dont_Shake_the_Wheel_Momentum-Aware_Planning_in_End-to-End_Autonomous_Driving_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 9.0
evidence: 端到端自动驾驶中的动量感知规划，引入轨迹动量和感知动量
tldr: 端到端自动驾驶常因单帧感知导致轨迹不稳定和遮挡脆弱性。本文提出MomAD框架，引入轨迹动量和感知动量以稳定预测。包含拓扑轨迹匹配（TTM）利用Hausdorff距离选择与历史路径一致的规划查询，以及动量规划交互器（MPI）利用历史查询扩展感知。实验表明MomAD在稳定性和安全性上显著优于基线方法。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 871, \"height\": 1100, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1795, \"height\": 453, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 870, \"height\": 344, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1797, \"height\": 794, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1803, \"height\": 441, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 862, \"height\": 271, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 863, \"height\": 352, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1805, \"height\": 215, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 863, \"height\": 357, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1798, \"height\": 215, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 864, \"height\": 328, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-song-dont-shake-the-wheel-momentum-aware-planning-in-end-to-end-autonomous-driving-cvpr-2025-paper/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 862, \"height\": 222, \"label\": \"Table\"}]"
motivation: 单帧感知导致的轨迹抖动和遮挡问题影响端到端驾驶稳定性。
method: 设计拓扑轨迹匹配和动量规划交互器，利用历史轨迹和感知信息平滑规划。
result: 在CARLA和nuScenes上，MomAD减少了轨迹抖动并提升了碰撞规避能力。
conclusion: 动量感知机制有效提升了端到端自动驾驶规划的鲁棒性。
---

## Abstract
End-to-end autonomous driving frameworks enable seamless integration of perception and planning but often rely on one-shot trajectory prediction, which may lead to unstable control and vulnerability to occlusions in single-frame perception. To address this, we propose the Momentum-Aware Driving (MomAD) framework, which introduces trajectory momentum and perception momentum to stabilize and refine trajectory predictions. MomAD comprises two core components: (1) Topological Trajectory Matching (TTM) employs Hausdorff Distance to select the optimal planning query that aligns with prior paths to ensure coherence; (2) Momentum Planning Interactor (MPI) cross-attends the selected planning query with historical queries to expand static and dynamic perception files. This enriched query, in turn, helps regenerate long-horizon trajectory and reduce collision risks. To mitigate noise arising from dynamic environments and detection errors, we introduce robust instance denoising during training, enabling the planning model to focus on critical signals and improve its robustness. We also propose a novel Trajectory Prediction Consistency (TPC) metric to quantitatively assess planning stability. Experiments on the nuScenes dataset demonstrate that MomAD achieves superior long-term consistency (>3s) compared to SOTA methods. Moreover, evaluations on the curated Turning-nuScenes shows that MomAD reduces the collision rate by 26% and improves TPC by 0.97m (33.45%) over a 6s prediction horizon, while closed-loop on Bench2Drive demonstrates an up to 16.3% improvement in success rate.

---

## 论文详细总结（自动生成）

# 论文总结：Don't Shake the Wheel: Momentum-Aware Planning in End-to-End Autonomous Driving

## 1. 核心问题与整体含义（研究动机和背景）

- **研究动机**：端到端自动驾驶框架通常依赖单帧（one-shot）轨迹预测，这会导致：（1）控制不稳定（轨迹抖动、振荡）；（2）对单帧感知中的遮挡和关键视觉线索丢失敏感，从而引发安全隐患。
- **核心问题**：如何利用历史轨迹和感知信息（即“动量”）来稳定、平滑并精细化轨迹预测，克服单帧预测的时序不一致性。
- **整体含义**：提出**动量感知驾驶（MomAD）** 框架，将“轨迹动量”和“感知动量”引入规划过程，使当前预测继承历史路径的连贯性，并扩展感知视野，提升长期规划和碰撞规避能力。

## 2. 方法论：核心思想、关键技术细节

### 核心思想
- **轨迹动量**：通过匹配当前候选多模态轨迹与历史预测轨迹，减少ego车辆路径的突变，保证控制一致性。
- **感知动量**：通过聚合历史时刻的规划查询，融合长期地图元素和周围agent的意图，弥补单帧感知信息的不足。

### 关键技术模块
1. **拓扑轨迹匹配（TTM）**：
   - 输入：当前时刻的多模态候选轨迹集合 \(T_t = \{T_t^k\}_{k=1}^K\)（K=6×3，对应6条轨迹×3种驾驶指令）和历史轨迹 \(T_{t-1}\)。
   - 坐标变换：将当前轨迹从t时刻坐标系变换到t-1时刻坐标系（公式：\(T_t^k \leftarrow R_{t-1}^{-1}(T_t^k - \Gamma_{t-1})\)）。
   - 距离度量：采用**Hausdorff距离**（双向最大偏差）评估候选轨迹与历史轨迹的整体对齐程度（公式2），克服欧氏距离对局部变化的敏感性。
   - 选择策略：选择Hausdorff距离最小的候选轨迹索引 \(k^*\)（公式3），保证当前预测与历史路径连贯。

2. **动量规划交互器（MPI）**：
   - 目标：增强选中的规划查询 \(Q_t^{p^*}\) 的上下文感知能力。
   - 长视野查询混合器：首先对历史规划查询 \(Q_{t-1}^p\) 和对应的得分 \(S_{t-1}^p\) 进行元素级交互，并通过LSTM处理（公式4），得到反映时间演化的代理查询 \(Q_{t-1}^{p'}\)。
   - 交叉注意力：以当前选中的查询 \(Q_t^{p^*}\) 为query，以 \(Q_{t-1}^{p'}\) 为key和value，得到富化后的查询 \(\tilde{Q}_t^{p^*}\)（公式5）。
   - 轨迹重新生成：将富化查询与实例特征、ego锚点位置输入PlanHead，生成改进后的多模态轨迹和得分。

3. **鲁棒实例去噪（训练时）**：
   - 问题：稀疏感知模块提供的实例特征可能因检测不稳定、地图动态变化而含有噪声。
   - 方法：在训练中，对实例特征施加可控的高斯噪声，并通过轻量级编码器-解码器Transformer模块学习去噪，使模型学会区分关键与无关特征，提高对感知噪声的鲁棒性。
   - 推理时不加噪声，去噪能力自然生效。

4. **新评估指标：轨迹预测一致性（TPC）**
   - 计算当前预测轨迹与上一时刻预测轨迹之间的差异（经坐标变换后），并只保留时间重叠部分，用mask过滤有效轨迹（公式6）。TPC越低表示预测越一致。

## 3. 实验设计

### 数据集与场景
- **nuScenes**：1000个场景（训练700，验证150），每场景20秒，关键帧2Hz，6个环视摄像头。用于开环评估感知、地图、规划。
- **Turning-nuScenes**：从nuScenes验证集中筛选转弯场景（阈值：3s与0.5s的未来轨迹夹角≥25°），共17个场景、680个样本，用于挑战时序不一致性。
- **Bench2Drive**：基于CARLA Leaderboard 2.0的闭环评估协议，包含44个交互场景、220条路线（多种天气和地点）。训练使用base set（1000个clip），评估使用官方220条路线。

### 对比方法
- 开环对比：UniAD、VAD、SparseDrive（均为端到端方法）。
- 闭环对比：VAD（确定性及多模态变体）、SparseDrive。
- 评价指标：L2位移误差（L2）、碰撞率（Col.）、TPC（新提出）、FPS。

### 实验分组
1. **主表规划结果**（nuScenes）：含UniAD/VAD指标和VAD指标两种协议，报告1s/2s/3s平均L2、Collision Rate、TPC。
2. **Turning-nuScenes规划结果**：对比SparseDrive，报告相同指标。
3. **长轨迹预测（6s）**：在nuScenes和Turning-nuScenes上对比SparseDrive，报告4s/5s/6s L2、Col.、TPC。
4. **Bench2Drive闭环结果**：报告开放循环L2，闭环DS、SR（成功率）、Effi、Comf。
5. **感知与运动预测结果**：检测（mAP, NDS）、跟踪（AMOTA）、在线地图（mAP）、运动预测（minADE, minFDE等）。
6. **消融实验**：
   - 感知模块（ED +噪声）影响（表6）。
   - 历史帧数t的影响（表7）：t=1（无历史）、t=2（前一帧）、t=3（前两帧）。
   - MP内部子模块（Add vs 长视野查询混合器）的影响（表8）。
7. **可视化比较**：多帧轨迹对比（图4）。

## 4. 资源与算力
- **文中提及**：MomAD在RTX4090上FPS为7.8，SparseDrive为9.0。作者未明确说明训练使用的GPU型号、数量、训练时长（仅提“训练10个epoch”用于长轨迹预测实验）。因此算力细节不充分。

## 5. 实验数量与充分性
- **实验组数**：共8个表格+可视化，涵盖：主规划结果（2表）、长轨迹（1表）、闭环（1表）、感知/运动（1表）、消融（3表）。各表内还有不同时间步长、不同指标的子对比。
- **充分性**：
  - 同时覆盖开环和闭环评估，且使用专门的转弯子集（Turning-nuScenes）弥补原数据集偏向直路的局限，实验设计较全面。
  - 消融实验覆盖了感知去噪、历史帧数、MPI子模块等多个维度，归因清晰。
  - 但缺少与更多SOTA方法（如VADv2等）的直接对比，仅在开环中主要对比SparseDrive，闭环中对比了VAD和SparseDrive。此外，未在nuScenes上进行长轨迹预测的完整对比（仅有6s实验），且未在更多数据集（如Waymo）上验证泛化性。

## 6. 主要结论与发现
- MomAD在nuScenes上L2 0.60m、碰撞率0.09%、TPC 0.54m，优于UniAD、VAD、SparseDrive。
- 在Turning-nuScenes上，相比SparseDrive，碰撞率降低26%，TPC降低0.97m（33.45%）（6s预测）。
- 在Bench2Drive闭环中，成功率提升16.3%（对比VAD多模态变体），舒适性提升7.2%。
- 长轨迹预测（4-6s）在两类数据集上均显著改善L2、碰撞率和TPC，降幅达10%~33%。
- 消融表明：（1）感知去噪（噪声σ=0.1）最佳；（2）历史帧数为2（t=2）时规划提升最明显，更多帧（t=3）反而略降；（3）MPI中的长视野查询混合器优于简单的Add操作。

## 7. 优点
- **创新性**：将“动量”概念（来自物理和人类驾驶习惯）明确引入端到端规划，分别处理轨迹连续性和感知长视野，方法直观且有效。
- **针对性解决时序不一致**：通过TTM（Hausdorff距离）和MPI（cross-attention + LSTM）直接针对多模态轨迹的帧间抖动问题，而非仅优化单帧精度。
- **新指标**：提出TPC，弥补现有指标无法评估预测稳定性的空白。
- **实验严谨**：在开环+闭环、标准+挑战性子集（Turning-nuScenes）、短时+长时预测上均验证，消融覆盖关键模块。
- **公开代码**：提供GitHub仓库，促进复现。

## 8. 不足与局限
- **算力信息不完整**：未明确训练GPU型号、数量、总训练时长，影响可复现性评估。
- **实验覆盖有限**：仅在nuScenes和Bench2Drive（基于CARLA）上评估，缺乏Waymo、nuPlan等更大规模或真实世界数据集验证；仅对比了少数基线（UniAD, VAD, SparseDrive），未对比VADv2等更近期的工作。
- **历史帧数敏感性**：t=2最优，t=3反而下降，说明历史利用长度需要精细调优，且可能因长历史引入过时信息导致偏差。
- **模式塌缩风险**：作者自述“teacher-forcing导致轨迹多样性受限”，虽提出未来用扩散模型改进，但当前MI模块仍可能限制多模态表达的丰富度。
- **实时性稍弱**：FPS 7.8略低于SparseDrive（9.0），对实际部署可能存在压力（但文中未提及具体硬件平台约束）。
- **仅依赖相机**：未融合LiDAR/雷达，可能对夜间、恶劣天气感知鲁棒性不足（但该方法本身不限制输入模态）。

（完）
