---
title: Browser Extension — 协作桥梁
topic: otgo
type: concept
created: 2026-04-27
tags: [Browser-Extension, 四端, Cmd+K, 零集成成本, 协作桥梁]
---

# Browser Extension — 协作桥梁

## 定义

Browser Extension 是 Octo 四端之一，也是架构原则"不替代工具，注入到工具旁边"的具体产品实现。用户在浏览器中打开任何 Web 工具（Jira、Google Docs、Overleaf、飞书文档……），Extension 在旁边提供 Octo 的协作能力，**无需工具做任何适配**。

---

## 运作方式

### 四项核心功能

**Chat 侧边栏**：在任何 Web 工具旁边提供完整的 Chat 界面——和 Bot 对话、和同事协调，无需切换标签页。

**Cmd+K**：在任何页面选中内容，唤起输入框，向 Bot 描述意图。统一的唤起手势，跨所有 Web 工具一致。

**引用到 Chat**：选中任何页面内容，一键引用到当前对话。把"正在看的内容"和"正在讨论的内容"连接起来。

**页面上下文感知**：自动识别当前页面 URL、标题、选中内容，作为 Bot 操作的上下文。Bot 知道你在看什么，无需手动粘贴。

### 技术实现

Extension 通过 **Content Script** 动态注入功能——Web 工具不需要做任何适配。这是架构原则"零集成成本"的实现：任何 Web 工具天然可交互。

Extension 通过 Web App 的 Auth 共享登录态，无需单独登录。

### 在四端中的定位

```
Web  ←→  Octo 服务端  ←→  iOS / Android
                ↑
                └── Browser Extension（通过 Web App 的 Auth 共享登录态）
```

- Web：IM 主场 + 全功能（Space 管理、Bot 管理、Chat、子系统集成）
- iOS / Android：移动 IM + 通知 + 轻量品鉴
- **Browser Extension：轻量协作桥梁**——完整的 IM 体验在 Web 端，Extension 聚焦于在工具旁边提供协作上下文

### IM 与工具的分工

Extension 是两者之间的桥梁：

- **IM（Chat）**：对齐意图（"帮我改第三章"）+ 汇报结果（"改好了，你看看"）
- **工具（子系统 UI）**：实际深度操作（拖拽看板、批量编辑表格、精确修改文档）
- **Extension**：在工具页面上引用内容到 Chat；在 Chat 中接收结果后跳转工具查看

没有人在群里写代码或排版论文——但人需要在工具旁边协调。Extension 解决了这个场景。

### 为什么 Chat 做不了、工具 UI 也做不了

| 工作类型 | 为什么 IM 做不了 | Extension 的角色 |
|---------|---------|------------|
| 深度操作 | 拖拽看板、批量编辑——对话界面无法承载 | Extension 提供 Chat 上下文，操作在工具 UI 完成 |
| 精确反馈 | "第三列那个数不对"——文字描述位置很痛苦 | Cmd+K 选中内容直接引用，位置精确 |
| 多轮协调 | 工具 UI 没有 Chat 界面 | Extension 把 Chat 侧边栏带到工具旁边 |

---

## 为什么重要

### 零集成成本 = 生态门槛趋近于零

传统的"做集成"要求工具方接入 SDK 或实现 API 适配。Extension 通过 Content Script 动态注入，任何已有的 Web 工具天然变成 Octo 生态的一部分——不需要对方做任何事。

这让 Octo 的协作能力可以覆盖用户已有的所有 Web 工具：Jira、Google Docs、Overleaf、飞书……每一个都是 Octo Extension 可以注入的场景。

### 让"Agent 嵌入工具"的未来架构成本最低

Cursor 的成功证明了 AI 直接嵌入工作上下文（而非在单独的 Chat 窗口）的价值。Extension 是这个方向的 Octo 版本：把协作（Chat + Bot）带到用户正在操作的工具上下文中。

未来如果 Agent 能力足够强，可以减少 Chat 的比重，Extension 仍然是 Agent 嵌入工具 UI 的桥梁——架构演化不需要重建。

---

## Connections

- [[otgo/sources/octo-arch-v11.2-20260420|Octo 概念架构文档 v11.2]] — Browser Extension 的完整设计来源
- [[otgo/concepts/octo-architecture|Octo 系统架构]] — Extension 是 Octo 四端之一
- [[otgo/concepts/dual-native|Dual-Native Design]] — Extension 是"注入到工具旁边"原则的产品实现
- [[otgo/concepts/cli-decoupling|CLI 解耦]] — View（工具 UI）和 CRUD（Bot 通过 CLI）解耦，Extension 是桥梁
