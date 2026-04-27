---
title: Dual-Native Design
topic: otgo
type: concept
created: 2026-04-27
tags: [GUI设计, Dual-Native, 产品原则, 品鉴, Agent协作]
---

# Dual-Native Design

## 定义

Dual-Native Design 是 Octo GUI 设计的根本原则：**底层为 Agent 而建，表层为人而渲染。两者从不妥协，各自极致。** 目的是让人和 Agent 更高效地 co-work。

传统产品只回答一个问题——"对人好不好？"。Octo 必须同时回答两个：**对人好不好？对 Agent 好不好？**

---

## 运作方式

### 三道设计检验

每个设计决策必须同时通过：
1. 人好不好用？
2. Agent 好不好接？
3. 两者协作是否更高效？

只满足其中一条不够——Dual-Native 是"同时达到各自的原生体验"，不是折中。

### IM 是协调通道，Workspace 是工作台

**Octo 不以 IM 为轴，以品鉴和编排为轴。**

IM 适合协调，不适合干活。没有人在群里写代码、排版论文或审核表格。

| 工作类型 | IM 的局限 | Workspace 的解法 |
|---------|---------|-----------------|
| 深度阅读/审核 | 线性对话流，无法空间化呈现文档 | 文档渲染视图（PDF/表格/代码） |
| 精确反馈 | 描述位置痛苦（"第三段那个公式"） | 在渲染视图上直接选中 + Cmd+K |
| 批量处理 | 逐个问效率极低 | 品鉴队列 + 批量操作 |
| 全局监控 | IM 是串行的，看不到并行状态 | Monitor 活动态势面板 |

### 两个关键战略判断

**判断一：未来所有主流软件都会 Agentic 化。** 飞书有 CLI，Google Workspace 有完整 API，Overleaf 天然可 CLI。Agent 通过 CLI 操作一切是不可逆趋势——Octo 架构必须顺应这个趋势。

**判断二：Octo 不能以 IM 为轴。** 以 IM 为核心，打不过企微和飞书。Octo 的机会是"让他们抛弃以 IM 为轴的思路，他们做不到——而这个路径恰好更适合 Agentic Working 的新时代"。

### 正反馈飞轮

**用得越多 → Context 越厚 → AI 反馈越准 → 品鉴越高效 → 产出越好 → 积累更多好 Context → 循环。**

---

## 为什么重要

### 差异化的护城河来源

飞书/企微的设计哲学是"人与人协作"，一旦他们要支持 Agent 原生协作，就需要推翻整个 IM 中心化的产品假设——他们的现有用户不允许他们这样做。

Octo 从第一天就为 Agent 原生设计，因此可以在"Agent 协作"这个维度上达到飞书/企微无法企及的体验深度。

### "以品鉴为轴"的产品哲学

品鉴（通过/驳回/批注）是品鉴者与 Agent 交互的核心行为——这是"我品故我在"的产品落地。所有 GUI 设计都服务于一个目标：让品鉴者的 taste 更快、更准、更无摩擦地被 Agent 理解和执行。

---

## Connections

- [[otgo/sources/dual-native-design-v1.5-20260404|Dual-Native Design v1.5]] — 本概念的完整设计文档
- [[otgo/concepts/cli-decoupling|CLI 解耦]] — Dual-Native 的核心架构实现
- [[otgo/concepts/taste-philosophy|品 (Taste) 哲学]] — "以品鉴为轴"的哲学基础
- [[otgo/concepts/lonxia-matrix|龙虾矩阵]] — Dual-Native 服务的组织模型
- [[otgo/concepts/file-space|File Space]] — Context/Taste 的存储与飞轮的物理载体
- [[otgo/concepts/octo|octo 平台]] — Dual-Native 设计的产品载体
