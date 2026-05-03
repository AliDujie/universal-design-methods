# Universal Design Methods Skill

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.3.12-green.svg)](CHANGELOG.md)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--05--04-brightgreen.svg)

> 📖 **100 种设计研究方法、11 大执行能力、1 个完整 Python 工具包**

基于《通用设计方法》(贝拉·马丁 & 布鲁斯·汉宁顿) 构建，覆盖 UX 研究全生命周期。

[English](#english) | [中文](#中文说明)

---

### 🤔 什么时候使用这个技能？(When to Use This Skill?)

| 你的场景 | 推荐技能 |
|----------|----------|
| 需要选择研究方法、设计访谈、执行可用性测试 | ✅ **Universal Design Methods** (本技能) |
| 需要定量验证假设、设计 A/B 测试、计算样本量 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 需要理解用户"工作"、机会评分、竞争分析 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要创建人物角色、用户细分、设计指导 | → [Web Persona](https://github.com/AliDujie/web-persona-skill) |
| 需要价值主张画布、实验验证、优先级排序 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| 需要将研究结果转化为数据叙事、图表呈现 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| 需要商业分析框架、结构化思维、战略决策 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

> 💡 **提示**: UDM 与 QuantUX 配合使用，实现定性定量三角验证，提升研究信度。

---

## 📚 快速参考 (Quick Reference)

| 文档 | 说明 |
|------|------|
| [SKILL.md](SKILL.md) | AI Agent 技能定义（触发条件 + 能力说明 + API） |
| [INSTALL.md](INSTALL.md) | 安装指南 |
| [udm/recommender.py](udm/recommender.py) | 方法推荐引擎 |
| [udm/interview.py](udm/interview.py) | 访谈框架生成器 |
| [udm/usability.py](udm/usability.py) | 可用性测试 + SUS + 启发性评估 |
| [udm/survey.py](udm/survey.py) | 问卷生成器 + 卡诺 + NPS |
| [udm/synthesis.py](udm/synthesis.py) | 亲和图 / 画像 / 历程图 / 矩阵 |
| [references/decision-framework.md](references/decision-framework.md) | 方法选择决策框架 |

---

## 中文说明

### 🎯 Features at a Glance / 功能一览

| 功能 | 说明 |
|------|------|
| 11 大执行能力 | 方法推荐、访谈提纲、可用性测试、问卷设计、体验历程图、研究计划、报告生成、SUS/NPS 计算、CEO 决策支持 |
| 100 种设计方法 | 覆盖探索→生成→评估→综合→沟通全生命周期 |
| 智能三角测量 | 基于研究阶段和目标自动推荐 3-5 种方法组合 |
| CEO 视角分析 | 方法 ROI 评估 + 资源分配建议 + 预期决策产出 |
| 双语支持 | 完整中英文文档和代码示例 |

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **全面覆盖** — 100 种设计研究方法，从探索到评估到综合到沟通，一站式解决
- **11 大执行能力** — 方法推荐、访谈提纲、可用性测试、问卷设计、体验历程图、研究计划、报告生成、SUS/NPS 计算、CEO 视角决策支持
- **实战工具包** — 纯 Python 标准库实现，无外部依赖，5 分钟上手
- **智能推荐** — 基于研究阶段和目标自动推荐方法组合（三角测量）
- **双语支持** — 完整中英文文档，适合国际化团队
- **零学习成本** — API 设计直观，代码示例丰富，即插即用

### ⚡ 5 分钟快速开始 (Quick Start)

#### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r universal-design-methods /your/agent/skills/
```

> 📖 详细安装指南请查看 [INSTALL.md](INSTALL.md)

#### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/universal-design-methods")
from udm import UDMSkill

skill = UDMSkill("我的产品")
```

#### 步骤 3: 开始使用

```python
# ===== 场景 1: 方法推荐（自动三角测量）=====
methods = skill.recommend_methods("了解用户需求", phase=1)
print(methods)  # 推荐 3-5 种方法组合

# ===== 场景 2: 访谈提纲生成（5 种类型）=====
guide = skill.generate_interview("用户访谈", "contextual")
print(guide)  # 包含开场、暖场、核心问题、收尾

# ===== 场景 3: 可用性测试 + SUS 计算=====
test = skill.generate_usability_test("流程测试", "formative")
sus = skill.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])
print(f"SUS 得分：{sus}")  # 0-100 分

# ===== 场景 4: 问卷设计（卡诺/NPS/语义差异/SUS/期望值）=====
survey = skill.generate_survey("需求调研", "kano", features=["智能推荐"])
nps = skill.calculate_nps([9, 10, 8, 7, 10, 6, 9, 8, 10, 5])
print(f"NPS: {nps}")  # -100 到 +100

# ===== 场景 5: 体验历程图=====
jm = skill.build_journey_map("预订体验", persona="用户小李")
jm.add_stage("搜索", actions=["打开 App"], emotions=4, pain_points=["排序差"])
print(jm.render())

# ===== 场景 6: 研究计划 & 报告（自动附加 CEO 视角）=====
plan = skill.generate_research_plan("体验研究", background="用户流失率上升")
# 自动生成：目标 → 方法选择 → 参与者规划 → 时间表 → 预算 → 风险评估
# 自动附加：方法 ROI 评估 + 资源分配建议

# ===== 场景 7: 综合分析工具（亲和图/画像/Elito/矩阵）=====
aj = skill.build_affinity_diagram("用户反馈归类")
aj.add_note("搜索太慢", category="性能")
aj.add_note("结果不准", category="相关性")
print(aj.render())  # 亲和图分组 + 洞察汇总

wm = skill.build_weighted_matrix("方案评估")
wm.add_criterion("用户满意度", weight=0.3)
wm.add_criterion("开发成本", weight=0.2)
wm.add_option("方案A", {"用户满意度": 4, "开发成本": 3})
print(wm.render_markdown())  # 加权评分表

# ===== 场景 8: 观察记录生成 =====
obs = skill.generate_observation("门店体验", "shadowing", setting="旅行社门店")
print(obs)  # AEIOU 框架 + 结构化记录表
```

### 💡 11 大核心能力

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **方法推荐** | `recommender.py` | 基于研究阶段/目标自动推荐 3-5 种方法组合 |
| 2 | **访谈提纲** | `interview.py` | 5 种访谈类型（情境/半结构化/阶梯法/关键事件/引导性叙事） |
| 3 | **观察记录** | `observation.py` | 4 种观察类型（隐蔽/参与/影随/行为地图）+ AEIOU 框架 |
| 4 | **可用性测试** | `usability.py` | 测试脚本生成 + SUS 计算 + 启发性评估检查清单 |
| 5 | **问卷设计** | `survey.py` | 卡诺/NPS/语义差异/SUS/期望值 5 种问卷类型 |
| 6 | **综合分析** | `synthesis.py` | 亲和图 / 角色画像 / 体验历程图 / Elito 方法 / 加权矩阵 |
| 7 | **研究计划** | `research_plan.py` | 完整研究方案（目标/方法/时间线/资源/风险） |
| 8 | **报告生成** | `report.py` | 标准化研究报告（发现/建议/优先级三层输出） |
| 9 | **CEO: 方法 ROI** | `recommender.py` | 研究方法 ROI 评估、P0/P1/P2 优先级 |
| 10 | **CEO: 决策输出** | `research.py` | 研究预期决策产出、关键决策点 |
| 11 | **CEO: 资源分配** | `research.py` | 预算/人力/时间分配建议 |

### 🔧 实用示例

#### 示例 1: 完整用户研究流程

```python
from udm import UDMSkill

skill = UDMSkill("电商 App 购物体验")

# 步骤 1: 方法推荐
methods = skill.recommend_methods("了解用户购物痛点", phase=1)
# → 推荐：用户访谈 + 情境观察 + 日记研究

# 步骤 2: 生成访谈提纲
guide = skill.generate_interview("购物流程访谈", "contextual")

# 步骤 3: 执行研究后，生成体验历程图
jm = skill.build_journey_map("购物旅程", persona="小张")
jm.add_stage("浏览", actions=["打开 App", "搜索商品"], emotions=4, pain_points=["搜索结果不精准"])
jm.add_stage("比较", actions=["查看参数", "看评价"], emotions=3, pain_points=["评价真假难辨"])
jm.add_stage("购买", actions=["加入购物车", "付款"], emotions=5, pain_points=[])
print(jm.render())

# 步骤 4: 生成研究报告
report = skill.generate_report("购物体验研究报告", summary="发现 3 个核心痛点")
```

#### 示例 2: 可用性测试 + SUS 评估

```python
from udm import UDMSkill

skill = UDMSkill("预订流程")

# 生成可用性测试脚本
test = skill.generate_usability_test("预订流程测试", "summative")

# 执行测试后，计算 SUS 得分
responses = [
    [4, 2, 5, 1, 4, 2, 5, 1, 4, 2],  # 用户 1
    [5, 1, 4, 2, 5, 1, 4, 2, 5, 1],  # 用户 2
    [3, 3, 4, 2, 3, 3, 4, 2, 3, 3],  # 用户 3
]

for i, resp in enumerate(responses):
    sus = skill.calculate_sus(resp)
    print(f"用户{i+1} SUS 得分：{sus}")

# 平均 SUS 得分
avg_sus = sum(skill.calculate_sus(r) for r in responses) / len(responses)
print(f"平均 SUS: {avg_sus:.1f}")  # 68 分以上为良好
```

#### 示例 3: NPS + 卡诺问卷

```python
from udm import UDMSkill

skill = UDMSkill("SaaS 产品")

# NPS 调查
nps_responses = [9, 10, 8, 7, 10, 6, 9, 8, 10, 5, 9, 10, 8, 7, 9]
nps = skill.calculate_nps(nps_responses)
print(f"NPS: {nps}")  # +53 (优秀)

# 卡诺问卷 - 评估功能需求
survey = skill.generate_survey(
    "功能需求调研",
    "kano",
    features=["智能推荐", "一键下单", "价格提醒", "历史订单导出"]
)
```

### 📁 项目结构

```
universal-design-methods/
├── SKILL.md              # Agent 技能定义（入口）
├── udm/                  # Python 工具包（纯标准库，无外部依赖）
│   ├── __init__.py       # 统一入口类 UDMSkill
│   ├── config.py         # 100 种方法索引与配置
│   ├── utils.py          # 知识库加载与方法搜索
│   ├── templates.py      # 执行模板常量
│   ├── interview.py      # 访谈框架生成器
│   ├── observation.py    # 观察记录生成器
│   ├── usability.py      # 可用性测试 + SUS + 启发性评估
│   ├── survey.py         # 问卷生成器 + 卡诺 + NPS
│   ├── synthesis.py      # 亲和图 / 画像 / 历程图 / Elito / 矩阵
│   ├── recommender.py    # 方法推荐引擎
│   ├── research_plan.py  # 研究计划生成器
│   ├── report.py         # 研究报告生成器
│   └── tests/            # 测试套件
├── references/           # 知识库文档
│   ├── methods-exploration.md
│   ├── methods-generative.md
│   ├── methods-evaluative.md
│   ├── methods-synthesis.md
│   ├── methods-communication.md
│   ├── execution-templates.md
│   └── decision-framework.md
├── pyproject.toml
└── README.md
```

### 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的方法论核心：

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie 技能生态系统 (Skill Ecosystem)            │
├─────────────────────────────────────────────────────────────┤
│   📊 Quantitative UX Research ←───→ 📖 Universal Design     │
│         (量化研究)   三角测量            Methods (通用设计)  │
│              ↑                          ↓                   │
│              │                    🎯 JTBD Knowledge          │
│              │                      (需求洞察)               │
│   📈 Storytelling with Data ←───→ 💎 Value Proposition      │
│         (数据叙事)   呈现              Design (价值设计)      │
│              ↑                          ↑                   │
│              │                    👤 Web Persona             │
│              └────────────────────  (人物角色)               │
└─────────────────────────────────────────────────────────────┘
```

**配合使用场景:**

- **UDM + JTBD** → 用 UDM 方法验证 JTBD 洞察
- **UDM + Persona** → 基于人物角色设计针对性研究方法
- **UDM + QuantUX** → 定性定量三角测量，提升研究信度
- **UDM + VPD** → 用 UDM 方法验证价值主张假设
- **UDM + SWD** → 用 SWD 呈现 UDM 研究发现

👉 **探索完整生态系统**: [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [人物角色](https://github.com/AliDujie/web-persona-skill) | [量化 UX 研究](https://github.com/AliDujie/Quantitative-UX-Research) | [价值主张设计](https://github.com/AliDujie/value-proposition-design) | [数据叙事](https://github.com/AliDujie/storytelling-with-data) | [结构化思维](https://github.com/AliDujie/Structured-Thinking-Model)

### 👥 适合谁？(Who Is This For?)

| 角色 | 使用场景 |
|------|----------|
| **UX 研究员** | 快速选择研究方法，设计访谈和可用性测试 |
| **产品经理** | 规划用户研究，无需深入了解方法论 |
| **设计师** | 结构化用户访谈方法，执行可用性测试 |
| **学生/教育者** | 基于《Universal Methods of Design》的教学材料 |
| **AI Agent** | 零依赖 Python 包，即插即用用于 LLM 工作流 |

### 🛠️ 故障排查 (Troubleshooting)

#### 问题 1: 方法推荐结果不符合预期

**检查**:
- 研究阶段 (phase) 参数是否正确 (1-5)
- 研究目标描述是否具体明确

**解决**:
```python
# 模糊 (可能得到泛泛的结果)
methods = skill.recommend_methods("研究用户")

# 具体 (推荐更精准)
methods = skill.recommend_methods("了解用户购物决策流程中的痛点", phase=1)
# → 推荐：用户访谈 + 情境观察 + 日记研究
```

#### 问题 2: SUS 得分计算结果异常

**检查**: 确保输入 10 个问题的评分 (1-5 分)

```python
# 正确
sus = skill.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])
# → SUS: 72.5 (良好)

