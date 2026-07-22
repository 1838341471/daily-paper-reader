---
title: "RoCA: Robust Cross-Domain End-to-End Autonomous Driving"
title_zh: RoCA：鲁棒的跨域端到端自动驾驶框架
authors: "Rajeev Yasarla, Shizhong Han, Hsin-Pai Cheng, Apratim Bhattacharyya, Shweta Mahajan, Litian Liu, Yunxiao Shi, Risheek Garrepalli, Hong Cai, Fatih Porikli"
date: 2026-04-30
pdf: "https://openreview.net/pdf/95a84909dd20724702715f37ac767abc2e8d6d20.pdf"
tags: ["query:av-pnc"]
score: 5.0
evidence: 提出一种跨域鲁棒的端到端自动驾驶框架，利用高斯过程实现跨域规划与控制
tldr: 针对端到端自动驾驶跨域部署的挑战，本文提出RoCA框架。该框架通过建模自车与周围车辆信息的联合概率分布，并利用高斯过程学习基令牌，提升了跨域（如城市）的驾驶性能，避免了大型语言模型带来的高昂微调成本。实验表明RoCA在多个城市场景中表现出强鲁棒性，为端到端自动驾驶的实际部署提供了可行方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 端到端自动驾驶跨域部署面临性能下降与高成本微调问题。
method: 采用高斯过程建模自车与周围车辆信息的联合概率分布，学习可迁移的基令牌。
result: 在多个城市跨域场景下表现出比现有方法更强的鲁棒性与泛化能力。
conclusion: RoCA为端到端自动驾驶的跨域适应提供了有效的鲁棒方案。
---

## Abstract
End-to-end (E2E) autonomous driving has recently emerged as a new paradigm, offering significant potential. However, few studies have looked into the practical challenge of deployment across domains (e.g., cities). Although several works have incorporated Large Language Models (LLMs) to leverage their open-world knowledge, LLMs do not guarantee cross-domain driving performance and may incur prohibitive retraining costs during domain adaptation. In this paper, we propose RoCA, a novel framework for robust cross-domain E2E autonomous driving. RoCA formulates the joint probabilistic distribution over the tokens that encode ego and surrounding vehicle information in the E2E pipeline. Instantiating with a Gaussian process (GP), RoCA learns a set of basis tokens with corresponding trajectories, which span diverse driving scenarios. Then, given any driving scene, it is able to probabilistically infer the future trajectory. By using RoCA together with a base E2E model in source-domain training, we improve the generalizability of the base model, without requiring extra inference computation. In addition, RoCA enables robust adaptation on new target domains, significantly outperforming direct finetuning. We extensively evaluate RoCA on various cross-domain scenarios and show that it achieves strong domain generalization and adaptation performance.

---

## 论文详细总结（自动生成）

由于提供的文本仅为 OpenReview 的验证页面，不包含论文的实际内容，无法进行结构化分析和总结。

（完）
