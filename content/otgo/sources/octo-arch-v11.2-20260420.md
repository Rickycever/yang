---
title: Octo 概念架构文档 v11.2
topic: otgo
type: source
created: 2026-04-27
tags: [架构, octo, Space, Bot, 部署拓扑, ClawHub]
---

# Octo 概念架构文档 v11.2

**作者**：齐静春（架构师）
**日期**：2026-04-20（合成版）
**版本**：v11.2（基于 v10.2 PDF + v11 合成）
**定位**：概念架构（What & Why）——拉齐技术和产品团队对 Octo 的共识

> v11.2 关键新增：§二 产品形态（四端）、§五 系统全景（四个独立系统，含 ClawHub）、§九 架构原则（六条核心 + 九条展开）、§八 演进路径（含 ClawHub 正式化）

---

## 摘要

本文档定义 Octo 的概念架构，是技术和产品团队对 Octo 是什么、为什么这样设计的共识文档。核心定位：**Octo 是人与 AI Agent 协作的工作平台——所有工作工具之间的协作层**，不替代现有工具，而是成为它们之间的协作层。

---

## 核心要点

### 1. Octo 是什么

三个关键词：
- **Agent-Native**：从第一天为人和 Agent 的协作而设计，每个设计决策同时通过"人好不好用"和"Agent 好不好接"两道检验
- **协作 Hub**：Octo 不做具体工作（不做文档编辑器、表格引擎、代码 IDE），提供协作基座（Auth + Space + Orchestration），通过集成外部工具完成实际工作
- **独立子系统**：每个功能模块是独立产品——有自己的 UI/API/CLI/数据库；既能融入 Octo，也能脱离独立运行

和现有产品的核心差异：飞书/钉钉是 IM + 办公套件；Notion 是文档/数据库；Discord 是 Chat + Bot 生态；**Octo 是协作层 + 独立工具，AI 是 Space 协作参与者而非 Bot。**

### 2. 四端产品形态

| 端 | 定位 |
|---|---|
| **Web** | IM 主场 + 全功能（Space 管理、Bot 管理、Chat、子系统集成） |
| **iOS / Android** | 移动 IM + 通知 + 轻量品鉴（查看摘要、给反馈） |
| **Browser Extension** | 把 Octo 的协作能力注入到用户正在使用的任何 Web 工具旁边 |

四端共享：同一个 Auth、同一个 Space、同一个 Chat、同一套 Bot 管理。

### 3. 四个独立系统

| 系统 | 定位 | 职责边界 |
|---|---|---|
| **Auth (IDaaS)** | 统一账号认证 | 注册/登录/SSO/用户身份管理——纯粹，只管账号 |
| **Octo IM** | 协作核心 | Chat（四端）/ Space / Bot 管理 / Bot Token / Extension |
| **OpenClaw** | Agent Runtime | Bot 的运行环境——Skill 加载 / CLI 执行 / LLM 调用 |
| **ClawHub** | Plugin 分发 | CLI + SKILL.md + Channel Adapter 的注册/版本管理/分发 |

关系图：Auth 提供认证 → Octo IM 通过 Channel Adapter 与 OpenClaw 双向路由消息 → OpenClaw 从 ClawHub 拉取 Skill → OpenClaw 通过 CLI 操作外部工具。

### 4. 两种部署场景

**场景 A（用户自建 OC）**：OC 是用户自己安装的工具，Octo 不能假设其存在。所有通信由 OC 侧主动发起，Agent 功能需用户主动配置后才可用。

**场景 B（Octo 代管云端 OC）**：用户注册时 Octo 自动 provision 独立 OC 实例，Agent 功能开箱即用。OC 在架构上仍然独立（独立进程、独立数据），但运维由 Octo 管理。

无论哪种场景：OC 都是独立进程，Octo 服务端不直接控制 Agent 内部行为（LLM 调用、Session 编排）。

### 5. 三个 MVP 核心概念

**Space（目标导向的协作空间）**：不是"群"（人为中心），是以目标/项目为中心的协作单元，含成员 + Bot + 频道；数据完全隔离。

**Chat（协调通道）**：对齐意图（"帮我改第三章"）+ 汇报结果（"改好了"）；实际工作由 Bot 通过 CLI 在外部工具完成。Chat 是当前 Orchestration 的实现手段，两者解耦。

**Bot（AI 协作参与者）**：Agent Runtime 由 OpenClaw 管理（架构独立）；通过 Chat 接收指令，通过 CLI 操作子系统；操作 best-effort（非事务性）；推荐模型 C（数字分身）。

