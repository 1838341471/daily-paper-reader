---
title: "RealisMotion: Decomposed Human Motion Control and Video Generation in the World Space"
title_zh: RealisMotion：在世界空间中进行解耦的人体运动控制与视频生成
authors: "Jingyun Liang, Jingkai Zhou, Shikai Li, Chenjie Cao, Lei Sun, Yichen Qian, Weihua Chen, Fan Wang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/4390e29da1bd04e2a2c6241f44e910191ae4ab94.pdf"
tags: ["query:traj-pred"]
score: 7.0
evidence: 在人体运动视频生成中显式控制轨迹
tldr: 本文提出RealisMotion，将人物视频生成解耦为前景主体、背景、人类轨迹和动作模式四个独立元素，解决现有方法无法分别控制这些要素的问题。该方法在地面感知的3D世界坐标系中编辑运动，将2D轨迹反投影到3D实现轨迹控制，并支持动作与轨迹的自由组合。该框架为可控人体运动生成提供了更强的灵活性和表达力。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有视频生成方法无法分别控制前景主体、背景、人类轨迹和动作模式。
method: 构建地面感知的3D世界坐标系，将运动与外观、主体与背景、动作与轨迹解耦，并通过2D轨迹反投影到3D实现轨迹控制。
result: 实现灵活可组合的人体视频生成，支持对轨迹和动作的独立编辑。
conclusion: 解耦控制框架扩展了人体运动生成的表现力，为轨迹级生成提供新思路。
---

## Abstract
Generating human videos with realistic and controllable motions is a challenging task. While existing methods can generate visually compelling videos, they lack separate control over four key video elements: foreground subject, background video, human trajectory, and action patterns. In this paper, we propose a decomposed human motion control and video generation framework that explicitly decouples motion from appearance, subject from background, and action from trajectory, enabling flexible mix-and-match composition of these elements. Concretely, we first build a ground-aware 3D world coordinate system and perform motion editing directly in the 3D space. Trajectory control is implemented by unprojecting edited 2D trajectories into 3D with focal-length calibration and coordinate transformation, followed by speed alignment and orientation adjustment; actions are supplied by a motion bank or generated via text-to-motion methods. Then, based on modern text-to-video diffusion transformer models, we inject the subject as tokens for full attention, concatenate the background along the channel dimension, and add motion (trajectory and action) control signals by addition. Such a design opens up the possibility for us to generate realistic videos of anyone doing anything anywhere. Extensive experiments on benchmark datasets and real-world cases demonstrate that our method achieves state-of-the-art performance on both element-wise controllability and overall video quality.

---

## 论文详细总结（自动生成）

## 1. 核心问题与研究动机

- 本文针对**人体动作可控视频生成**这一挑战性任务展开研究。
- 现有生成方法虽然能生成视觉上逼真的人体视频，但**无法对视频中的四个关键要素进行独立控制**：
  - 前景主体（Foreground Subject）
  - 背景视频（Background Video）
  - 人类轨迹（Human Trajectory）
  - 动作模式（Action Patterns）
- 研究核心目标是**实现上述要素的解耦控制**，使各要素能够独立编辑并自由组合（mix-and-match），从而实现对“任何人在任何地点做任何事情”的灵活生成。

## 2. 方法论

### 2.1 核心思想

- 将人体视频生成**显式解耦**为三个维度：
  - 运动与外观解耦（motion from appearance）
  - 主体与背景解耦（subject from background）
  - 动作与轨迹解耦（action from trajectory）
- 解耦后的各要素通过统一的框架进行组合注入，实现可编辑、可组合的生成。

### 2.2 关键技术细节

- **地面感知的3D世界坐标系**：
  - 构建一个具备地面感知的3D世界坐标系。
  - 直接在3D空间中进行运动编辑，而非在2D图像平面上操作。
- **轨迹控制**：
  - 将编辑后的2D轨迹**反投影（unproject）到3D空间**。
  - 包含**焦距校准（focal-length calibration）** 与**坐标变换（coordinate transformation）**。
  - 在3D空间中完成**速度对齐（speed alignment）** 和**方向调整（orientation adjustment）**。
- **动作供给**：
  - 动作的来源有两种：预构建的**动作库（motion bank）**、或通过**文本生成动作（text-to-motion）** 方法生成。
