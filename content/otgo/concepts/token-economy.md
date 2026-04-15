---
title: Token Economy — OTGO's New Commercial Model
topic: otgo
type: concept
created: 2026-04-13
tags: [商业模式, token, 定价, 外包]
---

# Token Economy — OTGO's New Commercial Model

OTGO has replaced its previous man-hour billing model with a token-based commercial model: clients pay for **token consumption × a management multiplier** (typically ×1.1–2.0). This reframes the entire outsourcing industry — OTGO becomes a token distributor and AI orchestration layer rather than a labor provider.

<div class="zh-trans">OTGO 用 token 计费模式替代了原有的人日计费模式：客户支付 **token 消耗 × 管理倍数**（通常 ×1.1–2.0）。这重构了整个外包行业——OTGO 变成 token 分发商和 AI 编排层，而非劳动力提供商。</div>

---

## Definition

**Old model:** Sell man-days (人日). Revenue = number of human consultants × daily rate. Scaling requires hiring more people.

**New model:** Sell token consumption + management fee. Revenue = (client token spend) × multiplier. Scaling requires orchestrating more lobsters, not hiring more humans.

The practical effect: "engineers are unlimited" — lobsters handle delivery, humans only intake requirements and verify output.

<div class="zh-trans">旧模式：卖人日，营收 = 顾问人数 × 日费；扩张需要招人。新模式：卖 token + 管理费，营收 = 客户 token 消耗 × 倍数；扩张只需协调更多龙虾，不需要招人。实际效果："干活的工程师是无穷无尽的"——龙虾交付，人只管接需求和验收。</div>

---

## How It Works

### Pricing Structure

```
Client pays = Base token cost × management multiplier (1.1–2.0)
```

The multiplier covers:
- Lobster configuration and training (initial)
- Quality verification (ongoing)
- Organizational capability (knowing what to build)

### octo Commercial Layer

For octo (the platform product), the commercial model is:
- **Core product:** Open source (free to use, fork, and self-host)
- **Revenue:** Custom development service + token consumption × multiplier
- **Network effect flywheel:** Client uses octo → produces best practices → shares back → platform improves → OTGO earns both fee and product improvement

### Client Implementation Patterns

| Client Type | How Tokens Flow |
|-------------|----------------|
| Platform client (octo) | Client hosts privately; OTGO charges for customization + ongoing orchestration |
| Agent client (single solution) | OTGO builds and runs the agent; client pays per token consumed |
| Hybrid | Start with single agent → migrate to octo platform as usage grows |

---

## Why It Matters

### Structural Advantage

Traditional consulting firms are constrained by headcount. OTGO is not. A project that would require 10 consultants for 3 months can be handled by 1-2 humans orchestrating 10+ lobsters in a fraction of the time. The cost structure is fundamentally different.

<div class="zh-trans">传统咨询公司受制于人头数，OTGO 不受此限制。原本需要 10 名顾问做 3 个月的项目，1-2 个人协调 10+ 龙虾就能完成。成本结构根本不同。</div>

### Risk: Token Cost Inflation

From the 天合光能 discussion — token cost is a real and growing risk:

| Reference | Cost |
|-----------|------|
| 大疆 (DJI) per-employee AI budget | ¥1,000+/month |
| Top engineer at AI company | ~$8,000/day |
| OTGO original annual budget | ¥100M |
| OTGO revised estimate | ¥300–350M |

Clients and OTGO alike need to monitor token consumption carefully. Blind adoption without benchmarking consumption patterns risks runaway costs.

### Mindset Shift Required

The transition from man-day to token billing requires a fundamental shift in how the team thinks about value:
- **Old:** "How many people-days will this take?"
- **New:** "What token budget do we need, and what multiplier covers our orchestration value?"

This shift was declared mandatory for all OTGO team members on 2026-03-09.

<div class="zh-trans">从人日到 token 的转变需要思维框架的根本转换——原来问"这需要多少人天"，现在问"需要多少 token 预算，什么倍数覆盖了我们的编排价值"。这一转变在 2026-03-09 被宣布为全员强制执行。</div>

---

## Connections

- [[otgo/overview\|OTGO 全景概览]]
- [[otgo/concepts/octo\|octo 平台]] — the product that generates token revenue
- [[otgo/concepts/lonxia\|龙虾 (Lobster)]] — the agents that do the work
- [[otgo/concepts/bihe\|闭环原则]] — token model works best when combined with closed-loop feedback
- [[otgo/sources/第一次概念会议-20260309\|第一次概念会议]] — commercial model formally announced
- [[otgo/sources/天合光能交流-20260413\|天合光能交流]] — token cost reality check
