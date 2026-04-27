---
title: 多 CC 协作模式
topic: otgo
type: concept
created: 2026-04-27
tags: [CC, 多Agent, 协作, 编排, 并行]
---

# 多 CC 协作模式

## 定义

多 CC 协作是 Octo 中实现并行任务执行的核心机制。**核心原则：CC 之间不直接对话。协作通过龙虾调度 + Context/File Space 共享介质完成。** 龙虾是唯一编排者，CC 之间保持零耦合。

---

## 运作方式

### 龙虾 vs CC 的角色分工

| | 龙虾（协调者） | CC 实例（执行者） |
|---|---|---|
| **对标** | Main Agent | Claude Code / Sub Agent |
| **特征** | 持久身份、长期记忆、有性格 | 干净 context、无记忆、完成即释放 |
| **做什么** | 接收指令、拆解任务、分配 CC、汇报结果 | 在干净环境中执行具体任务，返回结果 |
| **生命周期** | 长期存在，跨任务积累 | 任务级，完成就释放 |
| **类比** | 项目经理——记得你上次要什么 | 外包工人——给任务书就能干，干完走人 |

CC 是龙虾的标配后端。同样任务，CC 处理的经济效益比龙虾直接在 IM 中交互好 **5-10 倍**。

### 四种协作模式

| 模式 | 说明 | 典型场景 |
|------|------|---------|
| **串行链** | CC-1→CC-2→CC-3，前一个输出是后一个输入 | 数据驱动内容生产：拉数据→生成脚本→渲染 |
| **扇出** | 龙虾同时派多个 CC 并行，互不依赖 | 论文更新：图表更新 + 前后文检查可并行 |
| **流式** | 一个 CC 持续监听，事件触发其他 CC | 实时会议：CC-0 监听文字流，触发摘要/待办/Context查询 |
| **扇入** | 多个 CC 结果汇聚，龙虾做最终判断 | 多源数据整合，龙虾综合多个 CC 的输出 |

### 关键约束

1. **CC 零耦合**：加一个新子系统不需要改任何现有 CC 的逻辑
2. **龙虾管理依赖**：CC-2 依赖 CC-1 的输出时，由龙虾控制执行顺序，不由 CC 互相等待
3. **Context/File Space 是唯一数据交换介质**：CC 的输出写入 File Space，下一个 CC 从 File Space 读取

### 典型场景示例

**场景 A（流式）：实时会议**
- CC-0 监听 Optic 文字流，提取结构化事件 → 龙虾判断 → 并行派出 CC-1（查 Context 推送补充）、CC-2（更新会议摘要）、CC-3（识别待办更新看板）

**场景 B（串行链）：内容生产**
- 龙虾拆解 → CC-1 进 DM 拉指标（结果写入 Context）→ CC-2 基于数据生成脚本（进品鉴队列）→ 用户通过 → CC-3 渲染画布

**场景 C（串行链）：跨平台周报**
- CC-1 收集 PR → CC-2 生成周报（基于 Context 的格式偏好）→ CC-3 创建飞书文档 → CC-4 发送链接到 IM 群

**场景 D（扇出）：论文更新**
- CC-1 导出最新数据 → 同时并行：CC-2 更新图表+重新编译、CC-3 检查前后文描述——两者互不依赖

---

## 为什么重要

### 并行是提效的核心

多个 CC 同时工作，品鉴者只在关键节点介入——不是逐个看，是扫一眼 Monitor 全局，发现异常再 Zoom In。与线性执行相比，扇出模式可将任务完成时间压缩到单 CC 的 1/N。

### 零耦合的架构价值

CC 之间不直接通信意味着可以随时新增/替换子系统。接入一个新工具（新增一种 CLI 能力），现有的所有 CC 逻辑都不需要修改——这是 Octo"Link Everything"能力的关键保证。

---

## CC = Runtime Agent

文档中的"CC 实例（Claude Code）"即 Runtime Agent 的一种具体实现。在事项设计文档中，这套协作机制被进一步扩展：Runtime Agent 可以是 CC、Codex Pro、Cursor 或自研 Runtime——所有执行层 Agent 都通过事项的子事项结构被龙虾调度，执行结果写入事项执行载荷。

## Connections

- [[otgo/sources/dual-native-design-v1.5-20260404|Dual-Native Design v1.5]] — 多 CC 协作的完整设计来源
- [[otgo/concepts/runtime-agent|Runtime Agent]] — CC 是 Runtime Agent 的具体实现
- [[otgo/concepts/item|事项 (Item)]] — 多 CC 协作的产出通过事项执行载荷上报
- [[otgo/concepts/lonxia|龙虾 (Lobster)]] — 多 CC 协作的唯一编排者
- [[otgo/concepts/cli-decoupling|CLI 解耦]] — CC 执行的底层机制（CC 通过 CLI 干活）
- [[otgo/concepts/wukong-protocol|悟空协议]] — A↔A 通信的传输层
- [[otgo/concepts/file-space|File Space]] — CC 间数据交换的唯一介质
- [[otgo/concepts/lonxia-matrix|龙虾矩阵]] — 多 CC 协作在组织层面的映射
