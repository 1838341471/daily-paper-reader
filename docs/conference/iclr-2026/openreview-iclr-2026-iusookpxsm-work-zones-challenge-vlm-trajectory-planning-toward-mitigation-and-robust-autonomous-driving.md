---
title: "Work Zones challenge VLM Trajectory Planning: Toward Mitigation and Robust Autonomous Driving"
title_zh: 施工区域挑战VLM轨迹规划：迈向缓解与鲁棒自动驾驶
authors: "YIFAN LIAO, Zhen Sun, Xiaoyun Qiu, Zixiao Zhao, Wenbing Tang, Xinlei He, Xinhu Zheng, Tianwei Zhang, Xinyi Huang, Xingshuo Han"
date: 2025-09-17
pdf: "https://openreview.net/pdf?id=iuSOOkPxSm"
tags: ["query:av-pnc"]
score: 8.0
evidence: VLM在施工区域等复杂场景下的轨迹规划
tldr: "首次系统研究视觉语言模型在施工区域中的轨迹规划能力，发现主流VLM在68.0%的情况下生成错误轨迹。通过子图挖掘和聚类分析识别失败模式，提出了有效的缓解方法。实验结果强调了VLM在复杂场景中应用的局限性。"
source: ICLR-2026-Rejected-Public
selection_source: conference_retrieval
motivation: 视觉语言模型在复杂施工区域中的轨迹规划能力尚未被探索，且存在严重失败情况。
method: 通过子图挖掘和聚类分析识别VLM失败模式，并提出缓解策略。
result: "揭示VLM在施工区域轨迹规划中68%的失败率，并验证了缓解方法的有效性。"
conclusion: 工作表明VLM在非结构化场景中需要进一步改进以实现鲁棒自动驾驶。
---

## Abstract
Visual Language Models (VLMs), with powerful multimodal reasoning capabilities, are gradually integrated into autonomous driving by several automobile manufacturers to enhance planning capability in challenging environment.
However, the trajectory planning capability of VLMs in work zones, which often include irregular layouts, temporary traffic control, and dynamically changing geometric structures, is still unexplored.
To bridge this gap, we conduct the first systematic study of VLMs for work zone trajectory planning, revealing that mainstream VLMs fail to generate correct trajectories in 68.0\% of cases.
To better understand these failures, we first identify candidate patterns via subgraph mining and clustering analysis, and then confirm the validity of 8 common failure patterns through human verification.
Building on these findings, we propose REACT-Drive, a trajectory planning framework that integrates VLMs with Retrieval-Augmented Generation (RAG). Specifically,
REACT-Drive leverages VLMs to convert prior failure cases into constraint rules and executable trajectory planning code, while RAG retrieves similar patterns in new scenarios to guide trajectory generation.
Experimental results on the ROADWork dataset show that REACT-Drive yields a reduction of around $3\times$ in average displacement error relative to VLM baselines under evaluation with Qwen2.5-VL.
In addition, REACT-Drive yields the lowest inference time ($0.58$s) compared with other methods such as fine-tuning ($17.90$s).
We further conduct experiments using a real vehicle in 15 work zone scenarios in the physical world, demonstrating the strong practicality of REACT-Drive. 
Our code and demos are available on https://sites.google.com/view/react-drive.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：视觉语言模型（VLM）凭借其强大的多模态推理能力，逐渐被引入自动驾驶领域以提升复杂环境下的规划能力。然而，**施工区域**（work zones）常包含不规则布局、临时交通控制、动态几何结构等挑战，VLM在该场景下的轨迹规划能力尚未被系统研究。
- **研究背景**：现有主流VLM（如Qwen2.5-VL等）在普通道路场景中表现良好，但在施工区域这一高复杂度、非结构化场景中，其规划可靠性未知。
- **核心问题**：VLM能否正确生成施工区域的轨迹？失败的模式是什么？如何缓解？

