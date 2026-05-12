---
title: 明日开放平台（Open Platform）
topic: miaozhen
type: concept
created: 2026-05-12
tags: [mingri, open-platform, mcp, api, dmp, ai-agent]
---

# 明日开放平台（Open Platform）

## 定义

明日数据将自身 DMP 标准平台的全功能以 **API + MCP** 形式对外开放，使系统集成商、IT 部门和 AI Agent 能够以代码/协议调用方式使用 DMP 的圈包、画像、投放等核心能力，而无需通过图形界面操作。

---

## 运作方式

- **API 接口层**：覆盖明日 DMP 标准平台所有功能，总量近 30 个，支持系统化/自动化调用
- **MCP 服务层**：基于 Model Context Protocol，让 AI Agent 能够直接将 DMP 服务作为工具调用
- **商务模式扩展**：开放平台引入了新的合作形态——AI 代理商、系统集成商可基于 API/MCP 再封装，扩大 DMP 的触达范围

典型调用链路：
```
AI Agent → MCP 工具调用 → 明日开放平台 API → DMP 核心引擎（圈包/画像/投放）
```

---

## 为什么重要

传统 DMP 是"人操作界面"的产品，开放平台将其转变为"机器可调用的服务"。这使得：
1. **AI Agent 化**成为可能——DMP 能力可以被 Agent 编排进营销工作流
2. **降低合作门槛**——技术部门无需购买完整 SaaS 席位，按 API 调用计费
3. **生态扩展**——ClawHub 等 Agent 平台可以将 DMP 能力封装为 Skill 分发给更广泛的用户

---

## Connections

- [[miaozhen/entities/mingri-data|明日数据]] — 出品公司
- [[miaozhen/concepts/mingri-ai-agent-center|AI 能力中心]] — 开放平台是 AI Agent 化的基础设施层
- [[otgo/overview|OTGO]] — MCP 是 OTGO 生态（octo/ClawHub）与外部数据服务对接的标准协议
- [[miaozhen/concepts/data-agent-framework|Data Agent 框架]] — 秒针 DeepMiner 的类似路径：DMP 能力 → Agent 化封装
