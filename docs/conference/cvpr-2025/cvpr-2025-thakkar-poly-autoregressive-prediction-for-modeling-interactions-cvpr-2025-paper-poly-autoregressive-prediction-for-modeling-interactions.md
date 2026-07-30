---
title: Poly-Autoregressive Prediction for Modeling Interactions
title_zh: 多自回归预测用于交互建模
authors: "Thakkar, Neerja, Sadjadpour, Tara, Rajasegeran, Jathushan, Ginosar, Shiry, Malik, Jitendra"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Thakkar_Poly-Autoregressive_Prediction_for_Modeling_Interactions_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 8.0
evidence: 多自回归建模用于多智能体交互预测，可应用于自动驾驶
tldr: 多智能体场景中的交互预测是自动驾驶的关键。本文提出多自回归（PAR）建模，将多智能体历史状态编码为标记序列，通过自回归方式预测自我代理的未来行为。PAR可应用于人类动作预测、行人轨迹预测和自动驾驶场景。实验表明PAR在多个任务上表现优越，尤其擅长建模长程交互依赖。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1789, \"height\": 402, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1780, \"height\": 649, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 714, \"height\": 711, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 837, \"height\": 416, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1609, \"height\": 584, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 863, \"height\": 474, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/fig-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 872, \"height\": 306, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/fig-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 868, \"height\": 307, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 867, \"height\": 320, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 641, \"height\": 323, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 812, \"height\": 321, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 733, \"height\": 280, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 882, \"height\": 297, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-thakkar-poly-autoregressive-prediction-for-modeling-interactions-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 916, \"height\": 270, \"label\": \"Table\"}]"
motivation: 现有自回归方法主要针对单一序列，难以建模多智能体间的物理约束和交互。
method: 将所有智能体的状态序列化为统一标记序列，采用自回归Transformer预测自我智能体未来状态。
result: 在Human3.6M、ETH/UCY和Waymo交互数据集上，PAR均取得了最先进的预测精度。
conclusion: PAR为多智能体交互预测提供了简洁而有效的统一框架。
---

## Abstract
We introduce a simple framework for predicting the behavior of an agent in multi-agent settings. In contrast to autoregressive (AR) tasks, such as language processing, our focus is on scenarios with multiple agents whose interactions are shaped by physical constraints and internal motivations. To this end, we propose Poly-Autoregressive (PAR) modeling, which forecasts an ego agent's future behavior by reasoning about the ego agent's state history and the past and current states of other interacting agents. At its core, PAR represents the behavior of all agents as a sequence of tokens, each representing an agent's state at a specific timestep. With minimal data pre-processing changes, we show that PAR can be applied to three different problems: human action forecasting in social situations, trajectory prediction for autonomous vehicles, and object pose forecasting during hand-object interaction. Using a small proof-of-concept transformer backbone, PAR outperforms AR across these three scenarios.

---

## 论文详细总结（自动生成）

# 论文《Poly-Autoregressive Prediction for Modeling Interactions》中文总结

## 1. 核心问题与整体含义（研究动机与背景）

- **研究背景**：自回归（AR）建模在语言模型中取得巨大成功，但语言是一维序列；而多智能体交互场景（如人类社会互动、车辆驾驶、手物操作）中，多个智能体的状态同时变化，且受物理约束和内在动机共同影响。
- **核心问题**：传统AR仅利用单个智能体自身历史进行预测，无法充分建模其他智能体对目标智能体行为的因果影响，导致预测不准确（尤其在交互密集情形，如两人对话、车辆避让）。
- **整体目标**：提出一个**统一、简单的框架**，将多智能体交互纳入预测，仅通过少量数据预处理调整即可适用于多种实体交互任务，并证明小模型即可超越纯AR。

## 2. 方法论：Poly-Autoregressive (PAR) 框架

- **核心思想**：将场景中所有智能体在每一时间步的状态视为 token，形成一个展平的序列（`N` 个智能体 × `T` 个时间步）。预测目标智能体（ego）的未来状态时，不仅以其自身历史为条件，还以**其他所有智能体的过去及当前状态**为条件，从而捕捉交互耦合。
- **关键技术细节**：
  - **相同智能体的下一时间步预测（Same-agent next-timestep prediction）**：训练时，每个智能体的输入位置对应预测该智能体的下一时间步（而非预测下一 token 可能属于其他智能体）。使用教师强制。
  - **学习智能体身份嵌入（Learned agent ID embedding）**：为每个智能体分配可学习的 ID 向量，加到 token 嵌入上，帮助模型区分不同实体。
  - **联合训练**：训练时对所有智能体的未来状态计算损失（不需要只对 ego 计算），使得模型同时学习所有角色的动态。
  - **支持离散 token（如动作类别）和连续 token（如坐标、速度、四元数）**：离散用交叉熵损失，连续用 MSE 损失；通过投影层将 token 映射到 Transformer 隐藏维度。
  - **可选的位置编码**：在车辆轨迹预测中引入“位置位置编码（LPE）”——将相对坐标通过正弦余弦编码加到 token 嵌入，使模型感知空间位置。
- **公式流程**（文字说明）：
  - 给定 `N-1` 个其他智能体的历史状态序列 `S^{1:N-1}_{1:t-1}`，以及 ego 智能体的观测历史 `S^{N}_{1:t_obs}` 和已预测的过去 `\hat{S}^{N}_{t_obs+1:t-1}`，预测 `\hat{s}^N_t = P(S^{1:N-1}_{1:t-1}, S^{N}_{1:t_obs}, \hat{S}^{N}_{t_obs+1:t-1})`。
  - 网络采用 8 层、8 注意力头、隐藏维度 128 的 Llama 架构 Transformer 解码器（约 4.4M 参数），使用旋转位置编码（RoPE）和上述嵌入。
