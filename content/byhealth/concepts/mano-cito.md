---
title: Mano & Cito 双模型（DeepMiner核心架构）
topic: byhealth
type: concept
created: 2026-04-16
tags: [mano, cito, browser-automation, function-call, deepminer, ai-model]
---

# Mano & Cito 双模型（DeepMiner核心架构）

## 定义

Mano和Cito是明略科技DeepMiner平台的双核心模型，分别专攻「执行」和「推理」两种能力。与通用大模型全能路线不同，DeepMiner选择「专模型」策略：Mano专注网络/浏览器自动化，Cito专注复杂推理与工具调用，两者通过多Agent编排协同工作。

## 运作方式

### Mano：AI灵巧手

**定位**：Browser/UI Automation专用模型（BUA/CUA领域）

**核心能力**：
- 自主浏览器操作：导航、点击、填表、截图
- 跨系统数据抓取：电商、社媒、企业内系统
- OS级任务执行（OS-World赛道能力）

**性能基准**：
- Mind2Web赛道：第一名
- OS-World E2E赛道：第一名
- 任务执行速度：83秒（对比Browser-Use的456秒，快约5.5倍）

**在营销链路中的角色**：执行节点①②的数据抓取任务——竞品扫描、UGC数据收集、KOL数据获取。

### Cito：AI专家脑

**定位**：Complex Reasoning & Function Call专用模型

**核心能力**：
- 多步骤逻辑推理
- Function Call / Tool Use（API调用、工具编排）
- 结构化输出（报告、分析框架、brief生成）
- 内置闭环Reward机制（强化学习持续迭代）

**性能基准**：
- BFCL-V4（Berkeley Function Calling Leaderboard v4）：
  - 8b参数尺寸：第一名
  - 32b参数尺寸：第一名

**在营销链路中的角色**：驱动节点②③⑥的分析与生成任务——消费者洞察综合、内容策略制定、详情页结构设计。

## 为什么重要

### 专模型 vs 通用模型

| 维度 | 通用大模型路线 | 双专模型路线（DeepMiner） |
|------|--------------|--------------------------|
| 执行效率 | 中等，需提示工程优化 | 高，专训任务类型 |
| 成本 | 每次推理消耗更多token | 按任务类型路由，成本可控 |
| 可靠性 | 任务类型越多样，可靠性越分散 | 各类任务有专门优化，成功率更高 |
| 扩展性 | 依赖单一模型迭代 | 两个模型可独立升级 |

### 闭环Reward机制（Cito独有）

Cito内置强化学习奖惩机制：每次Function Call执行结果（成功/失败/部分成功）都作为训练信号反馈，使模型在企业特定工具环境中持续自我优化，无需人工标注数据。

## Connections

- [[byhealth/overview|汤臣倍健×明略科技 全景概览]] — 所属话题入口
- [[byhealth/entities/deepminer|DeepMiner]] — Mano/Cito所属的平台实体
- [[byhealth/concepts/ai-marketing-full-chain|AI营销全链路（六节点）]] — 双模型在营销场景的具体应用
- [[byhealth/sources/deepminer-marketing-proposal-2025|明略科技×汤臣倍健方案]] — 模型能力的原始描述来源
