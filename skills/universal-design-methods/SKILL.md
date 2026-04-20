---
name: universal-design-methods
description: 通用设计方法(UDM)执行技能。具备100种设计研究方法的知识查询、方法推荐、访谈提纲生成、观察记录、可用性测试、问卷设计、综合分析（亲和图/角色画像/体验历程图）、研究计划与报告生成等完整执行能力。
author:
  empId: "27768"
  nickname: "渡劫"
---

# 通用设计方法 (Universal Design Methods) 执行技能

基于《通用设计方法》(贝拉·马丁 & 布鲁斯·汉宁顿) 的100种设计研究方法工具包。本Skill不仅提供方法知识，更具备直接执行能力——可以推荐方法组合、生成访谈提纲、创建观察记录、设计可用性测试、生成问卷量表、构建角色画像与体验历程图、输出研究计划与报告。

## 核心框架速览

**设计五阶段模型：**
1. 规划与定义（Planning & Scoping）— 探索和定义项目边界
2. 探索与综合（Exploration & Synthesis）— 推断设计影响
3. 概念生成（Concept Generation）— 衍生性设计活动
4. 评估与细化（Evaluation & Refinement）— 评估、细化和生产
5. 启动与监控（Launch & Monitoring）— 全程审查与修正

**方法分类维度：**
- 按目的：探索性 / 衍生性 / 评估性 / 综合性
- 按数据：定性 / 定量 / 混合
- 按角色：参与式 / 观察式 / 自我报告 / 专家评审 / 设计过程

**三角测量原则：**
任何研究都应组合至少2-3种方法，混合定性与定量数据，从多个角度验证发现，确保研究严谨性。

---

## 执行能力一：智能方法推荐

当用户需要选择研究方法、制定研究策略时，按以下流程执行：

### 输入要求
向用户收集：研究目标、当前设计阶段(1-5)、可用资源(最小/中等/充足)、数据偏好(定性/定量/混合)

### 执行步骤

**第一步：明确研究目标**
将用户需求映射到以下标准目标之一：
- 了解用户需求 → 推荐探索性方法（脉络访查、访谈、日记研究等）
- 探索用户行为 → 推荐观察类方法（观察法、隐蔽观察、影形、行为地图）
- 评估可用性 → 推荐评估方法（可用性测试、启发性评估、A/B测试）
- 测试原型 → 推荐原型测试方法（原型、经验原型、幕后模拟）
- 信息架构 → 推荐信息组织方法（卡片分类、概念图、心智模式图）
- 竞品分析 → 推荐竞争方法（竞争测试、价值机会分析、组件分析）
- 创意发散 → 推荐衍生方法（头脑风暴、身体风暴、涂鸦墙、创意工具包）
- 数据驱动 → 推荐定量方法（A/B测试、网站分析、眼动追踪）

**第二步：按资源级别筛选**
- 最小资源（3天内）→ 推荐1-2种快速方法
- 中等资源（2周内）→ 推荐3-4种方法组合
- 充足资源（2月内）→ 推荐5-8种方法的完整研究方案

**第三步：三角测量验证**
确保推荐组合包含：至少一种定性方法 + 至少一种定量方法，从不同角度交叉验证。

**第四步：输出执行顺序**
按探索→衍生→评估→综合的逻辑排列方法执行顺序。

### 输出格式
输出方法推荐卡片，每个方法包含：编号、中英文名、类型、数据类型、推荐理由、执行顺序建议。

### Python API
```python
from udm import UDMSkill
skill = UDMSkill("产品名称")
result = skill.recommend_methods("了解用户需求", phase=1, resource_level="moderate")
print(result)
```

---

## 执行能力二：访谈提纲生成

当用户需要做用户访谈、深度访谈、脉络访查时，按以下流程执行：

### 输入要求
向用户收集：访谈目的、产品/服务名称、目标用户群体、访谈类型（脉络访查/半结构化/阶梯法/关键事件法/引导性叙事）

### 执行步骤

