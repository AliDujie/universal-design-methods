---
name: universal-design-methods
description: >
  通用设计方法(UDM)执行技能。具备100种设计研究方法的知识查询、方法推荐、
  访谈提纲生成、观察记录、可用性测试、问卷设计、综合分析（亲和图/角色画像/体验历程图）、
  研究计划与报告生成等完整执行能力，以及CEO决策视角的研究方法ROI评估、决策产出说明与资源分配建议。
author: "渡劫"
version: "2.3.2"
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

支持4种观察类型：隐蔽观察(fly_on_wall)、参与观察(participant)、影随(shadowing)、行为地图(behavioral_mapping)。生成AEIOU观察框架（Activities/Environments/Interactions/Objects/Users）和结构化记录表。

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
| 研究 ROI、投入产出、方法评估 | CEO: 方法 ROI 评估 |
| 决策产出、研究价值、CEO 报告 | CEO: 预期决策产出 |
| 资源分配、预算、人力规划 | CEO: 资源分配建议 |
| 综合研究 + 决策 | 综合运用 + CEO 视角 |

## CEO 决策视角

在研究计划或报告生成后，自动附加商业决策支持分析：

**能力九：研究方法 ROI 评估** — 为推荐的研究方法计算投入产出比，按 ROI 评分排序，输出投资建议和 P0/P1/P2 优先级。帮助 CEO 理解每种研究方法的价值。

**API:** `skill.add_method_roi(methods)` — methods 可选，默认使用通用方法基线。

**能力十：预期决策产出** — 明确研究完成后 CEO 可获得的决策依据：问题诊断、量化数据、用户洞察、机会识别、验证报告，以及各阶段关键决策点。

**API:** `skill.generate_decision_outputs("如何提升预订转化率？")`

**能力十一：资源分配建议** — 为研究项目提供预算分配（研究执行40%/用户招募15%/工具10%/分析报告20%/应急15%）、人力分配、时间分配和资源风险评估。

**API:** `skill.generate_resource_allocation({"total": 500000, "headcount": 5, "timeline": "8 周"})`

**默认行为**: 当生成研究计划（能力七）或研究报告（能力八）时，自动附加 CEO 决策视角的 ROI 评估和资源分配建议。

## Python 工具包

统一入口：
```python
from udm import UDMSkill
skill = UDMSkill("我的产品")
```

核心模块：`config.py`(100种方法索引) / `utils.py`(知识库搜索) / `templates.py`(执行模板) / `interview.py`(访谈生成器) / `observation.py`(观察记录) / `usability.py`(可用性测试+SUS) / `survey.py`(问卷生成+卡诺+NPS) / `synthesis.py`(亲和图/画像/历程图/Elito/矩阵) / `recommender.py`(方法推荐引擎) / `research_plan.py`(研究计划) / `report.py`(研究报告)

### UDMSkill 方法一览

| 方法 | 能力 | 必填参数 | 返回 |
|------|------|---------|------|
| `recommend_methods()` | 智能方法推荐 | goal | Markdown |
| `generate_interview()` | 访谈提纲 | title, interview_type | Markdown |
| `generate_observation()` | 观察记录 | title, obs_type | Markdown |
| `generate_usability_test()` | 可用性测试 | title, test_type | Markdown |
| `generate_heuristic_checklist()` | 启发性评估 | — | Markdown |
| `calculate_sus()` | SUS 评分 | responses | Dict |
| `calculate_nps()` | NPS 评分 | responses | Dict |
| `generate_survey()` | 问卷设计 | title, survey_type | Markdown |
| `generate_research_plan()` | 研究计划 | title | PlanBuilder |
| `generate_report()` | 研究报告 | title | ReportBuilder |
| `search_knowledge()` | 知识检索 | keyword | Dict |
| `add_method_roi()` | CEO: 方法 ROI | methods(可选) | Markdown |
| `generate_decision_outputs()` | CEO: 决策产出 | research_question(可选) | Markdown |
| `generate_resource_allocation()` | CEO: 资源分配 | budget(可选) | Markdown |

### AI Agent 调用规则

| # | 规则 | 说明 |
|---|------|------|
| 1 | **统一入口** | 始终通过 `UDMSkill` 类调用，不直接实例化子模块 |
| 2 | **返回值** | 所有方法返回 Markdown 字符串，可直接展示 |
| 3 | **触发映射** | 根据用户意图选择对应能力（参见触发条件表） |
| 4 | **三角测量** | 组合至少 2-3 种方法，混合定性与定量 |
| 5 | **知识优先** | 方法论问题先调用 `search_knowledge()` 查询 |
| 6 | **CEO 决策默认附加** | 生成研究计划或报告时，自动附加 ROI 评估 + 资源分配建议 |
| 7 | **完整交付** | 每个任务产出完整可用的计划/报告/建议 |

## 知识库

知识文档位于 `references/` 目录，包含：

- `methods-exploration.md` — 探索性研究方法详解 (→ 关联: 能力一/二/三)
- `methods-generative.md` — 衍生性研究方法详解 (→ 关联: 能力一/六)
- `methods-evaluative.md` — 评估性研究方法详解 (→ 关联: 能力四/五)
- `methods-synthesis.md` — 综合分析方法详解 (→ 关联: 能力六)
- `methods-communication.md` — 成果沟通与其他方法详解 (→ 关联: 能力七/八)
- `execution-templates.md` — 执行模板集 (→ 关联: 全部能力)
- `decision-framework.md` — 决策框架与速查索引 (→ 关联: 能力一)

## 与其他 Skill 协作

UDM 是 AliDujie UX 研究技能生态系统的方法论核心：

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| UDM + JTBD | JTBD Knowledge | UDM 访谈方法挖掘用户 Job → JTBD 四力分析 → JTBD 机会评分 |
| UDM + QuantUX | Quantitative UX Research | UDM 定性发现 → QuantUX 定量验证 → UDM 综合报告 |
| UDM + VPD | Value Proposition Design | UDM 用户研究 → VPD 画布填充 → VPD 实验验证 |
| UDM + Persona | Web Persona | UDM 访谈/观察 → Persona 数据收集 → Persona 质量评审 |
| UDM + SWD | Storytelling with Data | UDM 研究发现 → SWD 图表选择 → SWD 数据故事构建 |
| UDM + STM | Structured Thinking Model | STM 分析框架 → UDM 研究方法匹配 → STM 决策建议 |

**协作示例（UDM → SWD）**：
```python
# Step 1: UDM 生成研究报告
from udm import UDMSkill
udm = UDMSkill("电商体验")
report = udm.generate_report("用户研究报告", summary="发现3个核心痛点")
# Step 2: SWD 将研究发现可视化
from swd import SWDSkill
swd = SWDSkill("用户体验汇报")
ctx = swd.build_context(audience="CEO", cta="批准体验优化预算")
chart = swd.recommend_chart(data_type="categorical", category_count=3)
```

**协作示例（UDM → JTBD → VPD 端到端）**：
```python
# Step 1: UDM 定性研究收集用户洞察
udm = UDMSkill("旅行预订")
interview = udm.generate_interview("商务用户访谈", "contextual", context="出差预订")
# Step 2: JTBD 分析核心 Jobs 和机会分数
from jtbd import JTBDSkill
jtbd = JTBDSkill("旅行预订平台")
# Step 3: VPD 填充画布并验证
from vpd import VPDSkill
vpd = VPDSkill("旅行预订", "商务人士")
```
