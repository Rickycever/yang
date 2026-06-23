---
title: 润典企业智能体解决方案
topic: agentic-player
type: source
created: 2026-06-23
tags: [enterprise-agent, wecom, restaurant, private-domain, mcp]
---

# 润典企业智能体解决方案

This is a 40-page solution deck for a restaurant-oriented enterprise agent named 小厨bot. It centers on WeCom as the primary interface and positions the agent as a store and operations copilot for ordering, stock checks, sold-out handling, reconciliation, repairs, knowledge lookup, and KPI-driven decision support.
<div class="zh-trans">这是一份约 40 页的餐饮行业企业智能体解决方案材料，产品名为小厨bot。材料以企微作为主入口，将智能体定位为门店与营运协同助手，覆盖订货、盘点、售罄、对账、报修、知识查找和 KPI 决策支持等场景。</div>

The deck's core proposition is to reduce system switching and make complex operations executable through natural language. Store staff can complete multi-step tasks in chat, while H5 cards, backend services, and system APIs handle the actual workflow execution.
<div class="zh-trans">材料的核心主张，是减少多系统切换，让复杂操作通过自然语言直接完成。门店员工在聊天窗口里就能发起多步骤任务，而 H5 卡片、后台服务和系统 API 负责真正的流程执行。</div>

## 摘要

The solution emphasizes six business outcomes: lower user friction, faster operational decisions, one-click task handling, private deployment for data security, improved store operations efficiency, and a path from manual management to intelligent optimization. It is especially focused on restaurant stores, online private-domain operations, and internal operational coordination.
<div class="zh-trans">该方案强调六个业务结果：降低使用门槛、加快营运决策、一键处理任务、私有化部署保障数据安全、提升门店运营效率，以及从人工管理走向智能优化的演进路径。它特别面向餐饮门店、线上私域运营和内部营运协同。</div>

At the architecture level, the deck describes a deterministic agent stack: LLM, context management, tool calling, Agent Loop, MCP, Sub-Agent, Skill reuse, RAG, permission control, and auditability. The practical implementation uses WeCom chat, H5 cards, backend routing, model gateways, knowledge bases, and business-system APIs.
<div class="zh-trans">在架构层面，材料描述的是一套确定性的 Agent 技术栈：LLM、上下文管理、工具调用、Agent Loop、MCP、Sub-Agent、技能复用、RAG、权限控制和审计能力。落地实现则结合企微聊天、H5 卡片、后台路由、模型网关、知识库和业务系统 API。</div>

## 核心要点

### 1. WeCom becomes the operational front door

The deck uses WeCom 1v1 chat and group chat as the single entry point for store, operations, and headquarters users. This keeps communication, task initiation, confirmation, and follow-up inside one familiar channel.
<div class="zh-trans">材料把企微的一对一聊天和群聊作为门店、营运和总部用户的统一入口。这样，沟通、发起任务、确认执行和后续反馈都被收敛在一个熟悉的渠道里。</div>

### 2. Operational tasks are decomposed into executable workflows

Examples include transfer orders, sold-out and recovery actions, damage write-offs, repairs, work-order lookup, and incident confirmation. The agent turns natural language into task drafts, cards, and API calls, so frontline staff can complete work without navigating multiple systems.
<div class="zh-trans">典型任务包括调拨、售罄与恢复、报损、报修、工单查询和案件确认。智能体把自然语言转成任务草稿、卡片和 API 调用，让一线员工无需在多个系统之间跳转就能完成工作。</div>

### 3. The operating model moves through three stages

The deck describes a progression from human-driven decision support, to 7x24 intelligent alerting, to dual-robot autonomous optimization. The long-term goal is a PDCA loop where diagnosis, execution, measurement, and iteration are all partially automated.
<div class="zh-trans">材料给出了一个三阶段演进：从人工驱动的决策支持，到 7x24 智能预警，再到双机器人自动优化。长期目标是形成 PDCA 闭环，让诊断、执行、衡量和迭代都具备一定自动化能力。</div>

### 4. Private deployment is a hard requirement

The solution repeatedly stresses that sensitive restaurant data should stay inside the enterprise network. The deployment stack includes K8s, model gateways, Milvus, PostgreSQL, Redis, Kafka, and multi-cloud or private-cloud compatibility.
<div class="zh-trans">材料反复强调餐饮敏感数据必须留在企业内网。部署栈包括 K8s、模型网关、Milvus、PostgreSQL、Redis、Kafka，并支持多云与私有化环境。</div>

## Connections

- [[agentic-player/overview|Agentic Player]] — 本主题入口
- [[agentic-player/concepts/wecom-store-agent|WeCom Store Agent]] — 企微门店智能体模式
- [[agentic-player/concepts/enterprise-agent-architecture|Enterprise Agent Architecture]] — 架构底座
- [[agentic-player/concepts/human-at-the-helm|Human-at-the-helm]] — 人机协作治理方式
- [[agentic-player/entities/xiaochubot|小厨bot]] — 本方案中的产品实体
