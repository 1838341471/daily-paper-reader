---
title: "Enduring, Efficient and Robust Trajectory Prediction Attack in Autonomous Driving via Optimization-Driven Multi-Frame Perturbation Framework"
title_zh: 基于优化驱动多帧扰动框架的自动驾驶轨迹预测持久、高效且鲁棒的攻击
authors: "Yu, Yi, Han, Weizhen, Wu, Libing, Liu, Bingyi, Wang, Enshu, Zhang, Zhuangzhuang"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Yu_Enduring_Efficient_and_Robust_Trajectory_Prediction_Attack_in_Autonomous_Driving_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 9.0
evidence: 直接研究自动驾驶轨迹预测的对抗攻击问题
tldr: 自动驾驶轨迹预测的脆弱性研究多采用单点攻击，易被过滤且环境适应性差。本文提出一种基于优化的多帧对抗攻击框架，通过LiDAR诱导的对抗位置搜索，实现持久、高效且鲁棒的攻击。实验表明该方法在多种防御下仍保持高攻击成功率，揭示了轨迹预测系统的安全隐患。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yu-enduring-efficient-and-robust-trajectory-prediction-attack-in-autonomous-driving-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 806, \"height\": 557, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yu-enduring-efficient-and-robust-trajectory-prediction-attack-in-autonomous-driving-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1464, \"height\": 791, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yu-enduring-efficient-and-robust-trajectory-prediction-attack-in-autonomous-driving-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1542, \"height\": 388, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yu-enduring-efficient-and-robust-trajectory-prediction-attack-in-autonomous-driving-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1777, \"height\": 887, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yu-enduring-efficient-and-robust-trajectory-prediction-attack-in-autonomous-driving-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 663, \"height\": 448, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yu-enduring-efficient-and-robust-trajectory-prediction-attack-in-autonomous-driving-cvpr-2025-paper/fig-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 614, \"height\": 435, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yu-enduring-efficient-and-robust-trajectory-prediction-attack-in-autonomous-driving-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 868, \"height\": 648, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yu-enduring-efficient-and-robust-trajectory-prediction-attack-in-autonomous-driving-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 594, \"height\": 262, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yu-enduring-efficient-and-robust-trajectory-prediction-attack-in-autonomous-driving-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 825, \"height\": 476, \"label\": \"Table\"}]"
motivation: 现有轨迹预测攻击方法多基于单点攻击，无法应对真实环境中的过滤和不确定性。
method: 提出优化驱动的多帧对抗位置搜索框架，实现持久且鲁棒的LiDAR诱导攻击。
result: 在多个数据集和防御方法下，该攻击方法保持高成功率，优于单点攻击。
conclusion: 该工作暴露了自动驾驶轨迹预测系统在面对多帧对抗时的脆弱性。
---

## Abstract
Trajectory prediction plays a crucial role in autonomous driving systems, and exploring its vulnerability has garnered widespread attention. However, existing trajectory prediction attack methods often rely on single-point attacks to make efficient perturbations. This limits their applications in real-world scenarios due to the transient nature of single-point attacks, their susceptibility to filtration, and the uncertainty regarding the deployment environment. To address these challenges, this paper proposes a novel LiDAR-induced attack framework to impose multi-frame attacks by optimization-driven adversarial location search, achieving endurance, efficiency, and robustness. This framework strategically places objects near the adversarial vehicle to implement an attack and introduces three key innovations. First, successive state perturbations are generated using a multi-frame single-point attack strategy, effectively misleading trajectory predictions over extended time horizons. Second, we efficiently optimize adversarial objects' locations through three specialized loss functions to achieve desired perturbations. Lastly, we improve robustness by treating the adversarial object as a point without size constraints during the location search phase and reduce dependence on both the specific attack point and the adversarial object's properties. Extensive experiments confirm the superior performance and robustness of our framework.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义

