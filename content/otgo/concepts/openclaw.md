---
title: OpenClaw — 全员龙虾落地计划
topic: otgo
type: concept
created: 2026-04-13
tags: [OpenClaw, 龙虾, 组织变革, 开源]
---

# OpenClaw — OTGO's Company-Wide Agent Adoption Program

OpenClaw is OTGO's internal initiative to drive adoption of 龙虾 (lobster AI agents) across the entire company, and simultaneously the name for the related open-source project. Launched in early 2026, it mandated that every business unit experiment with lobster agents and share results in a showcase event — the "点火计划 (Ignition Plan)."

<div class="zh-trans">OpenClaw 是 OTGO 推动龙虾 Agent 全公司落地的内部计划，同时也是相关开源项目的名称。2026年初启动，要求每个业务单元实验龙虾 Agent 并在"点火计划成果分享会"上展示结果。</div>

---

## Definition

OpenClaw operates on two levels:

1. **Internal transformation program:** Structured push to get all departments using lobster agents in real workflows — not as toys but as production systems producing measurable outcomes.

2. **Open-source project:** OTGO's public-facing agent framework, intended to grow a community of lobster practitioners outside the company and create a feedback loop of best practices.

<div class="zh-trans">OpenClaw 在两个层面运作：① 内部变革计划——推动所有部门在真实业务流程中使用龙虾 Agent，产出可量化成果；② 开源项目——对外的 Agent 框架，目标是在公司外部建立龙虾实践者社区，形成最佳实践的反馈闭环。</div>

---

## How It Works

### Ignition Plan Structure

- Teams form around real business problems
- 7-hour intensive showcase (2026-03-17): 24 teams, 60+ people
- Each team demonstrates: what they built, what worked, what broke, and what they learned
- 辉哥 provides live feedback focused on: taste, feedback loops, and collective intelligence

### Design Principles

**No all-knowing agents.** Every mature deployment used specialization. The pattern: one lobster per role, connected in a pipeline.

**SOP as curriculum.** Lobsters learn from structured mistake logs, benchmark sets, and case libraries. The human's job is to build these inputs, not to write prompts.

**Benchmark → Score → Iterate.** "小准" (a scoring agent) auto-evaluates output quality against human-defined acceptance criteria. Humans only need to provide case examples and correct answers.

**Skill portability.** A Skill written for one lobster can run on another with no modification (demonstrated: 93/100 score on first transfer). Skills are the reusable unit of capability.

<div class="zh-trans">核心设计原则：① 专职化分工，无万能龙虾；② SOP 作为龙虾的课程，人负责建 case 集；③ 小准自动打分迭代；④ Skill 跨龙虾可移植（首次移植 93 分，无需修改）。</div>

---

## Why It Matters

### Proof of Commercial Viability

The first showcase produced six commercially validated use cases generating real revenue — most notably the Gillette TVC, Walmart product selection report, and the KOL risk screening service (cost reduced to 1/10 of vendor cost). This validated that lobster-based delivery can replace traditional outsourcing in multiple verticals.

### Organizational Learning Velocity

24 teams running experiments simultaneously, all sharing results and solutions, creates organizational learning at a pace impossible through individual trial-and-error. The cross-team solution library (e.g., checkpoint-resume, Browser Relay, dual-channel comms) compressed months of individual discovery into a single afternoon.

<div class="zh-trans">24 支队伍同时实验并共享结果，使组织学习速度远超个人试错。跨团队解决方案库（断点续传、Browser Relay、双通道通信等）将数月的个人摸索压缩到了一个下午。</div>

### Connection to octo

辉哥's closing statement: "octo is the OS connecting all global lobsters." OpenClaw is the proof-of-concept that OTGO can coordinate a networked agent ecosystem. The internal showcase is the prototype for what octo enables at enterprise scale.

---

## Key Bottlenecks (Catalogued by OpenClaw)

| Type | Issue | Status |
|------|-------|--------|
| Context degradation | Long tasks cause instruction forgetting | Partially solved (checkpoint-resume) |
| Silent stop | Agent stops without notification | Partially solved (heartbeat monitors) |
| Token cost | Expensive at scale | Ongoing |
| Anti-scraping | Platform barriers for data access | Partially solved (Browser Relay/CDP) |
| Information silos | Multi-agent data inconsistency | Partially solved (async data bus) |
| 企微/腾讯会议 API | Cannot directly access meeting recordings | Unsolved |
| Emotion/narrative | Lobsters weak at character arcs and emotional logic | Unsolved |

---

## Connections

- [[otgo/overview\|OTGO 全景概览]]
- [[otgo/concepts/lonxia\|龙虾 (Lobster Agent)]] — the core capability OpenClaw adopts
- [[otgo/concepts/octo\|octo 平台]] — OpenClaw is the internal proof-of-concept for octo's mission
- [[otgo/concepts/bihe\|闭环原则]] — all OpenClaw projects evaluated on closed-loop criteria
- [[otgo/sources/openclaw-点火计划-20260317\|OpenClaw 点火计划成果分享会]] — the detailed showcase record
- [[otgo/entities/wu-minghui\|吴明辉 (辉哥)]] — initiated and hosted OpenClaw
