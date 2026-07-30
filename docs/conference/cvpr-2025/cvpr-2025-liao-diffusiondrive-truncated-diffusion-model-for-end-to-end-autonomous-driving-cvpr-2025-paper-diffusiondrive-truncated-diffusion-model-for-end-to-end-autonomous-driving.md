---
title: "DiffusionDrive: Truncated Diffusion Model for End-to-End Autonomous Driving"
title_zh: DiffusionDrive：端到端自动驾驶的截断扩散模型
authors: "Liao, Bencheng, Chen, Shaoyu, Yin, Haoran, Jiang, Bo, Wang, Cheng, Yan, Sixu, Zhang, Xinbang, Li, Xiangyu, Zhang, Ying, Zhang, Qian, Wang, Xinggang"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Liao_DiffusionDrive_Truncated_Diffusion_Model_for_End-to-End_Autonomous_Driving_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 9.0
evidence: 端到端自动驾驶扩散模型生成多模式驾驶动作，直接相关规划与控制
tldr: 扩散模型在机器人策略学习中展现了多模态能力，但应用于自动驾驶面临实时性与动作生成多样性的挑战。本文提出截断扩散策略DiffusionDrive，利用先验多模式锚点截断扩散过程，从锚定高斯分布学习到多模式驾驶动作分布。在nuScenes上实现实时且多样的轨迹生成，显著提升了驾驶动作的质量与速度。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-liao-diffusiondrive-truncated-diffusion-model-for-end-to-end-autonomous-driving-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 876, \"height\": 516, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-liao-diffusiondrive-truncated-diffusion-model-for-end-to-end-autonomous-driving-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1456, \"height\": 1455, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-liao-diffusiondrive-truncated-diffusion-model-for-end-to-end-autonomous-driving-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1488, \"height\": 1119, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-liao-diffusiondrive-truncated-diffusion-model-for-end-to-end-autonomous-driving-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1818, \"height\": 506, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liao-diffusiondrive-truncated-diffusion-model-for-end-to-end-autonomous-driving-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1791, \"height\": 314, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liao-diffusiondrive-truncated-diffusion-model-for-end-to-end-autonomous-driving-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1803, \"height\": 508, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liao-diffusiondrive-truncated-diffusion-model-for-end-to-end-autonomous-driving-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 584, \"height\": 176, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liao-diffusiondrive-truncated-diffusion-model-for-end-to-end-autonomous-driving-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1803, \"height\": 424, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liao-diffusiondrive-truncated-diffusion-model-for-end-to-end-autonomous-driving-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 593, \"height\": 177, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liao-diffusiondrive-truncated-diffusion-model-for-end-to-end-autonomous-driving-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 585, \"height\": 177, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-liao-diffusiondrive-truncated-diffusion-model-for-end-to-end-autonomous-driving-cvpr-2025-paper/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1808, \"height\": 425, \"label\": \"Table\"}]"
motivation: 扩散模型生成驾驶动作时迭代步数多、实时性差，且多模态动作建模困难。
method: 提出截断扩散策略，引入多模式驾驶动作锚点，加速采样并保持多样性。
result: 在nuScenes上实现实时多样规划，超越现有扩散和确定性方法。
conclusion: 截断扩散策略有效平衡了生成多样性与推理速度，适合自动驾驶规划。
---

## Abstract
Recently, the diffusion model has emerged as a powerful generative technique for robotic policy learning, capable of modeling multi-mode action distributions. Leveraging its capability for end-to-end autonomous driving is a promising direction. However, the numerous denoising steps in the robotic diffusion policy and the more dynamic, open-world nature of traffic scenes pose substantial challenges for generating diverse driving actions at a real-time speed. To address these challenges, we propose a novel truncated diffusion policy that incorporates prior multi-mode anchors and truncates the diffusion schedule, enabling the model to learn denoising from anchored Gaussian distribution to the multi-mode driving action distribution. Additionally, we design an efficient cascade diffusion decoder for enhanced interaction with conditional scene context. The proposed model, DiffusionDrive, demonstrates 10x reduction in denoising steps compared to vanilla diffusion policy, delivering superior diversity and quality in just 2 steps. On the planning-oriented NAVSIM dataset, with the aligned ResNet-34 backbone, DiffusionDrive achieves 88.1 PDMS without bells and whistles, setting a new record, while running at a real-time speed of 45 FPS on an NVIDIA 4090. Qualitative results on challenging scenarios further confirm that DiffusionDrive can robustly generate diverse plausible driving actions.

