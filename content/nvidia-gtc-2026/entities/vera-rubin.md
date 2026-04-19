---
title: NVIDIA Vera Rubin NVL72
topic: nvidia-gtc-2026
type: entity
created: 2026-04-19
tags: [nvidia, gpu, vera-rubin, hardware, ai-factory]
---

# NVIDIA Vera Rubin NVL72

## 概览

NVIDIA 在 GTC 2026 发布的下一代旗舰 AI 计算平台，以物理学家 Vera Rubin（暗物质研究先驱）命名。是 Blackwell 之后的下一代架构，整合 GPU（Rubin）、CPU（Vera）、DPU（BlueField-4 STX）、LPU（Groq 3）、网络（NVLink 6 + Spectrum CPO）为一体的完整机架系统。

---

## 关键数据与规格

**Rubin GPU**：
- 336B 晶体管
- 50 PFLOPs（NVFP4）
- 288 GB HBM4，22 TB/s 内存带宽

**Vera CPU**：
- 256 核
- 300 TB/s LPDDR5X
- ETL Spine 专用互联
- 吞吐量：6.5X vs 上代

**BlueField-4 STX（DPU）**：
- 5x Tokens/sec
- 50 Tb/s 网络带宽
- 16TB Shared Context / GPU

**NVL72 系统级规格**：
- 3.6 EF NVFP4 算力
- 1.6 PB/s HBM4 带宽
- 260 TB/s NVLink 6 机内互联
- 性能/功耗：**10X vs Blackwell NVL72**

**完整 7 芯片体系**：

| 芯片 | 功能 |
|------|------|
| Rubin GPU | AI 计算主力 |
| Vera CPU | 数据预处理/ETL |
| CX9 | 400G 网络 |
| BlueField-4 (BF4) | DPU，智能网卡 |
| NVLink Switch | 机内 GPU 互联 |
| Groq 3 LPU | 高速 Prefill |
| Spectrum CPO | 光电共封装交换 |

---

## 技术路线图

```
2024: Blackwell (HBM3e) + Blackwell Ultra
2026: Rubin (HBM4) + Rubin Ultra (HBM4e) + Vera CPU + NVLink 6 Switch
2028: Feynman (Die Stacking + Custom HBM) + BlueField-5 + NVLink 8 CPO
```

**Rubin+LPX 组合**：将 Groq 3 LPX 与 Vera Rubin NVL72 集成，专攻 Ultra 档推理（$150/M tokens），AI Factory 年营收/GW 潜力达 $300B。

---

## Connections

- [[nvidia-gtc-2026/sources/gtc-2026-keynote|GTC 2026 主题演讲]] — 发布来源
- [[nvidia-gtc-2026/concepts/inference-inflection|推理拐点]] — Vera Rubin 的核心应用场景
- [[nvidia-gtc-2026/concepts/ai-factory|AI Factory]] — Vera Rubin 是 AI Factory 的核心计算单元
- [[nvidia-gtc-2026/entities/groq-3-lpx|Groq 3 LPX]] — Vera Rubin 的 Prefill 协同芯片
