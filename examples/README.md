# Universal Design Methods — Runnable Examples

Zero-dependency Python examples demonstrating UDM capabilities. Each script is standalone — just run it.

## Quick Start

```bash
# All examples require Python 3.8+ and the udm module in your path
# From the repo root:
PYTHONPATH=. python examples/01_method_recommendation.py
PYTHONPATH=. python examples/02_journey_map_usability.py
PYTHONPATH=. python examples/03_interview_guide.py
```

## Examples

| Script | What It Shows |
|--------|--------------|
| `01_method_recommendation.py` | Research method selection for a real product scenario |
| `02_journey_map_usability.py` | Building an experience journey map + usability SUS scoring |
| `03_interview_guide.py` | Generating structured interview guides with context |

## Try Before You Decide

Run any example to see what UDM can do in under 30 seconds:

```bash
PYTHONPATH=. python -c "
from udm import UDMSkill
skill = UDMSkill('Travel App')
methods = skill.recommend_methods('Why do users abandon the app after first use?')
print(methods)
"
```

No `pip install` needed — UDM uses only Python standard library.

## 🔗 Ecosystem Integration / 生态集成

UDM is the methodology engine of the AliDujie UX Research Ecosystem. Chain it with other skills:

- **Persona → UDM**: [Persona](https://github.com/AliDujie/web-persona-skill) defines users → UDM selects research methods
- **UDM → JTBD**: UDM interview transcripts → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) opportunity scoring
- **UDM → QuantUX**: UDM qualitative findings → [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) A/B validation
- **UDM → VPD**: UDM pain points → [VPD](https://github.com/AliDujie/value-proposition-design) canvas filling
- **UDM → SWD**: UDM research reports → [SWD](https://github.com/AliDujie/storytelling-with-data) executive stories
- **UDM → STM**: UDM research insights → [STM](https://github.com/AliDujie/Structured-Thinking-Model) strategic analysis

See the [full pipeline example](../README.md#complete-pipeline-example) in README.md for a 7-skill end-to-end workflow.
