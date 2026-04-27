# Octo — 概念架构文档 v11.2

**作者：** 齐静春（架构师）
**日期：** 2026-04-20（合成版）
**版本：** v11.2（基于 v10.2 PDF + v11 合成）
**状态：** Draft — 合成版
**定位：** 概念架构（What & Why）— 拉齐技术和产品团队对 Octo 的共识

> **v11.2 合成说明**
>
> - v11（2026-04-02）：早期 Workbench 框架，含部署拓扑、Bot 权限模型 A/B/C、子系统生态详论、完整演进路径。
> - v10.2（2026-04-09 PDF）：收敛版本，补齐四端产品形态、ClawHub 作为第四个独立系统、六条架构原则的简化表达，定位从 "Workbench" 调整为"协作层"。
> - 本 v11.2 以 v11 为底，插入 v10.2 的四端、ClawHub、简化定位、架构原则 六项关键信息。**原 v11 的论证（部署拓扑、Bot 权限模型、子系统生态、竞争路径）全部保留**——v10.2 的简化不等于丢弃细节，只是改变表达重心。
> - v11.2 关键新增：§二 产品形态（四端）、§五 系统全景（四个独立系统，含 ClawHub）、§九 架构原则（六条核心 + 九条展开）、§八 演进路径（含 ClawHub 正式化）
> - **推荐阅读顺序**：想快看架构 → 读 §一～§二 + §五 + §九 核心六条；想深入 → 全读。

---

## 一、Octo 是什么

**Octo 是一个人与 AI Agent 协作的工作平台——更准确地说，是所有工作工具之间的协作层。**

用户的工作工具已经存在——Jira、Google Docs、Overleaf、飞书文档、GitHub……问题不是缺工具，而是缺一个让人和 AI 在这些工具之间高效协作的层。**Octo 不替代这些工具。Octo 是它们之间的协作层。**

### 三个关键词

**Agent-Native：** 不是在传统协作工具上"加 AI 功能"，而是从第一天就为人和 Agent 的协作而设计。每个设计决策都需要同时通过两道检验——"人好不好用"和"Agent 好不好接"。

**协作 Hub：** Octo 自己不做具体工作（不做文档编辑器、不做表格引擎、不做代码 IDE）。它提供协作基座（Auth + Space + Orchestration），让人和 Agent 在这个基座上协调，然后通过集成的外部工具和子系统完成实际工作。

**独立子系统：** 每个功能模块（任务管理、文档、日历等，或 ISV 接入的第三方工具）都是独立的产品——有自己的 UI、API、CLI、数据库、技术栈。它们既能融入 Octo 成为 Hub 的一部分，也能脱离 Octo 独立运行。

### 和现有产品的区别

| 维度 | 飞书/钉钉 | Notion | Discord | Octo |
|------|---------|--------|---------|------|
| 核心 | IM + 办公套件 | 文档/数据库 | Chat + 社区 + Bot 生态 | 协作层 + 独立工具 |
| AI 角色 | Bot（被 @ 才响应的工具） | AI 块（文档内辅助） | Bot（自动化 + 扩展） | Space 协作参与者 |
| 协作模型 | 人 ↔ 人 | 人 ↔ 人 | 人 ↔ 人 ↔ Bot | 人 ↔ 人 ↔ Agent |
| 功能扩展 | 平台内组件/应用 | Integration | Bot + Activity | 独立子系统/外部工具（可独立运行） |
| 集成门槛 | 用平台 SDK 开发 | 写 API 适配器 | Bot API（Discord 专用） | follow 标准接口即可 |
| 组织单位 | 群/部门 | Workspace/Page | Server/Channel | Space（目标导向） |

---

## 二、产品形态：四个端

**四端完整覆盖：Web（主场）+ iOS + Android + Browser Extension（协作桥梁）。**

| 端 | 形态 | 定位 |
|---|---|---|
| **Web** | Web App | IM 主场 + 全功能（Space 管理、Bot 管理、Chat、子系统集成） |
| **iOS** | Native App | 移动 IM + 通知 + 快速响应（轻量品鉴、查看摘要、给反馈） |
| **Android** | Native App | 移动 IM + 通知 + 快速响应（同上） |
| **Browser Extension** | 浏览器插件 | 把 Octo 的协作能力注入到用户正在使用的任何 Web 工具旁边 |

### Browser Extension 细节

用户在浏览器中打开任何 Web 工具（Jira、Google Docs、Overleaf……），Extension 在旁边提供：

- **Chat 侧边栏**——和 Bot 对话、和同事协调
- **Cmd+K**——在任何页面选中内容，唤起输入框，向 Bot 描述意图
- **引用到 Chat**——选中内容一键引用到当前对话
- **页面上下文感知**——自动识别当前页面 URL、标题、选中内容，作为 Bot 操作的上下文

**Web 工具不需要做任何适配。** Extension 通过 Content Script 动态注入功能。

**Extension 是轻量协作桥梁。** 完整的 IM 体验、Space 管理、Bot 管理等在 Web 端。

### 移动端的定位

移动端不做子系统嵌入、不做复杂品鉴——只做 IM 通知 + 轻量审批 + 简要回复。**通知是移动端最重要的产品。**

### 四端关系

```
Web  ←→  Octo 服务端  ←→  iOS / Android
                 ↑
                 └── Browser Extension（通过 Web App 的 Auth 共享登录态）
```

四端共享：同一个 Auth、同一个 Space、同一个 Chat、同一套 Bot 管理。能力差异来自端的物理约束（屏幕大小、输入方式、后台限制），不来自功能设计。