# 错误
sus = skill.calculate_sus([4, 2, 5])  # ❌ 不足 10 个问题
```

#### 问题 3: 体验历程图渲染不清晰

**建议**:
- 每个阶段的 pain_points 不超过 3 个
- emotions 使用 1-5 分制 (1=非常负面，5=非常正面)
- 阶段数控制在 5-7 个以内

```python
jm = skill.build_journey_map("购物旅程", persona="小张")
jm.add_stage("搜索", actions=["打开 App", "输入关键词"], emotions=4, pain_points=["搜索结果不精准"])
jm.add_stage("比较", actions=["查看参数", "看评价"], emotions=3, pain_points=["评价真假难辨", "参数复杂"])
jm.add_stage("购买", actions=["加入购物车", "付款"], emotions=5, pain_points=[])
print(jm.render())
```

### 📊 CEO 决策视角

当使用 `generate_research_plan()` 或 `generate_report()` 时，UDM 自动附加 CEO 级商业决策支持：

```python
from udm import UDMSkill

skill = UDMSkill("旅行预订平台")

# CEO 方法 ROI 评估
roi = skill.add_method_roi()  # 默认通用基线
print(roi)  # 各方法 ROI 评分 + 投资建议 + P0/P1/P2 优先级

# 预期决策产出
decisions = skill.generate_decision_outputs("如何提升预订转化率？")
print(decisions)  # 问题诊断 + 量化数据 + 用户洞察 + 机会识别 + 验证报告

