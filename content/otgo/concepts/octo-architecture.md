---
title: Octo 系统架构
topic: otgo
type: concept
created: 2026-04-27
tags: [架构, Space, Chat, Bot, 部署拓扑, ClawHub, 连接密度]
---

# Octo 系统架构

## 定义

Octo 系统架构由四个独立系统构成，以 Space / Chat / Bot 为 MVP 核心三概念，采用两种部署场景（用户自建 vs. Octo 代管）。核心设计原则：**Octo 是协作层，不是工具**——它成为所有工作工具之间的协作基础设施，不替代工具。

---

## 运作方式

### 四个独立系统

| 系统 | 定位 | 职责边界 |
|---|---|---|
| **Auth (IDaaS)** | 统一账号认证 | 注册/登录/SSO/用户身份管理。纯粹——只管账号，不管 Space、不管外部工具、不管 Bot Token |
| **Octo IM** | 协作核心 | Chat（四端）/ Space / Bot 管理 / Bot Token / Browser Extension |
| **OpenClaw** | Agent Runtime | Bot 的运行环境——Skill 加载 / CLI 执行 / LLM 调用 / Sub-Agent 编排 |
| **ClawHub** | Plugin 分发 | CLI + SKILL.md + Channel Adapter 的注册 / 版本管理 / 分发 |

```
               Auth (IDaaS)
                  ↑ 认证
                  |
  用户(四端) → Octo IM ←── Channel Adapter ──→ OpenClaw ←── Skill ── ClawHub
                                                  ↓
                                           CLI 操作外部工具
```

**边界清晰**：Octo 不知道 Bot 内部怎么运行（OpenClaw 的事）；不知道外部工具的业务逻辑；不管外部工具的认证；Auth 只管账号认证。

### 两种部署场景

**场景 A：用户自建 OC**

OC 是用户自行安装的工具。Octo 不能假设其存在，也无法主动连接（不知道 IP、端口）。所有通信由 OC 侧主动发起（OC → Octo API）。核心功能（IM、子系统）在没有 OC 时完整可用；Agent 功能需用户主动配置连接后才可用。

**场景 B：Octo 代管云端 OC**

用户注册时 Octo 自动 provision 独立 OC 实例（每用户一个隔离实例）。Agent 功能开箱即用。OC 在架构上仍然独立——独立进程、独立数据；Octo 管 provisioning，不介入 Agent 内部行为。

| 维度 | 场景 A | 场景 B |
|------|--------|--------|
| Octo 能否假设 OC 存在 | 不能 | 能 |
| Agent 功能默认状态 | 不可用（需配置） | 开箱即用 |
| Agent 活动展示 | OC 主动上报（安装 Monitor Skill） | 同左 |
| Agent 实时 Terminal 流 | 不可行（OC 不暴露查询 API） | 不可行 |

**两种场景可以共存**：技术用户选择自建 OC（更多控制权），普通用户使用代管 OC（更低门槛）。

### 三个 MVP 核心概念

**Space（目标导向的协作空间）**

Space 是 Octo IM 内部的组织单元——一群人 + Bot + 相关频道/对话，以目标/项目为中心。

- 不是"群"（以人为中心聊天），而是以目标/项目为中心的工作单元
- 成员管理、频道管理、Bot 准入在 Space 内
- **数据完全隔离**——两个 Space 各自有独立数据，互不可见
- 类比：Slack Workspace / Discord Server，但面向目标而非话题

**Chat（协调通道）**

Chat 是人与人、人与 Bot 之间的协调通道，也是当前 Orchestration 的实现手段。

- 对齐意图（"帮我改第三章"）+ 汇报结果（"改好了"）
- 实际工作由 Bot 通过 CLI 在外部工具/子系统完成
- Chat 不可停用——它是 Bot 参与协作的核心通道
- **Orchestration 不等于 Chat**：两者解耦，Chat 是当前实现手段，未来可演化