---

## 三、部署拓扑（架构前提）

> 所有架构决策都建立在部署拓扑之上。拓扑决定了组件之间的通信可达性——什么能调什么、什么调不了什么。跳过拓扑直接谈分工，等于在流沙上画蓝图。

### 3.1 两种部署场景

OpenClaw（OC）的部署方式不同，会导致架构约束不同。存在两种部署场景：

**场景 A：用户自建 OC**

用户自行在本机（macOS 等）安装 OC，或在自己的云环境中部署。OC 是用户自己的工具，Octo 无法假设其存在，也无法控制其行为。用户可以选择将 OC 连接到 Octo API，也可以不连接。Octo 端侧（Web / iOS / Android / Extension）可能在完全不同的设备上——用户手机上用 Octo App，而 OC 跑在 Mac 上。

**场景 B：Octo 代管云端 OC**

用户注册成为 Octo 用户时，Octo 在云端自动为其 provision 一套独立的 OC 实例。每个用户一个隔离的 OC 实例，由 Octo 负责创建、配置和生命周期管理。OC 实例在架构上仍然与 Octo 服务端独立（独立进程、独立数据），但 Octo 可以确保其存在且已正确配置。

**两种场景的共性与差异：**

| 维度 | 场景 A（用户自建） | 场景 B（Octo 代管） |
|------|----------------|-----------------|
| OC 的提供者 | 用户自己 | Octo 平台 |
| OC 的部署位置 | 用户本机或用户自管云端 | Octo 管理的云端 |
| Octo 能否假设 OC 存在 | 不能 | 能——Octo 负责 provision |
| OC 与 Octo 的架构关系 | 完全独立 | 架构独立，运维由 Octo 管理 |
| Agent 功能可用性 | 需用户主动配置连接 | 开箱即用 |
| 通信方向 | OC → Octo API（OC 主动） | 已预配置，双向可达 |

无论哪种场景，OC 在架构上都是独立于 Octo 服务端的——独立进程、独立数据、通过 API 通信。区别在于 provisioning 和运维的归属。

### 3.2 拓扑约束

**两种场景共有的约束：**

**约束 1：OC 在架构上独立于 Octo 服务端。** 无论是用户自建还是 Octo 代管，OC 都是独立进程、独立数据、通过 API 与 Octo 通信。Octo 服务端不直接控制 OC 的内部行为（LLM 调用、Session 编排、CLI 执行）。

**约束 2：Octo 端侧与 OC 不在同一设备上。** 用户可能手机上用 Octo App，OC 跑在 Mac 或云端。端侧之间没有直接通信通道，只通过 Octo 服务端 API 间接关联。

**约束 3：Agent Runtime 的内部行为不在 Octo 的设计范围内。** Agent 怎么调 LLM、怎么编排 Sub-Agent、用什么模型——这些是 OC 的事。Octo 通过 API 与 OC 交互，不介入 Agent 内部逻辑。

**场景 A 特有的约束：**

**约束 A1：Octo 不能假设 OC 存在。** 用户可能没有安装 OC，或 OC 不在线。Octo 的核心功能（IM、子系统）必须在没有 OC 的情况下完整可用。Agent 相关功能需要用户主动配置 OC 连接后才可用。

**约束 A2：所有通信由 OC 侧主动发起。** Octo 服务端无法主动连接用户的 OC（不知道 IP、端口、是否在线）。

**场景 B 特有的特性：**

**特性 B1：Octo 可以确保 OC 存在。** 用户注册时 Octo 自动 provision OC，可以假设每个用户都有可用的 OC 实例。Agent 功能开箱即用。

**特性 B2：Octo 管理 OC 的生命周期。** Octo 负责 OC 实例的创建、配置、扩缩容、故障恢复。但不介入 Agent 内部行为。

### 3.3 拓扑对产品设计的影响

基于以上约束，可以推导出不同场景下的产品能力差异：

| 能力 | Octo 服务端自身 | 场景 A（用户自建 OC） | 场景 B（Octo 代管 OC） |
|------|-------------|-----------------|------------------|
| IM / Chat | ✓ | ✓ | ✓ |
| Auth / Space 管理 | ✓ | ✓ | ✓ |
| 子系统 API + UI | ✓ | ✓ | ✓ |
| Bot 身份管理 | ✓ | ✓ | ✓ |
| Bot 理解意图并执行操作 | — | 需用户配置 OC 连接 | ✓ 开箱即用 |
| Bot 通过 CLI 操作子系统 | — | 需用户配置 OC 连接 | ✓ 开箱即用 |
| Agent 活动状态（主动上报） | — | ✓ OC 通过 CLI 主动 report | ✓ OC 通过 CLI 主动 report |
| Agent 实时 Terminal 流（拉取式） | — | ✗ OC 无对外 API | ✗ OC 无对外 API |

**关键结论：**

- **场景 B 解决了 Agent 基础功能的可用性问题**——Bot 对话和操作子系统开箱即用。
- **Agent 活动展示走"主动上报"路径**，不走"Octo 轮询/探针"路径。OC 内部的 Session、Terminal 状态不对外暴露查询 API；但 Agent 可以安装对应 Skill，通过 `octo monitor report` 等 CLI 主动上报。**所有上报必须是用户授意的**（伦理学：不做肉鸡）。
- **场景 A 下需要降级设计**——没有 OC 连接时，Octo 的 IM、子系统仍完整可用，但 Agent 相关功能不可用。
- **两种场景可以共存**——高级用户/企业用户可能选择自建 OC（更多控制权），普通用户使用 Octo 代管的云端 OC（更低门槛）。

