---
title: File Space — 用户 Context 与 Taste 载体
topic: otgo
type: concept
created: 2026-04-27
tags: [File-Space, Context, Taste, 数据主权, 品鉴]
---

# File Space — 用户 Context 与 Taste 载体

## 定义

File Space 是每个 Octo 用户的个人知识与品鉴空间——**"我品故我在"的物理载体**。它存储用户与 Agent 协作过程中积累的所有 Context 和 Taste 信号，并以用户主权为原则：**Context 默认私有，分享是用户的自由选择**。

---

## 运作方式

### File Space 里存什么

| 内容 | 来源 | 价值 |
|------|------|------|
| **品鉴记录** | 品鉴操作栏、Cmd+K、IM 反馈 | Taste 信号——训练龙虾和私有模型的核心数据 |
| **过程信息** | 龙虾的编排决策 + CC 的 CLI 命令序列 + 用户的品鉴反馈 | 完整还原"用户如何指挥 Agent、Agent 如何干活、结果如何被品鉴"的全链路 |
| **源文件快照** | 被品鉴的 Artifact 的快照（来自各子系统） | 品鉴记录必须有主体上下文——"驳回了第三章"必须附带"第三章是什么" |
| **Taste 画像** | 系统从品鉴者的显性操作中提炼 | 用户的偏好总结，龙虾用来对齐品味 |

### 用户 File Space vs 龙虾 File Space

**这是两码事。**

| | 用户 File Space | 龙虾 File Space |
|---|----------------|----------------|
| **定位** | 品鉴者的 Taste 的家 | 龙虾的虚拟机工作目录 |
| **内容** | 品鉴记录、Taste 画像、Context 积累 | 干活的临时文件、工具依赖、Knowhow |
| **归属** | 永远属于用户，换了几只龙虾也不散 | 属于该龙虾实例 |

龙虾"来拜读"用户的 Taste 画像，在自己的工作目录里干活。Taste 跟用户走，不跟龙虾走。

### 两条采集管道

**IM 管道（自动流入）**：用户在 IM 中的指令、品鉴操作（通过/驳回/批注）、龙虾汇报——随对话自然产生，无需额外操作。

**CLI 管道（主动触发）**：用户或 Agent 主动调用：
- `octo context save` — 保存知识 checkpoint 和过程信息
- `octo monitor report` — 上报 Agent 工作状态

**Octo 不默认监控用户环境。** 不在 Agent 机器上装探针，过程信息靠 Agent 主动推送。

### 主体上下文原则

品鉴总是发生在一个具体的 Artifact 上。无论 Artifact 活在哪个子系统（Overleaf、飞书、妙啊），都要把快照拿回来，让品鉴记录和被品鉴的内容永远在一起——否则品鉴记录失去了 Context，Taste 学习就会失真。

### Context 的分享层级

| 选项 | 可见范围 |
|------|---------|
| 私有（默认） | 仅用户本人和自己的龙虾 |
| 团队分享 | 做知识原子化后同步给同事——可引用和学习 |
| 训练龙虾 | 作为 Taste 信号对齐龙虾偏好 |

### 知识灰区保守默认值

当龙虾接触过某领域的未公开知识后，该领域的所有推理产出默认视为"未公开"，需标注知识状态。龙虾不得将"未公开"的 Context 用于该领域之外的场景，除非品鉴者明确授权分享（伦理学 v2.5 §22B）。

---

## 为什么重要

### 飞轮的物理载体

File Space 是 Octo 正反馈飞轮的存储介质：**用得越多 → Context 越厚 → AI 反馈越准 → 品鉴越高效**。没有 File Space，飞轮就无法积累。

### 数据主权的具体实现

与飞书/企微"所有工作数据归组织"不同，Octo 的 File Space 将 Taste 画像存在**个人**名下：
- 个人的品鉴模式（Taste）属个人，可选择是否贡献给组织
- 组织的显性产出（代码/文档）属组织
- 这是"站知识工作者侧"战略定位的数据架构落地

---

## Connections

- [[otgo/sources/dual-native-design-v1.5-20260404|Dual-Native Design v1.5]] — File Space 设计的完整来源文档
- [[otgo/concepts/taste-philosophy|品 (Taste) 哲学]] — 为什么 Taste 必须住在用户空间
- [[otgo/concepts/dual-native|Dual-Native Design]] — File Space 是 Dual-Native 飞轮的物理载体
- [[otgo/concepts/lonxia-sanlv|龙虾三律]] — 第三律：暗默知识最高保护，File Space 的伦理约束
- [[otgo/sources/00-zhanlue-beijing-20260328|战略背景与产品哲学基底]] — 数据主权（显性归组织，隐性归个人）的哲学来源
