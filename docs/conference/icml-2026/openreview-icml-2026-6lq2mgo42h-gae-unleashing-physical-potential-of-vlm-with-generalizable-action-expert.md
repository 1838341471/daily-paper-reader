---
title: "GAE: Unleashing Physical Potential of VLM with Generalizable Action Expert"
title_zh: GAE：利用可泛化动作专家释放VLM的物理潜力
authors: "Mingyu Liu, Zheng Huang, Xiaoyi Lin, Muzhi Zhu, Canyu Zhao, Yating Wang, Haoyi Zhu, Hao Chen, Chunhua Shen"
date: 2026-04-30
pdf: "https://openreview.net/pdf/2f3ed7d7bc2a6c31c211fb1222f477e1c60bd2ec.pdf"
tags: ["query:av-pnc"]
score: 4.0
evidence: 通用动作专家将稀疏计划映射到密集动作，可应用于自动驾驶轨迹生成
tldr: 视觉语言模型虽具强推理规划能力，但将预测落实到精确机器人动作仍具挑战。本文提出通用动作专家GAE，通过稀疏几何接口将VLM预测的稀疏3D路点映射为连续动作轨迹，实现任务无关的动作生成。GAE在大规模数据集预训练后能快速适应新任务，减少机器人动作生成成本。实验表明该方法在多种机器人操作任务中有效，其稀疏到密集的映射思想也可为自动驾驶车辆的轨迹规划提供参考。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 视觉语言模型将推理转化为精确机器人动作时面临泛化性差和适应成本高的问题。
method: 提出通用动作专家GAE，将VLM预测的稀疏3D路点结合点云观测映射为连续动作轨迹。
result: 实验显示GAE在多任务中有效降低动作生成成本，提升泛化能力。
conclusion: 稀疏到密集的动作映射思想可为自动驾驶轨迹规划提供参考。
---

## Abstract
Vision-language models demonstrate strong reasoning and planning abilities, yet grounding these predictions into precise robot actions remains a central challenge. Existing Vision-Language-Action methods typically entangle reasoning and action generation, leading to limited generalization and costly adaptation. We propose to learn a \textbf{G}eneralizable \textbf{A}ction \textbf{E}xpert (\textbf{GAE}), a task-agnostic model that converts sparse geometric plans into dense robot actions. Our approach introduces a sparse geometric interface: the VLM predicts sparse 3D waypoints representing high-level intention, while GAE maps these waypoints together with real-time point cloud observations to continuous action trajectories. GAE is pretrained on a large-scale pointcloud–trajectory dataset comprising \textbf{150k} trajectories from both simulation and real-world robots. To further improve efficiency and generalization, we introduce an \textbf{Action Pre-training, Pointcloud Fine-tuning (APPF)} scheme that decouples learning action dynamics from geometry grounding. After pretraining, GAE is frozen and reused across downstream tasks, requiring only lightweight fine-tuning of the VLM to produce the sparse interface. Extensive experiments show that our method achieves strong performance and generalization across diverse visual domains, camera viewpoints, and natural language instructions.

---

## 论文详细总结（自动生成）

# GAE：利用可泛化动作专家释放VLM的物理潜力

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **核心问题**：视觉语言模型（VLM）在推理和规划方面能力强大，但将其预测落实为精确的机器人动作仍存在困难。现有视觉-语言-动作（VLA）方法通常将推理与动作生成耦合在一起，导致泛化能力受限，且跨任务部署成本高昂。
- **研究动机**：为机器人动作生成引入一个与任务无关的通用动作专家，将VLM的高级规划与低层动作执行解耦，从而降低适应新任务的成本，提升泛化能力。
- **整体含义**：通过稀疏几何接口，把VLM的语义理解与实时感知的运动控制分开，使动作生成模型可以大规模预训练并冻结复用，仅需轻量微调VLM即可适配下游任务。

