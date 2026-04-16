---
title: DeepMiner 多智能体架构
topic: miaozhen
type: concept
created: 2026-04-16
tags: [deepminer, swarm-supervisor, multi-agent, cot, human-in-loop, mcp, architecture]
---

# DeepMiner 多智能体架构

## 定义

DeepMiner的技术架构以 **Swarm+Supervisor** 模式为核心，结合洞察思维链（CoT）模板沉淀、Human-in-the-loop工作流和MCP数据系统集成，实现企业级数据分析的自动化与可靠性。

## 核心架构：Swarm + Supervisor

```
用户输入任务
     ↓
Supervisor（统一理解任务，分解为子任务，调度分配）
     ↓
Swarm（多个专业Agent并行协作执行）
  ├── 数据采集Agent（Mano：Browser User数据采集）
  ├── 数据处理Agent（清洗/建模/标签对齐）
  ├── 分析推理Agent（归因/预测/洞察）
  └── 报告生成Agent（图文报告/可视化）
     ↓
输出：结构化洞察报告 / Dashboard / API / MCP
```

**设计原则**：
- Supervisor负责理解任务全局，防止子任务方向偏差
- Swarm中各专业Agent分工明确，高效协作
- 平衡**确定性交付**（收敛场景）与**探索性分析**（发散场景）的PLAN双模式机制

## Mano 数据采集技术

- **BUA**（Browser User Agent）：大模型驱动的浏览器用户行为数据采集
- **CUA**（Computer User Agent）：计算机端自定义插件数据采集
- 支持定制化垂直行业数据读取（指定权威机构/数据系统/社媒账号）

## 洞察思维链（CoT）模板沉淀

将分析师的隐性经验显性化，沉淀为可复用的标准流程：

- 覆盖典型结构：行业分析 / 营销复盘 / 人群洞察 / 趋势归因
- 每一个报告背后是一条"数据驱动的思维链"
- 效果：分析师经验SOP化，复制能力，提升下限
- 用户可将对话过程"保存为任务模板"，后续同类任务自动按最佳路径执行

## Human-in-the-loop 工作流

在全自动Agent执行过程中，支持按需插入人工判断节点：

```
Agent执行中 → 触发人工判断节点 → 人工介入/确认 → Agent继续执行
```

- 支持多角色协同：跑数 / 建模 / 撰写 / 润色
- 企业内部按需配置分析流程，满足灵活复杂需求
- 适合"收敛思维、零失误"的高精度业务场景

## 数据系统集成（MCP）

通过 **MCP（数据中台服务协议）** 实现企业私有数据打通：

| 数据类型 | 来源示例 |
|---------|---------|
| 秒针商业化数据 | KOL数据/社媒舆情/媒体洞察/明日DMP |
| 客户一方数据 | Excel文件上传 / CRM / 用户行为 / 投放数据 |
| 外部公开数据 | Web search / 电商平台 / 权威研究机构报告 |
| 定制化数据 | 指定账号/数据系统的专属采集 |

## 产品输出层

```
DeepMiner应用层
    ├── 生成式洞察报告（结构化文档）
    ├── Dashboard（可视化看板）
    ├── API（程序化接入）
    ├── MCP（AI系统接入）
    └── Sub-Agent调度（供上层AI系统调用）
```

## 与传统方案的差异

| 对比维度 | 传统数据产品 | DeepMiner |
|---------|------------|----------|
| 交互方式 | 专业人员操作，SQL/固定报表 | 自然语言，无需编码 |
| 分析深度 | 描述"发生了什么" | 回答"为什么"和"应该做什么" |
| 执行 | 人工转化为行动 | 自动执行A-PDCA-R闭环 |
| 经验积累 | 依赖个人分析师 | CoT模板沉淀，组织级SOP |
| 数据整合 | 预定义场景 | 多源动态接入 |

## Connections

- [[miaozhen/overview|秒针/明略科技 全景概览]] — 所属话题
- [[miaozhen/sources/deepminer-data-agent-deck-20250920|DeepMiner商业数据分析智能体Deck]] — 概念来源
- [[miaozhen/concepts/data-agent-framework|Data Agent框架]] — 上层定位框架
- [[byhealth/entities/deepminer|DeepMiner（实体页）]] — 产品实体
- [[byhealth/concepts/mano-cito|Mano+Cito双模型]] — DeepMiner底层模型能力
- [[benz/concepts/agent-ready-data-platform|Agent-Ready数据中台]] — 明略科技数据中台架构
