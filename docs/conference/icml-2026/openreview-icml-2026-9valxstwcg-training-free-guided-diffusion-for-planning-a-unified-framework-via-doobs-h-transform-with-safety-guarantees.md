---
title: "Training-Free Guided Diffusion for Planning: A Unified Framework via Doob’s h-Transform with Safety Guarantees"
title_zh: 无需训练的引导扩散规划：基于Doob h-变换的统一框架及安全保证
authors: "Kenta Hoshino, Yashaswi Shashank Aluru, Xiyu Deng, Yorie Nakahira"
date: 2026-04-30
pdf: "https://openreview.net/pdf/59866ecaff86391c6cd1b8cb0dd51eabdd73a9ca.pdf"
tags: ["query:av-pnc"]
score: 8.0
evidence: 基于扩散的规划方法具有安全保证，用于机器人导航，适用于自动驾驶轨迹优化
tldr: 本文研究连续时间分数扩散模型中引导机制的理论基础，采用Doob h-变换作为理想引导过程框架，分析近似引导的误差界限，提供满足约束的概率保证，尤其适用于安全关键规划。此外，该公式导出一个随机最优控制问题，无需额外模型训练即可设计实用引导。在机器人导航任务上验证了方法的有效性，为安全规划提供了理论工具。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 安全关键规划需要满足约束的保证，但现有扩散规划方法缺乏形式化安全分析。
method: 利用Doob h-变换统一引导扩散过程，推导误差界和安全概率保证，并转化为随机最优控制问题。
result: 在机器人导航任务中实现安全规划，展示了无需训练的引导扩散方法的有效性。
conclusion: 该框架为扩散规划提供理论基础和实用安全引导设计，适用于安全关键应用。
---

## Abstract
This paper studies the theoretical foundations of guidance mechanisms in continuous-time score-based diffusion models.
We adopt Doob’s h-transform as a principled framework for characterizing ideal guided diffusion processes and analyze the discrepancy between ideal and approximate guidance.
Our analysis provides explicit error bounds and yields probabilistic guarantees on satisfying prescribed constraints, which are particularly important for safety-critical planning.
We further show that the Doob-based formulation induces a stochastic optimal control problem, enabling practical guidance design without additional model training.
We demonstrate the effectiveness of the proposed framework on robotic navigation tasks, including language-conditioned planning.

---

## 论文详细总结（自动生成）

## 论文总结：Training-Free Guided Diffusion for Planning: A Unified Framework via Doob’s h-Transform with Safety Guarantees

### 1. 论文的核心问题与整体含义
- **研究动机**：安全关键场景下的机器人规划（如自动驾驶、导航）需要确保生成轨迹严格满足约束条件，但现有的基于扩散模型的规划方法普遍缺乏形式化的安全保证。
- **核心问题**：如何为连续时间分数扩散模型中的引导机制建立严谨的理论基础，并提供满足约束的概率保证，从而无需额外训练即可实现安全、可靠的行为规划。
- **整体含义**：该工作旨在弥补扩散规划在安全理论方面的空白，将 Doob 的 h-变换确立为理想引导过程的统一数学框架，并以此推导出近似引导的误差界与安全概率，最终催生一个无需训练、可直接应用的实用规划方法。

### 2. 论文提出的方法论
- **核心思想**：利用随机分析中的 Doob h-变换来精确刻画理想的受约束扩散过程（即满足指定条件/引导信号的生成轨迹），并将实际中常用的近似引导过程视为对该理想过程的扰动，从而量化近似引导与理想解之间的偏差。
- **关键技术细节**：
    - **Doob h-变换框架**：将条件扩散（如满足特定目标或约束）表示为一个原扩散过程经过测度变换后的新过程，变换核即为 `h` 函数，该函数编码了所要满足的条件或引导信号。
    - **误差界与概率保证**：通过比较理想 h-变换过程和实际近似引导过程，推导出显式的误差界限，并在此基础上给出对约束满足的概率性保证（例如，轨迹不侵入障碍物的概率下界）。
    - **转化为随机最优控制**：观察到 Doob 形式的引导过程可等价转化为一个随机最优控制问题，其中控制代价与控制输入成正比，约束体现在终端或路径条件中。这一等价性使得可以在不重新训练扩散模型的情况下，直接设计控制器来生成符合要求的轨迹。