---

## 四、核心概念

> v10.2 把核心概念收敛为 **Space / Chat / Bot** 三个，作为 MVP 阶段最小自洽集合。本章按此结构组织，并在每个概念下保留 v11 的详细展开（子系统、Skill、Auth Service 等）。

### 4.1 Space（目标导向的协作空间）

Space 是 Octo IM 内部的组织单元——一群人 + Bot + 相关频道/对话。

- Space 是 Octo 内部概念，外部工具不需要知道
- 类似 Slack Workspace / Discord Server
- 成员管理、频道管理、Bot 准入在 Space 内
- **数据完全隔离**——两个 Space 都启用了 Task 子系统，各自有独立的任务数据，互不可见

传统 IM 的组织单位是"群"——以人为中心，本质是"这些人在一起聊天"。Space 是更高阶的抽象——以目标/项目为中心。Space 里不只有人，还有 Agent、工具、上下文，Space 本身就是一个工作单元。

**Space 的演化空间：** 当前 Space 约等于团队/项目级别的隔离边界。未来 Space 可以细化——一个 Space 内的 Channel 可以对应不同的工作流，类似 Discord 的 Server → Channel 结构，但以目标而非话题组织。

### 4.2 Chat（协调通道）

Chat 是人与人、人与 Bot 之间的协调通道，也是当前 Orchestration 的实现手段。

- 群聊 + 私聊
- IM 负责对齐意图（"帮我改第三章"）和汇报结果（"改好了，你看看"）
- 实际工作由 Bot 通过 CLI 在外部工具/子系统中完成
- Chat 不可停用——它是 Bot 参与协作的核心通道

**Orchestration vs Chat：** Chat 是技术实现手段（IM 消息能力），Orchestration 是职责定位（协调编排）。未来 Orchestration 可能不只是 Chat——还包括事件通知、状态同步、Agent 间直接通信等协调机制。但 MVP 阶段 Orchestration = 基于 Chat 的协调。

**Orchestration 的演化路径：**

- Phase 1：Chat 是唯一的 Orchestration 通道（MVP）
- Phase 2：Chat + Event Bus（子系统变更事件推送，Agent 可订阅）
- Phase 3：Chat + Event Bus + Agent-to-Agent Protocol（Agent 间无需经过 Chat 直接协调）
- Phase 4：Chat 退到人的监督通道，日常编排由事件和协议驱动

Chat 在每个阶段都存在，但占比逐渐下降。这个演化不需要架构变更——因为 Orchestration 和 Chat 从第一天就是解耦的。

### 4.3 Bot（AI 协作参与者）

Bot 是 Space 中的 AI 协作参与者。

- Bot 的 Agent Runtime 由 **OpenClaw** 管理（架构独立于 Octo 服务端）
- Bot 通过 Chat 接收指令，通过 CLI 操作外部工具
- Octo 不关心 Bot 内部怎么运行——只通过 Chat 和 Bot 通信

**不随权限模型变化的共识：**
- Bot 的 Agent Runtime 在架构上独立于 Octo 服务端（见 §3）。场景 B 下由 Octo 代管但架构不变
- Bot 对子系统的操作和人通过 UI 的操作是等价的（消费同一套 API）
- Bot 的操作是 best-effort（尽力而为），不保证事务性

**随权限模型变化的内容：** Bot 的身份定义、权限边界、所有权归属取决于 Bot 权限模型的选择（见附录 A）。

**Bot vs Discord Bot 的区别：** Discord 的 Bot 本质上是 API 自动化——响应命令、执行预定义逻辑。Octo 的 Bot 是 Agent——理解自然语言、主动参与协作、能在多个子系统间协调。这是第四代和第五代的代际差距。

### 4.4 子系统（Sub-System / 外部工具 / Application）

独立的功能模块或外部工具。每个子系统是一个完整的独立产品。

**子系统的五个特性：**
- **独立完整**——有自己的 UI、API、CLI、数据库、技术栈、repo、CI/CD
- **可独立运行**——脱离 Octo 也是一个可用的产品
- **CLI 必须 UI 可选**——至少提供 CLI（给 Agent 用），UI 按需提供（给人用）
- **可发现**——提供 SKILL.md，让 Bot 学会使用它
- **可追溯**——记录所有数据变更的操作者和时间

**子系统的准入条件**——什么能成为一个子系统：
1. 拥有独立的数据实体（不是另一个子系统数据的附属）
2. Bot 可以独立地对它执行有意义的操作
3. 对用户有独立的价值主张（不是"按钮级"功能）

**接入标准（ISV follow 这些就能接入）：**

| 接口 | 作用 | 面向谁 |
|------|------|--------|
| REST API | 数据读写 | 人的 UI + Agent 的 CLI |
| CLI | 命令行操作 | Agent（通过 Agent Runtime exec） |
| SKILL.md | 教 Agent 使用 CLI | Agent Runtime 加载 |
| Web UI | 人的操作界面 | 人（独立访问或通过 Extension 协作） |
| Auth 协议 | 身份认证 | 平台统一认证 |

**一方和三方子系统无差别**——架构不区分。相同的 Auth、相同的接口标准、相同的隔离方式。

### 4.5 Skill（能力契约）

Skill 是子系统与 Bot 之间的契约——一个 SKILL.md 文档，教 Bot 如何使用子系统的 CLI。Skill 是子系统侧的产出物，Agent Runtime 侧加载和使用。

**ClawHub 负责 Skill 的注册、版本管理和分发**（见 §5）。

