---
title: "MaskGWM: A Generalizable Driving World Model with Video Mask Reconstruction"
title_zh: MaskGWM：基于视频掩码重建的泛化驾驶世界模型
authors: "Ni, Jingcheng, Guo, Yuxin, Liu, Yichen, Chen, Rui, Lu, Lewei, Wu, Zehuan"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Ni_MaskGWM_A_Generalizable_Driving_World_Model_with_Video_Mask_Reconstruction_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 7.0
evidence: 驾驶世界模型预测环境变化，支持规划与轨迹预测
tldr: 现有驾驶世界模型受限于预测时长和泛化能力。本文结合像素级生成损失与掩码自编码器风格的特征学习，提出基于扩散Transformer的MaskGWM。通过掩码重建任务使模型学习更鲁棒的时空表示。在多个规划任务上，该世界模型能生成更长时序的准确环境预测，并提升了下游规划性能。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1770, \"height\": 413, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 509, \"height\": 502, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1756, \"height\": 926, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1778, \"height\": 468, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 823, \"height\": 507, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1668, \"height\": 518, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1129, \"height\": 380, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 874, \"height\": 628, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 588, \"height\": 211, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 718, \"height\": 379, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 562, \"height\": 235, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 989, \"height\": 383, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 496, \"height\": 236, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-ni-maskgwm-a-generalizable-driving-world-model-with-video-mask-reconstruction-cvpr-2025-paper/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 546, \"height\": 234, \"label\": \"Table\"}]"
motivation: 现有世界模型预测时长有限，泛化能力差。
method: 设计扩散Transformer架构，联合像素生成与MAE式掩码上下文学习。
result: 生成更长预测序列，并在下游规划任务上取得更好性能。
conclusion: 特征级与像素级损失结合的世界模型显著提升预测与规划能力。
---

## Abstract
World models that forecast environmental changes from actions are vital for autonomous driving models with strong generalization. The prevailing driving world model mainly build on pixel-level video prediction model. Although these models can produce high-fidelity video sequences with advanced diffusion-based generator, they are constrained by their predictive duration and overall generalization capabilities. In this paper, we explore to solve this problem by combining pixel-level generation loss with MAE-style feature-level context learning. In particular, we instantiate this target with three key design: (1) A more scalable Diffusion Transformer (DiT) structure trained with extra mask construction task. (2) we devise diffusion-related mask tokens to deal with the fuzzy relations between mask reconstruction and generative diffusion process. (3) we extend mask construction task to spatial-temporal domain by utilizing row-wise mask for shifted self-attention rather than masked self-attention in MAE. Then, we adopt a row-wise cross-view module to align with this mask design. Based on above improvement, we propose MaskGWM: a Generalizable driving World Model embodied with Video Mask reconstruction. Our model contains two variants: MaskGWM-long, focusing on long-horizon prediction, and MaskGWM-mview, dedicated to multi-view generation.Comprehensive experiments on standard benchmarks validate the effectiveness of the proposed method, which contain normal validation of Nuscene dataset, long-horizon rollout of OpenDV-2K dataset and zero-shot validation of Waymo dataset. Quantitative metrics on these datasets show our method notably improving state-of-the-art driving world model.

---

## 论文详细总结（自动生成）

# 详细中文总结

## 1. 核心问题与整体含义（研究动机与背景）
- **核心问题**：现有驾驶世界模型主要基于像素级视频预测（如扩散模型），虽然能生成高保真视频，但在**预测时长**和**泛化能力**上存在明显局限。模型往往无法稳定生成长时间序列，且对新场景（如天气变化、不同数据集）的零样本泛化能力差。
- **研究动机**：作者认为仅依靠扩散生成损失（像素级）不足以学习到鲁棒的视觉语义上下文，而自监督掩码自动编码器（MAE）能够有效地从大规模数据中学习特征表示。因此，将**像素级生成损失**与**MAE风格的特征级上下文学习**相结合，可能是提升世界模型泛化性和长时预测能力的关键。
- **整体含义**：提出一种名为**MaskGWM**的通用驾驶世界模型，通过联合扩散生成和视频掩码重建任务，实现更长的预测时间、更强的零样本迁移能力以及多视图生成能力。

## 2. 方法论：核心思想、关键技术细节、流程
- **核心思想**：在扩散Transformer（DiT）架构上，引入**视频掩码重建**（Video Mask Reconstruction）作为辅助任务，使模型在去噪过程中同时学习空间的场景对象建模和时间的目标运动建模。通过专门设计的掩码令牌和双分支掩码策略，解决扩散过程与掩码重建之间的模糊关系。
- **关键设计**：
  1. **扩散相关掩码令牌**（Diffusion-related Mask Tokens）：
     - 在编码器中丢弃不可见令牌后，用特殊掩码令牌填充。该令牌结合了可学习参数 \( p \) 和噪声嵌入 \( f_m(\epsilon) \)，并按时间步 \(\tau\) 线性插值：\( m_\tau = (1-\tau)f_m(\epsilon) + \tau p \)。
     - 当 \(\tau\) 大（高噪声）时，依赖可学习参数提供平均分布指导；当 \(\tau\) 小（低噪声）时，依赖噪声信息恢复细节，从而平衡两个任务。
  2. **时空双分支掩码策略**：
     - **空间分支**：使用跨帧共享的随机掩码 \( M_{spatial} \)，通过空间Transformer重建被掩码的令牌，建模场景内对象。
     - **时间分支**：使用逐帧不同的掩码 \( M_{time} \)，并采用**逐行移位掩码**（Row-wise Shift Mask）代替标准掩码自注意力。每行随机掩码相同数量的令牌，然后丢弃不可见令牌，可见令牌在时间轴上直接连接，形成移位自注意力。这样避免额外的3D注意力掩码开销，加速训练且保持时间上下文推理。
  3. **逐行交叉视图模块**：对于多视图生成，在视图维度上应用类似的逐行掩码，将不同视图的同一行特征水平拼接进行自注意力，实现高效的跨视图信息交换。
