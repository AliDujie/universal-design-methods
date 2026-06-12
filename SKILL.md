---
name: universal-design-methods
description: >
  通用设计方法(UDM)执行技能。具备100种设计研究方法的知识查询、方法推荐、
  访谈提纲生成、观察记录、可用性测试、问卷设计、综合分析（亲和图/角色画像/体验历程图）、
  研究计划与报告生成等完整执行能力，以及CEO决策视角的研究方法ROI评估、决策产出说明与资源分配建议。
author: "渡劫"
version: "2.4.59"
---

# 通用设计方法 (Universal Design Methods) 执行技能

基于《通用设计方法》(贝拉·马丁 & 布鲁斯·汉宁顿) 的100种设计研究方法工具包。本Skill不仅提供方法知识，更具备直接执行能力——可以推荐方法组合、生成访谈提纲、创建观察记录、设计可用性测试、生成问卷量表、构建角色画像与体验历程图、输出研究计划与报告。

## 🌐 AliDujie 技能生态系统

UDM 是 **方法论核心**——覆盖从探索到交付的完整研究生命周期：

```
┌─────────────────────────────────────────────────────────────┐
│                    AliDujie UX Research Ecosystem            │
│                                                             │
│   ┌──────────────┐                                          │
│   │   Persona    │ 👤 用户定义层 — 创建证据驱动的人物角色      │
│   └──────┬───────┘                                          │
│          │ 研究数据                                           │
│   ┌──────▼───────┐    ┌──────────────┐                      │
│   │  JTBD Skill  │◄──►│ UDM 本技能   │ 📖 方法论核心 — 100种 │
│   └──────┬───────┘    └──────┬───────┘    设计研究方法       │
│          │ 需求洞察           │ 定性发现                      │
│   ┌──────▼───────┐    ┌──────▼───────┐                      │
│   │  VPD Skill   │◄──►│  QuantUX     │ 📊 定量研究 — HEART/  │
│   └──────┬───────┘    └──────┬───────┘    A-B/MaxDiff        │
│          │ 价值主张           │ 定量验证                      │
│          └──────────┬────────┘                               │
│                     │ 研究发现                                │
│              ┌──────▼───────┐                                │
│              │  SWD Skill   │ 📈 数据叙事 — 数据可视化与汇报    │
│              └──────┬───────┘                                │
│                     │ 数据洞察                                │
│              ┌──────▼───────┐                                │
│              │  STM Skill   │ 🧠 战略分析 — 商业框架与决策      │
│              └──────────────┘                                │
│                                                             │
│  工作流: Persona → JTBD/UDM → QuantUX → VPD → SWD → STM    │
└─────────────────────────────────────────────────────────────┘
```

**UDM 的典型协作**：UDM 推荐方法并执行研究 → JTBD 结构化分析 Jobs → QuantUX 定量验证 → VPD 价值画布 → SWD 数据汇报 → STM 战略决策

## 🌟 为什么选择 UDM？

- **100 种方法全覆盖** — 从探索到沟通，一站式解决所有研究方法需求，无需拼接多个工具
- **11 大执行能力** — 不只是知识库，而是能直接产出访谈提纲、测试脚本、问卷、历程图、研究报告的实战工具
- **智能三角测量** — 自动推荐 3-5 种方法组合，混合定性+定量，提升研究信度
- **零学习成本** — 纯 Python 标准库，无外部依赖，`from udm import UDMSkill` 即可使用
- **CEO 决策视角** — 自动附加 ROI 评估、资源分配建议，帮你说清研究价值
- **双语支持** — 完整中英文文档，适合国际化团队
- **生态核心** — 与 JTBD、QuantUX、Persona、VPD、SWD 等 5 个技能无缝协作，覆盖用户研究全生命周期

## 🧭 快速决策：什么时候使用 UDM？

| 你的需求 | 推荐技能 |
|---------|---------|
| 需要选择研究方法、设计访谈、执行可用性测试 | ✅ **UDM（本技能）** |
| 需要理解用户"工作"、机会评分、竞争分析 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要定量验证假设、设计 A/B 测试、计算样本量 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 需要创建人物角色、用户细分、设计指导 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 需要价值主张画布、实验验证、优先级排序 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| 需要将研究结果转化为数据叙事、图表呈现 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| 需要结构化商业分析框架 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

> 💡 UDM 是方法论核心：先选方法做研究，再用其他技能深化分析或呈现。

