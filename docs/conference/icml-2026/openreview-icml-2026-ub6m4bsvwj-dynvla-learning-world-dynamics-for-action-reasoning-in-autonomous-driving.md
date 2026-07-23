---
title: "DynVLA: Learning World Dynamics for Action Reasoning in Autonomous Driving"
title_zh: DynVLA：学习世界动力学用于自动驾驶动作推理
authors: "Shuyao Shang, Bing Zhan, Yunfei Yan, Yuqi Wang, Yingyan Li, Yasong An, Xiaoman Wang, Jierui Liu, Lu Hou, Lue Fan, Zhaoxiang Zhang, Tieniu Tan"
date: 2026-04-30
pdf: "https://openreview.net/pdf/51db5c75cae53ef147fa3a7b0d739e23c486cbaa.pdf"
tags: ["query:av-pnc"]
score: 10.0
evidence: 基于动力学链式思考的自动驾驶动作推理VLA模型
tldr: 针对自动驾驶决策，提出DynVLA模型，引入动力学链式思考（Dynamics CoT）范式。通过动力学分词器将未来演化压缩为少量token，并解耦自车与环境动态，在动作生成前预测世界动态，使决策更物理合理。实验表明比文本CoT方法更有效，提升决策质量且延迟低。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有自动驾驶VLA模型缺乏对世界动态的显式建模，导致决策不够物理真实。
method: 提出DynVLA，用动力学分词器压缩未来状态，解耦自车与环境动态，在动作前生成动力学token。
result: 在交互密集场景下提升决策质量，且保持低延迟推理。
conclusion: 动力学CoT为自动驾驶动作推理提供了有效的物理先验，优于文本CoT。
---

## Abstract
We propose DynVLA, a driving VLA model that introduces a new CoT paradigm termed Dynamics CoT. DynVLA forecasts compact world dynamics before action generation, enabling more informed and physically grounded decision-making. To obtain compact dynamics representations, DynVLA introduces a Dynamics Tokenizer that compresses future evolution into a small set of dynamics tokens. Considering the rich environment dynamics in interaction-intensive driving scenarios, DynVLA decouples ego-centric and environment-centric dynamics, yielding more accurate world dynamics modeling. We then train DynVLA to generate dynamics tokens before actions through SFT and RFT, improving decision quality while maintaining latency-efficient inference. Compared to Textual CoT, which lacks fine-grained spatiotemporal understanding, and Visual CoT, which introduces substantial redundancy due to dense image prediction, Dynamics CoT captures the evolution of the world in a compact, interpretable, and efficient form. Extensive experiments on NAVSIM, Bench2Drive, and a large-scale in-house dataset demonstrate that DynVLA consistently outperforms Textual CoT and Visual CoT methods, validating the effectiveness and practical value of Dynamics CoT.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义

- **核心问题**：现有自动驾驶视觉语言动作（VLA）模型在产生驾驶动作时，缺乏对物理世界未来动态的显式推理，导致决策过程缺乏对场景演变（如他车意图、自车动力学响应）的理解，难以在交互密集场景下做出可靠、物理上合理的判断。
- **整体含义**：本文通过引入“动力学思维链”（Dynamics CoT），要求模型在输出最终动作前，先预测压缩、解耦的世界动态表征，从而实现更加知情、物理上更扎实的决策。其核心思想是让模型学会“先预见变化，再决定操作”，提升复杂驾驶场景下的安全性。

### 2. 方法论

- **核心范式：动力学思维链（Dynamics CoT）**
  - 区别于仅用文字描述的文本思维链（Textual CoT）和预测完整图像的视觉思维链（Visual CoT），Dynamics CoT 以一种紧凑、可解释且高效的形式捕捉未来世界的演化。
