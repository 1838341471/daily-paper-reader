---
title: "DriveMamba: Task-Centric Scalable State Space Model for Efficient End-to-End Autonomous Driving"
title_zh: DriveMamba：面向高效端到端自动驾驶的任务中心可扩展状态空间模型
authors: "Haisheng Su, Wei Wu, Feixiang Song, Junjie Zhang, Zhenjie Yang, Junchi Yan"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=MY0NHvqzi2"
tags: ["query:av-pnc"]
score: 8.0
evidence: DriveMamba提出高效状态空间模型用于端到端驾驶规划
tldr: 现有端到端系统依赖Transformer和BEV特征，存在信息损失、累积误差和二次复杂度问题。本文提出基于Mamba的状态空间模型DriveMamba，以任务为中心进行可扩展的时空建模。实验表明DriveMamba在效率和性能上均优于Transformer基线。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: Transformer的二次复杂度和手动排序设计限制了端到端系统的可扩展性和效率。
method: 提出基于Mamba的状态空间模型，采用任务中心设计，替代Transformer实现线性复杂度的时空建模。
result: 实验显示DriveMamba在多项规划指标上达到SOTA，同时推理速度显著提升。
conclusion: 状态空间模型是替代Transformer进行高效端到端自动驾驶建模的有效方案。
---

## Abstract
Recent advances towards End-to-End Autonomous Driving (E2E-AD) focus on integrating modular designs into a unified framework for joint optimization. Most of these advances follow a sequential paradigm (i.e., perception-prediction-planning) based on separable Transformer decoders and rely on dense BEV features to encode scene representations. However, such manual ordering design can inevitably cause information loss and cumulative errors, lacking flexible and diverse relation modeling among different modules and sensors. Meanwhile, insufficient training of image backbone and quadratic-complexity of attention mechanism also hinder the scalability and efficiency of E2E-AD system to handle spatiotemporal input. To this end, we propose DriveMamba, a Task-Centric Scalable paradigm for efficient E2E-AD, which integrates dynamic task relation modeling, implicit view correspondence learning and long-term temporal fusion into a single-stage Unified Mamba decoder. Specifically, both extracted image features and expected task outputs are converted into token-level sparse representations in advance, which are then sorted by their instantiated positions in 3D space. The linear-complexity operator enables efficient long-context sequential token modeling to capture task-related inter-dependencies simultaneously. Additionally, a bidirectional trajectory-guided "local-to-global" scan method is designed to preserve spatial locality from ego-perspective, thus facilitating the ego-planning. Extensive experiments conducted on nuScenes and Bench2Drive datasets demonstrate the superiority, generalizability and great efficiency of DriveMamba.

---

## 论文详细总结（自动生成）

# 论文中文详细总结

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：现有端到端自动驾驶（E2E-AD）系统多采用“感知-预测-规划”的序列范式，基于可分离的 Transformer 解码器和稠密 BEV 特征编码场景表示。这种手动排序设计会导致信息丢失和累积误差，且不同模块与传感器之间缺乏灵活多样的关系建模。同时，图像骨干网络训练不充分以及注意力机制的二次复杂度（quadratic complexity）严重限制了系统的可扩展性和效率，难以高效处理时空输入。
- **整体含义**：本文旨在探索一种线性复杂度的新型架构，替代 Transformer，以实现高效、可扩展且任务中心的端到端自动驾驶建模。

## 2. 论文提出的方法论
- **核心思想**：采用基于状态空间模型（State Space Model, SSM）的 Mamba 结构，替代 Transformer，实现线性复杂度的长序列建模。设计“任务中心可扩展范式”（Task-Centric Scalable Paradigm），将多任务（感知、预测、规划）动态关系建模、隐式视角对应学习和长期时序融合整合到单个**单阶段统一 Mamba 解码器**中。
- **关键技术细节**：
  - **Token 级稀疏表示**：先分别将提取的图像特征和期望的任务输出转换为 token 级稀疏表示，然后按照它们在 3D 空间中的实例化位置进行排序。
  - **线性复杂度算子**：利用 Mamba 的线性复杂度（相对于 Transformer 的二次复杂度）实现高效的长上下文顺序 token 建模，同时捕获任务相关的相互依赖关系。
  - **双向轨迹引导的“局部到全局”扫描方法**：设计了一种自车视角下的扫描策略，先局部后全局，以保持空间局部性，从而促进自车规划任务。
