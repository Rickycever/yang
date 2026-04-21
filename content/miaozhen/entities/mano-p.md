---
title: Mano-P 1.0（明略科技 GUI感知智能体）
topic: miaozhen
type: entity
created: 2026-04-21
tags: [mano-p, gui-agent, osworld, mininglamp, open-source]
---

# Mano-P 1.0

明略科技（Minstec）发布的 GUI 感知智能体模型，定位为企业 AI 自动化"最后一公里"解决方案。Apache 2.0 开源，OSWorld 基准全球第一。

---

## 概览

| 属性 | 内容 |
|------|------|
| 发布方 | 明略科技（Minstec） |
| 发布时间 | 2026年 |
| 开源协议 | Apache 2.0 |
| 官网 | mano-p.mingtao.ai |
| 模型规格 | 4B（本地）/ 72B（云端完整版） |
| 定位 | GUI 感知 Agent，纯视觉操控任意 GUI 界面 |

---

## 关键数据

| 指标 | 数值 |
|------|------|
| OSWorld 任务成功率 | 58.2%（全球第一，专有模型榜） |
| 领先第二名（opencua-72b） | +13.2% |
| 全球 SOTA 数量 | 13项 |
| 4B本地模型推理速度 | 476 tokens/s |
| 峰值内存占用 | 4.3GB |
| 本地部署硬件要求 | Mac mini/MacBook M4，32GB+ 内存 |

**覆盖基准**：OSWorld · ScreenSpot-V2 · MMBench · UI-Vision · GUI Grounding · CUA评测 · 多模态感知认知 · 视频理解 · 长上下文学习

---

## 产品形态

1. **本地端侧**：Mac 设备离线部署，数据零上云
2. **算力棒**：USB 4.0 即插即用，快速扩展现有设备
3. **云端API**：72B完整版，最高性能，支持高并发

---

## 开源进展

- 已开源：Mano-CUA 核心技能（OpenClaw/Claude Code 可接入）
- 月内开源：本地模型 + SDK 组件
- 后续：训练方法、技术论文、Token剪枝、混合精度量化，支持定制 GUI-VLA

---

## Connections

- [[miaozhen/concepts/gui-agent-cua|GUI Agent / CUA]] — Mano-P 所属技术范式
- [[miaozhen/sources/mano-p-intro-20260421|Mano-P产品介绍（2026）]] — 来源文件
- [[miaozhen/concepts/deepminer-agent-architecture|DeepMiner多智能体架构]] — Mano 是 DeepMiner 的"灵巧手"执行层
- [[miaozhen/overview|秒针/明略科技]] — 出品公司