### 💼 为什么团队选择 UDM

| 挑战 | 没有 UDM | 使用 UDM |
|------|----------|----------|
| 研究规划 | 花数小时研究方法论 | 秒级推荐 3 种方法组合 |
| 访谈提纲 | 质量参差不齐 | 5 种结构化类型，开箱即用 |
| 可用性测试 | 临时清单，遗漏关键项 | SUS 评分 + 启发式评估内置 |
| 问卷设计 | 复制粘贴模板 | 5 种问卷类型，含卡诺/NPS |
| 研究报告 | 自由格式，遗漏关键信息 | 标准化格式 + CEO 决策支持 |

## 🧭 快速参考卡片 / Quick Reference Card

| 研究问题 / Research Question | 推荐方法 / Recommended Methods | 预期产出 / Expected Output |
|---|---|---|
| 用户为什么流失？/ Why do users churn? | 流失访谈 + NPS 问卷 + 历程图 / Exit interviews + NPS survey + Journey map | 分级痛点 + 流失因素 / Severity-ranked pain points + churn factors |
| 改版是否更好？/ Is our redesign better? | 形成性可用性测试 + SUS / Formative usability test + SUS | SUS 分数 + 等级 / SUS score + grade |
| 用户想要什么功能？/ What features do users want? | 脉络访查 + 卡诺问卷 / Contextual inquiry + Kano survey | 优先级功能列表 / Prioritized feature list |
| 我们的用户是谁？/ Who are our users? | 影随观察 + 角色画像 / Shadowing + Persona building | 证据驱动人物角色 / Evidence-driven personas |
| 用户如何完成任务？/ How do users complete tasks? | 脉络访查 + 体验历程图 / Contextual inquiry + Journey map | 可视化痛点地图 / Visual pain-point map |
| 用户能否找到所需内容？/ Can users find things? | 启发式评估 + 可用性测试 / Heuristic eval + Usability test | 严重性分级问题列表 / Severity-rated issues |

### 🔗 Ecosystem Quick Start / 生态系统快速上手

UDM 是 7 技能工作流的**方法论核心**——覆盖从探索到交付的完整研究生命周期。

```python
# Step 1: UDM 推荐研究方法
from udm import UDMSkill
udm = UDMSkill("旅行平台")
plan = udm.recommend_methods("了解用户流失原因", phase=1)

# Step 2: 生成访谈提纲
guide = udm.generate_interview("用户深访", "contextual")

# Step 3: 可用性测试 + SUS 计算
sus = udm.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])  # → 72.5 (Good)

# Step 4: 体验历程图
jm = udm.build_journey_map("预订流程", persona="用户")
```

> 💡 **Try it now / 立即尝试**:
> ```python
> from udm import UDMSkill
> skill = UDMSkill("你的产品")
> print(skill.recommend_methods("了解用户为什么流失", phase=1))
> ```

### ✅ 5 分钟快速开始检查清单

- [ ] **安装** — `cp -r universal-design-methods /your/agent/skills/`
- [ ] **导入** — `from udm import UDMSkill`
- [ ] **初始化** — `skill = UDMSkill("你的产品")`
- [ ] **方法推荐** — `skill.recommend_methods("了解用户需求", phase=1)`
- [ ] **访谈提纲** — `skill.generate_interview("用户访谈", "contextual")`
- [ ] **可用性测试** — `skill.generate_usability_test("流程测试", "formative")`
- [ ] **体验历程图** — `skill.build_journey_map("预订体验", persona="用户")`

