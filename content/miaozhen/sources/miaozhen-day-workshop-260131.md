---
title: 秒针Day Workshop 内部材料（2026年1月31日）
topic: miaozhen
type: source
created: 2026-04-16
tags: [miaozhen, deepminer, tracking, dmp, ai-use-case, pg-china]
---

# 秒针Day Workshop 内部材料（2026年1月31日）

## 摘要

明略科技/秒针系统于2026年2月2日举办的内部Workshop，向宝洁中国（P&G）团队汇报2025年回顾与2026年规划。议程四部分：①团队新成员介绍；②Tracking项目2026年规划；③DMP项目2026年规划；④AI for Media Operation & TVC Use Case分享。客户案例品牌包括：Pantene、Ariel、Tide、Pampers、SK-II、Whisper。

## 核心要点

### 一、团队组织架构

秒针团队在明略科技CEO吴明辉旗下，分为三大产品线：
- **Account Team**（客户服务）：孙方超SVP统筹，下设Tracking、DMP Targeting、DMP Measurement、Data Service四条业务线
- **Miaozhen Product Team**（秒针产品）：刘沛President，含媒体/社会化产品、DMP产品、技术、数据架构
- **AI Product Team**（AI产品）：含DeepMiner产品（黄楠）和AI Solution（杨纯 Ricky Yang）

### 二、Tracking 2026年规划

**2025年回顾 → 2026年重点方向：**

| 方向 | 2025完成 | 2026规划 |
|------|---------|---------|
| 监测透明度 | IEEE引入、监测研究定量化 | 持续优化升级 |
| 数据源整合 | 规则研究及定量化升级 | 蚂蚁集团合作（设备ID验真） |
| 风险识别 | 风险识别与量化、实验室&CBP报告 | 创新探索、深化治理 |

**IVT监测技术革新（素材真实性验证）**：
两套方案并行研究：
- **HSV色彩空间分析**：形变容忍度高（正样本99.89%），适合水印/比例调整场景，但对结构布局不敏感
- **感知哈希（Perceptual Hash）算法**：结构敏感度高，64位哈希值，计算<10ms，但对变化容忍度低（正样本64.07%）

**蚂蚁集团合作**：验证设备ID真实性（时空一致性检测），预计2026年2月上线。

**OAID采集问题**：不同APP授权/获取频次不一致，百度出现同一CBP用户对应3个不同OAID，正与信通院合作验证真实性。

**IPTV监测**：专网环境首次突破——SDK由广电总局开发，机顶盒通过专网上报至总局集群，秒针与总局分工完成收数→清洗→计算，预计春节后跑通整体流程。

### 三、DMP 2026年规划

**明日数据（Meiritai）2025年升级成果（for P&G）：**
- 品类数据：基于运营商DPI数据构建品类偏好人群，P&G测试：品类偏好+LAL引流电商，效果较好
- 聚类算法：K-Means对Member Shopper人群挖掘细分特征，发现"有趣"新特征人群，对小众品线拉新效果好
- 开放平台：已完成23个API开发（涵盖DMP全功能），被多个客户/平台接入用于AI/系统集成
- 分析平台：AI+洞察已接入明略DM，实现AI人群洞察，归因分析执行提效50%

**2026年价值升级方向：功能型服务平台 → 结果型服务平台（RaaS化）**

主要产品升级：
1. **明日DMP（人群策略平台）**：新增Uplift人群、Core TA人群、流失预测人群、电商/媒体/社媒画像，对接阿里/京东媒体
2. **明日分析平台（营销分析平台）**：MTA分析、人群对比分析、营销历程分析
3. **营销增长平台**：打通广告/推送/短信等公域触点，AI驱动选→投→测→优闭环
4. **开放平台**：API接口扩展 + MCP服务上线

**算法升级共研：**
- **UPLIFT模型**：相比Propensity模型更精准识别"广告敏感人群"（ΔCVR = 曝光CVR - 非曝光CVR）。当前面临三大挑战：种子不"干净"、链路不"单纯"、特征不"明显"。优化方向：Uplift-Tree模型+品类×周期×频次多维特征
- **Core TA研究**：通过iMedia找到符合eMedia Core TA定义的人群，两套方案：建模（Propensity）和三方数据规则对齐。JD侧三方数据规则包效果优秀

**明日DMP AI洞察架构升级（DM接入）：**
- BEFORE：以How-to为主（人工逐环节处理）
- AFTER：以Know-How为主（AI Agent Plan-Tools-Memory架构）
- 核心挑战：AI会"偷懒"漏掉内容、AI策略"太平"（无差异化观点）、AI会"胡诌"联想
- 解决路径：领域知识注入、跨域数据引入、营销数据集与知识库优化

### 四、AI Use Cases（三个实战案例）

**Case 1：Media Delivery Fast Check（媒体投放快速检查）**
- 目标：DM = 数据整合分析 + 自动化Alert + 问答助理
- 三步实现路径：PG Media指标计算层标准化 → Alert规则集成（业务逻辑而非三段式平均）→ 规范产出格式（建立可验证可传递的分析产出规范）
- 成果：https://deepminer.com.cn/share/ETguoZQFRCFd8lnLCMNcRg
- 关键洞察：通过Skill封装构建可验证的分析流水线，用"数据分析行为准则"约束AI联想路径

**Case 2：MOB PCU投放效果分析（DMP PCU后分析）**
- 背景：MOB PCU报告横跨DMP包准备、MZ投放策略、DSP Serving逻辑、TM/JD平台数据等多源，依赖专家暗默知识
- 解决方案：跨数据源报告解读Skill——数据字典表（指标映射）→ 确定性计算（代码编辑器）→ 标准化扫描 → 专家级推理 → 结构化报告
- 核心价值：将"隐性直觉"转化为"数字资产"，让专家从"数据体力活"回归"业务决策"

**Case 3：AI赋能人群机会洞察至TVC创意落地**
- 八步流程：数据采集（小红书249,572条笔记）→ 人群画像 → 热点话题分析 → 基础产品出创意方向 → 分镜脚本 → 基于脚本产品图 → 爬取新片场样片 → 样片复刻生成
- DeepMiner vs DeepSeek核心差异：
  - 数据上传：DeepMiner可读取249,572条，DeepSeek仅读4%（约200+条）
  - 数据源：DeepMiner对接秒针social数据库（小红书平台），DeepSeek只能用公开资料
  - 视频爬取：DeepMiner可基于指定网站提取参考视频，DeepSeek不支持

## Connections

- [[miaozhen/overview|秒针/明略科技 全景概览]] — 所属话题
- [[miaozhen/concepts/ivt-monitoring-tech|IVT监测技术革新]] — Tracking方向核心技术
- [[miaozhen/concepts/dmp-ai-insight|明日DMP AI洞察架构]] — DMP AI化升级路径
- [[miaozhen/concepts/ai-tvc-creation|AI赋能人群洞察至TVC创意]] — Case 3详解
- [[byhealth/entities/deepminer|DeepMiner]] — 三个AI Use Case的执行平台
- [[nestle/entities/miaozhen|秒针明略（nestle项目视角）]] — 同一实体在雀巢项目中的描述
