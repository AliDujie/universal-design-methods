# UDM 跨技能协作指南

> 通用设计方法如何与 AliDujie 生态系统中的其他技能协作

---

## UDM 在生态系统中的位置

UDM 是 7 技能工作流的 **研究方法核心**，提供执行研究的方法论：

```
Persona → JTBD → UDM (你在这里) → QuantUX → VPD → SWD
```

## UDM → 其他技能的数据流转

### UDM → JTBD：从数据到洞察

UDM 执行用户访谈和观察，JTBD 将原始数据转化为结构化的 Jobs：

| UDM 输出 | → JTBD 输入 | 处理方式 |
|---------|-----------|---------|
| 访谈记录 | 用户原始语句 | 提取 Job 描述 |
| 观察记录 | 行为描述 | 映射到 Job 类型 |
| 体验历程图 | 痛点和情绪 | 评估 Job 严重度 |
| 亲和图 | 用户需求分组 | 形成 Job 框架 |
| NPS/SUS | 满意度基线 | 校准重要性评分 |

### UDM → QuantUX：从定性到定量

UDM 的定性发现是 QuantUX 假设的主要来源：

| UDM 输出 | → QuantUX 输入 | 验证方法 |
|---------|---------------|---------|
| 访谈发现的痛点 | A/B 测试假设 | 对照组实验 |
| 可用性测试 SUS | 改进后复测 | 统计显著性 |
| 问卷数据 | 行为趋势分析 | 时间序列 |
| 用户细分 | 分层抽样 | 分层分析 |

### UDM → VPD：从需求到价值主张

UDM 发现的用户需求直接转化为 VPD 画布输入：

| UDM 输出 | → VPD 画布位置 |
|---------|---------------|
| 用户目标描述 | 客户工作 |
| 痛点列表 | 客户痛点 |
| 期望功能 | 客户收益 |
| 竞品分析 | 替代方案评估 |
| 优先级排序 | 画布元素优先级 |

### UDM → SWD：从研究到呈现

UDM 的研究发现通过 SWD 转化为决策叙事：

| UDM 输出 | → SWD 呈现 |
|---------|-----------|
| 体验历程图 | 旅程可视化 |
| SUS/NPS 评分 | 仪表盘/趋势图 |
| 亲和图分组 | 主题矩阵 |
| 研究计划 → 报告 | 三幕叙事结构 |

### UDM → Persona：从数据到角色

UDM 研究数据为 Persona 提供证据支撑：

| UDM 输出 | → Persona 输入 |
|---------|---------------|
| 用户访谈 | 角色语录 (quote) |
| 行为观察 | 行为特征 (behaviors) |
| 态度访谈 | 态度倾向 (attitudes) |
| 用户细分 | 角色优先级 |

## 协作最佳实践

### 1. 先定性后定量

```
UDM (访谈 8-12 人) → 发现假设 → QuantUX (验证假设 n>1000)
```

- 用 UDM 探索"为什么"和"是什么"
- 用 QuantUX 验证"有多少"和"是否显著"

### 2. 三角验证

任何重要结论都应通过至少 2-3 种方法验证：

```
UDM 访谈 (定性) + QuantUX 调查 (定量) + 日志分析 (行为) = 高信度
```

### 3. 迭代循环

研究不是线性的，需要迭代：

```
UDM 初步发现 → JTBD 结构化 → VPD 设计 → QuantUX 验证
    ↑                                                    |
    └──────────── SWD 呈现 ──→ 新的研究问题 ──→ UDM ─────┘
```

### 4. 数据可追溯

每个结论都应该能追溯回原始数据：

| 层级 | 数据源 | 可追溯性 |
|------|--------|---------|
| 结论 | SWD 叙事 | ← 研究发现 |
| 发现 | UDM 报告 | ← 原始数据 |
| 数据 | 访谈/问卷 | ← 录音/原始回复 |

## 端到端工作流示例

### 场景：优化旅行平台用户留存

```python
# === 阶段 1: UDM 定性研究 ===
from udm import UDMSkill

udm = UDMSkill("旅行平台")

# 方法推荐
methods = udm.recommend_methods("了解用户为什么不再使用我们的平台", phase=1)
# → 推荐: 退出访谈 + 日记研究 + 可用性测试

# 执行退出访谈
exit_guide = udm.generate_interview("流失用户退出访谈", "contextual")

# 计算当前 SUS 基线
baseline_sus = udm.calculate_sus([3, 2, 4, 2, 3, 2, 4, 2, 3, 2])
# SUS = 45.0 (需要改进)

# === 阶段 2: JTBD 结构化洞察 ===
from jtbd import JTBDSkill

jtbd = JTBDSkill("旅行平台")
# 访谈数据 → JTBD Jobs:
# "快速完成预订而不浪费时间" (Opportunity: 8.5)
# "确保行程可靠不出错" (Opportunity: 7.8)

# === 阶段 3: QuantUX 定量验证 ===
from quantux import QuantUXSkill

quantux = QuantUXSkill("旅行平台")

# HEART 指标体系
heart = quantux.build_heart_framework(
    happiness="整体满意度",
    engagement="月均预订次数",
    retention="90 天留存率",
    task_success="预订完成率"
)

# A/B 测试优化方案
sample = quantux.calculate_ab_sample_size(baseline=0.25, mde=0.05)
# → 每组需要 6,710 样本

# === 阶段 4: VPD 价值主张设计 ===
from vpd import VPDSkill

vpd = VPDSkill("旅行平台", "回流用户")
canvas = vpd.analyze_canvas(
    product_name="回归礼遇",
    jobs=["快速找回使用习惯", "获得专属优惠"],
    pains=["忘记如何使用", "价格没有优势"],
    gains=["快速上手", "专属折扣"]
)

# === 阶段 5: SWD 呈现决策 ===
from swd import SWDSkill

swd = SWDSkill("留存优化汇报")
story = swd.build_story(
    protagonist="留存团队",
    imbalance="90 天留存率从 45% 降至 28%",
    resolution="优化后回升至 38%，SUS 从 45 提升到 68"
)
```

---

*本文档是 AliDujie Universal Design Methods 技能生态系统的补充参考。*
