---
title: 明日 AI 能力中心
topic: miaozhen
type: concept
created: 2026-05-12
tags: [mingri, ai-agent, clawhub, dmp-agent, skill, human-in-loop]
---

# 明日 AI 能力中心

## 定义

明日数据在自身 DMP 核心能力之上构建的 AI Agent 层，包含两个分发渠道：**AI 市场**（在第三方 Agent 平台 ClawHub 发布 DMP Agents）和**技能商店**（按场景封装 DMP 专项 Skills）。核心理念是将传统需要人工操作的 DMP 工作流，转化为 AI 可自动化执行的 Agent 任务。

---

## 运作方式

### 已发布 Agents（ClawHub）
1个月内 200+ 下载，已上线：
- **基础功能 Agents**：圈包、画像等基础操作自动化
- **离线画像 Agents**：批量画像分析任务
- **全自动画像洞察 Agents**：四层输出结构——人群总览 → 各标签 Top 分析（地域/属性/兴趣/APP/手机/线下） → 综合策略建议（产品/渠道/内容/区域市场） → 深度分析建议（洞察到执行的过渡）
- **智能人群圈包 Agents**：含 4 个人机协同确认节点

### 智能圈包 Agent 的人机协同节点

| 节点 | 确认内容 |
|------|---------|
| 节点 1 | 标签推荐列表（标签 ID/名称/选择理由/所有方）+ AND/OR 组合逻辑 |
| 节点 2 | 圈包方案信息确认（创建前） |
| 节点 3 | 投前测量与洞察结果确认 |
| 节点 4 | 投放订单信息最终确认（创建前） |

这种"自动化 + 关键节点人工确认"的设计，是 DMP 操作高风险性（直接影响广告投放预算）的应对策略。

### 技能商店（Skill Store）
- 按场景和功能封装的专项 Skills，供 AI Agents 调用
- 目标：让 Agent 平台中的任意 Agent 能"看得懂、高质高效"地调用 DMP 服务
- 状态：开发中（截至 2026-05-12）

---

## 为什么重要

1. **DMP 行业首批进入 Agent 生态**：明日数据率先在 ClawHub 发布 DMP Agents，是传统数据服务商向 Agent 化转型的早期信号
2. **Human-in-loop 设计范式**：圈包 Agent 的 4 节点确认机制，是高风险业务操作中 AI 自动化与人工控制平衡的参考案例
3. **ClawHub 作为分发渠道**：借助 OTGO 生态的 Skill 分发平台触达更广泛用户，而非自建流量入口

---

## Connections

- [[miaozhen/concepts/mingri-open-platform|明日开放平台]] — AI Agent 化的上层应用，开放平台是其基础设施
- [[miaozhen/entities/mingri-data|明日数据]] — 出品公司
- [[otgo/concepts/skill-marketplace|Skill Marketplace]] — ClawHub 是 OTGO 生态的 Skill 分发平台，明日数据是其上的内容提供商
- [[miaozhen/concepts/deepminer-agent-architecture|DeepMiner Agent 架构]] — 同赛道对比：DeepMiner 的 Swarm+Supervisor vs 明日的 4 节点 Human-in-loop
- [[ai-trends/concepts/agentic-ai-management|Agent 管理]] — 企业在 Agent 时代如何管控 AI 操作高风险业务的典型案例