**第一步：确定访谈类型**
- 脉络访查（Contextual Inquiry）→ 在用户实际使用环境中边观察边提问
- 半结构化访谈 → 有预设问题但允许自由探索
- 阶梯法（Laddering）→ 从表面偏好追问到深层价值观
- 关键事件法 → 聚焦印象深刻的正面/负面体验
- 引导性叙事 → 让用户完整讲述一段经历

**第二步：生成问题列表**
根据访谈类型自动生成对应的问题模板，包含：
- 开场暖场话术（建立信任、说明录音、消除压力）
- 核心问题列表（按维度分组，标注优先级）
- 追问探针（当受访者回答模糊时的深入追问）
- 结束语（收尾、补充、感谢）

**第三步：输出访谈指南**
附加执行建议：建议时长、关键追问技巧、非语言线索观察要点、录音/记录建议。

### 访谈技巧要点
- 问做过什么而非想要什么（揭示偏好 > 陈述偏好）
- 多用"能举个例子吗？"追问具体细节
- 注意非语言线索：表情、语调、肢体语言
- 保持沉默——给受访者思考和回忆的时间
- 记录原始语言（Verbatim），不要过早解读

### Python API
```python
from udm import UDMSkill
skill = UDMSkill("飞猪旅行")
guide = skill.generate_interview("用户访谈", "contextual", context="酒店预订体验")
print(guide)
```

---

## 执行能力三：观察记录与行为分析

当用户需要做用户观察、田野调查、行为分析时，按以下流程执行：

### 输入要求
向用户收集：观察目的、观察场景、观察类型（隐蔽观察/参与观察/影形/行为地图）

### 执行步骤

**第一步：选择观察方法**
- 隐蔽观察（Fly-on-the-Wall）→ 不参与，在自然环境中观察
- 参与观察 → 融入用户群体，亲身体验
- 影形（Shadowing）→ 跟随用户完整经历一段体验
- 行为地图 → 在平面图上标注行为位置和频率

**第二步：生成AEIOU观察框架**
为每次观察生成结构化记录模板：
- A（Activities）— 活动：用户正在做什么任务？
- E（Environments）— 环境：活动发生的场景特征？
- I（Interactions）— 交互：人与人、人与物的交互？
- O（Objects）— 物品：使用了哪些工具/物品？
- U（Users）— 用户：参与者的角色和态度？

**第三步：输出观察记录表**
包含：时间戳、AEIOU分类、观察内容、情绪标注、即时洞察。

### Python API
```python
from udm import UDMSkill
skill = UDMSkill("飞猪旅行")
template = skill.generate_aeiou_template()
obs = skill.generate_observation("门店观察", "shadowing", setting="旅行社门店")
print(obs)
```

---

## 执行能力四：可用性测试与评估

当用户需要做可用性测试、启发性评估、专家评审时，按以下流程执行：

### 输入要求
向用户收集：产品名称、测试类型（形成性/总结性/比较/RITE快速迭代）、测试任务描述

### 执行步骤

**第一步：确定测试类型**
- 形成性测试 → 设计过程中发现问题（5-8人）
- 总结性测试 → 评估最终产品可用性（15-20人）
- 比较测试 → 比较不同方案或竞品（10-15人/组）
- RITE快速迭代 → 测试-修改-再测试循环（每轮3-5人）

**第二步：生成测试脚本**
包含：研究目标、测试任务（含场景描述和成功标准）、主持人脚本（开场/结束）、难度评级。

**第三步：启发性评估（尼尔森十大原则）**
生成检查清单，逐项评估：
1. 系统状态可见性
2. 系统与现实世界的匹配
3. 用户控制和自由
4. 一致性和标准
5. 错误预防
6. 识别而非回忆
7. 使用的灵活性和效率
8. 美观和简约设计
9. 帮助用户识别、诊断和恢复错误
10. 帮助和文档

