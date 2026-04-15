---
title: 奔驰中国
topic: benz
type: entity
created: 2026-04-15
tags: [benz, mercedes-benz, automotive, china-market, cdp]
---

# 奔驰中国

## 概览

奔驰中国（Mercedes-Benz China）是梅赛德斯-奔驰集团在中国的运营主体，负责豪华汽车的销售、服务和数字化运营。在 CDP+MA 项目中，奔驰中国是需求方，正在推进营销数字化中台的建设。

**数字化特点：**
- 已建设 Databricks 数据湖，具备用户表/车辆表/人人车关系表基础数据资产
- 已有埋点供应商，**不接受双埋点部署**（关键约束）
- CRM 系统为 BMBS，BMBS 客户 ID 是核心主键
- 营销渠道分散，触达编排能力尚缺

---

## 关键数据

| 指标 | 数值/要求 |
|------|------|
| 目标实施时限 | 首次实施含数据初始化 3 个月内完成 |
| 系统可用率要求 | ≥ 98.5% |
| API P95 响应 | ≤ 500ms |
| 合规框架 | PIPL + 奔驰内部 DPOB 数据保护政策 |
| 人群圈选目标 | 百万级用户，≤ 30 秒 |
| 安全认证要求 | ISO 27001、SOC 2 Type II 或等效 |

---

## CDP+MA 项目关键约束

1. **数据主权**：奔驰不接受数据出境至供应商云（字节/腾讯），要求私有化部署
2. **埋点兼容**：已有埋点供应商不变，要求供应商方案零侵入（不争埋点份额）
3. **Databricks 兼容**：MA 系统必须与 Databricks 数据平台官方标准完全兼容
4. **BMBS 对接**：效果数据须回流至 BMBS CRM，驱动经销商跟进优先级
5. **三个月交付**：首次实施含数据初始化须在项目启动后 3 个月内完成

---

## Connections

- [[benz/overview|奔驰 CDP+MA 项目全景概览]] — 项目主页
- [[benz/sources/benz-sow-ma-saas|奔驰 MA SaaS 平台采购 SOW]] — 需求方采购文件
- [[benz/sources/miaozhen-benz-cdp-ma-proposal-20260412|明略科技奔驰 CDP+MA 完整方案]] — 中标供应商方案
- [[adidas/entities/miaozhen|秒针 / 明略科技]] — 应标供应商
