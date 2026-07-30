---
title: "SOLVE: Synergy of Language-Vision and End-to-End Networks for Autonomous Driving"
title_zh: SOLVE：语言-视觉与端到端网络协同的自动驾驶框架
authors: "Chen, Xuesong, Huang, Linjiang, Ma, Tao, Fang, Rongyao, Shi, Shaoshuai, Li, Hongsheng"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_SOLVE_Synergy_of_Language-Vision_and_End-to-End_Networks_for_Autonomous_Driving_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 9.0
evidence: 直接针对自动驾驶的轨迹预测与规划
tldr: 现有方法在集成VLM与端到端模型时面临计算开销大、实时性差的问题。本文提出SOLVE框架，通过共享视觉编码器实现特征级知识共享，并提出轨迹链式思维(T-CoT)范式逐步优化轨迹预测。实验表明该方法在规划准确性上优于基线，同时保持实时性。该工作为语言-视觉融合在自动驾驶规划中的应用提供了新思路。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-solve-synergy-of-language-vision-and-end-to-end-networks-for-autonomous-driving-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 893, \"height\": 382, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-solve-synergy-of-language-vision-and-end-to-end-networks-for-autonomous-driving-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 850, \"height\": 471, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-solve-synergy-of-language-vision-and-end-to-end-networks-for-autonomous-driving-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1754, \"height\": 589, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-solve-synergy-of-language-vision-and-end-to-end-networks-for-autonomous-driving-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 835, \"height\": 498, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-chen-solve-synergy-of-language-vision-and-end-to-end-networks-for-autonomous-driving-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1764, \"height\": 1437, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-solve-synergy-of-language-vision-and-end-to-end-networks-for-autonomous-driving-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1300, \"height\": 742, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-solve-synergy-of-language-vision-and-end-to-end-networks-for-autonomous-driving-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 866, \"height\": 234, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-solve-synergy-of-language-vision-and-end-to-end-networks-for-autonomous-driving-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 795, \"height\": 240, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-solve-synergy-of-language-vision-and-end-to-end-networks-for-autonomous-driving-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 730, \"height\": 276, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-chen-solve-synergy-of-language-vision-and-end-to-end-networks-for-autonomous-driving-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 736, \"height\": 278, \"label\": \"Table\"}]"
motivation: 现有VLM与端到端模型集成效率低，难以实现实时决策。
method: 提出共享视觉编码器实现特征交互，并设计轨迹链式思维(T-CoT)来逐步优化轨迹预测。
result: 在多个自动驾驶数据集上，SOLVE在规划准确性和实时性上取得最优。
conclusion: 证明了语言-视觉协同能有效提升端到端自动驾驶规划性能。
---

## Abstract
The integration of Vision-Language Models (VLMs) into autonomous driving systems has shown promise in addressing key challenges such as learning complexity, interpretability, and common-sense reasoning. However, existing approaches often struggle with efficient integration and real-time decision-making due to computational demands. In this paper, we introduce SOLVE, an innovative framework that synergizes VLMs with end-to-end (E2E) models to enhance autonomous vehicle planning. Our approach emphasizes knowledge sharing at the feature level through a shared visual encoder, enabling comprehensive interaction between VLM and E2E components. We propose a Trajectory Chain-of-Thought (T-CoT) paradigm, which progressively refines trajectory predictions, reducing uncertainty and improving accuracy. By employing a temporal decoupling strategy, SOLVE achieves efficient asynchronous cooperation, aligning high-quality VLM outputs with E2E real-time performance. Evaluated on the nuScenes dataset, our method demonstrates significant improvements in trajectory prediction accuracy, paving the way for more robust and reliable autonomous driving systems.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：端到端自动驾驶系统虽然通过端到端学习简化了流程，但仍面临学习复杂性高、常识推理不足、可解释性有限以及因果混淆等问题。引入视觉-语言模型（VLM）可以缓解这些不足，但现有方法在集成VLM与端到端（E2E）模型时效率低下，计算开销大，难以满足实时决策需求。
- **研究动机**：旨在探索如何有效地协同VLM的高层推理能力与E2E模型的实时感知-规划能力，实现两者在**特征级**和**轨迹级**的深度融合，从而在保证实时性的前提下提升轨迹预测的准确性和鲁棒性。
- **整体含义**：提出了**SOLVE**框架，通过共享视觉编码器、轨迹链式思维（T-CoT）和时序解耦策略，实现VLM与E2E模型的高效协同，为构建更可靠、更智能的自动驾驶规划系统提供了新思路。

### 2. 论文提出的方法论

- **核心思想**：构建一个同时包含VLM和E2E模块的统一框架，核心在于两层协同：
  - **特征级协同**：通过共享的**顺序Q-Former（SQ-Former）** 视觉编码器，将多视图图像压缩成统一的视觉token，同时服务于VLM和E2E模型，实现感知特征的高效共享。
  - **轨迹级协同**：引入**轨迹链式思维（T-CoT）**，让VLM逐步优化轨迹预测；同时通过**时序解耦策略**，让E2E模型异步利用VLM的历史高质量轨迹作为初始化先验，平衡精度与实时性。
