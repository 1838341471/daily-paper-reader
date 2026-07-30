---
title: "ModeSeq: Taming Sparse Multimodal Motion Prediction with Sequential Mode Modeling"
title_zh: ModeSeq：通过序列模式建模驯服稀疏多模态运动预测
authors: "Zhou, Zikang, Zhou, Hengjian, Hu, Haibo, Wen, Zihao, Wang, Jianping, Li, Yung-Hui, Huang, Yu-Kai"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Zhou_ModeSeq_Taming_Sparse_Multimodal_Motion_Prediction_with_Sequential_Mode_Modeling_CVPR_2025_paper.pdf"
tags: ["query:av-traj-pred"]
score: 9.0
evidence: 稀疏多模态运动预测与序列模式建模
tldr: 多模态轨迹预测面临缺乏多模态真值、轨迹多样性不足和置信度不准的问题。本文提出ModeSeq，一种基于序列模式建模的新范式，通过自回归方式逐步生成多模态轨迹候选。该方法避免了后处理步骤，提升了轨迹多样性和置信度校准。在多个自动驾驶数据集上，ModeSeq优于现有工作的预测精度和模式覆盖。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhou-modeseq-taming-sparse-multimodal-motion-prediction-with-sequential-mode-modeling-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 863, \"height\": 324, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhou-modeseq-taming-sparse-multimodal-motion-prediction-with-sequential-mode-modeling-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1786, \"height\": 619, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhou-modeseq-taming-sparse-multimodal-motion-prediction-with-sequential-mode-modeling-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 870, \"height\": 420, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-zhou-modeseq-taming-sparse-multimodal-motion-prediction-with-sequential-mode-modeling-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1810, \"height\": 467, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhou-modeseq-taming-sparse-multimodal-motion-prediction-with-sequential-mode-modeling-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 874, \"height\": 233, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhou-modeseq-taming-sparse-multimodal-motion-prediction-with-sequential-mode-modeling-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1814, \"height\": 386, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhou-modeseq-taming-sparse-multimodal-motion-prediction-with-sequential-mode-modeling-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1807, \"height\": 331, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhou-modeseq-taming-sparse-multimodal-motion-prediction-with-sequential-mode-modeling-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1810, \"height\": 245, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-zhou-modeseq-taming-sparse-multimodal-motion-prediction-with-sequential-mode-modeling-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 874, \"height\": 627, \"label\": \"Table\"}]"
motivation: 现有轨迹预测方法轨迹多样性有限且模式置信度未校准，后处理步骤损害准确性。
method: 采用序列模式建模，将多模态预测转化为自回归模式生成，逐步产生轨迹候选。
result: 在交互式运动预测基准上，ModeSeq在多样性、准确性和校准方面均取得最优。
conclusion: 序列模式建模为多模态预测提供了更简洁有效的框架。
---

## Abstract
Anticipating the multimodality of future events lays the foundation for safe autonomous driving. However, multimodal motion prediction for traffic agents has been clouded by the lack of multimodal ground truth. Existing works predominantly adopt the winner-take-all training strategy to tackle this challenge, yet still suffer from limited trajectory diversity and uncalibrated mode confidence. While some approaches address these limitations by generating excessive trajectory candidates, they necessitate a post-processing stage to identify the most representative modes, a process lacking universal principles and compromising trajectory accuracy. We are thus motivated to introduce ModeSeq, a new multimodal prediction paradigm that models modes as sequences. Unlike the common practice of decoding multiple plausible trajectories in one shot, ModeSeq requires motion decoders to infer the next mode step by step, thereby more explicitly capturing the correlation between modes and significantly enhancing the ability to reason about multimodality. Leveraging the inductive bias of sequential mode prediction, we also propose the Early-Match-Take-All (EMTA) training strategy to diversify the trajectories further. Without relying on dense mode prediction or heuristic post-processing, ModeSeq considerably improves the diversity of multimodal output while attaining satisfactory trajectory accuracy, resulting in balanced performance on motion prediction benchmarks. Moreover, ModeSeq naturally emerges with the capability of mode extrapolation, which supports forecasting more behavior modes when the future is highly uncertain.

