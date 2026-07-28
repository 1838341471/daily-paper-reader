---
title: "LMGenDrive: LLM Reasoning Meets World Models for End-to-End Driving"
title_zh: LMGenDrive：LLM推理与世界模型结合的端到端驾驶
authors: "Hao Shao, Letian Wang, Yang Zhou, Yuxuan Hu, Zhuofan Zong, Steven L. Waslander, Wei Zhan, Hongsheng Li"
date: 2025-09-14
pdf: "https://openreview.net/pdf?id=fSnYZZ6v49"
tags: ["query:av-pnc"]
score: 8.0
evidence: 使用LLM推理和世界模型进行端到端驾驶规划与控制
tldr: 提出LMGenDrive框架，融合大语言模型的推理能力与生成式世界模型，实现端到端自动驾驶。通过想象和评估未来场景，提升在长尾和开放世界中的泛化能力。实验表明在复杂驾驶场景下规划性能显著优于基线。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 现有自动驾驶在长尾和开放世界场景中泛化能力不足，需要结合理解与想象。
method: 将LLM推理与生成式世界模型结合，使代理能想象并评估未来动作。
result: 在多个挑战性场景中验证了该方法相比基线的显著性能提升。
conclusion: 统一理解与想象是迈向通用自动驾驶智能体的有效途径。
---

## Abstract
Recent years have witnessed remarkable progress in autonomous driving, yet generalization to long-tail and open-world scenarios remains the primary bottleneck for large-scale deployment. To address this, one line of research explores LLMs and VLMs for their vision-language understanding and reasoning capabilities, equipping AVs with the ability not only to interpret rare and safety-critical situations when generating driving actions. In parallel, another line investigates generative world models to capture the spatio-temporal evolution of driving scenes, enabling agents to imagine and evaluate possible futures before acting. Inspired by human intelligence, which seamlessly unites understanding and imagination as a hallmark of AGI, this work explores a unified model that brings these two capabilities together for autonomous driving.
We present LMGenDrive, the first framework that unifies LLM-based multimodal reasoning with generative world models for end-to-end closed-loop autonomous driving. Given multi-view camera inputs and natural-language instructions, our model generates both realistic future driving videos and corresponding control signals. By coupling an LLM with generative video capabilities, LMGenDrive gains complementary benefits: future video prediction enhances the LLM's spatio-temporal scene understanding, while the LLM itself provides reasoning and instruction-following capabilities. A progressive three-stage training strategy—ranging from vision pretraining to multi-step long-horizon driving—is proposed to further improve stability and performance.
The resulting model can also operate in two complementary modes: low-latency online planning and autoregressive offline video generation.
Experiments show that LMGenDrive significantly outperforms state-of-the-art methods on challenging closed-loop driving benchmarks, improving instruction following, spatio-temporal reasoning, and robustness to rare scenarios. 
Our work not only sets a new state-of-the-art in autonomous driving, but also demonstrates that unifying multimodal understanding and generation offers a foundational new paradigm toward achieving embodied AGI.

---

## 论文详细总结（自动生成）

# LMGenDrive 论文详细总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：现有自动驾驶系统在长尾（long-tail）和开放世界（open-world）场景下的泛化能力不足，成为大规模部署的主要瓶颈。
- **研究背景**：当前两条研究路线分别探索了（1）利用大语言模型（LLM）和视觉-语言模型（VLM）增强对罕见和安全关键场景的理解与推理能力；（2）利用生成式世界模型（generative world model）捕捉驾驶场景的时空演化，使智能体能在行动前想象和评估可能的未来。人类智能天然融合了理解与想象，而现有方法尚未将二者统一。
- **整体含义**：本文提出LMGenDrive，首次将基于LLM的多模态推理与生成式世界模型统一到端到端闭环自动驾驶框架中，旨在实现类似人类的理解与想象力结合，从而提升复杂场景下的规划性能，并探索通往具身AGI的新范式。

## 2. 论文提出的方法论

