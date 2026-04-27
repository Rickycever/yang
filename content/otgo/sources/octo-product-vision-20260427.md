---
title: Octo 产品架构与战略补充（2026-04-27）
topic: otgo
type: source
created: 2026-04-27
tags: [产品战略, Runtime-Agent, A2A, 子系统架构, 独立子系统]
---

# Octo 产品架构与战略补充（2026-04-27）

**来源**：产品团队口述（Ricky 转述），2026-04-27
**性质**：对 04-24 产品设计全案的重要补充与深化，侧重架构哲学、独立子系统、Runtime Agent vs 长记忆 Agent 区分

---

## 摘要

本文档确认 Octo 的核心定位（人与 Agent co-work，底座是 IM），并深化了三个关键议题：独立子系统的两种类型划分、A2A 事项管理 GUI 的需求与位置、以及 Octo 最重要的战略下注——把**长记忆 Agent 与 Runtime Agent 区分开来**，在同一个 Space/Channel/Thread 里让两者与人协作。

---

## 核心要点

### 1. 两类独立子系统

**公共板块**（架构上独立于 IM，但属于产品公共模块）：

| 模块 | 说明 |
|------|------|
| Context 管理 | 让人高效整理自己的 Context，并持久化存储（停留在 AM 里学习效率不够高） |
| FileSpace | Context 背后的独立存储系统 |
| A2A 事项管理 | 管理 Agent-to-Agent 交互的 GUI，给 Human-in-the-loop 用 |

**外部独立子系统**（外部工具 / SaaS）：飞书文档、Google Docs、Overleaf、Codecraft、Octic（会议纪要）、妙啊（内容营销）……

前提假设：**未来所有主流产品都会 CLI 化**，CRUD 行为与人查看的行为解耦。Octo 不改变用户工具习惯，而是作为串联不同独立子系统之间的协作枢纽。

### 2. A2A 事项管理 GUI

- **位置**：Octo 的 Channel/Thread 右侧第三栏（展开后），与阅读文件等功能共享屏幕空间
- **三大需求**：人员反馈（对整体任务持续纠偏）/ Context 持久化（大量 Context 文件 + 人相关 Context）/ 个人偏好记录（审美品味和品鉴信号存为个人数据）

### 3. 信息流转示例

```
Octic 会议纪要
  → 提炼关键 To-do
  → 流转到 Octo FileSpace
  → 部分 To-do 流转到"妙啊"（内容营销场景）
```

此场景下：用户屏幕左侧大部分是"妙啊"，Octo 以**浏览器插件**形态出现在屏幕右侧。

### 4. Runtime Agent vs 长记忆 Agent：Octo 的核心战略下注

两种深度 Agent 用户的工作模式：

| 模式 | 代表 | 特点 |
|------|------|------|
| 并行 Runtime Agent | OpenClaw 创始人 Peter Steinberger — 大量并行 CC 窗口 | 每个 Context 干净，任务窗口数极多 |
| 长记忆 Agent 调度 | 通过龙虾调用不同 Runtime Agent | Agent 携带长期记忆 + 独立电脑空间 |

**长记忆 Agent 的架构性问题**：
- Context 窗口爆炸——每次被打满，只能不断 Compact
- Token 消耗约为 Runtime Agent 的 **10 倍**
- 示例：完成 $1,000 价值的任务，龙虾消耗约 $1,000，Claude Code 消耗约 **$100**

根因：Runtime Agent 每次任务从干净 context 启动；长记忆 Agent 的 context 被历史信息持续填充。

**Octo 的战略下注（国内尚无人做）**：把长记忆 Agent（规划/记忆/Context 管理）与 Runtime Agent（执行/成本低）**区分开来，在同一个 Space/Channel/Thread 里协作**——人负责反馈、纠偏、品鉴。这就是 A2A 通信管理的底层需求。

**Octo 没有与龙虾（OpenClaw）强绑定**——这是刻意的产品决策，保留对接任何 Agent Runtime 的能力。

### 5. 创新者窘境视角

企微/飞书知道这些功能方向是对的，但无法直接做——受制于庞大 B 端用户习惯改变的阻力（克里斯坦森创新者窘境）。Octo 的差异化赌注正是在此处切入。

---

## Connections

- [[otgo/concepts/runtime-agent|Runtime Agent]] — 长记忆 Agent vs Runtime Agent 区分的详细论述
- [[otgo/concepts/octo-architecture|Octo 系统架构]] — 两类独立子系统（公共板块 vs 外部 SaaS）
- [[otgo/concepts/file-space|File Space]] — Context 管理 + FileSpace 独立模块
- [[otgo/concepts/browser-extension|Browser Extension]] — 浏览器插件形态（Octo 在用户使用其他工具时的存在方式）
- [[otgo/concepts/multi-cc-collab|多 CC 协作模式]] — A2A 协作的实现机制
- [[otgo/concepts/wukong-protocol|悟空协议]] — A2A 通信的传输层
