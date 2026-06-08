---
title: 数据反馈优化大模型的数据流
topic: cross-border-marketing-aigc
type: source
created: 2026-06-08
tags: [data-flywheel, capi, creative-id, model-finetuning, ab-testing]
---

# 数据反馈优化大模型的数据流

## 摘要

这份资料详细展开“飞轮 A：创意模型微调”的工程数据流，说明如何把广告投放表现转化为可用于 LLM、Diffusion、Video Gen 和数字人模型微调的训练样本。核心循环是：广告投放 → 表现数据回流 → 训练样本构造 → 模型微调 → 新创意生成 → 再投放。

资料强调，难点不在模型本身，而在数据采集、Creative ID / Ad ID 追溯、训练样本过滤、线上 A/B 评估、防 reward hacking、防数据漂移和冷启动等软工程问题。

## 核心要点

- 训练数据必须能追溯到具体 Creative ID 和 Ad ID，否则无法把转化表现归因到具体素材。
- CAPI 事件中的 attribution_data.ad_id 是连接转化数据、广告对象和创意素材的关键锚点。
- 内部埋点需要补充 session 行为、落地页停留、视频完播率、多触点归因和 creative_id。
- 创意特征抽取应覆盖视觉特征、文案特征和业务元数据，形成 creative_features 表。
- 训练样本必须剔除冷启动、预算烧光提前下线、失败 A/B 测试、特殊节日、违规和低转化样本。
- 验证集和测试集应按时间切分，避免广告数据的时序泄漏。
- 新模型必须经过线上 A/B，主指标看 CPA / ROAS，辅助指标看 CTR / Hook Rate / 审核通过率。
- 冷启动阶段建议使用行业 benchmark、少量高预算验证、迁移学习和规则模板 + LLM 润色。

## Connections

- [[cross-border-marketing-aigc/concepts/creative-data-flywheel|创意数据飞轮]] — 本资料对应飞轮 A 的工程实现
- [[cross-border-marketing-aigc/concepts/creative-feature-library|创意特征库]] — 数据仓库和模型训练之间的关键资产
- [[cross-border-marketing-aigc/concepts/capi-attribution-pipeline|CAPI 归因管道]] — 数据回流入口
- [[cross-border-marketing-aigc/synthesis/meta-side-opportunity|Meta 侧 AIGC 创意机会]] — Meta 平台数据闭环的落地依据