## 2. 论文提出的方法论：核心思想、关键技术细节
- **核心思想**：首次系统评估VLM在施工区域中的轨迹规划能力，识别失败模式，并提出结合检索增强生成（RAG）的缓解框架 **REACT-Drive**。
- **关键技术细节**：
  - **失败模式识别**：
    1. 通过**子图挖掘**（subgraph mining）从VLM生成的错误轨迹中提取候选模式。
    2. 结合**聚类分析**（clustering）对模式进行分组。
    3. 经**人工验证**确认8种常见失败模式。
  - **REACT-Drive框架**：
    1. VLM将先前的失败案例转化为**约束规则**（constraint rules）和**可执行的轨迹规划代码**（executable trajectory planning code）。
    2. 在新场景中，**检索增强生成（RAG）** 检索相似模式，引导VLM生成更可靠的轨迹。
  - **公式/算法流程**（文字说明）：输入新场景视觉数据 → RAG检索相似失败模式及对应约束规则 → VLM结合规则和代码生成轨迹 → 输出最终轨迹。未提供具体数学公式，仅描述框架流程。

## 3. 实验设计
- **数据集**：使用 **ROADWork数据集**（施工区域相关数据集）。
- **场景**：包含15个真实物理世界的施工区域场景（实车实验）。
- **Benchmark**：以主流VLM（如Qwen2.5-VL）为基线。
- **对比方法**：
  - VLM基线（直接生成轨迹）
  - 其他方法如**微调（fine-tuning）**（耗时17.90s）
  - REACT-Drive与两者对比。

## 4. 资源与算力
- **文中未明确说明**使用的GPU型号、数量、训练时长等具体算力细节。仅提及推理时间：REACT-Drive为0.58s，微调方法为17.90s。未涉及训练阶段资源。

## 5. 实验数量与充分性
- **实验组数**：
  - 在ROADWork数据集上进行了定量评估（具体测试样本数量未给出）。
  - 对比了VLM基线、微调方法，并报告了平均位移误差（ADE）降低约3倍。
  - 进行了15个真实施工区域场景的实车实验，验证实用性。
- **充分性与客观性**：
  - 实验覆盖了**定量评估**（数据集）和**定性验证**（实车），具备一定全面性。
  - 对比方法只提到一种微调方法，未与其他VLM规划框架（如端到端方法）对比，可能不够充分。
  - 失败模式验证通过了人工确认，增强了可靠性。
  - 但实验样本量、基线多样性未详细说明，存在一定偏差风险。

## 6. 论文的主要结论与发现
- **核心发现**：主流VLM在施工区域轨迹规划中**68.0%的情况下生成错误轨迹**，表明VLM在该场景下存在严重局限性。
- **失败模式**：识别并验证了8种常见失败模式（具体模式内容未在摘要中列出）。
- **缓解效果**：提出的REACT-Drive相比VLM基线，**平均位移误差降低约3倍**，推理时间仅0.58秒，远低于微调方法的17.90秒。
- **实用性**：在15个真实施工区域场景中成功应用，证明框架的强实用性。

## 7. 优点
- **创新性**：首次系统研究VLM在施工区域中的轨迹规划问题，填补了空白。
- **方法设计的亮点**：
  - 结合子图挖掘、聚类和人工验证识别失败模式，方法严谨。
  - 将RAG引入VLM轨迹规划，利用历史失败案例指导新场景，实现高效纠正。
  - 输出可执行代码和约束规则，兼顾灵活性和安全性。
- **实验亮点**：同时进行了数据集实验和实车验证，增强了工程可行性。
- **效率优势**：推理时间仅0.58秒，满足实时性要求。

## 8. 不足与局限
- **实验覆盖**：只使用了ROADWork一个数据集，缺乏其他施工区域数据集验证。
- **对比方法**：仅对比了微调方法，未与更多VLM规划方法（如GPT-4V规划的基线）或传统规划方法比较。
- **失败模式通用性**：8种模式是否覆盖所有失败情况未知，可能受数据集限制。
- **偏差风险**：VLM错误率68%可能受限于特定VLM版本（Qwen2.5-VL），其他VLM表现如何未探索。
- **应用限制**：施工区域场景复杂多样，15个实车场景可能不足以代表所有情况；依赖RAG检索需要维护历史案例库。

（完）
