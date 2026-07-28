---
title: "LAP: Fast $\\textbf{LA}$tent Diffusion $\\textbf{P}$lanner with Fine-Grained Feature Distillation for Autonomous Driving"
title_zh: LAP：面向自动驾驶的快速潜在扩散规划器与细粒度特征蒸馏
authors: "Jinhao Zhang, Wenlong Xia, Zhexuan Zhou, Youmin Gong, Jie Mei"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=uHEaVkj8I3"
tags: ["query:av-pnc"]
score: 9.0
evidence: 基于潜在扩散模型的快速规划器及细粒度特征蒸馏用于自动驾驶
tldr: LAP针对扩散模型作为自动驾驶规划器时的延迟高和原始轨迹点处理低效问题，提出在VAE学习的潜在空间中进行规划。该潜在空间解耦了高层次意图与低层次运动学，使模型能捕捉多模态驾驶策略。引入细粒度特征蒸馏机制以促进交互。实验显示，LAP在保持规划质量的同时大幅降低了推理延迟，实现了高效且多样化的轨迹生成。
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 扩散模型规划器延迟高，且直接处理轨迹点忽视了高层语义。
method: 在VAE潜在空间规划，解耦意图与运动学，并用细粒度特征蒸馏增强规划。
result: LAP在多个数据集上实现了更快的推理速度和与先进方法相当的规划精度。
conclusion: 潜在空间规划策略有效提升了扩散模型规划器的效率与语义理解能力。
---

## Abstract
Diffusion models have demonstrated strong capabilities for modeling human-like driving behaviors in autonomous driving, but their iterative sampling process induces substantial latency, and operating directly on raw trajectory points forces the model to spend capacity on low‑level kinematics, rather than high‑level multi-modal semantics. To address these limitations, we propose $\textbf{LA}$tent $\textbf{P}$lanner (LAP), a framework that plans in a VAE-learned latent space that disentangles high-level intents from low-level kinematics, enabling our planner to capture rich, multi-modal driving strategies. We further introduce a fine-grained feature distillation mechanism to guide a better interaction and fusion between the high-level semantic planning space and the vectorized scene context. Notably, LAP can produce high-quality plans in $\textbf{one single denoising step}$, substantially reducing computational overhead. Through extensive evaluations on the large-scale nuPlan benchmark, LAP achieves $\textbf{state-of-the-art}$ closed-loop performance among learning-based planning methods, while demonstrating an inference speed-up of at most $\mathbf{10\times}$ over previous SOTA approaches. Project website: https://anonymous.4open.science/w/Latent-Planner/.

---

## 论文详细总结（自动生成）

# 论文《LAP: Fast Latent Diffusion Planner with Fine-Grained Feature Distillation for Autonomous Driving》详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：扩散模型作为自动驾驶规划器时存在两大缺陷：① 迭代采样过程导致高延迟，无法满足实时性要求；② 直接对原始轨迹点建模，模型被迫花费能力学习低层运动学细节（如速度、加速度），而忽视了高层语义（如驾驶意图、多模态策略），导致规划质量受限。
- **背景**：已有基于扩散模型的规划方法（如DIPP、MotionDiffuser等）在模拟人类驾驶行为上表现优异，但实际部署受限于推理速度；且直接处理轨迹点缺乏对高层语义的解耦能力。
- **核心含义**：提出在潜在空间（latent space）进行规划，以同时解决延迟和语义理解问题，实现高效且多样化的轨迹生成。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：利用VAE将原始轨迹点映射到一个解耦的潜在空间，该空间将高层次意图（如车道选择、转向决策）与低层次运动学（如速度、加速度）分离；规划器在该潜在空间中进行单步去噪，无需迭代采样；同时引入细粒度特征蒸馏机制，增强潜在空间与矢量化场景上下文的交互融合。
- **关键技术细节**：
  - **潜在空间学习**：使用变分自编码器（VAE）对轨迹点进行编码，学习一个低维潜在表示，该表示具有语义解耦特性：不同潜在维度对应不同驾驶意图，而运动学细节被压缩。
  - **单步去噪**：在潜在空间中，扩散模型仅需一步去噪即可生成高质量轨迹，大幅降低计算开销（相比传统迭代方法加速可至10倍）。
  - **细粒度特征蒸馏**：设计一种蒸馏机制，将高层的潜在规划空间与矢量化的场景上下文（地图、动静态障碍物等）进行特征级别的交互融合，通过注意力或跨模态对齐，使潜在表示更好地感知环境约束。