---

## 论文详细总结（自动生成）

# DiffusionDrive：端到端自动驾驶的截断扩散模型——论文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **背景**：扩散模型在机器人策略学习中展现出强大的生成能力，能够建模多模态（multi-mode）动作分布。将扩散模型引入端到端自动驾驶有望生成多样且合理的驾驶轨迹。
- **挑战**：
  - 原始扩散策略需要大量去噪步（如20步），导致推理延迟高，难以满足自动驾驶的实时性要求（FPS低）。
  - 直接应用 vanilla 扩散策略会导致“模式坍缩”（mode collapse）：不同随机噪声采样得到的轨迹高度重叠，多样性不足。
- **目标**：在保持实时性的同时，生成高质量、高多样性的驾驶动作。

## 2. 方法论：核心思想、关键技术细节与算法流程

### 2.1 核心思想：截断扩散策略（Truncated Diffusion Policy）

- **动机**：人类驾驶遵循固定的模式（如车道保持、变道），而非从纯高斯噪声随机采样。因此，利用先验锚点引导扩散过程。
- **训练阶段**：
  - 通过 K-Means 聚类在训练集上生成 \( N_{\text{anchor}} \) 个锚点轨迹 \( \{a_k\} \)。
  - 截断扩散噪声调度：只对锚点添加少量高斯噪声（扩散步数 \( T_{\text{trunc}} \ll T \)），得到“锚定高斯分布”（anchored Gaussian distribution）：
    \[
    \tau_i^k = \sqrt{\bar{\alpha}_i} a_k + \sqrt{1 - \bar{\alpha}_i} \epsilon, \quad \epsilon \sim \mathcal{N}(0,I)
    \]
  - 扩散解码器 \( f_\theta \) 以噪声轨迹和条件信息 \( z \) 为输入，预测分类得分 \( \hat{s}_k \) 和去噪轨迹 \( \hat{\tau}_k \)。
  - 损失函数：轨迹重建损失（L1） + 分类损失（BCE），仅正样本（最接近真实轨迹的锚点）参与重建。
- **推理阶段**：
  - 从锚定高斯分布中采样 \( N_{\text{infer}} \) 个噪声轨迹。
  - 仅用2步去噪（DDIM更新），最终选择得分最高的轨迹作为输出。
  - 推理时 \( N_{\text{infer}} \) 可动态调整（例如20、40），灵活性高。

### 2.2 架构设计：级联扩散解码器（Cascade Diffusion Decoder）

- 输入：采样噪声轨迹。
- 流程（每步）：
  1. **可变形空间交叉注意力**：与BEV/PV特征交互（基于轨迹坐标）。
  2. **智能体/地图交叉注意力**：与感知模块输出的查询交互。
  3. **FFN** + **时间步调制**（编码扩散步信息）。
  4. MLP 预测置信度得分和相对于初始噪声轨迹的偏移。
- 级联：堆叠2层相同的解码器，参数共享，用于迭代精化。
- 整体pipeline可集成多种现有感知模块（如Transfuser的BEV特征）。

## 3. 实验设计

### 3.1 数据集与Benchmark

- **NAVSIM**（主要数据集）：
  - 基于nuPlan，提供闭环仿真与规划指标。
  - 指标：PDMS（由NC、DAC、TTC、Comf、EP加权组合），关注非反应性仿真。
- **nuScenes**（辅助验证）：
  - 开放环评估，指标为L2误差和碰撞率。

### 3.2 对比方法

