---
title: Distilling Multi-modal Large Language Models for Autonomous Driving
title_zh: 面向自动驾驶的多模态大语言模型蒸馏
authors: "Hegde, Deepti, Yasarla, Rajeev, Cai, Hong, Han, Shizhong, Bhattacharyya, Apratim, Mahajan, Shweta, Liu, Litian, Garrepalli, Risheek, Patel, Vishal M., Porikli, Fatih"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Hegde_Distilling_Multi-modal_Large_Language_Models_for_Autonomous_Driving_CVPR_2025_paper.pdf"
tags: ["query:av-pnc"]
score: 9.0
evidence: 将大模型知识蒸馏至视觉规划器用于自动驾驶安全运动规划
tldr: 大型语言模型作为规划器在自动驾驶长尾场景中表现出色，但推理成本高。本文提出DiMA，将多模态大模型的知识通过代理任务蒸馏至纯视觉端到端规划器。联合训练使场景编码器学到结构化语义表示。在nuScenes上，该方法在保持高效的同时显著提升了规划的安全性，尤其在罕见场景下。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-hegde-distilling-multi-modal-large-language-models-for-autonomous-driving-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 829, \"height\": 695, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-hegde-distilling-multi-modal-large-language-models-for-autonomous-driving-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1608, \"height\": 613, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-hegde-distilling-multi-modal-large-language-models-for-autonomous-driving-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 693, \"height\": 713, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-hegde-distilling-multi-modal-large-language-models-for-autonomous-driving-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1805, \"height\": 559, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-hegde-distilling-multi-modal-large-language-models-for-autonomous-driving-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1802, \"height\": 1049, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-hegde-distilling-multi-modal-large-language-models-for-autonomous-driving-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 857, \"height\": 871, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-hegde-distilling-multi-modal-large-language-models-for-autonomous-driving-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1811, \"height\": 726, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-hegde-distilling-multi-modal-large-language-models-for-autonomous-driving-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1774, \"height\": 420, \"label\": \"Table\"}]"
motivation: LLM规划器推理成本高，视觉规划器缺乏常识知识。
method: 设计代理任务将多模态LLM知识蒸馏到视觉规划器的场景编码器中。
result: 蒸馏后的视觉规划器在长尾场景规划安全性接近LLM水平，推理更快。
conclusion: 知识蒸馏有效结合了LLM的常识与视觉规划器的效率。
---

## Abstract
Autonomous driving demands safe motion planning, especially in critical "long-tail" scenarios. Recent end-to-end autonomous driving systems leverage large language models (LLMs) as planners to improve generalizability to rare events. However, using LLMs at test time introduces high computational costs. To address this, we propose DiMA, an end-to-end autonomous driving system that maintains the efficiency of an LLM-free (or vision-based) planner while leveraging the world knowledge of an LLM. DiMA distills the information from a multi-modal LLM to a vision-based end-to-end planner through a set of specially designed surrogate tasks. Under a joint training strategy, a scene encoder common to both networks produces structured representations that are semantically grounded as well as aligned to the final planning objective. Notably, the LLM is optional at inference, enabling robust planning without compromising on efficiency. Training with DiMA results in a 37% reduction in the L2 trajectory error and an 80% reduction in the collision rate of the vision-based planner, as well as a 44% trajectory error reduction in long-tail scenarios. \ours also achieves state-of-the-art performance on the nuScenes planning benchmark.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **问题**：自动驾驶中的“长尾场景”（如三点转向、超车等罕见事件）对规划安全性构成严峻挑战。基于大语言模型（LLM）的规划器虽然能利用互联网规模知识提升泛化能力，但在推理时引入极高计算成本，限制了实际部署。而传统的纯视觉端到端规划器虽然高效，但缺乏常识知识，在长尾场景下表现不佳。
- **动机**：如何在不牺牲效率的前提下，将多模态大语言模型（MLLM）的世界知识“蒸馏”到纯视觉规划器中，使后者在推理时无需依赖LLM，同时保持鲁棒性。

## 2. 方法论

### 核心思想
- **DiMA**：通过联合训练一个共享的场景编码器（Scene Encoder），将MLLM的知识蒸馏到视觉规划器中，使视觉规划器学到语义更丰富、与规划目标更对齐的结构化场景表示。

### 关键技术细节
- **视觉规划器**：基于VAD或UniAD，包含场景编码器（输出结构化BEAM token嵌入：Bird's-Eye-View、Ego、Agent、Map）与规划Transformer。
- **MLLM**：包括适应层（Q-Former）、LLM（基于LLaVA-v1.5-7B）以及多个任务头。
- **蒸馏与联合训练**：
  - 场景编码器同时作为视觉规划器的特征提取器和MLLM的 tokenizer。
  - 两阶段训练：先预训练视觉规划器60 epochs，再联合训练30 epochs（使用LoRA微调LLM）。
- **设计四个监督任务**：
  1. **视觉问答（VQA）**：训练MLLM进行场景问答（交叉熵损失）。
  2. **特征蒸馏**：将MLLM中ego-token的隐层特征与视觉规划Transformer的特征通过KL散度对齐。
  3. **代理任务**（surrogate tasks）：
     - **掩码token重建**：随机遮罩BEV token，让MLLM重建（L2损失）。
     - **未来BEV预测**：预测未来帧的BEV token（L2损失）。
     - **场景编辑**：增删agent并构造对应的问答对，增强对交互的理解。