## 2. 论文提出的方法论
- **核心思想**：学习一个**通用动作专家（Generalizable Action Expert, GAE）**，它接收VLM预测的稀疏3D路点与实时点云观测，直接输出连续动作轨迹。这样，VLM只需负责高层意图表达（路点），动作执行由GAE负责。
- **关键技术细节**：
  - **稀疏几何接口**：VLM预测一组稀疏的3D路点（代表高层规划意图），而不是直接生成动作。
  - **GAE模型**：以路点和点云作为输入，映射为连续动作轨迹（如关节位置或末端执行器位姿序列）。
  - **两阶段训练策略（APPF）**：**动作预训练（Action Pre-training）** 阶段先在大规模点云-轨迹数据集上学得动作动态的先验；随后**点云微调（Pointcloud Fine-tuning）** 阶段再结合几何信息微调，从而实现动作动态与几何理解的解耦学习，提升效率与泛化。
- **算法流程（文字说明）**：
  1. VLM根据视觉观测和语言指令推理出若干个3D路点；
  2. 将路点连同当前时刻的点云观测一并送入预训练好的GAE；
  3. GAE输出从当前状态到路点的连续动作序列；
  4. 执行动作并循环上述过程，直至任务完成。
  5. 预训练后GAE参数冻结，下游任务只需微调VLM以适应新的路点输出格式。

## 3. 实验设计
- **数据集/场景**：
  - 大规模预训练数据集：包含约**15万**条来自仿真和真实机器人的点云-轨迹数据（150k trajectories）。
  - 下游测评场景：覆盖多种视觉域（如不同背景、光照）、相机视角和自然语言指令。
- **对比方法**：
  - 与现有的视觉-语言-动作（VLA）方法进行对比，具体名称未在摘要中列出，但应包含将推理与动作生成耦合的基线模型。
- **评估指标**：
  - 任务成功率，泛化能力（跨视觉域、视角、指令的稳定性）。

## 4. 资源与算力
- 文中未明确给出GPU型号、数量及训练时长的具体数值。摘要及已有信息并未提及相关算力细节。

## 5. 实验数量与充分性
- **实验组数**：
  - 预训练阶段使用了15万条轨迹的大规模数据集；
  - 下游实验涵盖多种视觉域、相机视角、自然语言指令，进行了多组对比和消融（从“extensive experiments”推断）；
- **充分性与客观性**：
  - 在多样化条件下测试了模型的泛化能力，较为充分；
  - 对比方法设置为现有VLA方法，客观性有保障；
  - 但因信息有限，无法判断是否包含详尽的消融研究（如不同路点密度、不同预训练策略的对比），实验细节尚需阅读全文。

## 6. 论文的主要结论与发现
- GAE能够将VLM的高层规划有效转换为可执行动作，与任务无关的架构设计大幅降低了任务适配成本。
- APPF训练策略将动作动态学习与几何理解解耦，提升了数据效率与泛化能力。
- 预训练后的GAE可在多种下游任务中冻结复用，仅需微调VLM，表现出跨视觉域、视角和指令的强大性能。
- 该稀疏到密集的映射思路也具备向自动驾驶等领域迁移的潜力，可为轨迹规划提供参考。

## 7. 优点（方法或实验设计亮点）
- **解耦设计**：将高层语义规划与低层动作生成分离，减少耦合带来的泛化瓶颈。
- **稀疏几何接口**：用稀疏3D路点作为中间表示，既保留VLM的强推理能力，又降低了动作生成的复杂度。
- **大规模预训练+轻量适配**：GAE一次预训练后直接冻结，下游任务仅需微调VLM，显著降低部署成本。
- **解耦训练策略（APPF）**：创新性地将动作动态学习与点云几何理解分阶段训练，提升效率。
- **跨实体的泛化性**：数据集涵盖仿真和真实机器人，方法具有较强的现实适用性。

## 8. 不足与局限
- **信息有限**：仅依据摘要和元数据，无法评估实验的全面性、消融设计的严谨性以及统计显著性。
- **算力要求不明**：未披露训练所需算力资源，无法评估实际落地成本。
- **动作空间的局限性**：假设动作轨迹可由路点和点云唯一确定，在复杂动态环境或需要力反馈的任务中可能不足。
- **对VLM的依赖**：下游任务仍需微调VLM，虽比全模型微调轻量，但仍需要VLM具备一定的适应性。
- **评估范围未明**：未提及在何种具体机器人平台和任务上评估，缺乏对失败案例的分析。
- **接口普适性**：稀疏路点作为接口是否适用于所有类型的机器人动作（如灵巧手操作、移动抓取等）有待验证。

（完）
