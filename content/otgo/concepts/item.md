---
title: 事项 (Item) — 结构化工作单元
topic: otgo
type: concept
created: 2026-04-27
tags: [事项, Item, 产品架构, Agent协议, 品鉴]
---

# 事项 (Item) — 结构化工作单元

## 定义

事项是 Octo 中与 Channel、Thread 同属产品基础结构的**一等公民对象**。核心定义：**一条被赋予结构化骨架的顶层消息**——挂上骨架后，它从"聊天"变成"工作"。骨架由人和 Agent 共同读写。

**"事项"不是一个功能，是一个标准**——它定义了"人 + 多层 Agent 协作"的标准化工作单元，Octo 是这个标准的第一个实现。

---

## 运作方式

### 5 个骨架字段

| 字段 | 说明 |
|------|------|
| **目标** | 要做什么 |
| **状态** | 做到哪了（见生命周期） |
| **归属链** | 谁派、谁做、谁评——Attribution Chain |
| **品鉴信号流** | 做得如何——append-only，历史永不覆盖 |
| **执行载荷** | 过程轨迹 + 产出物（diff / 文件 / 图片 / 素材引用）|

### 三种 UI 形态

**1. 对话流卡片**（轻量入口）  
状态徽章 + 标题摘要 + 认领人头像 + 快捷品鉴按钮（通过/驳回/批注）。对话流不被骨架侵占，只给最关键信息。

**2. 右侧面板详情**  
与 PDF、Markdown 同级的内容展示类型——右侧面板切换后展示：归属链、执行载荷（轨迹 / 产出 / 引用素材）、品鉴信号流、操作栏（通过 / 驳回 / 批注 / Cmd+K 深反馈）。

**3. Channel / Thread 总览视图**  
展示该频道/子区中所有事项的认领状态和进度地图，点击某项进入详情。

### 生命周期

```
todo ──claim──→ in_progress ──submit──→ in_review ──approve──→ done
                                              │
                                              ├─ reject → in_progress（重新做）
                                              └─ append 品鉴信号（永不丢失）
```

核心约定：
- **Agent 默认只标到 `in_review`**——最终 `done` 由具备品鉴权的实体（人或被授权代理龙虾）给出
- **品鉴信号 append-only**——改主意时追加新信号，不覆盖历史记录（Taste 完整可审计）
- claim 的那方负责推进状态

### 层级与容纳关系

```
Workspace
└── Category
    └── Channel
        ├── 消息
        ├── 事项          ← Channel 级大事项
        └── Thread
            ├── 消息
            └── 事项      ← 围绕讨论收敛的事项
```

事项自身可以有**子事项**——父事项由龙虾持有，子事项派给 Runtime Agent / Sub-Agent。支持任意深度的多层 Agent 编排。

### Agent 协议：事项是可观测通道

Runtime Agent 无论跑在本地/VM/云端，只要把执行信息写进事项，用户就能看见：
- 边做边把每一步执行轨迹写入执行载荷
- 产出物（unified diff、文件、图片）作为 artifact 附在事项上
- 完成后标 `in_review`，交品鉴者评

**事项是 Agent 和人之间唯一的回传通道**，解决远程 Agent 不可观测问题，同时解决"不能监控用户"的悖论——**用户主动写入事项**，而非 Octo 偷偷采集。

---

## 为什么重要

### Taste 学习的天然载体

品鉴信号与执行记录并排存于同一个事项——Agent 读同类历史事项即可学习用户 taste。**不需要独立的偏好数据库，也不需要独立的训练流程**——事项本身就是 Taste 采集现场和反馈通道。

### 天然合规审计

append-only 品鉴信号 + 执行轨迹 + 归属链 = 原生审计流。金融、医疗、法律行业"AI 必须可追溯"的要求，Octo 是原生满足，不是事后打补丁。

### 数字劳动力的归属

OC 是个人的，FileSpace 是个人的，通过事项历史养出来的龙虾也是个人的——员工跳槽，龙虾跟着走，投入时间和积累的品味不因跳槽蒸发。

---

## Connections

- [[otgo/sources/item-design-v2-20260427|事项（Item）设计 V2]] — 本概念的完整设计文档
- [[otgo/concepts/runtime-agent|Runtime Agent]] — 事项中的执行角色
- [[otgo/concepts/lonxia|龙虾 (Lobster)]] — 事项的编排者，持有父事项
- [[otgo/concepts/taste-philosophy|品 (Taste) 哲学]] — 品鉴信号流的哲学基础；Taste 三层传递性
- [[otgo/concepts/file-space|File Space]] — 事项的执行载荷和品鉴记录最终沉淀在 File Space
- [[otgo/concepts/dual-native|Dual-Native Design]] — 事项是 Dual-Native 的核心产品对象
- [[otgo/concepts/digital-avatar|数字分身]] — 事项历史是数字分身的训练语料
