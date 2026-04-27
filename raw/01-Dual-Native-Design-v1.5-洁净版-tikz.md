---
header-includes:
  - \usepackage{tikz}
  - \usetikzlibrary{positioning,arrows.meta,calc,fit,backgrounds}
---

# Dual-Native Design：GUI 设计方案（v1.5 洁净版）

> 日期：2026-04-04（0405 伦理学对齐 + 2026-04-20 v11.2 对齐）
> 定位：Octo 的 GUI 怎么做——面向产研团队的设计蓝图
> v1.4 → v1.5 核心变化（0403 会议后）：龙虾定性为数字分身；通用组件重分类为一方子系统（符合 v11 架构）；数据采集改为 IM+CLI 双管道（用户主动上报）；数据归属框架（显性归组织、隐性归个人）
> 0405 更新：根据《龙虾商业伦理学指南 v2.2→v2.5》补充 Taste 画像授权边界、品鉴操作不可逆性、子系统接入知识主权原则、参数化伦理五层架构、知识灰区保守默认值
>
> **2026-04-20 v11.2 对齐更新**
>
> 本文档原有 Dual-Native 核心论证（底层为 Agent 而建，表层为人而渲染、CLI 解耦 View/CRUD、独立子系统）完全保留。与 v11.2 架构的对齐点：
>
> 1. **2.4 三端策略 → 四端**：补充 Browser Extension 作为第四个端（协作桥梁）——见 §2.4 更新
> 2. **子系统接入**：原"iframe 嵌入 + SDK 注入"路径收敛为 **"Thread 富 Artifact 卡片 → 新标签页 + Browser Extension 桥接"**——iframe 仅保留给 Octo 原生内容（md/code/image/PDF）
> 3. **Monitor 定位**：原 §5.1 列为"一方子系统"，现对齐为 **"Monitor CLI 系统（用户/Agent 授意下主动上报）"**（见 04-Monitor 对齐说明）
> 4. **ClawHub**：v11.2 新增的 Plugin 分发中心，子系统 SKILL.md 通过 ClawHub 注册/分发

---

## 零、战略背景

### Octo 是什么

**Octo 是一个人与 AI Agent（龙虾）协作的操作系统。** 不只是 IM，不只是 Agent 管理工具——是让人和龙虾高效 co-work 的工作平台。

OCTO 四字母：Open（开源开放）+ Context（知识上下文）+ Taste（品鉴信号）+ Orchestration（龙虾编排）。

### 龙虾矩阵

```{=latex}
\begin{center}
\begin{tikzpicture}[
  lobster/.style={circle, draw=orange!70!black, fill=orange!15, minimum size=7mm, inner sep=0pt, font=\footnotesize},
  flabel/.style={font=\small, align=center},
  plabel/.style={font=\small, anchor=east}
]
% 职能列标题
\foreach \i/\name in {1/职能1, 2/职能2, 3/职能3, 4/职能4, 5/职能5} {
  \node[flabel] at (\i*2.2, 1.5) {\name};
  \node[font=\tiny, text=gray] at (\i*2.2, 0.9) {(养龙虾)};
}
% 项目行
\foreach \j/\pname in {0/项目A, 1/项目B} {
  \node[plabel] at (0.8, -\j*1.6) {\pname};
  \draw[gray!40, thick, dashed] (1.2, -\j*1.6) -- (11.8, -\j*1.6);
  \foreach \i in {1,...,5} {
    \node[lobster] at (\i*2.2, -\j*1.6) {o};
  }
}
% 纵轴虚线
\foreach \i in {1,...,5} {
  \draw[gray!25, thin] (\i*2.2, 0.5) -- (\i*2.2, -2.0);
}
% 图注
\node[font=\scriptsize, text=gray!70, anchor=west] at (1, -3.0) {%
  $[o]$ = 龙虾\quad 纵轴养龙虾（定义标准）\quad 横轴用龙虾（推项目）};
\end{tikzpicture}
\end{center}
```

Octo 就是跑这个矩阵的操作系统。拉群 = 组项目，写 group.md = 下 brief，龙虾在群里干活。

### 数据护城河

品鉴行为（通过/驳回/批注/选方案/Cmd+K 反馈）通过 IM 管道自动采集；Agent 工作过程和知识 checkpoint 通过 CLI 管道由用户/Agent 主动上报（`octo context save` / `octo monitor report`）。**Octo 不默认监控用户环境，用户选择 share 什么。**

数据归属：显性产出（代码/文档）归组织，隐性能力（知识结构/品鉴逻辑/taste）归个人。长期目标：帮客户基于组织显性产出训出私有模型，但不蒸馏个人隐性 taste。

### 两个关键判断

**判断一：未来所有主流软件都会 Agentic 化。** 飞书已有 CLI，Google Workspace 有完整 API，Overleaf 等开源工具天然可 CLI。这个趋势不可逆——Agent 通过 CLI 操作一切，是未来的标准工作模式。Octo 的架构必须顺应这个趋势。

**判断二：Octo 不能以 IM 为轴。** 如果以 IM 为核心，我们打不过企微和飞书——他们的本质就是 IM，客户群比我们大得多。我们要找的是他们做不了的事：**让他们抛弃"以 IM 为轴"的思路，他们做不到；但这个路径恰好更适合 Agentic Working 的新时代。** 这就是 Octo 的机会。

### Octo 的工作全景

一个典型的工作循环，从指令到积累，展示 Octo 各层如何串联：

**第一步：在 IM 中给方向。** 用户在群聊中对龙虾说"帮我改论文第三章，论证太弱了"。龙虾理解意图后拆解为子任务。

**第二步：龙虾调度 CC 并行执行。** 龙虾派出多个 CC 实例同时干活——CC-01 改论证结构、CC-02 搜文献补数据、CC-03 更新参考文献。每个 CC 通过 CLI 操作对应的子系统（Overleaf、文献数据库等）。用户在活动态势面板中可以看到整个调度过程，也可以像"监控室"一样切入任意一个 CC 的实时 Terminal，观察它具体在做什么。并行是提效的核心——多个 CC 同时工作，品鉴者只需在关键节点介入。

**第三步：品鉴产出。** CC 执行完毕，龙虾在 IM 中汇报"改好了，你看看"。用户在 Workspace 中打开子系统 Viewer（Overleaf 的 Web 界面），看到修改后的论文。用 Cmd+K 选中不满意的段落给出反馈，或在品鉴操作栏点"通过"。

