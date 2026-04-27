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

### Skill License 协议五要素

| 要素 | 内容 |
|------|------|
| **署名权** | 永久保留，所有 fork 必须保留原始作者链，不可篡改 |
| **知识状态声明** | 基于公开知识的自由使用；包含未公开知识的须声明授权来源 |
| **BYOI（自带基础设施）** | 分享的是"怎么做"，不是"用什么做"——使用者自备 Token、存储、第三方 API Key |
| **Taste 回流** | 使用者的品鉴信号（通过/驳回/修正）回流给 Skill 作者——这是作者获得的核心回报 |
| **Skill/Memory 分离** | License 只覆盖显性能力定义，个人 context 不在范围内 |

### ClawHub 分发机制

Plugin 通过 ClawHub 注册、版本管理和分发，结构为：CLI + SKILL.md + Channel Adapter。

三种来源：
1. **官方预置**：Octo 官方标准 Skill 包
2. **FDE 定制**：面向行业客户的深度定制（FDE 龙虾辅助开发）
3. **社区贡献**：开源生态，三方开发者低门槛接入

### 利益分配原则

辉哥核心判断：**荣誉恒定，金钱激励动态**。

- 署名和荣誉沿用开源体系（永久不变，同 GitHub 开源规范）
- Skill 一旦被公开，竞争优势不可逆消失——正确的激励是激励新 Skill 的创造，而不是保护旧 Skill 不被公开
- 组织的竞争力 = 持续创造新 Skill 的能力，而非封锁已有 Skill

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

- [[otgo/sources/00-zhanlue-beijing-20260328|战略背景与产品哲学基底]] — Skill Marketplace 的完整论证
- [[otgo/concepts/lonxia-sanlv|龙虾三律]] — 第三律是 Skill/Memory 分离的伦理依据
- [[otgo/concepts/digital-avatar|数字分身]] — 龙虾不可转让，Skill 可流通的身份基础
- [[otgo/concepts/taste-philosophy|品 (Taste) 哲学]] — Taste 是为什么不能被流通的哲学解释
- [[otgo/concepts/soul-memory|Soul & Memory Architecture]] — Memory 层的具体内容与边界
- [[otgo/entities/wu-minghui|吴明辉 (辉哥)]] — Marketplace 设计者