- **算法流程（文字说明）**：
  1. 多视角图像经骨干网络提取特征。
  2. 特征和任务输出（如目标检测、轨迹预测、规划路径）被转化为稀疏 token，并赋予 3D 空间坐标。
  3. 所有 token 按 3D 位置排序后输入 Mamba 解码器。
  4. Mamba 解码器通过状态空间模型进行双向（局部到全局）顺序处理，捕捉 token 之间的时空依赖。
  5. 最终输出多任务结果，包括规划轨迹。

## 3. 实验设计
- **数据集**：使用 **nuScenes** 和 **Bench2Drive** 两个公开自动驾驶数据集。
- **基准（Benchmark）**：端到端规划任务，评估指标包括碰撞率、位移误差（如 L2 error）、规划成功率等（具体指标需参考原文，但摘要未详列）。
- **对比方法**：主要与基于 Transformer 的基线方法（如 UniAD、VAD 等常见 E2E-AD 方法）进行比较，同时可能包括其他 SOTA 方法。

## 4. 资源与算力
- **文中未明确说明**使用的 GPU 型号、数量及训练时长。无法从摘要和元数据中获取具体算力信息，因此在后续总结中需指出这一点。

## 5. 实验数量与充分性
- **实验数量**：在两个不同复杂度数据集（nuScenes 和 Bench2Drive）上进行了评估，推测还包含消融实验（如验证双向轨迹引导扫描、稀疏 token 表示、单阶段解码器等模块的有效性），但具体组数未列出。
- **充分性评估**：实验覆盖了主流规划指标和两个代表性数据集，结果显示了 SOTA 性能，且验证了效率提升（推理速度显著）。但缺少极端场景（如恶劣天气、夜间）、真实路测以及安全性分析，因此整体**较充分但尚存提升空间**。实验设计较为客观公平，对比了 Transformer 基线。

## 6. 论文的主要结论与发现
- **主要结论**：基于 Mamba 的状态空间模型是替代 Transformer 进行高效端到端自动驾驶建模的有效方案。DriveMamba 在多项规划指标上达到 SOTA，同时推理速度显著提升，展示了线性复杂度架构在自动驾驶任务中的优越性。
- **发现**：任务中心设计和隐式视角对应学习可以减少手动排序带来的信息损失；双向轨迹引导扫描有助于保持空间局部性，提升规划质量。

## 7. 优点
- **效率高**：Mamba 的线性复杂度显著降低了计算开销，推理速度快于 Transformer 基线。
- **减少信息损失**：采用任务中心单阶段解码器，避免了模块间序列化导致的累积误差和手动关系限制。
- **可扩展性强**：稀疏 token 表示和长序列建模能力便于处理多传感器、多帧输入。
- **设计创新**：双向轨迹引导的“局部到全局”扫描方法贴近自车视角，有效融合局部细节与全局上下文。

## 8. 不足与局限
- **实验覆盖**：仅在 nuScenes 和 Bench2Drive 两个数据集上验证，未在更多挑战性场景（如无信号灯路口、密集行人、极端天气）进行测试；缺乏真实车辆部署验证。
- **细节缺失**：算力资源（GPU 型号、训练时长等）未公布，影响可复现性。
- **潜在偏差风险**：稀疏 token 表示可能丢失部分图像细节（如小物体、纹理），对感知精度有潜在影响。
- **可解释性**：状态空间模型的黑盒特性可能比 Transformer 更难解释，不利于安全分析。
- **长期时序建模**：虽然 Mamba 理论上支持长序列，但实际中是否完全克服 Transformer 的上下文长度限制仍需更深入评估。

（完）