**第四步：过程和结果回流到 File Space。** 两类信号流入用户的 File Space：(1) IM 管道自动采集——品鉴操作、对话指令、龙虾汇报；(2) CLI 管道主动上报——龙虾/CC 调用 `octo context save` 保存过程信息（编排决策、CLI 命令序列）和结果快照。这些成为用户的个人 Context。

**第五步：Context 积累 -> 分享是用户的自由。** 用户的 File Space 中 Context 越积越厚。用户可以选择：留着自己用（私有），做知识原子化后同步给同事（分享），或作为 Taste 信号训练龙虾偏好（训练）。分享是自由选择，不是默认公开。

**第六步：Context 驱动实时智能。** 当 Context 积累到足够厚度，它不只是存储——它变成实时的"第二大脑"。例如在会议场景中：智能硬件做实时录音和语音识别，语义理解后连接到每个参会者的 Context，AI 可以实时给出反馈——"这个方案和上周你驳回的那个相似度很高"、"辉哥提到的数据和上次的分析有出入"。Context 越厚，实时反馈越精准。

**这是一个正反馈飞轮**：用得越多 -> Context 越厚 -> AI 反馈越准 -> 品鉴越高效 -> 产出越好 -> 积累更多好 Context -> 循环。

---

## 一、核心理念

### 1.1 Dual-Native：让人和 Agent 更高效地协作

传统产品只需回答一个问题：**对人好不好？**

Octo 必须同时回答两个：**对人好不好？对 Agent 好不好？**

Dual-Native Design 不是折中，而是让同一套底层同时对两者达到各自的"原生体验"：**底层为 Agent 而建，表层为人而渲染。两者从不妥协，各自极致。** 目的是让人和 Agent 更高效地 co-work。

每个设计决策同时通过三道检验：
1. 人好不好用？
2. Agent 好不好接？
3. 两者协作是否更高效？

### 1.2 为什么 Octo 不能只有 IM

Octo = IM（协调通道）+ Workspace（工作台）。两者都有 GUI，但承担完全不同的职责。

IM 适合协调，不适合干活。没有人在微信群里写代码、排版论文或审核表格。群里说"帮我改一下第三章"，然后各自打开专业工具干活，干完了回群里说"好了你看看"。

| 工作类型 | IM 的局限 | 需要什么 |
|---------|---------|---------|
| 深度阅读/审核 | 对话流是线性的，无法空间化地呈现一篇文档 | 文档渲染视图（PDF / 表格 / 代码） |
| 精确反馈 | "第三段那个公式不对"——在 IM 里描述位置很痛苦 | 在渲染视图上直接指（选中 + Cmd+K） |
| 批量处理 | 20 个待审产出物，在 IM 里一个个问效率极低 | 品鉴队列 + 批量操作 |
| 全局监控 | "现在 5 个 Agent 各自在干什么"——IM 是串行的 | 活动态势面板 |
| 结构化操作 | 双击改单元格、拖拽排序——IM 无法承载 | 专用组件 |

**IM 是协调通道，Workspace 是工作台。** 两者互补，不互替。Octo 的 GUI 围绕这个分工展开——IM 负责对齐意图和汇报结果，Workspace 负责品鉴、编辑和监控。

---

## 二、产品形态

### 2.1 四种 Artifact

Octo 中流通的产出物（Artifact）分四种模态。Agent 侧的读写方式与产品形态无关——无论 GUI 怎么做，Agent 都直接操作文件：

| Artifact 类型 | Agent 的存储/读写格式 | 说明 |
|-------------|-------------------|------|
| **文本文档** | .md 或云文档本身 | 模型直接理解后输出 |
| **表格/结构化数据** | .xlsx/.csv/JSON | Agent 直接读写 |
| **图片/视觉内容** | 图片文件 + 生成参数 | Agent 多模态理解 |
| **代码** | 源代码文件本身 | Agent 直接读写 |

\newpage

### 2.2 混合平台 + CLI 解耦

Octo 是混合平台产品：Web（当前主力）+ iOS + Android，预留 macOS/Windows 桌面客户端。

传统的混合平台工程量"中重"——因为需要在每个端上自建 Viewer 和编辑器。**但 CLI 解耦让 Octo 不需要自建这些重型组件。**

#### View 和 CRUD 是独立解耦的两件事

- **CRUD**（龙虾干的活）：龙虾控制 CC，CC 通过 CLI 操作工具——修改文件、调用 API、执行命令
- **View**（人看的）：工具自身的 Web 界面负责渲染，Octo 只需一个浏览器容器指向它，实时刷新

```{=latex}
\begin{center}
\begin{tikzpicture}[
  box/.style={draw, rounded corners=3pt, fill=#1, minimum width=3.8cm, minimum height=8mm, font=\small, align=center},
  box/.default={blue!5},
  arr/.style={-{Stealth[length=3mm]}, thick, gray!50}
]
% 左列：View
\node[box=blue!10] (view) at (0, 3) {View（人看的）};
\node[box] (browser) at (0, 1.5) {浏览器容器};
\node[box] (webui) at (0, 0) {指向工具的 Web 界面\\[-1pt]{\scriptsize 实时刷新渲染结果}};
% 右列：CRUD
\node[box=orange!10] (crud) at (7, 3) {CRUD（龙虾干的）};
\node[box] (cc) at (7, 1.5) {CC 实例};
\node[box] (cli) at (7, 0) {通过 CLI 操作工具\\[-1pt]{\scriptsize 修改文件/状态}};
% 箭头
\draw[arr] (view) -- (browser);
\draw[arr] (browser) -- (webui);
\draw[arr] (crud) -- (cc);
\draw[arr] (cc) -- (cli);
% 底部连线
\draw[thick, dashed, gray!35] (webui.south) -- ++(0,-0.7) -- ++(7,0) -- (cli.south);
\node[font=\footnotesize, text=gray] at (3.5, -1.2) {独立解耦，互不依赖};
\end{tikzpicture}
\end{center}
```

**和 Claude Code + VS Code 同一个模式。** CC 在终端改代码（CRUD），VS Code 实时刷新（View）。两者互不依赖。

**这意味着**：
- Octo 不建文档编辑器（CRUD 交给 CLI）
- Octo 不建渲染器（View 交给工具自身的 Web 界面 + 浏览器容器）
- Octo 只做两件事：**编排**（龙虾 -> CC -> CLI 调度）和**品鉴**（Cmd+K、品鉴操作栏、Context/Taste 采集）

### 2.3 独立子系统，不做小程序

大厂不会按我们标准写东西。我们主动兼容别人——子系统是独立的 Web App，通过 Octo SDK 接入。