**Orchestration 演化路径**：
- Phase 1（MVP）：Chat 是唯一通道
- Phase 2：Chat + Event Bus（子系统变更事件，Agent 可订阅）
- Phase 3：Chat + Event Bus + Agent-to-Agent Protocol
- Phase 4：Chat 退到人的监督通道，日常编排由事件和协议驱动

Chat 占比逐渐下降，但架构不需要变更。

**Bot（AI 协作参与者）**

Bot 是 Space 中的 AI 协作参与者。

- Agent Runtime 由 **OpenClaw** 管理（架构独立于 Octo 服务端）
- 通过 Chat 接收指令，通过 CLI 操作外部工具
- 操作语义是 **best-effort**：多步操作某步失败，已执行步骤的结果保留，不自动回滚
- 当前推荐权限模型 C（数字分身）：审计追溯最清晰，子系统集成最简单，与伦理学 v2.5 §15 对齐

Bot 与 Discord Bot 的代际差距：Discord Bot 是 API 自动化（响应命令、执行预定义逻辑），Octo Bot 是 Agent（理解自然语言、主动参与协作、跨子系统协调）。

### 信息流：两条路径

```
路径一（人→UI）：  人 → 子系统 UI → 子系统 API → 数据变更
路径二（人→Agent）：人 → Chat → Octo API → Agent Runtime → CLI → 子系统
```

两条路径消费同一套子系统 API，操作等价。路径二在场景 B 默认可用，在场景 A 需配置。

**典型协作流**：

```
张三在 Chat："@Bot 帮我建个任务跟踪 Auth 的 review"
  → Octo Chat API 推送给 Agent Runtime
  → Agent Runtime 通过 CLI/API 调用 Task 子系统
  → Task 子系统创建任务，返回结果
  → Agent Runtime 回复："✓ 已创建任务：Auth Review · 指派给张三"
  → Web App 右侧自动显示刚创建的任务卡片
  → 张三点击切到 Task 全屏，或 Extension 并排操作
```

### 连接密度模型

Octo 的平台价值随连接密度增长：

```
Level 1: 人 ↔ 人（基本 IM）
Level 2: 人 ↔ Bot（Agent 协作）
Level 3: 人 ↔ Bot ↔ 子系统（操作闭环）  ← MVP 目标
Level 4: Bot ↔ 子系统 A + 子系统 B（跨系统编排）
Level 5: ISV 子系统 ↔ 平台生态（开放 Hub）
```

每提升一个 Level，平台的不可替代性显著增加。

### 语义契约

**子系统数据是 ground truth**：Chat 和子系统状态不一致时，子系统赢。Chat 是对话历史，不是状态存储。

**Chat 是审计日志**：线性特性在协调场景是劣势，但在审计场景是优势——完整记录谁说了什么、Bot 做了什么、结果如何。

**Bot 操作 best-effort**：不保证事务性，部分失败不自动回滚，Bot 向用户报告实际执行情况。

**渲染是子系统的事**：Octo 不理解子系统的内容类型，只提供外跳 + Extension 桥梁；Task 子系统自己决定怎么渲染任务。

### 强约束（不可妥协）

| 约束 | 理由 |
|------|------|
| 子系统架构独立 | 生态战略：ISV 低门槛接入，可独立运行 |
| Agent Runtime 不在 Octo 范围内 | 部署拓扑决定，不是设计偏好 |
| CLI 是 Agent 统一交互协议 | 不绑定底层实现，不需要 Artifact 抽象 |
| Space 数据完全隔离 | 安全和多租户的基础 |
| 子系统之间不直接通信 | 防止耦合；跨子系统数据组合通过人或 Bot 完成 |

---

## 为什么重要

### 两类独立子系统（2026-04-27 补充）

子系统进一步分为两类：

**公共板块**（架构上独立于 IM，但属于产品公共模块）：

| 模块 | 说明 |
|------|------|
| Context 管理 | 让人高效整理自己的 Context，持久化到 FileSpace（仅停留在 Agent Memory 里学习效率不够高） |
| FileSpace | Context 背后的独立存储系统 |
| A2A 事项管理 | 管理 Agent-to-Agent 交互的 GUI，给 Human-in-the-loop 用；位置：Channel/Thread 右侧**第三栏**，与阅读文件等功能共享屏幕空间 |

