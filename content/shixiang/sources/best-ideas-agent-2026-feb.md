---
title: 深度讨论高价值 Agent｜拾象 Best Ideas 精华总结
topic: shixiang
type: source
created: 2026-04-19
tags: [shixiang, agent, token, saas, openclaw, infra]
---

# 深度讨论高价值 Agent｜拾象 Best Ideas 精华总结

**来源类型**：社群讨论实录（19页 PDF）  
**时间**：2026年2月  
**出处**：拾象 Best Ideas 社群  

---

## 摘要

2026 年 2 月，一批高价值 Agent 产品（OpenClaw、Cowork、Claude in Excel）已在真实场景中展现出颠覆性效果。拾象 Best Ideas 社群围绕 Agent 的价值边界、Infra 机会、2026 年 Token 大爆炸、商业模式变化展开深度讨论，形成 7 个核心判断。

---

## 核心要点

### 1. 高价值 Agent 爆发：知识工作者是核心战场

- 今天高价值任务的主要承载者是**知识工作者**：coder、高级白领（Office 操作、前端建站、数据分析）
- 最受讨论的四款产品：**OpenClaw（Clawdbot）、Claude Code、Cowork、Claude in Excel**

**OpenClaw 三大巧思**：
1. **Long Horizon 持续运行**：部署在本地 Mac Mini 或云端 VM，7×24 小时不间断，从"召之即来"工具变成 Proactive Agent
2. **IM Gateway 嵌入日常流**：接入 Telegram/Slack/WhatsApp/飞书，实现"移动指挥，本地执行"（通勤路上发指令，家中电脑执行）
3. **预装 Claude Skills 生态**：类似早期智能手机预装 App 商店，降低使用门槛，这是 OpenClaw 最核心的 timing 巧思

**OpenClaw vs Manus**：
- Manus：中心化"交钥匙"体验，8000 台云端虚拟机，用户无法配置底层
- OpenClaw：去中心化、高度可配置，适应长尾需求，有效利用分散硬件
- 两者并非取代关系，Manus 积累了大量高价值场景数据（认知壁垒），可能反过来为 OpenClaw 类产品提供标准化服务

### 2. Cowork + Claude in Excel："10x 微软"市场

- Anthropic = "下一个微软"，Coding 能力领先打开 **10x 微软**市场
- Cowork 是 Claude Code 的自然延伸，依赖 Opus 4.5 能力飞跃（低 Token 消耗+高任务成功率），Coding 领域 AGI 事实上已达成
- **Excel 不是替代关系，而是正和博弈**：Agent 集成 Excel 会生产更多 Excel 文件；只要 Human-in-the-loop 存在，人就需要打开界面确认，Agent 无法脱离宿主
- 真正受冲击的是从 Excel 切分蛋糕的 SaaS 公司（如 Airtable），而非微软本身

### 3. 高价值 Agent 切分企业工资预算

- 订阅定价跃升：$20/月 → $200/月 → **$500/月（已出现）→ $1,000-2,000/月（酝酿中）**
- 收入来源根本转移：过去切营销/IT 预算 → 现在切**企业工资（劳动力）预算**
- 高价值 Agent 必须由行业专家主导，因为只有具备极深 Know-how 才能做好 Context Engineering 和评估 AI 产出质量

### 4. Token 消耗是衡量 AI-native 程度的核心指标

- 真正的 AI 原生 = 用大量 Token 解决复杂问题；用 UV/DAU 看业务说明仍在沿用旧逻辑
- Manus/Claude Code 单任务 Token 消耗是传统 Chat 的 **百倍甚至千倍**
- 已出现单用户 Token 日均消耗达 **billion 级别**的案例
- Token 与 Token 开始不等价：小参数模型（8B/30B）的 Token 价值快速逼近大模型；Cerebras 等专用芯片带来不同质的 Token

### 5. 2026 年 Token 用量至少 10x 增长

**三条 driver**：Long-horizon task、Proactive Agents、多模态

**开源模型"下限达标"是关键推力**：
- **GLM-4.7**：历史上首次真正在 Coding 和 Agentic 场景达到"可用下限"，带来"无感"使用体验
- **Kimi K2.5**：逻辑干练，已具备 Multi-Agent 并发处理能力
- 拐点意义：全球厂商不再依附于闭源巨头，可直接通过开源模型建立独立盈利闭环
- 制约瓶颈：硬件供应——预计 GPU 将再次进入"买不到"紧缺状态