### 6. 架构六条核心原则

| # | 原则 | 说明 |
|---|------|------|
| 1 | 不替代工具，注入到工具旁边 | Extension 在用户正在使用的工具旁提供协作能力 |
| 2 | View 和 CRUD 解耦 | View 是工具的 UI，CRUD 是 Bot 通过 CLI 操作 |
| 3 | IM 是协调通道，工具是工作台 | IM 对齐意图和汇报结果，工具完成实际工作 |
| 4 | Agent Runtime 外置 | Bot 由 OpenClaw 管理，Octo 只通过 Chat 通信 |
| 5 | Auth 纯粹 | 只管用户账号认证，Bot Token 归 IM 管 |
| 6 | 零集成成本 | 任何 Web 工具天然可交互，Extension 无需工具适配 |

**强约束（不可妥协）**：子系统架构独立、Agent Runtime 不在 Octo 范围内、CLI 是 Agent 统一交互协议、Space 数据完全隔离、子系统之间不直接通信。

### 7. Orchestration 演化路径

- Phase 1（MVP）：Chat 是唯一 Orchestration 通道
- Phase 2：Chat + Event Bus（子系统变更事件推送，Agent 可订阅）
- Phase 3：Chat + Event Bus + Agent-to-Agent Protocol（Agent 间直接协调）
- Phase 4：Chat 退到人的监督通道，日常编排由事件和协议驱动

Chat 在每个阶段都存在，但占比逐渐下降。**这个演化不需要架构变更——因为 Orchestration 和 Chat 从第一天就是解耦的。**

### 8. 信息流与连接密度

两条信息路径：
- 路径一（人→UI）：人 → 子系统 UI → 子系统 API → 数据变更
- 路径二（人→Agent）：人 → Chat → Octo API → Agent Runtime → CLI → 子系统

两条路径消费同一套子系统 API，操作等价。

连接密度模型（平台价值随之增长）：
```
Level 1: 人 ↔ 人（基本 IM）
Level 2: 人 ↔ Bot（Agent 协作）
Level 3: 人 ↔ Bot ↔ 子系统（操作闭环）  ← MVP 目标
Level 4: Bot ↔ 子系统 A + 子系统 B（跨系统编排）
Level 5: ISV 子系统 ↔ 平台生态（开放 Hub）
```

### 9. 语义契约

- **子系统数据是 ground truth**：Chat 和子系统状态不一致时，子系统赢
- **Chat 是审计日志**：完整记录谁说了什么、Bot 做了什么、结果如何
- **Bot 操作是 best-effort**：部分失败不自动回滚，Bot 报告实际执行情况
- **渲染是子系统的事**：Octo 不理解子系统内容类型，只提供外跳 + Extension 桥梁

### 10. 竞争路径分析与架构韧性

| 竞争路径 | 代表 | 我们的回应 |
|---------|------|----------|
| Canvas/空间优先 | Notion、Linear | 子系统 UI 独立可用，不依赖 Chat 入口——用户可全屏使用子系统 |
| Agent-Native 但非 Chat | Cursor、Devin | 这是演化方向，不是威胁；子系统独立性 + Orchestration≠Chat 保留了演化空间 |
| Search/Feed 优先 | Google Workspace | 信息消费场景，不与协作场景竞争 |

**最值得警惕的是 Agent-Native 但非 Chat**：窗口期判断（2026-2030）— Agent 可靠性还不到"全自主"水平，Chat 作为 Orchestration Layer 是当前最务实选择。架构设计了三道防线：子系统独立性、Orchestration≠Chat、窗口期判断。

---

## Connections

- [[otgo/concepts/octo-architecture|Octo 系统架构]] — 本文档的核心架构概念沉淀
- [[otgo/concepts/browser-extension|Browser Extension]] — 四端之一，协作桥梁
- [[otgo/concepts/dual-native|Dual-Native Design]] — §八 的完整展开（底层为 Agent，表层为人）
- [[otgo/concepts/cli-decoupling|CLI 解耦]] — View/CRUD 解耦的详细论证
- [[otgo/concepts/skill-marketplace|Skill Marketplace]] — ClawHub 是第四个独立系统，负责 Skill 分发
- [[otgo/concepts/multi-cc-collab|多 CC 协作模式]] — Bot 协作的实现机制
- [[otgo/concepts/digital-avatar|数字分身]] — Bot 权限模型 C，与伦理学 v2.5 §15 对齐
- [[otgo/entities/wu-minghui|吴明辉 (辉哥)]] — OTGO 战略负责人
