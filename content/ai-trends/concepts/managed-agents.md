---
title: Managed Agents
topic: ai-trends
type: concept
created: 2026-05-09
tags: [anthropic, agent-cloud, runtime, business-model, saas-to-agent]
---

# Managed Agents

## 定义

Anthropic 推出的托管型 Agent 产品形态：开发者只需定义模型、工具和指令，Agent 便在 Anthropic 托管的云端环境中运行，通过 session 执行任务、通过 events 回传状态。

这是 Anthropic 第一次将 Harness 做成托管产品，标志其从"按量收费的 API 公司"向"Agent 云公司 / Agent OS"的结构性转变。

## 运作方式

**开发者视角**：
1. 定义 Agent：指定模型 + 工具集 + 系统指令
2. 提交至 Anthropic 托管环境
3. 通过 session 触发任务执行
4. 通过 events 订阅状态回传（进度、结果、错误）

**商业模式转变**：
- 之前：卖 Token（按 API 调用量计费）
- 现在：卖 Runtime（托管 Agent 运行环境）
- Claude Code 可在本地运行，也可在 Anthropic 云端运行，session 管理与状态留存于 Anthropic 侧
- 用户粘性远高于单纯 API 调用：迁移成本包括 session 历史、工具配置、训练信号

**战略意义**：
- Anthropic 的 Agent Loop 哲学：充分信任模型，Harness 做到极简（与 LangChain 时代 rule-based 控制形成对比）
- 托管化让 Anthropic 沉淀"Agent 使用数据"，形成训练信号优势

## 为什么重要

- **对 Anthropic**：从单次 Token 消耗变为持续订阅的 Runtime 服务，ARPU 和粘性双升
- **对开发者**：无需自建 Agent 基础设施（调度/状态管理/错误恢复），降低门槛
- **对行业**：Anthropic 从 AI Model 公司向 AI Platform 公司进化，类比从 AWS EC2 向 SageMaker 的演进
- **竞争格局**：谁先锁定 Agent Runtime 层，谁就掌控 Agent 时代的"操作系统入口"

## Connections

- [[ai-trends/sources/era-of-agent-shixiang-2026-may|拾象 AGI 洞察 2026-05]] — 本概念的主要来源
- [[ai-trends/concepts/coding-agent|Coding Agent]] — Managed Agents 由 Coding Agent 的成功催生
- [[ai-trends/concepts/to-human-to-agent|To Human / To Agent]] — Managed Agents 是 To Agent 基础设施的核心节点
- [[ai-trends/concepts/ai-harness-infrastructure|AI Harness 基础设施]] — Harness 的托管化形态
