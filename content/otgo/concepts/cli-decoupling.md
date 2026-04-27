---
title: CLI 解耦 — View 与 CRUD 分离
topic: otgo
type: concept
created: 2026-04-27
tags: [架构, CLI, View, CRUD, 子系统]
---

# CLI 解耦 — View 与 CRUD 分离

## 定义

CLI 解耦是 Octo 架构的核心工程原则：**View（人看的）和 CRUD（龙虾干的）是独立解耦的两件事**，由完全不同的机制承担，互不依赖。这让 Octo 不需要自建渲染器和编辑器，轻装上阵。

---

## 运作方式

### 两条独立轨道

**CRUD（龙虾干的）**：
- 龙虾控制 CC 实例
- CC 通过 CLI 操作工具——修改文件、调用 API、执行命令
- CC 完成后结果写入工具的文件系统/状态

**View（人看的）**：
- 工具自身的 Web 界面负责渲染
- Octo 提供浏览器容器，指向工具的 Web 界面
- 浏览器容器实时刷新，人看到最新状态

两条轨道完全独立——CRUD 不依赖 View 存在，View 不依赖 CRUD 存在。

### 参照系：Claude Code + VS Code

这与 CC 和 VS Code 的分工模式完全相同：
- CC 在终端改代码（CRUD）
- VS Code 实时刷新显示最新代码（View）
- 两者互不依赖

Octo 把这个模式推广到所有子系统。

### Octo 只做两件事

由于 View 和 CRUD 都委托出去，Octo 聚焦于：

| Octo 的核心职责 | 具体内容 |
|--------------|---------|
| **编排** | 龙虾 → CC → CLI 调度，多 CC 并行/串行管理 |
| **品鉴** | Cmd+K 反馈、品鉴操作栏（通过/驳回）、Context/Taste 采集 |

| 委托出去 | 原因 |
|--------|------|
| 所有 Artifact 渲染 | 工具自身 Web 界面已是最好渲染器 |
| 所有 Artifact 编辑 | CC 通过 CLI 操作，不需要 Octo 自建编辑器 |

### 子系统接入方式

子系统是独立的 Web App，通过 Octo SDK 接入，一套接入规范适用所有子系统（一方和三方）：

```
CLI 接口（CRUD）+ SKILL.md + Auth 鉴权 + 品鉴信号回传（View 侧 SDK 注入）
```

- 自建子系统（妙啊、DM 3.0、研发工具）：按规范开发独立 Web App + CLI
- 外部子系统（飞书文档、Google Sheets）：通过 CLI 操作，Viewer 指向其原生 Web 界面

---

## 为什么重要

### 工程量降维

传统混合平台工程量"中重"——需要在每个端自建 Viewer 和编辑器。CLI 解耦让 Octo 不需要自建这些重型组件：工具的 Web 界面本身就是最好的渲染器，直接嵌入一个浏览器容器即可。

### Link Everything 成为可能

任何有 Web 界面 + CLI 的工具都可以接入——Jira、Overleaf、GitHub、飞书文档、Google Docs。接入标准统一，不限制子系统的技术栈和 UI 设计。这实现了 Octo 的"Link Everything"战略目标。

### 与 Dual-Native 的关系

CLI 解耦是 Dual-Native Design 的工程实现：
- Agent 侧（CRUD）：CC 通过 CLI 直接操作文件，这是 Agent 最原生的工作方式
- 人侧（View）：工具自身 Web 界面渲染，这是人看内容最原生的方式
- 两者各自最优，互不妥协

---

## Connections

- [[otgo/sources/dual-native-design-v1.5-20260404|Dual-Native Design v1.5]] — CLI 解耦的完整设计来源
- [[otgo/concepts/dual-native|Dual-Native Design]] — CLI 解耦是 Dual-Native 的工程实现
- [[otgo/concepts/multi-cc-collab|多 CC 协作模式]] — CC 如何通过 CLI 协作完成复杂任务
- [[otgo/concepts/lonxia|龙虾 (Lobster)]] — 龙虾作为编排者调度 CC 执行 CLI 操作
- [[otgo/concepts/octo|octo 平台]] — CLI 解耦架构的产品载体
