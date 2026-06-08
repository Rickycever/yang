---
title: CAPI 归因管道
topic: cross-border-marketing-aigc
type: concept
created: 2026-06-08
tags: [capi, attribution, event-quality, creative-id, meta-ads]
---

# CAPI 归因管道

## 定义

CAPI 归因管道是通过 Meta Conversions API 把广告主服务端事件、Pixel 事件、内部埋点和 Creative ID 关联起来的数据基础设施。它是创意数据飞轮的燃料入口。

在 iOS 14.5+ 和浏览器隐私限制下，单靠 Pixel 已无法稳定支撑归因和模型训练。CAPI + Pixel 双轨部署成为出海投放数据闭环的底线。

## 运作方式

CAPI 事件需要包含 event_name、event_time、event_id、event_source_url、action_source、user_data、custom_data 和 attribution_data。其中 attribution_data.ad_id 是把转化事件、Ad、Creative 和素材连接起来的关键字段。

内部埋点还需要补充 session 行为、落地页停留、视频完播率、多触点归因和 creative_id。只有 CAPI 与内部埋点都带上 Creative ID 或可反推 Creative ID，后续才能做“素材特征 → 投放表现 → 训练样本”的 join。

## 为什么重要

没有 CAPI，AIGC 创意工具只能看到素材生成和投放结果的碎片，很难建立真正的数据飞轮。商业上，这意味着工具只能做“生产效率提升”，不能做“转化效率提升”。

CAPI 归因管道还决定了模型训练数据的可信度。错误的归因会把本来由渠道、预算、促销或外部事件造成的表现差异误归因到创意上，导致模型学习错误方向。

## Connections

- [[cross-border-marketing-aigc/concepts/creative-data-flywheel|创意数据飞轮]] — CAPI 是飞轮数据入口
- [[cross-border-marketing-aigc/sources/flywheel-a-data-flow|数据反馈优化大模型的数据流]] — CAPI 字段和 join 逻辑来源
- [[cross-border-marketing-aigc/concepts/meta-advantage-api-boundary|Meta Advantage+ 与 Marketing API 边界]] — CAPI 与 Marketing API 共同构成平台接口层