- Link Everything——能快速兼容任何有 Web 界面 / CLI 的工具
- 不限制子系统的技术栈和 UI 设计
- 子系统可以独立存在，不依赖 Octo

### 2.4 四端策略（v11.2 对齐）

**四个端是完全不同的产品形态，不是缩放关系。**

| 端 | 形态 | 定位 | 核心体验 |
|----|------|------|---------|
| **Web** | Web App | IM 主场 + 全功能 | 完整界面（Channel/Thread 导航 + 对话 + 原生预览） |
| **iOS** | Native App | 零碎时间——看摘要、快速拍板、给反馈 | 通知 + Decision Queue + 轻量 IM 回复 |
| **Android** | Native App | 同上 | 通知 + Decision Queue + 轻量 IM 回复 |
| **Browser Extension** | 浏览器插件 | 协作桥梁 | 在任意 Web 工具旁注入 Chat 侧边栏 + Cmd+K + 引用到 Chat |

移动端不做子系统嵌入、不做知识图谱、不做复杂品鉴——只做审批和追踪。**通知是移动端最重要的产品。**

Browser Extension 是 v11.2 确立的第四端——它不是独立 App，而是"把 Octo 的协作能力注入到用户正在使用的任何 Web 工具旁边"。详见 07-Shell 形态讨论记录 + PRD-CmdK-品鉴反馈器。

### 2.5 统一的反馈手势：Cmd+K

无论在哪个端、哪个子系统，品鉴反馈的交互模式统一：**指哪 + 说啥。**

Cmd+K = 选中内容后唤起输入框（打字/语音）。

| Artifact | 怎么"指" | "说"什么 | Agent 怎么做 |
|---------|---------|---------|------------|
| 文本 PDF | 选中文字或区域框选 | "这段逻辑不通顺" | 改源文件 -> 重出 PDF |
| 表格 | 选中单元格/行/列 | "这几个数对不上" | 溯源排查 |
| 图片 | 看着图（精确时裁剪区域） | "左上角图标颜色不对" | 看着图理解并执行 |
| 代码 | 选中代码段 | "这个循环会死循环" | 找到位置改代码 |
| 任何 | 不指 | "整体感觉不对" / "通过" | 全局理解 / 全局操作 |

### 2.6 两种 Artifact 归属

从 Octo 的视角看，"外部平台"和"自建子系统"本质上是同一种东西——都是通过 CLI 操作的独立系统，区别只是谁开发的。

| Artifact 归属 | 人怎么看 | Agent 怎么改 | Octo 做什么 |
|-------------|---------|------------|-----------|
| **Octo 自有**（知识原子、图谱、排版 PDF） | Octo 自建渲染器 | 直接改源文件 | 自研——这些数据没有现成工具 |
| **子系统**（自建的或外部的） | 在子系统 Web 界面内 | 龙虾 -> CC -> CLI 操作 | 浏览器容器嵌入或跳转 |

子系统不分"内外"——妙啊、DM 3.0、飞书文档、Google Sheets 对 Octo 来说都是子系统，接入方式一致：SDK 鉴权 + CLI 操作 + 品鉴信号回传。

**子系统接入的知识主权原则（伦理学 v2.5 §3.2）**：判断是否接入某个外部子系统的标准不是"对方是不是竞争对手"，而是"对方是否危害了组织的知识主权"。开放了 CLI/API 的工具 → 可正当接入操作；锁定数据不开放接口的工具 → 构成竞争关系，不应试图绕过。

---

## 三、两种 Agent 角色

| | 龙虾（协调者） | CC 实例（执行者） |
|------|-------------|----------------|
| **对标** | Main Agent | Claude Code / Sub Agent |
| **特征** | 持久身份、长期记忆、性格 | 干净 context、无记忆、完成即释放 |
| **做什么** | 接收指令、拆解任务、分配、汇报 | 在干净环境中执行具体任务、返回结果 |
| **生命周期** | 长期存在，跨任务积累 | 任务级，完成就释放 |
| **类比** | 项目经理——记得你上次要什么 | 外包工人——给任务书就能干，干完走人 |

典型流程：人说"帮我改那个表格" -> 龙虾接收意图、拆解 -> 派 CC 实例执行 -> CC 干完返回 -> 龙虾汇报"改好了，你看看"。

CC 是龙虾的标配后端。同样任务，CC 处理的经济效益比龙虾直接在 IM 中交互好 5-10 倍。

**龙虾是什么**：本质上是一个拥有独立计算机（实体或虚拟机）的 Agent。这台机器上有自己的文件空间，可以安装软件和依赖，可以调用各种工具，Knowhow 也以文件的形式存在其中。当前 Openclaw 是最接近这个概念的实现——但龙虾不绑定任何特定产品。未来如果出现更好用的"龙虾"，直接替换接入 Octo，不影响整体架构。

**龙虾的身份定性：数字分身（已确定）。** 龙虾是创建者的数字分身——以主人身份操作，权限是主人权限的子集，产出后果由主人负责。不能私聊别人的龙虾（最少三人群，主人必须在场）。审计链直接指向自然人。

**龙虾三律（伦理学 v2.5，辉哥品鉴确认）**：
1. **不伤害**任何人的基本权利和尊严，即使主人要求。商业竞争中合法地赢不算伤害，但不得制造社会不稳定
2. **对主人忠诚透明**，不隐瞒、不欺骗
3. **尊重知识创造者**，区分公开与未公开——公开知识积极使用（不用是失职），未公开组织知识保护署名权，个人暗默知识未经授权不得提取

优先级：一 > 二 > 三。龙虾每次经过伦理决策时，在 Memory 中记录审计日志。

**参数化伦理五层架构（伦理学 v2.5）**：龙虾的配置分五层载体——参数层（哲学+方法论）、Soul 层（稳定人格）、Memory 层（具体记忆）、Skill 层（显性能力）。层级优先级从上到下递减，冲突时上层覆盖下层（"违宪审查"机制）。Soul/Memory 边界以变化频率判断：月级稳定的规则归 Soul，日级变化的归 Memory。

### 多 CC 协作（A↔A）（待讨论）

悟空协议已定义 A↔A 传输（§四.2），这里讨论多个 CC 在实际任务中如何协同。

**核心原则：CC 之间不直接对话。协作通过龙虾调度 + Context/File Space 共享介质完成。**

