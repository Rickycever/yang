---
title: Safe ChatFlow Delivery
topic: ai-customer-service
type: concept
created: 2026-11-01
tags: [dify, chatflow, compliance, workflow, retrieval]
---

# Safe ChatFlow Delivery

## Definition

Safe ChatFlow delivery is a set of design rules for Dify-based customer-service workflows: deterministic business logic stays in code, the LLM handles language and judgment within guardrails, and high-risk cases move to humans.

<div class="zh-trans">安全 ChatFlow 交付是一组面向 Dify 客服工作流的设计规则：确定性业务逻辑留在代码节点，LLM 在护栏内处理语言与判断，高风险案例转由人工处理。</div>

## How it works

Retrieval uses rewritten rather than raw user queries; topic-level chunks improve embedding quality; and a response should normally answer first and then ask one focused follow-up question. Graph-edge changes are major changes requiring full regression testing.

<div class="zh-trans">检索应使用改写后的用户问题而非原始输入；按主题组织的文本块能提升 embedding 质量；回复通常应先回答，再提出一个聚焦的追问。工作流图边改动属于重大变更，需完成全量回归测试。</div>

## Why it matters

These controls make the experience reliable enough for regulated customer conversations while keeping workflows adaptable across brands and use cases.

<div class="zh-trans">这些控制让系统能够在受监管的客户对话中保持可靠，同时仍可跨品牌、跨场景灵活适配。</div>

## Connections

- [[ai-customer-service/concepts/living-knowledge-base|Living Knowledge Base]] — The governed knowledge layer behind the workflow.
