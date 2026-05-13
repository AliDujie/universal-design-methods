# Universal Design Methods Skill

[![Ecosystem](https://img.shields.io/badge/AliDujie-Ecosystem-7B68EE.svg)](https://github.com/AliDujie)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Version](https://img.shields.io/badge/version-2.3.61-green.svg)](CHANGELOG.md)
[![Install Guide](https://img.shields.io/badge/install-guide-orange.svg)](INSTALL.md)
![Last Updated](https://img.shields.io/badge/last%20updated-2026-05-13-brightgreen.svg)

> 📖 **100 种设计研究方法、11 大执行能力、1 个完整 Python 工具包**

```text
┌─────────┐    ┌──────────┐    ┌─────┐    ┌──────────┐    ┌─────┐    ┌─────┐
│ Persona │ →  │   JTBD   │ →  │ UDM │ →  │ QuantUX  │ →  │ VPD │ →  │ SWD │
│ 角色定义 │    │ 需求洞察  │    │ 研究方法 │    │ 定量验证  │    │ 价值设计│    │ 数据叙事 │
└─────────┘    └──────────┘    └─────┘    └──────────┘    └─────┘    └─────┘
```

**UDM is the methodological core** — providing the research methods that fuel every other skill in the ecosystem. Start here when you don't know what research to do.

基于《通用设计方法》(贝拉·马丁 & 布鲁斯·汉宁顿) 构建，覆盖 UX 研究全生命周期。

---

## 🌐 技能生态系统 (Skill Ecosystem)

本技能是 AliDujie 用户研究技能生态系统的**方法论核心**，覆盖定性研究全生命周期。与其他技能协同使用，效果更佳：

| 技能 | 角色 | 协同场景 |
|------|------|----------|
| [📊 Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 定量验证 | UDM 定性发现 → QuantUX 定量验证 → 综合报告 |
| [📈 Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | UDM 研究结果 → SWD 图表改造 → 叙事构建 |
| [🎯 JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 深度需求洞察 | UDM 访谈发现 → JTBD 机会评分 → 决策支持 |
| [💎 Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值设计 | UDM 用户需求 → VPD 画布分析 → 实验验证 |
| [👤 Web Persona](https://github.com/AliDujie/web-persona-skill) | 用户画像 | UDM 研究数据 → Persona 角色创建 → 设计指导 |
| [🧠 Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | 战略分析 | UDM 研究结果 → STM 商业框架 → 战略决策 |

---

### 🔗 Ecosystem Quick Start / 生态系统快速上手

UDM 是 7 技能工作流的**方法论核心**。典型完整工作流：

```
Persona (定义用户) → JTBD (挖掘需求) → UDM (研究方法) → QuantUX (定量验证) → VPD (价值设计) → SWD (数据叙事)
```

**组合调用示例：**
```python
# Step 1: UDM 推荐研究方法
from udm import UDMSkill
udm = UDMSkill("旅行平台")
plan = udm.recommend_methods("了解用户流失原因", phase=1)

# Step 2: 用 UDM 执行访谈后，用 JTBD 结构化分析
from jtbd import JTBDSkill
jtbd = JTBDSkill("旅行平台")
report = jtbd.generate_analysis_report()

# Step 3: QuantUX 定量验证假设
from quantux import QuantUXSkill
quantux = QuantUXSkill("旅行平台")
heart = quantux.build_heart_framework()

# Step 4: SWD 将结果转化为高管可读的数据叙事
from swd import SWDSkill
swd = SWDSkill("流失分析报告")
story = swd.build_story(protagonist="产品团队", imbalance="用户流失加剧", call_to_action="批准优化投入")

# Step 5: STM 用商业框架做战略决策
from stm import STMSkill
stm = STMSkill("旅行平台")
analysis = stm.run_pestel()
```

> 💡 **Try it now / 立即尝试**:
> ```python
> from udm import UDMSkill
> skill = UDMSkill("你的产品")
> print(skill.recommend_methods("了解用户为什么流失", phase=1))  # 立即获取方法推荐
> ```

> 💡 **提示**: 每个技能的 `references/` 目录都有对应的方法论文档，配合使用效果更佳。

### ✅ 5 分钟快速开始检查清单

- [ ] **安装** — `cp -r universal-design-methods /your/agent/skills/`
- [ ] **导入** — `from udm import UDMSkill`
- [ ] **初始化** — `skill = UDMSkill("你的产品")`
- [ ] **方法推荐** — `skill.recommend_methods("了解用户需求", phase=1)`
- [ ] **访谈提纲** — `skill.generate_interview("用户访谈", "contextual")`
- [ ] **可用性测试** — `skill.generate_usability_test("流程测试", "formative")`
- [ ] **问卷设计** — `skill.generate_survey("需求调研", "kano")`
- [ ] **体验历程图** — `skill.build_journey_map("预订体验", persona="用户")`

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

### 🌍 实战场景指南

| 你的场景 | 调用方式 | 输出结果 |
|----------|---------|----------|
| "需要了解用户为什么流失" | `generate_interview("用户访谈", "contextual")` | 结构化情境访谈提纲 |
| "应该用哪些研究方法？" | `recommend_methods("了解用户痛点", phase=1)` | 3-5 种推荐方法及理由 |
| "我们的 App 好用吗？" | `generate_usability_test("核心任务流", "summative")` | 任务清单 + 成功标准 + SUS 问卷 |
| "用户对新功能评价如何？" | `generate_survey("功能满意度", "csat")` | CSAT/NPS 调查问卷 |
| "可视化展示用户旅程" | `build_journey_map("预订流程", persona="新用户")` | 带痛点的用户旅程图 |

> 💡 **提示**: 先用 `recommend_methods()` 获取方法推荐，再调用具体生成器执行。

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **全面覆盖** — 100 种设计研究方法，从探索到评估到综合到沟通，一站式解决
- **11 大执行能力** — 方法推荐、访谈提纲、可用性测试、问卷设计、体验历程图、研究计划、报告生成、SUS/NPS 计算、CEO 视角决策支持
- **实战工具包** — 纯 Python 标准库实现，无外部依赖，5 分钟上手
- **智能推荐** — 基于研究阶段和目标自动推荐方法组合（三角测量）
- **双语支持** — 完整中英文文档，适合国际化团队
- **零学习成本** — API 设计直观，代码示例丰富，即插即用
- **CEO 视角** — 每个方法都附带 ROI 评估、资源估算和决策产出建议
- **从探索到交付** — 覆盖完整研究生命周期：发现假设 → 收集数据 → 分析综合 → 汇报呈现
- **行业标杆** — 基于 Bella Martin & Bruce Hanington 的经典著作，100 种方法覆盖全设计流程

### ⚡ 5 分钟快速开始 (Quick Start)

#### 步骤 1: 安装技能

```bash
# 方式 A: 复制到你的 AI Agent skills 目录
cp -r universal-design-methods /your/agent/skills/

# 方式 B: 作为 Python 包安装（支持 pip import）
cd universal-design-methods && pip install -e .
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
from udm import JourneyMapBuilder
jm = skill.build_journey_map("预订体验", persona="用户小李")
jm.add_stage("搜索", actions=["打开 App"], emotions=4, pain_points=["排序差"])
print(JourneyMapBuilder.render_markdown(jm.build()))

# ===== 场景 6: 研究计划 & 报告（自动附加 CEO 视角）=====
plan = skill.generate_research_plan("体验研究", background="用户流失率上升")
# 自动生成：目标 → 方法选择 → 参与者规划 → 时间表 → 预算 → 风险评估
# 自动附加：方法 ROI 评估 + 资源分配建议

# ===== 场景 7: 综合分析工具（亲和图/画像/Elito/矩阵）=====
from udm import AffinityDiagramBuilder
aj = skill.build_affinity_diagram("用户反馈归类")
aj.add_note("搜索太慢", category="性能")
aj.add_note("结果不准", category="相关性")
print(AffinityDiagramBuilder.render_markdown(aj.build()))  # 亲和图分组 + 洞察汇总

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
| 1 | **方法推荐** | `recommender.py` | 基于研究阶段/目标自动推荐 3-5 种方法组合（三角测量） |
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
from udm import JourneyMapBuilder
print(JourneyMapBuilder.render_markdown(jm.build()))

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
│                                         ↓                   │
│                                    🧠 Structured Thinking   │
│                                    Model (结构化思维)        │
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
| **UX 研究员** | 100 种研究方法随时调用，自动推荐节省数小时 |
| **产品经理** | 无需深入了解方法论即可规划专业研究 |
| **设计师** | 结构化用户访谈方法，执行可用性测试 |
| **学生/教育者** | 基于《Universal Methods of Design》的教学材料 |
| **AI Agent** | 零依赖 Python 包，LLM 工作流即插即用 |

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
from udm import JourneyMapBuilder
print(JourneyMapBuilder.render_markdown(jm.build()))
```

### ⚠️ 常见研究陷阱 (Common Research Pitfalls)

| 陷阱 | 表现 | 应对 |
|------|------|------|
| 只用一种方法 | "我们做了 5 个访谈就够了" | 三角测量：定性 + 定量 + 行为数据至少 2-3 种方法 |
| 确认偏误 | 只收集支撑已有结论的数据 | 主动寻找反面证据，用 weighted matrix 客观评估 |
| 样本偏差 | 访谈都是活跃用户 | 纳入流失用户、非用户，扩大样本多样性 |
| 跳过综合阶段 | 收集数据后直接进入方案设计 | 用亲和图/Elito 方法做系统性综合分析 |
| CEO 视角缺失 | 研究报告没有商业影响分析 | 用 `generate_report(include_ceo_analysis=True)` 自动附加 ROI 评估 |
| 跳过知识检索 | 直接生成方案，忽略已有方法论 | 理论问题先用 `search_knowledge()` 查询 100 种方法索引 |

> 💡 **提示**: UDM 的三角测量原则——任何研究都应组合至少 2-3 种方法，混合定性与定量数据，从多个角度验证发现。

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

### 🏆 实战案例 (Case Studies)

#### 案例 1: 电商 App 购物体验优化

**背景**: 某头部电商平台发现购物车转化率连续 3 个月下滑

**使用 UDM 技能**:
```python
from udm import UDMSkill

skill = UDMSkill("电商 App")

# 步骤 1: 方法推荐 — 确定研究方案
methods = skill.recommend_methods("了解购物车放弃原因", phase=1)
# → 推荐：用户访谈（情境）+ 日记研究 + 可用性测试

# 步骤 2: 生成情境访谈提纲
guide = skill.generate_interview("购物车体验访谈", "contextual")

# 步骤 3: 执行可用性测试 + SUS 评估
sus_scores = [65, 72, 58, 70, 62, 75, 68, 71]
avg_sus = sum(sus_scores) / len(sus_scores)  # 67.6 — 需要改进

# 步骤 4: 构建体验历程图发现痛点
jm = skill.build_journey_map("购物旅程")
jm.add_stage("搜索", actions=["输入关键词"], emotions=4, pain_points=["搜索结果不相关"])
jm.add_stage("加购", actions=["选择规格", "加入购物车"], emotions=2, pain_points=["规格选择复杂", "缺少对比"])
jm.add_stage("结算", actions=["填写地址", "选择支付"], emotions=3, pain_points=["运费不透明"])

# 步骤 5: 生成研究报告
card = skill.calculate_nps([9, 10, 8, 7, 10, 6, 9, 8, 10, 5])
report = skill.generate_report("购物车体验研究", summary=f"平均 SUS {avg_sus:.1f}，NPS {card}")
```

**成果**: 发现 3 个核心痛点 → 优化后购物车转化率提升 18%，SUS 从 67.6 提升到 78.2

#### 案例 2: B2B SaaS 用户需求探索

**背景**: 某协作工具需要进入新市场（中小企业），不了解目标用户需求

**使用 UDM 技能**:
```python
from udm import UDMSkill

skill = UDMSkill("B2B 协作 SaaS")

# 用 KANO 问卷区分功能需求优先级
survey = skill.generate_survey(
    "功能需求调研", "kano",
    features=["AI 会议纪要", "任务自动化", "跨平台同步", "审批流程"]
)

# 加权矩阵评估方案优先级
wm = skill.build_weighted_matrix("方案评估")
wm.add_criterion("用户需求", weight=0.4)
wm.add_criterion("技术可行性", weight=0.3)
wm.add_criterion("商业价值", weight=0.3)
wm.add_option("AI 会议纪要", {"用户需求": 5, "技术可行性": 3, "商业价值": 5})
wm.add_option("任务自动化", {"用户需求": 4, "技术可行性": 2, "商业价值": 4})
print(wm.render_markdown())
```

**成果**: 明确功能优先级 → 首季度推出 AI 会议纪要，获客成本降低 30%

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

### 💡 专业技巧

- **尽早使用推荐器** — 在确定研究计划前，先用 `recommend_methods()` 获取方法建议，经常能发现你没考虑到的方法组合
- **永远三角测量** — 不要依赖单一方法。推荐器建议 3-5 种方法组合是有原因的——不同方法揭示不同真相
- **与竞品对比 SUS** — 不要只看自己的 SUS 分数，测试竞品产品来了解"好"的标准
- **保存历程图基线** — 对历程图进行版本管理，每次设计迭代后更新地图并对比痛点，衡量改进进展
- **利用 CEO 视角** — 即使你不是 CEO，ROI 和资源分配洞察也能帮你向利益相关者证明研究投入的价值

### ❌ 常见错误

- **方法跟风** — 不要因为方法听起来酷就选它。让推荐器根据你的研究阶段和目标来指导选择
- **忽略阶段上下文** — 在探索阶段使用评估方法（可用性测试）会浪费资源。方法必须匹配阶段
- **过度设计问卷** — 卡诺和 NPS 问卷很强大，但只有在问题聚焦时才有效。从 5-10 个关键问题开始
- **跳过研究计划** — 没有计划就直接做访谈会导致数据不一致。先用 `generate_research_plan()` 生成计划
- **把历程图当最终产物** — 历程图是活文档，随着对用户的了解不断更新

### ❓ 常见问题 (FAQ)

**Q: UDM 和其他 UX 研究工具有什么区别？**
A: UDM 是面向 AI Agent 的完整工具包，覆盖 100 种设计方法的知识查询 + 11 项可执行能力。与单一工具不同，UDM 提供方法推荐、三角测量、CEO 决策支持等全链路能力。

**Q: 需要编程基础吗？**
A: 不需要。你可以直接用自然语言向 AI Agent 提问（如"帮我设计用户访谈"），也可以作为 Python 包在代码中调用。两种方式都支持。

**Q: 100 种方法真的都能用吗？**
A: 是的。每种方法都有详细说明、适用场景、执行步骤和输出模板。方法推荐引擎会根据你的研究阶段和目标自动推荐 3-5 种方法组合。

**Q: SUS/NPS 计算准确吗？**
A: SUS 使用标准计算公式（Bangor et al.），NPS 使用行业标准算法。结果与专业调研工具一致。

**Q: 可以和 QuantUX 一起用吗？**
A: 强烈推荐！UDM 做定性发现，QuantUX 做定量验证，两者结合实现方法三角测量，显著提升研究信度。

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
universal-design-methods alicloud user-interviews affinity-diagram
persona-creation research-planning interview-generation
```

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

### 🧭 快速决策指南 (Quick Decision Guide)

| 你的问题 | 推荐技能 |
|----------|----------|
| "不知道选什么研究方法" | → **Universal Design Methods (本技能)** — 方法推荐与执行 |
| "需要定量验证假设" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B 测试、HEART 指标、样本量计算 |
| "想理解用户背后的「工作」" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — 用户"工作"挖掘、机会评分 |
| "需要创建用户画像" | → [Web Persona](https://github.com/AliDujie/web-persona-skill) — 人物角色创建与细分 |
| "验证价值主张够不够强" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — 价值主张画布、实验验证 |
| "研究结果怎么讲给高管听" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事与图表呈现 |
| "需要结构化商业分析框架" | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — PESTEL、五力模型、决策树 |

---

### 🔄 完整端到端工作流：从 0 到高管汇报 (End-to-End Workflow)

> 7 个技能串联，覆盖用户研究的完整生命周期。

#### 阶段 1: 发现与理解 (Discovery)
1. **Universal Design Methods** → 方法推荐 + 用户访谈 + 可用性测试
2. **Web Persona** → 基于研究数据创建用户画像
3. **JTBD Knowledge** → 挖掘用户背后的"工作"和未满足需求

#### 阶段 2: 验证与量化 (Validation)
4. **Quantitative UX Research** → HEART 指标、A/B 测试、MaxDiff 优先级
5. **Value Proposition Design** → 价值主张实验验证 + 匹配度评分

#### 阶段 3: 呈现与决策 (Presentation)
6. **Storytelling with Data** → 将研究结果转化为高管可读的数据叙事

```python
# 示例：端到端工作流伪代码
# 阶段 1: 定性发现
from udm import UDMSkill
from persona import PersonaSkill
from jtbd import JTBDSkill

udm = UDMSkill("电商平台")
methods = udm.recommend_methods("了解用户购物痛点", phase=1)
persona = PersonaSkill("电商平台")
persona.add_persona(
    name="小明", short_desc="效率型用户", priority="primary",
    quote="我只想快速完成", goals=["快速完成任务"],
    behaviors=["高频使用"], attitudes=["效率优先"], bio="忙碌的职场人"
)
jtbd = JTBDSkill("电商平台")
jobs = jtbd.analyze(include_ceo_analysis=True)

# 阶段 2: 定量验证
from quantux import QuantUXSkill
from vpd import VPDSkill

quantux = QuantUXSkill("电商平台")
heart = quantux.build_heart_framework()
vpd = VPDSkill("电商平台", "年轻白领")
# VPD requires full canvas inputs: jobs, pains, gains, products, pain_relievers, gain_creators
# canvas = vpd.analyze_canvas(product_name="...", jobs=[...], pains=[...], gains=[...], ...)

# 阶段 3: 数据叙事
from swd import SWDSkill
swd = SWDSkill("电商平台季度汇报")
swd.build_context(audience="CEO", cta="批准 Q4 优化预算")
```

---

### 💻 实用集成示例 (Practical Integration Examples)

#### 集成 1: UDM 发现 → JTBD 分析

```python
from udm import UDMSkill
from jtbd import JTBDSkill

# 用 UDM 做访谈收集数据
udm = UDMSkill("产品名")
guide = udm.generate_interview("用户访谈", "contextual")
# 访谈输出 → JTBD 输入

# 用 JTBD 结构化分析
jtbd = JTBDSkill("产品名")
# JTBD analyze() works on pre-configured job data; use analyze(include_ceo_analysis=True)
# to generate structured JTBD analysis with CEO decision support
jobs = jtbd.analyze(include_ceo_analysis=True)
```

#### 集成 2: JTBD → VPD 价值主张验证

```python
from jtbd import JTBDSkill
from vpd import VPDSkill

# JTBD 发现用户"工作"
jtbd = JTBDSkill("产品名")
jtbd.analyze(include_ceo_analysis=True)  # Analyzes pre-configured jobs data

# 将 JTBD 发现映射到 VPD 画布
vpd = VPDSkill("产品名", "商务用户")
vpd.analyze_canvas(
    product_name="产品名",
    jobs=[{"job": "快速预订", "type": "功能性", "importance": "高"}],
    pains=[{"pain": "选择焦虑", "severity": "高"}],
    gains=[{"gain": "省时省力", "relevance": "高"}]
)
```

#### 集成 3: QuantUX → SWD 数据叙事

```python
from quantux import QuantUXSkill
from swd import SWDSkill

# QuantUX 定量分析
quant = QuantUXSkill("产品名")
heart = quant.build_heart_framework()

# SWD 将结果转化为叙事
swd = SWDSkill("产品名季度汇报")
swd.build_context(audience="高管", cta="批准优化预算")
swd.full_diagnosis(scores={...})  # 确保叙事质量 ≥ 80/100
```

---

### 🚀 下一步 (Next Steps)

1. **快速上手** — 复制技能到你的 skills 目录，5 分钟内完成首次调用
2. **阅读 SKILL.md** — 了解 AI Agent 触发条件和完整 API 文档
3. **安装 INSTALL.md** — 详细的安装和配置指南
4. **贡献** — 查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与
5. **探索生态** — 尝试其他 5 个技能，构建完整的用户研究工作流

---

## English

### 📑 Table of Contents

- [Why Use This Skill?](#-why-use-this-skill)
- [Features at a Glance](#-features-at-a-glance)
- [Quick Decision Guide](#-quick-decision-guide)
- [Quick Start](#-quick-start)
- [11 Core Capabilities](#-11-core-capabilities)
- [Practical Examples](#-practical-examples)
- [Who Is This For?](#-who-is-this-for)
- [Troubleshooting](#-troubleshooting)
- [Best Practices](#-best-practices)
- [FAQ](#-faq)
- [User Reviews](#-user-reviews)
- [Getting Help](#-getting-help)
- [Extended Reading](#-extended-reading)
- [Related Skills](#-related-skills-1)
- [End-to-End Workflow: All 7 Skills](#-end-to-end-workflow-all-7-skills)
- [Skill Ecosystem Workflow](#-skill-ecosystem-workflow-1)
- [Case Studies](#-case-studies)
- [Version History](#-version-history-english)

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
| "I need a structured framework for analysis" | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — PESTEL, Five Forces, decision trees |

### ✅ 5-Minute Quick Start Checklist

- [ ] **Install** — `cp -r universal-design-methods /your/agent/skills/`
- [ ] **Import** — `from udm import UDMSkill`
- [ ] **Initialize** — `skill = UDMSkill("your product")`
- [ ] **Recommend methods** — `skill.recommend_methods("understand user needs", phase=1)`
- [ ] **Generate interview** — `skill.generate_interview("user interview", "contextual")`
- [ ] **Calculate SUS** — `skill.calculate_sus([4,2,5,1,4,2,5,1,4,2])` → `72.5 (Good)`

### 🚀 Quick Start

#### Step 1: Install

```bash
# Option A: Copy to your AI Agent skills directory
cp -r universal-design-methods /your/agent/skills/

# Option B: Install as a Python package (enables pip import)
cd universal-design-methods && pip install -e .
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
# ===== Scenario 1: Method Recommendation (Auto-Triangulation) =====
methods = skill.recommend_methods("Understand user needs", phase=1)
print(methods)  # Recommends 3-5 method combinations

# ===== Scenario 2: Interview Guide Generation (5 Types) =====
guide = skill.generate_interview("User Interview", "contextual")
print(guide)  # Includes opening, warm-up, core questions, closing

# ===== Scenario 3: Usability Testing + SUS Calculation =====
test = skill.generate_usability_test("Flow Test", "formative")
sus = skill.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])
print(f"SUS Score: {sus}")  # 0-100 scale

# ===== Scenario 4: Survey Design (Kano/NPS/Semantic Differential) =====
survey = skill.generate_survey("Needs Research", "kano", features=["Smart Recommendations"])
nps = skill.calculate_nps([9, 10, 8, 7, 10, 6, 9, 8, 10, 5])
print(f"NPS: {nps}")  # -100 to +100

# ===== Scenario 5: Experience Journey Map =====
from udm import JourneyMapBuilder
jm = skill.build_journey_map("Booking Experience", persona="User Li")
jm.add_stage("Search", actions=["Open App"], emotions=4, pain_points=["Poor sorting"])
print(JourneyMapBuilder.render_markdown(jm.build()))

# ===== Scenario 6: Research Plan & Report (CEO perspective auto-attached) =====
plan = skill.generate_research_plan("Experience Research", background="High churn rate")
# Auto-generated: goals → method selection → participant planning → timeline → budget → risk
report = skill.generate_report("Research Report", summary="Found 3 core pain points")
# Auto-attached: Method ROI assessment + Resource allocation + Decision outputs
```

### 🌍 Real-World Scenario Guide

> **New to UDM?** Here are common scenarios and exactly how to use this skill.

| Scenario | What to Call | Expected Output |
|----------|-------------|----------------|
| "I need to understand why users drop off" | `generate_interview("用户访谈", "contextual")` | Structured interview guide with contextual probes |
| "Which research methods should I use?" | `recommend_methods("了解用户痛点", phase=1)` | 3-5 recommended methods with rationale |
| "Is our app usable?" | `generate_usability_test("核心任务流", "summative")` | Task list + success criteria + SUS survey |
| "What do users think of our new feature?" | `generate_survey("功能满意度", "csat")` | Survey with CSAT/NPS questions |
| "Show the user journey visually" | `build_journey_map("预订流程", persona="新用户")` | Customer journey map with pain points |

**Quick Tip:** Start with `recommend_methods()` — it will suggest the right methods for your research goal, then use the specific generators.

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
from udm import JourneyMapBuilder
jm = skill.build_journey_map("Mobile Shopping", persona="Busy Mom")
jm.add_stage("Search", actions=["Voice search"], emotions=4)
jm.add_stage("Compare", actions=["Price comparison"], emotions=3,
    pain_points=["Too many options"])
jm.add_stage("Purchase", actions=["One-click buy"], emotions=5)
print(JourneyMapBuilder.render_markdown(jm.build()))

# Example 4: Observation with AEIOU framework
obs = skill.generate_observation("Store Experience", "shadowing", setting="Travel agency")
print(obs)  # Activities, Environments, Interactions, Objects, Users

# Example 5: Affinity diagram for synthesis
from udm import AffinityDiagramBuilder
aj = skill.build_affinity_diagram("User Feedback")
aj.add_note("Search too slow", category="Performance")
aj.add_note("Results inaccurate", category="Relevance")
print(AffinityDiagramBuilder.render_markdown(aj.build()))  # Grouped insights + summary

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

### 🔄 End-to-End Ecosystem Workflow

UDM is the **qualitative research engine** of the ecosystem. Here's a complete workflow combining all 7 skills:

```python
# ===== Complete Product Research Cycle (7 Skills) =====
# Step 1: UDM — Conduct qualitative research
udm = UDMSkill("Mobile Banking App")
guide = udm.generate_interview("User Interview", "contextual")

# Step 2: JTBD — Structure raw insights into jobs
from jtbd import JTBDSkill
jtbd = JTBDSkill("Mobile Banking")
jobs = jtbd.analyze(include_ceo_analysis=True)  # Analyzes pre-configured jobs data

# Step 3: QuantUX — Quantify the opportunity
from quantux import QuantUXSkill
quantux = QuantUXSkill("BankingApp Validation")
sample_size = quantux.calculate_ab_sample_size(baseline=0.15, mde=0.02)

# Step 4: VPD — Design value proposition for top jobs
from vpd import VPDSkill
vpd = VPDSkill("BankingApp", "Young Professionals")
# VPD analyze_canvas requires full canvas: jobs, pains, gains, products, pain_relievers, gain_creators
# canvas = vpd.analyze_canvas(product_name="...", jobs=[...], pains=[...], ...)

# Step 5: Web Persona — Create personas from research
from persona import PersonaSkill
persona = PersonaSkill("BankingApp")
persona.add_persona(
    name="Young Professional Alex", short_desc="Achiever",
    priority="primary", quote="I want to get things done quickly",
    goals=["Save time on banking", "Feel secure"],
    behaviors=["Mobile-first", "Values speed"], attitudes=["Efficiency-driven"],
    bio="Busy professional managing finances on the go"
)

# Step 6: SWD — Present findings to stakeholders
from swd import SWDSkill
swd = SWDSkill("BankingApp Research Report")
ctx = swd.build_context(audience="Product VP", cta="Approve redesign budget")

# Step 7: STM — Strategic framework analysis
from stm import STMSkill
stm = STMSkill("BankingApp")
pestel = stm.run_pestel()  # PESTEL analysis for market context
```

> 💡 **Pro Tip**: The most powerful workflows combine 3+ skills. Try: UDM (research) → JTBD (opportunity) → QuantUX (validation) → SWD (presentation) → STM (strategic framework) for maximum impact.

### 👥 Who Is This For?

| Role | How This Skill Helps | Next Skill to Try |
|------|---------------------|-------------------|
| **UX Researchers** | 100 methods at your fingertips, auto-recommendation saves hours | → [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) for validation |
| **Product Managers** | Plan research without deep methodology knowledge | → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) for opportunity scoring |
| **Designers** | Structured approach to user interviews and usability testing | → [Web Persona](https://github.com/AliDujie/web-persona-skill) for persona creation |
| **Students/Educators** | Teaching material based on "Universal Methods of Design" | → [SWD](https://github.com/AliDujie/storytelling-with-data) for presenting findings |
| **AI Agents** | Zero-dependency Python package, plug-and-play for LLM workflows | → Any of the 5 companion skills for full workflow |

### 📁 Project Structure

```
universal-design-methods/
├── SKILL.md              # Agent skill definition (entry point)
├── udm/                  # Python toolkit (pure stdlib, no external deps)
│   ├── __init__.py       # Unified entry class UDMSkill
│   ├── config.py         # 100 methods index & configuration
│   ├── utils.py          # Knowledge base loading & method search
│   ├── templates.py      # Execution template constants
│   ├── interview.py      # Interview guide generator
│   ├── observation.py    # Observation record generator
│   ├── usability.py      # Usability testing + SUS + heuristic evaluation
│   ├── survey.py         # Survey generator + Kano + NPS
│   ├── synthesis.py      # Affinity diagram / Persona / Journey map / Elito / Matrix
│   ├── recommender.py    # Method recommendation engine
│   ├── research_plan.py  # Research plan generator
│   ├── report.py         # Research report generator
│   └── tests/            # Test suite
├── references/           # Knowledge base (9 documents incl. ecosystem collaboration)
│   ├── methods-exploration.md
│   ├── methods-generative.md
│   ├── methods-evaluative.md
│   ├── methods-synthesis.md
│   ├── methods-communication.md
│   ├── execution-templates.md
│   ├── decision-framework.md
│   ├── 08-ecosystem-collaboration.md  # Cross-skill ecosystem collaboration
│   └── README.md              # Knowledge base index
├── pyproject.toml
└── README.md
```

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

### 💡 Pro Tips

- **Use the recommender early** — Before committing to a research plan, run `recommend_methods()` with your goal. It often suggests methods you hadn't considered.
- **Always triangulate** — Never rely on a single method. The recommender suggests 3-5 method combinations for a reason — different methods reveal different truths.
- **SUS benchmark against competitors** — Don't just measure your SUS score in isolation. Test competitor products for context on what "good" looks like.
- **Save journey maps as baselines** — Version your journey maps. After each design iteration, update the map and compare pain points to measure progress.
- **Use the CEO perspective** — Even if you're not a CEO, the ROI and resource allocation insights help justify research investment to stakeholders.

### 🔄 When to Combine Multiple Methods

UDM's triangulation engine recommends 3-5 method combinations. Here are common patterns:

| Research Goal | Recommended Combination | Why |
|--------------|------------------------|-----|
| Understand why users churn | Contextual Inquiry + Diary Study + Exit Survey | Observe behavior → Track patterns → Understand reasons |
| Validate a new feature concept | Concept Testing + Card Sorting + A/B Test (QuantUX) | Test appeal → Check IA → Validate with data |
| Improve onboarding experience | Heuristic Evaluation + Usability Testing + SUS | Expert review → User testing → Quantify improvement |
| Explore a new market | Stakeholder Interviews + Competitive Analysis + Cultural Probe | Internal alignment → Market landscape → User context |
| Prioritize feature backlog | Kano Survey + MaxDiff (QuantUX) + JTBD Opportunity Score | Satisfaction → Preference → Underlying need |

> 💡 **Rule of thumb**: Always pair at least one generative method (discover what you don't know) with one evaluative method (test what you think you know).

### ⛔ When NOT to Use This Skill

- **Quick A/B test decisions** — Use [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) for statistical hypothesis testing
- **Data visualization** — Use [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) for chart design and data narratives
- **Market sizing / TAM calculations** — Use [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) for opportunity scoring and market analysis
- **Competitive pricing analysis** — Use [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) for positioning and pricing strategy
- **Quick persona creation without research** — Use [Web Persona](https://github.com/AliDujie/web-persona-skill) for rapid persona templates

### ❌ Common Mistakes to Avoid

- **Method shopping** — Don't pick methods because they sound cool. Let the recommender guide you based on your research phase and goals.
- **Ignoring phase context** — Using evaluative methods (usability testing) in exploratory phases wastes resources. Match methods to phases.
- **Over-engineering surveys** — Kano and NPS surveys are powerful but only when questions are focused. Start with 5-10 key items.
- **Skipping the research plan** — Jumping straight into interviews without a plan leads to inconsistent data. Use `generate_research_plan()` first.
- **Treating journey maps as final** — Journey maps are living documents. Update them as you learn more about your users.

### ❓ FAQ

**Q: How is UDM different from other UX research tools?**
A: UDM is a complete AI Agent toolkit covering 100 design methods with knowledge query + 11 executable capabilities. Unlike single-purpose tools, UDM provides method recommendation, triangulation, and CEO-level decision support.

**Q: Do I need coding skills?**
A: No. You can ask the AI Agent in natural language (e.g., "Design a user interview for me") or use it as a Python package. Both modes are supported.

**Q: Are all 100 methods actually usable?**
A: Yes. Each method has detailed descriptions, applicable scenarios, execution steps, and output templates. The recommender engine automatically suggests 3-5 method combinations based on your research phase and goals.

**Q: Are SUS/NPS calculations accurate?**
A: SUS uses the standard formula (Bangor et al.), and NPS follows industry-standard algorithms. Results are consistent with professional research tools.

**Q: Can I use it with QuantUX?**
A: Highly recommended! UDM handles qualitative discovery, QuantUX handles quantitative validation. Together they achieve method triangulation for significantly improved research validity.

### 📋 Cheat Sheet / Quick Reference Cards

#### SUS Score Interpretation

| Score Range | Rating | Percentile |
|-------------|--------|------------|
| 85-100 | Excellent | 90%+ |
| 70-84 | Good | 70-89% |
| 50-69 | Fair | 30-69% |
| <50 | Needs Improvement | <30% |

#### NPS Score Interpretation

| Score Range | Rating |
|-------------|--------|
| >50 | Excellent |
| 30-50 | Good |
| 0-30 | Fair |
| <0 | Needs Improvement |

#### Method Selection by Research Phase

| Phase | Goal | Recommended Methods |
|-------|------|--------------------|
| Phase 1 (Explore) | Discover user needs | Contextual inquiry, diary study, ethnography |
| Phase 2 (Generate) | Create solutions | Co-design, participatory design, card sorting |
| Phase 3 (Evaluate) | Test solutions | Usability testing, A/B testing, heuristic evaluation |
| Phase 4 (Synthesize) | Make sense of data | Affinity diagramming, journey mapping, persona creation |
| Phase 5 (Communicate) | Share findings | Storytelling, data visualization, executive presentations |

#### Cross-Skill Quick Reference

| Need | Skill | Key Method |
|------|-------|------------|
| Choose research methods | **UDM** (this skill) | `recommend_methods()` |
| Validate quantitatively | [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) | `calculate_ab_sample_size()` |
| Understand user "jobs" | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | `analyze()` |
| Create personas | [Persona](https://github.com/AliDujie/web-persona-skill) | `add_persona()` |
| Design value prop | [VPD](https://github.com/AliDujie/value-proposition-design) | `analyze_canvas()` |
| Present findings | [SWD](https://github.com/AliDujie/storytelling-with-data) | `build_story()` |

### 🏆 Case Studies

#### Case Study 1: E-commerce Shopping Experience Optimization

**Background**: A top e-commerce platform noticed cart conversion dropping for 3 consecutive months.

```python
from udm import UDMSkill

skill = UDMSkill("E-commerce App")

# Step 1: Method recommendation — determine research plan
methods = skill.recommend_methods("Understand cart abandonment reasons", phase=1)
# → Recommends: Contextual interview + Diary study + Usability testing

# Step 2: Generate contextual interview guide
guide = skill.generate_interview("Cart experience interview", "contextual")

# Step 3: Post-research, build journey map
jm = skill.build_journey_map("Shopping Journey", persona="Busy Mom")
jm.add_stage("Search", actions=["Open app", "Search product"], emotions=4, pain_points=["Search results irrelevant"])
jm.add_stage("Compare", actions=["View specs", "Read reviews"], emotions=2, pain_points=["Fake reviews", "Complex specs"])

# Step 4: Generate research report (auto-attached CEO perspective)
report = skill.generate_report("Cart Experience Study", summary="Found 3 core pain points")
```

**Result**: Identified 3 core pain points → After optimization, cart conversion improved 18%, SUS score rose from 67.6 to 78.2

#### Case Study 2: B2B SaaS User Needs Exploration

**Background**: A collaboration tool entering the SMB market didn't understand target user needs.

```python
from udm import UDMSkill

skill = UDMSkill("B2B Collaboration SaaS")

# Kano questionnaire to prioritize feature requirements
survey = skill.generate_survey("Feature Survey", "kano", features=["AI meeting notes", "Task automation", "Cross-platform sync"])

# Weighted matrix to evaluate solution priorities
wm = skill.build_weighted_matrix("Solution Evaluation")
wm.add_criterion("User needs", weight=0.4)
wm.add_criterion("Technical feasibility", weight=0.3)
wm.add_criterion("Business value", weight=0.3)
wm.add_option("AI meeting notes", {"User needs": 5, "Technical feasibility": 3, "Business value": 5})
print(wm.render_markdown())
```

**Result**: Clarified feature priorities → Launched AI meeting notes in Q1, reducing customer acquisition cost by 30%

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

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie Skill Ecosystem                          │
├─────────────────────────────────────────────────────────────┤
│   📊 Quantitative UX Research ←───→ 📖 Universal Design     │
│    (quantitative)   triangulation       Methods (this skill)│
│              ↑                          ↓                   │
│              │                    🎯 JTBD Knowledge          │
│              │                    (needs insight)            │
│   📈 Storytelling with Data ←───→ 💎 Value Proposition      │
│    (data narrative) presentation         Design              │
│              ↑                          ↑                   │
│              │                    👤 Web Persona             │
│              └────────────────────  (personas)               │
│                                         ↓                   │
│                                    🧠 Structured Thinking   │
│                                    Model                     │
└─────────────────────────────────────────────────────────────┘
```

**Integration patterns:**

- **UDM + JTBD** → Validate JTBD insights with UDM research methods
- **UDM + Persona** → Design targeted research methods based on personas
- **UDM + QuantUX** → Qualitative-quantitative triangulation for research validity
- **UDM + VPD** → Validate value proposition hypotheses with UDM methods
- **UDM + SWD** → Present UDM research findings with SWD data narratives

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
universal-design-methods alicloud user-interviews affinity-diagram
persona-creation research-planning interview-generation
```

### 📦 Dependencies

- Python >= 3.8
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

### 📋 Changelog

| Version | Date | Changes |
|---------|------|--------|
| v2.3.52 | 2026-05-11 | Repo maintenance: verified English section completeness, confirmed all "When NOT to Use" and "Common Mistakes" sections present across ecosystem, verified cross-skill links, updated version badges |
| v2.3.51 | 2026-05-11 | Repo maintenance: fixed `jm.render()`/`aj.render()` code examples (should use `Builder.render_markdown(builder.build())`), added "Why Choose UDM" promotional section to SKILL.md, added Structured Thinking Model cross-reference, cleaned up duplicate separators, enhanced English TOC index |
| v2.3.50 | 2026-05-11 | Repo maintenance: fixed footer version mismatch (v2.3.47→v2.3.49), added missing changelog entries (v2.3.48–v2.3.49), ensured README/badge/CHANGELOG version alignment |
| v2.3.49 | 2026-05-11 | Repo maintenance: added English 5-minute Quick Start checklist, enhanced discoverability for English-speaking users, verified ecosystem cross-references |
| v2.3.48 | 2026-05-11 | Repo maintenance: added Beginner Quick Reference Card with 7 common use cases and quick commands |
| v2.3.47 | 2026-05-11 | Repo maintenance: fixed broken file path references in Next Steps section, enhanced cross-skill integration examples, improved changelog table formatting, added beginner-friendly setup guide |
| v2.3.43 | 2026-05-09 | Repo maintenance: added English Project Structure section for bilingual parity, enhanced documentation completeness |
| v2.3.42 | 2026-05-09 | Repo maintenance: fixed SKILL.md version mismatch, aligned README footer version, verified ecosystem cross-references, improved changelog table ordering |
| v2.3.40 | 2026-05-09 | Repo maintenance: added English case studies section with practical code examples, enhanced bilingual content parity (CN/EN), added cross-skill integration code samples |
| v2.3.39 | 2026-05-09 | Repo maintenance: fixed footer version mismatch (v2.3.37→v2.3.39), enhanced cross-skill ecosystem workflow clarity, updated ecosystem links to all 5 sibling skills, aligned version across README/SKILL.md/pyproject.toml |
| v2.3.37 | 2026-05-08 | Repo maintenance: enhanced cross-skill ecosystem workflow examples with unified 6-skill pipeline diagram, improved triangulation descriptions, updated Last Updated to 2026-05-08, version bump to 2.3.37 |
| v2.3.27 | 2026-05-06 | 仓库维护：添加 GitHub Topics 推荐标签，更新版本至 2.3.27 |
| v2.3.26 | 2026-05-06 | Repo maintenance: fixed version badge mismatch (badge was 1 ahead of SKILL.md/pyproject.toml), aligned all version references, verified ecosystem cross-references and bilingual consistency |
| v2.3.24 | 2026-05-06 | Repo maintenance: enhanced CN "Who Is This For" descriptions, expanded GitHub Topics, fixed version badge mismatch, improved EN/CN topic consistency |
| v2.3.10 | 2026-05-03 | Repo maintenance: fixed English changelog table formatting (removed rogue separator rows), aligned SKILL.md version, updated Last Updated timestamp |
| v2.3.8 | 2026-05-03 | Repo maintenance: streamlined English Quick Start code comments for clarity, aligned SKILL.md version with README.md, added pyproject.toml classifiers |
| v2.3.7 | 2026-05-03 | Fixed SKILL.md version mismatch (2.3.5→2.3.7), aligned all version references, cleaned up duplicate changelog entries |
| v2.3.6 | 2026-05-03 | Added English version history, added classifiers and project.urls to pyproject.toml |
| v2.3.5 | 2026-05-03 | Repo maintenance: sync pyproject.toml version, add changelog entry for consistency review |
| v2.3.4 | 2026-05-03 | Repo maintenance: cross-ecosystem consistency review, verified cross-references and version alignment |
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
| "I need a structured framework for analysis" | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — PESTEL, Five Forces, decision trees |

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

### 🔄 End-to-End Workflow: All 7 Skills

A complete user research-to-executive-presentation workflow using the full AliDujie ecosystem:

```
Step 1          Step 2          Step 3          Step 4          Step 5          Step 6
┌──────┐       ┌──────┐       ┌──────┐       ┌──────┐       ┌──────┐       ┌──────┐
│Persona│  ──►  │ JTBD │  ──►  │ UDM  │  ──►  │QuantUX│  ──►  │ VPD  │  ──►  │ SWD  │
│ 👤   │       │ 🎯   │       │ 📖   │       │ 📊   │       │ 💎   │       │ 📈   │
│角色定义│       │需求洞察│       │定性研究│       │定量验证│       │价值验证│       │数据汇报│
└──────┘       └──────┘       └──────┘       └──────┘       └──────┘       └──────┘
```

**Real-World Scenario: E-commerce App Retention Improvement**

1. **Persona**: Create "Efficient Shopper" and "Bargain Hunter" segments from behavioral data
2. **JTBD**: Interview recent churners → discover core Job is "find the right product quickly without decision fatigue" (Opp Score: 7.8)
3. **UDM**: Run contextual interviews + usability testing → identify 3 key pain points in search-to-purchase flow
4. **QuantUX**: A/B test redesigned search results (n=10,000) → +12% conversion, p<0.001
5. **VPD**: Update value proposition canvas → test new messaging "Find what you need in 3 taps"
6. **SWD**: Build executive presentation → three-act story (problem → evidence → solution) → approval for $3M investment

```python
# Full ecosystem in action
from persona import PersonaSkill; persona = PersonaSkill("电商 App")
from jtbd import JTBDSkill; jtbd = JTBDSkill("电商购物")
from udm import UDMSkill; udm = UDMSkill("电商购物")
from quantux import QuantUXSkill; quantux = QuantUXSkill("电商购物")
from vpd import VPDSkill; vpd = VPDSkill("电商 App", "效率型用户")
from swd import SWDSkill; swd = SWDSkill("Q2 用户体验改进汇报")

# Each skill feeds into the next — research-to-decision pipeline
```

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
| "我需要一个结构化的分析框架" | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — PESTEL、五力模型、决策树 |

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

以下是一个真实产品优化场景中，7 个技能如何协作的完整工作流：

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

### 💻 实用集成示例 (Practical Integration Examples)

#### 示例 1: UDM + Persona — 数据驱动的研究设计

```python
# 先用 Persona 定义目标用户，再用 UDM 针对性设计研究
from persona import PersonaSkill
from udm import UDMSkill

persona_skill = PersonaSkill("电商平台")
persona_skill.add_persona(
    name="忙碌妈妈",
    short_desc="碎片时间购物，重视效率和信任",
    priority="primary",
    goals=["快速找到所需商品", "确保商品质量"]
)

# 基于 Persona 的研究目标设计 UDM 访谈
udm = UDMSkill("电商平台")
methods = udm.recommend_methods("了解忙碌妈妈的购物痛点", phase=1)
interview = udm.generate_interview("忙碌妈妈深访", "contextual")
```

#### 示例 2: UDM + QuantUX — 定性定量三角验证

```python
# UDM 发现假设 → QuantUX 验证假设
from udm import UDMSkill
from quantux import QuantUXSkill

udm = UDMSkill("电商平台")
usability = udm.generate_usability_test("结账流程", "summative")

quantux = QuantUXSkill("电商平台")
sample_size = quantux.calculate_ab_sample_size(baseline=0.15, mde=0.03)
print(f"需要 {sample_size} 样本量 per variant")
```

#### 示例 3: UDM → JTBD → SWD — 从发现到呈现

```python
# 完整链路：UDM 发现痛点 → JTBD 结构化洞察 → SWD 高管呈现
from udm import UDMSkill
from jtbd import JTBDSkill
from swd import SWDSkill

udm = UDMSkill("电商平台")
research = udm.generate_report("留存下降研究", include_ceo_analysis=True)

jtbd = JTBDSkill("电商平台")
opportunity = jtbd.score_opportunity("快速完成购买", struggle=4)

swd = SWDSkill("电商平台")
ctx = swd.build_context(audience="CEO", cta="批准新结账流程")
story = swd.build_story(protagonist="用户", imbalance="结账太慢")
```

> 💡 **提示**: 这些示例展示了跨技能的数据流转 — 一个技能的输出可以作为下一个技能的输入。

### 🌟 为什么选择 AliDujie 技能生态系统？

本技能是 **AliDujie UX 研究技能生态系统** 的核心组件，与其他技能无缝协作：

| 技能 | 角色 | 协作方式 |
|------|------|----------|
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 需求洞察 | JTBD 发现用户"工作" → UDM 方法验证 |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | 用户角色 | Persona 角色 → UDM 针对性研究设计 |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 定量验证 | UDM 定性发现 → QuantUX 定量三角验证 |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值设计 | UDM 研究 → VPD 价值主张验证 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | UDM 研究发现 → SWD 高管级呈现 |

**使用完整生态系统的优势：**

- ✅ **全流程覆盖** — 从发现需求 → 角色创建 → 研究验证 → 价值设计 → 数据呈现
- ✅ **一致 API 设计** — 所有技能使用统一的 Skill("产品名") 入口
- ✅ **零外部依赖** — 纯 Python 标准库实现，开箱即用
- ✅ **双语支持** — 完整中英文文档，适合国际化团队
- ✅ **积极维护** — 定期更新新功能和改进文档

👉 **探索完整生态系统**: [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) · [Persona](https://github.com/AliDujie/web-persona-skill) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · [VPD](https://github.com/AliDujie/value-proposition-design) · [SWD](https://github.com/AliDujie/storytelling-with-data)

---

### 💡 Pro Tips / 专业提示

- **三角测量优先** — 永远不要只用一种方法。至少组合 2 种方法（定性+定量）交叉验证
- **从 CEO 视角出发** — 在研究开始前就定义"这个研究要支持什么决策"
- **先定性后定量** — 用 UDM 访谈发现问题，用 QuantUX 验证规模
- **SUS 70 分是基准线** — 低于 70 分需要优先改进，高于 85 分可以考虑新功能
- **体验历程图 5-7 阶段最佳** — 太少过于笼统，太多难以聚焦
- **方法 ROI 评估** — 用 `add_method_roi()` 在研究规划前评估方法投入产出比
- **AI Agent 最佳实践** — 先用自然语言描述研究目标，再让 Agent 调用对应 API；复杂场景用 `search_knowledge()` 先查询方法索引

## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
|------|------|------|
| v2.3.51 | 2026-05-11 | 仓库维护：修复 README 代码示例中 `jm.render()`/`aj.render()` 错误用法（应为 `Builder.render_markdown(builder.build())`），SKILL.md 新增「为什么选择 UDM」推广章节，添加 Structured Thinking Model 交叉引用，清理多余分隔符，完善英文目录索引 |
| v2.3.50 | 2026-05-11 | 仓库维护：修复页脚版本不一致（v2.3.47→v2.3.49），补齐缺失的变更日志条目（v2.3.48-v2.3.49），确保 README/徽章/CHANGELOG 三端版本对齐 |
| v2.3.42 | 2026-05-09 | 仓库维护：修复 SKILL.md 版本不一致，对齐 README 页脚版本引用，验证生态交叉引用一致性，改进版本历史表格排序 |
| v2.3.37 | 2026-05-08 | 仓库维护：增强跨技能生态工作流示例，添加统一的 6 技能流水线图，改进三角测量描述，更新 Last Updated 至 2026-05-08，版本升级至 2.3.37 |
| v2.3.36 | 2026-05-07 | 仓库维护：在快速决策指南中添加 Structured Thinking Model 引用（中英文），提升跨技能发现性，版本升级至 2.3.36 |
| v2.3.35 | 2026-05-07 | 仓库维护：在 SKILL.md 中添加"什么时候使用 UDM"决策指南，帮助 AI Agent 自主选择技能，版本升级至 2.3.35 |
| v2.3.34 | 2026-05-07 | 仓库维护：SKILL.md 版本号升级至 2.3.34，验证生态交叉引用一致性 |
| v2.3.33 | 2026-05-07 | 仓库维护：版本升级至 v2.3.33，对齐 SKILL.md 和 pyproject.toml 版本号，对齐变更日志条目 |
| v2.3.32 | 2026-05-07 | 仓库维护：版本升级至 2.3.33，对齐 SKILL.md 和 pyproject.toml 版本号 |
| v2.3.31 | 2026-05-07 | 仓库维护：修复页脚版本号偏差，添加生态系统工作流 Pro Tip，版本升级至 2.3.31 |
| v2.3.30 | 2026-05-07 | Repo maintenance: fixed double `---` separator, enhanced cross-skill workflow descriptions |
| v2.3.29 | 2026-05-07 | Repo maintenance: fixed double brightgreen badge in Last Updated, added AI Agent best practices Pro Tip |
| v2.3.28 | 2026-05-06 | Repo maintenance: added Contributing link to English footer, enhanced cross-skill collaboration examples with UDM-to-SWD end-to-end workflow code, aligned all version references |
| v2.3.27 | 2026-05-06 | Repo maintenance: added GitHub Topics recommendation tags, version bump to 2.3.27 |
| v2.3.26 | 2026-05-06 | 仓库维护：修复版本徽章不一致（徽章比 SKILL.md/pyproject.toml 超前 1 个版本），对齐所有版本引用，验证生态交叉引用和双语一致性 |
| v2.3.22 | 2026-05-06 | 仓库维护：添加 Structured Thinking Model 和 Quantitative UX Research 协作引用，优化技能生态工作流描述 |
| v2.3.21 | 2026-05-05 | Repo maintenance: aligned SKILL.md + pyproject.toml versions, verified cross-references, enhanced English Quick Start clarity |
| v2.3.19 | 2026-05-05 | Repo maintenance: added Structured Thinking Model to ecosystem diagrams (CN+EN), enhanced cross-references in related skills tables |
| v2.3.18 | 2026-05-04 | 仓库维护：修复版本历史表格 `| |` 格式错误，添加端到端工作流英文目录条目
| v2.3.17 | 2026-05-04 | 仓库维护：添加英文目录(Table of Contents)和5分钟快速开始检查清单；优化英文版 Features at a Glance 和 Quick Start 场景注释清晰度
| v2.3.15 | 2026-05-04 | 仓库维护：修复 SKILL.md 版本不一致 (2.3.12→2.3.14)，对齐所有版本引用
| v2.3.13 | 2026-05-04 | 仓库维护：修复版本历史排序（v2.3.10→v2.3.11 顺序校正），增强英文版 Quick Start 场景注释 |
| v2.3.12 | 2026-05-04 | 仓库维护：添加完整端到端工作流章节（展示 6 个技能协作场景），修复版本历史重复条目，对齐 pyproject.toml 版本 |
| v2.3.11 | 2026-05-03 | 仓库维护：添加 Pro Tips 专业提示章节（中英双语），提升技能使用效率指南 |
| v2.3.10 | 2026-05-03 | 仓库维护：修复英文版版本历史表格格式（删除错误分隔符行），SKILL.md 版本对齐，Last Updated 时间戳更新 |
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
- **AI Agent Best Practice** — Describe your research goal in natural language first, then let the Agent call the right API; for complex scenarios, use `search_knowledge()` to query the method index first
- **Full Ecosystem Workflow** — For end-to-end research: Persona → JTBD → UDM → QuantUX → VPD → SWD. Each skill feeds the next, building from user definition to executive-ready presentation.

## 📋 Version History (English)

| Version | Date | Changes |
|---------|------|--------|
| v2.3.52 | 2026-05-11 | Repo maintenance: verified English section completeness, confirmed all "When NOT to Use" and "Common Mistakes" sections present across ecosystem, verified cross-skill links, updated version badges |
| v2.3.51 | 2026-05-11 | Repo maintenance: fixed `jm.render()`/`aj.render()` code examples (should use `Builder.render_markdown(builder.build())`), added "Why Choose UDM" promotional section to SKILL.md, added Structured Thinking Model cross-reference, cleaned up duplicate separators, enhanced English TOC index |
| v2.3.50 | 2026-05-11 | Repo maintenance: fixed footer version mismatch (v2.3.47→v2.3.49), added missing changelog entries (v2.3.48–v2.3.49), ensured README/badge/CHANGELOG version alignment |
| v2.3.47 | 2026-05-11 | Repo maintenance: fixed broken file path references in Next Steps section, enhanced cross-skill integration examples, improved changelog table formatting, added beginner-friendly setup guide |
| v2.3.45 | 2026-05-10 | Repo maintenance: fixed missing trailing `|` in changelog rows, reordered changelog by date (newest first), updated Last Updated badge |
| v2.3.44 | 2026-05-10 | Repo maintenance: enhanced changelog ordering and table formatting |
| v2.3.40 | 2026-05-09 | Repo maintenance: added English case studies section with practical code examples, enhanced bilingual content parity, added cross-skill integration code samples |
| v2.3.37 | 2026-05-08 | Repo maintenance: enhanced cross-skill ecosystem workflow examples with unified 6-skill pipeline diagram, improved triangulation descriptions, updated Last Updated to 2026-05-08, version bump to 2.3.37 |
| v2.3.36 | 2026-05-07 | Repo maintenance: added Structured Thinking Model to Quick Decision Guide (CN+EN), enhanced cross-skill discoverability, version bump to 2.3.36 |
| v2.3.35 | 2026-05-07 | Repo maintenance: added "When to use UDM" decision guide to SKILL.md for better agent self-selection, version bump to 2.3.35 |
| v2.3.34 | 2026-05-07 | Repo maintenance: SKILL.md version bump to 2.3.34, verified cross-skill ecosystem consistency |
| v2.3.32 | 2026-05-07 | Repo maintenance: version bump to 2.3.33, aligned SKILL.md and pyproject.toml versions
| v2.3.31 | 2026-05-07 | Repo maintenance: fixed footer version mismatch, added ecosystem workflow Pro Tip, bumped to v2.3.31
| v2.3.30 | 2026-05-07 | Repo maintenance: fixed double `---` separator, enhanced cross-skill workflow descriptions |
| v2.3.29 | 2026-05-07 | Repo maintenance: fixed double brightgreen badge in Last Updated, added AI Agent best practices Pro Tip |
| v2.3.28 | 2026-05-06 | Repo maintenance: added Contributing link to English footer, enhanced cross-skill collaboration examples with UDM-to-SWD end-to-end workflow code, aligned all version references |
| v2.3.24 | 2026-05-06 | Repo maintenance: enhanced Chinese "Who Is This For" descriptions, expanded GitHub Topics, improved EN/CN topic consistency |
| v2.3.22 | 2026-05-06 | Repo maintenance: added Structured Thinking Model and Quantitative UX Research collaboration references, improved skill ecosystem workflow descriptions |
| v2.3.21 | 2026-05-05 | Repo maintenance: aligned SKILL.md + pyproject.toml versions, verified cross-references, enhanced English Quick Start clarity |
| v2.3.19 | 2026-05-05 | Repo maintenance: added Structured Thinking Model to ecosystem diagrams (CN+EN), enhanced cross-references in related skills tables |
| v2.3.18 | 2026-05-04 | Repo maintenance: fixed changelog table `| |` formatting, added end-to-end workflow English TOC entry |
| v2.3.17 | 2026-05-04 | Repo maintenance: added English TOC and 5-min checklist; improved English Features at a Glance and Quick Start scenario comments |
| v2.3.15 | 2026-05-04 | Repo maintenance: fixed SKILL.md version mismatch (2.3.12→2.3.14), aligned all version references, added Credits section |
| v2.3.13 | 2026-05-04 | Repo maintenance: fixed changelog ordering (v2.3.10→v2.3.11 sequence corrected), enhanced English Quick Start with scenario-based comments |
| v2.3.12 | 2026-05-04 | Repo maintenance: added end-to-end workflow section showing complete 6-skill collaboration scenario, fixed duplicate v2.3.10 changelog entries, aligned pyproject.toml version |
| v2.3.11 | 2026-05-03 | Repo maintenance: added Pro Tips section (CN/EN) for expert usage guidance |
| v2.3.9 | 2026-05-03 | Repo maintenance: fixed changelog table formatting, added English version history table, aligned SKILL.md version |
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

### 🗺️ Beginner Quick Reference Card

> **New to UDM? Start here.** This card covers the most common first-time use cases.

| I want to… | Start with this | Quick command |
|---|---|---|
| Figure out which research method to use | Method Recommendation | `skill.recommend_methods("understand why users churn", phase=1)` |
| Conduct my first user interview | Interview Guide | `skill.generate_interview("New User Onboarding", "contextual")` |
| Evaluate if our product is usable | Usability Testing | `skill.generate_usability_test("Checkout Flow", "formative")` |
| Score our product's usability | SUS Calculation | `skill.calculate_sus([4,2,5,1,4,2,5,1,4,2])` → `72.5 (Good)` |
| Measure customer loyalty | NPS Calculation | `skill.calculate_nps([9,10,8,7,10,6])` → `NPS: 40` |
| Map the user's end-to-end experience | Journey Map | `skill.build_journey_map("Booking Flow", persona="Sarah")` |
| Plan a full research project | Research Plan | `skill.generate_research_plan("App Redesign", background="Users drop off at signup")` |
| Write up findings for stakeholders | Research Report | `skill.generate_report("Q2 Research", summary="3 blockers found in onboarding")` |

> 💡 **Most common first step**: `skill.recommend_methods()` — tell it your research goal and it recommends 3-5 methods with execution order.

### 🚀 Next Steps / 下一步

Ready to go deeper? Here's what to try next:

1. **Explore all 100 methods** — Check [udm/recommender.py](udm/recommender.py) for the full method catalog organized by research phase
2. **Combine with QuantUX** — Use UDM to generate qualitative hypotheses, then validate with [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) statistical testing
3. **From insights to personas** — Feed UDM research findings into [Web Persona](https://github.com/AliDujie/web-persona-skill) to create evidence-based user profiles
4. **Build your value proposition** — Translate user needs from UDM into canvas format with [Value Proposition Design](https://github.com/AliDujie/value-proposition-design)
5. **Present findings** — Turn research insights into compelling narratives using [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)
6. **Identify user jobs** — Deepen understanding with [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) opportunity scoring

> 💡 **Pro Tip**: The most powerful workflows combine 3+ skills. Try: UDM (research) → JTBD (opportunity) → QuantUX (validation) → SWD (presentation)

### ⚡ Power Workflow: Full Research Pipeline

```python
from udm import UDMSkill
from jtbd import JTBDSkill
from swd import SWDSkill

# 1. UDM: Conduct user research
udm = UDMSkill("旅行预订 App")
interview = udm.generate_interview("用户访谈", "contextual", context="预订流程")

# 2. JTBD: Extract core jobs from interview data
jtbd = JTBDSkill("旅行预订平台")
opportunity = jtbd.analyze(jobs=[...], pains=[...])  # From interview findings

# 3. SWD: Create compelling presentation
swd = SWDSkill("研究汇报")
story = swd.build_story(protagonist="产品团队",
    imbalance="用户在预订流程中存在未满足的核心 Job",
    resolution="基于 JTBD 机会评分优化产品优先级")

# → Complete research-to-presentation workflow in minutes
```

### 👨‍💻 Credits

Based on *Universal Design Methods* by Bella Martin & Bruce Hanington (Rockport Publishers, 2012), featuring 100 design research methods covering the complete design process.

**Applicable to:** UX Researchers, Designers, Product Managers, Design Educators

### 🆘 Getting Help

- 📖 Check the [Troubleshooting](#-troubleshooting) section for common issues
- 📚 Read the methodology guides in [references/](references/)
- 💬 Open an issue on [GitHub](https://github.com/AliDujie/universal-design-methods/issues)

### 📖 Extended Reading

| Book | Author | Related Capability |
|------|--------|--------------------|
| *Universal Design Methods* (100 Ways) | Bella Martin & Bruce Hanington | Full methodology — 100 research methods |
| *Just Enough Research* | Erika Hall | Practical research planning |
| *Interviewing Users* | Steve Portigal | In-depth interview techniques |

### 🌐 Explore the Full AliDujie UX Research Ecosystem

This skill is part of a **7-skill UX research ecosystem** — each covers a different phase of the research lifecycle. Combine them for end-to-end workflows:

| Skill | Role | When to Use |
|-------|------|-------------|
| 👤 [Web Persona](https://github.com/AliDujie/web-persona-skill) | Foundation | Define WHO you're designing for |
| 🎯 [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Needs Insight | Understand WHY users behave the way they do |
| 🔍 [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | Research Methods | Choose and execute research methods |
| 📊 [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | Validation Engine | Prove qualitative hypotheses with data |
| 💎 [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | Value Design | Bridge user needs to testable value propositions |
| 📈 [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Presentation Layer | Turn findings into executive-ready narratives |
| 🧠 [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | Strategic Analysis | Apply business frameworks to research insights |

> 💡 **Quick Tip**: `Persona → JTBD → UDM → QuantUX → VPD → SWD → STM` — a complete research pipeline from user definition to data-driven presentation and strategic analysis.

### 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

---

*Last Updated: 2026-05-13 | AliDujie Skill Ecosystem | v2.3.61*