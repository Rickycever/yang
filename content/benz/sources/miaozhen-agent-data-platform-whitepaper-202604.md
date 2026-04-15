---
title: 明略科技 Agent-Ready 数据中台技术架构白皮书
topic: benz
type: source
created: 2026-04-15
tags: [miaozhen, agent-ready, mcp, data-platform, ai-agent]
---

# 明略科技 Agent-Ready 数据中台技术架构白皮书

**来源**：为 AI Agent 服务的数据中台——技术架构白皮书
**形式**：DOCX，约 10 章
**日期**：2026 年 4 月，版本 1.0
**保密级别**：机密，仅限内部及授权客户使用

---

## 文档定位

本白皮书定义了明略科技 Agent-Ready 数据中台的完整技术架构，是明略产品从"服务人的决策工具"向"驱动 AI Agent 自主决策的基础设施"转型的技术宣言。

核心论点：**传统数据中台不是给 Agent 用的**——接口碎片、存储单模态、调用不可观测，这三个结构性缺陷使现有平台无法支撑 Agent 时代的数据需求。

---

## 传统数据平台的三大结构性缺陷

| 缺陷 | 具体表现 | 对 Agent 的影响 |
|------|------|------|
| 接口碎片化 | 各系统各自暴露 REST API，格式/认证/错误处理不一致 | Agent 需为每个系统单独适配，维护成本高 |
| 存储单模态 | 只有关系型/OLAP 数据库，无向量库和图谱 | 无法处理语义检索，无法推理实体关系 |
| 黑盒不可观测 | 数据调用无溯源，结果无置信度标注 | Agent 输出无法解释，"幻觉"无从排查 |

---

## 解决方案：Agent-Ready 数据中台

核心三要素：
1. **MCP 标准协议**：数据能力以工具（Tool）形式封装，Agent 框架无关调用
2. **全模态统一存储**：结构化 + 向量 + 图谱同时在线，按意图自动路由
3. **完整可观测性**：每次 Agent 调用均有来源、版本、置信度可追溯

**适用的三类 Agent 场景：**

| Agent 类型 | 典型用户 | 核心诉求 |
|------|------|------|
| 营销 Agent | 品牌营销/CRM 运营 | 自动完成圈选、旅程编排、多渠道触达 |
| 问数 Agent（ChatBI） | 业务分析师、管理层 | 自然语言查数据，得到可信的分析结论 |
| 工作流 Agent | IT 运维、业务流程自动化 | 多工具协作完成复杂跨系统任务 |

---

## 竞品对比（能力矩阵）

| 能力维度 | 明略 Agent-Ready | 传统 CDP（神策/GrowingIO） | 通用大数据平台（AWS/阿里云） |
|------|------|------|------|
| MCP 标准接口 | ✅ 原生支持 | ❌ 自定义 API | ⚠️ 需二次封装 |
| 全模态存储 | ✅ 结构化+向量+图谱 | ❌ 仅结构化 | ⚠️ 各自独立 |
| 数据可观测性 | ✅ 调用溯源+置信度 | ❌ 无 Agent 追踪 | ⚠️ 基础日志 |
| 多租户隔离 | ✅ 行列级权限 | ✅ 租户隔离 | ✅ 账号级 |
| 冷启动能力 | ✅ 降级到规则驱动 | ❌ 需历史数据 | ❌ 无降级机制 |

---

## 五层架构设计

| 层级 | 名称 | 核心职责 | 关键技术 |
|------|------|------|------|
| L0 | 数据接入层 | 多源适配、格式标准化、质量校验 | Kafka · Flink CDC · 多源适配器 |
| L1 | 统一存储层（全模态） | 结构化/实时/向量/图谱/冷存统一管理 | StarRocks · Flink · Milvus · Neo4j · Hive/Iceberg |
| L2 | 数据治理层 | 元数据管理、数据血缘、多租户隔离、审计 | Keycloak RBAC · 数据字典 · 血缘图谱 |
| **L3** | **Agent 接口层（核心）** | **标准化暴露数据能力给 Agent 调用** | **MCP Server · Text-to-SQL · RAG · OpenAPI 网关** |
| L4 | 应用层 | 三类 Agent 上层业务逻辑 | 营销 Agent · ChatBI · LangGraph 工作流 Agent |

### L3 Agent 接口层——三路并行

**MCP Server（标准化工具接口）**
将数据能力封装为 MCP 标准工具：
- 圈人工具：自然语言/结构化条件 → 用户 ID 列表
- 标签查询工具：批量返回标签值
- 事件检索工具：用户行为事件序列
- 知识库检索工具：语义检索 + 置信度返回

**Text-to-SQL 引擎（问数 Agent 核心）**
- Schema 感知：自动加载租户数据字典，避免幻觉 SQL
- 查询沙箱：生成的 SQL 在只读沙箱执行，防数据污染
- 结果溯源：返回结果同时附带执行 SQL 和来源表信息

**RAG 检索服务（非结构化知识问答）**
- 基于 Milvus 向量库，支持文本/图片/视频多模态
- 检索结果附带文档来源/版本/更新时间
- 支持父子分块策略，提升长文档召回率

---

## 三大架构决策（ADR）

