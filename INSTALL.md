# Installation Guide

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Prerequisites

- Python 3.8 or higher
- No external dependencies required (pure standard library)

## Quick Install

### Option 1: Copy to Skills Directory

```bash
# For OpenClaw users
cp -r universal-design-methods ~/.openclaw/skills/

# For custom agent setups
cp -r universal-design-methods /your/agent/skills/
```

### Option 2: Clone from GitHub

```bash
git clone https://github.com/AliDujie/universal-design-methods.git
cd universal-design-methods
```

### Option 3: Install as Python Package

```bash
cd universal-design-methods
pip install -e .
```

## Verify Installation

```python
import sys
sys.path.insert(0, "/path/to/universal-design-methods")
from udm import UDMSkill

skill = UDMSkill("Test Product")
methods = skill.recommend_methods("Understand user needs", phase=1)
print(f"Successfully installed! Recommended {len(methods)} methods.")
```

## Platform Support

| Platform | Status |
|----------|--------|
| macOS | ✅ Fully supported |
| Linux | ✅ Fully supported |
| Windows | ✅ Fully supported |

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'udm'` | Ensure the skill directory is in your Python path |
| Import errors | Verify Python version >= 3.8 with `python --version` |

---

*Last Updated: 2026-05-01 | AliDujie Skill Ecosystem*
