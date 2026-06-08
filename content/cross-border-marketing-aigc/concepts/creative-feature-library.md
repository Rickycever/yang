---
title: 创意特征库
topic: cross-border-marketing-aigc
type: concept
created: 2026-06-08
tags: [creative-features, feature-store, clip, llm-labeling, performance-mapping]
---

# 创意特征库

## 定义

创意特征库是把每条广告素材的视觉特征、文案特征和业务元数据结构化存储，并与投放表现数据关联的资产库。它是从“素材表现好不好”走向“素材为什么表现好”的关键中间层。

在 AIGC 创意工具中，创意特征库通常通过 creative_id 连接素材库、ad_performance 表和训练样本表。

## 运作方式

视觉特征可由 CLIP、DINOv2 或自训练模型抽取，包括主体类型、主体占比、构图、色调、饱和度、背景复杂度、人脸、文字和 Logo 等。

文案特征可由 LLM 抽取，包括卖点类型、CTA 类型、文本长度、关键词和情感极性。业务元数据则包括行业、产品类目、目标受众、投放时段、版位和创意生成方式。

这些特征与 CTR、Hook Rate、IPM、CVR、CPA、ROAS、审核通过率、品牌一致性等指标关联后，可以用于特征到表现映射查询、Prompt 模板优化和模型训练样本构造。

## 为什么重要

没有创意特征库，投放团队只能看到结果指标，很难沉淀可迁移经验。创意特征库让团队知道“什么类型的素材在什么行业、什么受众、什么版位下有效”。

商业上，创意特征库是 AIGC 工具从“生成工具”升级为“决策工具”的关键。它让系统不仅能生产素材，还能解释、筛选和优化素材。

## Connections

- [[cross-border-marketing-aigc/sources/flywheel-a-data-flow|数据反馈优化大模型的数据流]] — 创意特征抽取和表结构来源
- [[cross-border-marketing-aigc/concepts/creative-data-flywheel|创意数据飞轮]] — 特征库是飞轮沉淀的数据资产
- [[cross-border-marketing-aigc/concepts/industry-template-system|行业模板体系]] — 模板优化依赖特征与表现映射
- [[cross-border-marketing-aigc/concepts/capi-attribution-pipeline|CAPI 归因管道]] — 特征库需要归因数据完成 join