- NAVSIM：UniAD、PARA-Drive、LTF、Transfuser、DRAMA、VADv2、Hydra-MDP及其变体。
- nuScenes：ST-P3、UniAD、OccNet、VAD、SparseDrive。

## 4. 资源与算力

- **硬件**：8块 NVIDIA 4090 GPU。
- **训练配置**：
  - 优化器：AdamW，学习率 \( 6 \times 10^{-4} \)，总batch size = 512。
  - 训练轮数：100 epochs（从零开始训练）。
- **推理速度**：在单块NVIDIA 4090上达到 **45 FPS**（去噪步仅2步）。
- **未明确信息**：具体训练耗时（小时数）未在文中给出。

## 5. 实验数量与充分性

### 5.1 实验组数

- 主表（NAVSIM）：7种方法对比，1张表。
- 路线消融（Roadmap，表2）：从Transfuser→Transfuser DP→Transfuser TD→DiffusionDrive，逐步验证贡献。
- 设计选择消融（表3）：6组（UNet vs. 解码器、空间交叉注意、智能体/地图交叉注意、级联等）。
- 去噪步数消融（表4）：1、2、3步对比。
- 级联阶段数消融（表5）：1、2、4阶段。
- 采样噪声数消融（表6）：10、20、40。
- nuScenes对比（表7）：6种方法对比。

### 5.2 充分性与公平性

- **充分**：覆盖了主要设计变量（去噪步数、解码器结构、采样数量、级联深度），验证了每个组件的贡献。
- **客观公平**：所有对比使用相同骨干网络（ResNet-34/50），指标计算方式一致，无额外后处理（除Hydra-MDP-W-EP外，但已单独标注）。
- **定性实验**：给出了两个挑战性场景的可视化，展示多模态轨迹的合理性。

## 6. 主要结论与发现

1. **性能领先**：在NAVSIM上以ResNet-34骨干达到**88.1 PDMS**，超越所有先前方法（包括Hydra-MDP-W-EP的86.5），且仅需20个锚点（对比VADv2的8192个）。
2. **实时性**：推理速度45 FPS，满足自动驾驶实时需求；相比vanilla扩散策略（7 FPS）提速6倍以上。
3. **多样性**：生成轨迹的mode diversity得分高达74%（Transfuser DP仅11%），且top-10轨迹包含合理变道等行为。
4. **泛化性**：在nuScenes上以ResNet-50骨干实现最低L2误差（0.57m）和碰撞率（0.08%），优于SparseDrive和VAD。

## 7. 优点

- **方法创新**：
  - 首次将扩散模型成功应用于端到端自动驾驶，并提出截断扩散策略，巧妙融合锚点先验与扩散生成能力。
  - 设计级联扩散解码器，高效交互感知特征，参数共享实现轻量化。
- **效率突出**：仅2步去噪即可达到甚至超越20步的vanilla扩散策略，同时保持高多样性。
- **灵活性**：推理时可动态调整采样数，适应不同资源约束。
- **实验扎实**：在两大数据集、多种指标、多组消融下验证，结论可信。

## 8. 不足与局限

- **锚点依赖性**：锚点通过K-Means聚类得到，聚类数量（20）及质量对性能有影响，但未探讨更优的锚点选择策略。
- **感知模块受限**：实验基于Transfuser的感知（BEV rasterization + 前视相机），未与更先进的感知（如UniAD的向量化表示、SparseDrive的稀疏表示）结合，可能限制了上限。
- **场景覆盖**：NAVSIM侧重挑战性场景（动态意图变化），但nuScenes场景较为简单；在极端长尾场景（如无标线路口、非常规行为）的泛化能力未验证。
- **训练成本**：未报告具体训练时间，但100 epoch在8×4090上可能需数天，对于快速迭代不够高效。
- **模式坍缩风险**：虽然多样性提升显著，但在某些决策点（如同时存在多个合理动作）时，top-1轨迹的选择可能并非最优，定性显示仍有时发生与GT slight偏差。

（完）
