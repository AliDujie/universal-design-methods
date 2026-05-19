# Installation Guide / 安装指南

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Prerequisites / 前置要求

- Python 3.8 or higher / Python 3.8 或更高版本
- No external dependencies required (pure standard library) / 无需外部依赖（纯标准库）

## Quick Install / 快速安装

### Option 1: Copy to Skills Directory / 方式一：复制到技能目录

```bash
# For OpenClaw users / 适用于 OpenClaw 用户
cp -r universal-design-methods ~/.openclaw/skills/

# For custom agent setups / 适用于自定义 Agent 配置
cp -r universal-design-methods /your/agent/skills/
```

### Option 2: Clone from GitHub / 方式二：从 GitHub 克隆

```bash
git clone https://github.com/AliDujie/universal-design-methods.git
cd universal-design-methods
```

### Option 3: Install as Python Package / 方式三：作为 Python 包安装

```bash
cd universal-design-methods
pip install -e .
```

## Verify Installation / 验证安装

```python
import sys
sys.path.insert(0, "/path/to/universal-design-methods")
from udm import UDMSkill

skill = UDMSkill("Test Product")
methods = skill.recommend_methods("Understand user needs", phase=1)
print(f"Successfully installed! Recommended {len(methods)} methods.")
# 安装成功！已推荐 {len(methods)} 种方法。
```

## Platform Support / 平台支持

| Platform / 平台 | Status / 状态 |
|----------|--------|
| macOS | ✅ Fully supported / 完全支持 |
| Linux | ✅ Fully supported / 完全支持 |
| Windows | ✅ Fully supported / 完全支持 |

## Troubleshooting / 故障排查

| Issue / 问题 | Solution / 解决方案 |
|-------|----------|
| `ModuleNotFoundError: No module named 'udm'` | Ensure the skill directory is in your Python path / 确保技能目录在 Python 路径中 |
| Import errors / 导入错误 | Verify Python version >= 3.8 with `python --version` / 确认 Python 版本 >= 3.8 |

## Related Skills / 相关技能

This skill is part of the AliDujie UX Research ecosystem. Consider exploring:
本技能是 AliDujie UX 研究生态系统的一部分，建议同时了解：

- [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — JTBD 访谈数据可作为 UDM 研究输入
- [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — UDM 定性发现可用 QuantUX 验证
- [Web Persona](https://github.com/AliDujie/web-persona-skill) — UDM 合成阶段可构建 Persona
- [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — UDM 生成阶段方法可与 VPD 结合
- [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — UDM 研究报告可交给 SWD 进行数据叙事

## Agent Integration / Agent 集成

### OpenClaw Integration

For OpenClaw users, UDM works as a first-class skill — drop it into `~/.openclaw/skills/` or `~/.agents/skills/` and the agent picks it up automatically:

```bash
# Clone directly into skills directory
git clone https://github.com/AliDujie/universal-design-methods.git ~/.agents/skills/universal-design-methods
```

### LangChain / LLM Agent Integration

```python
from udm import UDMSkill

# Wrap UDM as a tool for your agent
skill = UDMSkill("My Product")

# Tool definition example
tools = [
    {
        "name": "recommend_research_methods",
        "description": "Recommend 3-5 research methods for a given goal",
        "function": lambda goal, phase=None: skill.recommend_methods(goal, phase=phase)
    },
    {
        "name": "generate_interview_guide",
        "description": "Generate a structured interview guide",
        "function": lambda title, method, context=None: skill.generate_interview(title, method, context=context)
    },
    {
        "name": "score_usability",
        "description": "Calculate SUS score from 10 questionnaire responses (1-5 scale)",
        "function": lambda responses: skill.calculate_sus(responses)
    }
]
```

### When to Chain with Other Skills / 何时与其他技能串联

| If you need... | UDM first, then... |
|---------------|--------------------|
| User personas from research data | → [Persona Skill](https://github.com/AliDujie/web-persona-skill) |
| Structured Jobs analysis from interviews | → [JTBD Skill](https://github.com/AliDujie/jtbd-knowledge-skill) |
| Statistical validation of findings | → [QuantUX Skill](https://github.com/AliDujie/Quantitative-UX-Research) |
| Value proposition mapping | → [VPD Skill](https://github.com/AliDujie/value-proposition-design) |
| Executive data storytelling | → [SWD Skill](https://github.com/AliDujie/storytelling-with-data) |
| Strategic business frameworks | → [STM Skill](https://github.com/AliDujie/Structured-Thinking-Model) |
| CEO-level ROI & resource planning | → UDM CEO capabilities (built-in) |
| CTO/CMO/CPO strategic alignment | → [CEO/CPO/CMO/CTO Advisor Skills](https://github.com/AliDujie) |

---

*Last Updated: 2026-05-20 | AliDujie Skill Ecosystem | Version 2.3.90*
