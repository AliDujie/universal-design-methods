---
name: universal-design-methods
description: >
  通用设计方法(UDM)执行技能。具备100种设计研究方法的知识查询、方法推荐、
  访谈提纲生成、观察记录、可用性测试、问卷设计、综合分析（亲和图/角色画像/体验历程图）、
  研究计划与报告生成等完整执行能力。
author: "渡劫"
version: "2.0.0"
---

# 通用设计方法 (Universal Design Methods) 执行技能

基于《通用设计方法》(贝拉·马丁 & 布鲁斯·汉宁顿) 的100种设计研究方法工具包。本Skill不仅提供方法知识，更具备直接执行能力——可以推荐方法组合、生成访谈提纲、创建观察记录、设计可用性测试、生成问卷量表、构建角色画像与体验历程图、输出研究计划与报告。

## 核心框架

**设计五阶段模型：**
1. 规划与定义（Planning & Scoping）— 探索和定义项目边界
2. 探索与综合（Exploration & Synthesis）— 推断设计影响
3. 概念生成（Concept Generation）— 衍生性设计活动
4. 评估与细化（Evaluation & Refinement）— 评估、细化和生产
5. 启动与监控（Launch & Monitoring）— 全程审查与修正

**三角测量原则：** 任何研究都应组合至少2-3种方法，混合定性与定量数据，从多个角度验证发现。

---

## 执行能力一：智能方法推荐

当用户需要选择研究方法、制定研究策略时：收集研究目标、当前设计阶段(1-5)、可用资源(最小/中等/充足)、数据偏好(定性/定量/混合)。将需求映射为标准目标（了解用户需求/探索行为/评估可用性/测试原型/信息架构/竞品分析/创意发散/数据驱动），按资源级别筛选方法数量，确保三角测量验证（至少一种定性+一种定量），按探索-衍生-评估-综合逻辑排列执行顺序。

**API:** `skill.recommend_methods("了解用户需求", phase=1, resource_level="moderate")`

## 执行能力二：访谈提纲生成

支持5种访谈类型：脉络访查(contextual)、半结构化(semi_structured)、阶梯法(laddering)、关键事件法(critical_incident)、引导性叙事(directed_storytelling)。自动生成开场暖场话术、核心问题列表（按维度分组标注优先级）、追问探针、结束语，并附加执行建议。

**API:** `skill.generate_interview("用户访谈", "contextual", context="酒店预订体验")`

## 执行能力三：观察记录与行为分析

支持4种观察类型：隐蔽观察(fly_on_wall)、参与观察(participant)、影形(shadowing)、行为地图(behavioral_mapping)。生成AEIOU观察框架（Activities/Environments/Interactions/Objects/Users）和结构化记录表。

**API:** `skill.generate_observation("门店观察", "shadowing", setting="旅行社门店")`

## 执行能力四：可用性测试与评估

支持形成性/总结性/比较/RITE测试类型。生成测试脚本（含场景描述和成功标准）、尼尔森十大启发性评估检查清单、SUS可用性量表计算(0-100分+等级)、严重性评级(0-4级)。

**API:**
```python
test = skill.generate_usability_test("预订流程测试", "formative")
checklist = skill.generate_heuristic_checklist()
sus = skill.calculate_sus([4,2,5,1,4,2,5,1,4,2])   # {'score': '85.0', 'grade': 'A'}
nps = skill.calculate_nps([9,10,8,7,10,6,9,8,10,5]) # {'nps': 30.0, 'level': '良好'}
```

## 执行能力五：问卷与量表设计

支持卡诺(kano)、语义差异(semantic_differential)、NPS、SUS、期望值测试(desirability)。自动生成完整问卷（题目+选项+量表标签+预计填写时长），并计算卡诺分类、NPS分数。

**API:** `skill.generate_survey("功能需求调研", "kano", features=["智能推荐", "价格日历"])`

## 执行能力六：综合分析

