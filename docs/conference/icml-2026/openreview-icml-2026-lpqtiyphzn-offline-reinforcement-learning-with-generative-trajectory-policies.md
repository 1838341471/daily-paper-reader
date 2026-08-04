---
title: Offline Reinforcement Learning with Generative Trajectory Policies
title_zh: 基于生成轨迹策略的离线强化学习
authors: "Xinsong Feng, Leshu Tang, Chenan Wang, Haipeng Chen"
date: 2026-04-30
pdf: "https://openreview.net/pdf/6a56154b18763b639b76a9c407f935e2d860c792.pdf"
tags: ["query:av-pnc"]
score: 6.0
evidence: 面向离线强化学习的生成轨迹策略，捕获多模态行为，与轨迹规划相关
tldr: 本文针对离线强化学习中生成轨迹策略的两难问题：扩散策略迭代缓慢而一致性策略性能受损，提出统一视角，将扩散、流匹配与一致性模型看作连续时间生成轨迹的特例。基于该视角构建的方法可在保持多模态行为表达能力的同时提升生成效率，并在实验中展示出与现有方法相比更优的性能-速度权衡，对自动驾驶等轨迹生成场景具有启发意义。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 生成式策略在离线RL中面临迭代模型慢与单步模型性能差的权衡。
method: 将扩散、流匹配和一致性模型统一为连续时间生成轨迹视角，提出桥接迭代与单步生成的策略框架。
result: 在保留多模态建模能力的同时提升采样效率与性能。
conclusion: 为离线RL中的轨迹生成提供统一视角，可用于自动驾驶决策控制。
---

## Abstract
Generative models have emerged as a powerful class of policies for offline reinforcement learning (RL) due to their ability to capture complex, multi-modal behaviors. 
However, existing methods face a stark trade-off: slow, iterative models like diffusion policies are computationally expensive, while fast, single-step models like consistency policies often suffer from degraded performance. 
In this paper, we demonstrate that it is possible to bridge this gap.
The key to moving beyond the limitations of individual methods, we argue, lies in a unifying perspective that views modern generative models—including diffusion, flow matching, and consistency models—as specific instances of learning a continuous-time generative trajectory governed by an Ordinary Differential Equation (ODE).
This principled foundation provides a clearer design space for generative policies in RL and allows us to propose *Generative Trajectory Policies* (GTPs), a new and more general policy paradigm that learns the entire solution map of the underlying ODE.
To make this paradigm practical for offline RL, we further introduce two key theoretically principled adaptations. 
Empirical results demonstrate that GTP achieves state-of-the-art performance on D4RL benchmarks -- it significantly outperforms prior generative policies, achieving perfect scores on several notoriously hard AntMaze tasks.

---

## 论文详细总结（自动生成）

以下总结基于提供的论文元数据与摘要内容。由于正文未完整提供，部分细节只能依据摘要和元数据信息进行概括。

## 1. 核心问题与整体含义（研究动机与背景）

- 离线强化学习（Offline RL）中，生成模型因其能够捕捉复杂、多模态的行为分布，已成为一类强大的策略表示方法。
- 现有方法存在明显权衡：
  - **迭代式生成模型**（如扩散策略）性能较好，但计算开销大、采样速度慢；
  - **单步生成模型**（如一致性策略）速度快，但往往性能下降。
- 论文的核心问题是：**如何弥合“慢但性能好”与“快但性能差”之间的鸿沟**。
- 关键观点：现代生成模型（扩散模型、流匹配、一致性模型）本质上是学习一个由**常微分方程（ODE）控制的连续时间生成轨迹**的特例。这一统一视角为设计生成式策略提供了更清晰的设计空间。
- 整体含义：基于该视角，论文提出 **Generative Trajectory Policies（GTPs，生成轨迹策略）**，一种更通用的策略范式，试图同时获得多模态表达能力与高效采样的优势。

## 2. 提出的方法论

