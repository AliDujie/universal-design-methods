# Universal Design Methods (UDM) — Usage Guide

> 通用设计方法 · 使用指南

## 📐 Where UDM Fits in the Pipeline

```
Persona (Who) → JTBD (What) → UDM (How to Research) → QuantUX (Validate) → VPD (Value) → SWD (Present)
                                            ↑
                                       UDM sits here — the methodology engine
```

- **After** Persona & JTBD define users and their Jobs
- **Before** QuantUX validates hypotheses statistically
- **UDM** recommends methods, generates interview guides, runs usability tests, and produces reports

## ⚡ 5-Minute Quick Start / 5分钟快速开始

```bash
# 1. Install
cp -r universal-design-methods /your/agent/skills/

# 2. Use
python -c "from udm import UDMSkill; print(UDMSkill('My Product').recommend_methods('Understand user churn', phase=1))"
```

## 🔑 Core Workflows / 核心工作流

### 1. Research Planning / 研究规划

```python
from udm import UDMSkill

udm = UDMSkill("E-commerce App")

# Recommend methods for your research goal
methods = udm.recommend_methods("Understand why users abandon carts", phase=4)
# Returns 3-5 complementary methods with triangulation logic

# Generate a full research plan
plan = udm.generate_research_plan("Cart Abandonment Study")
plan.add_objective("Identify friction points in checkout flow", priority=1)
plan.add_method(48, "Formative usability test", "Find usability issues", participants=8, days=5)
```

### 2. Interview Design / 访谈设计

```python
# 5 interview types: contextual, semi_structured, laddering, critical_incident, directed_storytelling
guide = udm.generate_interview("Shopping Experience", "contextual", context="Online checkout")
print(guide)
# → Opening warm-up → Core questions (by dimension, with priority) → Probes → Closing
```

### 3. Usability Testing / 可用性测试

```python
# Generate test scripts (formative/summative/comparative/RITE)
test = udm.generate_usability_test("Checkout Flow", "formative")

# Run heuristic evaluation (Nielsen's 10 heuristics)
checklist = udm.generate_heuristic_checklist()

# Calculate SUS score (0-100, A-F grading)
sus = udm.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])
# → {'score': '85.0', 'grade': 'A'}

# Calculate NPS
nps = udm.calculate_nps([9, 10, 8, 7, 10, 6, 9, 8, 10, 5])
# → {'nps': 30.0, 'level': 'Good'}
```

### 4. Journey Mapping / 体验历程图

```python
jm = udm.build_journey_map("Checkout Experience", persona="Shopper")
jm.add_stage("Browse", actions=["Search products"], emotions=4, pain_points=["Filter too basic"])
jm.add_stage("Cart", actions=["Add to cart"], emotions=3, pain_points=["Shipping cost surprise"])
jm.add_stage("Checkout", actions=["Enter payment"], emotions=2, pain_points=["Form too long", "No guest checkout"])
```

### 5. CEO Decision Support / CEO 决策支持

```python
# Auto-included when generating research plans or reports
plan = udm.generate_research_plan("UX Audit", include_ceo_analysis=True)

# Or call directly
roi = udm.add_method_roi(methods=["Contextual Inquiry", "Usability Test"])
decision = udm.generate_decision_outputs("How to reduce cart abandonment?")
resource = udm.generate_resource_allocation({"total": 200000, "headcount": 3, "timeline": "6 weeks"})
```

## 📋 Common Scenarios / 常见场景

| Scenario | Methods | API Calls |
|----------|---------|-----------|
| New product discovery | Contextual inquiry + Diary study | `recommend_methods(goal, phase=1)` → `generate_interview()` |
| Usability audit | Heuristic eval + Usability test | `generate_heuristic_checklist()` → `generate_usability_test()` → `calculate_sus()` |
| Feature validation | A/B test planning + Survey | `recommend_methods(goal, phase=4)` → `generate_survey("kano")` |
| Competitive analysis | Comparative test + Expert review | `generate_usability_test("comparative")` → `generate_heuristic_checklist()` |
| Research report | Full pipeline | `generate_report()` → auto-includes CEO ROI + resource allocation |
| Lean UX sprint (2 weeks) | Interviews + Affinity + SUS | `generate_interview()` → affinity diagram → `calculate_sus()` |

### 🏥 Healthcare Portal Usability Audit — Full Example

```python
from udm import UDMSkill

udm = UDMSkill("Healthcare Portal")

# Step 1: Heuristic evaluation (Nielsen's 10 heuristics)
checklist = udm.generate_heuristic_checklist()
print(checklist)

# Step 2: Formative usability test
test = udm.generate_usability_test("Patient Registration Flow", "formative")
print(test)

# Step 3: SUS scoring after testing
sus = udm.calculate_sus([3, 2, 4, 1, 3, 2, 4, 1, 3, 2])
# → {'score': '77.5', 'grade': 'B'}  (above industry average 68)

# Step 4: Journey map of pain points
jm = udm.build_journey_map("Patient Portal", persona="Elderly Patient")
jm.add_stage("Login", actions=["Navigate to portal"], emotions=2,
             pain_points=["Forgot password flow is confusing"])
jm.add_stage("View Records", actions=["Click lab results"], emotions=3,
             pain_points=["Medical jargon is hard to understand"])

# Step 5: Full research report with CEO ROI
report = udm.generate_report("Healthcare Portal Usability Audit",
    summary="Identified 5 critical issues, SUS score 77.5 (Grade B)")
report.add_finding("Password recovery too complex",
    "Users abandon portal when they can't log in",
    severity=4, recommendation="Simplify to SMS OTP")
```

