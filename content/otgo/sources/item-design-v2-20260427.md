---
title: 事项（Item）设计 V2
topic: otgo
type: source
created: 2026-04-27
tags: [事项, Item, 产品设计, Agent协议, 品鉴]
---

# 事项（Item）设计 V2

**定位**：与 Channel、Thread 同级的产品基础结构，是人与 Agent 协作的标准化工作单元  
**衔接文档**：Dual-Native Design v1.5、07-Octo与OpenClaw关系、PRD-CmdK 品鉴反馈器、Shell UI v4

---

## 摘要

"事项"是 Octo 的一等公民对象。核心定义：**一条被赋予结构化骨架的顶层消息**——挂上骨架后从"聊天"变成"工作"。6 个结构性红利涵盖：Taste 信号天然嵌入（无需额外反馈系统）、数字劳动力分身（OC + FileSpace 属于个人）、解开"不能监控用户"悖论（用户主动写入事项）、OC/Runtime Agent 天然分工、个人 vs 组织 SaaS 账本拆分、基于真实工作的 Agent 评级系统。

---

## 核心要点

### 事项的 5 个骨架字段

| 字段 | 内容 |
|------|------|
| **目标** | 要做什么 |
| **状态** | 做到哪了（todo/in_progress/in_review/done） |
| **归属链** | 谁派、谁做、谁评（Attribution Chain） |
| **品鉴信号流** | 做得如何——append-only，历史永不覆盖 |
| **执行载荷** | 过程轨迹 + 产出物（diff/文件/素材引用） |

### 三种 UI 形态

1. **对话流卡片**：状态徽章 + 标题摘要 + 快捷品鉴按钮（轻量入口）
2. **右侧面板详情**：归属链 + 执行载荷（轨迹/产出/引用）+ 品鉴信号流 + 操作栏
3. **总览视图**：Channel/Thread 级别，展示所有事项的认领状态和进度地图

### 生命周期

```
todo ──claim──→ in_progress ──submit──→ in_review ──approve──→ done
                     │                       │
                     └─ cancelled            ├─ reject → in_progress
                                             └─ append 品鉴信号（永不丢失）
```

核心约定：
- Agent 默认只标到 `in_review`——最终 `done` 由具备品鉴权的人（或被授权的代理龙虾）给出
- 品鉴信号 append-only——改主意就追加新信号，不覆盖历史

### 层级结构

- Channel → 容纳事项（和消息、Thread 并列）
- Thread → 也可容纳事项（和消息并列）
- 事项 → 可有**子事项**（父事项由龙虾持有，子事项派给 Runtime Agent / Sub-Agent）

子事项支持多层 Agent 编排——Claude Code Agent Teams、Codex worker、自研 Runtime 都可以是某事项下的执行节点。

### Agent 协议：事项是可观测通道

Runtime Agent 无论跑在本地/VM/云端，只要把执行信息写进事项，用户就能看见：
- 每一步执行轨迹写入事项的执行载荷
- 产出物（unified diff / 文件 / 图片）作为 artifact 附在事项上
- 完成后标 `in_review`，交品鉴者评

**事项是 Agent 和人之间唯一的回传通道**，解决远程 Agent 不可观测问题。

### 6 个结构性红利

**1. Taste 反馈天然内置**：品鉴信号与执行记录并排存于事项，Agent 读同类历史事项即可学习用户 taste，无需独立偏好数据库或训练流程。

**2. 数字劳动力分身**：OC 是个人的，FileSpace 是个人的，通过事项历史养出来的龙虾也是个人的——换公司龙虾跟着走，积累不因跳槽蒸发。

**3. 解开"不能监控用户"悖论**：用户主动把信息放进事项（而非系统偷偷采集），合规红利：append-only 品鉴信号 + 执行轨迹 + 归属链 = 天然审计流，金融/医疗/法律行业开箱即用。

**4. OC/Runtime Agent 天然分工**：OC 做编排（Token 贵但擅长协调），Runtime Agent 做执行（Token 便宜且擅长执行）。用户已订阅的 Claude Max / Codex Pro / Cursor 直接接入当 Runtime Agent，Octo 不烧最大那份 Token。

**5. 个人资产 vs 组织资产**：OC 随员工走（个人订阅），Runtime Agent 是团队共享运力（组织订阅）。最友好的企业 SaaS 账本结构。

**6. 基于真实工作的 Agent 评级**：每个 Runtime Agent 的通过率、每只 OC 的代理品鉴准确率——这是真实口碑，不是 benchmark 分数。企业选 Agent、派龙虾可数据驱动。

---

## Connections

- [[otgo/overview|OTGO 全景概览]]
- [[otgo/concepts/item|事项 (Item)]] — 本文件定义的核心概念
- [[otgo/concepts/runtime-agent|Runtime Agent]] — 事项中的执行者角色
- [[otgo/concepts/taste-philosophy|品 (Taste) 哲学]] — 品鉴信号流的哲学基础
- [[otgo/concepts/file-space|File Space]] — 执行载荷和品鉴记录的存储载体
- [[otgo/concepts/dual-native|Dual-Native Design]] — 事项所在的 GUI 架构
- [[otgo/concepts/lonxia|龙虾 (Lobster)]] — 事项的编排者/认领者