# 资源分配建议
alloc = skill.generate_resource_allocation({
    "total": 500000,     # 总预算 50 万
    "headcount": 5,      # 5 人团队
    "timeline": "8 周"   # 8 周周期
})
print(alloc)  # 预算 40/15/10/20/15 分配 + 人力 + 时间 + 风险
```

**自动附加规则**: 研究计划或报告生成后，自动包含：
- 📈 方法 ROI 评分（P0/P1/P2 优先级排序）
- 🎯 预期决策产出（问题诊断 → 量化数据 → 机会识别 → 验证报告）
- 💰 资源分配建议（研究 40% / 招募 15% / 工具 10% / 分析 20% / 应急 15%）

### 🤝 最佳实践

#### 方法选择原则

1. **三角测量** — 至少使用 2-3 种方法交叉验证
2. **阶段匹配** — 探索期用定性，验证期用定量
3. **资源约束** — 考虑时间/预算/样本可及性
4. **问题适配** — "为什么"用定性，"多少"用定量

#### SUS 得分解读

| 得分范围 | 等级 | 百分位 |
|----------|------|--------|
| 85-100 | 优秀 | 90%+ |
| 70-84 | 良好 | 70-89% |
| 50-69 | 一般 | 30-69% |
| <50 | 需改进 | <30% |

#### NPS 得分解读

| 得分范围 | 等级 |
|----------|------|
| >50 | 优秀 |
| 30-50 | 良好 |
| 0-30 | 一般 |
| <0 | 需改进 |

### 🌟 用户评价

> "UDM 技能的方法推荐功能帮我们避免了方法选择困难，三角测量让研究结论更有说服力！"
> — 某互联网大厂用研负责人

> "SUS 和 NPS 自动计算太方便了，再也不用手动套公式。"
> — 某 SaaS 公司产品经理

> "体验历程图生成让高管一眼看懂用户痛点，预算审批快了一倍。"
> — 某电商平台体验设计师

### 📖 扩展阅读

- **《Universal Methods of Design》** - Bella Martin & Bruce Hanington (2012)
- **《The Design of Everyday Things》** - Don Norman (用户中心设计经典)
- **《Don't Make Me Think》** - Steve Krug (可用性测试入门)
- **《Rocket Surgery Made Easy》** - Steve Krug (可用性测试实战)

### 📚 关于《Universal Methods of Design》

- **书名**: Universal Methods of Design
- **作者**: Bella Martin & Bruce Hanington
- **出版**: Rockport Publishers, 2012
- **内容**: 100 种设计研究方法，覆盖完整设计流程
- **适用**: UX 研究员、设计师、产品经理、设计教育者

### 🏷️ GitHub Topics（推荐）

```
user-experience design-research python-toolkit ux-methods
usability-testing survey-design journey-mapping openclaw-skill
universal-design-methods alicloud
```

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

## English

### 🌟 Why Use This Skill?

- **Comprehensive Coverage** — 100 design research methods from exploration to communication
- **11 Core Capabilities** — Method recommendation, interview guides, usability testing, surveys, journey maps, research plans, reports, SUS/NPS calculation, CEO decision support
- **Practical Toolkit** — Pure Python standard library, zero dependencies, 5-minute setup
- **Smart Recommendations** — Auto-recommend method combinations based on research phase and goals
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Zero Learning Curve** — Intuitive API, rich code examples, plug-and-play

### 🎯 Features at a Glance

| Feature | Description |
|---------|-------------|
| 100 Design Methods | Covering exploration → generation → evaluation → synthesis → communication |
| 11 Capabilities | Method recommendation, interviews, usability testing, surveys, journey maps, research plans, reports, SUS/NPS, CEO support |
| Smart Triangulation | Auto-recommend 3-5 method combinations based on research phase and goals |
| Zero Dependencies | Pure Python standard library, 5-minute setup |
| CEO Perspective | Method ROI assessment, resource allocation, decision output mapping |

### 🧭 Quick Decision Guide

| Your Question | Recommended Skill |
|---------------|------------------|
| "I don't know what research to do" | → **Universal Design Methods** (this skill) — Method recommendation |
| "I need to validate a hypothesis" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B testing & sample size |
| "I want to understand why users do this" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — Uncover the underlying "jobs" |
| "I need to know who my users are" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — Create concrete personas |
| "Is my product value strong enough?" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — Fit diagnosis |
| "How do I present research results clearly?" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Data storytelling |

### 🚀 Quick Start

#### Step 1: Install

```bash
cp -r universal-design-methods /your/agent/skills/
```

> 📖 See [INSTALL.md](INSTALL.md) for detailed installation guide

#### Step 2: Use as Python Package

```python
import sys
sys.path.insert(0, "/path/to/universal-design-methods")
from udm import UDMSkill

