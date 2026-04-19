---
title: LLMflation — LLM 推理价格通缩趋势
topic: shixiang
type: concept
created: 2026-04-19
tags: [llmflation, llm-cost, inference, pricing, agent]
---

# LLMflation — LLM 推理价格通缩趋势

## 定义

LLMflation 指 LLM 推理价格正在经历的快速通缩现象。以 MMLU 为统一质量标尺，自 GPT-3 发布以来，3年内同等能力的推理成本下降约 **1,000 倍**（每年约10倍）。

## 运作方式

**价格通缩的速度分层**（Epoch AI 数据）：
- 最快：900x/year（高难度任务能力）
- 中位：40x/year
- 最慢：9x/year（通用知识任务）

**高难度能力的成本下降速度在最近一年明显加快。**

**为什么体感不便宜？（成本10x下降，但感知是反的）**

Agent 和多模态让每次 API 调用从"一问一答"变成"一个小 workflow"：
- 多轮思考（Reasoning/Thinking 模式）
- 多次工具调用
- 中间状态总结

本来1次 API 调用就能完成的任务，现在变成 **5-10次内部调用**，且输入内容变长（文件、多模态、上下文全丢进来）。单价降了，但单任务总成本持平甚至上升。

## 为什么重要

1. **应用层的机会**：单位能力成本下降 1000 倍，意味着曾经"太贵、没法商业化"的 AI 用例正在快速变得可行
2. **Infra 的护城河**：在 LLMflation 背景下，谁能更高效地编排调用链（Vapi/Retell/n8n 等），谁就拥有真正的差异化
3. **AI 企业 ARR 的基础**：成本通缩 + 用量增长共同驱动了头部 AI 公司从 $0 到 $1B+ ARR 的惊人速度（Claude Code 2025年从0到$1B ARR）

## Connections

- [[shixiang/sources/shixiang-lp-meeting-dec-2025|拾象 LP Meeting Dec 2025]] — 本概念的主要来源
- [[shixiang/concepts/ai-bubble|AI Bubble]] — LLMflation 是 OpenAI 能实现 $200-300B 收入的重要前提
- [[shixiang/overview|拾象AI洞察 全景概览]] — 所属话题入口
