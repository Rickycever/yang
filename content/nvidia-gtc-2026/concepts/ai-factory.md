---
title: AI Factory：AI 时代工业基础设施
topic: nvidia-gtc-2026
type: concept
created: 2026-04-19
tags: [ai-factory, data-center, nvidia, infrastructure]
---

# AI Factory

## 定义

AI Factory 是 NVIDIA 对"AI 时代数据中心"的重新定义——不是传统意义上的 IT 机房，而是**生产 Token 的工业设施**，类比制造业的工厂。原材料是数据，产品是 Token，核心设备是 GPU 集群。

---

## 运作方式

**核心等式**：AI Factory = 芯片 × 系统 × 软件 × 设施协同优化

NVIDIA 提出"极限协同设计（Extreme Co-Design）"：从芯片到机架到整栋建筑，统一规划 Power、Liquid Cooling、Networking，而非各层独立采购。

**DSX Platform（Data center Design eXperience）**：

| 模块 | 功能 |
|------|------|
| DSX Max-Q | 最大化能效比设计 |
| DSX Flex | 灵活部署配置 |
| DSX Sim | 建设前仿真验证 |
| DSX Exchange | 设计方案生态共享 |

**Vera Rubin AI Factory 密度对比**（同等 1GW）：

| 指标 | 旧架构（X86+Hopper） | Vera Rubin 架构 |
|------|---------------------|----------------|
| GPU 数量 | 600K | 300K（减半） |
| AI FLOPS | 1.2 ZFLOPS | 16 ZFLOPS（13X） |
| All-to-All Scale-up | 7.2 TB/s | 260 TB/s |
| Memory BW（含 Groq SRAM） | 2 EB/s | 100 EB/s |
| Tokens per Second | 2M | 700M（350X） |

**NVIDIA Space-1**：Vera Rubin 模块延伸至太空计算场景。

---

## 为什么重要

**供给侧**：AI Factory 的概念把算力生产从"IT 部门采购"变成"工业投资决策"，直接影响国家竞争力判断。这也是为什么各国政府开始以"主权 AI"为由大规模建设本地 AI Factory。

**需求侧**：对企业而言，自建 AI Factory 的门槛极高（能效/散热/网络要求全新）。这强化了云厂商和 NVIDIA 的双重护城河。

**成本结构**：DSX 框架把 AI Factory 的设计标准化，降低重复设计成本，同时也使 NVIDIA 生态更难被替代（设计工具绑定硬件路线图）。

---

## Connections

- [[nvidia-gtc-2026/sources/gtc-2026-keynote|GTC 2026 主题演讲]] — 本概念出处
- [[nvidia-gtc-2026/concepts/inference-inflection|推理拐点]] — AI Factory 服务的核心工作负载
- [[nvidia-gtc-2026/entities/vera-rubin|NVIDIA Vera Rubin NVL72]] — AI Factory 的核心计算单元
- [[industry-research/overview|行业研究]] — 量子计算对 GPU 行业的影响，与 AI Factory 趋势形成对照
