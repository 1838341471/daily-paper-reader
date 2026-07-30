---
title: Navigation World Models
title_zh: 导航世界模型
authors: "Bar, Amir, Zhou, Gaoyue, Tran, Danny, Darrell, Trevor, LeCun, Yann"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Bar_Navigation_World_Models_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 7.0
evidence: 提出生成式世界模型，通过仿真规划导航轨迹
tldr: 传统导航策略行为固定，难以动态融入约束。本文提出NWM，一个基于条件扩散Transformer的可控视频生成模型，根据历史观察和动作预测未来视觉观察。在熟悉环境中，NWM通过仿真和评估来规划轨迹，并能动态整合约束。实验表明该方法在多种规划任务上有效。该范式可迁移至自动驾驶规划。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1800, \"height\": 1110, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 645, \"height\": 1047, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 876, \"height\": 288, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1812, \"height\": 375, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 848, \"height\": 640, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 1803, \"height\": 393, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 1798, \"height\": 369, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 858, \"height\": 333, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/fig-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 863, \"height\": 302, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 878, \"height\": 388, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 683, \"height\": 108, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 730, \"height\": 233, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 797, \"height\": 185, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-bar-navigation-world-models-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1662, \"height\": 165, \"label\": \"Table\"}]"
motivation: 现有导航策略缺乏动态约束整合能力，且难以适应新环境。
method: 采用条件扩散Transformer（CDiT）训练大规模第一人称视频，生成未来观察并用于轨迹规划。
result: 在多个导航场景中，NWM能有效规划轨迹，并动态满足约束。
conclusion: 生成式世界模型为基于仿真的轨迹规划提供了新范式。
---

## Abstract
Navigation is a fundamental skill of agents with visual-motor capabilities. We introduce a Navigation World Model (NWM), a controllable video generation model that predicts future visual observations based on past observations and navigation actions. To capture complex environment dynamics, NWM employs a Conditional Diffusion Transformer (CDiT), trained on a diverse collection of egocentric videos of both human and robotic agents, and scaled up to 1 billion parameters. In familiar environments, NWM can plan navigation trajectories by simulating them and evaluating whether they achieve the desired goal. Unlike supervised navigation policies with fixed behavior, NWM can dynamically incorporate constraints during planning. Experiments demonstrate its effectiveness in planning trajectories from scratch or by ranking trajectories sampled from an external policy. Furthermore, NWM leverages its learned visual priors to imagine trajectories in unfamiliar environments from a single input image, making it a flexible and powerful tool for next-generation navigation systems.

---

## 论文详细总结（自动生成）

# 论文《Navigation World Models》详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：现有的视觉导航策略（如GNM、NoMaD）是“硬编码”的行为克隆，训练后无法动态融入新约束（例如“禁止左转”），也无法将更多计算资源分配给困难问题。另外，这类模型无法在不熟悉的环境中进行规划或想象。
- **动机**：借鉴人类规划时“想象未来轨迹并考虑约束”的能力，设计一个可泛化、可动态约束的**世界模型**，用于导航。
- **整体含义**：提出**Navigation World Model (NWM)**——一个基于第一人称视频和动作的可控视频生成模型。它能通过模拟未来观察来评估轨迹是否达到目标，从而进行规划或排名，克服了固定策略的局限性。

## 2. 方法论：核心思想、关键技术细节、算法流程
- **核心思想**：学习一个随机映射 \( F_\theta(s_{t+1} | s_t, a_t) \)，根据过去的潜视觉状态 \( s_t \) 和导航动作 \( a_t = (u, \omega) \)（平移+旋转）预测下一时刻的潜状态。使用预训练VAE将图像编码为潜变量，解码回像素。
- **关键创新——Conditional Diffusion Transformer (CDiT)**：
  - 采用扩散模型从噪声中恢复目标状态 \( s_{t+1} \)，条件为上下文帧 \( s_{t-k...t} \)、动作 \( a_t \)、时间偏移 \( k \)、扩散时间步 \( t \)。
  - CDiT块：与标准DiT不同，CDiT只对当前帧做自注意力，通过交叉注意力利用过去帧信息，复杂度 \( O(m n^2 d) \)（线性于帧数 \( m \)），远低于DiT的 \( O(m^2 n^2 d) \)。
  - 条件嵌入：对动作、时间偏移、扩散步长分别提取正弦余弦特征，经MLP映射后相加，通过AdaLN调制归一化和注意力输出。
- **训练目标**：
  - 简单损失 \( L_{\text{simple}} = \mathbb{E}[ \| s_{t+1} - F_\theta(s_{t+1}^{(t)} | s_t, a_t, t) \|^2 ] \)。
  - 同时预测噪声协方差，用变分下界 \( L_{\text{vlb}} \) 监督。
