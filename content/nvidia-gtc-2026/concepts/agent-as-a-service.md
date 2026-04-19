---
title: Agent-as-a-Service（AaaS）企业 IT 文艺复兴
topic: nvidia-gtc-2026
type: concept
created: 2026-04-19
tags: [agent, saas, enterprise-it, agentic-ai, openclaw]
---

# Agent-as-a-Service（AaaS）

## 定义

NVIDIA 在 GTC 2026 提出的企业 IT 演进判断：过去 20 年企业付费购买 SaaS 软件（静态功能订阅），未来将转向购买**能自主完成任务的 Agent 服务**（动态能力订阅）。软件的交付单位从"功能界面"变成"任务结果"。

---

## 运作方式

**范式对比**：

| 维度 | SaaS | Agent-as-a-Service |
|------|------|-------------------|
| 付费对象 | 软件使用权 | 任务完成结果 |
| 集成方式 | API 对接 | Agent 对话/工具调用 |
| 人机关系 | 人操作软件 | Agent 代替人操作 |
| 定价逻辑 | 按席位/月 | 按任务/结果 |

**NVIDIA 的基础设施布局**：

- **OpenClaw**：开放 Agent 协议/平台，类比 AI 时代的 HTTP 层
- **NVIDIA NemoClaw**：OpenClaw 的参考实现，提供构建专业化 Agent 的工具包
- **Nemotron 3 Super**：专为 OpenClaw 优化的旗舰开放模型

**Agent 生态关键层**（Keynote 架构图）：

```
Agent Frameworks/Protocols（OpenClaw, MCP 等）
        ↓
Frontier Model Builders → Model to Production
        ↓
AI for Customer Support / Software Dev / Healthcare / Robotics...
        ↓
Inference Frameworks → DL Frameworks
        ↓
NVIDIA AI Platform（GPU + 系统 + 软件）
```

---

## 为什么重要

**对企业决策者**：SaaS 竞争已进入存量博弈，而 AaaS 是尚未形成寡头的新蓝海。先建立 Agent 工作流的企业，将获得类似 2010 年代"率先上 SaaS"的先发优势。

**对销售侧**：从卖"软件席位"到卖"业务结果"，要求销售深入理解客户业务流程（而非功能对比）。这也是 Palantir FDE 模式价值的延伸版本——Agent 需要更深的驻场共创。

**NVIDIA 的战略意图**：通过 OpenClaw 控制 Agent 协议层，确保无论上层模型和应用如何竞争，NVIDIA 的推理基础设施始终是必经之路。

---

## Connections

- [[nvidia-gtc-2026/sources/gtc-2026-keynote|GTC 2026 主题演讲]] — 本概念出处
- [[nvidia-gtc-2026/entities/openclaw|OpenClaw]] — AaaS 的协议基础设施
- [[otgo/overview|OTGO]] — 构建企业 Agent 协作平台的代表性公司，octo 平台是 AaaS 的具体落地
- [[palantir/concepts/fde-model|FDE 驻场模式]] — AaaS 所需的深度驻场能力的先行者模式
- [[ai-trends/overview|AI趋势 2026]] — 腾讯白皮书提出 Agent 主流化，与 AaaS 判断吻合
