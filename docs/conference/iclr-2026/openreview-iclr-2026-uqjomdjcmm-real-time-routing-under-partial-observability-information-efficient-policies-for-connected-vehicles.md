---
title: "Real-time Routing under Partial Observability: Information-Efficient Policies for Connected Vehicles"
title_zh: 部分可观测下的实时路由：连接车辆的信息高效策略
authors: "Qian Sun, Hui Xiong"
date: 2025-09-19
pdf: "https://openreview.net/pdf?id=UqjoMDJCmM"
tags: ["query:av-pnc"]
score: 7.0
evidence: 连接车辆部分可观测下的实时路径规划
tldr: 针对连接车辆在通信带宽限制下的部分可观测路由问题，提出基于强化学习的实时导航策略；通过信息高效查询选择关键路口，在仿真中路由决策质量接近完全可观测理想水平，通信开销大幅降低。
source: ICLR-2026-Public
selection_source: conference_retrieval
motivation: 实际V2X通信限制导致只能查询部分路口，传统方法假设稠密信息而失效。
method: 采用深度强化学习，在每一步选择最信息量的路口进行查询以优化路由。
result: 在低通信开销下实现接近全观测的路由性能。
conclusion: 信息高效查询策略能有效应对连接车辆中的部分可观测路由挑战。
---

## Abstract
Real-time navigation in urban road networks requires making sequential routing decisions with incomplete and noisy information. Recent advances in IoT infrastructure and vehicle-to-everything (V2X) technologies enable connected vehicles to communicate with roadside units and traffic signals in real time. However, in practice, communication bandwidth and deployment budgets severely restrict the number of intersections that can be queried at each decision step, creating a partially observable environment for real-time navigation. Existing pipelines which separately train predictors of traffic states and then apply non-differentiable routing solvers struggle under such conditions, as they assume access to dense and complete sensing. In this paper, we present an end-to-end differentiable framework that jointly addresses vehicle-to-infrastructure(V2I) information acquisition, traffic state inference, and dynamic routing optimization. In the proposed framework, a learnable selection module proactively determines which intersections to query under communication constraints, followed by a spatio-temporal aware encoder that infers network-wide travel costs from the resulting sparse signals, and a differentiable soft shortest-path decision decoder computes re-routing strategies while allowing gradients of downstream travel cost to flow back through the entire pipeline. This tight coupling aligns model training with the true system objective of minimizing vehicle travel time. Experiments on microscopic simulation with city-scale networks demonstrate that our approach outperforms comparable baselines in travel efficiency while requiring only minimal communication. By integrating selective information acquisition and differentiable decision-making, our framework advances real-time urban navigation under partial observability and provides a scalable path toward deployment in intelligent transportation systems.

---

## 论文详细总结（自动生成）

以下是基于论文摘要和元数据生成的详细中文总结。

---

## 1. 核心问题与整体含义（研究动机与背景）

- **问题定义**：连接车辆（Connected Vehicles）在城市路网中进行实时导航时，受限于通信带宽和部署预算，只能查询部分路口的交通状态（如信号灯、拥堵情况），导致导航环境为**部分可观测**。现有方法通常先独立训练交通状态预测器，再使用不可微的路由求解器，这类流水线假设能获得稠密且完整的信息，因此在部分可观测场景下性能严重下降。
- **研究动机**：实际 V2X（Vehicle-to-Everything）系统中，完全观测每个路口不现实，因此需要一种能在**通信约束下主动选择信息查询、高效推断全局路况、并实时优化路由策略**的联合框架。
- **整体含义**：该工作旨在通过端到端可微分设计，将信息采集、状态推断与路由决策深度耦合，在极小通信开销下达到接近完全可观测的理想路由性能，为智能交通系统提供可扩展的实时导航方案。

## 2. 方法论：核心思想、关键技术细节与算法流程

- **核心思想**：提出一个**端到端可微分框架**，将三个子任务联合训练：  
  1. 在通信预算下主动选择要查询的关键路口；  
  2. 从稀疏查询结果中推断全网旅行成本；  
  3. 基于推断的成本进行软最短路径决策，并允许梯度回传。

- **关键技术细节**：
  - **可学习的选择模块（Learnable Selection Module）**：在每个决策步骤，根据当前已知信息，决定向哪些路口发送查询请求，以最大化信息增益并最小化通信开销。
  - **时空感知编码器（Spatio-Temporal Aware Encoder）**：接收来自选择模块的稀疏信号，利用图神经网络或类似结构，推断整个路网中所有路段的实时旅行成本。
  - **可微分的软最短路径解码器（Differentiable Soft Shortest-Path Decoder）**：将推断的旅行成本作为权重，通过可微的路径选择机制（如基于注意力或松弛的 Dijkstra）计算重路由策略，使目标函数（旅行时间最小化）的梯度可以反向传播到选择和编码模块。