### 🛒 E-Commerce Feature Prioritization — Kano + Journey Map

```python
from udm import UDMSkill

udm = UDMSkill("E-commerce App")

# Kano survey to classify features by user perception
survey = udm.generate_survey("Feature Prioritization", "kano",
    features=["One-click reorder", "AI size recommender", "Live chat support"])
print(survey)

# Journey map of current checkout experience
jm = udm.build_journey_map("Mobile Checkout", persona="First-time Buyer")
jm.add_stage("Product Page", actions=["Select size/color"], emotions=3,
             pain_points=["Size chart is confusing"])
jm.add_stage("Cart", actions=["Add to cart"], emotions=4,
             pain_points=["No clear shipping cost estimate"])
jm.add_stage("Payment", actions=["Enter card details"], emotions=2,
             pain_points=["No Apple Pay option", "Form validation errors unclear"])

# Research plan with resource allocation
plan = udm.generate_research_plan("Checkout Optimization Study")
plan.add_objective("Identify friction points causing cart abandonment", priority=1)
plan.add_method(48, "Formative usability testing", "Observe real checkout behavior",
    participants=8, days=5)
plan.add_method(71, "Kano survey", "Prioritize feature development", participants=100, days=7)
```

### 🌟 中文快速示例：旅行应用用户研究

```python
from udm import UDMSkill

udm = UDMSkill("旅行预订App")

# 1. 方法推荐 — 自动混合定性+定量
methods = udm.recommend_methods("了解用户为什么取消预订", phase=1)

# 2. 情境访谈提纲
guide = udm.generate_interview("取消预订原因", "contextual", context="酒店预订")

# 3. SUS 评分
sus = udm.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])
# → {'score': '85.0', 'grade': 'A'}  (优秀)

# 4. 完整研究报告（含 CEO 决策分析）
report = udm.generate_report("酒店预订体验研究")
report.add_finding("比价功能缺失",
    "用户需要切换多个 App 比较价格",
    severity=3, recommendation="内置一键比价功能")
```

## 🔗 Ecosystem Integration / 生态协作

```python
# Persona (who) → JTBD (what) → UDM (how) → QuantUX (validate) → VPD (value) → SWD (present)
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from quantux import QuantUXSkill
from vpd import VPDSkill
from swd import SWDSkill

# Example: E-commerce checkout optimization
persona = PersonaSkill("E-commerce")
persona.add_persona(name="Quick Shopper", archetype="Efficiency User", priority="primary",
    goals=["Complete purchase in under 2 minutes"],
    behaviors=["Uses search, skips browsing"], bio="Busy professional")

jtbd = JTBDSkill("E-commerce")
score = jtbd.score_opportunity("Find and buy quickly", struggle=4, alternative=3, market=5, budget=4)

udm = UDMSkill("E-commerce")
interview = udm.generate_interview("Quick Shopper", "contextual", context="Checkout flow")
plan = udm.generate_research_plan("Checkout UX Study", include_ceo_analysis=True)

quantux = QuantUXSkill("E-commerce")
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.05)

vpd = VPDSkill("E-commerce", "Quick Shoppers")
canvas = vpd.analyze_canvas(product_name="Quick Checkout",
    jobs=[{"description": "Buy quickly", "importance": 5}],
    pains=[{"description": "Too many steps", "severity": "critical"}])

swd = SWDSkill("Checkout Study")
story = swd.build_story(protagonist="Product Team",
    imbalance="Checkout takes 5 minutes, industry standard is 2",
    call_to_action="Simplify to one-page checkout")
```

## ⛔ When NOT to Use UDM / 何时不使用

UDM is the methodology core — pick methods, run research, produce reports. Use other AliDujie skills when:

