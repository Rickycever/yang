---
title: 奔驰 CDP+MA 项目全景概览
topic: benz
type: overview
created: 2026-04-15
tags: [benz, cdp, marketing-automation, miaozhen, china-market]
---

# 奔驰 CDP+MA 项目全景概览

## 摘要

奔驰中国正在推进营销数字化中台建设，核心目标：基于已有 Databricks 数据湖，构建 CDP+MA 一体化平台，实现客户全生命周期精准营销。明略科技（与阿迪达斯标签增补项目为同一供应商）提交了完整应标方案，核心差异化竞争优势为数据主权（私有化部署，数据不出奔驰机房）+ 零侵入埋点兼容 + 汽车行业专属 ID 体系（人-车关系）。

---

## 核心概念

- [[benz/concepts/marketing-automation|Marketing Automation（营销自动化）]] — MA Canvas 编排、全渠道触达、AI Agent 赋能、效果闭环
- [[benz/concepts/agent-ready-data-platform|Agent-Ready 数据中台]] — 专为 AI Agent 设计的数据基础设施范式（MCP 标准接口 + 全模态存储 + 可观测性）

---

## 核心实体

- [[benz/entities/benz|奔驰中国]] — 需求方，已有 Databricks 数据湖，BMBS CRM 为核心系统
- [[adidas/entities/miaozhen|秒针 / 明略科技]] — 应标供应商（跨话题引用，与阿迪达斯项目为同一供应商）

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 首次实施时限 | 3 个月（自项目启动） |
| 系统可用率要求 | ≥ 98.5% |
| P1 故障恢复 | ≤ 4 小时（RTO） |
| 数据丢失容忍 | ≤ 1 小时（RPO） |
| API 响应要求 | P99 ≤ 500ms |
| 百万人群圈选 | ≤ 30 秒 |
| 实时标签更新 | ≤ 5 秒（P90） |

---

## 三阶段交付路线

| 阶段 | 时间 | 里程碑 |
|------|------|------|
| Phase 1 — MVP | 0-3 个月 | CDP 底座 + 短彩信/站内信 + 3 个标杆场景 |
| Phase 2 — 全渠道 | 3-9 个月 | 微信/企微/APP Push + 实时标签 + Databricks 回流 |
| Phase 3 — AI 原生 | 9 个月+ | 车机/开屏 + 地理围栏 + AI Agent 策略推荐 |

---

## 明略科技竞争策略

本项目竞争格局为三方角逐（明略 vs 火山引擎 vs 腾讯）。明略的核心押注：

1. **数据主权**：奔驰不接受数据在字节/腾讯云，明略私有化部署满足这一关键约束
2. **零侵入**：奔驰已有埋点供应商且不接受双埋点，明略适配器架构无需替换
3. **汽车 ID 体系**：人-车关系三表（用户/车辆/人人车）是行业专属能力，已有 SGM 落地经验
4. **Databricks 原生对接**：效果数据原生回流数据湖，竞品需定制开发

---

## 时间线

- **2026-04-12**：明略科技提交 CDP+MA 完整方案 v1.0
- **2026-04-15**：资料入库 Wiki

---

## 来源

- [[benz/sources/miaozhen-benz-cdp-ma-proposal-20260412|明略科技奔驰 CDP+MA 完整方案]] — 供应商应标方案（业务框架 + 技术架构，含竞品矩阵）
- [[benz/sources/benz-sow-ma-saas|奔驰 MA SaaS 平台采购 SOW]] — 需求方采购文件（功能/技术/SLA/商务要求）
- [[benz/sources/miaozhen-cdp-pitch-2026|明略科技 CDP 产品提案 2026]] — 通用产品 Pitch（统·活·智框架，NeuroMA，头部客户）
- [[benz/sources/miaozhen-agent-data-platform-whitepaper-202604|明略科技 Agent-Ready 数据中台白皮书]] — 技术架构白皮书（MCP 接口层，三路存储，三类 Agent 场景）

---

## Connections

- [[adidas/overview|阿迪达斯 DMP 标签项目]] — 明略科技服务的另一大品牌，两个项目构成明略在大品牌数据智能业务的典型案例
- [[adidas/entities/miaozhen|秒针 / 明略科技]] — 本项目核心供应商
- [[ai-business/overview|AI 商业进化]] — CDP+MA 项目属于 AI+Data 企业数字化转型范畴