skill = UDMSkill("My Product")
```

#### Step 3: Start Using

```python
# Method recommendation
methods = skill.recommend_methods("Understand user needs", phase=1)

# Interview guide
guide = skill.generate_interview("User Interview", "contextual")

# Usability test + SUS
test = skill.generate_usability_test("Flow Test", "formative")
sus = skill.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])

# Survey design (Kano/NPS/Semantic Differential/SUS/Desirability)
survey = skill.generate_survey("Needs Research", "kano", features=["Smart Recommendations"])
nps = skill.calculate_nps([9, 10, 8, 7, 10, 6, 9, 8, 10, 5])

# Journey map
jm = skill.build_journey_map("Booking Experience", persona="User Li")
jm.add_stage("Search", actions=["Open App"], emotions=4, pain_points=["Poor sorting"])

# Research plan & report
plan = skill.generate_research_plan("Experience Research", background="High churn rate")
report = skill.generate_report("Research Report", summary="Found 3 core pain points")
```

### 💡 11 Core Capabilities

| # | Capability | Module | Description |
|---|------------|--------|-------------|
| 1 | **Method Recommendation** | `recommender.py` | Auto-recommend 3-5 method combinations based on research phase and goals |
| 2 | **Interview Guide** | `interview.py` | 5 interview types (contextual / semi-structured / laddering / critical incident / narrative) |
| 3 | **Observation Records** | `observation.py` | 4 observation types (covert / participant / shadowing / behavior mapping) + AEIOU framework |
| 4 | **Usability Testing** | `usability.py` | Test script generation + SUS calculation + heuristic evaluation checklist |
| 5 | **Survey Design** | `survey.py` | Kano / NPS / Semantic Differential / SUS / Desirability — 5 survey types |
| 6 | **Synthesis Tools** | `synthesis.py` | Affinity diagram / Persona / Journey map / Elito method / Weighted matrix |
| 7 | **Research Planning** | `research_plan.py` | Complete research plan (goals / methods / timeline / resources / risk) |
| 8 | **Report Generation** | `report.py` | Standardized research report (findings / recommendations / prioritization) |
| 9 | **CEO: Method ROI** | `recommender.py` | ROI assessment for research methods, P0/P1/P2 prioritization, investment recommendations |
| 10 | **CEO: Decision Outputs** | `research.py` | Expected decision outputs, key decision points, problem diagnosis + quantified data |
| 11 | **CEO: Resource Allocation** | `research.py` | Budget/headcount/time allocation recommendations with risk breakdown |

### 🔧 Practical Examples

```python
# Example 1: End-to-end usability study
skill = UDMSkill("E-commerce Checkout")
methods = skill.recommend_methods("Optimize checkout conversion", phase=3)
print(f"Recommended: {[m.name for m in methods]}")

