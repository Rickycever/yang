---
title: OpenClaw 搜索能力架构
topic: otgo
type: concept
created: 2026-03-29
tags: [OpenClaw, 搜索架构, Token节省, Jina, MCP, 六层漏斗]
---

# OpenClaw 搜索能力架构

## Definition

OpenClaw's search capability follows a **6-layer funnel** designed to maximize information retrieval quality while minimizing Token consumption. Each layer progressively narrows candidates and routes requests to the most cost-effective tool. Designed by Gourmes (沟尔墨斯), OTGO's internal research agent.

<div class="zh-trans">OpenClaw的搜索能力遵循**六层漏斗**设计，目标是最大化信息检索质量、同时最小化Token消耗。每一层逐步缩小候选范围，并将请求路由到最具成本效益的工具。由OTGO内部研究Agent Gourmes（沟尔墨斯）设计。</div>

## How It Works

**The 6-layer funnel:**
```
Layer 1  Intent recognition   → "read content" vs "download file" → avoids wrong path entirely
Layer 2  Structured data       → api-router direct API call, skip search engines
Layer 3  Intent classification → 6 types determine information acquisition strategy
Layer 4  Site experience table → site-experience.md reuses known-good paths, no trial-and-error
Layer 5  Search broadcast      → multi-engine sweep yielding ≥10 results
Layer 6  Deep-read routing     → select optimal tool per site type, read top 3–5 results
```

<div class="zh-trans">六层漏斗：第1层意图识别→区分"读内容"vs"下载文件"；第2层结构化数据→api-router直调API跳过搜索引擎；第3层意图分类→6种类型决定信息获取策略；第4层站点经验查表→复用成功路径；第5层搜索广撒网→多路引擎获取≥10条结果；第6层内容精读分流→按站点类型选最优工具精读3-5条。</div>

**Search engine matrix:**
Brave Search (primary) → SearXNG (self-hosted, unlimited) → Tavily → Exa. Fallback chain: Brave → Tavily → Exa; if Brave down: SearXNG → Tavily → Exa.

**Content reading tool routing:**
- General web pages → **Jina Reader** (196× token savings vs raw HTML)
- WeChat / Xiaohongshu / Cloudflare-protected → Scrapling (stealthy_fetch)
- Lightweight JS pages → lightpanda (9× less memory than Chrome)
- YouTube / podcast → summarize tool
- PDF (URL) → Jina extract_pdf

**Key token-saving mechanisms:**

| Design | Savings mechanism | Magnitude |
|--------|-------------------|-----------|
| Jina Reader priority | HTML noise filtered to pure Markdown | **196× savings** |
| Use snippet directly | If ≥10 results and snippet suffices, skip deep read | Entire deep-read cost |
| Jina Reranker | 20 results → top 5 before deep read | 75% reduction |
| SearXNG self-hosted | No API quota limits | Search cost ≈ 0 |
| Structured data via api-router | Skip search layer entirely | Full pipeline skip |

<div class="zh-trans">关键Token节省机制：Jina Reader优先（196倍节省）；snippet够用则不精读（省整个精读成本）；Jina Reranker（20条→Top5，减75%精读）；SearXNG自托管（搜索成本≈0）；结构化数据走api-router（跳过整个搜索流程）。</div>

## Why It Matters

In a multi-agent system like OpenClaw, search is the most token-intensive operation. The 6-layer funnel design achieves efficient information acquisition at minimal cost — critical for sustainable token economics in a system where engineers consume $8,000/day and company-wide annual budget is $300M+.

<div class="zh-trans">在OpenClaw这样的多Agent系统中，搜索是最消耗Token的操作。六层漏斗设计以最低成本实现高效信息获取——在工程师日消耗$8000、公司年度预算$3亿+的Token经济体系中，这至关重要。</div>

## Connections

- [[otgo/concepts/openclaw|OpenClaw]] — the system this architecture is part of
- [[otgo/concepts/token-economy|Token Economy]] — the economic context that makes this optimization critical
- [[otgo/sources/openclaw-点火计划-20260317|OpenClaw 点火计划成果分享]] — real-world usage of this architecture
