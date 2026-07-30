---
title: Multi-modal Knowledge Distillation-based Human Trajectory Forecasting
title_zh: 基于多模态知识蒸馏的行人轨迹预测
authors: "Jeong, Jaewoo, Lee, Seohee, Park, Daehee, Lee, Giwon, Yoon, Kuk-Jin"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Jeong_Multi-modal_Knowledge_Distillation-based_Human_Trajectory_Forecasting_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 8.0
evidence: 面向自动驾驶的行人轨迹预测，使用多模态知识蒸馏
tldr: 行人轨迹预测对自动驾驶至关重要，但实时提取文本等额外模态计算成本高。本文提出多模态知识蒸馏框架，教师模型使用完整模态（包括文本描述）训练，学生模型仅使用有限模态在线推理，通过蒸馏继承教师知识。实验表明学生模型在低计算资源下保持了接近教师模型的预测精度，适合资源受限的车载系统。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-jeong-multi-modal-knowledge-distillation-based-human-trajectory-forecasting-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 844, \"height\": 635, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-jeong-multi-modal-knowledge-distillation-based-human-trajectory-forecasting-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1781, \"height\": 597, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-jeong-multi-modal-knowledge-distillation-based-human-trajectory-forecasting-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1784, \"height\": 446, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-jeong-multi-modal-knowledge-distillation-based-human-trajectory-forecasting-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1801, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-jeong-multi-modal-knowledge-distillation-based-human-trajectory-forecasting-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 869, \"height\": 284, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-jeong-multi-modal-knowledge-distillation-based-human-trajectory-forecasting-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1804, \"height\": 496, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-jeong-multi-modal-knowledge-distillation-based-human-trajectory-forecasting-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 866, \"height\": 379, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-jeong-multi-modal-knowledge-distillation-based-human-trajectory-forecasting-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 869, \"height\": 389, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-jeong-multi-modal-knowledge-distillation-based-human-trajectory-forecasting-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 867, \"height\": 399, \"label\": \"Table\"}]"
motivation: 在线使用视觉语言模型提取文本描述计算量大，不适合实时系统。
method: 设计师生蒸馏框架，教师用多模态训练，学生以有限模态模仿教师输出分布。
result: 在多个行人轨迹数据集上，学生模型在显著降低推理时间的同时保持高准确率。
conclusion: 知识蒸馏有效平衡了多模态轨迹预测的精度与效率。
---

## Abstract
Pedestrian trajectory forecasting is crucial in various applications such as autonomous driving and mobile robot navigation. In such applications, camera-based perception enables the extraction of additional modalities (human pose, text) to enhance prediction accuracy. Indeed, we find that textual descriptions play a crucial role in integrating additional modalities into a unified understanding. However, online extraction of text requires the use of VLM, which may not be feasible for resource-constrained systems. To address this challenge, we propose a multi-modal knowledge distillation framework: a student model with limited modality is distilled from a teacher model trained with full range of modalities. The comprehensive knowledge of a teacher model trained with trajectory, human pose, and text is distilled into a student model using only trajectory or human pose as a sole supplement. In doing so, we separately distill the core locomotion insights from intra-agent multi-modality and inter-agent interaction. Our generalizable framework is validated with two state-of-the-art models across three datasets on both ego-view (JRDB, SIT) and BEV-view (ETH/UCY) setups, utilizing both annotated and VLM-generated text captions. Distilled student models show consistent improvement in all prediction metrics for both full and instantaneous observations, improving up to 13%. The code is available at github.com/Jaewoo97/KDTF.

---

## 论文详细总结（自动生成）

# 基于多模态知识蒸馏的行人轨迹预测论文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **问题**：行人轨迹预测在自动驾驶和移动机器人导航中至关重要，引入额外模态（如人体姿态、文本描述）能显著提升预测精度。然而，文本描述的在线提取依赖于计算代价高的视觉语言模型（VLM），在资源受限的移动系统中不可行。
- **动机**：如何在不增加在线计算负担的前提下，将多模态（包括文本）带来的预测增益传递给学生模型？本文提出知识蒸馏框架，使得学生模型在推理时仅使用有限的可用模态（如轨迹X或轨迹+人体姿态X+P），却能继承教师模型利用全部模态（X+P+文本S）所获得的综合运动意图理解能力。
- **整体含义**：本文首次将多模态知识蒸馏引入行人轨迹预测，证明文本在桥接模态差异、提升瞬时预测等方面具有关键作用，并验证了蒸馏框架在多种场景下的泛化性。

## 2. 论文提出的方法论：核心思想、关键技术细节、算法流程
### 核心思想
- 构建一个教师模型，同时利用轨迹（X）、3D人体姿态（P）和文本描述（S）进行训练，获得对运动意图的全面理解。
- 学生模型仅输入X或X+P，通过蒸馏损失对齐教师模型的两个关键潜在空间：**局部编码器输出（Q）**（表示单智能体粗粒度运动意图）和**全局编码器输出（H）**（表示智能体间交互后的完整运动意图）。
- 蒸馏过程与回归损失联合训练，使学生不仅模仿教师中间表示，还能独立完成轨迹预测，有时甚至超越教师（由于额外正则化）。

### 关键技术细节
- **模态嵌入**：分别使用MLP编码轨迹、人体姿态（SMPL参数），使用预训练TinyBERT编码文本（类token）。JRDB数据集中还有交互文本（S<sub>R</sub>）和行为文本（S<sub>A</sub>）。
- **局部编码器（E<sub>L</sub>）**：基于Transformer或图神经网络（HiVT）在模态和时间维度上融合特征，提取每个智能体的粗粒度运动意图Q。
- **全局编码器（E<sub>G</sub>）**：在智能体之间建模交互，输出H（最终特征表示）。JRDB中使用交互文本作为边特征。
- **解码器**：MLP将H映射为多模态未来轨迹（6种模式）。
- **蒸馏损失**：对Q和H分别计算KL散度（对MART）或余弦相似度+KL散度（对HiVT）。损失包括全观测、2帧、1帧三种设置，与回归损失加权求和。