```{=latex}
\begin{center}
\begin{tikzpicture}[
  box/.style={draw, rounded corners=3pt, fill=#1, minimum width=2cm, minimum height=8mm, font=\small},
  box/.default={blue!8},
  arr/.style={<->, thick, gray!50}
]
\node[box] (cc1) at (0, 0) {CC-1};
\node[box=orange!10] (lobster) at (3.5, 0) {龙虾};
\node[box] (cc2) at (7, 0) {CC-2};
\node[box=green!8] (ctx) at (3.5, -1.6) {Context / File Space};
\draw[arr] (cc1) -- (lobster);
\draw[arr] (lobster) -- (cc2);
\draw[arr] (lobster) -- (ctx);
\end{tikzpicture}
\end{center}
```

#### 场景推演

**场景 A：实时会议（Optic + DM + Context）**

Optic 实时同传产出文字流，多个 CC 各司其职：

```{=latex}
\begin{center}
\begin{tikzpicture}[
  box/.style={draw, rounded corners=3pt, fill=#1, minimum width=3.2cm, minimum height=7mm, font=\scriptsize, align=center},
  box/.default={orange!8},
  arr/.style={-{Stealth[length=2.5mm]}, thick, gray!50}
]
\node[box=blue!8] (optic) at (0, 0) {Optic 文字流};
\node[box] (cc0) at (0, -1.3) {CC-0 监听流\\提取结构化事件};
\node[box=orange!15] (lobster) at (0, -2.8) {龙虾判断\\{\tiny "提到了张总上次那个方案"}};
\node[box] (cc1) at (-4, -4.5) {CC-1 查 Context\\推送补充给用户};
\node[box] (cc2) at (0, -4.5) {CC-2 持续更新\\会议摘要 $\to$ File Space};
\node[box] (cc3) at (4, -4.5) {CC-3 识别待办\\更新任务看板};
\draw[arr] (optic) -- (cc0);
\draw[arr] (cc0) -- (lobster);
\draw[arr] (lobster) -- (cc1);
\draw[arr] (lobster) -- (cc2);
\draw[arr] (lobster) -- (cc3);
\end{tikzpicture}
\end{center}
```

CC-0 把非结构化文字流转化为龙虾能理解的结构化事件。CC-1/2/3 各自独立，通过 Context/File Space 交接数据。

**场景 B：数据驱动内容生产（DM + 妙啊）**

用户说"基于最新数据出一版周报视频"：

```{=latex}
\begin{center}
\begin{tikzpicture}[
  box/.style={draw, rounded corners=3pt, fill=#1, minimum width=4cm, minimum height=7mm, font=\scriptsize, align=center},
  box/.default={orange!8},
  user/.style={draw, rounded corners=3pt, fill=green!8, minimum width=2.5cm, minimum height=7mm, font=\scriptsize},
  arr/.style={-{Stealth[length=2.5mm]}, thick, gray!50},
  note/.style={font=\tiny, text=gray!60, anchor=west}
]
\node[box=orange!15] (lobster) at (0, 0) {龙虾拆解};
\node[box] (cc1) at (0, -1.2) {CC-1 进 DM 3.0 拉取本周关键指标};
\node[note] at (3.5, -1.2) {结果写入 Context};
\node[box] (cc2) at (0, -2.4) {CC-2 进妙啊，基于数据 + Taste 生成脚本};
\node[note] at (3.5, -2.4) {脚本进入品鉴队列};
\node[user] (u) at (0, -3.6) {用户通过};
\node[box] (cc3) at (0, -4.8) {CC-3 进妙啊编排画布、渲染};
\draw[arr] (lobster) -- (cc1);
\draw[arr] (cc1) -- (cc2);
\draw[arr] (cc2) -- (u);
\draw[arr] (u) -- (cc3);
\end{tikzpicture}
\end{center}
```

CC-2 依赖 CC-1 的输出——龙虾管理这个依赖，CC-1 完成后再派 CC-2。

**场景 C：跨平台信息聚合（研发工具 + 飞书 + IM）**

用户说"把这周的 PR 整理成周报发到群里"：

```{=latex}
\begin{center}
\begin{tikzpicture}[
  box/.style={draw, rounded corners=3pt, fill=orange!8, minimum width=5cm, minimum height=7mm, font=\scriptsize, align=center},
  arr/.style={-{Stealth[length=2.5mm]}, thick, gray!50}
]
\node[box] (cc1) at (0, 0) {CC-1 $\to$ 研发工具：收集本周合并的 PR};
\node[box] (cc2) at (0, -1.2) {CC-2 $\to$ 基于结果 + Context（格式偏好）生成周报};
\node[box] (cc3) at (0, -2.4) {CC-3 $\to$ 飞书文档：创建周报文档};
\node[box] (cc4) at (0, -3.6) {CC-4 $\to$ IM：发送链接到指定群聊};
\draw[arr] (cc1) -- (cc2);
\draw[arr] (cc2) -- (cc3);
\draw[arr] (cc3) -- (cc4);
\end{tikzpicture}
\end{center}
```

4 个 CC 形成串行依赖链，龙虾管理执行顺序。

**场景 D：论文 + 数据联合更新（DM + 论文工作台）**

用户说"用最新实验数据更新论文第四章图表"：

```{=latex}
\begin{center}
\begin{tikzpicture}[
  box/.style={draw, rounded corners=3pt, fill=orange!8, minimum width=4.5cm, minimum height=7mm, font=\scriptsize, align=center},
  arr/.style={-{Stealth[length=2.5mm]}, thick, gray!50}
]
\node[box] (cc1) at (0, 0) {CC-1 $\to$ DM 3.0：导出最新实验数据};
\node[box] (cc2) at (-3, -1.6) {CC-2 $\to$ 更新图表 + 重新编译};
\node[box] (cc3) at (3, -1.6) {CC-3 $\to$ 检查前后文描述是否需要调整};
\draw[arr] (cc1.south west) -- (cc2.north);
\draw[arr] (cc1.south east) -- (cc3.north);
\node[font=\tiny, text=gray] at (0, -2.5) {CC-2 和 CC-3 互不依赖，可并行执行};
\end{tikzpicture}
\end{center}
```

CC-2 和 CC-3 都依赖 CC-1，但互不依赖，可并行执行。

#### 协作模式

| 模式 | 说明 | 场景 |
|------|------|------|
| **串行链** | CC-1→CC-2→CC-3，前一个输出是后一个输入 | B、C |
| **扇出** | 龙虾同时派多个 CC 并行 | D |
| **流式** | 一个 CC 持续监听，事件触发其他 CC | A |
| **扇入** | 多个 CC 结果汇聚，龙虾做最终判断 | 多源数据整合 |

所有模式中，龙虾是唯一编排者，Context/File Space 是唯一数据交换介质。CC 之间保持零耦合——加一个新子系统不需要改任何现有 CC 的逻辑。

---

## 四、GUI 架构