[English](README.md#quick-start-5-minutes) | [中文](#中文说明)

> 💡 **Pro Tip — Chain JTBD Upstream / 上游串联 JTBD**:
> 先跑 **Persona → JTBD → UDM** 再开始研究。Persona 定义*谁*，JTBD 发现*未满足的 Jobs*，UDM 根据 JTBD 机会分数精准推荐方法。
> ```python
> from persona import PersonaSkill; from jtbd import JTBDSkill; from udm import UDMSkill
> p = PersonaSkill("旅行平台"); j = JTBDSkill("旅行平台"); u = UDMSkill("旅行平台")
> # JTBD 机会分数 → UDM 精准方法推荐，不再盲猜
> ```

## ⚡ 快速上手 (Quick Start)

```python
from udm import UDMSkill

skill = UDMSkill("你的产品名")

# 方法推荐 — 自动三角测量
methods = skill.recommend_methods("了解用户为什么流失", phase=1)

# 生成访谈提纲
guide = skill.generate_interview("用户深访", "contextual")

# 可用性测试 + SUS 计算
sus = skill.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])  # → 72.5 (Good)

# 体验历程图
jm = skill.build_journey_map("预订流程", persona="用户")
```

> 💡 **5 分钟上手**: `from udm import UDMSkill` → 纯标准库，零依赖，开箱即用。

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
| 观察记录、田野调查、AEIOU、影随 | 能力三 |
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

### ⛔ 何时不使用 UDM

- **纯 A/B 测试或统计分析** — 使用 [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) 做定量验证
- **创建人物角色** — 使用 [Web Persona](https://github.com/AliDujie/web-persona-skill)
- **数据可视化与叙事** — 使用 [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)
- **Jobs-to-be-Done 分析** — 使用 [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill)
- **价值主张画布** — 使用 [Value Proposition Design](https://github.com/AliDujie/value-proposition-design)
- **商业框架分析** — 使用 [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model)

## 知识库

知识文档位于 `references/` 目录，包含：

- `methods-exploration.md` — 探索性研究方法详解 (→ 关联: 能力一/二/三)
- `methods-generative.md` — 衍生性研究方法详解 (→ 关联: 能力一/六)
- `methods-evaluative.md` — 评估性研究方法详解 (→ 关联: 能力四/五)
- `methods-synthesis.md` — 综合分析方法详解 (→ 关联: 能力六)
- `methods-communication.md` — 成果沟通与其他方法详解 (→ 关联: 能力七/八)
- `execution-templates.md` — 执行模板集 (→ 关联: 全部能力)
- `decision-framework.md` — 决策框架与速查索引 (→ 关联: 能力一)

## 跨技能协作示例

UDM 与其他技能组合，覆盖用户研究全生命周期。以下是典型协作模式：

**UDM → JTBD（定性发现 → 需求洞察）**：
```python
# Step 1: UDM 做用户访谈收集原始数据
from udm import UDMSkill
udm = UDMSkill("旅行预订")
interview = udm.generate_interview("商务用户深访", "contextual", context="出差预订")
# Step 2: JTBD 将访谈发现结构化
from jtbd import JTBDSkill
jtbd = JTBDSkill("旅行预订平台")
opportunity = jtbd.score_opportunity("快速找到合适住处", struggle=4, alternative=3, market=4, budget=4)
```

**UDM → QuantUX（定性假设 → 定量验证）**：
UDM 可用性测试发现痛点 → QuantUX 设计 A/B 测试验证改进效果

**UDM → Persona（研究数据 → 角色创建）**：
UDM 访谈/观察收集行为数据 → Persona 创建证据驱动的人物角色

**UDM → VPD（用户研究 → 价值验证）**：
UDM 用户研究输出 Jobs/Pains/Gains → VPD 填充价值主张画布

**UDM → SWD（研究发现 → 数据叙事）**：
UDM 生成研究报告 → SWD 将关键发现转化为高管级数据故事

```python
# UDM → SWD 端到端示例：研究报告转数据故事
from udm import UDMSkill
from swd import SWDSkill

udm = UDMSkill("电商平台")
report = udm.generate_report("Q4 用户体验研究", summary="发现 3 个核心痛点导致 30% 流失")
report.add_finding("结账流程太复杂", "用户需要 7 步才能完成支付", severity=4, recommendation="简化为 3 步结账")

swd = SWDSkill("Q4 研究汇报")
story = swd.build_story(
    protagonist="产品决策委员会",
    imbalance="30% 用户因结账体验流失",
    call_to_action="投资 2 周时间优化结账流程",
    evidence=report.summary
)
# SWD 自动推荐合适的图表类型用于高管汇报
```

## 与其他 Skill 协作

UDM 是 AliDujie UX 研究技能生态系统的方法论核心：

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| UDM + JTBD | [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | UDM 访谈方法挖掘用户 Job → JTBD 四力分析 → JTBD 机会评分 |
| UDM + QuantUX | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | UDM 定性发现 → QuantUX 定量验证 → UDM 综合报告 |
| UDM + VPD | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | UDM 用户研究 → VPD 画布填充 → VPD 实验验证 |
| UDM + Persona | [Web Persona](https://github.com/AliDujie/web-persona-skill) | UDM 访谈/观察 → Persona 数据收集 → Persona 质量评审 |
| UDM + SWD | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | UDM 研究发现 → SWD 图表选择 → SWD 数据故事构建 |
| UDM + STM | [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | STM 分析框架 → UDM 研究方法匹配 → STM 决策建议 |

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

### 🔀 完整端到端流程：Persona → JTBD → UDM → QuantUX → VPD → SWD

一个完整的用户研究管道示例，串联全部 6 个技能：

```python
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from quantux import QuantUXSkill
from vpd import VPDSkill
from swd import SWDSkill

# 1. Persona — 定义目标用户
persona = PersonaSkill("旅行预订平台")
persona.add_persona(name="商务客", archetype="效率优先", priority="primary",
    goals=["30秒内完成酒店预订"], behaviors=["频繁出差，即时预订"],
    bio="每周出差的销售顾问")

# 2. JTBD — 发现未满足的需求
jtbd = JTBDSkill("旅行预订平台")
score = jtbd.score_opportunity("快速找到合适住处", struggle=4, alternative=3, market=4, budget=4)
# → Score: 7.6/10 — 高机会领域

# 3. UDM — 定性研究验证
udm = UDMSkill("旅行预订平台")
interview = udm.generate_interview("商务用户", "contextual", context="酒店预订")
sus = udm.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])  # SUS: 85.0, Grade A

# 4. QuantUX — 定量验证
quantux = QuantUXSkill("旅行预订平台")
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.03)
ab = quantux.analyze_ab_test("旧版", 5000, 1750, "新版", 5000, 1900)

# 5. VPD — 价值主张验证
vpd = VPDSkill("旅行预订", "商务客")
canvas = vpd.analyze_canvas(product_name="旅行预订",
    jobs=[{"description": "快速找到住处", "importance": 5}])

# 6. SWD — 高管数据故事
swd = SWDSkill("Q1 研究汇报")
story = swd.build_story(protagonist="产品委员会",
    imbalance="商务客预订体验差", call_to_action="优化一键预订")
```

## 最佳实践

| # | 原则 | 说明 |
|---|------|------|
| 1 | 三角测量 | 任何研究都应组合至少 2-3 种方法，混合定性与定量数据 |
| 2 | 阶段匹配 | 根据设计五阶段选择方法：探索期用定性，评估期用定量 |
| 3 | 资源适配 | 根据可用资源（时间/预算/人力）调整方法组合规模 |
| 4 | 迭代递进 | 从探索→生成→评估→综合，方法选择随项目推进递进 |
| 5 | CEO 视角 | 研究计划自动附加 ROI 评估和资源分配建议，辅助决策 |
| 6 | 先定性后定量 | 用 UDM 定性发现方向，再用 QuantUX 定量验证假设 |
| 7 | 知识检索优先 | 理论问题先调用 `search_knowledge()` 查询 100 种方法索引 |

## 参考资料

| 书名 | 作者 | 关键贡献 |
|------|------|---------|
| **Universal Design Methods** | Bella Martin & Bruce Hanington (2012) | 本 Skill 理论基础，100 种设计研究方法 |
| Just Enough Research | Erika Hall (2013) | 精益研究方法选择 |
| The Design of Everyday Things | Don Norman (2013) | 可用性评估原则 |
| Sprint | Jake Knapp (2016) | 快速设计冲刺方法 |

### AliDujie 技能生态

UDM 是 **AliDujie UX 研究技能生态系统** 的方法论核心，与其他 6 个技能协作：

| 技能 | 定位 | 协作模式 |
|------|------|---------|
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 需求洞察 | JTBD 发现 → UDM 验证 → 机会评分 |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 定量研究 | UDM 定性 → QuantUX 定量验证 |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | 用户角色 | UDM 访谈/观察 → Persona 数据收集 |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值验证 | UDM 用户研究 → VPD 画布填充 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | UDM 研究发现 → SWD 可视化汇报 |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | 战略框架 | STM 分析框架 → UDM 方法匹配 |

### 🔗 扩展生态 (Extended Ecosystem)

UDM 研究成果还可与以下管理技能结合，将用户洞察转化为战略决策：

| 扩展技能 | 协作场景 |
|---------|----------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | 研究 ROI 评估 → CEO 战略决策 |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | UDM 用户发现 → CPO 产品战略调整 |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | 用户洞察 → CMO 品牌定位与增长策略 |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | UDM 可用性/启发式发现 → CTO 技术投资优先级 |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | 研究报告 → CEO 计划审查与范围调整 |

### 💡 Pro Tip / 专业技巧
UDM 作为 AliDujie 生态系统的**方法论引擎**，其最大价值在于三角测量——当你不确定该用什么研究方法时，UDM 会自动推荐 3-5 种方法组合，并自动匹配定性+定量。推荐配合 [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) 做需求洞察、[QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) 做定量验证、[VPD](https://github.com/AliDujie/value-proposition-design) 做价值映射、[SWD](https://github.com/AliDujie/storytelling-with-data) 做数据叙事，形成端到端研究闭环。

## ❓ FAQ / 常见问题

**Q: 我应该从哪个阶段开始？**
如果是新项目，从阶段 1（规划与定义）开始。如果已经明确了研究目标，可跳到相关阶段。不带 `phase` 参数调用 `recommend_methods()` 会给出跨阶段建议。

**Q: 不用 Python 包也能用 UDM 吗？**
可以！UDM 的 `references/` 知识库包含 100 种方法的完整描述、执行模板和决策框架，全部是独立 markdown 文档，可直接阅读和应用。Python 包只是便捷的执行层。

**Q: UDM 与传统 UX 研究工具包有什么区别？**
传统工具包（如 IDEO 方法卡片）是**参考资料**，你需要手动设计访谈提纲、计算 SUS 分数。UDM 是**可执行知识**：同样的 100 种方法，打包为 Python 函数，直接产出可用文档。参考卡片 → 可运行软件。

**Q: 预算/时间有限时怎么做研究？**
最小可行研究：5-8 次情境访谈（能力二）+ 亲和图分析（能力六）+ 快速 SUS 测试（能力四）。定性 + 定量三角测量，无需完整研究周期。
快速上手：`skill.recommend_methods("了解用户痛点", phase=1, resource_level="minimal")` 返回最精简的有效组合。

**Q: UDM 和其他技能有什么区别？**
UDM 是方法论核心——帮你**选方法、做研究、出报告**。[JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) 专注 Jobs 分析，[QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) 专注统计验证，[VPD](https://github.com/AliDujie/value-proposition-design) 专注价值主张画布，[Persona](https://github.com/AliDujie/web-persona-skill) 专注用户角色创建，[SWD](https://github.com/AliDujie/storytelling-with-data) 专注数据可视化。

**Q: SUS 分数多少算好？**
SUS 分数 0-100。等级标准：A (80+)、B (68-79)、C (52-67)、D (37-51)、F (<37)。行业平均约 68 分。

**Q: UDM 可以和生态中的其他技能一起用吗？**
可以且推荐。完整工作流：[Persona](https://github.com/AliDujie/web-persona-skill) 定义用户 → UDM 推荐方法并执行研究 → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) 分析 Jobs → [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) 定量验证 → [VPD](https://github.com/AliDujie/value-proposition-design) 映射价值主张 → [SWD](https://github.com/AliDujie/storytelling-with-data) 数据故事呈现。

**Q: 我的研究项目只有 1 周时间怎么办？**
最小可行研究：3 次情境访谈（能力二）+ 亲和图分析（能力六）+ 快速 SUS 测试（能力四）。调用 `skill.recommend_methods("了解用户痛点", phase=1, resource_level="minimal")` 自动返回最精简组合。

### 📖 Recommended Learning Path / 推荐学习路径

1. **Start with the README** — Quick start + 30-second method recommendation
2. **Read USAGE.md** — Detailed workflows for all 11 capabilities with code examples
3. **Explore references/** — Deep dive into 7 method reference documents covering exploration, generation, evaluation, synthesis, and communication
4. **Try the full pipeline** — Chain all 6 AliDujie skills end-to-end (see [Ecosystem Quick Start](#-ecosystem-quick-start--生态系统快速上手))
5. **Customize via config** — Adjust AnalysisConfig for your context (see [INSTALL.md](INSTALL.md))

### 📚 Resources / 资源

- [README.md](README.md) — Full documentation
- [USAGE.md](USAGE.md) — Detailed usage guide / 详细使用指南
- [INSTALL.md](INSTALL.md) — Installation guide
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [SECURITY.md](SECURITY.md) — Security policy and responsible use
- [references/](references/) — 7 method reference documents (exploration, generative, evaluative, synthesis, communication, execution templates, decision framework)
- [udm/](udm/) — Core Python module source code
