# Octo 产品架构与战略补充 — 2026-04-27

> **来源**：产品团队口述（Ricky 转述），2026-04-27
> **性质**：对 04-24 产品设计全案的重要补充与深化，侧重架构哲学、独立子系统、Runtime Agent vs 长记忆Agent 区分
> **关联**：memory/dmwork-product-design.md（主设计文档）

---

## 一、核心定位再确认

**Octo = 人与 Agent 一起 Cowork 的产品，底座是 IM。**

IM 本身在通信和信息安全方面需要大量考量，因此大部分功能（"脚手架"工具）以**独立子系统**形态存在，而非耦合在 IM 内部。

---

## 二、独立子系统架构

### 2.1 公共板块（架构上独立于 IM，但属于产品的公共模块）

类比企业微信的日程系统：日程本身是独立系统，但可以作为消息卡片分享到群聊。

**已规划/规划中的公共模块：**

| 模块 | 说明 | 状态 |
|------|------|------|
| **Context 管理** | 让个人能快速整理自己的 Context（涉及整理就必然需要存储） | 规划中 |
| **FileSpace** | Context 背后的独立存储系统 | 规划中 |
| **A2A 事项管理** | 管理 Agent-to-Agent 交互，给人看的 GUI 界面 | 规划中 |

**核心洞察**：如果 Context 仅停留在 Agent Memory（AM）中，对 Agent 的学习效率不够高。应有专门的产品功能让人高效整理个人 Context，并持久化到 FileSpace。

### 2.2 外部独立子系统（外部工具 / SaaS）

**前提假设：未来所有主流产品都会 CLI 化。**

CLI 化带来的关键变化：**CRUD 行为与人查看的行为解耦。**

用户保留自己的工具习惯：
- 飞书文档 / 企微文档
- Google Docs
- Overleaf（论文）
- Codecraft（内部工具）
- Octic（孔老师的产品，会议纪要等）
- 妙啊（内容营销）

**Octo 不改变用户习惯，而是作为串联不同独立子系统之间的协作枢纽。**

### 2.3 信息流转示例

```
Octic 会议纪要
    → 提炼关键 To-do
    → 流转到 Octo FileSpace
    → 部分 To-do 流转到"妙啊"（内容营销场景）
```

在这个场景下：
- 用户屏幕左侧大部分是"妙啊"
- **Octo 以浏览器插件形态出现在屏幕右侧**

---

## 三、A2A（Agent-to-Agent）管理

### 3.1 为什么需要 A2A 管理 GUI

- Agent 之间如果纯 GUI 沟通，无人参与时理论上不需要独立界面
- **但目前大量工作需要 Human-in-the-loop**，所以必须有管理 A2A 的 GUI
- **位置**：Octo 的 Channel/Thread 右侧第三栏（展开后），与阅读文件等功能共享屏幕空间

### 3.2 A2A 管理的三大需求

| 需求 | 说明 |
|------|------|
| **人员反馈** | 人必须对整体任务进行反馈和持续纠偏 |
| **Context 持久化** | 大量 Context 文件 + 与人相关的 Context 文件需要被存下来 |
| **个人偏好记录** | 人的审美品味和品鉴信号需要存为个人数据 |

---

## 四、关键战略判断：Runtime Agent vs 长记忆 Agent

### 4.1 两种 Agent 工作习惯

深度使用 Agent 的人有两种典型模式：

| 模式 | 代表 | 特点 |
|------|------|------|
| **并行 Runtime Agent** | OpenClaw 创始人 Peter Steinberger — 大量并行 Claude Code 窗口 | 任务窗口数极多，每个 Context 干净 |
| **长记忆 Agent 调度** | 通过龙虾（OpenClaw）调用不同 Runtime Agent（Claude Code / Codex） | Agent 携带独立电脑空间+长期记忆 |

### 4.2 长记忆 Agent 的架构性问题

龙虾 / Hermes Agent 的记忆机制会存入大量内容，且嵌入在 LLM 内部，导致：

| 问题 | 说明 |
|------|------|
| **上下文窗口爆炸** | Context 每次被打满，只能不断压缩（Compact）|
| **Token 消耗巨大** | 同等任务，龙虾/Hermes 约为 Runtime Agent 的 **10 倍** |

**成本对比示例**：
- 龙虾完成 $1,000 价值的任务 → Token 消耗约 $1,000
- Claude Code / Codex 完成同等任务 → Token 消耗约 **$100**

**根因**：架构机制差异。Runtime Agent 的 Context 是干净的（每次任务独立上下文），长记忆 Agent 的 Context 被历史信息持续填充。

### 4.3 Octo 的战略下注

**Octo 没有与龙虾（OpenClaw）强绑定**，这是刻意的产品决策。

核心理念（**国内尚无人做**）：
> 把具有长期记忆的独立 Agent（OpenClaw / Hermes）与实际干活的 Runtime Agent（Claude Code / Codex）**区分开来**。
> 两者职责不同，但需要在**同一个 Space / Channel / Thread** 里协作。

这意味着 Octo 要同时支持：
1. **长记忆 Agent**：负责规划、记忆、Context 管理
2. **Runtime Agent**：负责执行具体任务，Context 干净、成本低
3. **人**：负责反馈、纠偏、品鉴

三者在统一的通信空间中协作，这就是 A2A 通信管理的底层需求。

### 4.4 创新者窘境视角

> 企微/飞书知道这些功能是对的，但无法直接做——受制于庞大 B 端用户习惯改变的阻力（克里斯坦森创新者窘境）。Octo 的 "different bet" 正是在此处切入。

---

## 五、与 04-24 设计全案的关系

| 04-24 设计全案已有 | 本次补充/深化 |
|---|---|
| 四层结构（Space/分组/频道/Thread） | 独立子系统架构（公共模块 vs 外部 SaaS） |
| L1-L4 编排架构 | Runtime Agent vs 长记忆 Agent 的区分 |
| Playbook 设计 | 信息跨系统流转（Octic → FileSpace → 妙啊） |
| Agent Card + 管理体系 | A2A 管理 GUI（第三栏）+ 三大需求 |
| Agent一等公民 | 不与龙虾强绑定的战略决策 |
| 通信基础设施定位 | CLI 化前提 + Octo 作为串联枢纽 |
| — | Octo 浏览器插件形态 |
| — | Context 管理 + FileSpace 独立模块 |
| — | 个人品味/偏好信号持久化 |

---

## 六、关键概念速查

| 术语 | 含义 |
|------|------|
| **Runtime Agent** | 执行具体任务的 Agent（如 Claude Code、Codex），Context 干净、成本低 |
| **长记忆 Agent** | 携带长期记忆+独立电脑空间的 Agent（如 OpenClaw/龙虾、Hermes），Context 持续积累 |
| **FileSpace** | Octo 的独立存储系统，承载个人 Context 和文件 |
| **A2A 事项管理** | Agent-to-Agent 交互的管理 GUI，给 Human-in-the-loop 用 |
| **公共板块** | 架构上独立于 IM 的产品公共模块（Context 管理/FileSpace/A2A 事项等） |
| **CLI 化前提** | 未来主流产品都会 CLI，CRUD 与查看行为解耦 |
| **浏览器插件形态** | Octo 在用户使用其他工具时以右侧插件形式存在 |