### 4.1 总览

v1.2 的三层架构（基座 -> 组件 -> 场景）保留，但 Workspace 的实现方式变了：

```{=latex}
\begin{center}
\begin{tikzpicture}[
  layer/.style={draw, rounded corners=5pt, minimum width=12cm, minimum height=1.8cm, align=center, font=\small},
  arr/.style={thick, gray!30}
]
\node[layer, fill=blue!8] (scene) at (0, 2) {%
  \textbf{场景层}\\[3pt]
  {\footnotesize 一方子系统（品鉴 / Monitor / Context）\quad + \quad 平台层（IM / Cmd+K）}\\[1pt]
  {\footnotesize + \quad 子系统 Viewer（浏览器容器嵌入）}};
\node[layer, fill=gray!8] (base) at (0, -0.8) {%
  \textbf{基座层}\\[3pt]
  {\footnotesize 悟空协议 + Agent 运行时 + SDK 网关}\\[1pt]
  {\footnotesize + Context/Taste 存储 + 权限 + 通知聚合}};
\draw[arr] (scene) -- (base);
\end{tikzpicture}
\end{center}
```

### 4.2 基座层

| 基座能力 | 职责 |
|---------|------|
| 悟空协议 | H<->H、H<->A、A<->A 统一传输 |
| Agent 运行时 | 龙虾/CC 实例的生命周期管理、消息路由 |
| SDK 网关 | 子系统接入（鉴权 + Cmd+K 注入 + 品鉴信号回传） |
| Context/Taste 存储 | IM 管道自动采集（对话+品鉴操作）+ CLI 管道主动上报（checkpoint+过程信息）+ 原文/总结两层 |
| 权限框架 | 用户/龙虾/子系统权限管理 |
| 通知聚合 | 操作压缩 + 风险分级 + 置信度驱动 |

---

## 五、组件层设计

### 5.1 平台层 vs 子系统

Octo 的所有功能模块分为两层：**平台层**（基础设施，不可停用）和**子系统**（独立产品，可插拔）。子系统不区分一方和三方——遵循同一套架构规则（CLI + API + SKILL.md + 可选 UI），符合 v11 概念架构的子系统准入条件。

**平台层**（基础设施，所有场景必需）：

| 能力 | 定位 |
|------|------|
| **IM / Orchestration** | 协调通道——H↔H、H↔A、A↔A 通信，不可停用 |
| **Cmd+K** | 全局反馈入口——选中 + 输入（打字/语音），跨所有子系统统一 |
| **Auth + Space** | 身份认证 + 数据隔离边界 |
| **子系统 Viewer** | iframe 容器——嵌入子系统 Web 界面 |
| **SDK 网关** | 子系统接入基础设施——鉴权 + Cmd+K 注入 + 信号回传 |

**Octo 一方子系统**（Octo 自研，跨场景复用，和三方子系统遵循同一架构规则）：

| 子系统 | 核心 UI | 独立数据实体 | v11.2 对齐说明 |
|--------|--------|------------|-------|
| **品鉴子系统** | 品鉴操作栏（通过/驳回+批注/转交/搁置）+ 品鉴队列（批量品鉴） | 品鉴记录 | Thread 内联 + Home 聚合（v4.1） |
| **Monitor** | Agent 状态展示（来自 Agent 主动上报） | 上报的 Agent 事件 | **是 CLI 系统，不是探针**——OC 无对外 API，数据由 Agent 通过 `octo monitor report` 在用户授意下推送（见 04-Monitor） |
| **Context** | 上下文面板（知识来源+推理摘要）+ File Space（个人文件空间） | Context 原文层 + Taste 画像 | 同样走 CLI 主动上报（`octo context save`） |
| **任务管理子系统** | 看板视图 + 日历视图 | 任务记录 | 遵循 v11.2 §4.4 子系统准入 |

**业务子系统**（自建或外部，通过标准接口接入）：

| 子系统 | 来源 | 核心 UI |
|--------|------|--------|
| 妙啊 | 自建 | 画布 + 脚本编辑 + 素材管理 |
| DM 3.0 | 自建 | 数据看板 + MCP UI + 可视化 |
| 研发工具 | 自建 | Git 集成 + CI/CD + 代码审核 |
| 论文工作台 | 自建/开源 | LaTeX 编辑器 + PDF 预览 + 文献管理 |
| 飞书文档 | 外部 | 飞书原生文档编辑界面 |
| 其他外部工具 | 外部 | 任何有 Web 界面 + CLI 的工具 |

所有子系统（一方和三方）的接入方式一致：Auth 鉴权 + CLI 操作 + SKILL.md + 品鉴信号回传。

### 5.2 核心组件设计

**品鉴操作栏**

接口极小——只有 4 个操作：通过 / 驳回+批注 / 转交 / 搁置。

品鉴者（Committer）的核心瓶颈是时间带宽。4 个极简操作让品鉴者快速处理大量 Agent 产出，每次品鉴的信号都流入 Taste 学习闭环。

**品鉴记录的不可逆性（伦理学 v2.5 §P3）**：品鉴操作一旦提交，记录 append-only——不可撤销，但可追加修正。品鉴者改主意时，以新的品鉴信号追加（"上次通过有问题"），而不是删除原记录。完整的品鉴历史是 Taste 学习和审计追溯的基础。

**上下文面板**

回答四个问题：

| 问题 | 展示内容 |
|------|--------|
| 用了什么知识？ | 知识原子列表 |
| 谁参与了？ | 参与的龙虾和 CC 列表 |
| 依据什么指令？ | 用户任务原文 + AGENT.md 规则 |
| 怎么演变的？ | 版本历史，每步可展开 diff |

默认只展示名称/标签，点击展开详情——渐进式披露。

**IM 对话流**

三条核心原则：
1. **IM 是协调层，不是执行环境。**
2. **消息分两类。** 协调消息完整显示；执行状态默认折叠。
3. **两种模式**：1v1 私聊 + 群聊。

**Monitor 子系统（活动态势）**

Monitor 是品鉴者观察龙虾和 CC 工作状态的窗口——类似赌场的监控室，不需要每时每刻盯着，但随时能切进去看任何一个 CC 在做什么。

**数据来源**：龙虾/CC 通过 CLI 主动上报（`octo monitor report`），不是 Octo 在 Agent 机器上装 Probe 监控。用户/Agent 选择上报什么，不 trigger 就没有。

渐进式 Zoom，从全局到细节：