- **规划流程**：
  - 给定当前状态 \( s_0 \) 和目标 \( s^* \)，定义能量函数 \( E = -S(s_T, s^*) + \text{约束惩罚} \)，其中相似度 \( S \) 使用LPIPS或DreamSim。
  - 使用交叉熵方法（CEM）优化动作序列，最小化能量。
  - **排名**：利用外部策略（如NoMaD）采样多条轨迹，NWM模拟并选择能量最低的。

## 3. 实验设计：数据集、场景、基准与对比方法
- **数据集**：
  - **已知环境**（训练与评估）：SCAND（社交导航）、TartanDrive（越野）、RECON（开放世界）、HuRoN（社交交互）。动作由机器人位姿变化计算。
  - **未知环境**（零样本）：Go Stanford（训练时不使用，仅用于测试泛化）。
  - **无标签数据**：Ego4D（仅时间偏移，无动作标签），用于额外训练。
- **评估指标**：
  - 视频预测：LPIPS、DreamSim、PSNR、FID、FVD。
  - 导航规划：绝对轨迹误差（ATE）、相对位姿误差（RPE）。
- **对比方法**：
  - DIAMOND（UNet扩散世界模型）、GNM（通用导航策略）、NoMaD（扩散策略+目标条件）。
- **消融实验**：模型规模（CDiT vs DiT）、目标数量、上下文长度、时间/动作条件对预测性能的影响。

## 4. 资源与算力
- **文中明确**：CDiT-XL（1B参数）在**8台H100机器（每台8GPU，共64块H100）**上训练，总batch size=1024（配合4个目标即4096），学习率8e-5，使用AdamW优化器。未给出具体训练时长（小时数），但提及XL规模需要多机。
- **其他模型**：较小型号在类似配置下训练，但无详细计时。

## 5. 实验数量与充分性
- **实验组数**：至少6组主要实验——
  1. 消融模型（CDiT vs DiT，不同参数量）；
  2. 消融目标数量、上下文长度、条件设置；
  3. 视频预测精度对比（与DIAMOND，随时间变化）；
  4. 视频生成质量（FVD对比DIAMOND）；
  5. 导航规划（独立规划 vs 排名，ATE/RPE对比GNM、NoMaD）；
  6. 约束规划（三种约束条件）；
  7. 未知环境泛化（加Ego4D vs 不加）。
- **充分性评价**：实验设计全面：在**已知环境**（RECON等）评估预测和规划，在**未知环境**（Go Stanford）评估泛化。消融覆盖关键因素。对比方法均是目前SOTA且公开的，公平性较好（使用相同数据/设置）。但未知环境部分仅测试了一个数据集，泛化实验有限。

## 6. 主要结论与发现
- **预测与生成**：NWM在单步和多步视频预测上显著优于DIAMOND（LPIPS/FVD更低）。CDiT在相同FLOPs下比DiT预测更准，且扩展到1B参数时性能持续提升。
- **规划能力**：
  - 独立规划（使用CEM优化的NWM）在RECON上达到**ATE=1.13，RPE=0.35**，优于GNM（1.87/0.73）和NoMaD（1.93/0.52）。
  - 排名NoMaD的轨迹：采样32条时ATE=1.78，RPE=0.48，优于原始NoMaD。
  - 能够成功遵守“先直后转”“先左/右转后直”等约束，仅轻微损失精度。
- **未知环境泛化**：加入Ego4D无标签数据后，在Go Stanford上的预测LPIPS从0.658降至0.652（微小改善），DreamSim和PSNR也提升。
- **局限性**：在OOD环境中易出现模式崩溃（生成图像向训练数据坍缩）；难以模拟动态物体（如行人）；当前只支持3自由度动作，未扩展到6DoF或机器人手臂。

## 7. 优点
- **方法创新**：提出CDiT计算高效且可扩展，适合长视频上下文。
- **通用性**：单一模型跨多个环境和机器人形态，还能利用无标签数据提升泛化。
- **灵活规划**：支持独立规划、外部策略排名、约束动态集成，能力强于固定策略。
- **消融详实**：对模型架构、条件输入、上下文等进行了系统消融。

## 8. 不足与局限
- **未知环境性能有限**：即使加了Ego4D，泛化增益不大（LPIPS仅降0.006），且模型可能生成与训练数据类似的内容（模式崩溃）。
- **动态物体缺失**：框架未建模移动物体（如行人），在社交导航场景效果受限。
- **动作维度限制**：仅3DoF（平移+偏航），未涵盖6DoF（俯仰、滚转）或机器人关节动作。
- **规划依赖扩散采样**：每次规划需多次推理，实时性可能不足；文中未给出运行时间。
- **实验覆盖**：未知环境仅测试Go Stanford一个场景，缺乏更多OOD场景验证。
- **风险评估**：在真实机器人上使用前需彻底验证安全性，文中未讨论失败场景下的保障机制。

（完）