### 4.6 Auth Service（认证服务）

平台层基础设施，提供统一的身份认证和授权。以下在所有方案中都成立：

- 用户身份管理
- Space 管理
- Token 签发与验证
- 子系统启用状态管理

**v10.2 原则补充：Auth 纯粹**——只管用户账号认证，不管 Space（归 IM）、不管外部工具（各自鉴权）、不管 Bot Token（归 IM）。

---

## 五、系统全景

### 5.1 四个独立系统

| 系统 | 定位 | 职责边界 |
|---|---|---|
| **Auth (IDaaS)** | 统一账号认证 | 注册 / 登录 / SSO / 用户身份管理 |
| **Octo IM** | 协作核心 | Chat（四端）/ Space / Bot 管理 / Bot Token / Extension |
| **OpenClaw** | Agent Runtime | Bot 的运行环境——Skill 加载 / CLI 执行 / LLM 调用 |
| **ClawHub** | Plugin 分发 | CLI + SKILL.md + Channel Adapter 的注册 / 版本管理 / 分发 |

### 5.2 系统间关系

```
                Auth (IDaaS)
                   ↑ 认证
                   |
   用户(四端) → Octo IM ←── Channel Adapter ──→ OpenClaw ←── Skill ── ClawHub
                                                   ↓
                                            CLI 操作外部工具
```

- **Octo IM → Auth**：用户登录认证
- **Octo IM ↔ OpenClaw**：通过 Channel Adapter 双向消息路由（用户在 Chat 说话 → Bot 收到；Bot 回复 → Chat 显示）
- **OpenClaw → ClawHub**：拉取 Skill（CLI + SKILL.md），学习如何操作外部工具
- **OpenClaw → 外部工具**：通过 CLI 执行操作

### 5.3 边界清晰

- Octo 不知道 Bot 内部怎么运行（OpenClaw 的事）
- Octo 不知道外部工具的业务逻辑（工具自己的事）
- Octo 不管外部工具的认证（用户自己已登录）
- Auth 只管账号认证，不管 Space、不管外部工具

### 5.4 这四个系统与 v11 的映射

v11 中的"平台层"现在明确拆为三个系统：Auth（独立 IDaaS）、Octo IM（Chat + Space + Bot 管理 + Extension）、ClawHub（v11 没有独立提出，v10.2 新增）。

OC 是独立的 Agent Runtime（v11 已有此定位），ClawHub 补齐了 Skill/Plugin 的分发侧。

---

## 六、IM 是协调通道，工具是工作台

IM 适合协调，不适合干活。没有人在群里写代码或排版论文。

- **IM**：对齐意图（"帮我改第三章"）+ 汇报结果（"改好了，你看看"）
- **工具**：实际操作（Bot 通过 CLI 操作，人通过 Web UI 操作）
- **Extension**：两者之间的桥梁（在工具页面上引用内容到 Chat，在 Chat 中接收结果后跳转到工具查看）

### View 和 CRUD 解耦

- **View**（人看的）= 工具自身的 Web UI
- **CRUD**（Bot 干的）= 通过 CLI 操作工具

两者独立，互不依赖。

### 详细论证（保留 v11 §5.2）

一个常见的问题：既然人和 Agent 可以用自然语言对话，为什么不直接做一个聊天界面就够了？反过来——既然有子系统的专业 UI，为什么还需要 Chat？

**Chat 的角色是协调，不是干活。** 和人类的工作方式一样——没有人在微信群里写代码、排版论文或审核表格。群里说"帮我建个任务"，Agent 去子系统里操作，然后回群里说"建好了"。

| 工作类型 | IM 做不了 | 需要子系统提供 |
|---------|---------|-----------|
| 深度操作 | 拖拽看板、批量编辑表格 | 子系统的专业 UI |
| 空间化展示 | 对话流是线性的 | 看板/日历/甘特图等视图 |
| 精确反馈 | "第三列那个数不对"——描述位置痛苦 | 在 UI 上直接指（Cmd+K） |
| 全局监控 | 对话串行，无法并行展示 | 仪表盘/概览视图 |

**但 Chat 做三件子系统 UI 做不到的事：**

| 协调能力 | 为什么需要 Chat |
|---------|-------------|
| 实时意图对齐 | 多人 + 多 Agent 快速达成共识，Canvas 模式的交互效率远不如 Chat |
| Agent 校准 | Agent 还不够可靠时，人需要在 loop 里持续校准——而校准最自然的方式就是对话 |
| 操作可观测性 | Chat 记录天然是审计日志，Agent 做了什么、为什么做、结果如何——全部可追溯 |

所以 Octo 的布局是：Chat 为主（协调中心）+ 子系统为辅（工作台）。

- **Chat 占主工作区**——协调是高频动作，人和 Agent 的协作主要在这里发生
- **外部工具全屏或 Browser Extension 并排**——深度操作时，在外部工具自己的 Web UI 中进行，Extension 在旁边提供 Thread 上下文和 Cmd+K
- **Octo 原生内容**（md / code diff / image / PDF）可在 Web App 右栏原生预览

---

## 七、为什么是"独立子系统"而不是"前端组件"

这是整个架构中最关键的设计选择。

**前端组件模式：** 所有功能以 UI 组件的形式运行在同一个进程中，通过事件总线联动。组件是平台内部的积木——不能独立存在、不能独立部署，必须用平台的技术栈。

