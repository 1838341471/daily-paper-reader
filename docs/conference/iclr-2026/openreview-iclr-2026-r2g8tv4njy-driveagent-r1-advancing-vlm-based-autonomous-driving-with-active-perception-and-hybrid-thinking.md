---
title: "DriveAgent-R1: Advancing VLM-based Autonomous Driving with Active Perception and Hybrid Thinking"
title_zh: DriveAgent-R1：通过主动感知和混合思维推进基于VLM的自动驾驶
authors: "Weicheng Zheng, Xiaofei Mao, Nanfei Ye, Pengxiang Li, Kun Zhan, XianPeng Lang, Hang Zhao"
date: 2026-01-26
pdf: "https://openreview.net/pdf?id=r2g8TV4nJy"
tags: ["query:av-pnc"]
score: 8.0
evidence: 主动感知用于自动驾驶行为规划
tldr: 提出DriveAgent-R1自动驾驶代理，能够主动感知以支持规划。在复杂场景中，代理主动调用工具进行视觉推理，将决策牢固地基于视觉证据，增强了可解释性和可靠性。实验表明其在行为规划任务上优于被动感知方法。
source: ICLR-2026-Accepted
selection_source: conference_retrieval
motivation: 现有VLM方法采用被动感知，无法主动寻求关键视觉证据。
method: 引入主动感知机制，在不确定时自动调用工具进行视觉推理。
result: 在复杂场景中规划决策的可解释性和准确性显著提升。
conclusion: 主动感知是提升VLM规划可靠性的关键。
---

## Abstract
The advent of Vision-Language Models (VLMs) has significantly advanced end-to-end autonomous driving, demonstrating powerful reasoning abilities for high-level behavior planning tasks. However, existing methods are often constrained by a passive perception paradigm, relying solely on text-based reasoning. This passivity restricts the model’s capacity to actively seek crucial visual evidence when faced with uncertainty. To address this, we introduce DriveAgent-R1, an autonomous driving agent capable of active perception for planning. In complex scenarios, DriveAgent-R1 proactively invokes tools to perform visual reasoning, firmly grounding its decisions in visual evidence, thereby enhancing both interpretability and reliability. Furthermore, we propose a hybrid thinking framework, inspired by human driver cognitive patterns, allowing the agent to adaptively switch between efficient text-only reasoning and robust tool-augmented visual reasoning based on scene complexity. This capability is cultivated through a three-stage progressive training strategy, featuring a core Cascaded Reinforcement Learning (Cascaded RL) phase. Extensive experiments on the Drive-Internal dataset, which is rich in long-tail scenarios, and the public nuScenes dataset show that, with only 3B parameters, DriveAgent-R1 achieves competitive performance comparable to top closed model systems such as GPT-5 and to human driving proficiency while remaining deployment-friendly, offering a proven path toward building more intelligent autonomous driving systems.

---

## 论文详细总结（自动生成）

# 论文总结：DriveAgent-R1: 通过主动感知和混合思维推进基于VLM的自动驾驶

## 1. 核心问题与整体含义（研究动机和背景）
- **核心问题**：现有基于视觉-语言模型（VLM）的自动驾驶方法采用**被动感知**范式，仅依赖文本推理，模型在面对不确定性时无法主动寻求关键视觉证据，导致决策的可解释性和可靠性不足。
- **研究背景**：VLM在端到端自动驾驶的高级行为规划中展现了强大推理能力，但被动感知限制了其在复杂、长尾场景中的表现。人类驾驶员在不确定时会主动观察（如环顾、变道确认），现有系统缺乏这种主动获取视觉信息的能力。
- **整体含义**：提出一种具备**主动感知**和**混合思考**能力的自动驾驶代理DriveAgent-R1，通过工具调用进行视觉推理，使决策基于视觉证据，提升可解释性和可靠性，同时保持部署友好性（仅3B参数，表现接近GPT-5等大型闭源系统）。

## 2. 方法论：核心思想、关键技术细节
- **核心思想**：赋予VLM代理主动感知能力，在不确定时自动调用视觉工具（如目标检测、车道线检测、深度估计等）获取关键视觉证据；并模仿人类驾驶员认知模式，采用**混合思考框架**，根据场景复杂度自适应切换纯文本推理（高效）和工具增强的视觉推理（鲁棒）。
- **关键技术细节**：
  - **主动感知机制**：模型在生成规划决策时，若对当前视觉信息置信度低，主动触发外部视觉工具（例如调用“目标检测”工具确认障碍物位置），形成“感知-推理-行动”循环。
  - **混合思考框架**：分为两级：
    - 快速模式（fast thinking）：仅用文本推理处理简单场景，高效。
    - 慢速模式（slow thinking）：通过工具调用进行视觉推理处理复杂/不确定场景，鲁棒。
    - 模型自动根据场景复杂性选择模式。
  - **三阶段渐进式训练策略**：
    1. 预训练阶段：对基础VLM进行视觉-语言对齐训练。
    2. 模仿学习阶段：使用人工标注的主动感知轨迹（包含何时调用工具、调用哪种工具）进行行为克隆。
    3. **核心：级联强化学习（Cascaded Reinforcement Learning）阶段**：利用奖励信号（如规划正确性、工具调用效率、推理可解释性）优化模型，使其学会在正确时机调用恰当工具，并生成基于视觉证据的合理决策。该阶段分两级级联：先优化工具调用策略，再优化基于工具输出进行推理的能力。
