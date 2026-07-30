---
title: "GEM: A Generalizable Ego-Vision Multimodal World Model for Fine-Grained Ego-Motion, Object Dynamics, and Scene Composition Control"
title_zh: GEM：一种可泛化的自我视觉多模态世界模型，用于细粒度自我运动、物体动力学和场景组成控制
authors: "Hassan, Mariam, Stapf, Sebastian, Rahimi, Ahmad, Rezende, Pedro M B, Haghighi, Yasaman, Brüggemann, David, Katircioglu, Isinsu, Zhang, Lin, Chen, Xiaoran, Saha, Suman, Cannici, Marco, Aljalbout, Elie, Ye, Botao, Wang, Xi, Davtyan, Aram, Salzmann, Mathieu, Scaramuzza, Davide, Pollefeys, Marc, Favaro, Paolo, Alahi, Alexandre"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Hassan_GEM_A_Generalizable_Ego-Vision_Multimodal_World_Model_for_Fine-Grained_Ego-Motion_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 7.0
evidence: 世界模型控制自我轨迹，支持规划
tldr: 世界模型在自动驾驶中可用于规划，但目前缺乏对自我轨迹的精细控制。本文提出GEM，一种可泛化的自我视觉多模态世界模型，通过参考帧、稀疏特征、人体姿态和自我轨迹预测未来帧，实现对自我运动、物体动力学和场景组成的精细控制。基于4000+小时多模态数据训练，可生成稳定的长时预测，为轨迹规划提供可控环境。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-hassan-gem-a-generalizable-ego-vision-multimodal-world-model-for-fine-grained-ego-motion-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1791, \"height\": 677, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-hassan-gem-a-generalizable-ego-vision-multimodal-world-model-for-fine-grained-ego-motion-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1804, \"height\": 577, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-hassan-gem-a-generalizable-ego-vision-multimodal-world-model-for-fine-grained-ego-motion-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 698, \"height\": 506, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-hassan-gem-a-generalizable-ego-vision-multimodal-world-model-for-fine-grained-ego-motion-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 881, \"height\": 671, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-hassan-gem-a-generalizable-ego-vision-multimodal-world-model-for-fine-grained-ego-motion-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 752, \"height\": 497, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-hassan-gem-a-generalizable-ego-vision-multimodal-world-model-for-fine-grained-ego-motion-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1799, \"height\": 665, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-hassan-gem-a-generalizable-ego-vision-multimodal-world-model-for-fine-grained-ego-motion-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 867, \"height\": 461, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-hassan-gem-a-generalizable-ego-vision-multimodal-world-model-for-fine-grained-ego-motion-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 873, \"height\": 527, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-hassan-gem-a-generalizable-ego-vision-multimodal-world-model-for-fine-grained-ego-motion-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 875, \"height\": 475, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-hassan-gem-a-generalizable-ego-vision-multimodal-world-model-for-fine-grained-ego-motion-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1811, \"height\": 299, \"label\": \"Table\"}]"
motivation: 现有世界模型缺乏对自我轨迹的精细控制，难以用于规划。
method: 提出GEM模型，以自我轨迹为条件，自回归预测未来RGB和深度帧。
result: 在多个领域实现可控的长期帧预测，证明了轨迹控制的有效性。
conclusion: GEM提供了一种可泛化的自我轨迹控制方法，有助于自动驾驶规划研究。
---

## Abstract
We present GEM, a Generalizable Ego-vision Multimodal world model that predicts future frames using a reference frame, sparse features, human poses, and ego-trajectories. Hence, our model has precise control over object dynamics, ego-agent motion and human poses. GEM generates paired RGB and depth outputs for richer spatial understanding. We introduce autoregressive noise schedules to enable stable long-horizon generations. Our dataset is comprised of 4000+ hours of multimodal data across domains like autonomous driving, egocentric human activities, and drone flights. Pseudo-labels are used to get depth maps, ego-trajectories, and human poses. We use a comprehensive evaluation framework, including a new Control of Object Manipulation (COM) metric, to assess controllability. Experiments show GEM excels at generating diverse, controllable scenarios and temporal consistency over long generations. Code, models, and datasets are fully open-sourced.

---

## 论文详细总结（自动生成）

## 论文详细中文总结

### 1. 核心问题与整体含义

- **研究动机**：现有的自我视觉世界模型（如自动驾驶、人机交互、无人机导航）通常仅支持单一的自我运动控制（如自车轨迹），缺乏对场景中其他物体动态、人体姿态的精细控制，且大多局限于单一任务域，难以泛化到多个视觉领域。
- **整体含义**：本文提出GEM，一个可泛化的多模态世界模型，能够同时控制自我运动、物体运动和人体姿态，并生成RGB和深度图，支持多域（驾驶、人类活动、无人机）应用，为复杂交互场景的预测和规划提供更强的可控性和泛化能力。

### 2. 方法论

