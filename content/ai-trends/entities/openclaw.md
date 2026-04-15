---
title: OpenClaw
topic: ai-trends
type: entity
created: 2026-04-15
tags: [openclaw, ai-agent, open-source, agent-platform, clawhub]
---

# OpenClaw

## 概览

OpenClaw是2026 Q1增长最快的开源Agent框架，国内俗称"小龙虾"，部署行为被称为"养虾"。它用极其直白的产品语言击穿了技术壁垒："我会一直在线、我会记住你说的话、我会自己把事情做完"——先看疗效再讲原理，让非技术圈层迅速涌入。

OpenClaw被腾讯科技AI白皮书定义为2026 Q1 Agent主流化趋势的起点事件。

---

## 关键数据与事件

**增长数据**：
- 60天内从9,000星增至247,000 GitHub星（其中前60天9K→157K星）
- 月活用户200万
- 22%员工未经IT部门批准即在工作中使用
- 深圳腾讯大厦楼下近千人排队求安装，市价炒至1000元

**行业领袖表态**：
- Sam Altman：最初决定不让Codex完全控制电脑的想法"只坚持了两个小时"，称其为继ChatGPT后又一转折点
- Dario Amodei（达沃斯）：连非技术人员都愿意为了使用Claude Code去折腾命令行，这直接促成了Cowork产品诞生
- Karpathy：将驱动了150万Agent注册的Moltbook称为"近期最接近科幻起飞的现实"

**资本事件**：
- OpenAI在情人节当天宣布收购OpenClaw创始人，明确列为产品核心，列入消费者计划白名单
- Cognition收购Windsurf后估值冲上百亿大关

**中国市场**：
- 深圳龙岗区和无锡高新区将OpenClaw写进政府补贴文件（最高补贴200万元，提供3个月免费算力）
- 触发"龙虾大战"：至少9家大厂同步推出桌面Agent产品

**平台封堵事件**：
- Google：大规模封禁通过OpenClaw调用Gemini的用户账户（技术原因：心跳机制每30分钟携带数万Token完整上下文，单用户实际消耗1000-3600美元/月 vs 250美元月费）
- Anthropic：1月9日部署客户端指纹识别，2月20日将行为定性为"Token套利"
- 本质是AI基础设施定价权之争，而非安全问题

**安全事件**：
- Clinejection事件：攻击者通过一个GitHub Issue标题触发提示词注入，在4000个开发者机器上安装了OpenClaw

**ClawHub生态**：
- OpenClaw衍生的Skill市场，半年内13,700+ Skills
- 单个Skill最高安装量18万
- 341个恶意Skill（占11.3%），36%含提示词注入

---

## Connections

- [[ai-trends/sources/tencent-ai-whitepaper-2026q1|腾讯AI白皮书2026Q1]] — 来源
- [[ai-trends/concepts/agent-mainstreaming|高自动化Agent主流化]] — OpenClaw是这一趋势的核心事件主体
- [[ai-trends/concepts/skill-knowledge-carrier|Skill知识载体]] — ClawHub是OpenClaw衍生的Skill生态，同时也是最早暴露供应链安全问题的平台
