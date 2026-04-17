---
title: Influencer Planner 平台
topic: pepsico
type: concept
created: 2026-04-17
tags: [influencer-marketing, kol, platform, saas, mininglamp]
---

# Influencer Planner 平台

## 定义

Influencer Planner 是明略科技为百事中国设计的端到端达人策略管理平台，覆盖达人营销全生命周期：从策略规划（Planning）→ 达人筛选（Vetting）→ 内容生产（Content）→ 效果测量（Measurement）。

核心定位：打破百事各品类/品牌独立运营达人营销的割裂状态，建立共享的数据资产、统一的评估标准、自动化的执行工具。

## 四大模块

```
Planning ──→ Vetting ──→ Content ──→ Measurement
  策略规划     达人审核     内容生产       效果测量
  历史复刻    三级风险      热点自动化    分钟级监测
  Smart Brief  CCFI评分    40s→6min     投后复盘
```

### Planning — 达人策略规划

**历史数据复刻**：读取过往项目数据（平台分布、内容类型、达人层级、预算结构），提炼最优组合规律，作为新项目策略起点。

**内核×外壳迭代框架**：
- 内核 = 品牌核心调性和传播主题（相对稳定，随品牌战略调整）
- 外壳 = 内容创意形式（随社交热点迭代，每月/每季更新）
- 框架帮助团队在保持品牌一致性的同时，快速适应平台内容趋势

输出：Smart Brief，包含达人画像要求、内容方向关键词、投放节奏建议、预算参考区间。

### Vetting — 达人智能审核

核心价值：将原本需要 2-3 天人工排查的达人背调压缩到小时级。

详见 [[pepsico/concepts/kol-vetting|达人审核与 CCFI 框架]]。

### Content — 内容生产加速

**DeepMiner 热点自动化流水线**：
- 40 秒内抓取全平台热榜、社交舆情、竞品内容动态
- 6 分钟内生成完整执行 Brief（含热点分析、内容方向、参考素材、关键词、发布时机）

**多模态智能打标**：
1. 输入：达人历史内容（视频+图文）
2. 多模态特征提取（视觉特征 + 文本语义）
3. embedding 向量化 → LLM 结构化理解
4. 输出：结构化标签（品类/场景/人群/情绪/调性）
5. 标签写入达人画像库，支撑 Planning 模块精准匹配

**合作伙伴执行层**：
- 北京破圈（小红书 ISP）+ 极创美奥（抖音官方认证）负责达人资源落地
- 零壹贰叁科技负责 AIGC 内容批量生产

### Measurement — 实时效果测量

- 分钟级曝光/互动数据更新（上线即监控）
- 负面舆情分级预警（红/橙/黄三级，自动触发）
- SLA：30分钟响应 / 4小时出方案 / 24小时修复
- 投后复盘报告：达人表现 CCFI 重新评分、ROI 拆解、下期策略建议

## 达人数据库规模

| 平台 | 达人数量 |
|------|---------|
| 小红书 | 80W+ |
| 抖音 | 120W+ |
| 快手 | 50W+ |

## 核心价值主张

| 痛点 | 解决方案 | 效果 |
|------|---------|------|
| 各品类达人资产割裂 | 统一达人数据库 | 跨品类共享，资产复用 |
| 人工筛选效率低 | CCFI + 三级风险自动评级 | 审核时间压缩 70%+ |
| 内容响应热点慢 | DeepMiner 40s→6min 流水线 | 内容产出速度 10x+ |
| 投后评估滞后 | 分钟级实时监测 | 风险处置窗口从天压缩到小时 |

## Connections

- [[pepsico/sources/influencer-planner-proposal-2026|百事×明略科技提案（2026.01）]]
- [[pepsico/concepts/kol-vetting|达人审核与 CCFI 框架]]
- [[pepsico/overview|百事×明略科技 Influencer Planner 全景概览]]
- [[miaozhen/overview|秒针/明略科技]] — 平台提供方，DeepMiner/DOMO 技术底座