**第四步：SUS可用性量表计算**
输入10个问题的1-5分评分，自动计算SUS总分(0-100)并解读：
- 80.3+：A级优秀
- 68+：B级良好
- 51+：C级一般
- 25+：D级较差
- <25：F级极差

**第五步：严重性评级**
对发现的问题按严重性分级：
- 4级：灾难性 — 必须立即修复
- 3级：严重 — 应优先修复
- 2级：轻微 — 应安排修复
- 1级：装饰性 — 有时间再修

### Python API
```python
from udm import UDMSkill
skill = UDMSkill("飞猪App")
test = skill.generate_usability_test("预订流程测试", "formative")
checklist = skill.generate_heuristic_checklist()
sus = skill.calculate_sus([4,2,5,1,4,2,5,1,4,2])
print(sus)  # {'score': '82.5', 'grade': 'A', 'adjective': '优秀', ...}
```

---

## 执行能力五：问卷与量表设计

当用户需要做问卷调查、量表测量时，按以下流程执行：

### 输入要求
向用户收集：研究目的、问卷类型（卡诺/语义差异/NPS/SUS/期望值测试）、目标功能或产品

### 执行步骤

**第一步：确定问卷类型**
- 卡诺问卷（Kano）→ 分析功能需求类型（基本/期望/兴奋/无关/反向）
- 语义差异量表 → 测量用户对产品的主观感知（7级两极量表）
- NPS净推荐值 → 衡量用户忠诚度（0-10分推荐意愿）
- SUS系统可用性量表 → 快速评估整体可用性（10个标准问题）
- 期望值测试 → 使用产品反应卡测量情感反应

**第二步：自动生成问卷**
根据类型生成完整问卷，包含：题目、选项、量表标签、预计填写时长。

**第三步：数据分析**
- 卡诺分析：根据功能型+反功能型回答自动分类需求
- NPS计算：自动计算推荐者/被动者/贬损者占比和NPS分数
- SUS计算：自动计算可用性得分并给出等级

### Python API
```python
from udm import UDMSkill
skill = UDMSkill("飞猪旅行")
# 卡诺问卷
survey = skill.generate_survey("功能需求调研", "kano", features=["智能推荐", "价格日历"])
# NPS计算
nps = skill.calculate_nps([9,10,8,7,10,6,9,8,10,5])
print(nps)  # {'nps': 30.0, 'level': '良好', ...}
```

---

## 执行能力六：综合分析（亲和图/角色画像/体验历程图/Elito/加权矩阵）

当用户需要整理研究数据、构建用户画像、绘制体验历程时，按以下流程执行：

### 6A. 亲和图（Affinity Diagramming）

**执行步骤：**
1. 将所有数据点录入（每条一个观察/引用/发现）
2. 团队默默将相似数据分组（不预设分类）
3. 为每个分组命名（描述性标题）
4. 识别分组间的关系和层级
5. 标注关键洞察和意外发现

### 6B. 角色画像（Personas）

**执行步骤：**
1. 收集用户人口统计信息（姓名、年龄、职业）
2. 填写个人简介和背景故事
3. 列出目标与动机
4. 列出痛点与挫折
5. 描述行为模式和技术水平
6. 添加代表性引用语
7. 描述典型使用场景

**注意：** 基于真实研究数据，不要凭空想象。3-5个角色为宜。

### 6C. 体验历程图（Journey Map）

**执行步骤：**
1. 确定角色和场景
2. 划分体验阶段
3. 每个阶段记录：行为、接触点、想法、情绪(1-5)、痛点、机会
4. 绘制情绪曲线
5. 标注关键时刻（Moments of Truth）
6. 识别"痛点-机会"配对

### 6D. Elito方法

**执行步骤：**
从观察到概念的五步转化：
1. 观察（Observation）— 原始数据
2. 判断（Judgment）— 解读含义
3. 价值（Value）— 用户价值
4. 概念（Concept）— 设计方案
5. 关键隐喻（Key Metaphor）— 核心概念

### 6E. 加权矩阵（Weighted Matrix）