**独立子系统模式（我们的选择）：** 每个功能是一个独立的产品——有自己的 repo、自己的 UI（任何技术栈）、自己的 API、自己的数据库。它通过标准接口（Auth + REST + CLI + SKILL.md）接入 Octo，但也完全可以脱离 Octo 独立运行。

**为什么选后者？**

**类比冯诺伊曼架构：** CPU、内存、外设各自独立实现，只需要 follow 统一的总线接口。CPU 不需要知道硬盘怎么存数据，硬盘不需要知道 CPU 怎么计算。各自极致优化，互不干扰。Octo 的子系统就是这种关系——Task 子系统不需要知道 Docs 子系统怎么渲染文档，它们通过标准接口与平台通信。

**生态战略：** 平台的终极护城河是生态。微信小程序、Slack App Directory、Discord Bot 生态，都指向同一方向：平台自己不做所有子系统，提供标准接口让第三方扩展。

- Discord 做对了什么？Bot 是一等公民，任何人可以写 Bot 扩展功能，平台不需要自己做所有事。结果：从游戏语音工具演化成社区操作系统。
- Slack 做对了什么？开放 API 和集成生态，让 Chat 成为其他工具的汇聚点。2000+ 个 App 比 Slack 自己做 2000 个功能强得多。

我们的独立子系统模式把这个逻辑推到极致：ISV 做一个"Jira 桥接器"子系统，只需要 follow 标准接口——用 Go、Rust、Python 什么都行。然后它既能独立运行服务自己的用户，也能接入 Octo 被 Bot 操作。

---

## 八、Dual-Native：底层为 Agent 而建，表层为人而渲染

每个子系统必须同时服务两个用户：人和 Agent。

- **给人用：** UI（Web、桌面、移动端——子系统自己选）
- **给 Agent 用：** CLI + SKILL.md

这不是"先做 UI 再补 CLI"——两者同等重要。CLI 是子系统的最低要求，没有 CLI 的子系统 Agent 无法操作，接入 Octo 的价值减半。

**CLI 是 Agent 与子系统之间的统一交互协议。** Agent 不关心子系统的底层实现——数据存在数据库、文件系统还是第三方 API 后面，Agent 都不需要知道。`task create --title "xxx"`、`glab issue create`、`docs write file.md` 都是 CLI 命令，Agent 统一通过 CLI 操作。

**不需要额外的 Artifact 抽象层。** 一种常见的误区是将所有数据抽象为"Artifact/文件"（如文档、表格、代码、媒体四类），并规定"Agent 直接操作文件"。这个抽象有三个问题：

1. **不通用。** 子系统的数据不一定是"文件"。Task 的数据是任务记录，Calendar 的数据是日程——这些是结构化数据，不适合抽象成文件。硬套 Artifact 反而丢失结构信息。
2. **绑定底层实现。** "Agent 直接操作文件"假设了数据以文件形式存在。但子系统可能用数据库、用第三方 API——Agent 不应关心也不需要关心。
3. **CLI 已经够了。** CLI 封装了底层实现细节，是 Agent 与子系统之间已经足够的交互协议。在 CLI 之上再加一层 Artifact 概念，是多余的抽象。

**渲染是子系统自己的事。** Task 子系统知道怎么渲染任务（看板/列表/时间线），Docs 子系统知道怎么渲染文档。Octo 不需要理解子系统的内容类型——它只提供外部跳转 + Extension 协作桥梁，子系统在自己的 UI 里自己渲染。这保持了子系统的独立性。

---

## 九、架构原则

### 9.1 六条核心原则（v10.2 简化表达）

| # | 原则 | 说明 |
|---|------|------|
| 1 | **不替代工具，注入到工具旁边** | Extension 在用户正在使用的工具旁提供协作能力 |
| 2 | **View 和 CRUD 解耦** | View 是工具的 UI，CRUD 是 Bot 通过 CLI 操作 |
| 3 | **IM 是协调通道，工具是工作台** | IM 对齐意图和汇报结果，工具完成实际工作 |
| 4 | **Agent Runtime 外置** | Bot 由 OpenClaw 管理，Octo 只通过 Chat 通信 |
| 5 | **Auth 纯粹** | 只管用户账号认证，Bot Token 归 IM 管 |
| 6 | **零集成成本** | 任何 Web 工具天然可交互，无需集成 |

### 9.2 九条展开原则（v11 详细版）

| # | 原则 | 说明 |
|---|------|------|
| 1 | 子系统完全独立 | 独立产品，可融入 Octo 也可独立运行。子系统之间不通信 |
| 2 | CLI 是 Agent 的统一交互协议 | Agent 通过 CLI 操作子系统，不关心底层实现。不需要额外的 Artifact 层 |
| 3 | Skill 即契约 | 子系统提供 SKILL.md 教 Bot 使用 CLI，Agent Runtime 加载执行 |
| 4 | Auth 是基础设施 | 统一认证，具体模式待定 |
| 5 | Agent Runtime 不在 Octo 范围内 | 拓扑决定：OC 架构独立于 Octo 服务端，Octo 提供 API，不介入 Agent 内部行为 |
| 6 | Orchestration 是协调中心 | 基于 Chat 实现，负责协调编排，子系统负责干活 |
| 7 | 渲染归子系统 | Octo 不理解子系统内容，只提供外跳 + Extension 协作桥梁 |
| 8 | 开放 Hub 而非封闭花园 | ISV follow 标准接口即可接入，不要求使用平台技术栈 |
| 9 | Chat 可退，架构不变 | Orchestration 不等于 Chat，架构为 Chat 退到后台留演化空间 |

### 9.3 强约束（不可妥协）