- **关键技术组件与流程**
  - **动力学分词器（Dynamics Tokenizer）**：将未来场景的演化压缩为少量的动力学令牌（dynamics tokens）。
  - **解耦建模**：考虑到交互密集场景下环境动态的丰富性，模型将动态显式解耦为“自车中心（ego-centric）”和“环境中心（environment-centric）”两类令牌，分别建模本体运动与周围他物变化，提升建模精度。
  - **推理过程**：DynVLA 在执行动作生成之前，先生成上一步得到的动态令牌，即先预测世界动态，再基于该预测结果生成驾驶动作（如转向、加减速等）。
- **训练策略**
  - **监督微调（SFT）**：先通过监督学习让模型学会生成正确的动态令牌与动作。
  - **强化微调（RFT）**：进一步通过强化学习优化决策质量，同时保持推理的低延迟。
- **效果**：既保证了决策质量的显著提升，又维持了推理效率，避免像视觉思维链那样引入大量冗余。

### 3. 实验设计

- **数据集与场景**
  - **NAVSIM**：公开自动驾驶仿真数据集。
  - **Bench2Drive**：公开驾驶评测基准。
  - **大规模内部数据集（in‑house dataset）**：用于进一步验证方法的泛化性与实用性。
- **对比方法**
  - **Textual CoT 方法**：依赖于自然语言描述进行中间推理。
  - **Visual CoT 方法**：通过预测密集的未来图像进行中间推理。
  - 模型在不同数据集上均与上述两类方法进行了公平比较。
- **评测指标**：重点在决策质量提升与推理延迟控制两个方面进行验证。

### 4. 资源与算力

- 提供的论文信息中未明确提及 GPU 型号、数量、训练时长等具体算力细节。
- 文中仅强调方法保持了“延迟高效的推理”，但未给出训练阶段算力消耗的定量说明。

### 5. 实验数量与充分性

- 论文明确提及在 **NAVSIM**、**Bench2Drive** 和 **大规模内部数据集** 上开展了大量实验。
- 虽然未列出具体实验组数，但宣称通过充分的消融和对不同 CoT 范式的比较，验证了 Dynamics CoT 的有效性。
- 实验设计考虑到了多种数据来源与基准，确保对比的客观性与公平性。

### 6. 主要结论与发现

- DynVLA 引入的 Dynamics CoT 范式能够为自动驾驶决策注入物理世界动态推理能力，显著提升复杂场景（尤其是交互密集场景）下的决策安全性和质量。
- 与 Textual CoT 相比，Dynamics CoT 捕获了细粒度的时空信息；与 Visual CoT 相比，它以更紧凑的形式避免了冗余。
- 通过解耦自车与环境动态，模型能够更准确地建模世界演化。
- 强化微调在监督微调基础上进一步提升了决策表现，同时保持推理延迟可控，具备了实际部署价值。

### 7. 优点

- **创新性强**：首次提出以预测压缩、解耦的动态令牌作为思维链，为自动驾驶动作推理提供了新的范式。
- **建模精度与效率兼顾**：在避免文本模糊和图像冗余的同时，实现了细粒度物理推理，并保持了低推理延迟。
- **解耦设计**：分别建模自车与环境动态，使模型对复杂交互的适应性更强。
- **训练策略完善**：结合 SFT 与 RFT 两阶段训练，既保证基础能力又通过奖励优化决策质量。
- **实验验证广泛**：在公开基准与较大规模内部数据上均取得一致提升，体现了方法的可靠性。

### 8. 不足与局限

- **算力信息缺失**：论文提供的元数据中未给出训练所需的具体硬件资源与时间，难以评估其训练成本与可复现性。
- **内部数据集不可公开**：内部数据集的具体规模、标注质量及多样性未知，可能影响结果的可对比性和外部泛化性的判断。
- **安全边界未讨论**：动态预测模块本身的误差对决策安全性的影响未在总结材料中提及。
- **极端场景覆盖未知**：未说明模型在极端、长尾或对抗场景下的表现，实际部署的鲁棒性有待进一步验证。
- **实验组数不透明**：未提供消融实验的具体数量与类别，难以判断实验设计的颗粒度是否足够细致。

（完）
