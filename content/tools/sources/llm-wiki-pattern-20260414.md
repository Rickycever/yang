---
title: LLM Wiki 模式（Andrej Karpathy）
topic: tools
type: source
created: 2026-04-14
tags: [LLM Wiki, 知识库, RAG替代, 复利知识, Karpathy]
---

# LLM Wiki 模式

## Summary

A methodology for building personal knowledge bases using LLMs, proposed by Andrej Karpathy. The core departure from RAG: instead of retrieving from raw documents at query time, the LLM **incrementally builds and maintains a persistent wiki** — extracting, integrating, and cross-referencing knowledge as new sources arrive. The wiki is a **compounding artifact** that gets richer with every source added and every question asked.

<div class="zh-trans">Andrej Karpathy提出的使用LLM构建个人知识库的方法论。与RAG的核心区别：不在查询时从原始文档检索，而是LLM**增量构建并维护一个持久化的Wiki**——在新资料到来时提取、整合和建立交叉引用。Wiki是一个**复利产物**，随着每次添加资料和每次提问而变得更丰富。</div>

## Key Points

**The core difference from RAG:**
RAG: add files → LLM retrieves chunks at query time → generates answer → nothing is built up.
LLM Wiki: add file → LLM reads, extracts, integrates into wiki → updates entity pages, concept pages, synthesis → cross-references already exist at query time.

"The wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read."

<div class="zh-trans">与RAG的核心区别：RAG：添加文件→LLM在查询时检索片段→生成答案→什么都没有积累。LLM Wiki：添加文件→LLM读取、提取、整合到Wiki→更新实体页/概念页/综合页→查询时交叉引用已经存在。"Wiki是持久化的复利产物。交叉引用已经在那里。矛盾已经被标记。综合已经反映了你读过的一切。"</div>

**Three layers:**
1. **Raw sources** — immutable source of truth (LLM reads, never modifies)
2. **The wiki** — LLM-generated and maintained markdown files (summaries, entities, concepts, synthesis)
3. **The schema** — configuration document (CLAUDE.md / AGENTS.md) that makes the LLM a disciplined wiki maintainer

**Three operations:**
- **Ingest**: drop new source → LLM reads, writes summary, updates entity/concept pages, appends to log
- **Query**: ask question → LLM reads index, drills into relevant pages, synthesizes answer with citations. Good answers can be filed back as new pages.
- **Lint**: periodic health check — find contradictions, stale claims, orphan pages, missing cross-references, data gaps

<div class="zh-trans">三个操作：Ingest（摄入新资料，LLM写摘要+更新实体/概念页+追加日志）；Query（提问，LLM读索引+精读相关页+综合答案，好答案可归档为新页面）；Lint（定期健康检查，发现矛盾/过时内容/孤立页/缺失交叉引用/数据空白）。</div>

**Why it works:**
"The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass."

The human's job: curate sources, direct analysis, ask good questions, think about what it all means. The LLM's job: everything else.

<div class="zh-trans">"维护知识库的繁琐部分不是阅读或思考——而是记账。LLM不会感到无聊，不会忘记更新交叉引用，可以一次性修改15个文件。"人的工作：策划资料、指导分析、提好问题、思考整体含义。LLM的工作：其他一切。</div>

## Connections

- [[tools/concepts/llm-wiki|LLM Wiki 工具概念]] — the conceptual summary
- [[ai-business/concepts/context-system|上下文系统]] — enterprise-scale parallel concept: context as competitive moat
