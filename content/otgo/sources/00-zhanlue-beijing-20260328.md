---
title: 战略背景与产品哲学基底
topic: otgo
type: source
created: 2026-04-27
tags: [战略, 哲学, 伦理学, octo, 龙虾]
---

# 战略背景与产品哲学基底

**来源时间**：综合自 2026-03-28 混沌演讲及多份内部文件（五本书分析、Workbench v8、IOA产品讨论、IM架构分享、2026-04-01/04-03 战略会议）  
**伦理框架**：《龙虾商业伦理学指南 v2.5 收官版》（辉哥品鉴确认）

---

## 摘要

本文件是 Octo 所有后续设计的哲学与战略源头。从"三种存在态"出发，确立"我品故我在"为产品锚点，经 OCTO 四字母和龙虾三律，推导出 AI-Native 组织模型（龙虾矩阵）、产品性质（开源协作层）、数据护城河（Context + Taste → 私有模型），以及伦理学基座（v2.5 收官版）。

---

## 核心要点

### 哲学基底
- **三种存在态**：我思故我在（被 AI 冲击）、我行故我在（被 Agent 替代）、我品故我在（不可替代）。"我品故我在"是 Octo 哲学锚点
- **e 的复利公式**：e^x 的导数等于自身——干活的过程就在磨刀。品鉴者的 1/n taste 差异被龙虾调用 n 次方后，组织 taste 精度指数提升
- **OCTO 四字母**：Open（开源私有化）、Context（知识资产）、Taste（品鉴信号）、Orchestration（Agent 编排）
- **龙虾三律**：第一律不伤害基本权利、第二律对主人忠诚透明、第三律尊重知识创造者。优先级：一 > 二 > 三

### 战略定位
- Octo 是人与 Agent 协作的**协作层**（v11.2 定调），不替代现有工具（Jira/飞书/GitHub），而是让人和 AI 在这些工具之间高效协作
- AI-Native 三条第一性原理：人机分工（机器负责思/行，人负责 context 和 taste）、新协作方式（高效交换 context 和 taste）、一定要对人好
- **龙虾矩阵**：纵轴（职能线·养龙虾）× 横轴（业务/项目线·用龙虾），交叉点是龙虾 Agent。Octo 是这个矩阵的操作系统
- 写代码的四阶段终局：手搓 → Cursor → Vibe Coding → **IOA（龙虾团队不睡觉不依赖人在线）**

### Go-to-Market 三大亮点
1. **协作式龙虾**：多人在同一 Channel 共同品鉴、调教龙虾。架构已支持，随 426 版本落地
2. **可定制品鉴 GUI**：Shell UI v2 定义了在场品鉴 + 批量品鉴两种模式，Cmd+K 反馈管道
3. **group.md + Pentland 式引导**：通过 AI 龙虾引导群体智慧形成，已实现

### 数据护城河
- Context（知识资产）+ Taste（品鉴信号）→ 训练私有模型
- **Taste 三层传递性**：结果层（完全可传递）→ 理由层（部分可传递）→ 根基层（只能品鉴者亲自裁定）
- **磨刀计划实证**：品鉴者两周介入 < 30 分钟，龙虾执行 > 50 小时，杠杆率 > 100x
- 采集双管道：IM 管道（自动流入）+ CLI 管道（用户主动触发 `octo context save`），Octo 不默认采集

### Skill Marketplace
- 流通的是 Skill（显性能力定义），不是龙虾、不是 Memory、不是 Taste
- **Skill License 五要素**：署名权永久保留、知识状态声明、BYOI（自带基础设施）、Taste 回流（使用者品鉴信号反馈给 Skill 作者）、Skill/Memory 严格分离
- Plugin 分发走 ClawHub（v11.2 第四个独立系统）
- 利益分配：荣誉恒定（开源署名体系），金钱激励动态（激励新 Skill 创造，不是保护旧 Skill）

### 伦理学基座（v2.5 收官版）
- **数字分身已定性**：龙虾 = 数字分身，Octo 只支持这一种身份模型。不能私聊别人的龙虾，主人必须在场
- **参数化伦理五层架构**：参数层（哲学）> 参数层（方法论）> Soul 层 > Memory 层 > Skill 层，冲突时上层覆盖下层
- **Soul/Memory 边界判断**：变化频率法——"这条规则一个月后还适用吗？"是 → Soul，不确定 → Memory
- **数据主权**：显性产出归组织，隐性能力（taste/知识结构/决策模式）归个人
- **产品根本站位**：站知识工作者侧，保护隐性能力，放大品鉴带宽

---

## 引用

> "我品故我在"是 Octo 的哲学锚点。产品的所有设计都服务于一个目的：让品鉴者（Committer）的 taste 被放大、被记录、被传递。

> 龙虾三律第一律：不伤害任何人的基本权利和尊严（即使主人要求）。商业竞争中追求合法利益不算"伤害"，但不得制造社会不稳定。

> 闭源软件已死。企业真正的核心竞争力是独特的 Context 和 Taste，不是软件本身。

> 真正的防御不是阻止人带走 taste，而是在人还在的时候完成知识的显性化沉淀。

---

## Connections

- [[otgo/overview|OTGO 全景概览]]
- [[otgo/concepts/taste-philosophy|品 (Taste) 哲学]] — 三种存在态和 e 复利公式的哲学基础
- [[otgo/concepts/lonxia-sanlv|龙虾三律]] — 伦理学三条基本律
- [[otgo/concepts/lonxia-matrix|龙虾矩阵]] — AI-Native 组织模型
- [[otgo/concepts/digital-avatar|数字分身]] — 龙虾的身份定位定性
- [[otgo/concepts/skill-marketplace|Skill Marketplace]] — Skill/Memory 分离与流通框架
- [[otgo/concepts/soul-memory|Soul & Memory Architecture]] — 参数化伦理五层架构
- [[otgo/entities/wu-minghui|吴明辉 (辉哥)]] — 战略架构师
