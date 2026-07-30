---
title: "Scenario Dreamer: Vectorized Latent Diffusion for Generating Driving Simulation Environments"
title_zh: Scenario Dreamer：基于向量化潜在扩散的驾驶仿真环境生成
authors: "Rowe, Luke, Girgis, Roger, Gosselin, Anthony, Paull, Liam, Pal, Christopher, Heide, Felix"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Rowe_Scenario_Dreamer_Vectorized_Latent_Diffusion_for_Generating_Driving_Simulation_Environments_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 7.0
evidence: 生成驾驶仿真环境用于自动驾驶车辆规划，支持轨迹规划与控制
tldr: 现有驾驶仿真环境生成方法依赖栅格化表示和规则行为，缺乏多样性和真实性。本文提出Scenario Dreamer，采用向量化潜在扩散模型直接生成车道图和智能体边界框，并配合闭环行为模块。在多个规划基准上验证了仿真环境的有效性，提升了规划策略的泛化能力。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-rowe-scenario-dreamer-vectorized-latent-diffusion-for-generating-driving-simulation-environments-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1643, \"height\": 703, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-rowe-scenario-dreamer-vectorized-latent-diffusion-for-generating-driving-simulation-environments-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1810, \"height\": 727, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-rowe-scenario-dreamer-vectorized-latent-diffusion-for-generating-driving-simulation-environments-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 786, \"height\": 539, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-rowe-scenario-dreamer-vectorized-latent-diffusion-for-generating-driving-simulation-environments-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1801, \"height\": 360, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-rowe-scenario-dreamer-vectorized-latent-diffusion-for-generating-driving-simulation-environments-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1268, \"height\": 363, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-rowe-scenario-dreamer-vectorized-latent-diffusion-for-generating-driving-simulation-environments-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1796, \"height\": 286, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-rowe-scenario-dreamer-vectorized-latent-diffusion-for-generating-driving-simulation-environments-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 865, \"height\": 201, \"label\": \"Table\"}]"
motivation: 现有栅格化生成方法计算效率低，规则行为缺乏多样性。
method: 提出向量化潜在扩散模型生成初始场景，并学习闭环智能体行为。
result: 生成的仿真环境在多样性、真实性和规划性能上均优于现有方法。
conclusion: 向量化扩散框架为自动驾驶规划提供了更高效逼真的仿真数据源。
---

## Abstract
We introduce Scenario Dreamer, a fully data-driven generative simulator for autonomous vehicle planning that generates both the initial traffic scene--comprising a lane graph and agent bounding boxes--and closed-loop agent behaviours. Existing methods for generating driving simulation environments encode the initial traffic scene as a rasterized image and, as such, require parameter-heavy networks that perform unnecessary computation due to many empty pixels in the rasterized scene. Moreover, we find that existing methods that employ rule-based agent behaviours lack diversity and realism. Scenario Dreamer instead employs a novel vectorized latent diffusion model for initial scene generation that directly operates on the vectorized scene elements and an autoregressive Transformer for data-driven agent behaviour simulation. Scenario Dreamer additionally supports scene extrapolation via diffusion inpainting, enabling the generation of unbounded simulation environments. Extensive experiments show that Scenario Dreamer outperforms existing generative simulators in realism and efficiency: the vectorized scene-generation base model achieves superior generation quality with around 2x fewer parameters, 6x lower generation latency, and 10x fewer GPU training hours compared to the strongest baseline. We confirm its practical utility by showing that reinforcement learning planning agents are more challenged in Scenario Dreamer environments than traditional non-generative simulation environments, especially on long and adversarial driving environments.

---

## 论文详细总结（自动生成）

# Scenario Dreamer 中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：现有的自动驾驶仿真环境生成方法存在两大瓶颈：一是将初始交通场景编码为栅格化（rasterized）图像，导致参数冗余和计算浪费（大量空像素）；二是使用基于规则的智能体行为模型，缺乏多样性和真实性。
- **整体含义**：本文提出一种完全数据驱动的生成式仿真器——Scenario Dreamer，能够同时生成初始交通场景（包含车道图与智能体边界框）以及闭环智能体行为，旨在为自动驾驶规划提供无限量、多样化且逼真的模拟环境，克服现有仿真器依赖有限预录制驾驶日志的局限。

## 2. 论文提出的方法论

### 核心思想
- 将生成式仿真分解为**初始场景生成**与**行为模拟**两个独立模块，分别使用向量化潜在扩散模型和自回归Transformer，实现高效、逼真的环境生成与交互。

### 关键技术细节

#### 2.1 初始场景生成——向量化潜在扩散模型（Vectorized Latent Diffusion Model）
- **两阶段训练**：
  1. **自编码器（Autoencoder）**：使用Transformer编码器 \(E_\phi\) 和解码器 \(D_\gamma\)，直接对向量化场景元素（车道中心线、智能体边界框）进行潜在编码。编码器采用**分解注意力（factorized attention）** 块，分别建模车道-车道、车道-物体、物体-物体交互，并显式学习车道连通性 \(A\)（4种邻接类型：后继、前驱、左、右）。
  2. **潜在扩散模型**：训练噪声预测网络 \(\epsilon_\theta\) 从潜在分布 \(p(H)\) 中采样，同样使用分解注意力Transformer，并引入**正弦位置编码**解决集合结构数据的排列歧义问题，通过递归排序（按x、y、max x、max y）为潜在标记赋予位置信息。
- **损失函数**：标准DDPM目标，\(\mathcal{L}_{dm} = \mathbb{E}\left[\|\epsilon_t - \epsilon_\theta(H_t, t)\|^2\right]\)。
- **支持多种生成模式**：
  - **初始场景生成**：采样 \((N_o, N_l)\)，从扩散模型生成潜在表示并解码。
  - **车道条件物体生成**：固定地图 \(M\)，仅生成物体。
  - **场景修复（Inpainting）**：通过扩散修复实现场景外推，生成无界仿真环境。训练时专门对“分区场景”进行条件解码，并训练分类器 \(f_\phi\) 预测新区域的车道数量。

