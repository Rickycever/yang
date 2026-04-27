---
title: Runtime Agent — 执行层 Agent
topic: otgo
type: concept
created: 2026-04-27
tags: [Runtime-Agent, 执行, Agent分工, 组织资产, 经济效益]
---

# Runtime Agent — 执行层 Agent

## 定义

Runtime Agent 是 Octo 多 Agent 架构中的**执行层**——专注于在干净环境中执行具体任务，完成即释放。与 OpenClaw（龙虾，个人编排层）构成 Octo 的双层 Agent 分工。典型实现：Claude Code（CC）、Codex Pro、Cursor、自研 Runtime。

---

## 运作方式

### OC vs Runtime Agent 分工表

| 维度 | OpenClaw（龙虾·编排层） | Runtime Agent（执行层） |
|------|----------------------|----------------------|
| **核心职责** | 编排——接收指令、拆解任务、调度 Agent、汇报 | 执行——在干净 context 中完成具体子任务 |
| **记忆** | 持久身份，长期跨任务积累 | 无记忆，每次从干净 context 启动 |
| **Token 成本** | 贵（OC 消耗是 Runtime Agent 的 5-10 倍） | 便宜 |
| **归属** | **个人资产**——随员工走，跟着人离职 | **组织资产**——团队共享运力，不跟个人绑定 |
| **典型类比** | 项目经理——记得你上次要什么 | 外包工人——给任务书就能干，干完走人 |

### 个人资产 vs 组织资产

这是事项设计带来的 SaaS 账本拆分：

- **OC 付个人订阅**——员工离职，OC 连同在其上积累的 taste 和事项历史一起带走。组织不扣留
- **Runtime Agent 付团队订阅**——这是组织购买的共享算力，人人可调用，集中采购可议价，不跟员工变动

对企业而言：个人订阅是员工的工具成本（员工自己消化或报销），组织订阅是基础设施成本（可集中管控）。两者分开，账本最清晰。

### 用户已有订阅的 Runtime Agent 直接接入

用户已经付费的订阅（Claude Max / Codex Pro / Cursor）可以直接接入当 Runtime Agent 使用：
- **Octo 不烧最大那份 Token**——编排和品鉴采集在 OC 侧，执行在用户自己的 Runtime 订阅侧
- 单用户订阅能做得很薄

### 基于真实工作的 Agent 评级

每个 Runtime Agent 在事项里的执行记录都会留存：
- 完成了多少事项
- 通过率多少（品鉴者通过的比例）
- 驳回率和驳回原因分布

这是**基于真实工作的口碑**，不是 benchmark 分数、不是发布会 PR。企业选用哪个 Runtime Agent，可以数据驱动。未来进入 Octo 生态的 Runtime Agent 需要"被事项考核过的履历"。

### 在多层 Agent 编排中的位置

```
品鉴者（人）
  └── OpenClaw（龙虾·编排）
        ├── 持有父事项
        └── 派子事项给 Runtime Agent（CC / Codex / 自研）
              ├── 执行具体任务
              ├── 写执行轨迹到事项载荷
              └── 标 in_review，交龙虾或人评
```

任意深度：Runtime Agent 可以继续派 Sub-Agent，每一层都通过事项的子事项结构承载。

---

## 为什么重要

### 解决 Token 经济的核心矛盾

OC 贵但擅长编排，Runtime Agent 便宜且擅长执行——硬让 OC 亲自写代码或画图是资源错配。分工后，贵的 Token 花在值得的地方（协调、品味、决策），便宜的 Token 花在执行上。

**架构根因**（2026-04-27 产品团队补充）：长记忆 Agent 的 context 被历史信息持续填充，每次都需要 Compact；Runtime Agent 每次任务从干净 context 启动。成本差距以实际案例量化：

| Agent 类型 | 完成 $1,000 价值任务的 Token 消耗 |
|-----------|-------------------------------|
| 龙虾 / 长记忆 Agent | 约 $1,000 |
| Claude Code / Runtime Agent | 约 **$100** |

**Octo 没有与龙虾（OpenClaw）强绑定**——这是刻意的产品决策（国内尚无人做这个区分）。Octo 保留对接任何长记忆 Agent（OpenClaw / Hermes）和任何 Runtime Agent 的能力，让两者在同一个 Space/Channel/Thread 里协作。

### 知识工作者保护的落地

"数字劳动力分身属于个人"不只是哲学宣言——OC 个人订阅 + 事项历史 + FileSpace 构成了一套具体的产权机制：
- 员工投入时间养出的 OC、积累的 taste、参与过的事项历史 → 归员工个人
- 企业购买的 Runtime Agent 算力 → 归组织
- 两者的权责边界清晰，Octo 的设计强制执行这个边界

---

## Connections

- [[otgo/sources/item-design-v2-20260427|事项（Item）设计 V2]] — Runtime Agent 分工的完整论述来源
- [[otgo/sources/octo-product-vision-20260427|Octo 产品架构与战略补充]] — Token 成本量化数据 + Octo 不强绑定龙虾的战略决策
- [[otgo/concepts/item|事项 (Item)]] — Runtime Agent 通过事项上报执行轨迹和产出
- [[otgo/concepts/lonxia|龙虾 (Lobster)]] — Runtime Agent 的上游编排者
- [[otgo/concepts/multi-cc-collab|多 CC 协作模式]] — Runtime Agent（CC）的协作模式
- [[otgo/concepts/token-economy|Token 经济]] — Runtime Agent 的成本经济性
- [[otgo/concepts/digital-avatar|数字分身]] — OC 是数字分身，Runtime Agent 是执行工具
- [[otgo/concepts/skill-marketplace|Skill Marketplace]] — Runtime Agent 的评级和 ClawHub 生态
