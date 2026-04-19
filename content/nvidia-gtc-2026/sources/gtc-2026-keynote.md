---
title: NVIDIA GTC 2026 主题演讲 Keynote
topic: nvidia-gtc-2026
type: source
created: 2026-04-19
tags: [nvidia, gtc, inference, ai-factory, vera-rubin, agent]
---

# NVIDIA GTC 2026 主题演讲

**来源类型**：大会主题演讲 PDF（76页）  
**时间**：2026年  
**主讲**：Jensen Huang（黄仁勋）

---

## 摘要

GTC 2026 是 NVIDIA 的年度核心战略发布会。核心信号只有一个：**推理拐点（Inference Inflection）已经到来**。AI 工作负载已从训练转向推理，Token 成为新大宗商品，算力即收入。NVIDIA 围绕这一判断发布了全新硬件平台 Vera Rubin、深度整合 Groq 3 LPX、构建 AI Factory 基础设施规范，并将企业 IT 的未来定义为从 SaaS 转向 Agent-as-a-Service。

---

## 核心要点

### 1. 推理拐点：AI 商业逻辑的根本转变

- "Inference is the Workload. Tokens are the New Commodity. Compute is Revenue."
- ChatGPT 推出以来推理算力需求增长了 10,000 倍
- 所有头部推理 endpoint（Kimi K2.5、Qwen 3、GPT MoE 系列）均跑在 NVIDIA 上，NVIDIA 是全球推理标准
- 推理市场按"交互性（Tokens per Second/User）"分为五档：Free / Medium / High / Premium / Ultra，对应 $0 → $150 定价

### 2. 性能代际跃升：Blackwell → Rubin → Rubin+LPX

- **Blackwell vs. Hopper**：相同工作负载 35X 更低 Token 成本
- **Rubin NVL72 vs. Blackwell NVL72**：Tokens/MW 再提升 10X
- **Rubin+LPX 组合**：解锁 Ultra 档（$150/M tokens），整体年营收机会从 $30B（Hopper时代/GW）→ $150B（Rubin）→ **$300B（Rubin+LPX）**
- GB300 NVL72 vs 竞品：35X 更低成本，50X 更高 Perf/Watt

### 3. Vera Rubin NVL72：新旗舰平台

- 核心规格：10X Perf/W，3.6 EF NVFP4，1.6 PB/s HBM4，260 TB/s NVLink6
- Vera CPU：256核，300 TB/s LPDDR5X，ETL Spine，6.5X Throughput
- BlueField-4 STX：5x Tokens/sec，50 Tb/s 网络带宽，16TB Shared Context/GPU
- 完整 7 芯片体系：Rubin GPU + Vera CPU + CX9 + BF4 + NVLink Switch + Groq 3 LPU + Spectrum CPO

### 4. NVIDIA × Groq 深度整合

- Groq 3 LPX（LPU）整合进 NVIDIA 机架：784B 晶体管，9.6 PFLOPs FP8，4GB SRAM，1,200 TB/s SRAM带宽
- LPU 专注 Prefill（首Token速度），GPU 专注 Decode（后续Token生成），NVIDIA Dynamo 统一调度
- Groq 3 LPX：256芯片规模，640 TB/s Scale-Up带宽，2H26 量产

### 5. AI Factory：AI 时代的工业基础设施

- 1GW AI Factory 对比：旧架构（X86+Hopper）600K GPU，1.2 ZFLOPS；Vera Rubin 架构 300K GPU，16 ZFLOPS（13X 密度）
- DSX Platform：芯片→机架→AI Factory 全栈协同设计（DSX Max-Q / DSX Flex / DSX Sim / DSX Exchange）
- NVIDIA Space-1：Vera Rubin 模块化太空计算

### 6. 数据基础设施：结构化 + 非结构化

- 结构化数据：$120B 市场，AI Ground Truth
- 非结构化数据：100's ZB/年，AI Context 来源
- 代表案例：IBM+Nestlé（Order-to-Cash 从15min→3min，83%成本节省），Dell+NTT DATA（3X速度提升），Google Cloud+Snap（76%成本节省）

### 7. Agentic AI：从 SaaS 到 Agent-as-a-Service

- 企业 IT 正在经历"Renaissance"：SaaS → Agent-as-a-Service
- 发布 **NVIDIA NemoClaw**（OpenClaw 参考实现）：开放 Agent 构建工具包
- OpenClaw 已有 OTGO 等伙伴生态

### 8. NVIDIA 模型矩阵

| 模型 | 领域 |
|------|------|
| Nemotron 3 Super/Ultra | Agentic AI |
| Cosmos | Physical AI |
| GR00T N | Robotics |
| Alpamayo | Autonomous Vehicles |
| BioNeMo | Biology AI |
| Earth-2 | AI Physics |

- **Nemotron 3 Ultra**：5X 效率，最高 Reasoning 准确率（GB200 NVL72 上）
- **Nemotron 3 Super**：最佳 OpenClaw 开放模型
- 全球 Nemotron Coalition 扩张：TII、Sarvam AI、HUMAIN、AI Singapore、NAVER 等

### 9. DLSS 5：3D-Guided Neural Rendering

- 游戏侧：DLSS 5 基于 3D 几何引导的神经渲染，质量跃升

---

## 引用

> "Inference is the Workload. Tokens are the New Commodity. Compute is Revenue."

> "AI Factories are the Industrial Infrastructure of the AI Era."

> "Enterprise IT Renaissance from SaaS to Agent-as-a-Service."

---

## Connections

- [[nvidia-gtc-2026/overview|NVIDIA GTC 2026 全景概览]]
- [[nvidia-gtc-2026/concepts/inference-inflection|推理拐点（Inference Inflection）]]
- [[nvidia-gtc-2026/concepts/ai-factory|AI Factory：AI 时代工业基础设施]]
- [[nvidia-gtc-2026/concepts/agent-as-a-service|Agent-as-a-Service（AaaS）]]
- [[nvidia-gtc-2026/entities/vera-rubin|NVIDIA Vera Rubin NVL72]]
- [[nvidia-gtc-2026/entities/openclaw|OpenClaw 开放 Agent 协议]]
