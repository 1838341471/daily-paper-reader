---
title: "WestWorld: A Knowledge-Encoded Scalable Trajectory World Model for Diverse Robotic Systems"
title_zh: WestWorld：面向多类机器人系统的知识编码可扩展轨迹世界模型
authors: "Yuchen Wang, Jiangtao Kong, Sizhe Wei, Xiaochang Li, Haohong Lin, Hongjue Zhao, Tianyi Zhou, Lu Gan, Huajie Shao"
date: 2026-04-30
pdf: "https://openreview.net/pdf/8810a4114256df804745ae8c7e2b3babeffa3e24.pdf"
tags: ["query:av-pnc"]
score: 8.0
evidence: 知识编码的轨迹世界模型，用于机器人动力学学习，可直接应用于自动驾驶规划与控制
tldr: 针对轨迹世界模型难以扩展到多类机器人系统的问题，WestWorld提出系统感知的混合专家模型，通过可学习系统嵌入动态组合专家，并融入物理领域知识，实现零样本泛化。在多种机器人上的动力学学习实验表明，该模型有效支持规划与控制任务，可推广至自动驾驶领域。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有轨迹世界模型无法有效扩展到大量不同动力学系统，且忽略物理结构领域知识。
method: 提出系统感知的混合专家模型（Sys-MoE），通过可学习系统嵌入路由专家，并编码领域知识。
result: 在多种机器人系统中提升了规划与控制的零样本泛化能力。
conclusion: WestWorld为跨系统轨迹学习提供了可扩展框架，是机器人规划与控制的有力工具。
---

## Abstract
Trajectory world models play a crucial role in robotic dynamics learning, planning, and control. While recent works have explored trajectory world models for diverse robotic systems, they struggle to scale to a large number of distinct system dynamics and overlook domain knowledge of physical structures. To address these limitations, we introduce *WestWorld*, a kno**W**ledge-**E**ncoded **S**calable **T**rajectory **World** model for diverse robotic systems. To tackle the scalability challenge, we propose a novel system-aware Mixture-of-Experts (Sys-MoE) that dynamically combines and routes specialized experts for different robotic systems via a learnable system embedding. To further enhance zero-shot generalization, we incorporate domain knowledge of robot physical structures by introducing a structural embedding that aligns trajectory representations with morphological information. After pretraining on 89 complex environments spanning diverse morphologies across both simulation and real-world settings, *WestWorld* achieves significant improvements over competitive baselines in zero- and few-shot trajectory prediction. Additionally, it shows strong scalability across a wide range of robotic environments and significantly improves performance on downstream model-based control for different robots. Finally, we deploy our model on a real-world Unitree Go1, where it demonstrates stable locomotion performance. The code is available at https://github.com/511205787/WestWorld.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）  
- **核心问题**：现有轨迹世界模型（trajectory world models）在多类机器人系统的动力学学习、规划和控制中存在两个关键瓶颈：  
  - **可扩展性不足**：难以应对大量不同动力学特性的系统，当系统种类增多时性能下降。  
  - **领域知识缺失**：忽略机器人物理结构（形态学）的先验知识，导致跨系统泛化能力受限。  
- **研究动机**：机器人领域正朝着通用化、跨形态的方向发展，迫切需要一种能统一建模不同机器人动力学、并支持零样本/少样本泛化的轨迹世界模型，以服务于下游规划与控制任务。  
- **整体含义**：提出WestWorld模型，通过融入物理结构知识编码和系统感知的动态专家组合机制，实现可扩展、高泛化的跨机器人轨迹预测，为多类机器人（包括自动驾驶车辆）的基于模型的规划和控制提供强力工具。

### 2. 论文提出的方法论  
- **核心思想**：构建一个知识编码的可扩展轨迹世界模型，能够根据机器人系统的不同特性动态适配模型结构，并利用物理结构先验提升泛化。  
- **关键技术细节**：  
  - **系统感知的混合专家模型（Sys‑MoE）**  
    - 为不同类型的机器人系统设计不同的“专家”子网络，通过一个可学习的系统嵌入向量（system embedding）动态路由并加权组合这些专家，从而实现跨系统扩展。  
  - **结构嵌入与领域知识融合**  
    - 引入结构嵌入（structural embedding），将机器人形态学信息（如关节数、连杆长度、构型等）映射到与轨迹表示对齐的潜在空间，使模型在学习动力学时能显式利用物理结构知识。  
  - **预训练与微调范式**  
    - 在涵盖多种形态的89个仿真和真实环境数据上进行预训练，获得具备泛化能力的基础模型；可在新系统上仅用少量数据（few-shot）甚至零样本（zero-shot）进行轨迹预测。  
