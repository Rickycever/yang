---
title: OpenClaw vs Hermes：一文深入理解两大通用 Agent
topic: otgo
type: source
created: 2026-04-12
tags: [OpenClaw, Hermes, 通用Agent, 技术架构, 竞品对比]
---

# OpenClaw vs Hermes：两大通用 Agent 深度对比

## Summary

A technical deep-dive from the "架构师 (JiaGouX)" WeChat account comparing OpenClaw and Hermes as general-purpose Agent systems. Both are beyond "model wrappers" — they are long-running engineering environments for Agents. The key insight: they solve fundamentally different problems. OpenClaw is a **local-first Agent Gateway** (control plane for real-world inlets, sessions, devices, permissions). Hermes is a **learning Agent Runtime** (closed loop that compounds experience so the Agent improves over time).

<div class="zh-trans">来自"架构师（JiaGouX）"公众号的技术深度对比文章，对比了OpenClaw和Hermes这两大通用Agent系统。两者都超越了"模型包装器"阶段——它们是Agent的长期运行工程环境。核心洞见：它们解决的是根本不同的问题。OpenClaw是**本地优先的Agent Gateway**（真实世界入口、会话、设备、权限的控制面）。Hermes是**学习型Agent Runtime**（让Agent随时间积累经验、持续改进的闭环）。</div>

## Key Points

**Shared characteristics (both are general-purpose agents):**
Both have Skills, Memory, Context, tool calling, and execution environments. Both support multi-channel messaging. Both have moved past the "model + prompt" stage into structured, long-running agent operation.

<div class="zh-trans">两者都有Skills、Memory、Context、工具调用和执行环境。两者都支持多渠道消息。两者都超越了"模型+提示词"阶段，进入了结构化的长期Agent运行模式。</div>

**OpenClaw's core asset — Gateway control plane:**
OpenClaw connects WhatsApp, Telegram, Slack, Discord, Signal, iMessage, Matrix, Feishu, LINE, WeChat, WebChat and more, then manages sessions, routing, nodes, tools, and security policies through a unified Gateway. Its "thickness" is in the **inlet layer and control plane** — multi-device, multi-channel coordination with auditable trust models.

<div class="zh-trans">OpenClaw连接WhatsApp、Telegram、Slack、Discord、Signal、iMessage、Matrix、飞书、LINE、微信、WebChat等，通过统一Gateway管理会话、路由、节点、工具和安全策略。它的"厚度"在于**入口层和控制面**——多设备、多渠道协同，带可审计的信任模型。</div>

**Hermes's core asset — learning execution loop:**
Hermes emphasizes self-improving agent, closed learning loop, automatic Skill creation and repair, FTS5 session search, Honcho user modeling, and six execution backends (local / Docker / SSH / Daytona / Singularity / Modal). Skills in Hermes = "successful execution paths that get crystallized into procedural memory."

<div class="zh-trans">Hermes强调自我改进Agent、闭环学习循环、自动创建和修补Skills、FTS5会话搜索、Honcho用户建模，以及六种执行后端（本地/Docker/SSH/Daytona/Singularity/Modal）。Hermes中的Skills = "成功执行路径被结晶为程序性记忆"。</div>

**Skills — same word, different semantics:**
OpenClaw: "humans define skills, system loads and governs them." Hermes: "agent auto-creates skills after completing complex tasks by distilling the success path."

<div class="zh-trans">OpenClaw：人定义技能，系统负责加载和治理。Hermes：Agent完成复杂任务后自动提炼成功路径并创建技能。</div>

**Security philosophy:**
OpenClaw: trust model + configuration audit. Hermes: defense-in-depth, from approval gates to container isolation, tightening at each layer.

<div class="zh-trans">OpenClaw：信任模型+配置审计。Hermes：纵深防御，从审批门到容器隔离逐层收紧。</div>

**Migration path:**
Hermes supports `hermes claw migrate` — imports OpenClaw personas, memory, skills, allowlist, some messaging settings. But migration means configuration transfer, not workflow transfer.

<div class="zh-trans">Hermes支持`hermes claw migrate`——导入OpenClaw的persona、memory、skills、allowlist、部分消息设置。但迁移的是配置，不是整套使用方式。</div>

**Decision guide:**
- Need multi-inlet assistant + governance plane → **OpenClaw**
- Need long-term repeated task experience accumulation + self-improvement → **Hermes**

<div class="zh-trans">选择指南：需要多入口助理和治理面 → OpenClaw；需要长期重复任务的经验沉淀和自我改进 → Hermes。</div>

## Connections

- [[otgo/concepts/openclaw|OpenClaw]] — the product being compared
- [[otgo/concepts/hermes|Hermes]] — the competing system analyzed
- [[otgo/sources/openclaw-点火计划-20260317|OpenClaw 点火计划成果分享]] — OpenClaw in practice
