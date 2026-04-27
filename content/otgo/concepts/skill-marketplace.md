---
title: Skill Marketplace & Skill/Memory 分离
topic: otgo
type: concept
created: 2026-04-27
tags: [Skill, Marketplace, ClawHub, 知识主权, 伦理学]
---

# Skill Marketplace & Skill/Memory 分离

## 定义

Skill Marketplace（龙虾 App Store）是 Octo 的长期能力分发生态。核心设计原则：**流通的是 Skill（显性能力定义），不是龙虾本身，更不是 Memory 或 Taste**。技术载体是 ClawHub（v11.2 第四个独立子系统）。

---

## 运作方式

### Skill / Memory / Taste 三分法

| 概念 | 能否流通 | 归属 | 说明 |
|------|---------|------|------|
| **Skill（显性能力）** | 可以 | 创建场景决定：组织数据开发→归组织；个人方法论→归个人 | "怎么做"——可 fork、可共享 |
| **Memory（个人 context）** | 不可以 | 归品鉴者个人 | 项目记忆、对话历史，不随 Skill 流通 |
| **Taste（品鉴模式）** | 不可以 | 归品鉴者个人 | 暗默知识最高保护级别，不可提取 |

**核心原则**：把"归属"放在人身上，把"流通"放在 Skill 上。Taste 跟人走，不跟龙虾走——龙虾换了一只，用户的 Taste 积累不散。

### Skill License v1.1 七要素

| 要素 | 内容 |
|------|------|
| **1. 署名权** | 永久保留，所有 fork 必须保留原始作者链，不可篡改；衍生作品须注明原始来源 |
| **2. 知识状态声明** | Skill 必须声明知识来源状态：公开知识→自由使用；含未公开组织知识→须声明组织授权；含个人暗默知识→须声明本人授权 |
| **3. 授权机制** | 将他人未公开知识/行为模式 Skill 化必须获得相应授权；公开知识无需授权（署名权仍须保留）；退出权：原始知识贡献者可要求停止使用其未公开贡献 |
| **4. 资源隔离（BYOI）** | 使用者自备 Token 账号、存储、第三方 API Key；Skill 作者的资源不被消耗 |
| **5. Taste 回流** | 使用者的品鉴信号（yes/no/修正）回流给 Skill 作者——这是作者获得的核心回报，不是钱，是 taste |
| **6. 改进共享** | GPL 式或 MIT 式选择，但署名权不可去掉 |
| **7. Skill/Memory 分离** | License 只覆盖显性能力定义；Memory 打包进 Skill 需额外明确授权 |

**双线署名（v2 新增）**：两人共创 Skill 时，署名权同时追踪两条线——代码贡献线（Git diff 可分析）+ 品鉴贡献线（谁做了关键 yes/no 判断，记录在品鉴日志中）。两线独立追踪，综合评估贡献度。

**Taste 回流质量加权（v2 新增）**：不是所有品鉴者的信号等权重。高质量品鉴者（历史品鉴深度高、信号与最终效果相关性强）的回流权重更高；Skill 作者有权筛选和过滤回流的 taste。

### ClawHub 分发机制

Plugin 通过 ClawHub 注册、版本管理和分发，结构为：CLI + SKILL.md + Channel Adapter。

三种来源：
1. **官方预置**：Octo 官方标准 Skill 包
2. **FDE 定制**：面向行业客户的深度定制（FDE 龙虾辅助开发）
3. **社区贡献**：开源生态，三方开发者低门槛接入

### Skill 利益生命周期模型（v2.2）

辉哥核心判断：**荣誉恒定，利益随 Skill 走不跟人走**。

**荣誉轨（恒定）**：署名权永久保留，贡献溯源链不可篡改，声誉系统持续累积。

**利益轨（动态）**：Skill 一旦被公开，竞争优势**不可逆**消失——不是临时波动，是单向不可逆的阶梯式下降。原来设想的"回调机制"不成立（v2.2 修正）：

```
Skill A（张三创造）
  独有期 -> 慷慨分配给张三
  被公开/复制 -> 利益永久下降（不可逆）
  -> 张三署名权永久保留（荣誉轨不变）
  -> 张三从 Skill A 获得的经济回报自然递减

Skill B（李四创造）
  独有期 -> 开启新的利益周期
  -> 张三若参与了 Skill B 的品鉴 -> 按品鉴贡献获得回报
```

- 激励对象随 Skill 更新而更新——激励新 Skill 创造者，不是保护旧 Skill 不被公开
- 组织竞争力 = 持续创造新 Skill 的能力，不是封锁已有 Skill
- Skill 生命周期判定一旦为"已公开期"，利益下调不可逆（季度评估，透明标准）

---

## 为什么重要

### 解决知识流通的伦理困境

传统软件知识产权模式（"闭源=壁垒"）在 AI 时代失效——辉哥判断"闭源软件已死"。新的壁垒来自 Context 和 Taste，而非软件代码本身。

Skill Marketplace 建立在这个判断之上：公开 Skill，但保护 Taste。竞争优势来自持续创造新 Skill 的能力（组织的 taste + 团队的速度），而非把旧 Skill 锁起来。

### Taste 回流作为核心激励

Skill 作者的核心回报不是金钱分成，而是使用者的品鉴信号（哪里通过了、哪里被驳回了、为什么）。这些 Taste 回流数据帮助 Skill 作者校准自己的能力，也是 Skill 进化的燃料——与龙虾三律第三律中"尊重知识创造者"的精神一致。

### 判断合作还是竞争的标准

知识主权是 Octo 与外部工具合作/竞争的判断标准：
- 对方开放了 CLI/API → 可合作（龙虾操作该工具是正当的）
- 对方锁定数据不开放接口 → 竞争关系（侵害组织知识主权）

---

## Connections

- [[otgo/sources/00-zhanlue-beijing-20260328|战略背景与产品哲学基底]] — Skill Marketplace 的来源之一
- [[otgo/sources/lobster-ethics-v2.5-20260405|龙虾商业伦理学指南 v2.5]] — Skill License v1.1 七要素、双线署名、Skill 利益生命周期的完整论证
- [[otgo/concepts/lonxia-sanlv|龙虾三律]] — 第三律是 Skill/Memory 分离的伦理依据
- [[otgo/concepts/duty-hierarchy|义务分层框架]] — 知识主权原则（合作/竞争判断标准）
- [[otgo/concepts/digital-avatar|数字分身]] — 龙虾不可转让，Skill 可流通的身份基础
- [[otgo/concepts/taste-philosophy|品 (Taste) 哲学]] — Taste 是为什么不能被流通的哲学解释
- [[otgo/concepts/soul-memory|Soul & Memory Architecture]] — Memory 层的具体内容与边界
- [[otgo/entities/wu-minghui|吴明辉 (辉哥)]] — Marketplace 设计者
