---
title: SaaS 终结？——激进派 vs 保守派
topic: shixiang
type: concept
created: 2026-04-19
tags: [saas, software, agent, ontology, palantir]
---

# SaaS 终结？

## 定义

高价值 Agent 对 SaaS 软件形成实质性冲击，引发"Software is being eaten"（软件被吞噬）的争论。拾象社群将两种立场结构化为激进派（软件被吞噬）和保守派（Software as Tools）。

---

## 两派观点

### 激进派：软件被吞噬

**核心逻辑**：软件本质上只是流程的载体。当 Agent 能直接操作数据和 API 时：
- 专为人类设计的复杂 UI 和业务逻辑封装（审批流、填表）将失去意义
- Agent 会直接绕过"中间态"，接管任务
- 传统软件开发的精细化分工（前端/后端/测试/UI）失去物理基础——一人在 Agent 辅助下，80% 认知设计 + 20% 执行

**代表案例**：TapTap Creator——不懂代码的用户输入"把贪吃蛇做成 3D"，系统直接生成游戏内容。Unity/Unreal 等复杂引擎将被自然语言生成取代。

**真正受冲击的对象**：从 Excel 切分蛋糕的 SaaS（如 Airtable），而非微软本身（因为 Claude in Excel 是正和游戏，会生产更多 Excel 文件）。

### 保守派：Software as Tools

**核心逻辑**：必须区分人与工具：

| 维度 | Agent（工人） | 软件（工具/机器） |
|------|-------------|----------------|
| 准确性 | 概率性输出 | 100% 确定稳定 |
| 角色 | 做判断、发明创造 | 流水线精确执行 |
| 类比 | 老师傅 | 焊接电路板的机器 |

- 企业软件（ERP 等）核心价值在于**绝对稳定和可复现**，这是概率性 Agent 无法替代的
- 软件不会被替代，而会**退化为底层工具和数据库**，由 Agent 通过代码驱动（而非 UI 供人点击）
- 软件的未来壁垒 = **Ontology（本体论）**：定义清楚企业内部组织逻辑、隐私边界和业务上下文

**Palantir 路径**：Ontology 正是 Palantir 构建护城河的核心——帮助企业定义"数字骨骼"，是 Agent 操作数据的语义前提。

---

## 为什么重要

**对销售决策**：判断客户是否会迁移 SaaS 预算到 Agent，关键看他们的工作流是否需要"概率性创意"（适合 Agent）还是"确定性执行"（仍需软件）。

**对企业战略**：SaaS 公司的应对路径：从"UI 宿主"转型为"数据/Ontology 定义者"。谁控制了业务上下文和数据语义，谁就是 Agent 时代的软件护城河。

**对投资视角**：美股 SaaS 被普遍看空（激进派叙事主导），但保守派视角指向了 Palantir 等 Ontology 类公司的长期价值。

---

## Connections

- [[shixiang/sources/best-ideas-agent-2026-feb|Best Ideas Agent 讨论（2026-Feb）]] — 本概念出处
- [[palantir/concepts/fde-model|Palantir FDE 模式]] — 保守派"Ontology"壁垒的最佳实践者
- [[nvidia-gtc-2026/concepts/agent-as-a-service|Agent-as-a-Service]] — 从 SaaS 到 AaaS 的宏观背景
- [[shixiang/concepts/agent-infra|Agent 专用 Infra]] — SaaS 退化为底层工具后，Agent Infra 层成为新机会