**ADR-01：采用 MCP 而非自定义 API**
- 问题：Agent 如何以统一方式调用来自不同底层存储的数据能力？
- 背景：MCP 是 Anthropic 发布的开放协议，已获阿里云 DataWorks、Cursor、主流 Agent 框架采用
- 选定：MCP Server——Agent 框架无关，Claude/GPT-4/自研 LLM 均可直接调用
- 放弃：自定义 REST API（生态锁定）、GraphQL（对 Agent 而言过重）

**ADR-02：三路存储并存 + 意图路由**
- 问题：不同查询需求差异极大，单一存储引擎无法兼顾
- 选定：StarRocks（精确查询）+ Milvus（语义检索）+ Neo4j（关系推理），按意图自动路由
- 路由规则：业务查询 → StarRocks；语义搜索 → Milvus；实体关系推理 → Neo4j
- 关键：同一次 Agent 调用可跨存储引擎联合查询

**ADR-03：行列级多租户隔离**
- 问题：SaaS 多租户场景下数据安全 vs 部署成本如何平衡？
- 选定：行列级权限（RLS/CLS）+ 租户 Schema 隔离混合模式
- 放弃：纯物理隔离（每租户独立集群，成本不可控）
- 实现：StarRocks RLS + Keycloak RBAC，新租户开通无需新增存储实例

---

## 三阶段演进路线

| 阶段 | 时间 | 建设重点 | 阶段成果 |
|------|------|------|------|
| Phase 1 | 0–6 个月 | 结构化底座 + Text-to-SQL | 问数 Agent Demo 可用，自然语言查数据 |
| Phase 2 | 6–12 个月 | 向量库 + MCP 标准化 + 营销 Agent | 三路存储全线，营销 Agent 圈选-触达闭环 |
| Phase 3 | 12 个月+ | 知识图谱 + Multi-Agent 协作框架 | 工作流 Agent 上线，跨系统任务全自动化 |

---

## 技术选型说明

| 组件 | 选型 | 理由 | 放弃方案 |
|------|------|------|------|
| OLAP 引擎 | StarRocks | 亿级秒查，原生 RLS，国内落地丰富 | ClickHouse（RLS 弱）、Doris |
| 流处理 | Flink + Kafka | 行业标准，Flink CDC 直接对接数据库变更 | Spark Streaming（延迟高）|
| 向量数据库 | Milvus | 开源领先，多模态，LangChain 生态集成好 | Pinecone（闭源，数据出境风险）|
| 图数据库 | Neo4j | 最成熟，Cypher 表达力强，有 LLM 插件 | NebulaGraph（国产，生态小）|
| 权限管理 | Keycloak | 开源企业级 IAM，OIDC/OAuth 2.0 完整支持 | Auth0（SaaS，数据出境风险）|
| Agent 编排 | LangGraph | 有状态图编排，适合复杂多步骤工作流 | AutoGen（微软，生态较小）|

---

## 数据安全与合规

- **传输加密**：TLS 1.2/1.3
- **存储加密**：AES-256
- **数据主权**：所有数据存储于中国境内合规云（阿里云/华为云），数据不出境
- **全操作审计**：Agent 每次调用均记录操作人/租户/调用时间/返回行数，不可篡改
- **Agent 调用安全**：MCP Tool 独立权限控制；Text-to-SQL 只读沙箱；调用频率限制（防 DDoS 式数据拉取）

---

## 快速启动路径（12周）

- W1-2：搭建 StarRocks + Flink，接入一个核心数据源
- W3-4：接入 Text-to-SQL 引擎 + LLM（Claude/GPT），跑通问数 Agent Demo
- W5-8：MCP Server 封装，接入第二数据源，完成基础多租户隔离
- W9-12：Milvus 接入，RAG 上线，完成 Phase 1 验收

**关键成功因素：**
- 数据质量先行（数据治理和字典要在 Agent 接入前完成）
- Schema 文档化（字段注释越详细，Text-to-SQL 越准确）
- 安全评审前置（多租户隔离在 Phase 1 就定义，后期修改成本极高）

---

## 重要披露：明略 Agent 战略进展

> "明略已完成 **Hermes Agent** 架构调研、**AgentPortal** 产品内测、**MCP 数据接口标准化**等前期工作，具备从架构设计到产品落地的完整工程能力。"

这表明 Hermes 是明略内部 Agent 框架名称（参见 OTGO wiki 中的 Hermes 竞品分析），AgentPortal 是面向客户的 Agent 管理入口产品。

---

## Connections

- [[benz/concepts/agent-ready-data-platform|Agent-Ready 数据中台]] — 本文件提出的核心架构概念
- [[adidas/entities/miaozhen|秒针 / 明略科技]] — 本文件作者
- [[benz/sources/miaozhen-cdp-pitch-2026|明略科技 CDP 产品提案 2026]] — 同一产品线的通用 Pitch
- [[benz/sources/miaozhen-benz-cdp-ma-proposal-20260412|明略科技奔驰 CDP+MA 完整方案]] — 本架构在具体项目中的落地
- [[otgo/concepts/hermes|Hermes]] — 本文件揭示 Hermes 为明略自研 Agent 框架
- [[tools/concepts/llm-wiki|LLM Wiki]] — MCP 作为数据接口标准，与 Agent 工具链密切相关
