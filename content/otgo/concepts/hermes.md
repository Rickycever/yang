---
title: Hermes Agent
topic: otgo
type: concept
created: 2026-04-12
tags: [Hermes, 通用Agent, 学习型, 自我改进, 竞品]
---

# Hermes Agent

## Definition

Hermes is a general-purpose Agent Runtime that emphasizes self-improvement through a closed learning loop. Unlike OpenClaw, which focuses on the control plane (inlets, sessions, permissions), Hermes focuses on **experience accumulation** — the agent gets better at repeated tasks because it automatically crystallizes successful execution paths into Skills.

<div class="zh-trans">Hermes是一个通用Agent Runtime，强调通过闭环学习实现自我改进。与聚焦控制面（入口、会话、权限）的OpenClaw不同，Hermes聚焦于**经验积累**——Agent在重复任务中自动将成功执行路径结晶为Skills，从而持续变强。</div>

## How It Works

Hermes operates on a closed learning loop:
1. Agent receives a task and executes it
2. Successful execution paths are automatically distilled into "procedural memory" (Skills)
3. Next time a similar task arrives, the Agent leverages those Skills to take fewer wrong turns
4. FTS5 session search allows the agent to query past conversations for relevant context

Six execution backends: local, Docker, SSH, Daytona, Singularity, Modal.

User modeling via Honcho integration provides persistent user profiles across sessions.

<div class="zh-trans">Hermes运行在闭环学习循环上：1.Agent接收任务并执行；2.成功执行路径自动提炼为"程序性记忆"（Skills）；3.下次相似任务来临时，Agent利用这些Skills少走弯路；4.FTS5会话搜索让Agent查询历史对话获取相关上下文。支持六种执行后端：本地/Docker/SSH/Daytona/Singularity/Modal。通过Honcho集成实现跨会话的持久用户建模。</div>

## Why It Matters

**Comparison with OpenClaw:**

| Dimension | OpenClaw | Hermes |
|-----------|----------|--------|
| Core asset | Gateway control plane | Learning execution loop |
| Skills semantics | Human-defined, system-governed | Agent auto-created from success paths |
| Security | Trust model + config audit | Defense-in-depth, container isolation |
| Strength | Multi-inlet + multi-device governance | Long-term task self-improvement |

Migration: `hermes claw migrate` can import OpenClaw personas, memory, skills, allowlist — but this transfers configuration, not workflow.

<div class="zh-trans">与OpenClaw对比：核心资产（Gateway控制面 vs 学习执行循环）；Skills语义（人定义 vs Agent自动创建）；安全方案（信任模型 vs 纵深防御）；适用场景（多入口治理 vs 长期任务自我改进）。迁移：`hermes claw migrate`可导入OpenClaw配置，但不等于迁移使用方式。</div>

## Connections

- [[otgo/concepts/openclaw|OpenClaw]] — the system Hermes is most directly compared to
- [[otgo/sources/openclaw-vs-hermes-20260412|OpenClaw vs Hermes 对比文章]] — source analysis
