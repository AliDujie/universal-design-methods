# Universal Design Methods Skill

100 种设计研究方法、8 大执行能力、1 个完整 Python 工具包。

基于《通用设计方法》(贝拉·马丁 & 布鲁斯·汉宁顿) 构建，覆盖 UX 研究全生命周期。

## 快速开始

### 作为 Agent Skill 使用

将本仓库放入你的 AI Agent skills 目录，Agent 会自动读取 `SKILL.md` 获取执行指令。

### 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/universal-design-methods")
from udm import UDMSkill

skill = UDMSkill("我的产品")

# 方法推荐（自动三角测量）
methods = skill.recommend_methods("了解用户需求", phase=1)

# 访谈提纲（5种类型）
guide = skill.generate_interview("用户访谈", "contextual")

# 可用性测试 + SUS 计算
test = skill.generate_usability_test("流程测试", "formative")
sus = skill.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])

# 问卷设计（卡诺/NPS/语义差异/SUS/期望值）
survey = skill.generate_survey("需求调研", "kano", features=["智能推荐"])
nps = skill.calculate_nps([9, 10, 8, 7, 10, 6, 9, 8, 10, 5])

# 体验历程图
jm = skill.build_journey_map("预订体验", persona="用户小李")
jm.add_stage("搜索", actions=["打开App"], emotions=4, pain_points=["排序差"])

# 研究计划 & 报告
plan = skill.generate_research_plan("体验研究", background="用户流失率上升")
report = skill.generate_report("研究报告", summary="发现3个核心痛点")
```

## 项目结构

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

## 依赖

- Python >= 3.8
- 无外部依赖（纯标准库实现）
- 兼容 macOS / Linux / Windows

## 运行测试

```bash
python -m udm.tests.test_all
```

## 相关技能

- [storytelling-with-data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事与可视化
- [jtbd-knowledge-skill](https://github.com/AliDujie/jtbd-knowledge-skill) — Jobs-to-be-Done 理论
- [web-persona-skill](https://github.com/AliDujie/web-persona-skill) — 人物角色创建
- [value-proposition-design](https://github.com/AliDujie/value-proposition-design) — 价值主张设计
- [Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research) — 量化 UX 研究

## 许可

MIT License

## 作者

[@AliDujie](https://github.com/AliDujie)