- **研究动机**：轨迹预测是自动驾驶系统中的关键模块，但现有针对轨迹预测的对抗攻击方法多采用单点攻击（如 SinglePoint Attack），仅对当前帧的历史轨迹状态施加扰动。这类攻击在真实世界中面临三个挑战：① 单点攻击持续时间短，易被模型过滤；② 搜索最优对抗位置（放置物理物体）的计算空间巨大，现有方法扩展性差；③ 攻击成功高度依赖攻击点精确对齐和物体属性（大小、朝向），鲁棒性不足。
- **整体意义**：本文揭示了自动驾驶轨迹预测系统在面对多帧、持久化物理攻击时的脆弱性，提出了同时实现持久性、高效性和鲁棒性的攻击框架，对自动驾驶安全研究具有重要警示作用。

## 2. 方法论

- **核心思想**：提出“优化驱动的多帧扰动框架”（OMP-Attack），通过两阶段流程实现间接轨迹预测攻击：第一阶段生成多帧目标状态扰动；第二阶段通过优化算法找到能产生这些扰动的对抗物体位置。
- **关键技术细节**：
  - **持久多帧攻击（Enduring Multi-frame Attack）**：
    - 不是对单一轨迹施加多点扰动，而是对连续多个历史轨迹逐帧施加单点攻击。从当前帧开始，依次向前一帧回退，得到 n 帧连续的扰动序列。
    - 利用 PGD（投影梯度下降）迭代优化每一帧的扰动，目标是最小化预测轨迹与原始规划轨迹的平均轨迹距离（ATD）。
  - **高效位置优化（Efficient Location Optimization）**：
    - 设计三个损失函数：位置损失（Lpose，欧几里得距离）、朝向损失（Lheading，余弦相似度）和形状损失（Lshape，动态时间规整距离），综合衡量检测到的状态扰动与目标状态扰动的相似度。
    - 采用粒子群优化（PSO）算法搜索最优的 M 个对抗位置，平衡搜索性能与效率。
  - **鲁棒攻击策略（Robust Attack Strategy）**：
    - “精确攻击，模糊优化”：攻击阶段精确模拟物体大小、朝向等属性以生成强有效扰动；优化阶段仅将物体视为中心点，忽略尺寸和朝向，降低对攻击点和物体属性的依赖。
    - 实际部署时，只要物体至少有一个点覆盖中心点即可产生主要扰动，其他点提供辅助扰动，从而扩大攻击区域，增强鲁棒性。

- **公式/算法流程**（文字描述）：
  1. 初始化：随机生成 Q 组对抗位置，通过感知模块获取状态扰动分布，采样得到 n 帧初始扰动。
  2. 对每一帧历史轨迹，加入初始扰动后输入预测模型，使用 PGD 迭代更新扰动，得到该帧的目标状态扰动。
  3. 将所有帧的目标扰动拼接成多帧目标状态扰动集合。
  4. 初始化 PSO 粒子（每组代表 M 个物体的3D坐标），循环迭代：在当前位置放置物体，模拟点云、检测、跟踪得到检测到的状态扰动，计算三个损失函数加权和，更新粒子位置直至收敛。

## 3. 实验设计

- **数据集**：nuScenes 数据集（包含感知和预测任务），手动选取 50 个符合攻击场景的驾驶场景（具体筛选标准见原文附录）。
- **基准方法**：
  - SP-Attack（SinglePoint Attack，唯一现有的间接攻击方法）
  - Brute-Force 搜索（随机生成位置并选取最优）
  - 干净场景（无攻击）
  - 消融变体：SP-Attack + PSO、OMP-Attack 无 PSO（使用 SP-Attack 的手动匹配方法）
- **对比方法**：白盒攻击和黑盒迁移攻击（目标模型为 Agentformer）。
- **评估指标**：
  - 平均轨迹距离（ATD，越低越好）
  - 平均规划响应误差（PRE，越高越好）
  - 碰撞率（CR，越高越好）

## 4. 资源与算力

- 论文中**未明确说明**所使用的 GPU 型号、数量或训练时长。仅在实现细节中提及攻击阶段查询次数 1000、PSO 粒子数 10、最大迭代 100，但未给出具体硬件配置或运行时间。因此无法定量评估算力需求。

## 5. 实验数量与充分性

