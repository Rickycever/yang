---
title: 明日DMP AI洞察架构（RaaS化转型）
topic: miaozhen
type: concept
created: 2026-04-16
tags: [dmp, ai-insight, raas, uplift-model, core-ta, mcp, open-platform]
---

# 明日DMP AI洞察架构（RaaS化转型）

## 定义

明日数据（Meiritai）是秒针/明略科技的DMP产品，2026年战略方向是从"功能型服务平台"升级到"结果型服务平台"（RaaS化——Results as a Service）。核心路径是将AI Agent引入DMP的每个功能层，把原本依赖专家判断的分析工作封装为可复用、可传递的"知识资产"。

## 运作方式

### 架构升级：How-to → Know-How

**旧模式（以How-to为主）**：
品牌方（BU/BA）提业务需求 → DA/DS翻译成数据需求 → DMP执行 → 人工包装报告 → 多轮确认 → 执行 → 效果反馈
- 优势：专业化处理，专家经验驱动
- 劣势：实现周期长，多环节传递失焦，对探索型业务不友好

**新模式（以Know-How为主）**：
AI Agent（Plan + Tools + Memory + Sub-Agent）基于封装好的最佳实践/场景能力/处理工艺，直接理解需求并执行
- 优势：灵活高效，以结果为导向，使用门槛低，快速复制
- 劣势：非最佳路径、AI执行质量不可控、对专业领域能力有限

**四大AI能力模块**：
- **AI Insight**：多源数据全维度洞察 + 北极星指标挖掘
- **AI Targeting**：基于营销目标+全链路效果数据分析与预测的人群圈选
- **AI Planning**：投放目标和方式下，不同定向人群转化效果测算及优化策略
- **AI测量**：多维度全链路评估投放效果，评估Marketing Driven的业务贡献

### 算法升级：UPLIFT模型

**研究目标**：找到广告敏感人群（即看了广告才会买、不看不会买的人），提升广告投放边际效益。指标：ΔCVR = 曝光CVR - 非曝光CVR

**三阶段研究进展**：
1. 可研与选型：确认Ad to购买存在因果关联性，正/负样本在P包中存在交叉分布
2. 离线效果验证：Uplift-T方式（P(A)-P(B)）和Uplift-S方式（P(C)）测试，结论：传统P模型无法有效识别广告对转化的因果性
3. 新方案设计（当前）：Uplift-Tree模型 + 优化负样本种子 + 品类×周期×频次多维特征

**三大挑战**：
- 种子不"干净"：正样本中无法区分是否不看广告也会买
- 链路不"单纯"：转化窗口长，曝光到购买期间干扰因素多
- 特征不"明显"：用户在"本品""广告"维度特征稀疏

### 算法升级：Core TA研究

**目标**：通过iMedia（内容媒体）找到符合eMedia（电商媒体）Core TA定义的人群，赋能内容营销，提升后效转化。

**两套方案**：
- 方案一：建模方式——探索Propensity模型各Tier下的匹配度，高分端匹配效果接近Shopper包
- 方案二：三方数据规则对齐——JD侧三方数据规则包效果优秀，推动天猫侧测试

### 2026年产品矩阵（明日数据）

| 产品层 | 产品名 | 核心能力 |
|--------|--------|---------|
| 人群策略平台 | 明日DMP | Uplift人群/Core TA/流失预测/电商画像 |
| 营销分析平台 | 明日分析平台 | MTA分析/人群对比/营销历程分析 |
| 营销增长平台 | 营销增长平台 | AI驱动选投测优闭环 |
| 数据服务平台 | 营销数据服务平台 | 营销主数据库/知识库/Panel/隐私计算 |
| 开放能力 | 开放平台 | 23个API + MCP服务（2026 H1） |

**MCP服务**：2026 H1新增，支持AI系统/平台以标准化接口接入明日DMP全部功能，是DeepMiner Agent接入DMP的技术桥梁。

## 为什么重要

1. **知识资产化**：将"隐性直觉"（专家经验）转化为"数字资产"（可复用的Skill和方法论），解决人员依赖问题
2. **RaaS商业模式**：从卖数据/服务 → 卖结果，与Palantir的RaaS路径高度一致，是DMP行业的商业模式升级方向
3. **UPLIFT vs Propensity**：Propensity模型只找"可能购买的人"，UPLIFT找"因为广告才购买的人"——后者才是广告真正的ROI来源

## Connections

- [[miaozhen/overview|秒针/明略科技 全景概览]] — 所属话题
- [[miaozhen/sources/miaozhen-day-workshop-260131|秒针Day Workshop材料]] — 内容来源
- [[miaozhen/concepts/ivt-monitoring-tech|IVT监测技术革新]] — 同属2026年能力升级
- [[byhealth/entities/deepminer|DeepMiner]] — AI洞察和Agent能力的底层平台
- [[palantir/concepts/raas|RaaS（Results as a Service）]] — 同一商业模式在Palantir的应用
- [[nestle/concepts/sales-driven-retargeting|Sales-driven Retargeting]] — 明日DMP在雀巢项目中的落地案例