#### 2.2 行为模拟——自回归Transformer（CtRL-Sim）
- 基于**返回条件自回归Transformer**，建模多智能体联合分布 \(p_\theta(A_t, G_t | S_t) = \pi_\theta(A_t | S_t, G_t) p_\theta(G_t | S_t)\)，其中 \(G_t\) 为未来折扣回报（奖励函数惩罚与自车碰撞）。
- 支持**指数倾斜**：在推理时对回报模型进行正/负倾斜，生成友好或对抗性驾驶行为。
- 使用k-disks token化方案支持多类型智能体（车辆、行人、自行车）。

#### 2.3 仿真框架
- 结合GPUDrive，定义自车路线，使用CtRL-Sim模拟其他智能体，支持任意长仿真。通过训练时加入二进制指示符（场景是否可通过Nocturne过滤），推理时使用分类器引导采样有效场景。

## 3. 实验设计

### 数据集
- **Waymo Open Motion Dataset**：包含车辆、行人、自行车；车道中心线及连通性。
- **nuPlan dataset**：包含车辆、行人、静态物体；车道中心线、连通性及交通灯状态。
- 两者均以自车为中心，使用64m × 64m FOV，车道中心线经压缩处理。

### 评估指标
- **车道图生成**：Urban Planning指标（连通性、密度、可达性、便利性）、Frechet距离（FD）、最长路线长度、端点距离。
- **初始智能体生成**：Jensen-Shannon散度（JSD）指标（最近距离、横向偏差、角度偏差、长度、宽度、速度）、碰撞率。
- **行为仿真**：额外评估指标详见附录。

### 对比方法
- **nuPlan**：SLEDGE（DiT-L 和 DiT-XL），基于栅格化的潜在扩散模型。
- **Waymo**：DriveSceneGen（由于未收敛，使用带特权版本的Ground Truth栅格化）。
- **行为模型**：规则型IDM、数据驱动Trajeglish（定量/定性结果见附录）。

## 4. 资源与算力

- **Scenario Dreamer (B)**：377M参数，在4块A100 GPU上训练24小时（共96 GPUh）。
- **Scenario Dreamer (L)**：679M参数，在8块A100 GPU上训练32小时（共256 GPUh）。
- **SLEDGE DiT-XL**：769M参数，960 GPUh（作者复现时发现略逊于原文报告）。
- **DriveSceneGen**：未明确报告算力。

## 5. 实验数量与充分性

- **主要实验**：在nuPlan和Waymo两个数据集上进行车道图与智能体生成对比（表1、表2），含完整指标。
- **消融实验**（表3）：在nuPlan上验证三个设计选择：
  - 去除学习车道连通性（使用启发式拓扑）
  - 去除车道排序（排列歧义）
  - 替代为非分解注意力（Non-factorized）
- **规划器评估**（表4）：使用PPO规划器在GPUDrive中训练，在Waymo测试场景、Scenario Dreamer短路线（55m）和长路线（100m）上评估，并测试负倾斜（对抗）行为。
- **充分性**：实验覆盖两个主流数据集、多个对比方法、完整消融、与下游规划器结合，充分且公平。但未提供行为模型独立对比的完整表格（仅附录提及），且DriveSceneGen为特权版本，对比不完全对等。

## 6. 论文的主要结论与发现

- **向量化处理显著优于栅格化**：Scenario Dreamer在车道图和智能体生成上全面超越SLEDGE和DriveSceneGen，且参数更少、延迟更低、训练GPU时更少（2×参数、6×延迟、10×GPU时）。
- **数据驱动行为模拟提升真实性**：结合CtRL-Sim（尤其是负倾斜对抗行为）能生成更具挑战性的场景，显著降低RL规划器成功率（尤其长路线 + 对抗行为）。
- **修复性外推有效**：通过扩散修复实现无界仿真，在密集复杂路口仍能保持空间一致性。
- **实用价值**：Scenario Dreamer可生成无限数量、交互式、安全关键的环境，推动自动驾驶规划研究。

## 7. 优点

- **方法创新**：首次将向量化潜在扩散模型用于驾驶仿真环境生成，直接操作向量化场景元素，避免栅格化冗余。
- **高效性**：因子化注意力设计减少计算量，潜在空间维度可定制（车道维度大于物体维度），实现更快推理和更少参数。
- **灵活性**：支持场景修复、车道条件生成、密度控制、对抗行为控制（指数倾斜），提供高度可控性。
- **下游集成验证**：与GPUDrive和PPO规划器结合，展示了实际挑战价值。
- **实验系统全面**：覆盖多个数据集、对比方法、消融、规划器评估，充分证明优势。

## 8. 不足与局限

- **交通灯信号**：生成的交通灯逻辑偶有无效，未完全解决交通规则一致性。
- **地图类型局限**：当前仅生成车道中心线，未包含道路边缘、人行横道等其他元素。
- **行为模型与初始场景解耦**：可能忽略两者之间的联合分布依赖（虽有意解耦以降低频率）。未提供行为模型独立对比的完整表格。
- **DriveSceneGen对比公平性**：由于DriveSceneGen未收敛，使用特权栅格化版本作为上限对比，可能低估其真实性能差距。
- **可扩展性**：虽然支持无界场景，但未评估极长路线（>100m）或极端密集场景下的稳定性与计算开销。
- **隐私与安全**：生成数据可能隐含训练数据偏差，未讨论泛化到未知场景的风险。

（完）
