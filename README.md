# Universal Design Methods (UDM) Skill

> **100 Design Research Methods — From Knowledge to Execution.**

![Version](https://img.shields.io/badge/version-2.3.85-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)

Based on *Universal Design Methods* by Bella Martin & Bruce Hanington (2012). A complete toolkit covering **100 design research methods** across 5 phases, with **11 executable capabilities** — from method recommendation to interview guides, usability testing, journey maps, research plans, reports, and CEO-level ROI analysis.

## 💼 Why Teams Choose UDM

| Challenge | Without UDM | With UDM |
|-----------|------------|----------|
| Research Planning | Hours studying methodology | Instant 3-method combo recommendation |
| Interview Guides | Inconsistent quality | 5 structured types, out of the box |
| Usability Testing | Ad-hoc checklists | Built-in SUS scoring + heuristic evaluation |
| Survey Design | Copy-paste templates | 5 survey types including Kano/NPS |
| Research Reports | Free-form, missing key info | Standardized format + CEO decision support |

## 🌟 Why UDM?

- **100 methods covered** — From exploration to communication, one-stop solution for all research needs
- **11 executable capabilities** — Not just knowledge, but produces interview guides, test scripts, surveys, journey maps, research plans, and reports
- **Smart triangulation** — Auto-recommends 3-5 method combos, mixing qual + quant, improving research reliability
- **Zero learning curve** — Pure Python standard library, no external dependencies, `from udm import UDMSkill` to start
- **CEO decision perspective** — Auto-attaches ROI assessment, resource allocation advice, helps you articulate research value
- **Bilingual support** — Full CN/EN documentation, suitable for international teams
- **Ecosystem core** — Seamlessly collaborates with JTBD, QuantUX, Persona, VPD, SWD (5 skills), covering the full user research lifecycle

## ⚡ Quick Start (5 Minutes)

### Install

```bash
# Copy the skill to your agent's skills directory
cp -r universal-design-methods /your/agent/skills/
```

### Use in Python

```python
from udm import UDMSkill

# Initialize with your product name
skill = UDMSkill("Travel Booking Platform")

# 1. Recommend research methods
methods = skill.recommend_methods("Understand why users churn", phase=1)
print(methods)

# 2. Generate interview guide
guide = skill.generate_interview("User Deep Dive", "contextual", context="Hotel booking experience")
print(guide)

# 3. Calculate SUS score
result = skill.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])
# → {'score': '85.0', 'grade': 'A'}

# 4. Build a journey map
jm = skill.build_journey_map("Booking Process", persona="Business Traveler")
jm.add_stage("Search", actions=["Open app"], emotions=4, pain_points=["Confusing sorting"])
jm.add_stage("Compare", actions=["Switch between apps"], emotions=2, pain_points=["Time-consuming"])
from udm.synthesis import JourneyMapBuilder
print(JourneyMapBuilder.render_markdown(jm.build()))

# 5. Full research plan (with CEO ROI analysis)
plan = skill.generate_research_plan("Hotel Booking UX Research", background="Users report complex booking flow")
from udm.research_plan import ResearchPlanBuilder
print(ResearchPlanBuilder.render_markdown(plan.build()))
```

**Zero dependencies** — pure Python standard library. No `pip install` needed.

## 🧩 11 Executable Capabilities

| # | Capability | What It Does |
|---|-----------|-------------|
| 1 | **Smart Method Recommendation** | Auto-recommends 3-5 methods with triangulation (qual + quant) |
| 2 | **Interview Guide Generation** | 5 types: contextual, semi-structured, laddering, critical incident, directed storytelling |
| 3 | **Observation Records** | 4 types: fly-on-wall, participant, shadowing, behavioral mapping + AEIOU framework |
| 4 | **Usability Testing** | Formative/summative/comparative/RITE, heuristic evaluation, SUS scoring, severity rating |
| 5 | **Survey & Scale Design** | Kano, semantic differential, NPS, SUS, desirability testing |
| 6 | **Comprehensive Analysis** | Affinity diagrams, persona building, journey maps, Elito method, weighted matrices |
| 7 | **Research Plan Generation** | Complete plans with objectives, methods, participants, timeline, budget, risk |
| 8 | **Research Report Generation** | Structured reports: executive summary, findings (by severity), design recommendations |
| 9 | **CEO: Method ROI Assessment** | ROI scoring for research methods, P0/P1/P2 prioritization |
| 10 | **CEO: Decision Outputs** | Expected decision outcomes from research completion |
| 11 | **CEO: Resource Allocation** | Budget, headcount, timeline allocation with risk assessment |

## 📐 Design Five Phases

1. **Planning & Scoping** — Explore and define project boundaries
2. **Exploration & Synthesis** — Infer design implications
3. **Concept Generation** — Derivative design activities
4. **Evaluation & Refinement** — Assess, refine, and produce
5. **Launch & Monitoring** — Ongoing review and correction

## 🌐 Ecosystem Integration

UDM is the **methodology core** of the AliDujie UX Research Ecosystem:

```
Persona → JTBD/UDM → QuantUX → VPD → SWD → STM
```

| Upstream | Downstream | Collaboration |
|----------|-----------|---------------|
| Persona (user data) | JTBD (need insights) | UDM interviews → JTBD structured analysis |
| JTBD (Jobs discovery) | QuantUX (quantitative validation) | UDM qualitative → QuantUX A/B testing |
| UDM (method selection) | VPD (value proposition) | UDM user research → VPD canvas filling |
| UDM (findings) | SWD (data storytelling) | UDM reports → SWD executive presentations |
| UDM (insights) | STM (strategic frameworks) | UDM methods → STM strategic analysis |

Cross-skill example:
```python
# UDM → JTBD → VPD end-to-end
from udm import UDMSkill
from jtbd import JTBDSkill
from vpd import VPDSkill

udm = UDMSkill("Travel Booking")
interview = udm.generate_interview("Business Users", "contextual")

jtbd = JTBDSkill("Travel Booking Platform")
opportunity = jtbd.score_opportunity("Find suitable hotel quickly", struggle=4, alternative=3, market=4, budget=4)

vpd = VPDSkill("Travel Booking", "Business Travelers")
canvas = vpd.analyze_canvas(product_name="Travel Booking", jobs=[{"description": "Find hotel quickly"}])
```

## 📖 Knowledge Base

| Document | Topic | Linked Capabilities |
|----------|-------|-------------------|
| `references/methods-exploration.md` | Exploratory research methods | 1, 2, 3 |
| `references/methods-generative.md` | Generative research methods | 1, 6 |
| `references/methods-evaluative.md` | Evaluative research methods | 4, 5 |
| `references/methods-synthesis.md` | Synthesis & analysis methods | 6 |
| `references/methods-communication.md` | Communication & reporting methods | 7, 8 |
| `references/execution-templates.md` | Execution template library | All |
| `references/decision-framework.md` | Decision framework & quick reference | 1 |

## 📁 Project Structure

```
universal-design-methods/
├── SKILL.md              # Agent-facing skill definition
├── README.md             # This file — GitHub landing page
├── pyproject.toml        # Package configuration
├── INSTALL.md            # Detailed installation guide
├── CHANGELOG.md          # Version history
├── LICENSE               # MIT License
├── CODE_OF_CONDUCT.md    # Community standards
├── references/           # 7 knowledge base documents
├── udm/                  # Python executable toolkit
│   ├── __init__.py       # UDMSkill unified entry point
│   ├── config.py         # 100-method index
│   ├── utils.py          # Knowledge base search
│   ├── templates.py      # Execution templates
│   ├── interview.py      # Interview guide generator
│   ├── observation.py    # Observation record generator
│   ├── usability.py      # Usability testing + SUS
│   ├── survey.py         # Survey design + Kano + NPS
│   ├── synthesis.py      # Affinity/persona/journey/Elito/matrix
│   ├── recommender.py    # Method recommendation engine
│   ├── research_plan.py  # Research plan generator
│   ├── report.py         # Research report generator
│   └── tests/
│       └── test_all.py   # Test suite
└── .github/              # CI/CD workflows & issue templates
```

## 🧪 Testing

```bash
cd universal-design-methods
python udm/tests/test_all.py
# Or with pytest:
python -m pytest udm/tests/test_all.py -v
```

## 📋 When NOT to Use UDM

- **Pure A/B testing or statistical analysis** → Use [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research)
- **Creating user personas** → Use [Web Persona](https://github.com/AliDujie/web-persona-skill)
- **Data visualization & storytelling** → Use [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)
- **Jobs-to-be-Done analysis** → Use [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill)
- **Value proposition canvas** → Use [Value Proposition Design](https://github.com/AliDujie/value-proposition-design)
- **Business framework analysis** → Use [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model)

## 📚 References

| Book | Author | Contribution |
|------|--------|-------------|
| **Universal Design Methods** | Bella Martin & Bruce Hanington (2012) | Foundation — 100 design research methods |
| Just Enough Research | Erika Hall (2013) | Lean research method selection |
| The Design of Everyday Things | Don Norman (2013) | Usability evaluation principles |
| Sprint | Jake Knapp (2016) | Rapid design sprint methods |

## 🔗 Extended Ecosystem

| Extended Skill | Collaboration Scenario |
|---------------|----------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | Research ROI → CEO strategic decisions |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | UDM user findings → CPO product strategy |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | User insights → CMO brand positioning |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | Research reports → CEO plan review |

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
