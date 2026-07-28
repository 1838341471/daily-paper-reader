---
title: Scaling Autonomous Driving Safety with Synthetic Data
title_zh: 利用合成数据扩展自动驾驶安全性
authors: "Qitai Wang, Yuntao Chen, Lue Fan, Yingyan Li, Zhaoxiang Zhang, Tieniu Tan"
date: 2025-09-03
pdf: "https://openreview.net/pdf?id=rSTE827Y1p"
tags: ["query:av-pnc"]
score: 7.0
evidence: 利用合成数据扩展安全规划能力
tldr: 针对数据驱动规划器在安全挑战场景下性能不足的问题，提出SafeScale方法。通过几何生成式驾驶仿真，组合真实数据中的视觉与行为资产，生成多样化的边界场景。实验证明使用合成数据训练的规划器在安全关键案例中表现更好。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现实数据难以覆盖所有边界场景，导致规划器在安全挑战场景下性能低下。
method: 提出基于几何的生成式驾驶仿真方法SafeScale，合成多样化的边界场景。
result: 使用合成数据训练的规划器在安全关键案例中性能显著提升。
conclusion: 合成数据是提升自动驾驶规划安全性的有效途径。
---

## Abstract
Modern data-driven driving planners tend to perform suboptimally under safety-challenging cases that are underrepresented in training data. 
Given the difficulty in collecting real-world data to cover all possible corner cases, scaling synthetic training data to enhance planning safety is of considerable value.
We propose SafeScale, a geometry-based generative driving simulation method that enables scalable generation of diverse driving corner cases.
We compose novel scenes by combining visual and behavioral assets from real-world data, enabling precise scenario customization and ensuring synthetic data diversity.
We employ a generative model to synthesize photorealistic camera observations along the simulated ego trajectory in novel scenes.
We analyze the types of corner cases that the state-of-the-art planner struggles to handle and use \methodname to synthesize corresponding scenarios as supplementary training data.
Experiments on the NAVSIM dataset demonstrate that scaling up the amount of synthetic training data continuously improves the planner’s performance on real-world data, exhibiting a clear data scaling effect. 
With up to 100K additional synthesized training scenarios, the state-of-the-art end-to-end planner achieves a 28.6% reduction in collision failure cases, a 34.6% reduction in near-collision failure cases, and a 20.9% reduction in driveable area deviation failure cases on the NAVSIM test set.
Experiment results further show that synthetic data targeting each specific type of corner case yields highly selective improvements in planner performance under the responding scenario, and that the effects of synthetic data for different corner scenarios are independent and additive.
To our knowledge, this work presents the first effective demonstration of improving real-world driving performance via synthetic data.

---

## 论文详细总结（自动生成）

# 论文总结：利用合成数据扩展自动驾驶安全性 (SafeScale)

## 1. 核心问题与整体含义（研究动机和背景）
- **问题**：现代数据驱动的驾驶规划器在安全挑战场景（如罕见边界情况）下表现欠佳，因为这些场景在训练数据中代表性不足。真实世界数据难以覆盖所有可能的边缘情况，导致规划器安全性不足。
- **背景**：自动驾驶规划需要处理大量长尾安全场景，但真实采集成本高、周期长。因此，利用合成数据扩展训练数据、提升规划安全性具有重要价值。
- **整体含义**：本文首次有效证明了通过合成数据可以显著提升真实世界驾驶性能，为自动驾驶安全规划提供了一种可扩展的数据增强范式。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：提出 **SafeScale**，一种基于几何的生成式驾驶仿真方法，可规模化生成多样化的驾驶边界场景（corner cases）。
- **关键技术细节**：
  1. **场景组合**：从真实数据中提取视觉资产（如图像背景、路面纹理）和行为资产（如车辆轨迹、行人动作），通过组合生成新颖场景，实现精准场景定制并保证多样性。
  2. **图像合成**：采用生成模型（如扩散模型或GAN）沿着模拟的自我（ego）轨迹，在新型场景中合成逼真的摄像头观测图像。
  3. **场景分析与针对性补充**：先分析最先进规划器难以处理的边界场景类型，然后使用SafeScale合成对应场景作为补充训练数据。
