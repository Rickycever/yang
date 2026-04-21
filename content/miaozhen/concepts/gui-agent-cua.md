---
title: GUI Agent / CUA（Computer Use Agent）
topic: miaozhen
type: concept
created: 2026-04-21
tags: [gui-agent, cua, computer-use, rpa, automation]
---

# GUI Agent / CUA（Computer Use Agent）

## 定义

GUI Agent（也称 CUA，Computer Use Agent）是一类能够直接感知图形用户界面（GUI）并像人一样操作计算机的 AI Agent。其核心能力是：**看屏幕 + 做动作**，无需 API、无需代码注入，通过纯视觉理解任意软件界面并完成操作。

与传统 RPA（规则脚本自动化）的本质区别：RPA 依赖预定义规则和 DOM 结构，界面一变即失效；CUA 通过视觉理解适应变化，像人一样"看到什么就操作什么"。

---

## 运作方式

标准 GUI Agent 的执行闭环分四步：

1. **感知（Perceive）**：截取当前屏幕，使用视觉大模型识别 UI 元素（按钮、输入框、菜单等）
2. **规划（Plan）**：将自然语言指令拆解为具体操作步骤序列
3. **操作（Act）**：执行鼠标点击、键盘输入、窗口切换等动作
4. **验证（Verify）**：对比预期结果与实际状态，判断是否需要纠错或重试

跨应用任务时，Agent 可自主串联多个窗口和系统，形成端到端的任务链。

**评测基准**：OSWorld 是目前最权威的 GUI Agent 基准，测试 Agent 在真实操作系统环境中完成任务的成功率。Mano-P 1.0 以 58.2% 成功率位居 OSWorld 全球第一（专有模型榜）。

---

## 为什么重要

**解决自动化最后一公里**：传统企业有大量遗留系统没有 API，ERP、政务系统、财务软件等只能通过 GUI 操作。CUA 使这些场景也可以被 Agent 自动化。

**数据安全优势**：CUA 不需要将业务数据传输到云端做 API 解析，纯本地视觉处理，天然适配高合规要求场景（金融、医疗、政务）。

**降低接入门槛**：无需 API 对接或系统改造，任何有 GUI 的软件都可以直接成为 Agent 的操作对象，部署成本大幅降低。

**与 LLM Agent 的关系**：CUA 是 Agent 的"手"，负责执行层；LLM 是"脑"，负责理解和规划。Mano-P 的 Mano（灵巧手）+ Cito（专家脑）双模型架构体现了这一分工。

---

## Connections

- [[miaozhen/entities/mano-p|Mano-P 1.0]] — 明略科技基于此范式的产品，OSWorld全球第一
- [[miaozhen/concepts/deepminer-agent-architecture|DeepMiner多智能体架构]] — Mano 作为灵巧手模块集成于 DeepMiner
- [[miaozhen/sources/mano-p-intro-20260421|Mano-P产品介绍（2026）]] — 来源文件
