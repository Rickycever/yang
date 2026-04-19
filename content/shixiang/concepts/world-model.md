---
title: World Model — 数字大脑与物理世界的 Interface
topic: shixiang
type: concept
created: 2026-04-19
tags: [world-model, multimodal, robotics, video-generation, spatial-intelligence]
---

# World Model — 数字大脑与物理世界的 Interface

## 定义

World Model 是对时间与空间的深度理解——不只是生成视频，更能根据当前状态与动作，模拟并预测未来的世界演化。拾象判断：2026年将是多模态的大年，World Model 是连接数字大脑与物理世界的核心 Interface。

## 运作方式

**技术背景：Omni-in, Omni-out**
- Google 和 OpenAI 技术路径已收敛：视觉、音频、文本被统一 Token 化，纳入同一个自回归序列建模
- 模型开始有了"通感"：语言模型 Scaling 中的自回归和 RL 都已在多模态中得到复用

**两大技术流派**：

**路线A：实时交互派（Real-time Interactive）**
- 关注低延迟（<100ms）与可玩性
- 目标：取代 Unity/Unreal，从"3D 渲染"转向"神经推理"
- 落地场景：Video-native games、虚拟人、XR
- 代表：Decart（估值$500M+，AI版Minecraft引擎）、Odyssey（好莱坞级高保真重建）、Genie 3（Google DeepMind，最强多模态，可交互3D环境）

**路线B：物理仿真派（Physics & Spatial）**
- 关注物理准确性（Physical Accuracy）与3D一致性
- 目标：成为 AI 的"训练场"
- 落地场景：机器人导航训练、自动驾驶极端场景模拟（Sim-to-Real）
- 代表：World Labs（李飞飞团队，LWM从2D视频学隐式3D结构）、General Intuition（用游戏数据训练Agent直觉）、NVIDIA Cosmos（平台型，内置物理引擎 Guardrails）

**机器人的关键数据问题**：
- Generalist：27万条真实机器人交互数据，称发现了 scaling law
- Sunday：改造 Umi，用手套低成本收集千万条众包家庭数据
- Physical Intelligence (π)：每周更新数据收集 Pipeline，在真实 Airbnb 环境内持续收集数据
- 世界模型和 YouTube 数据即将成为重要数据来源

## 为什么重要

1. **机器人训练的核心解法**：World Model 解决了现实数据不足的问题，机器人可以在"合成世界"中训练
2. **Multimodal Agent 的能力跃升**：Agent 具备了"看懂 UI、读懂屏幕"的能力，为接管人类繁琐操作铺平道路
3. **潜在娱乐/游戏 upside**：Video-native games 是新一代娱乐形态
4. **2026年是多模态大年**：多模态进步让有能力的团队都可以有自己的 bet，机器人一上来就分化

## Connections

- [[shixiang/sources/shixiang-lp-meeting-dec-2025|拾象 LP Meeting Dec 2025]] — 本概念的主要来源
- [[shixiang/concepts/continual-learning|Continual Learning]] — World Model 数据是 Continual Learning 的来源之一
- [[shixiang/overview|拾象AI洞察 全景概览]] — 所属话题入口