- **核心思想**：融合LLM的推理、指令跟随能力与生成式世界模型对未来场景的想象能力，形成互补增强。通过未来视频预测提升LLM的时空理解，而LLM提供高层次推理指导。
- **关键技术细节**：
  - 输入：多视角相机图像 + 自然语言指令。
  - 输出：真实的未来驾驶视频 + 相应的控制信号。
  - 架构：将LLM与生成视频能力耦合，形成端到端模型。
  - 两种运行模式：低延迟在线规划（low-latency online planning）和自回归离线视频生成（autoregressive offline video generation）。
- **训练策略**：提出了渐进式三阶段训练策略（progressive three-stage training strategy）：
  1. 视觉预训练（vision pretraining）
  2. 多步短时域规划
  3. 多步长时域驾驶（multi-step long-horizon driving）
  - 该策略旨在提升训练稳定性和最终性能。
- **算法流程（文字描述）**：
  - 输入多视角图像和指令，经视觉编码后送入LLM。
  - LLM推理输出控制信号，同时生成未来帧视频。视频预测结果反馈至LLM增强时空理解。
  - 模型在闭环仿真中执行动作，并根据预测的未来反馈调整决策。

## 3. 实验设计

- **使用的数据集/场景**：未具体说明，但提及在挑战性闭环驾驶基准（challenging closed-loop driving benchmarks）上进行评估。
- **Benchmark**：未具体命名，但从上下文推测可能包括CARLA等常见闭环仿真基准，或作者自定义的包含长尾、开放世界场景的测试集。
- **对比方法**：与最新方法（state-of-the-art methods）比较，在指令跟随、时空推理、罕见场景鲁棒性上显著超越。未列出具体基线名称。

## 4. 资源与算力

- **文中未明确说明**使用的GPU型号、数量、训练时长等具体算力信息。仅提及渐进式三阶段训练策略，但未披露训练成本。

## 5. 实验数量与充分性

- **实验数量**：摘要中未给出具体实验组数（如消融实验、不同场景测试等）。但提到在“多个挑战性场景”中验证了性能提升，并对比了SOTA。暗示可能包含多种不同复杂度的场景。
- **充分性与公平性**：
  - 充分性：仅从摘要看，缺少对消融实验（如三阶段训练的效果、视频预测模块的贡献）的详细描述，也未报告统计显著性指标。可能不够充分。
  - 客观与公平：声称“显著超越SOTA”，但未给出结果表格或详细比较设置（如是否采用相同评测指标、是否控制随机种子等）。需谨慎看待。

## 6. 论文的主要结论与发现

- LMGenDrive框架统一理解与想象，在端到端闭环自动驾驶中显著优于现有方法，在指令跟随、时空推理和罕见场景鲁棒性方面均有提升。
- 未来视频预测增强了LLM的时空场景理解，LLM提供了推理和指令跟随能力，二者互补。
- 提出的三阶段训练策略有效改善了长时域驾驶的稳定性与性能。
- 该工作不仅在自动驾驶上设立了新的SOTA，还表明了统一多模态理解与生成是实现具身AGI的基础新范式。

## 7. 优点

- **方法创新**：首次将LLM推理与生成式世界模型融合到端到端驾驶框架中，统一了理解与想象两种能力。
- **架构灵活性**：支持在线低延迟规划和离线视频生成两种模式，适用于不同部署需求。
- **训练策略**：三阶段渐进训练有助于稳定训练和长时域规划。
- **实验亮点**：在挑战性长尾场景中取得显著提升，展示了泛化能力。

## 8. 不足与局限

- **实验细节缺失**：未公开具体数据集、评估指标、基线方法名称以及结果数值，使得可重复性和客观性存疑。
- **算力不透明**：未报告训练/推理所需的计算资源，难以评估方法的实际部署成本。
- **局限推断**：
  - 当前方法可能仍依赖仿真环境，在真实世界复杂动态场景中的泛化能力有待验证。
  - 视频生成的真实性和实时性可能存在折衷，在线模式下视频预测的延迟可能影响实时控制。
  - 对于极长尾场景，LLM的幻觉或世界模型的误差可能导致错误想象与决策。
  - 实验覆盖范围不够清晰，可能缺少对安全性、可解释性等方面的系统性评估。

（完）
