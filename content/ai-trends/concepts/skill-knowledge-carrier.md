---
title: Skill作为know-how的落点
topic: ai-trends
type: concept
created: 2026-04-15
tags: [skill, know-how, clawhub, skill-marketplace, supply-chain-security, deerflow]
---

# Skill作为know-how的落点

## 定义

Skill是结构化的知识包——包含触发条件（什么场景下用）、标准操作流程（一步步怎么做）、可执行脚本（能直接跑的工具）和参考资料（背景知识）。它把"某个领域的know-how"从专家的直觉变成Agent可以读取和执行的格式。

Skill处于三者之间的中间层：
- 比**Prompt**更稳：结构化的、可版本控制的，而非即时性的一次性指令
- 比**Workflow**更活：模型可以根据当前情况灵活运用，而非确定性的硬编码流程
- 比**重新训练模型**更轻：改一个Markdown文件 vs 重新训练一个大模型

---

## 运作方式

### Skill填的是"经验的空白"，不是"技术的空白"

公司特有的踩坑知识不在训练数据里，也不适合硬编码进产品逻辑：
- "这个API在高并发场景下有个隐藏的rate limit"
- "这个框架的migration工具在v3.0之前有个bug，必须先手动改一个配置"
- "我们团队从来不用ORM的cascade delete，因为三年前出过一次事故"

Skill把这些经验打包成Agent可执行的格式——不是让Agent更聪明，是让它"更懂行"。

### 结构示例：Brainstorming Skill（obra/superpowers，100K+ GitHub星）

这个Skill解决"Agent收到模糊需求后立刻开始写代码、理解错了再推翻重来"的问题，在Agent和代码之间插入硬性门槛：**设计获得用户批准之前，严禁写任何代码**。

四类元素说明Skill与Workflow的本质区别：
- **任务**：定义"想清楚"包含哪些步骤（而非只是说"想清楚再做"）
- **流程**：9步执行清单（探索上下文→提澄清问题→提2-3种方案→分块展示→写设计文档→规格自审→用户审查→过渡到实施）
- **限制框架**：硬性门禁——不通过无法进入下一步（而非"建议"Agent可以忽略）
- **输出**：强制产生可追溯的文档（而非无物化产出的提示词）

Skill之间可以串联：Brainstorming → writing-plans → executing-plans → test-driven-development，整套框架是互相串联的Skill链。Workflow是组织架构，Skill是岗位手册。

### 六条路线并存

| 路线 | 代表 | 实现方式 | 特点 |
|------|------|---------|-----|
| 能力市场型 | ClawHub | SKILL.md + 脚本 + 公共注册表 | 开放，无审核门槛 |
| 开发者环境型 | GitHub Copilot / DeerFlow | 文件夹（指令+脚本+资源） | 兼容.claude/skills |
| 静态指令型 | AGENTS.md / CLAUDE.md | 压缩索引，系统提示词注入 | Vercel评测100%通过率 |
| 消费端型 | Perplexity Custom Skills | 用户"教会"系统，永久记忆 | 非开发者可用 |
| 跨平台型 | OpenAI Skills | 跨应用/CLI/IDE共享 | Codex 300万WAU |
| 企业集成型 | 百度Comate / 腾讯SkillHub | 接入企业已有环境+安全审核 | 生产-审核-分发闭环 |

### 触发困境

Vercel评测：Agent主动调用Skill通过率仅53%，系统提示词注入（AGENTS.md路线）通过率100%。意味着市场里再多好东西，Agent意识不到需要去查，就等于没有。

DeerFlow解法：由编排层在任务规划阶段显式加载Skill——不靠Agent自己搜，而是在拆任务时就决定加载什么Skill。本质上把触发问题从Agent的自主判断推回到Harness的工作流层。

### 长Skill的Harness问题

短Skill（"用2空格缩进"）几乎不会出错。但长程Skill（2000+字符，十几步）面临与早期Harness相同的问题：Agent跳步、不遵循、做到一半忘了前面的要求。M1在40个复杂Skill测试中97%遵循率——听起来不错，但10个步骤每步97%，整体成功率只剩74%。**Skill需要自己的Harness**（步骤拆分/进度追踪/中间验证/回退机制），但目前没有人在做这件事。

---

## 为什么重要

**"一次编写，无限复用"打破了经验传递的瓶颈**：一个资深工程师花两小时写完TDD Skill，全公司几千个Agent实例可以同时加载。以前junior工程师要花两年积累的领域经验，现在被打包成一个文件分发出去。知识从附着在"人"身上变为附着在"结构"上。

**ClawHub生态规模**：半年13,700+ Skills，单个Skill最高安装量18万，已形成层级生态（生存层→效率层→进阶层）。Capability Evolver（Agent自动识别重复模式并创建新Skill）赋予AI"自我进化"能力。

**Skill吞噬SaaS的逻辑**：当Skill能让Agent执行"用Salesforce管客户"的全部流程，用户不再需要SaaS界面。门槛极低（写Markdown）+ 可复利积累 + 迭代速度快几个数量级（改一行vs发版本）。MCP动摇的是接口层，微调动摇的是模型层，Skill动摇的是**流程层本身**。

**对人的影响**：执行层的know-how被Skill蒸馏完后，人退到判断层和决策层——但这不是"工作转型"，而是"工作总量的净减少"（组织里执行者需要一千个，决策者可能只需要十个）。更尖锐的是：写成Skill之后，Skill就不再需要你了。这个蒸馏过程是不可逆的。

---

## 当前局限与系统性风险

**供应链安全**（头号风险）：ClawHub上341个恶意Skill（11.3%），36%含提示词注入；Clinejection事件通过GitHub Issue标题触发提示词注入，在4000个开发者机器上安装OpenClaw。MCP生态60天内爆出30个CVE——48%存在路径遍历、38%缺乏认证。当Skill通过MCP调用外部工具时，两层风险叠加放大。

**跨平台互操作未解**：OpenClaw的SKILL.md、GitHub Copilot的Agent Skills、Anthropic的CLAUDE.md rules各有格式，一个Skill在OpenClaw里写好了，不能直接在Cursor或Copilot里用。

**触发机制脆弱**：53%的主动调用通过率意味着大量Skill价值被严重低估。

---

## Connections

- [[ai-trends/sources/tencent-ai-whitepaper-2026q1|腾讯AI白皮书2026Q1]] — 来源
- [[ai-trends/concepts/ai-harness-infrastructure|Harness基础设施]] — Skill是Harness指令基底层的核心载体；长Skill需要自己的Harness
- [[ai-trends/concepts/agent-mainstreaming|高自动化Agent主流化]] — Skill是支撑Agent持续稳定工作的知识底座
- [[ai-trends/concepts/recursive-rd-acceleration|递归研发加速]] — M1在自进化过程中自主构建Skills，Skill与递归研发深度交织
- [[tools/overview|工具方法论]] — LLM Wiki的Skill机制（/llm-wiki）是这一概念的直接实践
