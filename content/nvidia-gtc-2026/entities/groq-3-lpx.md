---
title: Groq 3 LPX
topic: nvidia-gtc-2026
type: entity
created: 2026-04-19
tags: [groq, lpu, inference, nvidia, prefill]
---

# Groq 3 LPX

## 概览

Groq 3 LPX 是 Groq 公司第三代 LPU（Language Processing Unit）的高密度版本，GTC 2026 上由 NVIDIA 宣布深度整合进 Vera Rubin AI Factory 体系。两者形成分工协作：LPU 专注 Prefill（首 Token 速度），GPU 专注 Decode（后续 Token 生成）。

---

## 关键数据

**Groq 3 LPU 单芯片**：
- 784B 晶体管
- 9.6 PFLOPs（FP8）
- 4 GB SRAM
- 1,200 TB/s SRAM 带宽（vs Rubin GPU 22 TB/s HBM4）：**55X 带宽优势**

**Groq 3 LPX 系统**：
- 每节点：8 LPUs + Host CPU + FPGA
- Scale-Up：256 芯片，640 TB/s 互联带宽
- 量产时间：**2H26**（2026年下半年）
- 互联格式：BF4（BlueField-4 集成）

**AI 推理性能（Groq 3 LPX 系统级）**：
- AI Inference Compute：315 PFLOPS
- SRAM Capacity：128 GB
- Memory Bandwidth：40 PB/s

---

## 分工逻辑

推理工作负载分两阶段：

| 阶段 | 描述 | 瓶颈 | 最优硬件 |
|------|------|------|---------|
| Prefill | 处理输入 prompt，生成 KV Cache | 内存带宽（读大量 token） | **Groq 3 LPU**（1,200 TB/s SRAM） |
| Decode | 逐 Token 自回归生成 | 计算吞吐（FLOPS） | **NVIDIA Rubin GPU** |

**NVIDIA Dynamo** 作为统一调度层，在 Vera Rubin NVL72 与 Groq 3 LPX 之间动态分配 Prefill/Decode 任务，实现整体最优的 Tokens/MW。

---

## Connections

- [[nvidia-gtc-2026/sources/gtc-2026-keynote|GTC 2026 主题演讲]] — 发布来源
- [[nvidia-gtc-2026/entities/vera-rubin|NVIDIA Vera Rubin NVL72]] — 与 Groq 3 LPX 协同的主计算平台
- [[nvidia-gtc-2026/concepts/inference-inflection|推理拐点]] — Groq 整合的商业背景