---

## 论文详细总结（自动生成）

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **研究动机**：自动驾驶中运动预测面临未来行为多模态（即多种可能性）的挑战。由于真实数据仅提供单一未来轨迹（缺乏多模态真值），现有方法普遍采用胜者通吃（winner-take-all, WTA）训练策略，但存在轨迹多样性不足、模式置信度未校准的问题。部分工作通过生成大量候选轨迹并用后处理（如非极大抑制）挑选代表，但这牺牲了准确性且超参数难以通用。
- **整体含义**：本文提出 **ModeSeq**，一种将多模态预测建模为序列生成的新范式。通过逐步解码模式，显式捕捉模式间相关性，并结合 **Early‑Match‑Take‑All (EMTA)** 训练策略，在无需密集预测或启发式后处理的情况下，同时提升轨迹多样性、准确性和置信度校准，并拥有模式外推能力（可动态调整输出模式数量）。

## 2. 论文提出的方法论

- **核心思想**：将模式视为序列，利用自回归方式逐步推断下一个模式。与传统并行解码（一次性输出所有模式）不同，ModeSeq 在每一步解码时依赖之前已生成的模式嵌入，从而强化模式间关系，促进多样性。
- **关键技术细节**：
  - **场景编码**：采用 QCNet 作为编码器（可替换），提取以智能体和地图为中心的嵌入。
  - **单层 ModeSeq**：每一层包含两个 Transformer 模块：
    - **Memory Transformer**：将当前步的输入查询与之前所有步的模式嵌入进行交叉注意力，融合历史模式信息。
    - **Context Transformer**：将条件化后的查询与场景嵌入（包括时间、地图、邻居智能体）融合，获得上下文感知的模式嵌入。
    - **预测头**：对每个模式输出轨迹和置信度（MLP）。
  - **多层迭代精炼**：堆叠多个 ModeSeq 层，每层之间执行**模式重排**（按置信度降序排列模式嵌入），使下一层优先处理高置信度的模式。
  - **EMTA 训练策略**：
    - 匹配准则：根据基准定义（如速度加权距离或末点误差<2m）判断预测轨迹是否匹配真值。
    - 正样本选择：在匹配的模式中，选择**最早解码步**的模式作为正样本，其余匹配模式视为负样本（强制它们远离真值以覆盖更多模式）。
    - 若无匹配，则回退到 WTA。
    - 损失：回归使用 Laplace 负对数似然，置信度使用二值 Focal Loss。
- **公式/算法流程**（文字说明）：
  1. 编码器计算场景嵌入 Ψ。
  2. 初始化第 0 层模式嵌入为可学习向量 e。
  3. 对每一层 ℓ：
     - 初始化空记忆库 Ω。
     - 对每个解码步 k：
       - Memory Transformer：ˆm_k = MemFormer(query=m_{k}^{(ℓ-1)}, key/value=Ω)
       - Context Transformer：m_k^{(ℓ)} = CtxFormer(query=ˆm_k, key/value=Ψ)
       - 将 m_k^{(ℓ)} 推入 Ω。
     - 使用预测头输出轨迹和置信度。
  4. 层间进行模式重排（按置信度降序）。
  5. 计算 EMTA 损失（正样本为最早匹配步）。

## 3. 实验设计

- **数据集**：
  - **Waymo Open Motion Dataset (WOMD)**：48.7 万训练 / 4.4 万验证 / 4.5 万测试样本，1.1s 历史，8s 未来。
  - **Argoverse 2 Motion Forecasting Dataset**：19.99 万训练 / 2.5 万验证 / 2.5 万测试样本，5s 观察，6s 预测。
- **Benchmark**：标准评测指标包括：
  - **mAP** 和 **Soft mAP**（评估置信度校准与模式覆盖），**Miss Rate (MR)**（衡量成功率），**minADE** 和 **minFDE**（轨迹精度），**b‑minFDE**（含 Brier 分数）。