- **算法流程（文字描述）**  
  1. 输入：机器人当前状态、动作序列、系统标识（或结构描述）。  
  2. 编码：通过结构编码器将机器人形态信息转为结构嵌入；将系统标识转为系统嵌入。  
  3. 动态路由：Sys‑MoE模块根据系统嵌入选择并混合多个动力学专家子网络。  
  4. 轨迹预测：结合结构嵌入和专家输出，解码生成未来状态序列。  
  5. 训练目标：最小化预测轨迹与真实轨迹的误差，同时学习系统嵌入和结构嵌入。

### 3. 实验设计  
- **数据集/场景**：  
  - **预训练数据**：89个复杂环境，覆盖多种机器人形态，包括仿真（各类构型机器人、自动驾驶场景）和真实世界数据（如Unitree Go1四足机器人）。  
- **Benchmark**：  
  - **轨迹预测**：零样本（zero-shot）和少样本（few-shot）轨迹预测精度。  
  - **下游控制**：基于模型的机器人控制性能（例如在真实机器人上的运动执行效果）。  
- **对比方法**：  
  - 竞争性基线（competitive baselines），文中未列具体名称，但应是同期先进的轨迹世界模型或多任务动力学学习方法。

### 4. 资源与算力  
- 从提供的摘要和元数据中，**未明确说明**训练所用GPU型号、数量或训练时长。  
- 若需要完整的算力信息，需查阅论文正文或附录。

### 5. 实验数量与充分性  
- **实验组数推测**：  
  - 预训练覆盖89个环境，规模较大。  
  - 至少包含零样本预测实验、少样本预测实验、下游控制实验，以及真实机器人部署实验。  
  - 很可能有消融实验（验证Sys‑MoE、结构嵌入等模块的贡献），但摘要未详细列出。  
- **充分性与公平性**：  
  - 从描述看，实验设计较全面，涵盖仿真与真实环境、预测与控制任务，且与竞争方法对比。  
  - 因缺乏具体实现细节和全面对比的数据，无法完全判断公平性，但从顶级会议接收评分（8.0）可以认为实验设计在审稿过程中被认为充分。

### 6. 论文的主要结论与发现  
- WestWorld在零样本和少样本轨迹预测任务上显著超越现有基线方法。  
- 模型展现出良好的可扩展性，能有效扩展到大量不同机器人环境中。  
- 在下游基于模型的控制任务中，WestWorld对不同机器人的控制性能有显著提升。  
- 在真实Unitree Go1四足机器人上部署，验证了模型的稳定运动控制能力，证明了其实际应用价值。

### 7. 优点  
- **新颖的系统感知MoE架构**：利用了可学习系统嵌入来动态路由专家，解决了多系统扩展难题。  
- **物理知识编码**：显式融合机器人形态学信息，提升了跨形态泛化的理论依据和实际效果。  
- **任务闭环验证**：不仅预测轨迹，还连接到规划与控制，并在真实机器人上完成了控制闭环实验，证明方法的实用性。  
- **规模化预训练**：在89个多样环境上预训练，展示了大规模机器人数据驱动模型的潜力，为通用机器人基础模型提供了路径。

### 8. 不足与局限  
- **算力与工程细节缺失**：摘要未提及训练资源消耗，大规模预训练的计算成本可能较高，对资源有限的研究者可能不友好。  
- **真实世界测试有限**：仅在单一型号的真实机器人（Unitree Go1）上进行了控制验证，其在更广泛真实系统、更复杂地形或动态环境中的鲁棒性尚待检验。  
- **形态表征的普适性**：结构嵌入依赖预定义的形态学描述，对于非刚性、变形或模块化重构的机器人系统，其适用性需进一步验证。  
- **对比评估不详**：摘要未列出所比基线的具体名称和性能数值，难以完全判断其领先幅度和公平性。  
- **领域侧重**：虽提及可推广至自动驾驶，但具体在自动驾驶规划控制（AV-PNC）场景下的实验和评测细节未披露，该方向的应用效果有待进一步验证。

（完）