### 6. 给 Agent 设计的 Infra 是刚需

现有互联网 Infra 对 Agent 处于"敌对"状态：
- Cloudflare 等防火墙频繁拦截 Agent，IP 被封锁
- 缺少专门为 Agent 设计的安全、审计、支付接口、浏览器环境
- Agent 执行 Long-horizon 任务时容易"断片"，人反而成了全流程最慢的环节

**两类 Infra 机会**：
- **Infra of Agent**：构建 Agent 的 Infra（如 Agent 专用浏览器 BrowserUse，显著节省 Token 并提升成功率）
- **Infra for Agent**：给 Agent 用的 Infra（专用网络、支付系统）

高阶需求：**主动对齐**——Agent 主动构建用户数字分身，理解隐性知识，而非每次靠用户写 Prompt 对齐

**CPU 回潮有限**：Agent 沙盒进入门槛低，云厂商定价无溢价，利润有限

### 7. SaaS 的终结？

**激进派（软件被吞噬）**：Agent 直接操作数据和 API，复杂 UI 和业务逻辑封装将失去意义；TapTap Creator 已出现（自然语言生成 3D 游戏）

**保守派（Software as Tools）**：
- Agent 产出具有概率性 = 工人
- 软件具有 100% 准确性 = 工具/机器
- 软件不会被替代，而会退化为底层工具/数据库，由 Agent 通过代码驱动
- 软件的未来壁垒在于 **Ontology（本体论）**：定义清楚企业内部组织逻辑、隐私边界和业务上下文（Palantir 路径）

### 8. Agent 真正泛化的三条路径

**路径 1：人群分层渗透**（三种平行产品形态）
1. 硬核程序员：Claude Code（高门槛、极致控制权、Terminal/CI 环境）
2. 知识工作者/白领：Manus（交钥匙体验，降低技术门槛）
3. 普通大众：OpenClaw 类 IM Bot（病毒传播，社交网络效应，类比 AOL/Facebook 早期）

**路径 2：Agent 是"电脑"还是"手机"？**
- 电脑派：Agent 革命是智能本身的变革（非分发渠道变革），需要用户跨越技术门槛，是精英向大众缓慢渗透的过程
- 手机派：必须像微信一样零门槛，等待 Google/Apple 在 OS 底层完成深度封装

**路径 3：屏幕只是过渡，具身机器人才是终局**
- 当前数字 Agent 是在为不完美的数字基建"填坑"（宝马跑在山路上）
- 主导讨论的是程序员和投资人，缺乏对几十亿普通劳动者（体力劳动）的同理心
- Agent 终极形态：进入物理世界，AI 从屏幕走出来解决真实的体力劳动问题

---

## 引用

> "Token 消耗量才是衡量 AI-native 程度的核心指标，如果还在用 UV 或日活看业务，说明还在沿用旧的逻辑。"

> "高价值 Agent 一定会切分企业工资（劳动力）预算，而不再是软件预算。"

> "今天的屏幕内 Agent 本质上只是一个不断变化的过渡性'壳'，Agent 的终局是进入物理世界。"

---

## Connections

- [[shixiang/overview|拾象AI洞察]] — 所属话题
- [[shixiang/concepts/proactive-agent|Proactive Agent]] — OpenClaw 的核心架构模式
- [[shixiang/concepts/token-as-metric|Token 消耗量作为 AI-native 指标]] — 本文最核心的判断之一
- [[shixiang/concepts/open-source-floor|开源模型下限达标]] — Token 爆炸的关键驱动力
- [[shixiang/concepts/agent-infra|Agent 专用 Infra]] — 当前最大的确定性机会
- [[shixiang/concepts/end-of-saas|SaaS 终结？]] — 两派观点的结构化对比
- [[shixiang/concepts/agent-generalization|Agent 泛化三条路径]] — 跨越鸿沟的战略思考
- [[nvidia-gtc-2026/concepts/agent-as-a-service|Agent-as-a-Service]] — GTC 2026 对 AaaS 的战略判断与本文呼应
- [[otgo/overview|OTGO]] — octo 是 AaaS/Agent 生态的具体落地方向