- **对比方法**：主要与 **QCNet**（稀疏预测）、**MTR 系列**（MTR v3, MTR++，密集预测+后处理）比较。也提及了 **RMP Ensemble** 等 ensemble 方法。
- **实验设置**：K=6 个模式，隐藏维度 128，解码器 6 层，每层6步。WOMD 上训练 30 轮，Argoverse 2 上 64 轮，batch size 32，初始学习率 5e‑4，余弦退火。AdamW 优化器，权重衰减 0.1，dropout 0.1。部分消融使用 20% WOMD 数据。

## 4. 资源与算力

- 论文**未明确说明**所使用的 GPU 型号、数量以及训练耗时。仅在“Implementation Details”中给出了训练轮数、batch size 等超参数，但未提及算力资源。因此无法评估计算成本。

## 5. 实验数量与充分性

- **实验组数**：
  - 主表对比：WOMD 验证集与测试集、Argoverse 2 验证集与测试集，各对比 3~5 种方法。
  - 消融实验 4 组（表 3‑5 及图 3‑5），分别考察：
    - 序列模式建模 vs. DETR-like 解码器（表 3）。
    - EMTA vs. WTA 及忽略样本策略（表 3）。
    - 模式重排与忽略样本策略（表 4）。
    - 迭代层数影响（图 3）。
    - 模式数量：3 模式 vs. 6 模式（表 5）。
    - 模式外推：6 模式训练 → 更多步推理（图 5）。
  - 实验设计较全面，覆盖了主要创新点。
- **充分性与客观性**：
  - 对比方法均为当前 SOTA，基线公平（相同编码器 QCNet）。
  - 消融实验逐一验证了序列建模、EMTA、模式重排、迭代精炼的作用。
  - 在 WOMD 和 Argoverse 2 两个大型公开基准上验证，具有代表性。
  - 不足之处：未对比更多基线（如 Wayformer、TNT 等），可能遗漏某些近期方法；部分消融仅用 20% 数据训练，可能影响泛化结论，但作者说明了这一点。

## 6. 论文的主要结论与发现

- ModeSeq 在稀疏模式下实现了与密集预测相当的覆盖率和更优的置信度校准，同时避免后处理带来的精度损失。
- 序列模式建模 + EMTA 训练显著提升了 Soft mAP 和 MR，且轨迹精度仅轻微下降（minADE <0.02m，minFDE <0.04m），整体更均衡。
- 模式重排协调 EMTA 训练，促进高置信度、匹配轨迹尽早出现。
- ModeSeq 具备模式外推能力：训练时生成 6 个模式，推理时可扩展至更多步数，且误差持续降低，适用于不确定性高的场景。
- 在 WOMD 2024 挑战赛中，集成版 ModeSeq 在无激光雷达方法中排名第一。

## 7. 优点

- **创新性**：首次将序列建模引入模式维度，突破并行解码的局限。
- **简洁高效**：无需密集模式预测或后处理，直接输出稀疏、多样、校准好的轨迹。
- **训练策略独特**：EMTA 通过最早匹配作为正样本，简单有效，促进模式覆盖。
- **外推能力**：动态调整推理时模式数，适应不同不确定性程度。
- **实验充分**：在两大基准上验证，消融实验支持各组件贡献。

## 8. 不足与局限

- **推理延迟较高**：6 模式时约 143ms，是 QCNet 的两倍（69ms），可能影响实时性。但 3 模式时延迟差距缩小（86ms vs 63ms），且 3 模式 ModeSeq 的 mAP 已超过 6 模式 QCNet。
- **未报告训练资源**：未说明 GPU 型号、数量及训练时间，难以复现成本。
- **消融实验部分使用 20% 数据**：结论可能受限于数据量，全数据消融可增强说服力。
- **未与更多近期方法（如 Wayformer）对比**：对比基线较少，可能未完全体现优势。
- **对匹配准则的依赖**：EMTA 中是否匹配依赖于手工阈值（如 2m FDE），不同阈值可能影响结果。
- **方法通用性**：虽然在 WOMD 和 Argoverse2 上有效，但未在其他场景（如第三方行人数据集）验证。

（完）
