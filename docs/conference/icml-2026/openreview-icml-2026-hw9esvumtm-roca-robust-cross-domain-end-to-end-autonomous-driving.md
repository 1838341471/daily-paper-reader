---
title: "RoCA: Robust Cross-Domain End-to-End Autonomous Driving"
title_zh: RoCA：鲁棒跨域端到端自动驾驶
authors: "Rajeev Yasarla, Shizhong Han, Hsin-Pai Cheng, Apratim Bhattacharyya, Shweta Mahajan, Litian Liu, Yunxiao Shi, Risheek Garrepalli, Hong Cai, Fatih Porikli"
date: 2026-04-30
pdf: "https://openreview.net/pdf/95a84909dd20724702715f37ac767abc2e8d6d20.pdf"
tags: ["query:av-pnc"]
score: 8.0
evidence: 鲁棒跨域端到端自动驾驶框架，直接贡献于规划与控制
tldr: 端到端自动驾驶跨域部署面临性能下降和重训练成本高的问题，现有大语言模型方法难以保证性能。本文提出RoCA框架，利用高斯过程学习基础令牌，建模车辆信息的联合分布，实现鲁棒跨域驾驶。实验表明RoCA在跨域场景下稳定且域适应成本低，为端到端自动驾驶的实际应用提供了新方案。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 端到端自动驾驶在跨城市等域迁移时性能损失大，大语言模型方法域适应成本高。
method: 提出RoCA，用高斯过程联合建模自车与周围车辆令牌，实现概率分布学习。
result: 实验表明RoCA跨域驱动性能稳健，域适应开销低。
conclusion: RoCA为端到端自动驾驶的跨域鲁棒性提供了有效且高效的解决方案。
---

## Abstract
End-to-end (E2E) autonomous driving has recently emerged as a new paradigm, offering significant potential. However, few studies have looked into the practical challenge of deployment across domains (e.g., cities). Although several works have incorporated Large Language Models (LLMs) to leverage their open-world knowledge, LLMs do not guarantee cross-domain driving performance and may incur prohibitive retraining costs during domain adaptation. In this paper, we propose RoCA, a novel framework for robust cross-domain E2E autonomous driving. RoCA formulates the joint probabilistic distribution over the tokens that encode ego and surrounding vehicle information in the E2E pipeline. Instantiating with a Gaussian process (GP), RoCA learns a set of basis tokens with corresponding trajectories, which span diverse driving scenarios. Then, given any driving scene, it is able to probabilistically infer the future trajectory. By using RoCA together with a base E2E model in source-domain training, we improve the generalizability of the base model, without requiring extra inference computation. In addition, RoCA enables robust adaptation on new target domains, significantly outperforming direct finetuning. We extensively evaluate RoCA on various cross-domain scenarios and show that it achieves strong domain generalization and adaptation performance.

---

## 论文详细总结（自动生成）

由于提供的文本仅为 OpenReview 的验证页面，不包含论文的实际内容，无法进行结构化分析和总结。

（完）