**外部独立子系统**（外部 SaaS 工具）：飞书文档、Google Docs、Overleaf、Octic（会议纪要）、妙啊（内容营销）……前提假设是**未来所有主流产品都会 CLI 化**，Octo 不改变用户工具习惯，而是作为串联不同工具之间的协作枢纽。

**信息流转示例**：Octic 会议纪要 → 提炼 To-do → 流转到 FileSpace → 部分 To-do 流转到妙啊。此场景下用户屏幕左侧是妙啊，Octo 以浏览器插件形态出现在右侧。

### 独立子系统 vs. 前端组件：一个根本性选择

前端组件模式：所有功能以 UI 组件形式运行在同一进程，组件是平台内部积木——不能独立存在，必须用平台技术栈。

独立子系统模式（Octo 的选择）：每个功能是独立产品——有自己的 repo/UI/API/数据库；通过标准接口（Auth + REST + CLI + SKILL.md）接入 Octo，也完全可以脱离 Octo 独立运行。

**生态战略**：Discord 把 Bot 作为一等公民，任何人可以写 Bot 扩展功能，从游戏语音工具演化成社区操作系统。Slack 的 2000+ 个 App 比 Slack 自己做 2000 个功能强得多。独立子系统把这个逻辑推到极致：ISV 用任何技术栈构建子系统，接入 Octo，既服务自己的用户也被 Octo 的 Bot 操作。

**类比冯诺伊曼架构**：CPU、内存、外设各自独立实现，只需 follow 统一总线接口。Octo 的子系统关系同构——Task 子系统不需要知道 Docs 子系统怎么渲染，它们通过标准接口与平台通信。

### 竞争路径与架构韧性

Octo 选了 Chat-Centric + Agent-Native + 独立子系统，但这不是唯一的路：

- **Canvas/空间优先**（Notion, Linear）：子系统 UI 独立可用，不依赖 Chat 入口——这是防线
- **Agent-Native 非 Chat**（Cursor, Devin）：这是演化方向而非威胁，Orchestration≠Chat 从第一天已解耦；Chat 是窗口期内最务实选择（Agent 尚不能全自主，人需要在 loop 内校准）
- **Search/Feed**（Google Workspace）：信息消费场景，不与协作场景竞争

**设计原则：Chat 是当前 Orchestration 的最佳实现，但架构不能与 Chat 耦合。子系统的独立性是对所有竞争路径的通用防线。**

**创新者窘境视角**：企微/飞书知道这些功能方向是对的，但无法直接做——受制于庞大 B 端用户习惯改变的阻力（克里斯坦森创新者窘境）。Octo 的差异化赌注正是在此处切入。

---

## Connections

- [[otgo/sources/octo-arch-v11.2-20260420|Octo 概念架构文档 v11.2]] — 完整来源文档
- [[otgo/sources/octo-product-vision-20260427|Octo 产品架构与战略补充]] — 两类子系统划分、A2A 管理 GUI 位置、信息流转示例
- [[otgo/concepts/browser-extension|Browser Extension]] — 四端之一，零集成成本协作桥梁
- [[otgo/concepts/dual-native|Dual-Native Design]] — 底层为 Agent 而建，表层为人而渲染的设计哲学
- [[otgo/concepts/cli-decoupling|CLI 解耦]] — View/CRUD 分离，Skill 即契约
- [[otgo/concepts/skill-marketplace|Skill Marketplace]] — ClawHub 是第四个独立系统，负责 Plugin 分发
- [[otgo/concepts/multi-cc-collab|多 CC 协作模式]] — Bot 在 Octo 架构中的协作编排
- [[otgo/concepts/wukong-protocol|悟空协议]] — H↔H/H↔A/A↔A 通信的传输层
- [[otgo/concepts/digital-avatar|数字分身]] — Bot 权限推荐模型 C，一 Bot 一主人
- [[otgo/concepts/item|事项 (Item)]] — 子系统中结构化工作单元的设计