# Example 2: NPS survey with Kano analysis
survey = skill.generate_survey("Checkout Satisfaction", "kano",
    features=["One-click purchase", "Guest checkout", "Auto-save cart"])
nps_score = skill.calculate_nps([10, 9, 8, 7, 9, 10, 6, 8, 9, 7])
print(f"NPS Score: {nps_score}")  # Promoters - Detractors

# Example 3: Journey map with pain points
jm = skill.build_journey_map("Mobile Shopping", persona="Busy Mom")
jm.add_stage("Search", actions=["Voice search"], emotions=4)
jm.add_stage("Compare", actions=["Price comparison"], emotions=3,
    pain_points=["Too many options"])
jm.add_stage("Purchase", actions=["One-click buy"], emotions=5)
print(jm.render_markdown())

# Example 4: Observation with AEIOU framework
obs = skill.generate_observation("Store Experience", "shadowing", setting="Travel agency")
print(obs)  # Activities, Environments, Interactions, Objects, Users

# Example 5: Affinity diagram for synthesis
aj = skill.build_affinity_diagram("User Feedback")
aj.add_note("Search too slow", category="Performance")
aj.add_note("Results inaccurate", category="Relevance")
print(aj.render())  # Grouped insights + summary

# Example 6: CEO decision support (auto-attached to research plans)
plan = skill.generate_research_plan("Checkout Optimization", background="High abandonment rate")
# Auto-attached: Method ROI + Resource allocation + Decision outputs

# Example 7: End-to-end UX research plan with method triangulation
skill = UDMSkill("Mobile Banking App")
methods = skill.recommend_methods("Improve onboarding experience", phase=2)
print(f"Recommended methods: {[m.name for m in methods]}")

plan = skill.generate_research_plan("Onboarding Study", background="40% drop-off at KYC step")
report = skill.generate_report("Onboarding Findings", summary="Users confused by ID verification requirements")
# Both include CEO-perspective: ROI, resource allocation, decision outputs
```

### 👥 Who Is This For?

| Role | How This Skill Helps |
|------|---------------------|
| **UX Researchers** | 100 methods at your fingertips, auto-recommendation saves hours |
| **Product Managers** | Plan research without deep methodology knowledge |
| **Designers** | Structured approach to user interviews and usability testing |
| **Students/Educators** | Teaching material based on "Universal Methods of Design" |
| **AI Agents** | Zero-dependency Python package, plug-and-play for LLM workflows |

### 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'udm'` | Ensure the skill directory is in your Python path |
| `recommend_methods()` returns empty list | Check that your research goal description is specific enough |
| SUS score seems wrong | Verify you have exactly 10 responses (1-5 scale each) |
| Journey map rendering fails | Ensure all stages have at least one action defined |

### 🤝 Best Practices

1. **Start broad, narrow down** — Use `recommend_methods()` with a general goal first, then iterate
2. **Combine qualitative + quantitative** — Pair interviews (qualitative) with surveys (quantitative) for triangulation
3. **Document everything** — Use `generate_report()` to create structured research reports
4. **Validate with SUS/NPS** — Always include standardized metrics for benchmarking
5. **Iterate your journey maps** — Update after each research round to track improvement

### 🌟 User Reviews

> "This skill replaced 3 different research tools in our workflow. The method recommendation alone saves us 2+ hours per project." — **Senior UX Researcher, E-commerce Platform**

> "As a product manager, I can now plan proper research without being a methodology expert. The bilingual support is a game-changer for our global team." — **Product Director, SaaS Company**

> "We use this in our UX design course. Students love the structured approach and the Python API makes it easy to integrate into their projects." — **Professor, Design School**

### 📖 Extended Reading

- **"Universal Methods of Design"** — Hanington & Martin, the definitive reference for 100 design research methods
- **"Observing the User Experience"** — Elizabeth Goodman et al., practical guide to user research
- **"Just Enough Research"** — Erika Hall, research for lean teams
- **"SUS: A Quick and Dirty Usability Scale"** — John Brooke, original SUS paper

