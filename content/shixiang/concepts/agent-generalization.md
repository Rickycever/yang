---
title: Agent 泛化三条路径——从几千万到几十亿用户
topic: shixiang
type: concept
created: 2026-04-19
tags: [agent, generalization, adoption, robot, embodied-ai]
---

# Agent 泛化三条路径

## 定义

当前真正使用过 Agent（Claude Code/Manus）的用户约几千万，而 Chatbot 用户已达 20 亿。要跨越这 50-100 倍的鸿沟，拾象提出三种维度不同的路径。

---

## 三条路径

### 路径 1：人群分层渗透

三种平行产品形态，同时推进，覆盖不同用户层：

| 形态 | 代表产品 | 目标用户 | 核心设计逻辑 |
|------|---------|---------|------------|
| 硬核工具 | Claude Code | 程序员 | 高门槛、极致控制权、Terminal/CI 环境，大量 Token 消耗换来 Agent 威力 |
| 生产力工具 | Manus | 知识工作者/白领 | "交钥匙"体验，不懂代码也能"一人抵一个团队" |
| 社交/大众产品 | OpenClaw IM Bot | 普通大众 | Telegram/Discord IM 嵌入，病毒传播，类比 AOL/Facebook 普及互联网 |

### 路径 2：电脑 vs. 手机——谁的产品范式？

**电脑派**：Agent 革命是智能本身的变革，不是分发渠道变革（不像移动互联网靠 App Store 爆发）。用户需要像当年学 DOS 命令一样跨越门槛，是精英向大众**缓慢渗透**的过程。

**手机派**：几十亿用户级别的普及必须像微信一样"零门槛"。终局需要等待 Google/Apple 在 OS 底层完成深度封装——**OS 级 Agent**，将环境配置、隐私安全等复杂问题全部"黑盒化"，只留极简交互界面。

### 路径 3：屏幕只是过渡，具身机器人才是终局

**当前局限**：
1. 数字 Agent 在为不完美的数字基建"填坑"（宝马跑在山路上）——这是临时解决方案
2. 主导 Agent 讨论的是程序员和投资人，对全球几十亿体力劳动者缺乏同理心

**终局判断**：Agent 必须进入物理世界，AI 从屏幕走出来，解决真实的体力劳动问题，才能实现真正的"大众化"。每年出现的新软件"壳"都是量变，具身机器人才是质变。

---

## 为什么重要

**对企业战略**：不同的泛化路径对应不同的客户获取策略。路径 1 指向"从程序员开始"（自下而上）；路径 2 指向"等待操作系统级整合"（自上而下）；路径 3 指向机器人/具身 AI 赛道。

**对 Ricky 的业务场景**：面向企业高管和知识工作者，Manus 类的"交钥匙"路径（路径 1 第 2 层）最接近当前采用节点。OS 级 Agent（路径 2 手机派）是未来 2-3 年的催化剂。

**对投资**：路径 3 是最长期的判断，但方向最明确——具身机器人是 Agent 的终极载体（与 NVIDIA GR00T 战略高度吻合）。

---

## Connections

- [[shixiang/sources/best-ideas-agent-2026-feb|Best Ideas Agent 讨论（2026-Feb）]] — 本概念出处
- [[shixiang/concepts/proactive-agent|Proactive Agent]] — OpenClaw 路径的技术核心
- [[shixiang/concepts/agent-infra|Agent 专用 Infra]] — 泛化的基础设施前提
- [[nvidia-gtc-2026/entities/openclaw|OpenClaw]] — 路径 1 大众社交形态的代表产品
- [[nvidia-gtc-2026/entities/vera-rubin|NVIDIA Vera Rubin NVL72]] — GR00T 具身机器人的算力基础
