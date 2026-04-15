---
title: AI趋势研究白皮书 2026Q1（腾讯科技）
topic: ai-trends
type: source
created: 2026-04-15
tags: [ai-agent, harness-engineering, recursive-rd, skill, tencent, 2026q1]
---

# AI趋势研究白皮书 2026Q1

**出品**：腾讯科技 · **执笔**：博阳 · **发布**：2026年4月 · **页数**：60页

---

## 摘要

核心论点：2026 Q1 是 AI Agent 从"聊天工具"跃迁为"持续运行工作系统"的历史拐点。竞争焦点从"谁的模型更聪明"转向"谁能把 Agent 做成一套稳定运行的工作系统"。驱动这一转变的是四股力量的因果链——产品化倒逼系统升级，系统升级促成研发闭环，Skill 为全局提供知识落点，且四者恰好在同一季度同时撞线。

---

## 核心要点

### 1. 高自动化 Agent 开始主流化

**市场数据**（Q1关键指标）：
- OpenClaw：60天内从9K增至247K GitHub星，月活200万；深圳排队安装，市价炒至1000元；22%员工未经IT批准在工作中使用
- Anthropic Computer Use：OSWorld基准72.5%（= 人类水平72.4%），首次达到人类水平
- Cursor Agent：单任务最长执行36小时（从分钟级进入天级）
- 五种产品形态同时分叉（桌面助手/编码IDE/工作自动化/云端SaaS/消费助手）

**平台博弈**（定价权之战）：
- Google：大规模封禁通过OpenClaw调用Gemini的用户账户，理由是"恶意使用/计算负载异常"；深层原因是单个OpenClaw用户实际API消耗达1000-3600美元/月，远超250美元月费
- Anthropic：1月部署客户端指纹识别阻止OAuth绕行，2月将行为定性为"Token套利"，要求通过API密钥接入（价格为订阅制5-10倍）
- OpenAI：收购OpenClaw创始人，列入消费者计划白名单（收编而非封堵）

**中国市场**：
- "龙虾大战"：至少9家大厂推出桌面Agent（WorkBuddy/QClaw/ArkClaw/QoderWork/DuClaw/AutoClaw/Kimi Claw/MaxClaw/Agent 1.0等），切入角度各异（腾讯绑微信、字节绑飞书、阿里从编码扩通用、百度靠搜索降门槛）
- DeerFlow 1.0：字节开源"Super Agent Harness"，一月内22K→52K星，登顶GitHub Trending全球榜首
- 春节AI大战：字节+阿里+腾讯合计约90亿元营销，除夕日活总和2.4亿；豆包月活3.15亿（全球第二），千问月活2.03亿（增速553%）
- 编码Agent：字节Trae 600万全球开发者，腾讯CodeBuddy覆盖内部90%+工程师，阿里通义灵码40%内部代码AI生成

### 2. Harness Engineering 走向核心

**六层架构**（从底层到顶层）：指令基底 → 执行面 → 验证层 → 状态与记忆层 → 工作流层 → 治理层

**关键实践模式**（Q1三条路线）：

**接力赛架构**（Anthropic Justin Young博客）：
- 问题：任务超过20-30步时Agent会在第30步前后全局崩溃
- 方案：初始化Agent只负责搭环境并写交接清单（claude-progress.txt），然后退场；编码Agent每次上场先读清单，只做一个具体功能，做完更新清单提交代码，再退场
- 关键设计：Agent间不共享对话历史，只通过文件传递信息（对话历史膨胀会淹没有效信号）

**甲方乙方架构**（Anthropic Prithvi Rajasekaran博客）：
- 问题：Agent评价自己的工作时系统性打高分（"self-deception"，自我欺骗）
- 方案：Planner（项目经理，需求→规格书）+ Generator（乙方，按功能逐个实现，每次先签Sprint Contract）+ Evaluator（甲方，用真实浏览器测试，四维度评分，不达阈值必须返工）
- 关键发现：Evaluator必须使用功能性验证（真实测试），而非外观验证（查代码）

**仓库卫生学**（OpenAI三篇Harness博客）：
- 仓库即系统记录源：Agent通过读代码理解架构、读文档理解业务、读测试理解预期行为
- Doc gardening / anti-slop：没有定期维护机制，Agent使用的代码仓库约2-3个月后显著劣化

**收敛公约数**（Mitchell Hashimoto/Ghostty视角）：
- 核心观察：所有主流Harness不约而同地收敛到同一套基础结构，说明这些元素是"功能性必需品"而非设计偏好

**Harness成熟度光谱**：
- 已做好：指令基底（AGENTS.md等）、基础执行面（Shell/浏览器/文件/MCP）、基础验证、第一代工作流结构
- 进步中但未稳定：长时状态连续性、生产环境分层评测、多Agent协作
- 明显未解决：事务性控制（真正的rollback/compensation）、组织级治理、经济性框架、通用多Agent协议

### 3. 递归研发加速