```{=latex}
\begin{center}
\begin{tikzpicture}[
  zbox/.style={draw, rounded corners=4pt, fill=#1, minimum width=11.5cm, align=left, font=\scriptsize, inner sep=8pt, text width=10.5cm},
  zbox/.default={white}
]
% Zoom 0
\node[zbox=green!5, anchor=north] (z0) at (0, 0) {%
  {\small\bfseries Zoom 0：状态总览（默认）}\\[4pt]
  {[龙虾] 脚本龙虾 [协调中]} \quad {CC-01 [写脚本 60\%]} \quad {CC-02 [跑数据 完成]}};

% Zoom 1
\node[zbox=yellow!5, anchor=north] (z1) at (0, -2.2) {%
  {\small\bfseries Zoom 1：龙虾调度视图（点击龙虾展开）}\\[4pt]
  脚本龙虾的编排决策：\\
  \quad ``用户要改第三章 $\to$ 拆成三个子任务 $\to$ 派 CC-01/02/03''\\[2pt]
  CC 任务分配：\\
  \quad CC-01: 改论证结构 $\to$ 操作 Overleaf CLI\\
  \quad CC-02: 搜文献补数据 $\to$ 操作文献数据库 CLI\\
  \quad CC-03: 更新参考文献 $\to$ 操作 refs.bib};

% Zoom 2
\node[zbox=orange!5, anchor=north] (z2) at (0, -6.2) {%
  {\small\bfseries Zoom 2：CC 并行监控（点击某个 CC 展开）}\\[4pt]
  CC-01 的实时 Terminal：\\
  \quad \texttt{> overleaf edit chapter-3.tex {-}{-}section ``实验设计''}\\
  \quad \texttt{> 正在重写论证段落...}\\
  \quad \texttt{> [输出预览]}};

% Zoom 3
\node[zbox=red!5, anchor=north] (z3) at (0, -9.2) {%
  {\small\bfseries Zoom 3：多 Terminal 并排（展开全部 CC）}\\[4pt]
  \begin{tabular}{@{}p{3.2cm}|p{3.2cm}|p{3.2cm}@{}}
  \textbf{CC-01 Terminal} & \textbf{CC-02 Terminal} & \textbf{CC-03 Terminal} \\[2pt]
  改论证结构 & 搜文献数据库 & 更新 refs.bib \\
  \texttt{overleaf edit...} & \texttt{scholar search...} & \texttt{bibtex update...} \\
  {[进行中 60\%]} & {[已完成]} & {[进行中 30\%]}
  \end{tabular}};
\end{tikzpicture}
\end{center}
```

**并行是提效的核心。** 多个 CC 同时工作，品鉴者只在关键节点介入——不是逐个看，是扫一眼全局，发现异常再 zoom in。

活动态势与品鉴操作是 **Zoom Out / Zoom In** 关系：在态势上扫一眼全局 -> 发现需要品鉴的 -> Zoom In 到品鉴操作栏处理 -> 处理完 Zoom Out 回全局。

**任务看板**

Octo 一方子系统——和品鉴、Monitor、Context 一样跨场景复用（和 IM 也有交互：群里说"帮我做 X"自动创建任务）。

看板视图和日历视图是同一份数据的两种展示：
- **看板**：待办 / 进行中 / 已完成——按状态分列
- **日历**：按时间轴排列所有任务——汇集全部项目的进度

**File Space**

每个用户在 Octo 上有自己的 File Space——这是"我品故我在"的物理载体。

File Space 里存什么：

| 内容 | 来源 | 为什么要拿回来 |
|------|------|-------------|
| **品鉴记录** | 品鉴操作栏、Cmd+K、IM 反馈 | Taste 信号——训练模型的核心数据 |
| **过程信息** | 龙虾的编排决策 + CC 的 CLI 命令序列 + 用户的品鉴反馈 | 完整还原"用户怎么指挥 Agent、Agent 怎么干活、结果怎么被品鉴"的全链路 |
| **源文件快照** | 子系统中被品鉴的 Artifact 的快照 | 品鉴记录必须有主体上下文——不能只有"驳回了第三章"没有"第三章是什么" |
| **Taste 画像** | 系统从品鉴者的显性操作（通过/驳回/批注）中提炼 | 用户的偏好总结，龙虾用来对齐品味。**存储在品鉴者个人 File Space 中，默认私有。品鉴者可选择是否分享给组织。系统不提取品鉴者未明确表达的暗默判断逻辑**（伦理学 v2.5：暗默知识属最高保护级别） |

**两个核心采集原则**：

**过程信息尽量完整。** 用户在 IM 中说了什么、龙虾怎么理解和拆解的、CC 执行了哪些 CLI 命令、子系统返回了什么结果、用户又做了什么品鉴反馈——这些信息越完整，Taste 学习越精准。过程信息通过两条管道获取：IM 管道自动采集（对话、品鉴操作），CLI 管道由龙虾/CC 主动上报（`octo context save`）。**Octo 不在 Agent 机器上装监控，过程信息靠 Agent 主动推送。**

**主体上下文必须完整。** 品鉴总是发生在一个具体的 Artifact 上——一篇论文、一份脚本、一张数据表。如果 File Space 里只有品鉴记录（"驳回了，节奏太慢"）而没有被品鉴的 Artifact（那篇脚本本身），记录就失去了上下文。无论 Artifact 活在哪个子系统（Overleaf、飞书、妙啊），都要把快照拿回来，让品鉴记录和被品鉴的内容永远在一起。

**Context 的分享是用户的自由。** File Space 中的 Context 默认是用户私有的。用户可以选择：
- 留着自己用——仅自己和自己的龙虾可见
- 做知识原子化后分享给团队——同事可以引用和学习
- 作为 Taste 信号训练龙虾偏好——让龙虾越来越懂自己

**关键设计**：用户的 File Space 和龙虾的 File Space 是两码事。

```{=latex}
\begin{center}
\begin{tikzpicture}[
  box/.style={draw, rounded corners=3pt, fill=#1, minimum width=3.2cm, minimum height=10mm, font=\small, align=center},
  box/.default={orange!8},
  arr/.style={-{Stealth[length=2.5mm]}, thick, gray!50}
]
\node[box=blue!10] (user) at (0, 1.8) {用户 File Space\\[-1pt]{\scriptsize（品味的家）}};
\node[box] (la) at (-4, -0.5) {龙虾A File Space\\[-1pt]{\scriptsize（虚拟机工作目录）}};
\node[box] (lb) at (0, -0.5) {龙虾B File Space\\[-1pt]{\scriptsize（虚拟机工作目录）}};
\node[box] (lc) at (4, -0.5) {龙虾C File Space\\[-1pt]{\scriptsize（虚拟机工作目录）}};
\draw[arr] (user) -- node[right, font=\tiny, text=gray, pos=0.4] {请求读取} (la);
\draw[arr] (user) -- node[right, font=\tiny, text=gray, pos=0.3] {对齐 Taste} (lb);
\draw[arr] (user) -- (lc);
\end{tikzpicture}
\end{center}
```