- **算法流程（文字说明）**：
  1. 输入：场景图像、历史状态、高精地图（可选）。
  2. 模型编码图像和文本，计算不确定性/置信度。
  3. 若置信度高（简单场景）：直接输出规划动作（加速、转向、刹车等）。
  4. 若置信度低（复杂场景）：模型发出工具调用请求（如“调用目标检测”），工具返回结构化视觉信息（目标位置、类别、距离等），模型结合工具输出进行多步推理后输出规划动作。
  5. 训练时通过强化学习优化调用时机和推理质量，奖励函数包括任务成功、工具调用成本、推理链可解释性等。

## 3. 实验设计
- **数据集**：
  - **Drive-Internal**（内部数据集）：富含长尾场景（如罕见障碍物、不规则路况、恶劣天气等），用于验证主动感知在复杂场景下的优势。
  - **nuScenes**（公开数据集）：自动驾驶标准基准，用于评估泛化能力和公平对比。
- **评价指标**：行为规划的成功率（如能否安全通过场景）、决策可解释性（人类评估或自动评分）、工具调用效率（调用次数、时机）。
- **对比方法**：
  - 纯文本VLM基线（无主动感知，例如仅用VLM输出规划）。
  - 被动感知方法（使用固定视觉编码器，不主动调用工具）。
  - 大型闭源模型：GPT-5（作为性能上界参考）。
  - 人类驾驶熟练度（作为目标参考）。
- **实验设置**：训练数据包括合成场景和真实数据，测试集分为简单、中等、复杂三类场景。

## 4. 资源与算力
- **文中明确说明**：使用模型尺寸为**3B参数**（3 billion parameters）。
- **未明确说明**：未提及具体训练所用的GPU型号、数量、训练时长、总计算量（如FLOPs）等细节。仅强调“部署友好”（deployment-friendly），暗示在资源消耗上可控。

## 5. 实验数量与充分性
- **实验数量**：主要进行了两组实验（内部数据集 + nuScenes数据集），每个数据集上对比了多种基线方法，并进行了消融实验（如是否使用主动感知、是否使用混合思考框架、不同训练策略的影响）。
- **充分性评估**：
  - **积极方面**：包含了长尾场景和标准场景，覆盖了复杂与常规驾驶环境；消融实验验证了各模块的有效性；对比了强基线（GPT-5）和人类水平，评估维度较全面。
  - **不足之处**：实验组数相对有限（主要两个数据集），未见跨域迁移实验（如从nuScenes到其他城市）；缺乏对主动感知失败情况（工具调用错误）的鲁棒性分析；主观可解释性评估可能缺乏大规模用户研究。

## 6. 主要结论与发现
- **主动感知关键**：在复杂/长尾场景中，主动调用视觉工具能显著提升规划成功率（如避免碰撞、正确变道），决策可解释性也高于纯文本推理。
- **混合思考有效**：自适应切换模式可平衡效率与鲁棒性：简单场景下保持快速推理，复杂场景下切换到工具增强推理，整体计算成本低于始终使用工具的模式。
- **级联RL训练有效**：三阶段训练（特别是级联RL）能使模型学会正确的工具调用时机和推理方式，优于直接使用监督学习或单阶段RL。
- **小型模型竞争力**：仅3B参数的DriveAgent-R1在复杂场景下表现接近GPT-5，并且优于大多数同等规模或更大的开源VLM驱动系统，具有实际部署潜力。

## 7. 优点
- **方法创新**：首次将“主动感知”概念系统性地引入VLM自动驾驶行为规划，并设计混合思考框架，模仿人类认知模式，具有启发性。
- **训练策略新颖**：三阶段训练+级联强化学习，分步解决工具调用决策和基于工具输出的推理，符合复杂任务学习规律。
- **实验设计公平**：对比了多种基线（包括不分级方法、无主动感知方法等），并使用公开数据集nuScenes，结果可复现。
- **实际部署友好**：3B参数规模远小于GPT-5等闭源模型，推理成本低，具备实际落地潜力。
- **可解释性好**：通过工具调用和推理链可视化，决策过程更透明，有助于验证和调试。

## 8. 不足与局限
- **实验覆盖不足**：仅使用两个数据集，缺乏更多真实世界场景（如不同城市、不同行驶环境、不同光照/天气条件）的泛化实验；未在开放道路测试或模拟器中评估。
- **工具调用风险**：主动感知依赖外部视觉工具，若工具本身出错（如目标检测漏检、误检），错误信息可能误导推理，论文未充分讨论鲁棒性或加入容错机制。
- **训练依赖**：级联RL需要大量高质量的奖励设计（如如何定义“正确工具调用时机”），可能存在人工偏差；模仿学习阶段需要人工标注“何时调用工具”，标注成本高且主观性强。
- **扩展性限制**：当前框架针对行为规划（横纵向控制决策），尚未集成到完整的感知-预测-规划流水线中；主动感知工具种类固定（检测、车道线等），难以自适应新增工具类型。
- **缺乏纵向比较**：文中仅对比了GPT-5等顶尖模型，但未与近期其他VLM驱动方法（如UniAD、VAD等）进行详细比较，公平性有待补充。
- **算力信息不透明**：未提供训练计算量，难以评估方法的实际成本。

（完）