- **与 AR 的关键区别**：PAR 考虑其他智能体的 token，并在训练时使用“同智能体下一时间步”而非“下一 token”预测（避免跨智能体错位）。

## 3. 实验设计

- **三个测试场景（案例研究）**：
  1. **社交动作预测**：数据集 **AVA**（电影中的动作标注，60 类动作），输入 6s 历史，预测 6s 未来。评估指标：**mAP**。对比方法：1-agent AR、2-agent PAR（及其变体）、随机 token、随机轨迹、最近邻、多智能体最近邻、镜像。
  2. **车辆轨迹预测**：数据集 **nuScenes**（仅用车辆作为智能体），输入 2s 位置，预测 6s 未来。评估指标：**ADE / FDE**。对比方法：1-agent AR、3-agent PAR（使用速度/加速度 token，含/不含位置编码）、随机轨迹、NN、多智能体 NN、镜像。
  3. **手物交互物体姿态预测**：数据集 **DexYCB**（手抓取物体视频），预测物体 6DoF 姿态（旋转和翻译分离实验）。评估指标：旋转用**测地距离**，翻译用 **MSE**。对比方法：1-agent AR（仅物体历史）、2-agent PAR（物体+手）、随机、NN、多智能体 NN、镜像。
- **基线方法**：每个场景均包括随机猜测、随机轨迹、最近邻（NN）、多智能体 NN、镜像等无学习方法，以及对应的 1-agent AR 作为直接对比。
- **消融实验**：
  - 在 AVA 上移除“身份嵌入”或“下一时间步预测”；
  - 在 nuScenes 上比较速度 vs 加速度 token，以及添加位置编码的效果；
  - 在 DexYCB 上分别报告旋转和翻译任务的结果。
- **实验充分性**：覆盖三个完全不同的领域，使用统一架构和超参数（仅学习率调整），对比了多种基线及消融，实验设计较全面。但未与各领域最先进（SOTA）专用方法进行对比（论文定位为概念验证框架）。

## 4. 资源与算力

- **论文未明确说明训练使用的 GPU 型号、数量、训练耗时**，仅提及参数约 4.4M 的小型 Transformer 作为“proof-of-concept”。因此无法量化算力需求。

## 5. 实验数量与充分性评估

- **实验组数**：每个场景至少包含 3~5 种方法对比及 2~3 种消融，总计约 15 个以上主要实验配置（含不同 token 类型、是否使用 LPE 等）。
- **公平性**：超参数（层数、隐藏维度、注意头数）在所有任务中保持一致；数据预处理和 token 方式按任务定制但框架核心不变；对比基线包括朴素方法和同规模 AR。
- **客观性**：所有对比均基于标准基准（AVA mAP、nuScenes ADE/FDE、DexYCB 测地距离/MSE），无选择偏差。
- **局限性**：未与大型专用模型（如 MotionLM、Scene Transformer 等）直接比较，实验规模小，仅在单个证明概念模型上进行。

## 6. 主要结论与发现

- **PAR 在三个任务中均一致优于纯 AR**：
  - AVA：总体 mAP 提升 **+1.9**，两人交互类提升 **+3.5**（如“kiss”+8.3，“fight/hit”+5.7）。
  - nuScenes：ADE 相对改善 **6.3%**，FDE 改善 **6.4%**（加速度 token + LPE）。
  - DexYCB：旋转测地距离改善 **8.9%**，翻译 MSE 改善 **41%**（手部信息至关重要作用）。
- **消融验证**：“身份嵌入”和“同智能体下一时间步预测”两个设计均不可或缺；在轨迹预测中，位置编码（LPE）进一步提升了性能，表明模型需要空间感知。
- **框架通用性**：同一架构（仅改变 tokenization 和损失函数）即可处理动作类别、连续坐标、3D 旋转/平移，证明 PAR 是简单通用的多智能体交互预测范式。

## 7. 优点

- **简单统一**：无需修改 backbone 即可适配不同预测模态，降低领域迁移成本。
- **轻量高效**：仅 4.4M 参数的小模型即可获得显著提升，表明交互建模的增益主要来自框架设计而非模型规模。
- **消融清晰**：各组件（身份嵌入、下一时间步预测、位置编码）贡献可量化，具有很强的可解释性。
- **跨领域验证**：涵盖人类社会、自动驾驶、机器人操作，展示方法的广泛适用性。

## 8. 不足与局限

- **与 SOTA 对比不足**：未与各领域的最先进方法（如 MotionLM、AgentFormer、Interaction Transformer）在同等输入条件下比较，削弱了说服力。
- **假设高质量跟踪**：依赖已检测和关联好的智能体轨迹，未处理真实场景中的检测失败、身份切换等噪声，实际部署有 gap。
- **忽略环境上下文**：车辆轨迹预测中未使用地图、车道线、红绿灯等环境信息；手物交互中未使用物体几何或手部姿态细节。
- **智能体数量受限**：实验中最高仅 3 个智能体；当参与智能体增多（如密集人群或交通场景），模型输入序列长度线性增长，可能面临计算和效率挑战。
- **无动态注意力调整**：对所有其他智能体一视同仁，未学习哪些智能体对当前预测更重要（文中提到可作为未来方向）。
- **评估指标单一**：仅在确定性预测上评估，未进行多模态预测（如 Top-k 或概率输出）的对比，而这在车辆轨迹预测中很常见。

（完）