| 约束 | 理由 |
|------|------|
| 子系统架构独立 | 生态战略：ISV 低门槛接入，子系统可独立运行 |
| Agent Runtime 不在 Octo 范围内 | 部署拓扑决定，不是设计偏好 |
| CLI 是 Agent 统一交互协议 | 不绑定底层实现，不需要 Artifact 抽象 |
| Space 数据完全隔离 | 安全和多租户的基础，不可降级 |
| 子系统之间不直接通信 | 防止耦合，保持独立性 |

### 9.4 可演化的设计选择

| 设计选择 | 当前实现 | 演化方向 |
|---------|---------|---------|
| Orchestration 实现 | 基于 Chat | Chat + Event Bus + Agent-to-Agent Protocol |
| 布局 | Chat 为主 | Chat 比重可下降，子系统全屏可成为主模式 |
| Bot 权限模型 | 推荐模型 C（数字分身） | 可引入模型 A（Bot 即应用）要素 |

### 9.5 必须统一的平台能力

以下能力由 Octo 平台层统一提供，所有子系统必须 follow，不可自行实现：

| 能力 | 提供者 | 为什么必须统一 |
|------|--------|------------|
| 身份认证 | Octo Auth | 单点登录，用户和 Bot 统一身份 |
| Space 数据隔离 | Octo 平台 | 安全边界不可由子系统自定义 |
| CLI 接口标准 | 子系统 follow 规范 | Agent 需要一致的交互方式 |
| SKILL.md 格式 | 子系统 follow 规范 | Agent 需要标准化的能力发现机制 |

---

## 十、竞争路径与架构韧性

> 我们选了 Chat-Centric + Agent-Native + 独立子系统。但这不是唯一的路。以下三条竞争路径各有合理性——架构需要对它们保持韧性，而不是赌对一条路。

### 10.1 Canvas/空间优先

**代表：** Notion、Miro、Linear、Coda

**主张：** 工作的核心交互不是"对话"，而是"结构化空间"。文档、看板、白板、数据库才是工作的主战场，Chat 只是辅助通信手段。

**它的合理性：** Chat 是线性的，工作是非线性的。重要决策淹没在聊天流里过两天就找不到了。Notion 的增长证明了大量团队确实把结构化空间当作工作中枢。

**我们的回应：** 这正是"子系统 UI 必须独立可用"的设计初衷。子系统提供看板、文档、日历等结构化视图——它们不是 Chat 的附属品，而是独立的专业工作台。如果用户更习惯在子系统全屏视图中工作，完全可以——Chat 退到通知和例外处理的角色。架构不强迫用户从 Chat 入口操作。

### 10.2 Agent-Native 但不 Chat-Centric

**这条最值得警惕。**

**代表趋势：** Cursor（AI 嵌入编辑器）、Devin（自主 Agent）、Computer Use（直接操作 UI）

**主张：** AI Agent 的交互不一定要走 Chat。Agent 可以直接嵌入子系统 UI（Cursor 的 AI 不在 Chat 里，在编辑器里），或者根本不需要人实时交互（给目标自己跑）。Chat 是因为 Agent 还不够聪明才需要的"降级交互"。

**它的合理性：** 如果 Agent 能力足够强，Chat 确实可能退化为低频的"目标设定"界面，日常工作中人直接在各个子系统 UI 里操作，Agent 嵌入式辅助。Cursor 的成功不是因为 Chat，而是因为 AI 直接在你的工作上下文中操作。

**我们的回应：** 这条路径不是威胁，是我们的演化方向。架构设计了三道防线：

1. **子系统独立性**——每个子系统都有完整的 UI + API，天然支持"Agent 嵌入子系统 UI"的模式。未来子系统内部集成 Agent 能力时，架构不需要改。
2. **Orchestration 不等于 Chat**——Orchestration 是协调编排的职责，Chat 是当前的实现手段。未来 Orchestration 可能演化为事件驱动 + 状态同步 + Chat 三者并存，Chat 的比重可以下降。
3. **窗口期判断**——Agent 可靠性还没到"全自主"水平的这个窗口期（至少 2026—2030），Chat 作为 Orchestration Layer 是最务实的选择。人需要在 loop 里校准 Agent，对话是最低摩擦的校准方式。

### 10.3 Search/Feed 优先

**代表：** Google Workspace、算法推荐系统

**主张：** 不需要主动"对话"或"组织空间"，系统基于算法推送需要的信息。

**我们的回应：** 适合信息消费场景，不适合协作场景。协作需要双向交互和即时反馈，和 Octo 的目标场景不重叠。不构成直接竞争。

### 10.4 架构韧性总结

| 竞争路径 | 架构韧性策略 |
|---------|----------|
| Canvas/空间优先 | 子系统 UI 独立可用，不依赖 Chat 入口 |
| Agent-Native 非 Chat | Orchestration ≠ Chat，子系统可独立集成 Agent |
| Search/Feed | 不同场景，不构成竞争 |

**设计原则：Chat 是当前 Orchestration 的最佳实现，但架构不能与 Chat 耦合。子系统的独立性是对所有竞争路径的通用防线。**

---

## 十一、信息流

### 两条路径

```
路径一（人 → UI）：    人 → 子系统 UI → 子系统 API → 数据变更
路径二（人 → Agent）：  人 → Chat → [Octo API] → Agent Runtime → CLI → 子系统
```

两条路径消费同一套子系统 API，操作等价。

