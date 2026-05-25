# Universal Design Methods — Runnable Examples

Zero-dependency Python examples demonstrating UDM capabilities. Each script is standalone — just run it.

## Quick Start

```bash
# All examples require Python 3.8+ and the udm module in your path
# From the repo root:
PYTHONPATH=. python examples/01_method_recommendation.py
PYTHONPATH=. python examples/02_journey_map.py
PYTHONPATH=. python examples/03_ecosystem_pipeline.py
```

## Examples

| Script | What It Shows |
|--------|--------------|
| `01_method_recommendation.py` | Research method selection for a real product scenario |
| `02_journey_map.py` | Building and rendering an experience journey map |
| `03_ecosystem_pipeline.py` | Full 6-skill pipeline: Persona → JTBD → UDM → QuantUX → VPD → SWD |

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
