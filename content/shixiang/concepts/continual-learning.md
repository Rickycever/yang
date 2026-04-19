---
title: Continual Learning — 下一代 AI 范式
topic: shixiang
type: concept
created: 2026-04-19
tags: [continual-learning, online-learning, ai-paradigm, llm, rl]
---

# Continual Learning — 下一代 AI 范式

## 定义

Continual Learning（持续学习）指模型能够在推理过程中持续从交互数据中学习更新，而非训练完成后参数冻结。拾象将其定义为"从 Static（冻结的智能）到 Living（越用越聪明）"的范式转变。

当前 LLM 的本质问题：在推理时表现出色，但无法从每天的交互中吸取教训——训练一次，用半年，期间模型无法自我进化。

## 运作方式

**当前数据 Scaling 的三个阶段（拾象比喻）**：
- **Pre-train data**（石油）：量大但快用完，Pre-training 确实搞不出更多数据
- **RL 专家数据**（新能源）：有用但慢，是当前 30%-50% 的增长来源
- **Self-improvement / Continual Learning**（核聚变）：还没突破，突破就无敌

**技术路径**：
- Online RL：模型从推理时的用户反馈信号实时更新，Cursor 是雏形（用户 accept/reject 代码 → 小时级更新模型）
- Learn From Inference：不是离线 batch 更新，而是推理即训练
- Sample Efficiency：Ilya Sutskever 的核心论点——真正的 Superintelligence 在于用极少样本快速掌握新领域（比喻：一个高智商15岁实习生，看几个案例就能学会法律）

**基础设施要求**：Continual Learning 的成熟同样需要新的训练基础设施支持，不只是算法突破。

## 为什么重要

1. **是 AGI 商业化的关键卡点**：AI 替代劳动力（Option 1）和 AI 创造增量价值（Option 2）都需要模型的可靠性大幅提升，而可靠性的本质是持续学习和适应。

2. **是下一代范式的核心信号**：拾象判断 2026 年将看到范式级别的信号，而机器人、世界模型、多模态都不构成范式级别的问题——Continual Learning 才是唯一重要的真问题。

3. **重新定义模型竞争**：当前范式下拼战略 bet 和组织执行力，Continual Learning 突破后将重新洗牌。

4. **Proactive Agent 的底层支撑**：Proactive Agent 需要长期记忆、主动行动，本质是 Continual Learning 在产品层的体现。

## Connections

- [[shixiang/sources/shixiang-lp-meeting-dec-2025|拾象 LP Meeting Dec 2025]] — 本概念的主要来源
- [[shixiang/concepts/proactive-agent|Proactive Agent]] — Continual Learning 在产品层的落地形态
- [[shixiang/concepts/world-model|World Model]] — 多模态数据是 Continual Learning 的重要数据来源
- [[shixiang/overview|拾象AI洞察 全景概览]] — 所属话题入口
