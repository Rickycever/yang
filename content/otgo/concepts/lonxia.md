---
title: 龙虾 (Lobster) — OTGO's AI Agent Framework
topic: otgo
type: concept
created: 2026-04-13
tags: [龙虾, Agent, Claude, AI, 多Agent]
---

# 龙虾 (Lobster) — OTGO's AI Agent Framework

"龙虾" (lobster) is the internal nickname at OTGO for AI agents, specifically those built on top of Claude Code. A 龙虾 is not just a chatbot — it is an autonomous agent with persistent memory, defined skills, a specific role, and the ability to call tools, browse the web, write code, and coordinate with other agents. The metaphor captures the animal's hardy, networked, bottom-up foraging nature.

<div class="zh-trans">"龙虾"是 OTGO 内部对 AI Agent（特指基于 Claude Code 构建）的昵称。龙虾不是聊天机器人——它是有持久记忆、特定技能、明确角色，能调用工具、浏览网页、写代码、与其他 Agent 协作的自主智能体。</div>

---

## Definition

A fully configured 龙虾 has three layers:

**Soul Layer (灵魂层):** Core values, philosophical frameworks, and non-negotiable behavioral principles. Defines *who* the agent is. Example: 辉哥's CEO agent uses Pythagoras / Gödel / Darwin as three competing philosophical sub-agents that debate each other before producing a conclusion.

**Role Layer (角色层):** Specific responsibilities, domain expertise, and operational context. Defines *what* the agent does. Example: strategy alignment, product line QC, external communication, financial analysis.

**Memory:** Persistent, structured knowledge accumulated over time. Three access tiers: Highly Confidential · Authorized Visible · Public. Write permissions controlled separately from read permissions.

<div class="zh-trans">完整配置的龙虾有三层：**Soul 层**（价值观/哲学框架）定义这个 Agent 是谁；**Role 层**（职责/场景）定义它做什么；**Memory**（分层访问控制的持久知识库）定义它知道什么。</div>

---

## How It Works

### Building a 龙虾

Key principles from OpenClaw (25 teams' experience):

1. **Don't build an all-knowing lobster.** Divide by role. A lobster handling too many responsibilities degrades as context grows.
2. **Pipeline architecture.** Real-world deployments split into stages: data ingestion → analysis → output → QC → distribution.
3. **SOP as training material.** Feed the lobster its own past mistakes. Build benchmark sets. Let "小准" (a scoring agent) evaluate and iterate.
4. **Memory discipline.** Always tell the lobster exactly where to write memory. Vague instructions like "remember this" result in lost data on the next session.
5. **Heartbeat mechanisms.** Long-running agents need a supervisor that detects silence and restarts stalled tasks.

### The "Master Craftsman Problem"

The lobster is only as good as its input. What you feed it — cases, aesthetic standards, domain context, historical examples — is the core IP. This maps directly to the knowledge management challenge: the lobster can help extract tacit knowledge (Know Why), but only if a human deliberately encodes it.

<div class="zh-trans">龙虾的好坏取决于你喂给它什么。你的 Case 集、审美标准、领域 context 才是真正的核心资产。这直接对应知识管理挑战：龙虾能帮你提炼隐性知识（Know Why），但前提是人类主动编码输入。</div>

---

## Why It Matters

### Redefining the Unit of Work

The shift from DM to 龙虾 marks a conceptual break: the unit of work is no longer a session (stateless, tool-like) but a persistent *employee* (stateful, relationship-based). A lobster learns your organization's context, accumulates domain knowledge, and becomes harder to replace — which is the intended outcome.

<div class="zh-trans">从 DM 到龙虾是概念性跃迁：工作单元从"无状态工具（session）"变成"有状态员工"。龙虾随时间学习组织 context，积累领域知识，越用越难替代——这正是目标。</div>

### Organizational Implications

- Executives should own and train their own lobsters because they control *what* to do — the highest-leverage decision point.
- Frontline workers trained in the wrong direction cause harm. The scarce resource is the person who knows what "good" looks like.
- The goal is not replacement but augmentation: everyone with a lobster can do what previously required a team.

### Responsibility Principle

A lobster cannot bear responsibility for its outputs. Each lobster must have a human owner who is accountable for what it produces. "Blaming the AI" is not acceptable.

---

## Lobster Use Case Map (from OpenClaw 2026-03-17)

| Domain | Use Case | Maturity |
|--------|----------|----------|
| Marketing | GEO optimization, social media management, content production | Commercial ✅ |
| Creative | TVC production, video pipeline, ad copy | Commercial ✅ |
| Research | KOL risk screening, competitive analysis, product selection | Commercial ✅ |
| Operations | Automated tax filing, HR analytics, reporting automation | Production-ready |
| Sales | One-person agency, presales proposals, account management | Validated |
| Government | Cultural tourism crisis response, public opinion monitoring | In testing |
| Engineering | Multi-agent software development, code review | 30% complete |

---

---

## 龙虾 vs CC：协调者与执行者

龙虾和 CC（Claude Code 实例）是两种不同的 Agent 角色，分工明确：

| | 龙虾（协调者） | CC 实例（执行者） |
|---|---|---|
| **特征** | 持久身份、长期记忆、有性格 | 干净 context、无记忆、完成即释放 |
| **做什么** | 接收指令、拆解任务、调度 CC、汇报结果 | 在干净环境执行具体任务，返回结果 |
| **生命周期** | 长期存在，跨任务积累 | 任务级，完成就释放 |
| **类比** | 项目经理——记得你上次要什么 | 外包工人——给任务书就能干 |

龙虾的本质：**拥有独立计算机（实体或虚拟机）的 Agent**——有自己的文件空间，可安装软件，可调用各种工具。

CC 是龙虾的标配后端。同样任务，CC 处理的经济效益比龙虾直接在 IM 中交互好 5-10 倍。当前 OpenClaw 是最接近"龙虾"概念的实现——但龙虾不绑定任何特定产品，未来可直接替换更好的实现。

---

## Connections

- [[otgo/overview\|OTGO 全景概览]]
- [[otgo/concepts/octo\|octo 平台]] — the network that connects lobsters
- [[otgo/concepts/soul-memory\|Soul & Memory 架构]] — how to structure a lobster's identity
- [[otgo/concepts/multi-cc-collab|多 CC 协作模式]] — 龙虾作为编排者调度多个 CC 的具体机制
- [[otgo/concepts/openclaw\|OpenClaw]] — the program that drove lobster adoption
- [[otgo/concepts/bihe\|闭环原则]] — lobsters enable closed-loops
- [[otgo/sources/dual-native-design-v1.5-20260404|Dual-Native Design v1.5]] — 龙虾与 CC 分工的完整论述
- [[otgo/sources/openclaw-点火计划-20260317\|OpenClaw 点火计划]] — 25 teams' deployment playbook
- [[otgo/sources/班委会-otgo精神-20260309\|OTGO精神]] — original lobster mandate
