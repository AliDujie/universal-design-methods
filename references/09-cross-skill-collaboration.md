# 跨技能协作指南 (Cross-Skill Collaboration Guide)

> UDM 是 AliDujie UX 研究生态系统的**方法论核心**——覆盖从探索到交付的完整研究生命周期。
> UDM is the **methodology core** of the AliDujie UX Research Ecosystem — spanning the full research lifecycle from exploration to delivery.

## 🌐 生态系统总览 (Ecosystem Overview)

UDM 与以下 6 个技能无缝协作，形成端到端用户研究管道：

| # | 技能 | 定位 | 关键产出 |
|---|------|------|---------|
| 1 | [Web Persona](https://github.com/AliDujie/web-persona-skill) | 👤 用户定义层 | 证据驱动的人物角色 |
| 2 | [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 🎯 需求洞察层 | Jobs 结构化 + 机会评分 |
| 3 | **UDM (本技能)** | 📖 方法论核心 | 研究方法推荐 + 执行 |
| 4 | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 📊 定量验证层 | HEART/A-B/MaxDiff |
| 5 | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 💎 价值验证层 | 价值主张画布 + 实验 |
| 6 | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 📈 数据叙事层 | 可视化 + 高管汇报 |
| 7 | [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | 🧠 战略分析层 | 商业框架 + 决策 |

```
Persona → JTBD → UDM → QuantUX → VPD → SWD → STM
  👤       🎯      📖       📊        💎      📈      🧠
  who     what    how     verify    value  present  strategy
```

## 🔀 典型协作模式 (Collaboration Patterns)

### 模式一：UDM → JTBD（定性发现 → 需求洞察）

**场景**：通过 UDM 执行用户访谈后，需要将原始访谈数据结构化为 Jobs 分析。

```python
# Step 1: UDM 执行用户访谈收集原始数据
from udm import UDMSkill
udm = UDMSkill("旅行预订")
interview = udm.generate_interview("商务用户深访", "contextual", context="出差预订")
# → 获得结构化访谈提纲，执行访谈后获得原始数据

# Step 2: JTBD 将访谈发现结构化
from jtbd import JTBDSkill
jtbd = JTBDSkill("旅行预订平台")
# 基于访谈中提取的用户行为，进行四力分析和机会评分
opportunity = jtbd.score_opportunity(
    job="快速找到合适住处",
    struggle=4,   # 现有方案痛苦程度
    alternative=3, # 替代方案充足度
    market=4,     # 市场规模
    budget=4      # 用户支付意愿
)
# → Score: 7.6/10 — 高机会领域
```

**数据流向**：UDM 访谈原始记录 → JTBD Jobs 提取 → 机会评分排序

### 模式二：UDM → QuantUX（定性假设 → 定量验证）

**场景**：UDM 可用性测试发现痛点后，需要用定量方法验证改进效果。

```python
# Step 1: UDM 定性研究发现问题
from udm import UDMSkill
udm = UDMSkill("电商应用")
sus_before = udm.calculate_sus([3, 2, 4, 1, 3, 2, 4, 1, 3, 2])  # → 77.5, Grade B
# 发现：结账流程过长是主要痛点

# Step 2: QuantUX 设计 A/B 测试验证改进
from quantux import QuantUXSkill
quantux = QuantUXSkill("电商应用")
# 计算样本量
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.05)
# → 需要每组 ~600 样本
# 分析 A/B 测试结果
ab = quantux.analyze_ab_test("旧版", 5000, 1750, "新版", 5000, 1900)
# → 转化率从 35% 提升到 38%，统计显著
```

**数据流向**：UDM 定性痛点发现 → 设计改进方案 → QuantUX A/B 实验验证

### 模式三：UDM → Persona（研究数据 → 角色创建）

**场景**：UDM 收集的行为数据用于创建或更新人物角色。

```python
# Step 1: UDM 收集用户行为数据
from udm import UDMSkill
udm = UDMSkill("健康管理")
observation = udm.generate_observation("用户使用习惯", "shadowing", setting="健身房")
# → 获得 AEIOU 观察框架和结构化记录

# Step 2: Persona 创建证据驱动的人物角色
from persona import PersonaSkill
persona = PersonaSkill("健康管理")
persona.add_persona(
    name="健身达人小王",
    archetype="效率优先型",
    priority="primary",
    goals=["快速记录训练数据", "追踪体脂变化"],
    behaviors=["每天打卡训练计划", "喜欢分享成果到社区"],
    bio="28岁程序员，每周健身4次",
    context=observation  # 关联 UDM 观察数据作为证据
)
```

**数据流向**：UDM 访谈/观察行为数据 → Persona 角色画像构建

### 模式四：UDM → VPD（用户研究 → 价值验证）

**场景**：UDM 用户研究输出 Jobs/Pains/Gains，VPD 填充价值主张画布。

```python
# Step 1: UDM 用户研究
from udm import UDMSkill
udm = UDMSkill("在线教育")
survey = udm.generate_survey("功能需求调研", "kano",
    features=["AI 错题本", "学习进度同步", "家长监控面板"])

# Step 2: VPD 填充价值主张画布
from vpd import VPDSkill
vpd = VPDSkill("在线教育", "K12学生")
canvas = vpd.analyze_canvas(
    product_name="在线学习平台",
    jobs=[
        {"description": "快速找到薄弱知识点", "importance": 5},
        {"description": "获得个性化练习", "importance": 4},
    ],
    pains=[
        {"description": "题目太难容易放弃", "severity": "high"},
        {"description": "学习反馈不及时", "severity": "medium"},
    ],
    gains=[
        {"description": "成绩提升可见", "impact": "high"},
    ]
)
```

**数据流向**：UDM 用户研究 → Jobs/Pains/Gains 提取 → VPD 画布填充

### 模式五：UDM → SWD（研究发现 → 数据叙事）

**场景**：UDM 生成研究报告后，需要转化为高管级数据故事。

```python
# Step 1: UDM 生成研究报告
from udm import UDMSkill
udm = UDMSkill("电商平台")
report = udm.generate_report("用户体验研究报告", summary="发现3个核心痛点")
report.add_finding("搜索不准确", "用户需要多次修改搜索词", severity=3, recommendation="优化搜索算法")

# Step 2: SWD 将研究发现可视化
from swd import SWDSkill
swd = SWDSkill("Q1 用户体验汇报")
ctx = swd.build_context(audience="CEO", cta="批准体验优化预算")
chart = swd.recommend_chart(data_type="categorical", category_count=3)
story = swd.build_story(
    protagonist="产品委员会",
    imbalance="搜索体验差导致 30% 用户流失",
    call_to_action="投入 50 万优化搜索算法"
)
```

**数据流向**：UDM 研究报告 → 关键发现提取 → SWD 数据故事 + 图表推荐

### 模式六：UDM ↔ STM（双向协作：战略框架 ↔ 研究方法）

**场景**：STM 提供商业分析框架，UDM 匹配研究方法执行验证。

```python
# Step 1: STM 定义分析框架
from stm import STMSkill
stm = STMSkill("旅行平台")
swot = stm.analyze_swot("旅行预订平台")
# → 识别出战略机会和威胁

# Step 2: UDM 匹配研究方法验证假设
from udm import UDMSkill
udm = UDMSkill("旅行平台")
# 基于 SWOT 中的威胁，推荐研究方法
methods = udm.recommend_methods("验证竞品差异化策略的有效性", phase=1)
# → 推荐：竞品分析 + 用户深访 + 语义差异量表

# Step 3: UDM 执行研究 → STM 更新战略建议
# ...研究执行后...
strategic_recommendation = stm.recommend_strategy("差异化优先")
```

**数据流向**：STM 框架定义研究方向 → UDM 执行研究验证 → STM 更新战略建议

## 🔄 完整端到端流程 (Full End-to-End Pipeline)

串联全部 6 个技能的完整用户研究管道：

```python
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from quantux import QuantUXSkill
from vpd import VPDSkill
from swd import SWDSkill

# ─── 1. Persona — 定义目标用户 ─────────────────────────
persona = PersonaSkill("旅行预订平台")
persona.add_persona(
    name="商务客", archetype="效率优先", priority="primary",
    goals=["30秒内完成酒店预订"],
    behaviors=["频繁出差，即时预订"],
    bio="每周出差的销售顾问"
)

# ─── 2. JTBD — 发现未满足的需求 ────────────────────────
jtbd = JTBDSkill("旅行预订平台")
score = jtbd.score_opportunity(
    "快速找到合适住处", struggle=4, alternative=3, market=4, budget=4
)
# → Score: 7.6/10 — 高机会领域

# ─── 3. UDM — 定性研究验证 ─────────────────────────────
udm = UDMSkill("旅行预订平台")
interview = udm.generate_interview("商务用户", "contextual", context="酒店预订")
sus = udm.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])
# → SUS: 85.0, Grade A

# ─── 4. QuantUX — 定量验证 ─────────────────────────────
quantux = QuantUXSkill("旅行预订平台")
n = quantux.calculate_ab_sample_size(baseline=0.35, mde=0.03)
ab = quantux.analyze_ab_test("旧版", 5000, 1750, "新版", 5000, 1900)

# ─── 5. VPD — 价值主张验证 ─────────────────────────────
vpd = VPDSkill("旅行预订", "商务客")
canvas = vpd.analyze_canvas(
    product_name="旅行预订",
    jobs=[{"description": "快速找到住处", "importance": 5}]
)

# ─── 6. SWD — 高管数据故事 ─────────────────────────────
swd = SWDSkill("Q1 研究汇报")
story = swd.build_story(
    protagonist="产品委员会",
    imbalance="商务客预订体验差",
    call_to_action="优化一键预订"
)
```

## 📊 协作决策矩阵 (Collaboration Decision Matrix)

| 你的研究阶段 | 主要技能 | 协作技能 | 目标 |
|-------------|---------|---------|------|
| **用户是谁？** | Persona | — | 定义目标用户画像 |
| **用户需要什么？** | JTBD | Persona | 发现未满足的需求 |
| **怎么研究？** | **UDM** | JTBD/Persona | 推荐方法 + 执行研究 |
| **假设对吗？** | QuantUX | UDM | 定量验证定性发现 |
| **价值匹配吗？** | VPD | UDM/JTBD | 验证价值主张 |
| **怎么汇报？** | SWD | UDM/VPD | 数据可视化 + 故事 |
| **战略方向？** | STM | UDM/VPD | 商业框架分析 |

## 🎯 触发词映射 (Trigger Mapping)

当用户提到以下场景时，考虑跨技能协作：

| 用户意图 | 触发技能 | 推荐协作 |
|---------|---------|---------|
| "了解用户需求" | UDM + JTBD | UDM 访谈 → JTBD 机会评分 |
| "验证改版效果" | UDM + QuantUX | UDM 可用性测试 → QuantUX A/B |
| "创建用户画像" | Persona + UDM | UDM 观察 → Persona 创建 |
| "功能优先级" | UDM + VPD | UDM Kano 调研 → VPD 画布 |
| "向高管汇报" | UDM + SWD | UDM 报告 → SWD 数据故事 |
| "竞品分析" | UDM + STM | UDM 竞品测试 → STM 战略框架 |
| "端到端研究" | 全部 6 个技能 | 完整管道协作 |

## 📝 最佳实践 (Best Practices)

1. **顺序执行，数据驱动**：每个技能的输出是下游技能的输入。确保数据在管道中流动。
2. **UDM 是入口**：不确定用什么方法？先用 `recommend_methods()`，再根据推荐结果选择协作技能。
3. **最小可行管道**：时间紧张时，至少跑 UDM → SWD（研究 → 汇报）。
4. **三角测量**：UDM 推荐的方法组合本身就包含定性+定量，与 QuantUX 协作时不需要重复验证所有假设。
5. **文档传递**：每个技能产出的 Markdown 报告可以直接作为下一个技能的 context 输入。

---

*本文档是 universal-design-methods 技能知识库的扩展参考。更多方法详情请见其他 `references/` 文档。*
