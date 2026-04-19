---
title: Agent 专用 Infra——两类确定性机会
topic: shixiang
type: concept
created: 2026-04-19
tags: [infra, agent, browseruse, security, infrastructure]
---

# Agent 专用 Infra

## 定义

当前互联网 Infra 是为**人**设计的，对 Agent 处于"敌对"状态。这一结构性缺口催生了两类确定性机会：**Infra of Agent**（构建 Agent 的基础设施）和 **Infra for Agent**（给 Agent 使用的基础设施）。

---

## 运作方式

**当前 Infra 对 Agent 的"敌对"表现**：

| 问题类型 | 具体表现 |
|---------|---------|
| 网络层 | Cloudflare 等防火墙频繁拦截，IP 被封锁 |
| 安全层 | 缺乏专门的审计接口、权限管控、适配浏览器环境 |
| 支付层 | 无 Agent 友好的支付接口（典型案例：OpenClaw 在 Polymarket 重复下注 40 次，亏损 $14,000） |
| 执行层 | Long-horizon 任务容易"断片"，需人类反复介入 |
| 节奏层 | 机器执行太快，人类决策/反馈速度成为瓶颈，人是全流程最慢的环节 |

**两类机会**：

**Infra of Agent**（构建 Agent 的设施）：
- Agent 专用浏览器（如 BrowserUse）：显著节省 Token 消耗并提升任务成功率，已吸引大量 ChatGPT 请求
- Agent 专用 Sandbox：从 Code Interpreter 到 Sandbox 的演进，推高 CPU 使用量
- 注意：CPU/Sandbox 机会壁垒较低，云厂商/模型厂商均可原生提供，定价无溢价

**Infra for Agent**（给 Agent 用的设施）：
- 专用网络（能通过防火墙的代理/路由）
- Agent 支付系统（有明确的成功/失败返回参数）
- 安全与审计框架

**高阶需求：主动对齐（Proactive Alignment）**：
- 未来 Infra 需具备"建模用户"能力：Agent 主动构建用户数字分身，理解思维习惯和隐性知识
- 用户不再需要每次费力写 Prompt 来对齐 AI
- 字节跳动等大厂正在探索相关产品（工具自动优化用户指令 + 联动 Post-training 能力）

---

## 为什么重要

**对创业者**：Agent Infra 是 2026 年确定性最高的赛道之一。当前 Agent 就像"性能极佳的宝马跑车，被迫跑在崎岖山路上"，改造道路（Infra）比改造汽车（模型）更确定性。

**对企业**：Agent 在"裸奔"状态下执行高权限任务（如读取私钥、操作股票账户）会带来巨大安全风险。安全 Infra 是企业级 Agent 采用的前提条件。

**对投资者**：Infra of Agent 中，BrowserUse 类产品已验证商业可行性；Infra for Agent 中，Agent 专用支付/安全网关是最先出现的结构性需求。

---

## Connections

- [[shixiang/sources/best-ideas-agent-2026-feb|Best Ideas Agent 讨论（2026-Feb）]] — 本概念出处
- [[shixiang/concepts/proactive-agent|Proactive Agent]] — Infra 需要支撑 Proactive Agent 的持续运行
- [[nvidia-gtc-2026/concepts/agent-as-a-service|Agent-as-a-Service]] — AaaS 的实现依赖成熟的 Agent Infra
- [[otgo/overview|OTGO]] — octo 平台是 Infra of Agent 的企业侧实践