- **核心思想**：GTP 不局限于某一种具体的生成模型，而是学习底层 ODE 的**完整解映射（solution map）**，从而统一并超越扩散、流匹配和一致性模型。
- **技术细节**（根据摘要可提炼的内容）：
  - 将扩散、流匹配、一致性模型视为连续时间生成轨迹的特例，建立统一的理论基础；
  - 提出 GTP 范式，直接建模生成轨迹的完整演化；
  - 为使该范式在离线 RL 中实用，论文引入了**两个具有理论依据的关键适应性设计**（具体内容摘要未展开）。
- **公式或算法流程**：摘要中未给出具体公式或伪代码。从文字描述看，GTP 学习的是 ODE 的解映射，而非仅学习从噪声到样本的单步映射或迭代去噪过程，因此可能同时兼顾迭代方法的表达力与单步方法的效率。

## 3. 实验设计

- **基准（Benchmark）**：使用 D4RL 标准基准。
- **任务/场景**：特别提到了 AntMaze 系列任务，且指出这些任务“非常困难”。
- **对比方法**：与先前多种生成式策略方法进行对比，但摘要未列出具体基线名称。
- **评估指标**：未在摘要中明确给出，但结合 D4RL 惯例，应为归一化得分（normalized score）。
- **实验覆盖**：摘要仅提到 D4RL 和 AntMaze，未说明是否包含 Gym-MuJoCo、Adroit、Kitchen 等其他 D4RL 域。

## 4. 资源与算力

- 提供的摘要和元数据中**未说明**使用的 GPU 型号、数量、训练时长或计算资源规模。
- 因此无法对算力开销进行评估，只能指出该信息在论文中可能包含于实验设置部分，但不在本文提供的文本范围内。

## 5. 实验数量与充分性

- **数量**：从摘要看，论文至少进行了 D4RL 基准上的对比实验，并突出了 AntMaze 上的结果。但没有提供具体的任务数量、重复实验次数等信息。
- **充分性**：
  - 摘要声称“显著优于先前生成式策略”并“在多个 AntMaze 任务上取得完美分数”，说明实验结果具有一定的说服力；
  - 但缺少对消融实验、不同超参数敏感性、运行时间/吞吐量对比以及更多任务域的详细描述；
  - 基于现有材料，**无法完全判断实验是否充分、公平**，需要阅读论文全文（尤其是实验设置和基线实现细节）才能评估。

## 6. 主要结论与发现

- GTP 在 D4RL 基准上取得了**最先进的性能（state-of-the-art）**。
- 相比先前的生成式策略，GTP 有显著提升。
- 在多个公认困难的 **AntMaze 任务上获得了满分/完美分数**。
- 这说明“迭代性能优势”与“单步效率优势”之间的权衡可以通过统一生成轨迹的视角得到有效缓解。

## 7. 优点（方法与实验设计的亮点）

- **理论视角新颖**：将扩散、流匹配和一致性模型统一为 ODE 驱动的连续时间生成轨迹，提供了更清晰、更一般化的设计空间。
- **方法通用性强**：GTP 作为更通用的策略范式，有可能兼容并改进现有多种生成式策略。
- **性能与效率兼得**：实验结果证明 GTP 在多模态表达能力与生成效率之间取得了更优的平衡。
- **结果有冲击力**：在 AntMaze 这类长期决策、稀疏奖励的困难任务上获得完美分数，是离线 RL 中较有说服力的结果。

## 8. 不足与局限

- **内容不完整**：由于仅提供了摘要和元数据，无法详细评估方法的具体设计（如两个理论适应性修改的具体形式）、损失函数、网络结构等。
- **实验细节缺失**：未提供完整的基准覆盖范围、消融实验、运行时间比较、超参数选择等，因此无法判断实验的全面性和公平性。
- **算力信息未说明**：无法评估其实际计算成本。
- **应用限制**：论文主要面向离线 RL 的轨迹策略学习，虽然元数据提示其与自动驾驶轨迹规划相关，但摘要本身并未直接验证在真实自动驾驶场景中的效果。
- **潜在偏差风险**：D4RL 基准本身存在任务多样性有限、数据分布固定等问题，单一基准上的 SOTA 结果未必能完全代表真实世界复杂环境中的泛化能力。

（完）
