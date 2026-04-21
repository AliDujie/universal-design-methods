# Universal Design Methods Skill (通用设计方法执行技能)

> 🎯 **100 种设计研究方法，8 大执行能力，1 个完整工具包**

基于《通用设计方法》(贝拉·马丁 & 布鲁斯·汉宁顿) 的 100 种设计研究方法工具包。

## 🌟 为什么使用这个技能？

- **省时省力** — 无需记忆 100 种方法，AI 自动推荐最适合的方法组合
- **专业可靠** — 基于经典著作，覆盖 UX 研究全生命周期
- **开箱即用** — 纯 Python 标准库，无外部依赖，5 分钟上手
- **三角测量** — 自动推荐定性 + 定量方法组合，提升研究信度
- **双语支持** — 完整中英文文档，适合国际化团队

## 🚀 5 分钟快速开始

### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r skills/universal-design-methods ~/.aoneclaw/skills/
```

### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/universal-design-methods")
from udm import UDMSkill

# 初始化技能
skill = UDMSkill("我的产品")
```

### 步骤 3: 开始使用

```python
# 场景 1: 不知道用什么方法？让 AI 推荐！
methods = skill.recommend_methods("了解用户需求", phase=1)
print(methods)  # 自动推荐访谈、问卷、观察等方法组合

# 场景 2: 需要访谈提纲？30 秒生成！
guide = skill.generate_interview("用户访谈", "contextual")
print(guide)  # 包含开场白、核心问题、追问技巧

# 场景 3: 要做可用性测试？完整方案一键生成！
test_plan = skill.generate_usability_test("流程测试", "formative")
print(test_plan)  # 包含任务设计、指标、脚本

# 场景 4: 回收了 SUS 问卷？自动计算分数！
sus_score = skill.calculate_sus([4,2,5,1,4,2,5,1,4,2])
print(f"SUS 得分：{sus_score}")  # 自动计算并解读

# 场景 5: 需要 NPS 分析？一键完成！
nps = skill.calculate_nps([9,10,8,7,10,6,9,8,10,5])
print(f"NPS: {nps}")  # 自动分类推荐者/被动者/贬损者

# 场景 6: 设计 KANO 问卷？features 一键生成！
survey = skill.generate_survey("需求调研", "kano", features=["智能推荐", "离线模式"])
print(survey)  # 包含功能型、反向型、期望型问题
```

## 💡 核心特性

- **100 种方法完整索引** — 按阶段、目的、数据类型快速筛选
- **8 大执行能力** — 方法推荐、访谈提纲、观察记录、可用性测试、问卷设计、综合分析、研究计划、研究报告
- **Python API** — 纯标准库实现，无外部依赖，可直接导入使用
- **知识库** — 7 个 Markdown 知识文档，支持关键词搜索
- **三角测量** — 自动推荐定性 + 定量方法组合

## 📁 项目结构

```
universal-design-methods/
├── skills/universal-design-methods/
│   └── SKILL.md                 # AI Agent 技能定义
├── udm/                         # Python 工具包（纯标准库）
│   ├── __init__.py              # 统一入口类 UDMSkill
│   ├── config.py                # 100 种方法索引与配置
│   ├── utils.py                 # 知识库加载与方法搜索
│   ├── templates.py             # 模板常量
│   ├── interview.py             # 访谈框架生成器
│   ├── observation.py           # 观察记录生成器
│   ├── usability.py             # 可用性测试引擎
│   ├── survey.py                # 问卷生成器
│   ├── synthesis.py             # 综合分析引擎
│   ├── recommender.py           # 方法推荐引擎
│   ├── research_plan.py         # 研究计划生成器
│   └── report.py                # 研究报告生成器
├── methods-*.md                 # 知识库文档
├── execution-templates.md       # 执行模板
├── decision-framework.md        # 决策框架
└── README.md                    # 本文件
```

## 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的一部分：

- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — 量化研究、HEART 框架、A/B 测试
- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done 理论、进步力量分析
- **[Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design)** — 价值主张画布、商业模式设计
- **[Web-Persona-Skill](https://github.com/AliDujie/web-persona-skill)** — 人物角色创建、用户细分
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — 数据叙事、可视化设计

**推荐组合使用**：本技能 (定性方法) + Quantitative-UX-Research (定量方法) = 完整三角测量研究方案

## 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

## 📚 关于《通用设计方法》

- **书名**: Universal Methods of Design
- **作者**: Bella Martin & Bruce Hanington
- **内容**: 100 种设计研究方法的系统化工具包
- **适用**: UX 研究员、产品经理、设计师、创业者

## 📜 许可

本技能仅供内部学习和研究使用。

## 👨‍💻 作者

- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫
