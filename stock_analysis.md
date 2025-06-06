# 上市公司商业报告生成器工作分步文档

## 第一步｜确定商业分析报告需要哪些内容

### 报告核心内容规划
- 公司基本信息板块（公司名称、股票代码、行业分类、上市时间等）
- 财务状况分析板块（盈利能力、成长能力、营运能力、偿债能力）
- 市场表现板块（股价走势、波动率、与大盘对比）
- 行业对比分析板块（与同行业公司的关键指标对比）
- 投资建议板块（评级、理由、风险因素）
- 总结与展望板块

### 确定各板块详细内容
- 财务状况应包含哪些具体指标（ROE、毛利率、净利率等）
- 市场表现应关注哪些时间段（近一个月、近一年、近五年）
- 投资建议需要哪些维度的评估

## 第二步 根据内容看需要哪些数据

### 数据需求分析
- 公司基本信息数据：来源于BaoStock基础数据接口
- 财务数据：需获取至少近5年的年度财务数据和近8个季度的季度财务数据
- 市场交易数据：需获取不同时间粒度的K线数据（日K、月K）
- 行业数据：获取同行业主要竞争对手的数据进行对比

### 数据获取规划
- BaoStock API调用流程设计
- 数据处理与整合方案
- 数据存储格式确定（JSON结构）
- 异常处理策略（如何处理缺失数据、错误数据）

## 第三步 在扣子工作流中的大模型输出中吧数据给结构化

### 输出结构设计
- 确定JSON输出格式的具体字段和层次结构
- 为每个报告板块设计对应的JSON结构
- 定义必要的嵌套关系和数组结构

### 提示词优化
- 明确要求大模型输出符合预定义的JSON结构
- 提供示例输出格式指导大模型
- 添加内容质量要求（客观、专业、数据支持、逻辑清晰）
- 确保大模型理解各字段含义，提供字段说明

### 错误处理策略
- 如果输出不符合JSON格式如何进行后处理
- 设计输出验证机制

## 第四步根据结构化的数据设计html模板

### 界面规划
- 整体布局设计（导航、内容区、侧边栏等）
- 响应式设计考虑（在不同设备上的显示效果）
- 色彩方案确定（专业金融报告风格）

### 内容展示设计
- 如何将结构化数据映射到视觉元素
- 重要信息的突出显示方式
- 图表类型选择（折线图、柱状图、雷达图等）
- 交互设计（可折叠区域、悬停效果等）

### 用户体验优化
- 导航与阅读体验设计
- 视觉层次规划
- 打印与导出考虑

## 第5步 测试

### 功能测试
- 输入不同类型股票代码测试（主板、创业板、科创板等）
- 异常情况测试（无数据、数据极端值、停牌股票等）
- 报告生成速度测试

### 内容质量评估
- 报告内容的专业性和准确性评估
- 与人工编写报告对比分析
- 收集用户反馈改进内容

### 用户体验测试
- 界面友好度测试
- 导航便捷性测试
- 可读性测试

### 迭代优化计划
- 根据测试结果确定优化重点
- 长期改进路线图制定
- 新功能规划（如报告比较、历史报告追踪等）

