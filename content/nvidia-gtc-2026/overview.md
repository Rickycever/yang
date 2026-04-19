---
title: NVIDIA GTC 2026 全景概览
topic: nvidia-gtc-2026
type: overview
created: 2026-04-19
tags: [nvidia, gtc, inference, ai-factory, vera-rubin, agent, openclaw]
---

# NVIDIA GTC 2026 全景概览

GTC 2026 是 NVIDIA 的年度战略发布会，核心信号：**推理拐点已经到来**，AI 商业化进入新阶段——Token 是新大宗商品，算力即营收，AI Factory 是新工业基础设施，Enterprise IT 正从 SaaS 向 Agent-as-a-Service 迁移。

---

## 核心概念

- [[nvidia-gtc-2026/concepts/inference-inflection|推理拐点（Inference Inflection）]] — 推理成为 AI 主工作负载，10,000X ChatGPT 算力需求，Token 经济五档定价
- [[nvidia-gtc-2026/concepts/ai-factory|AI Factory]] — AI 时代的工业基础设施，极限协同设计（DSX），1GW Vera Rubin 产 700M Tokens/sec
- [[nvidia-gtc-2026/concepts/agent-as-a-service|Agent-as-a-Service（AaaS）]] — 企业 IT 文艺复兴，从 SaaS 到动态 Agent 服务的范式转移

---

## 核心实体

- [[nvidia-gtc-2026/entities/vera-rubin|NVIDIA Vera Rubin NVL72]] — 新旗舰平台，10X Perf/W，7 芯片 5 机架体系，$300B 营收机会
- [[nvidia-gtc-2026/entities/groq-3-lpx|Groq 3 LPX]] — NVIDIA 深度整合的 LPU，1,200 TB/s SRAM 带宽，专攻 Prefill
- [[nvidia-gtc-2026/entities/openclaw|OpenClaw]] — 开放 Agent 协议，NemoClaw 参考实现，Nemotron 3 Super 配套模型

---

## 关键数据

| 指标 | 数值 |
|------|------|
| ChatGPT 以来推理算力增长 | 10,000X |
| Blackwell vs Hopper Token 成本 | 35X 更低 |
| Rubin vs Blackwell Tokens/MW | 10X 更高 |
| Rubin+LPX AI Factory 年营收潜力/GW | $300B |
| Vera Rubin NVL72 性能/功耗 vs Blackwell | 10X |
| 1GW Vera Rubin Tokens/sec | 700M（vs 旧架构 2M） |

---

## 时间线

- **2024**：Blackwell 发布，Blackwell Ultra
- **2026**：Rubin + Vera CPU + Groq 3 LPX + BlueField-4 STX + OpenClaw / NemoClaw 发布（本次 GTC）
- **2H26**：Groq 3 LPX 量产
- **2028**：Feynman（Die Stacking + Custom HBM）+ BlueField-5 + NVLink 8 CPO

---

## 来源

- [[nvidia-gtc-2026/sources/gtc-2026-keynote|GTC 2026 主题演讲 PDF]] — 76 页，Jensen Huang，2026

---

## Connections

- [[industry-research/overview|行业研究]] — 此前已有 NVIDIA vs 量子计算防御策略分析，GTC 2026 是延续
- [[ai-trends/overview|AI趋势 2026]] — 推理拐点、Agent 主流化与 GTC 判断高度吻合
- [[otgo/overview|OTGO]] — octo 平台加入 OpenClaw 生态
- [[shixiang/overview|拾象AI洞察]] — Proactive Agent 胜负手判断与 AaaS 趋势呼应
