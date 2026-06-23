---
title: WeCom Store Agent
topic: agentic-player
type: concept
created: 2026-06-23
tags: [wecom, restaurant-agent, private-domain, workflow, enterprise-agent]
---

# WeCom Store Agent

## 定义

WeCom Store Agent is an enterprise agent pattern that uses WeCom as the main interaction surface for store staff, operations teams, and headquarters teams. It combines chat, H5 cards, backend routing, APIs, knowledge retrieval, and task execution into one operational channel.
<div class="zh-trans">WeCom Store Agent 是一种企业智能体模式，以企微作为门店员工、营运团队和总部团队的主交互界面。它把聊天、H5 卡片、后台路由、API、知识检索和任务执行整合进同一个营运通道。</div>

## 运作方式

The pattern works best when frontline users need to complete routine business actions without switching systems. A user describes the task in natural language, the agent drafts or validates the request, and the backend handles the actual execution through business-system services.
<div class="zh-trans">这种模式最适合一线用户需要在不切换系统的情况下完成日常业务动作的场景。用户用自然语言描述任务，智能体负责生成或校验请求，后台再通过业务系统服务完成真正的执行。</div>

In the restaurant solution deck, this pattern covers transfer orders, sold-out and recovery actions, damage write-offs, repairs, work-order lookup, and knowledge questions. The same interface can also support notifications, confirmations, and exception handling.
<div class="zh-trans">在餐饮方案中，这一模式覆盖调拨、售罄与恢复、报损、报修、工单查询和知识问答。同一套界面还可以承载通知、确认和异常处理。</div>

## 为什么重要

For operations-heavy businesses, the channel matters as much as the model. Putting the agent inside WeCom reduces adoption friction, shortens response cycles, and keeps the workflow close to the people who actually execute the work.
<div class="zh-trans">对于重运营业务来说，入口渠道和模型本身同样重要。把智能体放进企微，可以降低使用阻力、缩短响应周期，并让流程更贴近真正执行工作的人。</div>

## Connections

- [[agentic-player/sources/rundian-enterprise-agent-solution-20260623|润典企业智能体解决方案]] — 本概念来源
- [[agentic-player/concepts/enterprise-agent-architecture|Enterprise Agent Architecture]] — 该模式的技术底座
- [[agentic-player/concepts/human-at-the-helm|Human-at-the-helm]] — 该模式的人机分工原则
- [[agentic-player/entities/xiaochubot|小厨bot]] — 这一模式中的产品实现