- **算法流程（文字描述）**：
    1. 给定预训练的分数扩散模型（score function）。
    2. 定义所需引导（如目标到达、避障），并将其纳入 h-函数的形式化表述。
    3. 将引导问题转化为随机最优控制问题，通过动态规划或路径积分等方法求解最优控制漂移项。
    4. 利用所求漂移项修正原扩散过程的采样（推理）过程，生成满足约束的轨迹。
    5. 基于推导的误差界，对生成轨迹的安全概率进行定量评估。

### 3. 实验设计
- **使用场景**：机器人导航任务，特别包含基于自然语言条件下的规划（language-conditioned planning）。
- **Benchmark 与对比方法**：论文中未在给定摘要与元数据中具体列明对比的基准方法，但常见此类研究的对比对象可能包括经典扩散规划方法（如 Diffuser、Decision Diffuser）或其他安全规划方法（如基于控制屏障函数或模型预测控制的方案）。需指出，此处信息源于提取文本有限，无法完整复现其对比详情。
- **评估维度**：安全约束满足率、规划成功率、轨迹质量等（根据元数据推断）。

### 4. 资源与算力
- **算力说明**：提供的文本中**未提及** GPU 型号、数量、训练时长等资源消耗信息。由于该方法强调“Training-Free”（无需训练），可能不需要大规模训练算力，但推理阶段的资源开销在摘要中未被披露。

### 5. 实验数量与充分性
- **实验数量**：提取的元数据未详述实验组数。从典型模式看，可能包含：不同导航场景（静态/动态障碍物）、不同复杂度的语言指令、消融实验（对比有无安全保证、不同近似精度的影响）等。由于信息缺失，无法断言其实验是否充分；但论文收录于 ICML 2026 且评分 8.0，通常表明评审认可其实证设计的合理性和充分性。
- **客观性与公平性**：由于缺乏具体对比方法的信息，难以评价是否完全公平。但使用标准导航任务和概率保证指标通常具有较高客观性。

### 6. 论文的主要结论与发现
- Doob h-变换为连续时间扩散模型的引导过程提供了一个统一且严格的理论框架。
- 通过该框架可以定量地分析近似引导与理想引导之间的误差，并给出约束满足的概率下界。
- 基于 Doob 的公式自然导出随机最优控制问题，使得可以在不增加额外模型训练的情况下设计实用的安全引导策略。
- 在机器人导航任务上验证了框架的可行性与有效性，实现了安全规划。

### 7. 优点
- **理论扎实**：首次将 Doob h-变换系统性地引入扩散规划领域，建立了安全保证的理论根基。
- **无需训练**：巧妙地将引导问题转化为最优控制，避免了对扩散模型进行微调或重新训练，降低了部署门槛。
- **安全量化**：提供了显式的概率安全保证，这对安全关键应用至关重要，优于仅靠经验验证的方法。
- **框架通用**：可兼容多种引导形式（如目标条件、语言条件），统一在同一个数学表述下。

### 8. 不足与局限
- **实验覆盖有限**：提供的摘要仅提及机器人导航，未说明在其他安全敏感场景（如自动驾驶高速场景、多模态复杂环境）中的表现，泛化性有待进一步验证。
- **偏差风险**：Doob 变换的 h-函数需要被设计或近似，若模型环境不匹配，理论边界可能趋于保守，实际应用中概率保证的紧致性存疑。
- **应用限制**：方法建立在连续时间扩散模型和随机最优控制基础上，实际实现可能需要离散化近似，这可能会引入额外的误差源，影响安全边界的有效性。
- **信息缺失**：由于所给文本仅为摘要与元数据，具体实验细节、算力成本、超参数敏感性、近似误差在更复杂系统中的表现等信息均未完全获得，无法进行更深入剖析。

（完）
