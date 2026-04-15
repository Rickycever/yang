---
title: Harness基础设施（AI Harness Infrastructure）
topic: ai-trends
type: concept
created: 2026-04-15
tags: [harness, memory, context, observability, eval, invisible-failures]
---

# Harness基础设施（AI Harness Infrastructure）

## 定义

为AI模型提供"驾驭层"的基础设施——不是让模型更强，而是让模型的能力被可靠地驾驭和利用。核心包含两个子层：**记忆与上下文管理**，以及**评估与可观测性**。随着模型日益商品化，差异化正在转移到这一层。

---

## 运作方式

### 记忆与上下文管理

基础RAG解决了"模型能否访问数据"的问题，但复合AI系统（Compound AI Systems）需要更高层次的记忆基础设施：
- **跨会话上下文**：跨多次对话保持连贯的用户画像和任务状态
- **用户偏好记忆**：记住用户风格、决策模式、历史交互
- **组织知识接入**：将CRM记录、内部文档、专有数据实时融入模型响应

趋势：开发者曾经手写向量数据库和检索系统，现在这已成为独立的基础设施类别，以"即插即用"语义层的形式出现。

### 评估与可观测性（关键挑战）

传统监控的盲区：传统指标（完成率、延迟、错误码、点赞/踩）无法捕获对话AI的典型失效模式。

**78%的AI失效是不可见的**（来源：arxiv.org/abs/2603.15423）：

| 失效模式 | 描述 | 为什么监控不到 |
|---------|------|--------------|
| 信心陷阱 | AI自信地给出错误答案，用户接受 | 用户没有报错，仪表盘显示正常 |
| 漂移 | AI逐渐回答了不同于原始问题的问题 | 每个单独的回复看起来合理 |
| 静默失配 | AI误解请求，但输出足够似是而非，用户不反馈 | 无投诉信号，对话表面完整 |

关键洞察：即使换用更强的模型，93%的案例中这些模式依然存在。原因是**交互动态**（模型如何呈现输出、用户如何表达意图），而不是模型能力的缺口。

新兴解决方案：
- **Bigspin.ai**：生产环境实时监控，将模型输出与黄金数据集和用户反馈对比
- **Braintrust、Judgment Labs**：语义评估指标平台
- **LLM-as-a-judge**：用语言模型评估语言模型输出质量的技术范式

---

## 为什么重要

**商业影响**：一个对话AI在关键业务流程中悄悄失效（如合规审查、客户服务、财务分析），其损失可能远超系统停机，但不会触发任何告警。

**模型商品化的必然结果**：当基础模型能力趋于同质，差异化必然向上迁移——记住什么、可靠地执行什么、如何知道自己是否出了问题，这些成为真正的竞争力。

**对企业AI治理的意义**：EU AI Act要求高风险系统有持续监控和日志，Harness基础设施是满足合规要求的技术实现层。

---

---

## 补充：Harness Engineering实践模式（来自腾讯AI白皮书2026Q1）

2026 Q1，Harness Engineering从BVP所描述的基础设施概念进化为具体的工程实践。三条路线从不同痛点切入，但都在搭同一套东西：

### 接力赛架构（Anthropic）
- **问题**：任务超过20-30步时，Agent会在第30步前后全局崩溃——不是偶尔犯错，而是彻底丧失全局视野
- **方案**：初始化Agent负责搭环境并写claude-progress.txt（交接清单）后退场；编码Agent每次上场先读清单，只做一个具体功能，做完更新清单提交代码，再退场
- **关键设计**：Agent间只通过文件传递信息，不共享对话历史（对话历史会不断膨胀淹没有效信号）

### 甲方乙方架构（Anthropic）
- **问题**：Agent评价自己工作时系统性打高分（self-deception，自我欺骗）——结构性偏差而非偶然失误
- **方案**：Planner（规格书）+ Generator（每功能先签Sprint Contract）+ Evaluator（用真实浏览器测试，四维度评分，不达阈值必须返工）
- **关键发现**：Evaluator必须使用功能性验证，而非外观验证（查代码）

### 仓库卫生学（OpenAI）
- **仓库即系统记录源**：Agent通过读代码理解架构、读文档理解业务、读测试理解预期行为；代码库质量直接决定Agent工作质量
- **Doc gardening / anti-slop**：没有定期维护机制，Agent使用的代码仓库约2-3个月后显著劣化

### Harness成熟度光谱（2026 Q1评估）

| 状态 | 内容 |
|------|------|
| **已做好** | 指令基底（AGENTS.md等规则文件）、基础执行面（Shell/浏览器/文件/MCP）、基础验证、第一代工作流结构（Planner/Generator/Evaluator） |
| **进步中但未稳** | 长时状态连续性（跨天跨会话记忆）、生产环境分层评测、多Agent协作 |
| **明显未解决** | 事务性控制（真正的rollback/compensation/一致性保障）、组织级治理与审计、经济性框架（模型路由/预算分配）、通用多Agent协议 |

**总判断**：足以构成第一代稳定骨架，但不足以成为最终框架。

## Connections

- [[ai-trends/overview|AI趋势全景概览]] — 所属话题
- [[ai-trends/sources/bvp-ai-infra-roadmap-2026|BVP AI基础设施路线图]] — 来源（前沿1，基础定义）
- [[ai-trends/sources/tencent-ai-whitepaper-2026q1|腾讯AI白皮书2026Q1]] — 来源（趋势二，具体实践模式）
- [[ai-trends/concepts/dataops-agentops|DataOps+AgentOps]] — 可观测性与AgentOps在监控维度高度重叠
- [[ai-trends/concepts/agentic-ai-management|Agent管理]] — Harness基础设施是Agent管理的技术底座
- [[ai-trends/concepts/skill-knowledge-carrier|Skill知识载体]] — Skill是Harness指令基底层的核心载体
- [[palantir/concepts/ontology|Ontology]] — Palantir Ontology是企业级语义记忆层的一种实现形式
