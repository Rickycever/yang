---
title: octo — 开源企业 Agent 协作平台
topic: otgo
type: concept
created: 2026-04-13
tags: [octo, 产品, 平台, 开源, 多Agent]
---

# octo — Open-Source Enterprise Agent Collaboration Platform

octo (八爪鱼, "octopus") is OTGO's flagship product: an open-source enterprise AI collaboration platform designed as the operating layer for 龙虾 (AI agents). Its tagline: **"Discord / 飞书 for AI agents."** Where existing tools (飞书, 企业微信, 钉钉) are built for humans to collaborate, octo is built for agents to collaborate — while humans observe, guide, and verify.

<div class="zh-trans">octo（八爪鱼）是 OTGO 的旗舰产品：面向龙虾 Agent 的开源企业 AI 协作平台，定位是 **"AI 用的飞书/Discord"**。现有工具面向人协作，octo 面向 Agent 协作——人类在旁观察、引导和验收。</div>

---

## Definition

octo connects individual 龙虾 agents into a networked organization with:
- **Global persistent memory** across sessions and devices (vs. DM where memory resets per session)
- **Cross-device, cross-team agent collaboration**
- **MCP GUI support** for tasks requiring graphical interface automation
- **Private deployment** — full code and data ownership by the client

The product metaphor: each lobster is an individual brain; octo is the nervous system that connects them into a collective organism.

<div class="zh-trans">octo 将独立龙虾 Agent 连接成网络：全局持久记忆（跨 session、跨设备）、跨团队 Agent 协作、MCP GUI 支持、私有化部署（代码数据全归客户）。比喻：每只龙虾是独立大脑，octo 是将它们连成集体有机体的神经系统。</div>

---

## How It Works

### Positioning in the Ecosystem

octo does not replace existing communication platforms. It inserts itself as a "tentacle" into the networks humans already use (飞书, 企业微信, 个人微信, 腾讯会议), capturing context in real-time or near-real-time, and feeding it into the agent network.

Over time, intelligence and compute accumulate on the octo side. The existing platforms become distribution channels; octo becomes the core node.

<div class="zh-trans">octo 以"触角"方式进入人类现有社交网络（飞书、企微、个人微信等），实时捕捉 context 并注入 Agent 网络。算力和智慧在 octo 侧积累，现有平台逐渐变成渠道，octo 成为核心节点。</div>

### Key Differentiator vs. DM (Previous OTGO Product)

| Dimension | DM | octo + 龙虾 |
|-----------|-------|-------------|
| Memory | Isolated per session | Global, persistent across all sessions |
| Agent network | Single user's agents, high homogeneity | Multi-user, genuinely heterogeneous roles |
| Architecture | Monolithic | Distributed, each agent transparent |
| Trajectory | DM 2.0 deprecated; 3.0 rebuilding | Primary product, active development |

### Commercial Model

| Component | Detail |
|-----------|--------|
| Core product | Open source (clients can fork, customize, private-deploy) |
| Revenue | Custom development service fee + token consumption × management multiplier (×1.1–2) |
| Network effect | Client uses octo → produces best practices → feeds back into platform → platform improves |

---

## Why It Matters

**For OTGO:** Octo is the moat. Open-source removes the "data monopoly" objection that blocks 飞书/企微 adoption. The small-team + lobster development model already exceeds 飞书's 5,000-person team in iteration speed. OTGO's "position advantage" is that incumbents *cannot* open-source without eliminating their own workforce.

**For clients:** Octo solves the AI coordination layer that every enterprise needs but no current tool provides. Clients who deploy octo become dependent on it as agents continuously learn their organization's context — switching cost grows over time.

**For the industry:** Octo embodies the architectural principle that AI systems should be transparent, auditable, and controllable — addressing the "black box" problem that blocks AI adoption in mission-critical enterprise settings.

<div class="zh-trans">对 OTGO：octo 是护城河——开源消除了数据垄断顾虑，小团队+龙虾迭代速度已超越飞书5000人。对客户：octo 解决了每个企业都需要但目前没有工具提供的 AI 协调层，越用越难离开。对行业：octo 体现了 AI 系统应该透明、可审计、可控的架构原则。</div>

---

## Status & Timeline

| Date | Milestone |
|------|-----------|
| 2026-03-09 | Internal testing; basic IM connection first |
| 2026-03-17 | 辉哥 announces octo as global lobster OS; target internal launch April 15 |
| 2026-04-13 | Presented to 天合光能 as architecture reference; open-source release upcoming |

---

## Connections

- [[otgo/overview\|OTGO 全景概览]]
- [[otgo/concepts/lonxia\|龙虾 (Lobster Agent)]] — the agents octo connects
- [[otgo/concepts/bihe\|闭环原则]] — octo enables closed-loop by capturing complete context
- [[otgo/concepts/token-economy\|Token 经济]] — commercial model for octo deployments
- [[otgo/concepts/openclaw\|OpenClaw]] — internal program demonstrating octo's value
- [[otgo/sources/班委会-otgo精神-20260309\|OTGO精神]] — original positioning statement
- [[otgo/sources/第一次概念会议-20260309\|第一次概念会议]] — product strategy and sales formalized
- [[otgo/sources/天合光能交流-20260413\|天合光能交流]] — external articulation of architecture
