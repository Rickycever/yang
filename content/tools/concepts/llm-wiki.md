---
title: LLM Wiki
topic: tools
type: concept
created: 2026-04-14
tags: [LLM Wiki, 知识管理, RAG替代, Quartz, Obsidian]
---

# LLM Wiki

## Definition

LLM Wiki is a personal knowledge management pattern where an LLM incrementally builds and maintains a structured, interlinked wiki from raw source documents. Unlike RAG (which retrieves at query time), the LLM writes and updates the wiki as new sources arrive — creating a compounding knowledge base where synthesis and cross-references accumulate over time.

<div class="zh-trans">LLM Wiki是一种个人知识管理模式，LLM从原始资料文档增量构建并维护一个结构化的相互链接的Wiki。与RAG（在查询时检索）不同，LLM在新资料到来时写入和更新Wiki——创建一个综合和交叉引用随时间积累的复利知识库。</div>

## How It Works

**Practical setup (this wiki's implementation):**
- Raw sources: `/Users/ricky/Documents/AI笔记本` (Obsidian notes)
- Wiki: `/Users/ricky/Documents/MyWiki` (Quartz + LLM-generated pages)
- Schema: `SCHEMA.md` — defines page types, bilingual format, wikilink rules
- Tool: `/llm-wiki` Claude Code skill

**Page taxonomy:**
- `source/` — per-document summaries with key points + quotes
- `concept/` — extracted concepts, how they work, why they matter
- `entity/` — profiles of people, organizations, products
- `synthesis/` — cross-cutting analysis spanning multiple sources
- `overview/` — topic entry points

**Indexing:**
- `index.md` — catalog of all pages, updated on every ingest
- `log.md` — append-only operation history (grep-parseable)

<div class="zh-trans">实践设置（本Wiki的实现）：原始资料（AI笔记本，Obsidian笔记）→Wiki（MyWiki，Quartz+LLM生成页面）→Schema（SCHEMA.md，定义页面类型、双语格式、Wikilink规则）→工具（/llm-wiki Claude Code技能）。页面分类：source（文档摘要）、concept（提炼的概念）、entity（人/组织/产品档案）、synthesis（跨资料综合分析）、overview（话题入口）。索引：index.md（所有页面目录）+log.md（操作历史，可grep解析）。</div>

## Why It Matters

This is the personal-scale implementation of the same principle as enterprise context systems: **knowledge compounds through structured maintenance**. Each new source added to the wiki touches 5–15 existing pages — updating, connecting, flagging contradictions. By the time you ask a question, the answer is half-written already.

<div class="zh-trans">这是与企业上下文系统相同原则的个人规模实现：**知识通过结构化维护复利增长**。添加到Wiki的每个新资料会涉及5-15个现有页面——更新、连接、标记矛盾。当你提问时，答案已经写了一半。</div>

## Connections

- [[tools/sources/llm-wiki-pattern-20260414|LLM Wiki 模式（Karpathy原文）]] — source
- [[ai-business/concepts/context-system|上下文系统]] — enterprise-scale parallel concept
- [[tools/overview|工具方法论概览]] — topic overview
