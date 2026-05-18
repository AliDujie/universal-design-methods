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

- **Pure statistical analysis / A/B testing** → Use [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research)
- **Creating personas** → Use [Web Persona](https://github.com/AliDujie/web-persona-skill)
- **Data visualization** → Use [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)
- **JTBD analysis** → Use [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill)
- **Value proposition canvas** → Use [Value Proposition Design](https://github.com/AliDujie/value-proposition-design)

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