- **损失函数**：总损失 = 规划损失（来自视觉规划器） + LLLM + Ldistill + Lrecon + Lfuture。

## 3. 实验设计

- **数据集**：
  - 主要规划数据集：nuScenes（开放循环规划），约28k样本（train/val 22k/6k）。
  - VQA数据：DriveLM（4k子样本、300k QA对），以及用Llama3自动生成补充数据。
- **基准与评估协议**：
  - 采用两种评估策略：
    - **标准化评估**（来自PARA-Drive）：统一处理L2误差平均方式及碰撞率，用于全验证集和“targeted”子集（转向场景）。
    - **VAD评估**（原始VAD协议）：用于与未公开发布代码的方法比较。
  - 长尾场景：三个手工选择的子集（三点转向、停止后起步、超车），其中“三点转向”为零样本场景。
- **对比方法**：
  - 视觉规划器：UniAD、VAD（Tiny/Base）、PARA-Drive、AD-MLP。
  - MLLM规划器：TOKEN、DriveVLM、OmniDrive（比较时使用VAD评估）。

## 4. 资源与算力

- **文中未明确说明**使用的GPU型号、数量及具体训练时间。只提及训练配置：两阶段训练（60 epochs预训练 + 30 epochs联合训练），MLLM的LLM部分使用LoRA微调（LoRA rank未提及）。
- **硬件推断**：由于使用了LLaVA-v1.5-7B模型，推测需要较大显存（如A100或V100），但本文未量化。规划器不同变体的推理延迟给出（如VAD-Tiny 59.5ms，VAD-Base 224.3ms，DiMA-Dual 286ms），表明视觉分支高效。

## 5. 实验数量与充分性

- **实验数量**：主要包括三个主要表格（表1-3）和消融实验表（表4），以及定性结果（图1、4）。
  - 表1（标准化评估）：包含全验证集和targeted子集，对比5种baseline和多个DiMA变体。
  - 表2（VAD评估）：对比7种以上方法，包括近期MLLM方法（DriveVLM、OmniDrive）。
  - 表3（长尾场景）：三个子集上对比VAD、PARA-Drive、TOKEN及DiMA变体（含MLLM分支）。
  - 表4（消融实验）：8组实验逐步验证每个组件（场景标记种类、蒸馏、各代理任务）的贡献。
- **充分性**：实验范围覆盖了通用场景、困难场景（targeted）、长尾零样本场景；对比方法包括当时的主要SOTA；消融设计系统地检验了设计决策；使用了两种评估协议以确保与其他工作的公平比较（解决了以往评估不一致问题）。
- **公平性**：作者明确指出使用标准化评估以消除不一致，并与TOKEN（开放了代码）和PARA-Drive进行了直接对比。对于未开源的方法（DriveVLM等），采用原始VAD评估协议对比已发布的数据。

## 6. 主要结论与发现

- **性能提升**：训练DiMA后，视觉规划器的L2轨迹误差降低37%，碰撞率降低80%；在长尾场景中轨迹误差降低44%。
- **与SOTA对比**：DiMA在nuScenes规划基准上达到最佳性能，同时推理时不需LLM（比TOKEN等纯LLM方法更高效、更准确）。
- **零样本能力**：在“三点转向”这种未见过的场景中，DiMA显著优于基线，且MLLM分支可进一步提升性能（DiMA-Dual）。
- **蒸馏有效性**：联合训练和代理任务使场景表示更富语义、更鲁棒，消融实验证实每个组件均有贡献。

## 7. 优点

- **方法设计**：
  - 创新性地将视觉规划器的结构化BEAM token作为MLLM的输入（场景编码器可训练），优于之前冻结编码器的做法。
  - 设计的代理任务（掩码重建、未来预测、场景编辑）高效地将时空推理能力从LLM转移到视觉编码器。
  - 推理时LLM可弃用，兼顾效率与鲁棒性。
- **实验设计**：
  - 同时采用标准化评估和原始评估，确保公平性。
  - 专门设置长尾场景评估，并包含零样本测试（三点转向）。
  - 消融实验逐步累积，清晰展示了各组件贡献。
- **实用价值**：在不增加推理开销的前提下大幅提升安全性，适合实际部署。

## 8. 不足与局限

- **数据集局限**：仅在nuScenes开放循环规划上评估，未在闭环仿真（如CARLA）或其他更大规模数据集（如Waymo）上验证。闭环评估能更真实反映规划器鲁棒性。
- **计算资源信息缺失**：未公开训练所需GPU型号、数量及时长，不利于复现和算力估算。
- **VQA数据依赖**：部分QA对通过Llama3自动生成，可能存在噪声或偏差，未量化对规划性能的影响。
- **蒸馏损失权重**：未详细讨论损失权重设定，缺乏敏感性分析。
- **MLLM分支的额外开销**：虽然视觉分支高效，但DiMA-Dual混合推理需要LLM，延迟增加（286ms vs 59.5ms），可能限制实时性。
- **泛化性**：未讨论方法迁移到其他任务（如换道、交叉口）的难度。

（完）
