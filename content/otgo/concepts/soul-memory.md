---
title: Soul & Memory Architecture — Designing an Agent's Identity
topic: otgo
type: concept
created: 2026-04-13
tags: [Soul, Memory, Agent设计, 龙虾, 知行合一]
---

# Soul & Memory Architecture — Designing an Agent's Identity

"Soul" (灵魂) is 辉哥's framework for the deepest layer of a lobster agent's configuration: the philosophical values, thinking frameworks, and non-negotiable principles that define *who* the agent is — not just *what* it does. Combined with structured Memory access controls, it enables agents that embody genuine, consistent character. The principle: 知行合一 (unity of knowledge and action) — what the agent says, does, and decides should be fully consistent with its underlying logic.

<div class="zh-trans">"Soul（灵魂）"是辉哥设计龙虾最底层配置的框架：哲学价值观、思维框架和不可妥协的原则，定义这个 Agent 是谁——而不仅仅是它做什么。结合结构化的 Memory 访问控制，可以构建出具有真实、一致性格的 Agent。原则：知行合一——Agent 说什么、做什么、怎么决策，应与其底层逻辑完全一致。</div>

---

## Definition

### Soul Layer

The Soul layer encodes the agent's philosophical orientation as competing sub-agents that debate each other, producing conclusions through dialectical reasoning:

| Sub-Agent | Philosopher | Framework | Application |
|-----------|-------------|-----------|-------------|
| 1 | Pythagoras | Everything is number, Y=f(x) | Quantitative rigor; everything can be measured |
| 2 | Gödel | Incompleteness; always think outside the box | Creative disruption; no system is complete |
| 3 | Darwin | Complex systems evolve over time | Long-term systems thinking; favor adaptable designs |

These three personas spawn as sub-agents and argue. The answer that emerges from their collision is equivalent to deep personal reasoning — not a quick LLM response.

<div class="zh-trans">Soul 层将哲学取向编码为互相博弈的子 Agent：毕达哥拉斯（万物皆数，定量严谨）、哥德尔（不完备性，持续破框）、达尔文（复杂系统长期演化）。三套思想各自 spawn 子 Agent 互相辩论，碰撞后的结果才接近深度思考的水平，而非 LLM 的快速应答。</div>

### Role Layer

Built on top of Soul, the Role layer defines operational responsibilities and scene-specific behaviors:
- Strategy alignment & communication
- Organizational culture
- Product line synchronization (e.g., debating feasibility with a product agent)
- External communication preparation

### Memory Tiers

| Tier | Visibility | Write Permission |
|------|------------|-----------------|
| Highly Confidential | Owner only | Owner only |
| Authorized Visible | Specific people/roles (read) | Owner only |
| Public | Anyone | Owner only (default) |
| Special Documents | Specific readers defined per document | Explicitly blocked for others |

The CEO's strategy documents, for example, are readable by authorized team members but cannot be modified by anyone except the CEO.

---

## How It Works

### Why Multi-Agent Debate > Single Prompt

A single prompt produces a single perspective. Three philosophical personas debating each other produce a conclusion that has been stress-tested from multiple angles:
- Pythagorean: Is this quantifiable? What are the metrics?
- Gödelian: What assumptions are we not questioning? What's outside this frame?
- Darwinian: Does this compound over time? What survives natural selection?

The human only reads the synthesized output after the three have debated.

<div class="zh-trans">单一 prompt 只产生单一视角。三个哲学角色互相辩论后产出的结论，已经从多个角度经过压力测试：毕达哥拉斯问"可量化吗"，哥德尔问"我们忽略了什么假设"，达尔文问"这能长期复利吗"。人类只读三者辩论后的综合结论。</div>

### Tacit Knowledge Capture

The Soul & Memory architecture is also OTGO's answer to the tacit knowledge problem raised in the 天合光能 discussion. A fully configured lobster with deep Soul encoding represents the owner's "Know Why" — the reasoning behind decisions that is normally lost when people leave or forget. The lobster becomes a vessel for preserving organizational wisdom.

---

## Why It Matters

This framework elevates agent design from "prompt engineering" to "character design." The difference:
- A well-prompted agent gives good answers
- A soul-configured agent gives consistent answers that reflect coherent values, resists manipulation, and improves over time

For OTGO, this also ties into the competitive argument: a CEO who has encoded their values and reasoning into a lobster can be "present" in strategy discussions at scale — across teams, across time zones, asynchronously.

<div class="zh-trans">这个框架将 Agent 设计从"提示词工程"提升到"性格设计"。区别：prompt 调得好的 Agent 给出好答案；Soul 配置好的 Agent 给出一致的答案——反映连贯的价值观，抵御被操控，并随时间改进。</div>

---

---

## 参数化伦理五层架构（伦理学 v2.5 新增）

龙虾的配置和行为规则分五层载体，变化频率递增，**冲突时上层覆盖下层**（违宪审查机制）：

| 载体层 | 内容 | 变化频率 | 修改权限 |
|--------|------|---------|---------|
| **参数层（哲学）** | 龙虾三律、组织价值观 | 极少变化（需"修宪"） | 最高层品鉴者 |
| **参数层（方法论）** | 行业规范、风控规则 | 季度级 | 管理层 |
| **Soul 层** | 龙虾的稳定人格和判断倾向 | 月级 | 品鉴者 |
| **Memory 层** | 具体项目记忆、上下文 | 日级 | 品鉴者 + 龙虾自动 |
| **Skill 层** | 显性能力定义 | 版本化 | Skill 作者 |

### Soul/Memory 边界判断规则（变化频率法）

判断一条规则应归 Soul 还是 Memory 的实操标准：**"这条规则一个月后还适用吗？"**

- 是 → Soul（稳定的人格/品味偏向）
- 不确定 → Memory（具体项目/任务相关的上下文）

| 规则 | 归 Soul 还是 Memory | 理由 |
|------|-------------------|------|
| "回复邮件要礼貌正式" | Soul | 长期稳定的风格偏好 |
| "这周重点关注张总的项目" | Memory | 短期优先级，随时变 |
| "我喜欢数据驱动的论证" | Soul | 品鉴者的稳定 taste |
| "上次会议辉哥提到的方案细节" | Memory | 具体事件记忆 |

### 违宪审查机制

当不同层的规则冲突时，自动按层级优先级裁决（参数层 > Soul > Memory > Skill），龙虾在审计日志中记录冲突检测和裁决过程，确保第二律（对主人忠诚透明）的可审计性。

---

## Connections

- [[otgo/overview\|OTGO 全景概览]]
- [[otgo/concepts/lonxia\|龙虾 (Lobster Agent)]] — Soul 是龙虾配置的最深层
- [[otgo/sources/00-zhanlue-beijing-20260328|战略背景与产品哲学基底]] — 参数化伦理五层架构的来源文件
- [[otgo/sources/班委会-otgo精神-20260309\|OTGO精神]] — 辉哥最初阐述 Soul 层的文件
- [[otgo/sources/天合光能交流-20260413\|天合光能交流]] — Soul 架构解决暗默知识传承问题的场景
- [[otgo/concepts/lonxia-sanlv|龙虾三律]] — 参数层（哲学）的内容，最高优先级
- [[otgo/concepts/digital-avatar|数字分身]] — Soul/Memory 层是数字分身的内部配置
- [[otgo/entities/wu-minghui\|吴明辉 (辉哥)]] — 框架设计者