- **实验组数**：论文从多个角度进行了实验，包括：
  - 攻击有效性对比（表1，对比 SP-Attack、Brute-Force、消融变体）
  - 粒子数量影响（5/10/15/20，表1）
  - 持久性实验（前4个时间步的ATD、PRE、CR，图3，可视化图4）
  - 鲁棒性实验（物体朝向0°/45°/90°/135°，表2；物体直径0.1-0.5m，图5；攻击点偏差0-1m，图6）
  - 黑盒迁移性实验（表3，白盒/黑盒对比）
- **充分性评价**：
  - 实验覆盖了攻击效果、耐久性、鲁棒性、迁移性等多个维度。
  - 与最新 SOTA 方法（SP-Attack）进行了公平对比（使用相同的 AD 模型和场景设置）。
  - 进行了充分的消融实验（PSO 有无、粒子数量、物体属性变化、偏差距离等）。
  - 实验设计较为客观，统计结果清晰。但未展示在不同驾驶场景（如城市、高速）下的细分结果，也未与其他非间接攻击方法（如有直接攻击）对比。

## 6. 主要结论与发现

- OMP-Attack 在攻击有效性上远超 SP-Attack：ATD 降低 47%，PRE 提升 100%，CR 提升 52%。
- 持久性：OMP-Attack 在多帧上保持稳定攻击性能，ATD 最大增幅小于 1.6 米，而 SP-Attack 增加 4 米。在较早帧上甚至优于当前帧。
- 鲁棒性：物体朝向变化（0°-135°）对 ATD 影响很小（波动约 0.8-1.2 米），物体直径变化（0.1-0.5m）下 ATD 波动小于 0.5 米，PRE 波动小于 1.1 米。攻击点偏差 0-1 米时，OMP-Attack 的 ATD 最大衰减不超过 25%，而 SP-Attack 在 0.1 米偏差下 ATD 即增加 3 米失效。
- 黑盒迁移性：OMP-Attack 的白盒位置在 Agentformer 黑盒模型上仍能显著降低 ATD（降低 3.386 米），优于 SP-Attack。
- 结论：所提框架实现了持久、高效、鲁棒的轨迹预测攻击，暴露了自动驾驶系统在物理世界中的安全隐患。

## 7. 优点

- **创新性**：首次提出多帧持久化的间接攻击方法，克服了单点攻击时间短的局限。
- **高效性**：采用 PSO 优化结合三个专门设计的损失函数，在大搜索空间中快速找到有效位置。
- **鲁棒性设计**：“精确攻击，模糊优化”策略巧妙解耦了攻击生成和位置搜索，大幅降低对物体属性和攻击点精度的依赖，提高了实际部署可能性。
- **实验全面**：涵盖了与 SOTA 的对比、消融、持久性、鲁棒性（多因素）和迁移性，验证充分。
- **实用性**：使用物理可实现的圆形纸板作为对抗物体，攻击成本低且可复现；黑盒迁移性表明方法具有实际威胁性。

## 8. 不足与局限

- **场景限定**：仅研究了单一场景（受害者 AV 直行，对抗车辆停靠路边），未考虑多车、交叉路口、变道等更复杂的交通场景。
- **物体类型单一**：仅使用圆形纸板作为对抗物体，未探讨其他形状、材质或颜色物体的效果。
- **模型依赖**：攻击依赖于对预测模型的白盒访问，虽然展示了黑盒迁移性，但迁移后性能有所下降（CR 从 64% 降至 26%），且仅测试了 Agentformer 一个目标模型，泛化性证据有限。
- **未考虑防御机制**：实验未评估常见的对抗防御（如输入滤波、鲁棒训练、异常检测）对 OMP-Attack 的削弱效果，实际防御环境下攻击成功率可能降低。
- **计算资源未报告**：未说明 GPU 型号、训练时间等，不利于他人复现和评估实际攻击成本。
- **偏差风险**：手动选取 50 个符合攻击场景的场景，可能引入选择偏差；实验结果未给出方差或置信区间，可复现性需验证。
- **物理可实现验证缺失**：虽然方法基于 LiDAR 点云模拟，但未进行真实物理世界实验验证（如实际放置纸板并用真实 LiDAR 检测），仅停留在模拟层面。

（完）