- **核心思想**：基于Stable Video Diffusion（SVD）作为骨干网络，通过引入三种控制信号（自我轨迹、DINOv2稀疏特征、人体姿态）实现细粒度可控的视频生成，并采用自回归噪声调度实现长序列帧的稳定生成。
- **关键技术细节**：
  - **自我运动控制**：将全局的自我轨迹（3D轨迹投影到鸟瞰图2D位置）通过傅立叶嵌入后，利用LoRA模块注入到UNet的交叉注意力层。
  - **对象级控制**：从参考帧提取稀疏DINOv2特征图，通过随机掩码和零填充得到条件特征；引入学习到的身份嵌入（Identity Embedding）区分是移动已有对象还是插入新对象；训练时利用光流将令牌迁移到后续帧。特征通过ObjectNet（类似UNet输入分支的网络）处理后加到UNet输入层的输出中。
  - **人体姿态控制**：将渲染的人体骨架图像通过PoseNet（小型CNN）提取特征，同样加到UNet特征中。
  - **多模态生成**：将深度图作为额外模态，使用与图像相同的VAE编码/解码，输入时连接两个模态，输出时通过单独的投影层P_depth预测深度噪声。
  - **长序列生成**：采用自回归采样和动态噪声调度：初始化阶段逐帧开始去噪，自回归阶段每完成一帧全去噪后移除并添加新噪声帧，终止阶段直到剩余帧全部处理完；训练时使用带随机偏移的噪声分布来匹配推理过程。
- **算法流程**：输入参考帧、噪声潜变量（RGB和深度）、条件（轨迹、DINO特征、人体姿态） → UNet去噪（分帧加噪/去噪） → 依次生成未来RGB和深度帧。

### 3. 实验设计

- **数据集**：
  - 驾驶域：OpenDV（1747h）、BDD（1000h）、Nuscenes（5.5h）、Driving Dojo（150h）等共3211小时。
  - 人类自我活动：EgoExo4D（1000h）。
  - 无人机：自采集YouTube视频（27.4h）。
  - 总计约4238小时多模态数据，均使用伪标签生成深度、轨迹和人体姿态。
- **基准数据集**：Nuscenes验证集和OpenDV验证集的随机子集。
- **对比方法**：Vista（最相近的基线）、DriveGAN、DriveDreamer、DriveDreamer-2、WoVoGen、Drive-WM、GenAD等。
- **评价指标**：
  - 视频质量：FID、FVD。
  - 自我运动控制：平均位移误差（ADE）。
  - 对象运动控制：新提出的COM（Control of Object Manipulation），用YOLOv11检测并计算边界框中心位置差异。
  - 人体姿态控制：基于DWPose的COCO AP（平均精度）。
  - 深度质量：AbsRel、δ<1.25。
  - 还进行了人类评估（116次响应，对比短/长视频）。

### 4. 资源与算力

- 文中**未明确说明**GPU型号、数量及训练时长。
- 致谢部分提到：本项目由瑞士国家超算中心（CSCS）提供算力支持，项目ID a03（运行于Alps超级计算机）。具体训练细节仅在补充材料中提及（但本文未提供补充材料细节），因此无法准确量化。

### 5. 实验数量与充分性

- **实验组数**：
  - 质量对比：在两个数据集（Nuscenes、OpenDV）上进行FID/FVD对比，覆盖7种基线方法。
  - 长序列质量对比：生成150帧，统计6个长度点（25,50,75,100,125,150），与Vista对比。
  - 人类评估：100个视频（50短+50长），116人参与。
  - 可控性评估：自我运动（3组ADE：Nuscenes全集、Nuscenes子集、OpenDV）、对象运动（COM，2数据集）、人体姿态（AP，2种IoU标准）。
  - 深度质量结果在补充材料中（提及但未在正文展示）。
  - 消融实验在补充材料中。
- **充分性**：实验覆盖了主要可控维度，并引入了主观评估，整体较为充分。但消融实验未在正文呈现，控制信号的独立贡献分析不够直观；对比方法（如Vista）只复现了其公开结果，可能因训练差异导致公平性略欠。

### 6. 主要结论与发现

- GEM在长序列生成中表现优于Vista（更低的FVD和FID），人类评估中长视频被明显偏好。
- 自我运动控制：在有歧义的场景（Nuscenes子集）中条件生成ADE比无控制降低18%（从3.59→2.85），证明控制有效。
- 对象运动控制：COM值在Nuscenes和OpenDV上分别降低68.8%和79%，条件生成显著提升对象跟踪精度。
- 人体姿态控制：条件生成AP（大尺度、严格IoU）从0.00提升到0.12，证明控制有效。
- 多模态生成（深度）质量可接受，但未提供与其他方法的直接对比。

### 7. 优点

- **高度可控性**：同时支持自我运动、对象移动/插入、人体姿态三种控制，且通过DINOv2特征支持新对象插入。
- **多域泛化**：在驾驶、人类活动、无人机三个不同领域进行了训练和测试，展示了强大泛化能力。
- **多模态输出**：生成RGB和深度，提供几何信息。
- **长序列稳定性**：创新自回归噪声调度，显著优于滑动窗口方法（Vista）在长序列上的表现。
- **数据集规模与质量**：利用4000+小时数据并精心筛选，生成伪标签，开源了所有代码、模型和数据集，促进了社区研究。
- **新指标**：提出COM用于评估对象运动控制。
- **人类评估**：证实长序列主观质量优势。

### 8. 不足与局限

- **视觉质量**：FID在Nuscenes上比Vista差（10.5 vs 6.6），可能是由于数据筛选优先可控性而非视觉质量，以及未在Nuscenes上充分微调。
- **长序列质量仍有退化**：论文承认长序列质量与一致性仍需提升。
- **算力信息缺失**：未报告具体训练资源，可复现性受影响。
- **人体姿态控制AP较低**：仅0.12（严格IoU），控制精确度有限，尤其对小人体。
- **消融实验未在正文展示**：读者无法直接看到各组件的贡献，需查阅补充材料。
- **深度模态评估不全面**：深度质量仅用相对误差和阈值，未与现有深度生成方法对比，也未在控制任务中独立验证。
- **泛化测试范围有限**：仅在驾驶和人类活动/无人机的有限子集上测试，更多域（如机器人、室内）未涉及。

（完）