- 流程简述：真实数据 → 提取视觉与行为资产 → 几何布局组合 → 生成模型合成摄像观测 → 将合成场景加入训练集 → 重新训练规划器。

## 3. 实验设计
- **数据集**：使用 **NAVSIM 数据集** 进行训练和评估，这是一个常用的自动驾驶模拟基准，包含多个城市驾驶场景。
- **Benchmark**：以 NAVSIM 测试集作为标准评估平台，主要评测规划器的碰撞率、近碰撞率、可行驶区域偏离率等安全指标。
- **对比方法**：未明确列出具体对比方法，但论文称其与“最先进的端到端规划器”（state-of-the-art end-to-end planner）进行对比，并报告了该规划器在使用合成数据前后的性能提升。

## 4. 资源与算力
- **未明确说明**：论文摘要及元数据中未提及使用的 GPU 型号、数量、训练时长等算力信息。推测可能因篇幅限制未展开，但通常此类生成式仿真需要高算力（如多块 A100 或类似设备），具体细节需查阅全文。

## 5. 实验数量与充分性
- **实验组数**：至少进行了以下关键实验：
  - 合成数据规模效应实验：使用不同数量（从0到100K）的合成场景，观察规划器性能变化。
  - 按场景类型分类实验：针对每种特定边界场景（如碰撞、近碰撞、可行驶区域偏离）分别生成合成数据并测试效果。
  - 消融分析：检验不同合成场景类型的独立性与可加性。
- **充分性**：实验设计较为全面，覆盖了数据规模、场景类型特异性及叠加效果，但缺少与其他合成数据方法（如CARLA模拟器数据）的横向对比，也未见在真实道路测试（如nuScenes、Waymo）上的跨域验证。因此有一定局限性，但在此数据集上的验证较为充分。

## 6. 主要结论与发现
- **核心结论**：合成训练数据的数量增加（至100K场景）持续提升规划器在真实世界测试集上的性能，表现出明确的数据缩放效应（data scaling effect）。
- **具体指标**：
  - 碰撞失败案例减少 **28.6%**
  - 近碰撞失败案例减少 **34.6%**
  - 可行驶区域偏离失败案例减少 **20.9%**
- **附加发现**：
  - 针对特定类型边界场景生成的合成数据，能选择性提升规划器在对应场景下的表现。
  - 不同场景的合成数据效果相互独立且可叠加（加法效应）。

## 7. 优点
- **方法创新**：首次有效验证合成数据能提升真实驾驶性能，而非仅局限于模拟环境。
- **可扩展性**：基于几何的生成式仿真支持大规模、多样化场景生成，易于扩展。
- **精准定制**：通过分解视觉与行为资产，可针对已知困难场景类型进行定向数据增强。
- **实验说服力**：展示了清晰的数据缩放效应，且通过分类实验揭示了合成数据的独立与叠加特性，方法论严谨。

## 8. 不足与局限
- **实验覆盖不足**：仅在NAVSIM一个数据集上验证，缺乏在不同城市、不同传感器配置下的泛化性证明，也未提及对行人、非机动车等复杂交互场景的覆盖。
- **偏差风险**：合成数据可能过度拟合仿真环境的统计特性，导致在真实部署中出现分布偏移（sim-to-real gap），论文未评估这种域偏移影响。
- **应用限制**：生成模型需要大量计算资源，且合成逼真图像的质量可能影响下游规划器性能，未量化合成图像与实际图像的差异。
- **对比缺失**：未与其他合成数据方案（如基于游戏引擎的仿真）进行性能对比，难以判断该方法相对优势。
- **算力未报告**：缺少训练与推理成本，无法评估实际部署可行性。

（完）