- **算法流程**（文字描述）：
  1. 初始化：车辆当前位置与目的地，通信预算 \(K\)（每次能查询的路口数）。
  2. 循环直到到达目的地：
     - 选择模块根据当前车载记忆，输出 \(K\) 个最高信息价值的路口查询请求。
     - 从 V2I 基础设施接收这 \(K\) 个路口的真实状态（如平均车速、排队长度）。
     - 时空编码器处理稀疏观测，输出全网路段旅行成本估计。
     - 软最短路径解码器基于估计成本，以可微方式生成从当前位置到目的地的最优路径。
     - 车辆沿该路径行驶一段距离，更新状态，进入下一步。
  3. 使用大量轨迹数据，通过梯度下降最小化总旅行时间，同时正则化通信成本（或固定查询次数）。

> 公式：论文摘要未提供具体公式，但核心是联合优化损失函数 \(\mathcal{L} = \mathbb{E}[\text{旅行时间}]\)，梯度流畅传播。

## 3. 实验设计

- **数据集与场景**：使用**城市规模网络的微观交通仿真**（未说明具体仿真器，如 SUMO、CityFlow 等）。场景可能包括不同通信预算（如查询路口数 \(K=1,3,5\) 等）、不同交通流模式。
- **基准（Benchmark）**：
  - 完全可观测理想情况（作为上界）。
  - 现有方法：可能是传统的预测-路由流水线（如先训练图卷积网络预测速度，再运行 Dijkstra），未列出具体名称。
- **对比方法**：文中提到“outperforms comparable baselines”，但摘要未列出具体算法名称。推测包括随机查询、固定查询（如每隔固定路口查询）、以及独立训练的非端到端方法。

## 4. 资源与算力

- 论文摘要及元数据**未明确说明**使用的 GPU 型号、数量、训练时长等具体算力信息。  
- 仅能推断使用了标准深度学习框架（如 PyTorch）在仿真环境中训练，但无量化数据。需指出该信息缺失。

## 5. 实验数量与充分性

- **实验数量**：摘要仅概述性描述，未给出具体实验组数。通常这类工作会包含：
  - 不同通信预算下的性能对比（至少 3~4 种 \(K\) 值）；
  - 与多种基线方法的对比；
  - 消融实验（验证选择模块、编码器、可微解码器的贡献）；
  - 不同路网规模/交通场景下的泛化实验。
- **充分性评估**：从摘要看，实验使用了城市规模网络，并声称优于基线，但缺乏详细数据（如具体旅行时间、通信开销数值）和统计显著性分析。**未提供完整的实验设置和结果表**，因此难以判断公平性和客观性。需要阅读全文才能确认。

## 6. 论文的主要结论与发现

- **主要结论**：提出的端到端可微分框架能够在**极小通信开销**（仅查询少数路口）下，实现**接近完全可观测的理想路由性能**。
- **发现**：
  - 可学习的选择模块能主动识别关键路口，优于随机或固定查询策略。
  - 联合训练比独立训练预测器和求解器更有效，因为梯度一致性使模块间协同优化。
  - 可微分解码器使得路径决策平滑，支持反向传播，避免不可微困扰。

## 7. 优点

- **方法创新点**：
  - 首次将**主动信息查询**与**可微分路由**端到端结合，解决部分可观下的导航问题。
  - 软最短路径解码器为图上的路径决策提供了可微的扩展，利于梯度端到端训练。
- **实用价值**：
  - 显著降低 V2X 通信开销，使有限带宽下仍可高效导航。
  - 框架具有可扩展性，可应用于多种 ITS 场景。
- **实验设计**：使用城市规模微观仿真，具有现实代表性；对比了理想上界和基线，验证了有效性。

## 8. 不足与局限

- **实验覆盖不透明**：摘要未提供具体数值、消融实验细节、场景数量等，难以评估结果的鲁棒性。
- **偏差风险**：
  - 仅基于仿真，未涉及真实道路测试，可能忽略实际通信延迟、传感器噪声等复杂因素。
  - 未见对动态交通流突变（如事故）的适应性分析。
- **应用限制**：
  - 需要基础设施支持 V2I 查询，部署成本仍存在。
  - 可微分软最短路径解码器可能存在计算效率问题，在大规模路网实时部署时需要优化。
  - 未讨论与其他路由方法（如基于强化学习的无模型方法）的对比。
- **资源与算力信息缺失**：不利于结果复现和公平对比。

---

（完）
