---
title: Dual-Native Design — GUI 设计方案 v1.5
topic: otgo
type: source
created: 2026-04-27
tags: [GUI设计, Dual-Native, 产品架构, 子系统, 品鉴]
---

# Dual-Native Design — GUI 设计方案 v1.5

**来源时间**：v1.4 原版 2026-04-04，0405 补充伦理学对齐，v1.5 于 2026-04-20 对齐 v11.2 架构  
**定位**：Octo GUI 的设计蓝图，面向产研团队

---

## 摘要

本文件定义了 Octo GUI 的核心设计原则——Dual-Native Design（底层为 Agent 而建，表层为人而渲染）——以及由此推导出的产品形态、四端策略、子系统架构、File Space 设计、Monitor 子系统。v11.2 关键变化：三端扩充为四端（新增 Browser Extension）；iframe 嵌入路径收敛为 Thread 富 Artifact 卡片；Monitor 确认为 CLI 主动上报，非探针监控。

---

## 核心要点

### Dual-Native Design
- 每个设计决策同时通过三道检验：对人好用？对 Agent 好接？两者协作更高效？
- **IM 是协调通道，Workspace 是工作台**——两者互补不互替
- Octo 不以 IM 为轴，以**品鉴和编排**为轴
- 两个关键判断：(1) 未来所有主流软件都会 Agentic 化；(2) Octo 以 IM 为轴打不过企微/飞书

### CLI 解耦（View 和 CRUD 独立）
- **CRUD**（龙虾干的）：CC 通过 CLI 操作工具修改文件
- **View**（人看的）：工具自身 Web 界面负责渲染，Octo 只提供浏览器容器
- 结果：Octo 不建渲染器，不建编辑器——只做**编排**和**品鉴**
- 与 Claude Code + VS Code 同一模式

### 四端策略（v11.2）
| 端 | 定位 | 核心体验 |
|----|------|---------|
| Web | IM 主场 + 全功能 | Channel/Thread 导航 + 原生预览 |
| iOS/Android | 移动品鉴 | 通知 + Decision Queue + 轻量回复 |
| Browser Extension | 协作桥梁 | 在任意 Web 工具旁注入 Chat 侧边栏 + Cmd+K |

移动端不做子系统嵌入，只做审批和追踪。**通知是移动端最重要的产品。**

### 两种 Agent 角色
| | 龙虾（协调者） | CC 实例（执行者） |
|---|---|---|
| 对标 | Main Agent | Claude Code / Sub Agent |
| 特征 | 持久身份、长期记忆、性格 | 干净 context、无记忆、完成即释放 |
| 类比 | 项目经理——记得你上次要什么 | 外包工人——给任务书就能干 |

CC 是龙虾的标配后端，经济效益比龙虾直接在 IM 中交互好 5-10 倍。

### 多 CC 协作（四种模式）
- CC 之间不直接对话——协作通过龙虾调度 + Context/File Space 共享介质完成
- **串行链**：CC-1→CC-2→CC-3，前一个输出是后一个输入
- **扇出**：龙虾同时派多个 CC 并行（互不依赖任务）
- **流式**：一个 CC 持续监听，事件触发其他 CC
- **扇入**：多个 CC 结果汇聚，龙虾做最终判断

### 统一反馈手势：Cmd+K
在任何端、任何子系统，品鉴反馈模式统一：**指哪 + 说啥**。
- 文本 PDF：选中文字 → "这段逻辑不通顺"
- 表格：选中单元格 → "这几个数对不上"
- 代码：选中代码段 → "这个循环会死循环"
- 任何 Artifact：不指 → "整体感觉不对" / "通过"

### 子系统架构
平台层（IM/Cmd+K/Auth/Viewer/SDK 网关，不可停用）+ 一方子系统（品鉴/Monitor/Context/任务管理）+ 业务子系统（妙啊/DM 3.0/研发工具等）。子系统间不直接通信，通过事件总线解耦。

### File Space（用户的 Taste/Context 载体）
- 内容：品鉴记录、过程信息（编排决策 + CLI 命令序列）、源文件快照、Taste 画像
- **用户 File Space 和龙虾 File Space 是两码事**——Taste 住在用户空间，龙虾换了一只也不散
- 采集双管道：IM 管道（自动）+ CLI 管道（`octo context save` 主动上报）
- Context 默认私有，用户可选择留着用/原子化分享/训练龙虾

### Monitor 子系统（活动态势）
- **是 CLI 主动上报系统，不是探针监控**——Agent 授意下通过 `octo monitor report` 推送
- 渐进式 Zoom 0→3：状态总览 → 龙虾调度视图 → CC 并行监控 → 多 Terminal 并排
- 与品鉴操作是 Zoom Out / Zoom In 关系

### 品鉴操作栏
4 个极简操作：通过 / 驳回+批注 / 转交 / 搁置。  
品鉴记录不可逆（append-only）——可追加修正，不可删除原记录。

---

## 引用

> Octo 不以 IM 为轴，以品鉴和编排为轴。IM 是协调通道，Workspace 是工作台。CLI 解耦 View 和 CRUD，让 Octo 轻装上阵——只做编排和品鉴，渲染和编辑交给最好的工具。

> 底层为 Agent 而建，表层为人而渲染。两者从不妥协，各自极致。

---

## Connections

- [[otgo/overview|OTGO 全景概览]]
- [[otgo/concepts/dual-native|Dual-Native Design]] — 本文件的核心设计原则
- [[otgo/concepts/cli-decoupling|CLI 解耦]] — View/CRUD 分离架构
- [[otgo/concepts/file-space|File Space]] — 用户 Context/Taste 载体
- [[otgo/concepts/multi-cc-collab|多 CC 协作模式]] — 四种协作模式详解
- [[otgo/concepts/wukong-protocol|悟空协议]] — H↔H/H↔A/A↔A 通信基础
- [[otgo/concepts/lonxia|龙虾 (Lobster)]] — 协调者角色
- [[otgo/concepts/taste-philosophy|品 (Taste) 哲学]] — 品鉴设计的哲学基础
- [[otgo/entities/wu-minghui|吴明辉 (辉哥)]] — 战略设计者