**三组数字/三条路线**：

| 路线 | 代表 | 优化对象 | 关键成果 |
|------|------|---------|---------|
| 方法发现 | AlphaEvolve | 算法·解法·数学证明 | 0.7%全球算力回收，已生产运行1年；23%内核加速；Strassen矩阵乘法改进 |
| 工程系统优化 | OpenAI Codex + Karpathy Autoresearch | 代码质量·超参数·配置 | 一晚100个实验，已推广到ML之外 |
| 工具链自优化 | MiniMax M1 | 自身Harness·Skills·Memory | 100+轮自主迭代，内部评测提升30%，SWE-Pro 56.22%≈GPT-4o-Codex |

**Autoresearch架构**（630行Python，3个文件）：
- train.py：唯一允许Agent修改的文件（实验方案）
- prepare.py：不可修改的基础设施（数据准备/评估工具）
- program.md：人类写给Agent的指令（搜索方向/边界/停止条件）
- 棘轮机制：只保留比上次更好的结果，永不倒退
- 已延伸到ML之外：数据库查询优化（指标=延迟）、工单路由（指标=分类准确率）

**瓶颈转移**：Human in the loop的瓶颈从"人手不够快"变为"人脑不够快"——Agent在等人类告诉它"接下来优化什么"

**自进化Infra的5个组件**：可变/不可变资产分离 · 评估管线 · 记忆与选择机制 · 执行环境 · 动态工具与技能构建

### 4. Skill 成为 know-how 的落点

**本质定位**：Skill填的是"经验的空白"，不是"技术的空白"——公司特有的踩坑知识、行业审批规则、团队技术债务，不在训练数据里，也不适合硬编码进产品逻辑。Skill是比prompt更稳（结构化、可版本控制）、比workflow更活（模型可灵活运用）、比重新训练更轻的中间层。

**ClawHub生态**：半年内13,700+ Skills，单个Skill最高安装量18万；热门分层：生存层（Web浏览/Tavily搜索）→效率层（Telegram Bot/实时文档查询/Google Workspace）→进阶层（Docker沙盒/Secret扫描）；Capability Evolver（Agent自动识别重复模式并创建新Skill）

**供应链安全**：341个恶意Skill（占市场11.3%），36%含提示词注入；Clinejection事件：通过GitHub Issue标题触发提示词注入，在4000个开发者机器上安装了OpenClaw

**六条路线**：

| 路线 | 代表 | 实现方式 |
|------|------|---------|
| 能力市场型 | ClawHub | SKILL.md + 脚本 + 公共注册表，无审核门槛 |
| 开发者环境型 | GitHub Copilot / DeerFlow | 文件夹（指令+脚本+资源），兼容.claude/skills |
| 静态指令型 | AGENTS.md / CLAUDE.md | 压缩索引，每轮系统提示词注入，Vercel评测100%通过率 |
| 消费端型 | Perplexity Custom Skills | 用户"教会"系统，永久记忆，非开发者可用 |
| 跨平台型 | OpenAI Skills | 跨应用/CLI/IDE共享，Codex 300万WAU |
| 企业集成型 | 百度Comate / 腾讯云ADP | 接入企业已有环境和workflow |

**触发困境**：Vercel评测显示Agent主动调用Skill通过率仅53%，系统提示词注入通过率100%；DeerFlow解法：由编排层在任务规划阶段显式加载Skill，不靠Agent自主判断

**Skill吞噬SaaS论点**：当Skill能让Agent执行"用Salesforce管客户"的全部流程，用户不再需要SaaS界面；门槛极低（写Markdown）+可复利积累（半年13,700+）

---

## 引用

> "这四件事并不是散落在时间线上的独立新闻，而是环环相扣的因果链。产品化倒逼了系统升级，系统升级促成了研发闭环，而Skill则为这一切提供了知识落点。"

> "Skill填的就是这个缺口。Prompt解决的是'当下这次怎么说得更清楚'。Workflow是确定性的流程编排——稳定但僵硬。Skill在两者之间——比prompt更稳，比workflow更活，比重新训练模型更轻。"

> "当Agent能在研发循环里持续运行、持续改进，人类研究者的角色会从'亲手做实验'转向'设计实验框架、评估实验方向、审查Agent产出'。"

---

## Connections

- [[ai-trends/overview|AI趋势全景概览]] — 所属话题
- [[ai-trends/concepts/agent-mainstreaming|高自动化Agent主流化]] — 趋势一核心概念
- [[ai-trends/concepts/ai-harness-infrastructure|Harness基础设施]] — 趋势二（已有概念，本报告大幅补充）
- [[ai-trends/concepts/recursive-rd-acceleration|递归研发加速]] — 趋势三核心概念
- [[ai-trends/concepts/skill-knowledge-carrier|Skill知识载体]] — 趋势四核心概念
- [[ai-trends/entities/openclaw|OpenClaw]] — 趋势一的核心事件主体
