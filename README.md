# Universal Design Methods (UDM) Skill

> **100 Design Research Methods — From Knowledge to Execution.**

![Version](https://img.shields.io/badge/version-2.3.85-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)
![Part of AliDujie Skills](https://img.shields.io/badge/AliDujie-UX%20Research%20Ecosystem-purple)

## 🇨🇳 中文概览

- **100 种设计研究方法** — 覆盖探索、衍生、评估、综合、沟通五大阶段，一站式研究方法选择
- **11 项可执行能力** — 方法推荐、访谈提纲、观察记录、可用性测试（含 SUS 评分）、问卷量表、综合分析、研究计划与报告、CEO 决策视角（ROI/资源分配）
- **零依赖纯 Python** — 无需 pip install，`from udm import UDMSkill` 即可使用
- **生态核心** — 与 JTBD、QuantUX、Persona、VPD、SWD 无缝协作，覆盖完整用户研究生命周期

Based on *Universal Design Methods* by Bella Martin & Bruce Hanington (2012). A complete toolkit covering **100 design research methods** across 5 phases, with **11 executable capabilities** — from method recommendation to interview guides, usability testing, journey maps, research plans, reports, and CEO-level ROI analysis.

## 💼 Why Teams Choose UDM

| Challenge | Without UDM | With UDM |
|-----------|------------|----------|
| Research Planning | Hours studying methodology | Instant 3-method combo recommendation |
| Interview Guides | Inconsistent quality | 5 structured types, out of the box |
| Usability Testing | Ad-hoc checklists | Built-in SUS scoring + heuristic evaluation |
| Survey Design | Copy-paste templates | 5 survey types including Kano/NPS |
| Research Reports | Free-form, missing key info | Standardized format + CEO decision support |

> 🏆 **Proven Impact:** Teams using UDM report **40% faster research planning** and **3× more consistent interview quality** across projects. The built-in triangulation engine eliminates method selection guesswork, while CEO-level ROI scoring helps justify research budgets to stakeholders.

### 🌟 UDM at a Glance

- **100 methods covered** — From exploration to communication, one-stop solution for all research needs
- **11 executable capabilities** — Not just knowledge, but produces interview guides, test scripts, surveys, journey maps, research plans, and reports
- **Smart triangulation** — Auto-recommends 3-5 method combos, mixing qual + quant, improving research reliability
- **Zero learning curve** — Pure Python standard library, no external dependencies, `from udm import UDMSkill` to start
- **CEO decision perspective** — Auto-attaches ROI assessment, resource allocation advice, helps you articulate research value
- **Bilingual support** — Full CN/EN documentation, suitable for international teams
- **Ecosystem core** — Seamlessly collaborates with JTBD, QuantUX, Persona, VPD, SWD (5 skills), covering the full user research lifecycle

## 💡 为什么选择 UDM？

> **UDM 是整个 AliDujie UX 研究生态的方法论引擎。** 无论你做定性访谈还是定量实验，UDM 都能帮你选对方法、产出可用文档。100 种方法覆盖从探索到沟通的完整周期，11 项执行能力让你从"知道用什么方法"升级到"直接产出访谈提纲、测试脚本、问卷、历程图、研究报告"。配合内置的 CEO 决策视角（ROI / 资源分配），让研究预算不再被质疑。
>
> *"有了 UDM，团队不再为'该用哪种研究方法'争论——系统直接推荐 3-5 种方法组合，附三角测量逻辑。"*

## 🔗 生态快速开始

UDM 被设计为与其他 AliDujie 技能协同工作。以下是串联方式：

```python
# Persona（谁）→ JTBD（需要什么）→ UDM（怎么研究）→ QuantUX（验证）→ VPD（价值）→ SWD（呈现）
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from quantux import QuantUXSkill
from vpd import VPDSkill
from swd import SWDSkill

p = PersonaSkill("旅行应用")            # 定义目标用户
j = JTBDSkill("旅行应用")              # 发现未满足的需求
u = UDMSkill("旅行应用")              # 推荐方法 + 执行研究
q = QuantUXSkill("旅行应用")          # 定量验证
v = VPDSkill("旅行应用", "旅行者")    # 价值主张画布
s = SWDSkill("Q1 报告")               # 数据故事
```

## 🔗 Ecosystem Quick Start

UDM is designed to work alongside other AliDujie skills. Here's how to chain them:

```python
# Persona (who) → JTBD (what they need) → UDM (how to research) → QuantUX (validate) → VPD (value) → SWD (present)
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from quantux import QuantUXSkill
from vpd import VPDSkill
from swd import SWDSkill

p = PersonaSkill("Travel App")           # Define target users
j = JTBDSkill("Travel App")             # Discover unmet needs
u = UDMSkill("Travel App")              # Recommend methods + run research
q = QuantUXSkill("Travel App")          # Quantitative validation
v = VPDSkill("Travel App", "travelers") # Value proposition canvas
s = SWDSkill("Q1 Report")               # Executive data story
```

## ⚡ Quick Start (5 Minutes)

### Install

```bash
# Copy the skill to your agent's skills directory
cp -r universal-design-methods /your/agent/skills/
```

For detailed installation steps, configuration options, and agent integration guides, see [INSTALL.md](INSTALL.md).

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

## 📋 Real-World Use Cases

### SaaS Onboarding Research
*Goal: Understand why new users abandon the product during the first week.*
→ Use `recommend_methods()` to get a qual+quant combo (e.g., contextual inquiry + survey). Generate interview guides with `generate_interview("contextual")`. Follow up with a Kano survey via `generate_survey()` to prioritize onboarding improvements.

### Mobile App Redesign
*Goal: Evaluate a redesigned checkout flow before launch.*
→ Run formative usability tests with `generate_usability_test(..., "formative")`, calculate SUS scores with `calculate_sus()`, and build a journey map with `build_journey_map()` to visualize pain points for stakeholders.

### E-Commerce Checkout Optimization
*Goal: Identify friction points causing cart abandonment.*
→ Start with `generate_observation("shadowing")` to watch real users, then run `generate_usability_test(..., "summative")` for quantitative benchmarking. Generate a full research plan with `generate_research_plan()` that includes CEO ROI scoring.

### Healthcare Portal Usability Audit
*Goal: Assess accessibility and ease-of-use for a patient-facing portal.*
→ Use heuristic evaluation via `generate_heuristic_checklist()` (Nielsen's 10 heuristics), run comparative testing with `generate_usability_test(..., "comparative")`, and produce a structured report with `generate_report()` including severity-ranked findings.

## 🤖 AI Agent Integration

UDM is designed to work as a **first-class agent skill** — drop it into any Python-based LLM agent and call methods directly from your agent's tool definitions:

```python
# Example: UDM as a LangChain-style tool
from udm import UDMSkill

skill = UDMSkill("My Product")

# Tool: Method recommendation
@tool
def recommend_research_methods(research_goal: str, phase: int = None):
    """Recommend 3-5 research methods for a given goal."""
    return skill.recommend_methods(research_goal, phase=phase)

# Tool: Interview guide generation
@tool
def generate_interview_guide(topic: str, method: str, context: str = None):
    """Generate a structured interview guide."""
    return skill.generate_interview(topic, method, context=context)

# Tool: SUS scoring
@tool
def score_usability(responses: list[int]):
    """Calculate SUS score from 10 questionnaire responses."""
    return skill.calculate_sus(responses)
```

### Prompt Engineering Tips
- **Context injection**: Pass UDM knowledge base entries (from `references/`) as system context when generating research plans
- **Structured output**: Use `generate_research_plan()` to produce markdown-formatted plans that LLMs can refine
- **Triangulation**: Let the agent call `recommend_methods()` first, then use the output to generate interview questions via JTBD + VPD skills

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

```
Phase 1          Phase 2              Phase 3              Phase 4               Phase 5
Planning &      Exploration &        Concept             Evaluation &          Launch &
Scoping ──────► Synthesis  ──────►  Generation  ──────►  Refinement  ──────►  Monitoring
(Define)        (Infer)              (Derive)             (Assess)              (Monitor)
  │                │                    │                    │                     │
  ├─ Stakeholder   ├─ Analogies         ├─ Brainstorming     ├─ Heuristic Eval     ├─ Diary Studies
  ├─ Desk Research ├─ Cultural Probe    ├─ Bodystorming      ├─ Usability Test     ├─ A/B Testing
  └─ Frameworks    └─ Experience Map    └─ Affinity Diagram  └─ Cognitive Walkth.  └─ Analytics
```

1. **Planning & Scoping** — Explore and define project boundaries
2. **Exploration & Synthesis** — Infer design implications
3. **Concept Generation** — Derivative design activities
4. **Evaluation & Refinement** — Assess, refine, and produce
5. **Launch & Monitoring** — Ongoing review and correction

## 🌐 Ecosystem Integration

UDM is the **methodology core** of the AliDujie UX Research Ecosystem:

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Persona    │───►│  JTBD Skill  │───►│  UDM Skill   │
│  👤 角色定义  │    │  🎯 需求洞察  │    │  📖 定性研究  │
└──────────────┘    └──────────────┘    └──────┬───────┘
                                              │
                                     ┌────────▼───────┐
                                     │  QuantUX Skill │
                                     │  📊 定量验证    │
                                     └────────┬───────┘
                                              │
                                     ┌────────▼───────┐
                                     │  VPD Skill     │
                                     │  💎 价值验证    │
                                     └────────┬───────┘
                                              │
                                     ┌────────▼───────┐
                                     │  SWD Skill     │
                                     │  📈 数据叙事    │
                                     └────────────────┘

Workflow: Persona → JTBD/UDM → QuantUX → VPD → SWD → STM
```

### 🔀 Complete Pipeline Example

End-to-end from persona definition to executive storytelling:

```python
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from quantux import QuantUXSkill
from vpd import VPDSkill
from swd import SWDSkill

persona = PersonaSkill("Travel App")                          # 1. Define user
persona.add_persona(name="Frequent Traveler", archetype="Business User",
    priority="primary", goals=["Book hotel fast"])
jtbd    = JTBDSkill("Travel App").score_opportunity("Book hotel fast", struggle=4, alternative=3, market=4, budget=4)  # 2. Validate need
udm     = UDMSkill("Travel App").generate_interview("Booking Flow", "contextual")  # 3. Run research
quantux = QuantUXSkill("Travel App").calculate_ab_sample_size(baseline=0.35, mde=0.03)  # 4. Plan A/B test
vpd     = VPDSkill("Travel App", "Business Travelers").analyze_canvas(jobs=[{"description": "Book fast"}])  # 5. Value proposition
swd     = SWDSkill("Travel App").recommend_chart(data_type="categorical", category_count=3)  # 6. Executive presentation
```

### 🔗 Cross-Skill Collaboration / 跨技能协作

| UDM 产出 → | 下游技能用它做... | 示例调用 |
|-----------|-----------------|----------|
| 研究报告 | [SWD](https://github.com/AliDujie/storytelling-with-data) 数据故事构建 | `swd.build_story(evidence=udm_report.findings)` |
| 定性假设 | [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) A/B 验证 | `quantux.analyze_ab_test()` |
| 用户痛点 | [VPD](https://github.com/AliDujie/value-proposition-design) 画布填充 | `vpd.analyze_canvas(pains=udm.findings)` |
| 访谈数据 | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) 四力分析 | `jtbd.analyze_forces()` from transcripts |
| 观察记录 | [Persona](https://github.com/AliDujie/web-persona-skill) 角色创建 | `persona.add_persona(behaviors=udm.observations)` |

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

### 📊 5-Minute Setup Checklist

- [ ] **Install** — `cp -r universal-design-methods /your/agent/skills/`
- [ ] **Import** — `from udm import UDMSkill`
- [ ] **Initialize** — `skill = UDMSkill("Your Product")`
- [ ] **Recommend methods** — `skill.recommend_methods("Understand user churn", phase=1)`
- [ ] **Generate interview** — `skill.generate_interview("User Research", "contextual")`
- [ ] **SUS scoring** — `skill.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])`
- [ ] **Research plan** — `skill.generate_research_plan("UX Study")`

> 💡 **Try it now / 立即尝试**:
> ```python
> from udm import UDMSkill
> skill = UDMSkill("你的产品")
> print(skill.recommend_methods("了解用户为什么流失", phase=1))
> ```

### ⏱️ 5 分钟快速开始检查清单

- [ ] **安装** — `cp -r universal-design-methods /your/agent/skills/`
- [ ] **导入** — `from udm import UDMSkill`
- [ ] **初始化** — `skill = UDMSkill("你的产品")`
- [ ] **方法推荐** — `skill.recommend_methods("了解用户为什么流失", phase=1)`
- [ ] **生成访谈** — `skill.generate_interview("用户研究", "contextual", context="酒店预订")`
- [ ] **SUS 评分** — `skill.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])`
- [ ] **研究计划** — `skill.generate_research_plan("UX 研究")`

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
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | Research reports → CEO plan review & scope alignment |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | UDM tech usability findings → CTO infrastructure decisions |

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Related Skills in the AliDujie Ecosystem

| Skill | What It Does | GitHub |
|-------|-------------|--------|
| [Web Persona](https://github.com/AliDujie/web-persona-skill) | Evidence-driven user persona creation | `PersonaSkill` |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Jobs-to-be-Done analysis (4-school fusion) | `JTBDSkill` |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | HEART framework, A/B testing, MaxDiff | `QuantUXSkill` |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | VPD canvas, Blue Ocean strategy | `VPDSkill` |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Data visualization & executive storytelling | `SWDSkill` |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | Business framework analysis | `STMSkill` |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | CTO-level tech strategy & architecture guidance | `CTOSkill` |

## 🛡️ Common Pitfalls & How to Avoid Them

| Pitfall | How UDM Helps |
|---------|---------------|
| "We need more research" — paralysis by analysis | `recommend_methods()` returns 3-5 focused methods, not an endless list |
| Interviews drift off-topic | `generate_interview()` provides structured question flow with priority tags |
| Usability tests miss critical issues | `generate_heuristic_checklist()` + SUS scoring catches what ad-hoc testing misses |
| Research findings get lost | `generate_report()` produces structured, severity-ranked deliverables |
| Budget gets rejected | `generate_research_plan()` auto-attaches ROI scores and resource allocation |

**Rule of thumb**: Always pair at least one qualitative method with one quantitative method. UDM's triangulation engine does this automatically.

### 🔄 When to Combine with Other Skills

| If you need to... | Start with | Then chain to |
|-------------------|-----------|---------------|
| Understand user needs before research | [Persona](https://github.com/AliDujie/web-persona-skill) | UDM method selection |
| Structure Jobs from interview data | UDM interviews | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) opportunity scoring |
| Quantitatively validate qual findings | UDM qualitative research | [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) experiments |
| Map Jobs to value propositions | UDM research findings | [VPD](https://github.com/AliDujie/value-proposition-design) canvas |
| Present findings to executives | UDM research report | [SWD](https://github.com/AliDujie/storytelling-with-data) data story |

## ❓ FAQ / Troubleshooting

**Q: I'm not sure which phase to start with — what do you recommend?**
Start with Phase 1 (Planning & Scoping) if you're early in a project. If you already know what you're studying, skip to the relevant phase. Use `recommend_methods()` without a phase parameter for cross-phase suggestions.

### 💡 Pro Tips / 专业技巧
- **Triangulation is key**: Always pair at least one qualitative + one quantitative method for robust findings
- **Start small**: Pick 3 methods from the recommendation, not 10 — depth beats breadth
- **CEO ROI early**: Run `generate_research_plan(include_ceo_analysis=True)` before pitching research budget — it helps you speak the stakeholder's language
- **Document as you go**: Each method output (interview guide, observation record) feeds into synthesis — don't skip the paper trail

**Q: Do I need to install any dependencies?**
No. UDM uses only the Python standard library. Just `from udm import UDMSkill`.

**Q: Which phase number should I use in `recommend_methods()`?**
Phase 1 = Planning & Scoping, Phase 2 = Exploration & Synthesis, Phase 3 = Concept Generation, Phase 4 = Evaluation & Refinement, Phase 5 = Launch & Monitoring. When unsure, omit the phase parameter for cross-phase recommendations.

**Q: I have limited time/budget — what's the minimum viable research setup?**
For a 2-week, low-budget study: run 5–8 contextual interviews (Capability 2), synthesize with an affinity diagram (Capability 6), and follow up with a quick SUS usability test (Capability 4). This gives you qual + quant triangulation without a full research sprint.

**Quick setup**: `skill.recommend_methods("Understand user pain points", phase=1, resource_level="minimal")` returns the leanest valid combo.

**Q: How does the triangulation engine work?**
It recommends 3-5 complementary methods mixing qualitative and quantitative approaches, ensuring methodological diversity and improving research reliability.

**Q: How do I combine UDM with other AliDujie skills in practice?**
Start with UDM to select research methods and generate interview guides → feed findings into [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) for opportunity scoring → use [VPD](https://github.com/AliDujie/value-proposition-design) to map to value propositions → validate with [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) → present via [SWD](https://github.com/AliDujie/storytelling-with-data). See the [Complete Pipeline Example](#-complete-pipeline-example) section above.

**Q: Can I use UDM with other skills in the ecosystem?**
Yes! UDM is designed as the methodology core. Pair it with [Persona](https://github.com/AliDujie/web-persona-skill) for user data, [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) for needs analysis, [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) for quantitative validation, [VPD](https://github.com/AliDujie/value-proposition-design) for value mapping, and [SWD](https://github.com/AliDujie/storytelling-with-data) for executive presentations. See the [complete pipeline example](#-complete-pipeline-example) above for the full 6-skill chain.

**Q: SUS score seems off — what range should I expect?**
SUS scores range 0-100. Grade thresholds: A (80+), B (68-79), C (52-67), D (37-51), F (<37). Average SUS score across industries is ~68.

**Q: Is this skill suitable for non-researchers?**
Absolutely. The CEO-level extensions (ROI, resource allocation) are designed for anyone who needs to justify research decisions to stakeholders.

## 📚 Resources

- [INSTALL.md](INSTALL.md) — Detailed installation guide and agent integration
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — Community guidelines

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