包含5个分析工具：亲和图(AffinityDiagramBuilder)、角色画像(PersonaBuilder)、体验历程图(JourneyMapBuilder)、Elito方法(ElitoAnalyzer)、加权矩阵(WeightedMatrixBuilder)。

**API:**
```python
jm = skill.build_journey_map("酒店预订体验", persona="商旅用户小李")
jm.add_stage("搜索", actions=["打开App"], emotions=4, pain_points=["排序不合理"])
jm.add_stage("比价", actions=["切换多个App"], emotions=2, pain_points=["太耗时"])
print(JourneyMapBuilder.render_markdown(jm.build()))

wm = skill.build_weighted_matrix("方案评估")
wm.add_criterion("用户满意度", weight=0.3)
wm.add_option("方案A", {"用户满意度": 4})
print(wm.render_markdown())
```

## 执行能力七：研究计划生成

收集项目名称、研究背景、核心研究问题、可用资源和时间，输出完整研究计划（目标、方法选择、参与者规划、时间表、预算、风险评估）。

**API:**
```python
plan = skill.generate_research_plan("酒店预订体验研究", background="用户反馈预订流程复杂")
plan.add_objective("了解用户预订酒店的核心痛点", priority=1)
plan.add_method(48, "访谈", "深入了解用户动机", participants=10, days=5)
print(ResearchPlanBuilder.render_markdown(plan.build()))
```

## 执行能力八：研究报告生成

输出结构化研究报告：执行摘要、研究概述、关键发现（按严重性分级）、设计建议（按优先级三层输出）。

**API:**
```python
report = skill.generate_report("酒店预订体验研究报告", summary="发现3个核心痛点")
report.add_finding("比价困难", "需要切换多个平台", severity=3, recommendation="一键比价")
print(ReportBuilder.render_markdown(report.build()))
```

---

## 触发条件

| 触发词/场景 | 激活能力 |
|------------|---------|
| 方法推荐、研究策略、选什么方法 | 能力一 |
| 访谈提纲、用户访谈、脉络访查 | 能力二 |
| 观察记录、田野调查、AEIOU、影形 | 能力三 |
| 可用性测试、启发性评估、SUS、尼尔森 | 能力四 |
| 问卷、量表、卡诺、NPS、语义差异 | 能力五 |
| 亲和图、角色画像、体验历程图、Elito、加权矩阵 | 能力六 |
| 研究计划、研究方案 | 能力七 |
| 研究报告、洞察报告 | 能力八 |
| 设计研究、用户研究、UX研究 | 综合运用一+二+七 |
| 产品评估、体验优化 | 综合运用四+六+八 |

## Python 工具包

统一入口：
```python
from udm import UDMSkill
skill = UDMSkill("我的产品")
```

核心模块：`config.py`(100种方法索引) / `utils.py`(知识库搜索) / `templates.py`(执行模板) / `interview.py`(访谈生成器) / `observation.py`(观察记录) / `usability.py`(可用性测试+SUS) / `survey.py`(问卷生成+卡诺+NPS) / `synthesis.py`(亲和图/画像/历程图/Elito/矩阵) / `recommender.py`(方法推荐引擎) / `research_plan.py`(研究计划) / `report.py`(研究报告)

## 知识库

知识文档位于 `references/` 目录，包含：

- `methods-exploration.md` — 探索性研究方法详解 (→ 关联: 能力一/二/三)
- `methods-generative.md` — 衍生性研究方法详解 (→ 关联: 能力一/六)
- `methods-evaluative.md` — 评估性研究方法详解 (→ 关联: 能力四/五)
- `methods-synthesis.md` — 综合分析方法详解 (→ 关联: 能力六)
- `methods-communication.md` — 成果沟通与其他方法详解 (→ 关联: 能力七/八)
- `execution-templates.md` — 执行模板集 (→ 关联: 全部能力)
- `decision-framework.md` — 决策框架与速查索引 (→ 关联: 能力一)
