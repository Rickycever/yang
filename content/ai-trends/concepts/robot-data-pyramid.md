---
title: 机器人数据金字塔
topic: ai-trends
type: concept
created: 2026-05-09
tags: [robotics, data-scaling, vla, world-model, embodied-ai]
---

# 机器人数据金字塔

## 定义

理解机器人数据体系的四层框架，对应 LLM 训练的不同阶段。2026 年是机器人数据 Scaling 的大年，整个行业围绕这个金字塔展开竞争。

## 运作方式

**四层结构（从底到顶）**：

| 层级 | 数据类型 | 对应 LLM 阶段 | 特点 |
|------|---------|--------------|------|
| 底层 | Egocentric Data（第一视角视频） | Pre-training | 成本最低、最易规模化，通过人类视角视频学习物理世界理解 |
| 第二层 | UMI 数据 | SFT | 成本与规模化程度居中；硬件构型必须与部署机器人完全一致 |
| 第三层 | Teleop 真机数据 | SFT | 历史最久，直接绑定具体硬件；4小时真机数据 + 前两层先验已可支持复杂灵巧任务 |
| 顶层 | World Model | RL | 支持无限复杂度与多样性，极度消耗算力；本质是用算力换真实世界交互 |

**代表动态**：
- Google Robotics & NVIDIA：主力推 Egocentric data scaling（NVIDIA EgoScale：20,854 小时第一视角视频预训练 VLA）
- Sunday、Generalist：UMI 数据方向
- 没有公司确定最优配比，egocentric data 的 scaling law 尚未出现

**技术路线转移：VLA → World Action Model（WAM）**

四大转移原因：
1. 灵巧运动不需要语言，物理智能才是机器人本质需求
2. WAM 直接学视频，不依赖 action-labeled data（采集成本低）
3. VLA 容易过拟合已见任务；WAM 更擅长物理泛化（换光线/材质不失败）
4. WAM 能"想象未来状态再选动作"，更适合 long-horizon task

WAM 在新任务与新环境的泛化能力比 SOTA VLA 提升 2 倍以上。

**硬件是关键瓶颈**：
- 灵巧手数据至今没有公司实现规模化采集，根本原因是硬件不成熟
- 硬件 first = AI first（对机器人公司而言）
- 华人创业者结构性机会：依托中国供应链打造机器人领域的 TSMC

## 为什么重要

- OpenAI/Google/NVIDIA 均已明确将自研 World Model 用于机器人，"World Model × 机器人"方向创业公司面临头部 Lab 直接竞争压力
- 硬件成熟度是整个数据金字塔的速率限制步骤
- 2026 年是数据 Scaling 大年，但 scaling law 尚未成熟（模型参数停在 7B-14B，远未达到 LLM 的协同 scaling 阶段）

## Connections

- [[ai-trends/sources/era-of-agent-shixiang-2026-may|拾象 AGI 洞察 2026-05]] — 本概念的主要来源
- [[ai-trends/concepts/world-models|World Models]] — World Model 是金字塔顶层的核心技术路线
- [[shixiang/concepts/world-model|世界模型]] — 拾象前序报告对 World Model 的分析