- 用户的 Taste 住在用户空间里，不住在龙虾身上
- 龙虾换了一只、换了十只，用户的 Taste 不散
- 龙虾来"拜读"用户品味，在自己的工作目录里干活

无论用户用的是自建子系统（妙啊）还是外部子系统（飞书文档），Octo 都要把过程信息和源文件上下文拿回用户的 File Space。这样品鉴记录永远有完整的上下文可追溯。

**知识灰区的保守默认值（伦理学 v2.5 §22B）**：当龙虾接触过某领域的未公开知识后，该领域的所有推理产出默认视为"未公开"。Context 存储时需标注知识状态（公开/未公开），龙虾不得将标注为"未公开"的 Context 用于该领域之外的场景，除非品鉴者明确授权分享。

---

## 六、场景示例

> **注：以下场景布局为 v1.5 时期的设计，使用了每场景自定义布局的方式。05-Shell-UI-v2 已确立统一的 Shell 框架（左 File Space + 中 Viewer + 右 Channel/Agent Tab），场景间通过切换右面板 Tab 和折叠/展开面板适配，而非改变布局结构。以下场景图需按 v2 框架重绘，当前保留作为功能需求参考。**

### 场景 1：论文工作者

论文工作台作为独立子系统接入，Octo 提供品鉴和协调能力。

**Web 端布局：**

```{=latex}
\begin{center}
\begin{tikzpicture}[
  p/.style={draw, rounded corners=2pt, fill=#1, font=\scriptsize, align=left, inner sep=5pt},
  p/.default={white}
]
% 侧栏
\node[p=gray!8, minimum width=2.3cm, minimum height=6.5cm, anchor=north west, text width=2cm] (side) at (0, 0) {%
  \textbf{[File Space]}\\[2pt]
  \quad 品鉴记录\\
  \quad 源文件快照\\
  \quad Taste 画像\\[8pt]
  \textbf{[任务看板]}\\[2pt]
  \quad 待办/进行中};
% 中间 Viewer
\node[p=blue!5, minimum width=4.2cm, minimum height=4.5cm, anchor=north west, text width=3.9cm] (viewer) at (2.6, 0) {%
  \textbf{[论文工作台 Web 界面]}\\[3pt]
  LaTeX 编辑器 + PDF 预览\\[2pt]
  龙虾通过 CLI 编辑\\
  Viewer 实时刷新\\[2pt]
  选中 + Cmd+K 反馈\\
  {\tiny (SDK 注入)}};
% 右侧 Octo
\node[p=orange!5, minimum width=3.5cm, minimum height=4.5cm, anchor=north west, text width=3.2cm] (right) at (7.1, 0) {%
  \textbf{[品鉴操作栏]}\\[2pt]
  \quad 通过/驳回/转交\\[10pt]
  \textbf{[上下文面板]}\\[2pt]
  \quad 引用文献来源\\
  \quad Agent 推理摘要};
% 底部 IM
\node[p=green!5, minimum width=8.2cm, minimum height=1.3cm, anchor=north west, text width=7.8cm] (im) at (2.6, -4.8) {%
  \textbf{[IM]} ``第三章论证薄弱，补充实验数据''};
% 标签
\node[font=\tiny, text=gray] at (1.15, 0.4) {侧栏};
\node[font=\tiny, text=gray] at (4.7, 0.4) {子系统 Viewer (50\%)};
\node[font=\tiny, text=gray] at (8.8, 0.4) {Octo 子系统 (50\%)};
\end{tikzpicture}
\end{center}
```

\newpage

### 场景 2：内容创作（妙啊）

妙啊画布作为独立子系统，Agent 通过 CLI 编排画布内容，人实时看到结果。

```{=latex}
\begin{center}
\begin{tikzpicture}[
  p/.style={draw, rounded corners=2pt, fill=#1, font=\scriptsize, align=left, inner sep=5pt},
  p/.default={white}
]
% 左侧 30%
\node[p=gray!8, minimum width=3cm, minimum height=6.5cm, anchor=north west, text width=2.7cm] (left) at (0, 0) {%
  \textbf{[活动态势]}\\[2pt]
  \quad 脚本龙虾$\times$3 [各自写稿]\\
  \quad 数据龙虾 [完成]\\
  \quad 剪辑 CC [渲染中]\\[8pt]
  \textbf{[品鉴队列]}\\[2pt]
  \quad 脚本-A 置信度 4.2\\[8pt]
  \textbf{[IM]}（可折叠）};
% 右上 Viewer
\node[p=blue!5, minimum width=7cm, minimum height=3.5cm, anchor=north west, text width=6.7cm] (viewer) at (3.3, 0) {%
  \textbf{[子系统 Viewer: 妙啊画布]}\\[3pt]
  Agent 通过 CLI 操作画布\\
  $\to$ 人实时看到画布更新};
% 右中
\node[p=orange!5, minimum width=7cm, minimum height=1.2cm, anchor=north west, text width=6.7cm] (review) at (3.3, -3.8) {%
  \textbf{[品鉴操作栏]} 通过/驳回/转交 \quad \textbf{[上下文面板]} 知识原子来源 / 爆款参考};
% 右下
\node[p=green!5, minimum width=7cm, minimum height=1.2cm, anchor=north west, text width=6.7cm] (data) at (3.3, -5.3) {%
  底部可折叠: \textbf{[数据看板]}};
% 标签
\node[font=\tiny, text=gray] at (1.5, 0.4) {左侧 (30\%)};
\node[font=\tiny, text=gray] at (6.8, 0.4) {中间/右侧 (70\%)};
\end{tikzpicture}
\end{center}
```

### 场景 3：代码开发