**路径二的可用性因部署场景不同：**
- **场景 B（Octo 代管 OC）：** 路径二默认可用。Agent Runtime 已预配置并连接，用户注册即可使用 Agent 功能。
- **场景 A（用户自建 OC）：** 路径二需要用户主动配置 OC 连接 Octo API。未配置时，用户回退到路径一。

### 协作流（典型场景）

```
张三在 Chat 说："@Bot 帮我建个任务跟踪 Auth 的 review"
    ↓
Octo Chat API 将消息推送给已连接的 Agent Runtime
    ↓
Agent Runtime 通过 CLI/API 调用 Task 子系统
    ↓
Task 子系统创建任务，返回结果
    ↓
Agent Runtime 通过 Chat API 回复："✓ 已创建任务：Auth Review · 指派给张三"
    ↓
Web App 右侧自动显示刚创建的任务卡片（Chat 上下文关联）
    ↓
张三想深入操作 → 点击切到 Task 全屏，或在新标签页打开 Task + Extension
```

### 连接密度模型

Octo 的平台价值随连接密度增长：

```
Level 1: 人 ↔ 人（基本 IM）
Level 2: 人 ↔ Bot（Agent 协作）
Level 3: 人 ↔ Bot ↔ 子系统（操作闭环）
Level 4: Bot ↔ 子系统 A + 子系统 B（跨系统编排）
Level 5: ISV 子系统 ↔ 平台生态（开放 Hub）
```

每提升一个 Level，平台的不可替代性显著增加。MVP 需要到 Level 3。

### 子系统之间不通信

**关键约束：** 子系统 A 不知道子系统 B 的存在。跨子系统的数据组合通过人或 Bot 完成——Bot 从 Task 子系统读任务列表，从 Calendar 子系统读日程，在 Chat 中组合呈现给人。

---

## 十二、语义契约

**子系统数据是 ground truth。** Chat 是对话历史，不是状态。当 Chat 和子系统状态不一致时，子系统赢。

**Chat 是审计日志。** Chat 的线性特性在协调场景是劣势（找不到旧信息），但在审计场景是优势——完整记录了谁说了什么、Bot 做了什么、结果如何。结构化搜索 + AI 摘要可以缓解信息衰减问题。

**Bot 操作是 best-effort。** 多步操作中某步失败，已执行步骤的结果保留，不自动回滚。Bot 向用户报告实际执行情况。

**渲染是子系统的事。** Octo 不理解子系统的内容类型，只提供外跳和 Extension 桥梁。Task 子系统自己决定怎么渲染任务，Docs 子系统自己决定怎么渲染文档。

---

## 十三、与 Agent Runtime 的边界

### 13.1 架构独立，运维可选

OC 在架构上始终独立于 Octo 服务端——独立进程、独立数据、通过标准 API 通信。但运维归属因部署场景不同：

| 维度 | 场景 A（用户自建） | 场景 B（Octo 代管） |
|------|----------------|-----------------|
| 架构关系 | 独立 | 独立 |
| 运维归属 | 用户 | Octo 平台 |
| Octo 能否假设其存在 | 不能 | 能 |
| Agent 功能默认状态 | 不可用（需配置） | 开箱即用 |

OC 也是独立产品——它可以连接 Discord、Telegram 等任何 Channel，不局限于 Octo。Octo 同样不依赖特定的 Agent Runtime，其 API 对任何 HTTP 客户端开放。

### 13.2 集成接口

Octo 提供标准 API，不为特定 Agent Runtime 定制：

| 接口层 | Octo 提供 | Agent Runtime 消费 |
|--------|---------|------------------|
| Chat API | 消息收发、频道管理 | 参与对话、接收用户指令 |
| 子系统 API | 数据 CRUD | 操作子系统（创建任务、写文档等） |
| Auth API | Token 验证、权限查询 | 鉴权 |
| 状态上报 API | 接收和存储 Agent 状态（主动上报路径） | 通过 CLI 主动 report |

在场景 A 中，所有连接由 OC 侧主动发起（OC → Octo API）。在场景 B 中，连接已预配置，OC 实例启动后自动连接。

### 13.3 Agent 可观测性的能力边界

**OC 不对外暴露 Agent 内部状态的查询 API。** OC 的 `sessions_list`、`subagents list` 等是 Agent 在 session 内部使用的工具，不是对外 HTTP 接口。

**可行的可观测性通过"主动上报"实现：**
- OC 安装对应 Skill（例如 Monitor Skill）后，Agent 可以通过 `octo monitor report` CLI 主动上报工作状态
- 所有上报必须是用户授意的（授权窗口 / Bypass Permission），不做肉鸡
- Monitor 子系统在 Octo 侧呈现这些上报的状态

**不可行的（至少当前）：**
- Octo 主动拉取 Agent 的活动状态、Terminal 流、进程树
- 对用户本机 OC 的探针/轮询

---

## 十四、扩展模型

### 14.1 子系统生态

1. 开发 → 独立构建（技术栈自选）
2. 注册 → 开发者中心提交
3. 上架 → **ClawHub**（Plugin 分发中心）
4. 安装 → Space 管理员启用
5. 发现 → Bot 从 ClawHub 拉取 SKILL.md
6. 运行 → 人用 UI，Agent 用 CLI
7. 停用 → 管理员停用，数据保留

### 14.2 生态飞轮

```
更多子系统 → Bot 能力更强 → 用户价值更高 → 更多用户 → 更多 ISV 愿意接入 → 更多子系统
```

这个飞轮的启动条件是 MVP 阶段的全链路验证——证明一个子系统通过标准接口接入后，Bot 确实能操作它，用户确实觉得有价值。

---

## 十五、演进路径

