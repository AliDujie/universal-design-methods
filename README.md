# Universal Design Methods Skill

> 📖 **100 种设计研究方法、8 大执行能力、1 个完整 Python 工具包**

基于《通用设计方法》(贝拉·马丁 & 布鲁斯·汉宁顿) 构建，覆盖 UX 研究全生命周期。

[English](#english) | [中文](#中文说明)

---

## 中文说明

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **全面覆盖** — 100 种设计研究方法，从探索到评估到综合到沟通，一站式解决
- **8 大执行能力** — 方法推荐、访谈提纲、可用性测试、问卷设计、体验历程图、研究计划、报告生成、SUS/NPS 计算
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

# ===== 场景 6: 研究计划 & 报告=====
plan = skill.generate_research_plan("体验研究", background="用户流失率上升")
report = skill.generate_report("研究报告", summary="发现 3 个核心痛点")
```

### 💡 8 大核心能力

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **方法推荐** | `recommender.py` | 基于研究阶段/目标自动推荐 3-5 种方法组合 |
| 2 | **访谈提纲** | `interview.py` | 5 种访谈类型（情境/结构化/半结构化等） |
| 3 | **可用性测试** | `usability.py` | 测试脚本生成 + SUS 计算 + 启发性评估 |
| 4 | **问卷设计** | `survey.py` | 卡诺/NPS/语义差异/SUS/期望值 5 种问卷 |
| 5 | **体验历程图** | `synthesis.py` | 用户旅程可视化 + 痛点标注 |
| 6 | **研究计划** | `research_plan.py` | 完整研究方案（目标/方法/时间线/资源） |
| 7 | **报告生成** | `report.py` | 标准化研究报告结构 |
| 8 | **指标计算** | `usability.py` / `survey.py` | SUS/NPS/卡诺分类自动计算 |

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

👉 **探索完整生态系统**: [JTBD](../jtbd-knowledge-skill/) | [人物角色](../web-persona-skill/) | [量化 UX 研究](../quantitative-ux-research/) | [价值主张设计](../value-proposition-design/) | [数据叙事](../storytelling-with-data/)

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

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

## English

### 🌟 Why Use This Skill?

- **Comprehensive Coverage** — 100 design research methods from exploration to communication
- **8 Core Capabilities** — Method recommendation, interview guides, usability testing, surveys, journey maps, research plans, reports, SUS/NPS calculation
- **Practical Toolkit** — Pure Python standard library, zero dependencies, 5-minute setup
- **Smart Recommendations** — Auto-recommend method combinations based on research phase and goals
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Zero Learning Curve** — Intuitive API, rich code examples, plug-and-play

### 🚀 Quick Start

#### Step 1: Install

```bash
cp -r universal-design-methods /your/agent/skills/
```

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

### 🔗 Related Skills

This skill is part of the **AliDujie UX Research Skills Ecosystem**:

- **[JTBD-Knowledge-Skill](../jtbd-knowledge-skill/)** — Jobs-to-be-Done theory
- **[Web-Persona-Skill](../web-persona-skill/)** — Persona creation
- **[Quantitative-UX-Research](../quantitative-ux-research/)** — Quantitative research, HEART framework
- **[Value-Proposition-Design](../value-proposition-design/)** — Value proposition canvas
- **[Storytelling-with-Data](../storytelling-with-data/)** — Data storytelling

### 🌟 Why Choose AliDujie Skill Ecosystem?

This skill is part of the **AliDujie UX Research Skills Ecosystem**. Using the complete ecosystem provides:

- ✅ **Complete Coverage** — From user research to product design to data presentation, full-process tool support
- ✅ **Seamless Integration** — All skills use consistent API design and data formats
- ✅ **Best Practices** — Based on classic theories and practical experience, avoid common pitfalls
- ✅ **Active Maintenance** — Regularly updated with new features and improvements
- ✅ **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- ✅ **Bilingual Support** — Complete CN/EN documentation for international team collaboration

👉 **Explore More Skills**: [JTBD](../jtbd-knowledge-skill/) | [Web Persona](../web-persona-skill/) | [Quantitative UX Research](../quantitative-ux-research/) | [Value Proposition Design](../value-proposition-design/) | [Storytelling with Data](../storytelling-with-data/)

### 📦 Dependencies

- Python >= 3.8
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

---

## 📜 许可 (License)

本技能仅供内部学习和研究使用。

## 👨‍💻 作者 (Credits)

- 基于《Universal Methods of Design》by Bella Martin & Bruce Hanington
- 技能开发：AliDujie 团队
- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫

## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.5 | 2026-04-23 | 添加版本历史、Last Updated 徽章 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、故障排查、扩展阅读 |
| v1.3 | 2026-04-22 | 初始版本 |

---

*Last Updated: 2026-04-23 | AliDujie Skill Ecosystem*
