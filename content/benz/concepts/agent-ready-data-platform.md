---
title: Agent-Ready 数据中台
topic: benz
type: concept
created: 2026-04-15
tags: [agent-ready, mcp, data-platform, ai-agent, multi-modal-storage]
---

# Agent-Ready 数据中台

## 定义

Agent-Ready 数据中台是一种专为 AI Agent 自主调用而设计的数据基础设施范式，区别于传统"服务人的决策工具"设计假设。

**传统数据平台的设计假设**：数据 → 报表 → 人 → 决策（人在中间，查询被动触发，延迟可接受，结果只需人类可读）

**Agent-Ready 的设计假设**：AI Agent 需要主动、高频调用数据能力（每次对话可能触发数十次工具调用），并要求接口标准化、存储全模态、结果可追溯。

Agent-Ready 不是在传统数据中台上打 AI 补丁，而是从底层重新设计数据暴露方式。

---

## 运作方式

### 三个核心设计要素

**1. MCP 标准接口（数据能力工具化）**

MCP（Model Context Protocol，Anthropic 发布的开放协议）将所有数据能力封装为标准化工具（Tool），Agent 无需适配具体底层系统：

- 圈人工具：自然语言/条件 → 用户 ID 列表
- 标签查询工具：批量返回标签值
- 事件检索工具：用户行为事件序列
- 知识库检索工具：语义检索 + 置信度

好处：Agent 框架无关——Claude、GPT-4、自研 LLM 均可调用，无需二次适配。

**2. 全模态统一存储（按意图路由）**

单一存储引擎无法满足 Agent 的多样化查询需求，需三路并存：

| 存储引擎 | 适用场景 | 典型技术 |
|------|------|------|
| 结构化 OLAP | 精确业务查询（销量、用户数、转化率） | StarRocks |
| 向量数据库 | 语义相似检索（内容推荐、知识问答） | Milvus |
| 图数据库 | 实体关系推理（用户-车辆-经销商关系链） | Neo4j |

同一次 Agent 调用可跨存储引擎联合查询，由意图路由层自动分发。

**3. 完整可观测性（结果可追溯）**

每次 Agent 调用数据均记录：
- 调用的 MCP 工具名称和参数
- 实际执行的查询（SQL 或向量查询）
- 数据来源表/文档、版本、更新时间
- 返回行数和置信度标注

这是 AI 结论从"不可信黑盒"到"可解释可审计"的关键。

### 三类 Agent 的数据调用模式

**营销 Agent**：自然语言策略 → MCP 圈人工具 → 画像标签工具 → 渠道触达 → 结果写回标签系统

**问数 Agent（ChatBI）**：用户提问 → Text-to-SQL（Schema 感知，只读沙箱）→ 数据结果 + 执行 SQL + 来源表

**工作流 Agent（LangGraph）**：复杂任务拆解 → 多工具并行调用 → 跨系统协作 → 全流程审计日志

---

## 为什么重要

**范式转变**：CDP/数据中台行业正在经历从"服务人"到"服务 Agent"的转型。随着企业 AI Agent 的普及，数据平台的核心用户从"人"变成了"Agent"，而现有平台的设计假设（接口、存储、可观测性）都基于人类使用场景，根本性地不适配 Agent 的高频、多模态、可追溯需求。

**竞争格局重塑**：传统 CDP 厂商（神策/GrowingIO）和通用大数据平台（AWS/阿里云）均不具备原生的 MCP 接口和 Agent 可观测性，需要二次封装。Agent-Ready 是新一代数据平台的核心分水岭。

**"AI 幻觉"的数据层解法**：大模型幻觉问题的根本原因之一是数据不可追溯。Agent-Ready 架构通过完整的调用链记录和置信度标注，让"AI 说了什么"和"数据依据是什么"可以对应，从数据层解决可信度问题。

**冷启动保障**：新租户或数据稀疏场景下，可降级到规则驱动（Rule-based），不完全依赖历史数据训练——这是与竞品的关键差异之一。

---

## 与传统 CDP 的关系

Agent-Ready 数据中台不是替代 CDP，而是 CDP 的升维：

- CDP 解决"数据从哪里来、长什么样"（数据统一、OneID、360° 视图）
- Agent-Ready 解决"数据怎么被 Agent 用"（接口标准化、存储全模态、调用可观测）

两者是底座与接口层的关系：先有 CDP 的数据底座，再有 Agent-Ready 的接口层让 Agent 能使用这些数据。

---

## Connections

- [[benz/sources/miaozhen-agent-data-platform-whitepaper-202604|明略科技 Agent-Ready 数据中台白皮书]] — 本概念的来源文件
- [[adidas/entities/miaozhen|秒针 / 明略科技]] — 提出本概念的公司
- [[adidas/concepts/dmp-cdp|DMP / CDP]] — Agent-Ready 的数据底座前提
- [[benz/concepts/marketing-automation|Marketing Automation（营销自动化）]] — 营销 Agent 的上层业务场景
- [[otgo/concepts/hermes|Hermes]] — 明略内部 Agent 框架，本架构的 Agent 调用方
