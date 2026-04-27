---
title: 悟空协议
topic: otgo
type: concept
created: 2026-04-27
tags: [协议, 通信, Agent, 基座层, 架构]
---

# 悟空协议

## 定义

悟空协议是 Octo 基座层的统一消息传输协议，覆盖三种通信路径：**H↔H（人与人）、H↔A（人与 Agent）、A↔A（Agent 与 Agent）**。所有 Octo 内的消息路由均基于悟空协议。

---

## 运作方式

### 三种通信路径

| 路径 | 场景 | 特点 |
|------|------|------|
| **H↔H** | 用户之间的 IM 对话 | 标准消息传输 |
| **H↔A** | 用户给龙虾下指令、龙虾汇报给用户 | 支持指令结构化、意图传递 |
| **A↔A** | 龙虾与 CC 之间的任务分派和结果返回 | 任务调度协议，包含 context 传递 |

### 在基座层的位置

悟空协议是 Octo 基座层的核心组成，与 Agent 运行时（龙虾/CC 生命周期管理）、SDK 网关共同构成底层基础设施。场景层的所有子系统通信最终都通过悟空协议转发。

### 与多 CC 协作的关系

A↔A 通信路径为多 CC 协作提供传输基础——龙虾派发任务给 CC、CC 返回结果给龙虾，都通过悟空协议完成。但**CC 之间不直接通信**，所有 A↔A 路由都经过龙虾或 Context/File Space 作为中间媒介。

---

## 为什么重要

统一协议是 Octo "Link Everything" 架构能力的基础。没有统一的 H↔H/H↔A/A↔A 传输层，人与 Agent 的无缝协作、多 Agent 编排、跨子系统联动都无法实现。悟空协议将人和 Agent 纳入同一个消息网络，是龙虾矩阵操作系统的通信骨架。

---

## Connections

- [[otgo/sources/dual-native-design-v1.5-20260404|Dual-Native Design v1.5]] — 悟空协议的设计文档来源
- [[otgo/concepts/multi-cc-collab|多 CC 协作模式]] — A↔A 通信路径的具体应用
- [[otgo/concepts/octo|octo 平台]] — 悟空协议所在的基座层
- [[otgo/concepts/lonxia|龙虾 (Lobster)]] — 协议的主要 Agent 参与方