- **算法流程**（文字说明）：
  - 输入多帧多视图视频，经VAE编码器和Patch嵌入得到潜在令牌。
  - 在训练时，随机选择使用空间掩码或时间掩码（各50%概率）。
  - 编码器仅处理可见令牌，不可见令牌被丢弃，然后填充扩散相关掩码令牌。
  - 通过对应的双分支Transformer（空间或时间）重建被掩码令牌的表示。
  - 最终所有令牌（可见+重建）送入完整DiT进行扩散去噪，损失函数为Rectified Flow的v-prediction损失与掩码重建损失（隐式包含在整体训练中）。

## 3. 实验设计
- **数据集**：
  - **OpenDV-2K**：大规模网络爬取驾驶视频（1740小时），用于预训练和长时预测评估。
  - **nuScenes**：多视图驾驶数据集，用于标准评测和多视图生成评估。
  - **Waymo**：用于零样本泛化测试（模型未见过的数据集）。
- **Benchmark与评价指标**：
  - 单视图评估：FID（图像保真度）、FVD（视频保真度），遵循VISTA的设置。
  - 多视图评估：FID、FVD，遵循Drive-WM的设置。
  - 零样本评估：在Waymo验证集上计算FVD和FID。
  - 长时预测：在OpenDV-2K验证集上计算不同时间步长的FVD增长率。
- **对比方法**：
  - 单视图：GenAD, VISTA, DriveGAN等。
  - 多视图：Drive-WM, DiVE, MagicDrive, DriveDreamer-2, Panacea等。

## 4. 资源与算力
- 论文中**未明确说明**训练所用的具体GPU型号、数量及总训练时长。
- 仅提及模型初始化自**SD3 medium checkpoint（2B参数）**，训练分为三个阶段，各阶段迭代次数和batch size有描述（Stage1：18K+24K+20K步；Stage2：未明确步数；Stage3：6K步）。但未给出实际硬件配置和耗时。

## 5. 实验数量与充分性
- **实验组数**：论文进行了**大量实验**，包括：
  - **主实验**：在nuScenes上对比单视图和多视图SOTA方法（Table 1）。
  - **零样本泛化**：在Waymo上与VISTA对比（Table 2）。
  - **长时预测**：在OpenDV-2K上对比VISTA的FVD曲线（Figure 6）。
  - **消融实验**：详细分析了掩码令牌设计（Table 3a）、双分支掩码策略（Table 3b）、掩码比例与移位注意力（Table 4a）、双分支重建结构（Table 4b）、跨视图模块设计（Table 4c）。
- **充分性与客观性**：实验设计较为充分，覆盖了生成质量、泛化、长时预测等多个维度；消融实验控制变量清晰，结果具有说服力。但部分对比方法（如VISTA）使用了官方checkpoint进行推理，确保公平性。整体实验比较客观。

## 6. 主要结论与发现
- MaskGWM在多个数据集上均取得了**最优或极具竞争力的结果**：
  - 单视图：FID 5.6, FVD 92.5（nuScenes），超过VISTA和GenAD。
  - 多视图：FID 8.9, FVD 65.4，无需未来布局信息。
  - 零样本：FVD 118.83（Waymo），显著优于VISTA。
  - 长时预测：FVD曲线增长更慢，表明长时间序列稳定性更强。
- 掩码重建作为辅助任务能有效提升生成质量和泛化能力；扩散相关掩码令牌的设计是成功的关键。双分支时空掩码策略优于单一掩码。

## 7. 优点
- **方法创新**：
  - 创新性地将**掩码自监督学习**引入驾驶世界模型的扩散训练中，并设计专门的扩散相关掩码令牌解决两个任务的冲突。
  - 提出**逐行移位掩码**，实现高效的时间建模，无需额外的注意力掩码，可复用FlashAttention等优化算子，提升训练速度。
  - 双分支掩码策略分别针对空间和时间上下文，使模型更全面地理解场景。
- **实验广度**：涵盖了标准评测、零样本泛化、长时预测、多视图等多个挑战性场景，验证了方法的通用性。
- **性能提升**：在多个指标上显著超越现有SOTA，尤其在长时预测和泛化上显示出优势。

## 8. 不足与局限
- **算力信息缺失**：未披露训练所需的具体GPU资源和时间，使得他人难以复现和评估成本。
- **下游任务验证不足**：论文仅评估了生成质量（FID/FVD），未将模型应用于下游的规划或控制任务，无法证明生成质量提升能直接转化为实际驾驶决策性能的提升。
- **泛化局限**：零样本验证仅在一个数据集（Waymo）上进行，且时间未说明是否为严格零样本（是否与训练集有重叠风险）。更多不同国家、不同风格的场景有待测试。
- **掩码策略的敏感性**：消融实验表明时间分支对掩码比例更敏感，可能需要针对不同数据分布调参。
- **模型复杂度**：基于2B参数的SD3，计算成本较高，可能限制实际部署。

（完）