### 算法流程（文字说明）
1. 教师模型使用完整模态（X+P+S）预训练，优化回归损失（包括全观测、瞬时2帧、1帧三种情况）。
2. 冻结教师模型，学生模型（仅X或X+P）从头训练，同时最小化回归损失和蒸馏损失（对齐Q和H）。
3. 蒸馏损失涉及教师和学生的局部编码器输出、全局编码器输出，同样覆盖三种观测设置。

## 3. 实验设计
### 使用数据集
- **JRDB**（主数据集）：机器人视角，含13个场景，提供3D人体姿态和人工标注的交互文本。
- **SIT**：机器人视角，使用VLM（PLLaVa）生成文本描述。
- **ETH/UCY**：鸟瞰视角，低分辨率，使用CLIP图像特征替代人体姿态，使用基于规则的文本（描述地图障碍物）。

### Benchmark
- 标准指标：ADE（平均位移误差）、FDE（最终位移误差），并特别报告瞬时观测（1帧、2帧）下的ADE1、ADE2、FDE1、FDE2。

### 对比方法
- **基线模型**：HiVT（图网络）、MART（Transformer）。论文还对比了ST（SocialTransmotion，专门处理多模态）和LED（扩散模型）。
- 所有模型均调整至相似参数量以确保公平。

## 4. 资源与算力
- **论文未明确说明使用的GPU型号、数量、训练时长**。仅在方法部分提到使用预训练TinyBERT、SMPL提取器等标准模块，但未披露硬件配置。这是本报告中需要指出的信息缺失。

## 5. 实验数量与充分性
### 实验组数概览
- **主要结果**：涵盖三个数据集（JRDB、SIT、ETH/UCY）、两种学生模态（X、X+P）、两种基线模型（HiVT、MART），以及全观测和瞬时观测，共约30余组定量结果。
- **消融实验**：
  1. 蒸馏组件消融（L<sub>LKD</sub> vs L<sub>GKD</sub>）。
  2. 交互文本S<sub>R</sub>的贡献（表5）。
  3. 不同VLM提示类型对文本生成的影响（表6）。
  4. 教师模型多模态增益验证（表1）。
- **定性结果**：展示了JRDB上的可视化预测对比。

### 充分性评价
- **充分**：实验覆盖了主流的ego-view和BEV-view数据集，两种典型模型架构（图+Transformer），多种模态组合，并对蒸馏核心组件进行了系统消融。公平性方面，基线模型参数调整相近，对比方法（ST、LED）也纳入评估。
- **客观**：指标使用标准ADE/FDE，报告全观测和瞬时情况，结果具有区分度。未发现明显倾向性或数据 cherry-picking。

## 6. 论文的主要结论与发现
- **文本描述是关键**：在教师模型中，文本S的引入带来最大性能提升（表1），并能桥接姿态噪声与轨迹之间的域差距。
- **知识蒸馏有效**：学生模型（仅X或X+P）经过蒸馏后，在所有数据集和观测设置下一致提升，最高达13%（SIT数据集上X+P学生提升13.03%）。
- **蒸馏局部和全局表示均重要**：消融表明仅蒸馏局部编码器（Q）提升约3%，仅蒸馏全局编码器（H）提升约2%，两者结合效果最佳（约5-6%）。
- **交互文本S<sub>R</sub>有额外增益**：在X模型上引入交互文本带来约4.6%提升，且对蒸馏也有帮助。
- **VLM提示类型影响性能**：描述过去行为的文本（Prompt 1）最适合知识蒸馏，因为与人体姿态直接相关。

## 7. 优点：方法或实验设计上的亮点
- **首次提出**多模态知识蒸馏用于轨迹预测，特别是将VLM生成的文本作为教师知识源。
- **框架通用性强**：可适配不同基线模型（Transformer、图网络）和不同数据集（ego-view、BEV-view）。
- **同时蒸馏局部和全局知识**：分别处理单智能体运动意图和交互，符合轨迹预测的层级结构。
- **瞬时预测设置**：评估1-2帧极端情况，凸显多模态和蒸馏的实际价值（如遮挡场景），实验更贴近真实部署。
- **多模态协同分析**：详细解释了文本如何弥合姿态噪声与轨迹之间的语义鸿沟，提供了深入理解。

## 8. 不足与局限
- **算力资源未公开**：缺少训练所需GPU型号、数量、时间等信息，不利于复现和能耗评估。
- **姿态模态实用性有待验证**：在JRDB上X+P在某些设置下比X还差（表1），表明姿态提取噪声可能损害性能，蒸馏部分缓解但未根本解决。
- **文本生成质量依赖VLM**：SIT数据集使用PLLaVa，但未对不同VLM进行鲁棒性测试；ETH/UCY使用规则文本，泛化性有限。
- **未讨论多模态对齐失效情况**：当文本描述不准确或与行为不一致时，可能误导学生，论文未分析失败案例。
- **应用场景限制**：仅测试行人，未扩展到车辆轨迹预测；且数据集场景有限（主要是校园/街道），极端杂乱场景未覆盖。
- **没有与直接使用教师模型在线推理做效率对比**：虽然知识蒸馏旨在降低推理成本，但未给出具体速度或参数量对比数据。

（完）
