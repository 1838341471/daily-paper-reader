---
title: "Ask Less, See More: Communication-Conditioned Token Pruning for Vehicle-to-Vehicle Cooperative Autonomous Driving with Multimodal Large Language Models"
title_zh: 问得更少，看得更多：面向车-车协同自动驾驶的通信条件化令牌修剪与多模态大语言模型
authors: "Shiqi Sun, Yantao Lu, Bingkun Sun, Ning Liu, Bo Jiang, Ying Zhang, Jinchao Chen, Chenglie Du"
date: 2026-04-30
pdf: "https://openreview.net/pdf/ff44d244907cf923bf81537e76958708e1d40378.pdf"
tags: ["query:av-pnc"]
score: 10.0
evidence: 提出基于多模态大语言模型的车车协同自动驾驶框架，实现基于语言的决策。
tldr: 现有车-车协同自动驾驶中，多模态大语言模型依赖密集令牌共享，通信与推理成本高，且令牌修剪策略未考虑LiDAR空间结构与多智能体融合。本文提出V2V-CCM框架，采用双阶段协同设计，第一阶段通过通信条件化令牌修剪降低冗余，第二阶段利用空间注意力融合关键信息进行语言推理决策。在遮挡场景的实验中，V2V-CCM在保持高决策准确率的同时大幅降低通信量，为安全高效的协同自动驾驶提供了新的范式。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有V2V-MLLM依赖密集令牌共享，通信与推理成本高，令牌修剪策略忽略LiDAR空间结构与多智能体融合。
method: 提出V2V-CCM双阶段框架：第一阶段通信条件化令牌修剪，第二阶段空间注意力融合关键信息进行语言推理决策。
result: 在遮挡安全场景中实现有效决策，显著降低通信与计算开销。
conclusion: V2V-CCM为协同自动驾驶提供了高效语言推理方案，平衡性能与成本。
---

## Abstract
Multimodal Large Language Models (MLLMs) offer a promising paradigm for vehicle-to-vehicle (V2V) cooperative autonomous driving, enabling language-based decision-making in safety-critical occluded scenarios. However, existing V2V–MLLM frameworks rely on dense token-level sharing and fusion, incurring high communication and inference costs. Moreover, conventional V2V perception methods are limited to feature-sharing paradigms without language reasoning, and existing token pruning strategies fail to consider LiDAR-specific spatial structure and multi-agent fusion. To address these limitations, we propose V2V Communication-Conditioned MLLM Framework (V2V-CCM), a dual-stage cooperative communication framework that broadcasts request messages to all agents and uses them to identify redundant visual tokens. Specifically, Question Semantic Message (QSM) encodes global question intent for question-relevant token selection, while Spatial Coverage Message (SCM) summarizes LiDAR features to identify spatially redundant tokens already observed by other agents. Integrated into dual-stage frameworks, V2V-CCM substantially reduces communication and inference costs while preserving question-relevant tokens and removing spatial redundancy. Extensive experiments on V2V-QA and V2V-GoT-QA demonstrate that V2V-CCM consistently outperforms existing pruning methods and achieves state-of-the-art performance.

---

## 论文详细总结（自动生成）

抱歉，根据你提供的文本内容，这只是一个验证页面的截取，而非真正的论文全文。我只能基于元数据和摘要进行有限分析，无法深入技术细节和实验设计。

---

#### 1. 论文的核心问题与整体含义
- **研究背景**：车-车协同（V2V）自动驾驶中，多模态大语言模型（MLLM）能基于语言推理处理遮挡等安全关键场景，但现有方法依赖密集的令牌级共享和融合，通信和推理成本高昂。
- **核心问题**：传统V2V感知仅停留于特征共享，缺乏语言推理；已有的令牌修剪策略忽略了激光雷达点云的空间结构和多智能体融合特性，导致通信冗余和推理低效。

#### 2. 论文提出的方法论
- **V2V-CCM框架**：一个双阶段协同通信框架。
  - 第一阶段：广播询问消息，并基于消息条件化修剪视觉令牌。
    - **问题语义消息**：编码全局问题意图，选择与问题相关的令牌。
    - **空间覆盖消息**：总结激光雷达特征，识别已被其他智能体观测过的空间冗余令牌。
  - 第二阶段：利用空间注意力融合关键信息，进行语言推理决策。
- **核心思想**：通过“通信条件化”的令牌修剪，在保留问题相关令牌和去除空间冗余的同时，大幅降低通信与推理开销。

#### 3. 实验设计
- **数据集/场景**：*V2V-QA* 和 *V2V-GoT-QA* 数据集（摘要中提及）。
- **对比方法**：与现有令牌修剪方法进行对比（摘要未列具体方法名）。
- **性能指标**：决策准确率、通信量、计算开销等（根据摘要推断）。

#### 4. 资源与算力
- **文中未提及**：根据提供的摘要，未说明GPU型号、数量、训练时长等信息。

#### 5. 实验数量与充分性
- **实验数量**：摘要提到“大量实验”，覆盖两个相关数据集，并与现有方法进行了比较。还应有消融研究验证两个消息模块的作用（推断，但摘要未明确列出）。
- **充分性评估**：摘要声称“ consistently outperforms”和“state-of-the-art performance”，但缺乏具体数据支持，无法从摘要判断实验是否详尽。

#### 6. 论文的主要结论与发现
- V2V-CCM在遮挡安全场景中实现了有效的语言推理决策。
- 方法显著降低了通信和计算成本。
- 在保持高决策准确率的前提下，优于现有令牌修剪方法，达到了最先进水平。

#### 7. 优点
- 提出通信条件化修剪，将“问什么”和“谁已看到”融入令牌筛选，兼顾任务关联性和空间协作性。
- 双阶段设计将视觉预处理与推理分离，降低联合优化难度。
- 为V2V-MLLM的实用化（高效通信+语言推理）提供了新范式。

#### 8. 不足与局限
- **实验覆盖**：仅基于摘要，无法确定是否在真实路测数据或更多样的对抗场景中验证。
- **偏差风险**：摘要未提消融实验细节或不同天气/光照的鲁棒性，可能泛化性存疑。
- **应用限制**：依赖其他智能体的可靠响应，在通信丢包或恶意攻击下的表现未讨论。
- **算力未知**：未报告实际部署的计算资源需求。

（完）