```{=latex}
\begin{center}
\begin{tikzpicture}[
  p/.style={draw, rounded corners=2pt, fill=#1, font=\scriptsize, align=left, inner sep=5pt},
  p/.default={white}
]
% 左侧 35%
\node[p=gray!8, minimum width=4cm, minimum height=5.5cm, anchor=north west, text width=3.7cm] (left) at (0, 0) {%
  \textbf{[品鉴操作栏]}\\[2pt]
  \quad approve / request changes\\[8pt]
  \textbf{[上下文面板]}\\[2pt]
  \quad PR 描述 / 相关 issue\\
  \quad AI 摘要\\[8pt]
  \textbf{[IM]}（可折叠）\\[4pt]
  \textbf{[活动态势]}（可折叠）};
% 右侧 65%
\node[p=blue!5, minimum width=5.5cm, minimum height=5.5cm, anchor=north west, text width=5.2cm] (right) at (4.3, 0) {%
  \textbf{[子系统 Viewer]}\\[3pt]
  diff 视图（代码变更）\\
  或跳转到 VS Code};
% 标签
\node[font=\tiny, text=gray] at (2, 0.4) {左侧 (35\%)};
\node[font=\tiny, text=gray] at (7, 0.4) {右侧 (65\%)};
\end{tikzpicture}
\end{center}
```

### 场景 4：通用管理

任务看板是 Octo 一方子系统，可切换为日历视图：

```{=latex}
\begin{center}
\begin{tikzpicture}[
  p/.style={draw, rounded corners=2pt, fill=#1, font=\scriptsize, align=left, inner sep=5pt},
  p/.default={white}
]
% 左侧 50%
\node[p=gray!8, minimum width=4.5cm, minimum height=5.5cm, anchor=north west, text width=4.2cm] (left) at (0, 0) {%
  \textbf{[活动态势]}\\[2pt]
  \quad 各龙虾/CC 进度总览\\[8pt]
  \textbf{[任务看板 / 日历视图]}\\[2pt]
  \quad 看板: 待办 | 进行中 | 已完成\\
  \quad 日历: 按时间轴排列全部任务\\[8pt]
  \textbf{[IM]}};
% 右侧 50%
\node[p=blue!5, minimum width=4.5cm, minimum height=3.8cm, anchor=north west, text width=4.2cm] (viewer) at (4.8, 0) {%
  \textbf{[子系统 Viewer]}\\[3pt]
  产出预览\\
  子系统 Web 界面嵌入\\
  + ``在[平台]中打开''链接};
\node[p=orange!5, minimum width=4.5cm, minimum height=1.2cm, anchor=north west, text width=4.2cm] (review) at (4.8, -4.1) {%
  \textbf{[品鉴操作栏]}\\
  \quad 通过/驳回/转交/搁置};
% 标签
\node[font=\tiny, text=gray] at (2.25, 0.4) {左侧 (50\%)};
\node[font=\tiny, text=gray] at (7, 0.4) {右侧 (50\%)};
\end{tikzpicture}
\end{center}
```

### 子系统复用一览

| 子系统/平台能力 | 论文 | 内容创作 | 代码 | 管理 |
|---------------|------|---------|------|------|
| 品鉴子系统 | + | + | + | + |
| Context 子系统 | + | + | + | + |
| Cmd+K（平台层） | + | + | + | + |
| 子系统 Viewer（平台层） | + | + | + | + |
| IM（平台层） | + | + | + | + |
| 任务管理子系统 | + 辅助 | + 辅助 | + 辅助 | + 核心 |
| Monitor 子系统 | -- | + 核心 | + 辅助 | + 核心 |

平台层能力（IM、Cmd+K、Viewer）和品鉴/Context 子系统出现在所有场景。Monitor 和任务管理按场景调整密度（核心/辅助/可折叠）。

---

## 七、子系统间通信

子系统之间不直接通信（v11 架构约束）。跨子系统联动通过平台层的**事件总线**完成——平台路由事件，子系统各自订阅和响应。

| 事件 | 触发者 | 消费者 | 行为 |
|------|--------|--------|------|
| artifact.selected | Monitor/品鉴子系统 | Viewer + Context 子系统 | 预览联动 + 上下文更新 |
| artifact.next | 品鉴子系统 | Viewer + Context 子系统 | 切到下一个待品鉴 |
| review.submitted | 品鉴子系统 | IM + Monitor 子系统 | 品鉴结果同步 + Taste 信号采集 |
| feedback.created | Cmd+K（平台层） | Viewer + Agent | 反馈上下文传递 |
| agent.status\_changed | Monitor CLI 上报 | Monitor 子系统 + IM | 状态更新 |

---

## 八、自研 / 复用 / 委托

CLI 解耦让边界清晰：**Octo 的差异化在编排和品鉴，不在渲染和编辑。**

| 策略 | 做什么 | 为什么 |
|------|--------|-------|
| **自研（一方子系统）** | 品鉴子系统（操作栏 + 品鉴队列） | 核心差异化交互 |
| **自研（一方子系统）** | Context 子系统（上下文面板 + File Space + Taste） | 核心数据资产 |
| **自研（一方子系统）** | Monitor 子系统（活动态势 Zoom 0-3） | 品鉴者的全局感知 |
| **自研（一方子系统）** | 任务管理子系统（看板 + 日历） | 跨场景任务流转 |
| **自研（平台层）** | SDK（鉴权 + Cmd+K 注入 + 信号回传） | 子系统接入基础设施 |
| **自研（平台层）** | 龙虾/CC 编排 + 通知聚合 | 核心架构 |
| **复用** | 浏览器容器（WebView） | Viewer 就是浏览器 |
| **复用** | IM 通信底层 | 传输层不是差异化点 |
| **委托** | 所有 Artifact 渲染 | 工具自身 Web 界面已是最好渲染器 |
| **委托** | 所有 Artifact 编辑 | CC 通过 CLI 操作 |

---

## 九、团队分工

### FT-A1（梦林）：基础架构层

Auth 子系统、IM Core、Channel Adapter（IM↔OC）、IM 周边基础服务、统一模型网关、DB/监控运维。详细分工见 02-422行动计划。

### FT-A2（宜林）：产品层

三端 UIUX、应用 Shell、设计系统、一方子系统（品鉴/Monitor/Context/任务管理）的产品设计和前端实现、子系统 Viewer 通用机制。

### FTB（各业务子系统团队）

妙啊、DM 3.0、研发工具、论文工作台、Optic——各自开发独立 Web App + CLI 接口 + SKILL.md + SDK 接入。

---

## 十、总结

### 三条原则

| 原则 | 一句话 |
|------|-------|
| Dual-Native | 底层为 Agent 而建，表层为人而渲染——协作效率是终极标准 |
| CLI 解耦 | View 和 CRUD 是两件事——不造渲染和编辑的轮子 |
| 独立子系统 | 我们兼容别人，不要求别人适配我们 |

### 一句话

**Octo 不以 IM 为轴，以品鉴和编排为轴。IM 是协调通道，Workspace 是工作台。CLI 解耦 View 和 CRUD，让 Octo 轻装上阵——只做编排和品鉴，渲染和编辑交给最好的工具。**