- **模型架构与信号注入**（基于现代文本到视频扩散Transformer）：
  - 前景主体：作为 **token** 注入，参与**全注意力（full attention）** 机制。
  - 背景视频：沿**通道维度（channel dimension）** 进行拼接。
  - 运动控制（轨迹+动作）：以**加法方式（by addition）** 注入控制信号。

### 2.3 算法流程概述

1. 输入文本提示、轨迹、动作及背景信息。
2. 将2D轨迹通过焦距校准和坐标变换反投影到3D世界坐标系。
3. 在3D空间中完成速度与方向的对齐调整。
4. 从动作库或text-to-motion模块获取动作模式。
5. 将主体token注入Transformer做全注意力处理，背景沿通道拼接，运动信号以加法方式融合。
6. 扩散Transformer模型生成最终视频。

## 3. 实验设计

- 论文在**基准数据集（benchmark datasets）** 和**真实世界案例（real-world cases）** 上进行了实验验证。
- 对比对象为现有的**文本到视频生成方法**及**可控人体运动生成方法**。
- 评估指标涵盖两个维度：
  - **元素级可控性（element-wise controllability）**
  - **整体视频质量（overall video quality）**
- ⚠️ 需要注意的是，由于提供的论文文本为OpenReview页面而非完整正文，**具体数据集名称（如HumanML3D、UBC Fashion等）未在文本中明确列出**。

## 4. 资源与算力

- 提供的文本中**未明确提及**使用的GPU型号、数量、训练时长或推理资源等具体算力信息。
- 若需了解训练开销，需参考论文原文的实验章节（当前提供内容中缺失这部分细节）。

## 5. 实验数量与充分性

- 论文声称在基准数据集和真实世界案例上均取得了**目前最优（SOTA）** 的性能。
- 从元数据看，该论文被 **ICML-2026接收**，评分为 **7.0**，属于较高水平，一定程度上侧面反映了评审对其实验设计合理性的认可。
- ⚠️ 然而，由于原文文本不完整，**无法确认具体实验组数**（如做了多少个数据集的实验、消融实验的覆盖范围等）。从可获取信息判断，实验涵盖了可控性与质量两大维度，并结合真实场景验证，整体设计是较为充分的，但客观性需以完整论文内容为准。

## 6. 主要结论与发现

- 所提出的解耦控制框架在**元素级可控性**和**整体视频质量**两方面均达到了当前最优水平。
- 该框架有效解决了现有方法无法独立控制前景主体、背景、轨迹和动作的问题。
- 通过在地面感知的3D世界坐标系中进行轨迹编辑与反投影，实现了更精准的轨迹级控制。
- 解耦设计**扩展了人体运动生成的表现力**，为轨迹级可控视频生成提供了新思路。

## 7. 优点

- **解耦设计的创新性**：将主体、背景、轨迹、动作四个维度完全解耦，突破了现有方法仅能耦合控制的局限。
- **3D世界坐标系的使用**：在地面感知的3D空间中进行运动编辑，比直接在2D平面操作更符合物理实际，提升了轨迹控制的精度。
- **灵活的动作来源**：支持动作库和文本生成动作两种方式，提升了易用性和扩展性。
- **架构兼容性**：基于现代文本到视频扩散Transformer设计，信号注入方式清晰（token/通道拼接/加法），具备良好的工程可实现性。
- **生成愿景明确**：支持"anyone doing anything anywhere"的自由组合式生成，应用前景广阔。

## 8. 不足与局限

- **信息不完整**：当前可获取的论文文本仅为摘要级别的信息，缺少完整的实验细节、消融实验、定量对比表格等，因此全面评估其优势与不足存在局限。
- **对3D反投影的依赖**：轨迹控制依赖焦距校准和坐标变换，若相机参数估计不准，可能引入累积误差，影响轨迹精度。
- **地面感知假设**：方法基于地面感知的3D世界坐标系，对非地面场景（如空中视角、水下等）的适应能力可能有限。
- **运动多样性受限**：动作库和text-to-motion的质量直接影响生成结果，对未见过的复杂交互动作可能泛化不足。
- **潜在偏差风险**：真实世界案例的展示可能存在选择性，难以排除对有利结果的倾向性展示。
- **算力开销未知**：未披露训练与推理的算力需求，对于实际部署的成本评估缺乏参考。

---

（完）