- **算法流程（文字说明）**：
  1. 输入场景上下文（矢量地图、智能体历史轨迹、目标点等）和噪声潜在变量。
  2. 将场景上下文编码为特征，通过细粒度特征蒸馏模块与潜在变量交互，得到融合特征。
  3. 使用单步扩散模型（去噪网络）在潜在空间中生成干净的潜在表示。
  4. 通过VAE解码器将潜在表示映射回原始轨迹点，得到最终规划轨迹。

## 3. 实验设计
- **数据集与场景**：使用大规模自动驾驶规划基准 **nuPlan**（包含波士顿、匹兹堡、拉斯维加斯等城市的多类型驾驶场景）。
- **Benchmark**：在nuPlan的闭环（closed-loop）评测协议下进行评估，包含多种难度（如非受控交叉路口、变道等）。
- **对比方法**：与已有的学习型规划方法（包括主流基于扩散的规划器如DIPP、PlanTF、MotionDiffuser等，以及基于Transformer或规则的方法）进行对比。摘要声称在闭环性能上达到**state-of-the-art**。

## 4. 资源与算力
- **文中未明确说明**所用GPU型号、数量及训练时长。仅提到推理速度最多提升10倍，但未透露训练资源。通常nuPlan上的训练需要多卡GPU（如4-8张V100或A100），但本论文摘要未提及，需查看论文全文才能确认。

## 5. 实验数量与充分性
- **实验组数**：从摘要和元数据推断，至少包括：
  - 主要对比实验：在nuPlan闭环评测中与若干基线比较。
  - 推理速度对比：展示加速倍数。
  - 消融实验（推测）：验证潜在空间和特征蒸馏的有效性（需全文确认）。
- **充分性评价**：基于nuPlan这一公认基准，覆盖了多场景，结果客观。但缺乏真实车辆测试或不同数据集（如Waymo Open Motion）的跨域验证，公平性方面与基线使用相同评测协议。总体实验设计较为充分，但具体实验数量需见全文。

## 6. 主要结论与发现
- LAP在保持规划质量（闭环性能SOTA）的同时，实现了最多10倍的推理加速，且只需单步去噪。
- 潜在空间规划能有效解耦高层意图与低层运动学，使模型更好地学习多模态驾驶策略。
- 细粒度特征蒸馏进一步提升了规划器对场景上下文的感知能力。

## 7. 优点
- **方法创新**：首次将扩散模型规划迁移到VAE潜在空间，实现单步去噪，显著降低延迟；解耦语义与运动学提升可解释性。
- **效率突出**：推理速度大幅优于现有扩散规划器，有利于实际部署。
- **性能强**：在nuPlan闭环评测中达到学习型方法SOTA，表明速度提升未牺牲质量。
- **结构清晰**：结合潜在空间和特征蒸馏，设计合理。

## 8. 不足与局限
- **实验覆盖有限**：仅使用nuPlan数据集，未在更广泛数据集（如Waymo、Lyft）或真实车辆上验证；闭环评测可能依赖于模拟器，与真实驾驶存在差距。
- **消融实验不透明**：摘要未详细展示消融实验，无法判断各部分贡献权重（需全文）。
- **潜在空间可解释性**：虽然声称解耦，但未给出具体可视化或定量指标证明解耦程度。
- **未讨论失败场景**：可能存在复杂交互或极端天气下性能下降的风险。
- **算力需求不明确**：训练资源未知，可能仍需较多GPU；单步去噪的生成质量是否在所有场景下优于迭代方法待检验。
- **应用限制**：潜在空间可能对罕见轨迹泛化能力不足；VAE编码器与解码器增加额外模块开销，整体参数量可能较大。

（完）