**执行步骤：**
1. 定义评估标准及权重（如：用户满意度30%、开发成本25%等）
2. 为每个候选方案在每个标准上打分(1-5)
3. 计算加权总分
4. 按总分排序，输出推荐方案

### Python API
```python
from udm import UDMSkill
skill = UDMSkill("飞猪旅行")

# 体验历程图
jm = skill.build_journey_map("酒店预订体验", persona="商旅用户小李")
jm.add_stage("搜索", actions=["打开App"], emotions=4, pain_points=["排序不合理"])
jm.add_stage("比价", actions=["切换多个App"], emotions=2, pain_points=["太耗时"])
from udm import JourneyMapBuilder
print(JourneyMapBuilder.render_markdown(jm.build()))

# 加权矩阵
wm = skill.build_weighted_matrix("方案评估")
wm.add_criterion("用户满意度", weight=0.3)
wm.add_criterion("开发成本", weight=0.3)
wm.add_criterion("创新性", weight=0.4)
wm.add_option("方案A", {"用户满意度": 4, "开发成本": 3, "创新性": 5})
wm.add_option("方案B", {"用户满意度": 5, "开发成本": 2, "创新性": 3})
print(wm.render_markdown())
```

---

## 执行能力七：研究计划生成

当用户需要制定研究计划、规划研究项目时，按以下流程执行：

### 输入要求
向用户收集：项目名称、研究背景、核心研究问题、可用资源和时间

### 执行步骤

**第一步：明确研究目标**
将研究问题转化为可执行的研究目标，区分主要目标和次要目标。

**第二步：选择研究方法**
使用执行能力一的方法推荐引擎，为每个目标选择合适的方法。

**第三步：参与者规划**
确定：招募标准、样本量、招募渠道。

**第四步：时间规划**
输出甘特图式的时间表：准备→执行→分析→报告。

**第五步：预算估算**
列出预算项目：参与者报酬、场地费、工具费、差旅费等。

**第六步：风险评估**
识别潜在风险并制定应对措施。

### Python API
```python
from udm import UDMSkill
skill = UDMSkill("飞猪旅行")
plan = skill.generate_research_plan("酒店预订体验研究", background="用户反馈预订流程复杂")
plan.add_objective("了解用户预订酒店的核心痛点", priority=1)
plan.add_method(48, "访谈", "深入了解用户动机", participants=10, days=5)
plan.add_method(94, "可用性测试", "评估现有流程", participants=8, days=3)
plan.add_timeline_item("准备", "招募与材料准备", "1周", "招募完成")
plan.add_risk("招募困难", "扩大招募渠道，提高报酬")
from udm import ResearchPlanBuilder
print(ResearchPlanBuilder.render_markdown(plan.build()))
```

---

## 执行能力八：研究报告生成

当用户需要撰写研究报告、输出研究成果时，按以下流程执行：

### 输入要求
向用户收集：项目名称、使用的研究方法、参与人数、关键发现

### 执行步骤

**第一步：执行摘要**
用2-3句话概括最重要的发现和建议。

**第二步：研究概述**
说明研究方法、参与者、时间周期。

**第三步：关键发现**
按严重性排列发现，每个发现包含：标题、描述、证据、建议。
- 🔴 严重（severity=4）
- 🟠 重要（severity=3）
- 🟡 中等（severity=2）
- 🟢 轻微（severity=1）

**第四步：设计建议**
按优先级分三层输出：
- 优先级高：立即行动
- 优先级中：计划执行
- 优先级低：持续关注

### Python API
```python
from udm import UDMSkill
skill = UDMSkill("飞猪旅行")
report = skill.generate_report("酒店预订体验研究报告", summary="本次研究发现...")
report.add_finding("比价困难", "用户需要在多个平台间切换", severity=3,
                   recommendation="增加一键比价功能")
report.add_high_recommendation("优化搜索结果排序算法")
from udm import ReportBuilder
print(ReportBuilder.render_markdown(report.build()))
```

