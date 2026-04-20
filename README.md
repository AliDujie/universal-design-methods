# Universal Design Methods Skill (通用设计方法执行技能)

基于《通用设计方法》(贝拉·马丁 & 布鲁斯·汉宁顿) 的100种设计研究方法工具包。

## 特性

- **100种方法完整索引** — 按阶段、目的、数据类型快速筛选
- **8大执行能力** — 方法推荐、访谈提纲、观察记录、可用性测试、问卷设计、综合分析、研究计划、研究报告
- **Python API** — 纯标准库实现，无外部依赖，可直接导入使用
- **知识库** — 7个Markdown知识文档，支持关键词搜索
- **三角测量** — 自动推荐定性+定量方法组合

## 快速开始

```python
import sys
sys.path.insert(0, "/path/to/universal-design-methods-skill")
from udm import UDMSkill

skill = UDMSkill("我的产品")

# 方法推荐
print(skill.recommend_methods("了解用户需求", phase=1))

# 访谈提纲
print(skill.generate_interview("用户访谈", "contextual"))

# 可用性测试
print(skill.generate_usability_test("流程测试", "formative"))

# SUS计算
print(skill.calculate_sus([4,2,5,1,4,2,5,1,4,2]))

# NPS计算
print(skill.calculate_nps([9,10,8,7,10,6,9,8,10,5]))

# 问卷生成
print(skill.generate_survey("需求调研", "kano", features=["智能推荐"]))
```

## 项目结构

```
├── skills/universal-design-methods/SKILL.md  # Skill执行指令
├── udm/                                       # Python工具包
│   ├── __init__.py          # 统一入口类 UDMSkill
│   ├── config.py            # 100种方法索引与配置
│   ├── utils.py             # 知识库加载与方法搜索
│   ├── templates.py         # 模板常量
│   ├── interview.py         # 访谈框架生成器
│   ├── observation.py       # 观察记录生成器
│   ├── usability.py         # 可用性测试引擎
│   ├── survey.py            # 问卷生成器
│   ├── synthesis.py         # 综合分析引擎
│   ├── recommender.py       # 方法推荐引擎
│   ├── research_plan.py     # 研究计划生成器
│   └── report.py            # 研究报告生成器
├── methods-*.md             # 知识库文档(5个)
├── execution-templates.md   # 执行模板
├── decision-framework.md    # 决策框架
└── SKILL.md                 # 旧版入口(保留兼容)
```

## 依赖

- Python >= 3.8
- 无外部依赖（纯标准库）
