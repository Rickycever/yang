---
title: GEA 企业级智能体架构
topic: ai-business
type: concept
created: 2026-04-10
tags: [GEA, 通用Agent, 上下文系统, 编排, 企业架构]
---

# GEA 企业级智能体架构

## Definition

GEA (Generative Enterprise Architecture) is a framework for deploying AI in enterprises centered on **one general-purpose agent + rich enterprise context + industry skills**, with an orchestration layer to coordinate multiple models and a Creative Reasoning Model for balancing convergent and divergent thinking.

<div class="zh-trans">GEA（通用企业级智能体架构）是一个以**一个通用Agent+丰富企业上下文+行业技能**为核心的企业AI部署框架，配合编排层协调多个模型，以及平衡收敛与发散思维的创意推理模型。</div>

## How It Works

**Architecture stack:**
```
General-Purpose Agent (code-capable)
    ├── Skills (industry skill library)
    └── Context (enterprise context)

Orchestration Layer
    ├── Model orchestration: which model handles which task
    ├── Task planning: Lead Agent (plan) + Sub Agents (execute)
    └── Creative Reasoning Model: diverge → converge
```

**Context = competitive moat:**
- Structured data (databases, tables) = the enterprise's single source of truth
- Unstructured data (images, video, decision logs, evaluation processes) = the enterprise's real Context — self-learning and accumulating over time

<div class="zh-trans">架构栈：通用Agent（会写代码）+技能库+上下文→编排层（模型编排+任务规划+创意推理模型）。上下文=竞争护城河：结构化数据（唯一真相）+非结构化数据（图文视频+决策过程+评价过程）=企业真正的Context，动态自我学习，越积越厚。</div>

**Counter-intuitive agent hierarchy:**
Research shows Lead Agent (planning) does NOT need the most advanced model — it needs to be good at planning and coordination. Sub Agents (execution) MUST use the strongest models available. This is counter-intuitive but validated in the literature.

<div class="zh-trans">反直觉的Agent层级：研究表明Lead Agent（规划）不需要最先进的模型——需要擅长规划和协调。Sub Agent（执行）必须用最强模型。这是反直觉的，但已在文献中验证。</div>

**Creative Reasoning Model:**
Traditional AI models excel at convergent tasks (math, definite answers). Commerce requires both convergence AND divergence (exploring uncertain but high-potential directions — James March's "Exploration vs Exploitation," 1991 Stanford). GEA's Creative Reasoning Model introduces divergence mechanisms at the orchestration layer, enabling parallel hypothesis testing at low cost.

<div class="zh-trans">创意推理模型：传统AI模型擅长收敛型任务（数学、确定答案）。商业需要收敛与发散并举（探索不确定但高潜力方向——James March 1991探索与利用理论）。GEA的创意推理模型在编排层引入发散机制，支持低成本并行假设测试。</div>

## Why It Matters

This architecture directly addresses the most common enterprise AI failure: organizations buy specialized agents for each function and end up with a zoo of disconnected tools. GEA's unified context system means the longer an enterprise uses the platform, the richer its context becomes — creating compounding competitive advantage that is hard to replicate.

<div class="zh-trans">该架构直接解决了最常见的企业AI失败：为每个职能购买专用Agent，最终得到一堆互不相连的工具。GEA的统一上下文系统意味着企业使用平台越久，上下文越丰富——创造难以复制的复利竞争优势。</div>

## Connections

- [[ai-business/concepts/context-system|上下文系统]] — the most critical component of this architecture
- [[ai-business/sources/gea-speech-20260410|GEA演讲]] — source
- [[otgo/concepts/octo|octo]] — OTGO's implementation of a similar general-purpose agent platform
- [[otgo/concepts/lonxia|龙虾 (Lobster)]] — OTGO's sub-agent model parallels the Sub Agent layer here