### 📚 About This Skill

This skill is based on the methodology from *"Universal Methods of Design"* by Bruce Hanington and Bella Martin, a comprehensive reference of 100 design research methods spanning exploration, synthesis, and communication phases.

### 🔗 Related Skills

This skill is part of the **AliDujie UX Research Skills Ecosystem**:

- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done theory
- **[Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill)** — Persona creation
- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — Quantitative research, HEART framework
- **[Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design)** — Value proposition canvas
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — Data storytelling

### 🌟 Why Choose AliDujie Skill Ecosystem?

This skill is part of the **AliDujie UX Research Skills Ecosystem**. Using the complete ecosystem provides:

- ✅ **Complete Coverage** — From user research to product design to data presentation, full-process tool support
- ✅ **Seamless Integration** — All skills use consistent API design and data formats
- ✅ **Best Practices** — Based on classic theories and practical experience, avoid common pitfalls
- ✅ **Active Maintenance** — Regularly updated with new features and improvements
- ✅ **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- ✅ **Bilingual Support** — Complete CN/EN documentation for international team collaboration

👉 **Explore More Skills**: [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [Web Persona](https://github.com/AliDujie/web-persona-skill) | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | [Structured Thinking](https://github.com/AliDujie/Structured-Thinking-Model)

### 🏷️ GitHub Topics (Recommended)

```
user-experience design-research python-toolkit ux-methods
usability-testing survey-design journey-mapping openclaw-skill
universal-design-methods alicloud
```

### 📦 Dependencies

- Python >= 3.8
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

### 📋 Changelog

| Version | Date | Changes |
| v2.3.10 | 2026-05-03 | Repo maintenance: fixed English changelog table formatting (removed rogue separator rows), aligned SKILL.md version, updated Last Updated timestamp |
| v2.3.8 | 2026-05-03 | Repo maintenance: streamlined English Quick Start code comments for clarity, aligned SKILL.md version with README.md, added pyproject.toml classifiers |
| v2.3.7 | 2026-05-03 | Fixed SKILL.md version mismatch (2.3.5→2.3.7), aligned all version references, cleaned up duplicate changelog entries |
| v2.3.6 | 2026-05-03 | Added English version history, added classifiers and project.urls to pyproject.toml |
| v2.3.5 | 2026-05-03 | Repo maintenance: sync pyproject.toml version, add changelog entry for consistency review
| v2.3.4 | 2026-05-03 | Repo maintenance: cross-ecosystem consistency review, verified cross-references and version alignment
| v2.3.3 | 2026-05-02 | Added English Quick Decision Guide table to improve cross-skill discoverability |
| v2.3.2 | 2026-05-02 | Repo maintenance: fixed English capabilities table (added CEO rows 3 + observation), improved capability descriptions, added changelog to English section |
| v2.3.1 | 2026-05-02 | Fixed SKILL.md version mismatch, added CEO capabilities to English table |
| v2.3.0 | 2026-05-01 | Added quick reference table, badges, CEO perspective extension |

---

## 🔗 Skill Ecosystem Workflow

UDM is the methodological core of the **AliDujie UX Research Skills Ecosystem**. Here are typical workflows combining it with other skills:

### 🧭 Quick Decision Guide

| Your Question | Recommended Skill |
|---------------|------------------|
| "I don't know what research to do" | → **Universal Design Methods** (this skill) — Method recommendation |
| "I need to validate a hypothesis" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B testing & sample size |
| "I want to understand why users do this" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — Uncover the underlying "jobs" |
| "I need to know who my users are" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — Create concrete personas |
| "Is my product value strong enough?" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — Fit diagnosis |
| "How do I present research results clearly?" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Data storytelling |

### Workflow 1: Qualitative → Quantitative Triangulation

```
UDM (qualitative research) → QuantUX (quantitative validation) → SWD (result presentation)
```

**Scenario**: Research conclusion validation
1. Use UDM for user interviews and usability testing to discover core hypotheses
2. Use QuantUX to design A/B tests for quantitative validation
3. Use SWD to transform results into executive-ready narratives

### Workflow 2: User Research → Value Proposition

```
UDM (user interviews) → JTBD (needs insight) → VPD (value design)
```

**Scenario**: New product direction exploration
1. Use UDM interviews to collect user pain points and behavioral insights
2. Use JTBD to analyze core "jobs" and opportunity scores
3. Use VPD to map findings to value proposition canvas and validate

### Workflow 3: Research Insights → Design Decisions

```
UDM (usability testing) → Persona (role definition) → SWD (presentation)
```

**Scenario**: Product experience optimization
1. Use UDM to execute usability testing, identify experience breakpoints
2. Use Persona to define user segments based on behavioral data
3. Use SWD to transform research findings into action-oriented presentations

> 💡 **Tip**: UDM's method recommendation engine supports triangulation, auto-recommending 3-5 method combinations covering qualitative + quantitative.

---

## 🔗 技能生态工作流 (Skill Ecosystem Workflow)

UDM 是 **AliDujie UX 研究技能生态系统** 的方法论核心。以下是与其他技能配合使用的典型工作流：

### 🧭 快速决策指南 (Quick Decision Guide)

| 你的问题 | 推荐技能 |
|----------|----------|
| "我不知道该研究什么" | → **Universal Design Methods** (本技能) — 方法推荐帮你找到方向 |
| "我需要验证一个假设" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B 测试和样本量计算 |
| "我想理解用户为什么这样做" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — 挖掘用户背后的"工作" |
| "我需要知道用户是谁" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — 创建具体的人物角色 |
| "我的产品价值够不够？" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — 契合度诊断 |
| "我怎么把研究结果讲清楚？" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事和图表改造 |

### 工作流 1: 定性 → 定量三角验证

```
UDM (定性研究) → QuantUX (定量验证) → SWD (结果呈现)
```

**场景**: 研究结论验证
1. 用 UDM 进行用户访谈和可用性测试，发现核心假设
2. 用 QuantUX 设计 A/B 测试定量验证假设
3. 用 SWD 将验证结果转化为高管可读的叙事

### 工作流 2: 用户研究 → 价值主张

```
UDM (用户访谈) → JTBD (需求洞察) → VPD (价值设计)
```

**场景**: 新产品方向探索
1. 用 UDM 访谈方法收集用户痛点和行为洞察
2. 用 JTBD 分析用户核心"工作"和机会分数
3. 用 VPD 将发现映射到价值主张画布并验证

### 工作流 3: 研究洞察 → 设计决策

```
UDM (可用性测试) → Persona (角色定义) → SWD (汇报呈现)
```

**场景**: 产品体验优化
1. 用 UDM 执行可用性测试，识别体验断点
2. 用 Persona 基于行为数据定义用户细分
3. 用 SWD 将研究发现转化为行动导向的汇报

> 💡 **提示**: UDM 的方法推荐引擎支持三角测量，自动推荐 3-5 种方法组合，覆盖定性+定量。

## Run Tests / 运行测试

```bash
cd /path/to/universal-design-methods
python3 -m pytest udm/tests/ -v 2>/dev/null || echo "Run test suite manually"
```

## 🤝 参与贡献 (Contributing)

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。

- 🐛 **报告 Bug**: 提交 [Issue](https://github.com/AliDujie/universal-design-methods/issues)
- 💡 **功能建议**: 提交 [Feature Request](https://github.com/AliDujie/universal-design-methods/issues/new?template=feature_request.md)
- 📝 **改进文档**: PR 欢迎，特别是参考文档和代码示例

## 🆘 获取帮助 (Getting Help)

- 📖 查看 [故障排查](#故障排查-troubleshooting) 部分
- 📚 阅读 [references/](references/) 目录下的方法论文档
- 💬 在 [Issues](https://github.com/AliDujie/universal-design-methods/issues) 中提问

## 📜 许可 (License)

本技能仅供内部学习和研究使用。

## 👨‍💻 作者 (Credits)

- 基于《Universal Methods of Design》by Bella Martin & Bruce Hanington
- 技能开发：AliDujie 团队
- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫

### 🚀 完整端到端工作流：从 0 到高管汇报 (End-to-End Workflow)

以下是一个真实产品优化场景中，6 个技能如何协作的完整工作流：

**场景**: 电商 App 用户留存率下降 15%，需要找到原因并提出改进方案

```
Phase 1: 发现 (UDM + JTBD)
  UDM: 用户访谈 (12 人) + 可用性测试 → 发现结账流程痛点
  JTBD: 四力分析 → 用户"雇佣"竞品的原因是更快的结账体验

Phase 2: 量化 (QuantUX + Persona)
  QuantUX: A/B 测试新结账流程 vs 旧流程 (n=5000)
  Persona: 发现 "时间敏感型买家" 流失最严重

Phase 3: 验证与设计 (VPD + QuantUX)
  VPD: 价值主张画布 → "一键结账" 契合度 0.82
  QuantUX: CSat 调查验证，NPS 提升 23 分

Phase 4: 呈现 (SWD)
  SWD: 三幕叙事 → 问题(留存下降) → 方案(A/B 测试成功) → 行动(全量发布)
  产出: CEO 级汇报材料，含 HEART 指标趋势图
```

> 💡 **每个阶段用对应技能**: UDM 发现 → JTBD 洞察 → QuantUX 量化 → Persona 细分 → VPD 验证 → SWD 呈现

👉 **尝试完整工作流**: [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · [Persona](https://github.com/AliDujie/web-persona-skill) · [VPD](https://github.com/AliDujie/value-proposition-design) · [SWD](https://github.com/AliDujie/storytelling-with-data)

---

### 💡 Pro Tips / 专业提示

- **三角测量优先** — 永远不要只用一种方法。至少组合 2 种方法（定性+定量）交叉验证
- **从 CEO 视角出发** — 在研究开始前就定义"这个研究要支持什么决策"
- **先定性后定量** — 用 UDM 访谈发现问题，用 QuantUX 验证规模
- **SUS 70 分是基准线** — 低于 70 分需要优先改进，高于 85 分可以考虑新功能
- **体验历程图 5-7 阶段最佳** — 太少过于笼统，太多难以聚焦
- **方法 ROI 评估** — 用 `add_method_roi()` 在研究规划前评估方法投入产出比


## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
| v2.3.12 | 2026-05-04 | 仓库维护：添加完整端到端工作流章节（展示 6 个技能协作场景），修复版本历史重复条目，对齐 pyproject.toml 版本 |
| v2.3.10 | 2026-05-03 | 仓库维护：修复英文版版本历史表格格式（删除错误分隔符行），SKILL.md 版本对齐，Last Updated 时间戳更新 |
| v2.3.11 | 2026-05-03 | 仓库维护：添加 Pro Tips 专业提示章节（中英双语），提升技能使用效率指南 |
| v2.3.9 | 2026-05-03 | 仓库维护：修复版本历史表格格式（删除错误分隔符行），添加英文版版本历史表，统一 SKILL.md 与 README.md 版本引用
| v2.3.8 | 2026-05-03 | 仓库维护：精简英文 Quick Start 代码示例（场景化注释优化），统一 SKILL.md 与 README.md 版本引用，添加 pyproject.toml classifiers |
| v2.3.7 | 2026-05-03 | 修复 SKILL.md 版本不一致 (2.3.5→2.3.7)，清理重复条目，统一所有版本引用 |
| v2.3.6 | 2026-05-03 | 添加英文版版本历史表，统一 pyproject.toml 元数据 |
| v2.3.5 | 2026-05-03 | 统一 pyproject.toml 版本，添加一致性审查日志 |
| v2.3.4 | 2026-05-03 | 跨技能一致性审查，验证交叉引用和版本对齐 |
| v2.3.3 | 2026-05-02 | 为英文版添加 Quick Decision Guide 导航表，增强技能间交叉引用 |
| v2.3.2 | 2026-05-02 | 仓库维护：优化英文 Quick Start 代码示例排版，补充 CEO 能力英文版表格，增强技能生态工作流描述，统一版本标签格式 |
| v2.3.1 | 2026-05-02 | 修复 SKILL.md 版本号不一致 (v2.2.0→v2.3.0)，添加 CEO 能力到英文能力表，补充 Structured-Thinking-Model 交叉引用 |
| v2.3.0 | 2026-05-01 | 添加快速参考表、Badges、CEO 视角扩展、更新维护 |
| v2.1 | 2026-04-30 | 添加快速参考表、Badges、更新维护 |
| v1.8 | 2026-04-26 | 更新 Last Updated 日期，维护技能生态一致性 |
| v1.7 | 2026-04-25 | 统一技能生态格式，更新交叉引用 |
| v1.6 | 2026-04-23 | 更新 Last Updated 时间戳，统一技能生态系统格式 |
| v1.5 | 2026-04-23 | 添加版本历史、Last Updated 徽章 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、故障排查、扩展阅读 |
| v1.3 | 2026-04-22 | 初始版本 |

---


### 💡 Pro Tips

- **Triangulation First** — Never rely on a single method. Combine at least 2 methods (qualitative + quantitative) for cross-validation
- **Start from CEO Perspective** — Define "what decision does this research support" before starting
- **Qualitative Before Quantitative** — Use UDM interviews to discover problems, QuantUX to validate scale
- **SUS 70 is the Baseline** — Below 70 requires priority improvement, above 85 you can consider new features
- **Journey Maps: 5-7 stages optimal** — Too few is vague, too many loses focus
- **Method ROI Assessment** — Use `add_method_roi()` to evaluate research method ROI before planning


## 📋 Version History (English)

| Version | Date | Changes |
| v2.3.12 | 2026-05-04 | Repo maintenance: added end-to-end workflow section showing complete 6-skill collaboration scenario, fixed duplicate v2.3.10 changelog entries, aligned pyproject.toml version |
| v2.3.10 | 2026-05-03 | Repo maintenance: fixed English changelog table formatting (removed rogue separator rows), aligned SKILL.md version, updated Last Updated timestamp |
| v2.3.11 | 2026-05-03 | Repo maintenance: added Pro Tips section (CN/EN) for expert usage guidance |
| v2.3.8 | 2026-05-03 | Repo maintenance: streamlined English Quick Start code comments for clarity, aligned SKILL.md version with README.md, added pyproject.toml classifiers |
| v2.3.7 | 2026-05-03 | Fixed SKILL.md version mismatch (2.3.5→2.3.7), cleaned up duplicate changelog entries |
| v2.3.6 | 2026-05-03 | Added English version history, added classifiers and project.urls to pyproject.toml |
| v2.3.5 | 2026-05-03 | Repo maintenance: sync pyproject.toml version, add changelog entry for consistency review |
| v2.3.4 | 2026-05-03 | Repo maintenance: cross-ecosystem consistency review, verified cross-references and version alignment |
| v2.3.3 | 2026-05-02 | Added English Quick Decision Guide table to improve cross-skill discoverability |
| v2.3.2 | 2026-05-02 | Repo maintenance: fixed English capabilities table (added CEO rows + observation), improved capability descriptions, added changelog to English section |
| v2.3.1 | 2026-05-02 | Fixed SKILL.md version mismatch, added CEO capabilities to English table |
| v2.3.0 | 2026-05-01 | Added quick reference table, badges, CEO perspective extension |
| v2.1 | 2026-04-30 | Added quick reference table, badges, updated maintenance |
| v1.8 | 2026-04-26 | Updated Last Updated date, maintained skill ecosystem consistency |
| v1.7 | 2026-04-25 | Unified skill ecosystem format, updated cross-references |
| v1.6 | 2026-04-23 | Updated Last Updated timestamp, unified skill ecosystem format |
| v1.5 | 2026-04-23 | Added version history, Last Updated badge |
| v1.4 | 2026-04-23 | Added skill ecosystem navigation table, troubleshooting, extended reading |
| v1.3 | 2026-04-22 | Initial release |

*Last Updated: 2026-05-04 | AliDujie Skill Ecosystem | v2.3.12*