| Need | Use Instead | Why |
|------|-------------|-----|
| Pure statistical analysis / A/B testing | [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) | Sample size calc, HEART metrics, MaxDiff |
| Creating user personas | [Web Persona](https://github.com/AliDujie/web-persona-skill) | Evidence-driven persona creation |
| Data visualization & storytelling | [SWD](https://github.com/AliDujie/storytelling-with-data) | Chart recommendations, executive narratives |
| Jobs-to-be-Done analysis | [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 4-school fusion, opportunity scoring |
| Value proposition canvas | [VPD](https://github.com/AliDujie/value-proposition-design) | VPD canvas, Blue Ocean strategy |
| Strategic business frameworks | [STM](https://github.com/AliDujie/Structured-Thinking-Model) | SWOT, Porter's 5 Forces, BCG matrix |

> 💡 **Better together**: UDM + these skills cover the full UX research lifecycle. Start with UDM for method selection, then chain downstream. See the [Ecosystem Integration](#-ecosystem-integration--生态协作) section above for code examples.

## 🧪 Testing / 测试

```bash
cd universal-design-methods
python udm/tests/test_all.py
# Or: python -m pytest udm/tests/test_all.py -v
```

## 📚 Resources / 资源

- [README.md](README.md) — Full documentation
- [SKILL.md](SKILL.md) — Agent-facing skill definition
- [INSTALL.md](INSTALL.md) — Installation guide
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [SECURITY.md](SECURITY.md) — Security policy

### 🔗 Related AliDujie Skills / 相关技能

| Skill | Use When | GitHub |
|-------|----------|--------|
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Structure Jobs from interview data | `JTBDSkill` |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | Validate qualitative findings statistically | `QuantUXSkill` |
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | Create personas from UDM research data | `PersonaSkill` |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | Map user research to value propositions | `VPDSkill` |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Present research findings to executives | `SWDSkill` |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | Strategic business analysis | `STMSkill` |
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | Research ROI → CEO strategic decisions | `CEOAdvisor` |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | UDM user findings → product strategy | `CPOAdvisor` |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | Tech usability → infrastructure decisions | `CTOSkill` |

## 💡 Pro Tips / 专业技巧

1. **Always start with `recommend_methods()`** — Before diving into a specific API, let UDM's triangulation engine suggest 3-5 complementary methods for your research goal. It automatically mixes qualitative and quantitative approaches so you don't miss blind spots.
2. **Pair qual + quant for credible findings** — Run at least one qualitative method (e.g., `generate_interview("contextual")`) alongside one quantitative method (e.g., `calculate_sus()` or `generate_survey("kano")`). Stakeholders trust findings backed by both types of evidence.
3. **Use `include_ceo_analysis=True` when pitching research budgets** — It auto-attaches ROI scoring, P0/P1/P2 prioritization, and resource allocation advice. Helps you speak the stakeholder's language before anyone asks "what's the return?"
4. **Chain synthesis outputs downstream** — Journey maps, affinity diagrams, and persona outputs from UDM feed directly into JTBD opportunity scoring, VPD canvas filling, and SWD executive storytelling. Don't let artifacts sit in a folder — wire them into the next skill.
5. **Lean UX Sprint (2-week minimum)** — For time-constrained teams: 5-8 contextual interviews (capability 2) → affinity diagram synthesis (capability 6) → quick SUS usability test (capability 4). This gives you qual + quant triangulation without a full research cycle.

**始终从 `recommend_methods()` 开始** — 在具体使用某个 API 之前，让 UDM 的三角测量引擎为你推荐 3-5 种互补的方法。它自动混合定性和定量方法，避免盲区。

**定性+定量搭配，结论更有说服力** — 至少运行一种定性方法（如 `generate_interview("contextual")`）和一种定量方法（如 `calculate_sus()` 或 `generate_survey("kano")`）。同时拥有两类证据的研究结果更容易获得利益相关者信任。

**推销研究预算时使用 `include_ceo_analysis=True`** — 自动附加 ROI 评分、P0/P1/P2 优先级排序和资源分配建议。在有人问"回报是什么"之前，用利益相关者的语言回答。

**把综合产出串联到下游技能** — UDM 产出的体验历程图、亲和图和角色画像可以直接输入 JTBD 机会评分、VPD 画布填充和 SWD 高管叙事。不要让文档躺在文件夹里——把它们接入下一个技能。

**精益 UX 冲刺（2 周最简方案）** — 时间紧张的团队：5-8 次情境访谈（能力二）→ 亲和图综合（能力六）→ 快速 SUS 测试（能力四）。定性+定量三角测量，无需完整研究周期。

## ❓ FAQ / Troubleshooting

**Q: I have 50 methods — which do I pick first?**
Don't pick manually. Use `recommend_methods()` with your research goal and it will auto-suggest 3-5 complementary methods with triangulation logic.
*不要手动选。用 `recommend_methods()` 输入研究目标，系统自动推荐 3-5 种互补方法。*

**Q: Can I use UDM for agile sprints?**
Yes — use the 2-week lean sprint template: 5 interviews → affinity diagram → SUS test. See the Research Sprint Template in README.md.
*可以——使用 2 周精益冲刺模板：5 次访谈→亲和图→SUS 测试。详见 README 中的 Research Sprint Template。*

**Q: My stakeholders don't value qualitative research — how do I change that?**
Use `generate_research_plan(include_ceo_analysis=True)` to attach ROI scoring and resource allocation. Speak their language: time saved, risk reduced, revenue impact.
*用 `generate_research_plan(include_ceo_analysis=True)` 附加 ROI 评分。用他们的语言说话：节省时间、降低风险、收入影响。*

**Q: How does UDM chain with other skills?**
UDM is the methodology engine: Persona/JTBD define who and what → UDM runs research → QuantUX validates → VPD maps value → SWD presents. See ecosystem pipeline in README.md.
*UDM 是方法论引擎：Persona/JTBD 定义用户和需求→UDM 执行研究→QuantUX 验证→VPD 映射价值→SWD 呈现。*
