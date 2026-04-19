---
title: Voice Agent — 新一代 OS 入口
topic: shixiang
type: concept
created: 2026-04-19
tags: [voice-agent, ai-os, rtt, elevenlabs, vapi, retell, conversational-ai]
---

# Voice Agent — 新一代 OS 入口

## 定义

Voice Agent 是以语音为核心交互方式的 AI Agent，已超越 SaaS 工具范畴，正在成为定义下一代计算平台的 OS 级入口层。拾象判断：Voice 是所有 Agent 中最早跑通"真正 ROI"的方向。

## 运作方式

**模型层演进**：
- 传统架构：STT（语音转文字）→ LLM（推理）→ TTS（文字转语音）三段式
- 新架构：Real-time Speech-to-Speech（End-to-end STS）— 更快反应、更强情绪、更自然打断
- 路线分化：极致速度（Cartesia/Sonic-3 超低延迟）vs 极致真实感（拟人化对话）

**Infra 层（Voice OS）**：
- 核心模块：语音路由（SIP/WebRTC）、打断策略（barge-in/turn-taking）、模型编排（STT/LLM/TTS 组合管理）、监控 & Failover
- Vapi：快速搭建/多场景，PLG 强，适合多元 SME
- Retell：更稳/更低延迟，ARR ~$36M，适合高并发+高要求场景
- 开源补充：LiveKit（音视频 RTC，医疗大量采用）、Pipecat（可编排，自由接模型）

**部署路径**：BYO SIP → Vapi/Retell 调度层 → 自选模型 → CRM/EHR 互通 → 人工接管兜底

**为什么 Voice = 下一个入口层**：
- 最符合人类直觉的交互："开口即达"，零摩擦，远胜 App/Web 点击
- 高频低认知任务首选：速度极快，零学习成本，极大提升效率
- 跨设备 OS 层入口：随时在线，渗透各类智能终端与 IoT

**ROI 已验证的场景**：
- Inbound/餐饮/客服：成本砍半，漏接率下降80%+（最先跑通 PMF）
- Outbound/Sales/Collections：回款提升20-30%，AI 负责筛选人类专注转化
- 医疗挂号/分诊：等待时间下降50%，弃号↓80%+（ROI 最夸张赛道）
- 智能眼镜/穿戴式设备：成为 AI 眼镜的 OS 层

**ROI 核心指标**：Containment（拦截率）60-90%，满意度提升（不情绪化），AHT 下降，成本 $0.07-0.30/min vs 人工

## 为什么重要

1. **最早商业化的 Agent**：ROI 可量化、可验证，是整个 Agent 生态的排头兵
2. **新入口争夺**：Voice Agent 可能吃掉 Super App、Google Search、手机厂商的流量入口
3. **企业级壁垒深**：RTC 基建 + CRM/EHR 深度集成 + 全套上线体系形成真正护城河

## Connections

- [[shixiang/sources/shixiang-lp-meeting-dec-2025|拾象 LP Meeting Dec 2025]] — 本概念的主要来源
- [[shixiang/concepts/proactive-agent|Proactive Agent]] — Voice 是 Proactive Agent 的重要交互形态
- [[shixiang/synthesis/how-to-play-ai-beta|How to Play AI Beta]] — Twilio 是对应的二级市场标的
- [[shixiang/overview|拾象AI洞察 全景概览]] — 所属话题入口