**Phase 1（MVP）**：平台层（Auth + Space + Orchestration）+ 第一个子系统 + Bot 集成 + Browser Extension（Chat 侧边栏 + Cmd+K + 引用到 Chat）+ OpenClaw Channel Adapter 集成。验证全链路——证明 人 → Chat → Bot → CLI → 子系统 的闭环可工作。

**Phase 2**：第二个子系统 + 跨子系统引用（Bot 协调）+ 移动端（iOS / Android）。验证扩展模型——证明新子系统接入成本低。

**Phase 3**：**ClawHub 正式化** + 三方子系统接入 + Event Bus。验证生态——证明 ISV 愿意且能够接入。

**Phase 4**：子系统 SDK（多语言）+ 开发者文档 + 公开 API + Orchestration 多通道演化 + 社区 Plugin 生态。验证平台成熟度——Chat 开始与事件/协议共存。

**每个 Phase 的验证标准：不是"功能做完了"，而是"假设被验证了"。**

---

## 十六、关键架构决策

| # | 决策 | 理由 |
|---|------|------|
| 1 | 独立子系统而非前端组件 | 生态战略：子系统可独立运行，ISV 低门槛接入，Octo 是开放 Hub |
| 2 | Chat 是当前 Orchestration 实现 | Bot 参与协作的核心通道、窗口期内最务实的选择 |
| 3 | Orchestration 与 Chat 解耦 | 为 Chat 退到后台留演化空间，架构不与特定交互方式绑定 |
| 4 | Agent Runtime 不在 Octo 范围内 | 拓扑决定：OC 架构独立，场景 B 下 Octo 管 provisioning 不管 Agent 行为 |
| 5 | Space = 目标导向的隔离空间 | 数据完全隔离，以目标/项目而非人为组织中心 |
| 6 | 子系统数据是 ground truth | 系统正确性的锚点 |
| 7 | 渲染归子系统 | Octo 不理解子系统内容，只提供外跳 + Extension 协作桥梁 |
| 8 | Skill 即契约，ClawHub 分发 | 子系统提供 SKILL.md，ClawHub 负责注册/版本/分发，Agent Runtime 加载执行 |
| 9 | 四端完整覆盖 | Web（主场）+ iOS + Android（移动品鉴/通知）+ Extension（协作桥梁） |
| 10 | Auth 纯粹 | 只管用户账号认证，Bot Token 归 IM，外部工具自行鉴权 |
| 11 | Bot 权限模型独立决策 | 影响面广，专题分析后决策（见附录 A） |

---

## 十七、术语表

| 术语 | 定义 |
|------|------|
| Space | Octo IM 内部的目标导向协作空间，数据完全隔离边界 |
| Chat | 人与人、人与 Bot 之间的协调通道；Orchestration 的当前实现 |
| Bot | Space 中的 AI 协作参与者，Agent Runtime 由 OpenClaw 管理 |
| Orchestration | 平台层协调编排能力，当前基于 Chat，未来多通道演化 |
| 子系统 | 独立的功能模块/外部工具，可融入 Octo 也可独立运行 |
| Skill | SKILL.md，教 Bot 使用子系统 CLI 的契约 |
| **ClawHub** | **Plugin（CLI + SKILL.md + Channel Adapter）分发中心** |
| Auth Service | 平台层认证基础设施（IDaaS） |
| Agent Runtime | Agent 运行环境（如 OpenClaw），架构独立于 Octo |
| Channel Adapter | Octo IM 和 OpenClaw 之间的消息路由桥梁 |
| Extension | 浏览器插件，把 Octo 协作能力注入到任何 Web 工具旁边 |
| Cmd+K | 在任何页面选中内容后唤起输入框的统一手势 |
| 部署拓扑 | Octo 服务端 + Octo 端侧（四端）+ Agent Runtime 三个独立区域 |
| Hub | Octo 的定位——集成独立子系统的协作中心 |
| Ground Truth | 子系统数据是系统的权威状态 |
| Best-effort | Bot 操作语义——尽力执行，部分失败不自动回滚 |
| 连接密度 | 平台价值的度量——节点类型和连接数的增长 |
| 窗口期 | Chat-Centric 策略成立的时间窗口（Agent 尚不能全自主） |

---

## 附录 A：Bot 权限模型推荐

Bot 权限模型是独立的设计议题，完整对比见《Bot 权限模型对比与设计影响分析》。

**三种候选模型：**
- **A: Bot 即应用**——Bot 本身是由开发者构建的应用，管理员安装使用
- **B: 一等公民**——Bot 和人平等，是 Space 的正式成员
- **C: 数字分身**——Bot 是用户的个人代理，操作归因到主人

**当前阶段推荐模型 C（数字分身），核心理由：**
1. 当前目标用户是有自己 Agent Runtime 的技术用户——模型 C 的前提成立
2. 审计追溯最清晰——直接指向自然人
3. 子系统集成最简单——权限交集由 Auth 计算，子系统无需感知 Bot 细节
4. 用户自主性最高——自助创建和管理 Bot
5. 与《龙虾商业伦理学指南 v2.5》第 15 节对齐——数字分身是伦理框架的基石

**需要接受的 Trade-off：** 用户需要理解 Token 概念和 Agent Runtime 配置；未来面向无 Agent Runtime 的用户时需引入模型 A 要素。

---

本文档定义 Octo 的概念架构。各系统技术细节在各自设计文档中展开。*Bot 权限模型* 的完整分析见专题文档，*伦理学* 见《龙虾商业伦理学指南 v2.5》。
