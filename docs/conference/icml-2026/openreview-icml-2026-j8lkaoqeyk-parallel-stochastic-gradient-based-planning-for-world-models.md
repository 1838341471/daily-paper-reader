---
title: Parallel Stochastic Gradient-Based Planning for World Models
title_zh: 基于世界模型的并行随机梯度规划
authors: "Michael Psenka, Michael Rabbat, Aditi S. Krishnapriyan, Yann LeCun, Amir Bar"
date: 2026-04-30
pdf: "https://openreview.net/pdf/b31649eeff6a45e3560c2a6b57d868d9e5a2287e.pdf"
tags: ["query:av-pnc"]
score: 6.0
evidence: 基于世界模型的随机梯度规划器，可应用于自动驾驶规划
tldr: 利用世界模型从视觉输入进行规划时，搜索空间巨大且非结构化。本文提出一种并行随机梯度规划器，将状态视为优化变量并施加软动力学约束，通过引入随机性和梯度修正实现长时域控制任务的高效求解。该方法在多种视觉控制任务中取得了优异性能，其优化框架可为基于学习世界模型的自动驾驶规划提供新思路。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 视觉世界模型用于规划时面临搜索空间巨大和非结构化的问题。
method: 提出并行随机梯度规划器，将状态作优化变量加软约束，引入随机性和梯度修正。
result: 在长时域视觉控制任务上取得高效性能。
conclusion: 优化框架可为基于世界模型的自动驾驶规划提供新思路。
---

## Abstract
World models simulate environment dynamics from raw sensory inputs like video. However, using them for planning can be challenging due to the vast and unstructured search space. We propose a robust and highly parallelizable planner that  leverages the differentiability of the learned world model for efficient optimization, solving long-horizon control tasks from visual input. Our method treats states as optimization variables ("virtual states") with soft dynamics constraints, enabling parallel computation and easier optimization. To facilitate exploration and avoid local optima, we introduce stochasticity into the states. To mitigate sensitive gradients through high-dimensional vision-based world models, we modify the gradient structure to descend towards valid plans while only requiring action-input gradients. Our approach can be viewed as a stochastic version of a non-condensed or collocation-based optimal controller. We provide theoretical justification and experiments on video-based world models, where our resulting planner outperforms existing planning algorithms like the cross-entropy method (CEM) and vanilla gradient-based optimization (GD) on long-horizon experiments, both in success rate and time to convergence.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

*   **核心问题**：如何高效利用基于原始视觉输入（如视频）学习到的世界模型进行长时域规划。世界模型能够模拟环境动态，但其带来的搜索空间巨大且高度非结构化，传统规划方法难以有效处理。
*   **研究动机与背景**：
    *   世界模型在从视觉信号中学习环境动态方面展现出潜力，但将其用于规划仍极具挑战。
    *   现有基于采样的方法（如交叉熵方法CEM）或朴素的梯度优化方法在长时域视觉控制任务上存在成功率低、收敛慢等问题。
    *   需要一种能够充分利用学习模型可微性，同时规避高维视觉梯度敏感性问题的规划器。

### 2. 论文提出的方法论

*   **核心思想**：将规划问题转化为一个可并行求解的随机梯度优化问题。
*   **关键技术细节与算法流程**：
    *   **状态作为优化变量（“虚拟状态”）**：与传统的仅优化动作序列不同，本方法直接将未来一段时间内的系统状态作为优化变量，从而允许并行计算和更宽松的优化空间。
    *   **软动力学约束**：不强制执行硬性的动力学约束（即下一状态必须严格等于世界模型预测），而是在优化目标中施加软约束，使状态向满足动力学的解区域下降。
    *   **引入随机性**：向状态变量中注入随机扰动，以促进探索并避免陷入局部最优。
    *   **梯度结构修正**：针对高维视觉世界模型反向传播梯度敏感的问题，修改梯度下降方向，使其能够朝有效计划下降，且**仅需动作输入对应的梯度**，无需完整展开所有层的梯度，从而稳定优化过程。
    *   **理论视角**：该方法可被视为一种随机版本的、非压缩或基于配置点的（non-condensed / collocation-based）最优控制器。

### 3. 实验设计

*   **数据集/场景**：
    *   基于视频的世界模型控制的多种长时域任务环境（具体环境名称摘要未列出，但明确为“vision-based world models”和“long-horizon experiments”）。
*   **Benchmark与对比方法**：
    *   对比方法包括：
        *   交叉熵方法（CEM）
        *   朴素的基于梯度的优化（GD，vanilla gradient-based optimization）
    *   评估指标：任务成功率（success rate）和收敛时间（time to convergence）。

### 4. 资源与算力

*   **文中未明确说明**：提供的摘要和元数据中均未提及所使用的GPU型号、数量、训练总时长或硬件消耗等算力信息。

### 5. 实验数量与充分性

*   **实验规模**：
    *   摘要未给出具体的实验组数。若归入不同任务、不同时域长度及消融研究，组数难以确定，但提到“多种视觉控制任务”和与两个基线方法的对比。
*   **充分性、客观性与公平性判断**：
    *   **充分性**：摘要仅呈现了与CEM和GD的对比结论，未展示消融实验内容，无法判断组件剥离实验的完整性。
    *   **客观性与公平性**：指标采用通用的成功率与收敛时间，对比对象为业内常见基线（CEM、GD），具备一定公平性，但未说明超参数调优范围等细节。

### 6. 论文的主要结论与发现

*   所提出的并行随机梯度规划器在长时域视觉世界模型控制任务上，**成功率和收敛速度均显著优于**交叉熵方法（CEM）和朴素的梯度优化方法。
*   仅需动作输入梯度、引入随机性和软约束的状态优化框架，能有效解决伴随高维视觉模型的规划难题，为基于学习世界模型的规划提供了新的高效实现路径。

### 7. 优点

*   **并行度高**：通过将状态设为优化变量，天然支持高度并行计算，提升效率。
*   **规避梯度病态**：创新性地修正梯度结构，仅依赖动作相关梯度，降低了对复杂视觉主干梯度的敏感性，使优化更稳定。
*   **理论与实验结合**：既有随机最优控制视角的理论支撑，又有在视觉世界模型上的实验验证。
*   **解决长时域任务**：方法在设计上能够应对长时域控制中出现的搜索空间巨大和局部最优问题。

### 8. 不足与局限

*   **算力透明度**：未披露任何算力消耗信息，复现成本和效率的可评估性受限。
*   **实验覆盖未知**：摘要中仅提及与CEM、GD的比较，未说明是否与其他现代规划方法（如MPPI、模型预测控制变体等）进行了对比；缺少对复杂度更高或随机性更强的环境的实验描述。
*   **偏差风险**：未提及随机种子数量或统计显著性，成功率可能受特定初始化或世界模型质量影响。
*   **应用限制**：对世界模型的可微性有依赖；软约束设计可能在高精度安全关键任务中引入满足度风险。

（完）
