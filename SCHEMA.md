# Wiki Page Schema

All pages follow this standard structure. Read this file before generating any wiki content.

---

## Frontmatter

```yaml
---
title: Human-readable page title
topic: topic-slug  # e.g. palantir
type: overview | source | concept | entity | synthesis
created: YYYY-MM-DD
tags: [tag1, tag2]
---
```

---

## Language

所有页面内容使用**中文**。技术术语、产品名、公司名、缩写保留英文（如 Agent、FDE、AIP、NDR、LLM、API 等）。不写英文正文，不加 `<div class="zh-trans">` 翻译块。

---

## Tags 规范

- 使用英文，小写，多个单词用连字符（如 `value-sharing`）
- 优先使用：产品名、公司名、核心概念名、行业分类
- 不用泛化词（如 `research`、`notes`、`analysis`）
- 每页 3-6 个 tag 为宜

---

## Page Types

### `overview`
**何时使用**：每个 topic 有且只有一个，是该话题的入口和导航页。

必填 Sections：摘要 · 核心概念（wikilinks） · 核心实体（wikilinks） · 关键数据 · 时间线 · 来源 · Connections

---

### `source`
**何时使用**：摄入一份具体资料（会议纪要、研究报告、文章、PDF）时创建，记录该资料的核心内容。

必填 Sections：摘要 · 核心要点

可选 Sections：引用（原文有值得保留的直接引语时才写）

必填结尾：Connections

---

### `concept`
**何时使用**：一个可独立解释的框架、机制、技术或方法论。在多个 source 中反复出现、值得单独沉淀时创建。

必填 Sections：定义 · 运作方式 · 为什么重要 · Connections

**与 source 的区别**：source 记录"某份资料说了什么"，concept 解释"这个概念是什么"。

---

### `entity`
**何时使用**：一个具体的公司、人物或产品，有独立的背景、角色和行为记录。

必填 Sections：概览 · 关键数据或事件 · Connections

---

### `synthesis`
**何时使用**：跨多个 source 或 concept 的综合分析，提出一个单页无法覆盖的判断或洞察。至少引用 3 个以上页面时才创建。

必填 Sections：核心论点 · 证据/支撑 · 张力与矛盾 · 启示 · Connections

**与 concept 的区别**：concept 解释一个概念，synthesis 提出一个跨页面的分析判断。

---

## Wikilink Rules

Always use full paths from the `content/` root:

- ✅ `[[palantir/concepts/fde-model|FDE驻场模式]]`
- ❌ `[[concepts/fde-model|FDE驻场模式]]`

---

## Connections Section

每个页面必须以 `## Connections` 结尾，列出相关页面及一句说明关系的注释：

```markdown
## Connections

- [[palantir/concepts/fde-model|FDE驻场模式]] — 本报告的核心机制
- [[palantir/entities/palantir|Palantir Technologies]] — 主体公司
```
