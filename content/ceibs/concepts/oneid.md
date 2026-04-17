---
title: OneID 打通
topic: ceibs
type: concept
created: 2026-04-17
tags: [oneid, identity-resolution, cdp, id-mapping]
---

# OneID 打通

## 定义

OneID 是将同一自然人在不同系统和平台上的多个 ID（手机号、微信 OpenID/UnionID、设备 ID、CRM ID、APP UID 等）归并为一个唯一标识符的过程，目的是形成统一的消费者视图（Single Customer View）。

## 运作方式

**三种打通方式**：

| 方式 | 机制 | 特点 |
|------|------|------|
| 优先级打通 | 按 ID 重要性排序（手机号 > UnionID > 会员号 > OpenID），有主次关系 | 减少无效绑定，降低计算复杂度 |
| 全关联打通 | ID 之间无主次，全量串联 | 覆盖最广，但计算复杂、关系链易错 |
| 算法打通 | 非确定性，通过 IP 时间轴等特征预测同一人的 ID | 不依赖强账号体系，可覆盖更多数据源 |

**底层技术**：
- 图计算（Graph Computing）：ID 之间的关系建模为图中的节点（Node）和边（Edge）
- Redis 存储：生成的 OneID 映射表实时存入 Redis，支持毫秒级查询
- 增量计算：新 ID 绑定事件触发局部重计算，不需全量重跑

**常见 ID 体系**（优先级从高到低）：手机号 → UnionID → 会员号 → OpenID

**企微打通额外维度**：将消费者 ID 与销售/导购员工 ID 关联，形成"消费者主题 × 员工/导购主题 × 映射关系主题"三层数据模型

## 为什么重要

中欧潜在学员的旅程横跨多个触点：朋友圈广告（微信 OpenID）→ 官网浏览（Cookie/Device ID）→ 企微咨询（External ID）→ CRM 录入（手机号）→ 报名系统（会员号）。没有 OneID，这五个触点看起来是五个人，无法形成完整的旅程视图。

OneID 是 CDP 的数据基础——标签、画像、MA 旅程都依赖统一用户视图才能正确运作。

## Connections

- [[ceibs/sources/mininglamp-proposal-2025|中欧×明略科技提案]] — 来源方案
- [[ceibs/overview|中欧商学院×明略科技 全景概览]]
- [[miaozhen/overview|秒针/明略科技]] — 明略 CDP 的 ID 打通核心能力
