---
title: Ontology — 业务本体层
topic: palantir
type: concept
created: 2026-04-15
tags: [Palantir, Ontology, 语义建模, 基础设施]
---

# Ontology（业务本体层）

## 定义

Ontology 是 Palantir 平台的语义基础设施层：将客户的真实业务实体（设备、人员、订单、流程等）及其关系，统一建模为机器可理解的语义模型（"业务本体"）。它是 Foundry、Gotham 和 AIP 的共同底层，不单独对外销售。

---

## 运作方式

**核心作用**：
- 统一语义层：让不同系统、不同数据源使用"同一种语言"描述业务对象
- 业务建模：将工厂、供应链、情报目标等复杂业务场景抽象为可计算的语义图谱
- AI就绪：为 AIP 提供业务语义理解基础，使 AI 能直接操作业务对象而非原始数据

**与其他产品的关系**：
- Foundry + Ontology：商业企业的数据操作系统 + 业务语义层
- Gotham + Ontology：政府情报平台 + 情报目标建模层
- AIP + Ontology：企业AI平台 + 业务对象理解层

**交付方式**：嵌入式，包含在平台订阅费中，无单独定价

---

## 为什么重要

Ontology 是 Palantir 技术护城河的核心组成：

1. **替换成本**：Ontology 建模深度嵌入客户业务流程，一旦建立，替换 Palantir 相当于重建整个业务语义层
2. **技术锁定**：客户的 AI 应用（AIP）依赖 Ontology 理解业务，与 Palantir 平台深度耦合
3. **FDE专属技能**：Ontology 建模需要本体建模师（Delta团队专项），是 FDE 驻场不可替代性的来源之一

---

## Connections

- [[palantir/concepts/product-portfolio|五大产品矩阵]] — Ontology在矩阵中的位置
- [[palantir/concepts/fde-model|FDE驻场模式]] — Delta团队中的本体建模师
- [[palantir/overview|Palantir 全景概览]]
- [[palantir/sources/palantir-biz-model-research-20260113|商业模式研究]]
