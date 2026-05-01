---
title: Skills 可编排架构
topic: ai-business
type: concept
created: 2026-05-01
tags: [Skills, MCP, 业务能力原子化, Agent编排, 意图驱动]
---

# Skills 可编排架构

## 定义

Skills 是业务能力的**原子单元**，是"系统能力"与"业务语义"之间的标准化翻译层。每个 Skill 是自然语言可描述的业务原子操作（如"查询客户信用额度""触发采购申请流程"），由 Agent 在上下文中动态编排组合成完整业务流程。

底层技术协议参考：Anthropic 2024年11月发布的 **MCP（Model Context Protocol）**——Skills 可理解为"企业语境下的 MCP Tools"。

---

## 运作方式

**一个 Skill 的完整定义包含五要素：**

| 要素 | 说明 |
|------|------|
| 名称和描述 | 自然语言可读，Agent 可直接理解 |
| 输入参数 | 类型、约束、说明 |
| 执行逻辑 | 调用哪个系统 API、执行什么操作 |
| 输出格式 | Agent 能理解并继续使用的结构化结果 |
| 权限边界 | 谁可以触发这个 Skill |

**Skills 按来源分为两类：**

- **平台 Skills**：由底层系统提供，相对稳定（"查询合同状态""触发报销审批""搜索员工信息"）
- **业务 Skills**：由业务团队根据自身规则构建，高度动态（"检查订单是否满足大客户优先级条件""生成本季度BD拜访建议"）

后者的可编排性，是这套架构区别于"把 Agent 接入 ERP API"的根本差异——业务规则不是硬编码的，而是动态的、可配置的、可用自然语言描述和调整的。

---

## 为什么重要

**传统业务规则的困境**：规则写在代码逻辑/数据库配置表/BPM流程引擎节点里，业务规则与技术实现高度耦合——改一个审批规则需要改代码→测试→发布→运维，业务人员完全没有控制权。

**Skills 实现的范式转移**：从"**流程驱动系统**"到"**意图驱动编排**"。

- 传统：系统按预设流程图执行，长尾场景全部失败
- Skills：Agent 根据当前意图和上下文，动态选择和组合 Skills，处理异常，请求人工确认

这也是 Agentforce、Microsoft Copilot 等产品的核心局限所在——它们的 Skills/能力体系仍处于早期，业务规则编排能力远未成熟。

---

## Connections

- [[ai-business/sources/im-agent-skills-kb-architecture-20260420|IM + Agent + Skills + KB：新一代企业软件架构]] — 本概念的原始来源
- [[ai-business/concepts/im-as-enterprise-entry|IM 作为企业统一入口]] — Skills 调用的触发入口
- [[ai-business/concepts/enterprise-knowledge-flywheel|企业知识飞轮]] — Skills 执行结果写回知识库，形成飞轮
- [[ai-business/concepts/gea-architecture|GEA 企业级智能体架构]] — GEA 中的"技能"层与 Skills 概念高度重叠
- [[ai-trends/concepts/mcp-model-context-protocol|MCP（Model Context Protocol）]] — Skills 的底层工业化协议标准