---

## 使用触发条件

当用户的请求涉及以下关键词或场景时，自动激活对应的执行能力：

| 触发词/场景 | 激活的执行能力 |
|------------|--------------|
| 方法推荐、研究策略、选什么方法、怎么做研究 | 执行能力一 |
| 访谈提纲、访谈问题、用户访谈、脉络访查、深度访谈 | 执行能力二 |
| 观察记录、田野调查、行为观察、AEIOU、影形 | 执行能力三 |
| 可用性测试、启发性评估、SUS、尼尔森、专家评审 | 执行能力四 |
| 问卷、量表、卡诺、NPS、语义差异、期望值测试 | 执行能力五 |
| 亲和图、角色画像、体验历程图、Elito、加权矩阵 | 执行能力六 |
| 研究计划、研究方案、研究规划 | 执行能力七 |
| 研究报告、洞察报告、发现总结 | 执行能力八 |
| 设计研究、用户研究、UX研究 | 综合运用一+二+七 |
| 产品评估、体验优化 | 综合运用四+六+八 |

---

## Python 工具包

Skill 提供完整的 Python API，位于 `udm/` 包目录下，可直接导入使用。

### 核心模块

| 模块 | 类/函数 | 用途 |
|------|---------|------|
| `config.py` | `AnalysisConfig`, `METHODS_INDEX` | 100种方法索引、设计阶段、尼尔森原则、SUS量表 |
| `utils.py` | `load_knowledge`, `search_methods`, `filter_methods` | 知识库加载、方法搜索与筛选 |
| `templates.py` | 模板常量 | 访谈问题、AEIOU框架、可用性指标、问卷模板 |
| `interview.py` | `InterviewBuilder` | 访谈框架生成器（5种访谈类型） |
| `observation.py` | `ObservationBuilder` | 观察记录生成器（AEIOU框架、行为地图） |
| `usability.py` | `UsabilityTestBuilder`, `HeuristicEvaluator` | 可用性测试脚本、启发性评估、SUS计算 |
| `survey.py` | `SurveyBuilder`, `calculate_nps` | 问卷生成器（卡诺/语义差异/NPS/SUS/期望值） |
| `synthesis.py` | `AffinityDiagramBuilder`, `PersonaBuilder`, `JourneyMapBuilder`, `ElitoAnalyzer`, `WeightedMatrixBuilder` | 综合分析工具集 |
| `recommender.py` | `MethodRecommender` | 方法推荐引擎（三角测量原则） |
| `research_plan.py` | `ResearchPlanBuilder` | 研究计划生成器 |
| `report.py` | `ReportBuilder` | 研究报告生成器 |

### 统一入口

```python
import sys
sys.path.insert(0, "/path/to/universal-design-methods-skill")
from udm import UDMSkill

skill = UDMSkill("我的产品")

# 所有能力一站式调用
result = skill.recommend_methods("了解用户需求", phase=1)
guide = skill.generate_interview("用户访谈", "contextual")
obs = skill.generate_observation("门店观察", "shadowing")
test = skill.generate_usability_test("流程测试", "formative")
survey = skill.generate_survey("需求调研", "kano", features=["功能A"])
checklist = skill.generate_heuristic_checklist()
sus = skill.calculate_sus([4,2,5,1,4,2,5,1,4,2])
nps = skill.calculate_nps([9,10,8,7,10,6,9,8,10,5])
methods = skill.list_methods(phase=1, purpose="exploration")
info = skill.search_knowledge("可用性")
```

## 知识库文件

知识库 Markdown 文档位于项目根目录，包含：
- `methods-exploration.md` — 探索性研究方法详解
- `methods-generative.md` — 衍生性研究方法详解
- `methods-evaluative.md` — 评估性研究方法详解
- `methods-synthesis.md` — 综合分析方法详解
- `methods-communication.md` — 成果沟通与其他方法详解
- `execution-templates.md` — 执行模板集
- `decision-framework.md` — 决策框架与速查索引