- **关键技术细节**：
  - **SQ-Former**：基于Q-Former架构，将静态场景线索（如天气、路况）和动态信息（障碍物、车道线）按顺序编码到固定数量的视觉query中。具体流程：先通过collector queries捕获静态线索（公式1），再与任务特定query（检测、车道线）连接，通过并行解码器获得更新后的视觉特征（公式2）。按“图像→3D检测→车道线”顺序进行，共使用384个query。
  - **T-CoT**：包含两阶段：
    - **轨迹选择**：从预定义的轨迹库（通过K-means聚类训练集得到36个候选轨迹，结合MLP预测轨迹）中选出top-k+1个候选，VLM根据场景选择最佳轨迹。
    - **轨迹细化**：以所选轨迹的waypoints作为参考，VLM生成更精确的最终轨迹。
  - **时序解耦策略**：VLM预测较长未来时域（超过自身延迟）的轨迹并存入记忆，E2E模型在后续帧中从记忆读取该轨迹（存在时间偏移）作为额外的规划query初始化，从而在不影响实时性的情况下利用VLM的高质量预测。
- **训练策略**：多阶段训练：
  1. 用OmniDrive的QA对训练VLM（含LoRA），优化SQ-Former的collector queries。
  2. 训练轨迹适配器，使轨迹token与VLM特征空间对齐。
  3. 冻结SQ-Former和适配器，训练E2E规划头。
  4. 联合微调VLM和E2E规划头（不冻结任何组件），并使用T-CoT。
  5. 在最后阶段，利用VLM历史帧的预测轨迹更新E2E规划器的初始化query。

### 3. 实验设计

- **数据集**：使用**nuScenes**数据集（urban environment，1000个场景，每个约20秒）。
- **Benchmark**：开放循环（open-loop）规划任务，即在给定历史帧条件下预测未来轨迹，与真实轨迹比较。
- **评价指标**：**L2位移误差**（1s/2s/3s及平均）和**碰撞率**。
- **对比方法**：包括UniAD、VAD-Base、AD-MLP、BEV-Planner、DriveVLM、OmniDrive、EMMA、DriveVLM-Dual等，涵盖纯端到端方法和VLM集成方法。

### 4. 资源与算力

- **文中未明确说明所使用的GPU型号、数量和训练时长**。仅在消融实验部分提到“训练SQ-Former和VLM 6个epoch”以优化计算资源，但未给出具体硬件配置。因此无法量化算力消耗，这是论文在实验可重复性方面的不足之处。

### 5. 实验数量与充分性

- **实验组数**：主要实验包括：
  - 主表（Table 1）：对比10+种方法，包含SOLVE的3个变体（E2E、VLM、Async）。
  - 消融实验4组（Table 2-5）：分别针对SQ-Former查询数、视觉编码顺序、T-CoT中轨迹数量、共享SQ-Former的效果。
  - 定性展示（Figure 5）：两个场景的轨迹可视化。
- **充分性与公平性**：
  - 对比了多种SOTA方法，涵盖纯E2E和VLM集成方法，且均使用相同的nuScenes开放循环设置，评价标准统一，较为公平。
  - 消融实验覆盖了所有核心设计（SQ-Former结构、T-CoT、共享机制），证明了各组件贡献。
  - **不足**：仅在nuScenes一个数据集上进行评估，未在Waymo、nuPlan等其他数据集上验证泛化性；仅进行开放循环测试，缺乏闭环仿真测试；未与最新的VLM方法（如DriveCoT）直接对比。因此实验虽然内部分析充分，但外部有效性有待加强。

### 6. 论文的主要结论与发现

- SOLVE在开放循环规划上达到**state-of-the-art**：SOLVE-VLM在平均L2误差（0.28m）和碰撞率（0.20%）上均优于所有对比方法。
- **共享SQ-Former和联合训练**显著提升性能：E2E和VLM分别下降1.5cm和0.6cm的L2误差（Table 5）。
- **T-CoT**通过提供轨迹先验和逐步细化，使VLM的L2误差降低1.1cm（Table 4）。
- **时序解耦策略**进一步提升E2E性能（Async版本L2误差从0.31降至0.30）。
- 定性结果证实VLM在复杂场景下（如偏离车道中心）相比E2E更具优势，而异步融合可纠正E2E的偏差。

### 7. 优点

- **创新性**：首次同时实现**特征级**（共享视觉编码器）和**轨迹级**（T-CoT与时序解耦）的双层协同，克服了以往仅靠post-processing集成的局限。
- **高效性**：SQ-Former用较少query（384）压缩多源信息，降低VLM计算成本；T-CoT仅需少量文本输出，避免长文本CoT的高开销。
- **实用性**：时序解耦策略允许VLM以异步方式提供高质量先验，不牺牲E2E的实时性，适合实际部署。
- **实验设计严谨**：多组消融逐一验证每个设计的效果，且控制变量（如训练epoch一致）合理。

### 8. 不足与局限

- **数据集单一**：仅在nuScenes上评测，缺乏跨数据集（如Waymo）的泛化验证，可能存在过拟合风险。
- **评估模式有限**：仅开放循环（open-loop），未进行闭环（closed-loop）模拟测试，无法评估规划-控制闭环稳定性及对偶发情况的反应。
- **性能偏差风险**：VLM依赖OmniDrive的QA数据，该数据集是nuScenes的扩展，可能对特定场景有偏差；此外，T-CoT中的轨迹库通过K-means聚类训练集得到，在分布外场景下可能失效。
- **计算资源未公开**：缺乏硬件和训练时间的详细信息，不利于复现和公平比较。
- **未与更近期的VLM方法对比**：如DriveCoT等同期工作未被纳入比较，可能遗漏更优基线。
- **实际部署挑战**：VLM部分仍需要较大内存和推理时间（尽管有LoRA和时序解耦），在资源受限的嵌入式平台上可能仍难以达到实时。

（完）
