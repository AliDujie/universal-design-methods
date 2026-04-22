"""UDM (Universal Design Methods) Python Toolkit

基于《通用设计方法》(贝拉·马丁 & 布鲁斯·汉宁顿) 的设计研究工具包。
覆盖100种设计研究方法的知识查询、方法推荐、执行指导、数据采集、
分析框架、业务决策和教练辅导等完整能力。

快速开始::

    from udm import UDMSkill
    skill = UDMSkill("我的产品")

    # 能力1: 方法推荐
    plan = skill.recommend_methods("了解用户需求", phase=1)

    # 能力2: 访谈提纲
    guide = skill.generate_interview("用户访谈", "contextual")

    # 能力3: 观察记录
    obs = skill.generate_observation("门店观察", "fly_on_wall")

    # 能力4: 可用性测试
    test = skill.generate_usability_test("预订流程测试", "formative")

    # 能力5: 问卷生成
    survey = skill.generate_survey("功能需求调研", "kano", features=["智能推荐"])

    # 能力6: 综合分析
    journey = skill.build_journey_map("预订体验历程")

    # 能力7: 研究计划
    rp = skill.generate_research_plan("体验研究计划")

    # 能力8: 研究报告
    report = skill.generate_report("体验研究报告")
"""

__version__ = "2.0.0"

from .config import (
    AnalysisConfig, METHODS_INDEX, DESIGN_PHASES,
    NIELSEN_HEURISTICS, SUS_QUESTIONS, KANO_CATEGORIES,
    KNOWLEDGE_FILES,
)
from .utils import (
    load_knowledge, load_all_knowledge, search_knowledge,
    get_method, find_method_by_name, search_methods,
    filter_methods, get_methods_for_phase, recommend_methods,
    format_method_card, format_methods_table,
)
from .templates import (
    INTERVIEW_TYPES, INTERVIEW_QUESTIONS, INTERVIEW_TIPS,
    AEIOU_FRAMEWORK, OBSERVATION_TYPES,
    USABILITY_TEST_TYPES, SEVERITY_RATINGS,
    SURVEY_TYPES, SEMANTIC_DIFFERENTIAL_PAIRS,
    PERSONA_TEMPLATE, JOURNEY_MAP_TEMPLATE,
    AFFINITY_DIAGRAM_STEPS, ELITO_METHOD_COLUMNS,
    RESEARCH_PLAN_TEMPLATE, RESEARCH_REPORT_TEMPLATE,
)
from .interview import InterviewBuilder, InterviewGuide
from .observation import ObservationBuilder, ObservationSession
from .usability import (
    UsabilityTestBuilder, UsabilityTestPlan,
    HeuristicEvaluator, HeuristicIssue,
    calculate_sus, interpret_sus, calculate_sus_batch,
    calculate_task_metrics, TaskResult,
)
from .survey import (
    SurveyBuilder, Survey,
    classify_kano, analyze_kano_results,
    calculate_nps,
)
from .synthesis import (
    AffinityDiagramBuilder, AffinityDiagram,
    PersonaBuilder, Persona,
    JourneyMapBuilder, JourneyMap,
    ElitoAnalyzer, ElitoRow,
    WeightedMatrixBuilder,
)
from .recommender import MethodRecommender, ResearchPlan
from .research_plan import ResearchPlanBuilder, ResearchPlanDoc
from .report import ReportBuilder, InsightReport

from typing import Dict, List, Optional


class UDMSkill:
    """UDM 统一入口类 - 封装全部执行能力

    用法::

        skill = UDMSkill("我的产品")

        # 能力1: 方法推荐
        plan = skill.recommend_methods("了解用户需求", phase=1)

        # 能力2: 访谈提纲
        guide = skill.generate_interview("用户访谈", "contextual")

        # 能力3: 可用性测试
        test = skill.generate_usability_test("预订流程测试", "formative")

        # 能力4: SUS计算
        result = skill.calculate_sus([4,2,5,1,4,2,5,1,4,2])

        # 能力5: 问卷生成
        survey = skill.generate_survey("需求调研", "kano", features=["智能推荐"])

        # 能力6: 启发性评估
        checklist = skill.generate_heuristic_checklist()
    """

    def __init__(self, product_name: str, config: Optional[AnalysisConfig] = None):
        self.product = product_name
        self.config = config or AnalysisConfig()
        self.recommender = MethodRecommender()

    # ── 能力1: 方法推荐 ──

    def recommend_methods(self, goal: str, phase: int = 0,
                          resource_level: str = "moderate") -> str:
        plan = self.recommender.recommend(goal, phase, resource_level)
        return MethodRecommender.render_markdown(plan)

    # ── 能力2: 访谈提纲生成 ──

    def generate_interview(self, title: str,
                           interview_type: str = "semi_structured",
                           context: str = "",
                           duration: int = 60) -> str:
        builder = InterviewBuilder(title, interview_type)
        if context:
            builder.set_context(context)
        builder.set_duration(duration)
        guide = builder.build()
        return InterviewBuilder.render_markdown(guide)

    # ── 能力3: 观察记录模板 ──

    def generate_observation(self, title: str,
                             obs_type: str = "fly_on_wall",
                             setting: str = "") -> str:
        builder = ObservationBuilder(title, obs_type)
        if setting:
            builder.set_setting(setting)
        session = builder.build()
        return ObservationBuilder.render_markdown(session)

    def generate_aeiou_template(self) -> str:
        return ObservationBuilder.generate_aeiou_template()

    # ── 能力4: 可用性测试 ──

    def generate_usability_test(self, title: str,
                                test_type: str = "formative",
                                tasks: Optional[List[Dict]] = None) -> str:
        builder = UsabilityTestBuilder(title, test_type)
        builder.set_product(self.product)
        if tasks:
            for t in tasks:
                builder.add_task(**t)
        plan = builder.build()
        return UsabilityTestBuilder.render_markdown(plan)

    def generate_heuristic_checklist(self) -> str:
        evaluator = HeuristicEvaluator(self.product)
        return evaluator.render_checklist()

    def calculate_sus(self, responses: List[int]) -> Dict:
        score = calculate_sus(responses)
        return interpret_sus(score)

    def calculate_sus_batch(self, all_responses: List[List[int]]) -> Dict:
        return calculate_sus_batch(all_responses)

    def calculate_nps(self, scores: List[int]) -> Dict:
        return calculate_nps(scores)

    # ── 能力5: 问卷生成 ──

    def generate_survey(self, title: str, survey_type: str,
                        features: Optional[List[str]] = None,
                        target: str = "") -> str:
        builder = SurveyBuilder(title, survey_type)
        builder.set_product(self.product)
        if features:
            builder.set_features(features)
        if target:
            builder.set_target(target)
        survey = builder.build()
        return SurveyBuilder.render_markdown(survey)

    def analyze_kano(self, features: Dict) -> Dict:
        return analyze_kano_results(features)

    # ── 能力6: 综合分析 ──

    def build_journey_map(self, title: str, persona: str = "") -> JourneyMapBuilder:
        builder = JourneyMapBuilder(title)
        if persona:
            builder.set_persona(persona)
        return builder

    def build_persona(self, name: str) -> PersonaBuilder:
        return PersonaBuilder(name)

    def build_affinity_diagram(self, title: str) -> AffinityDiagramBuilder:
        return AffinityDiagramBuilder(title)

    def build_elito(self, title: str) -> ElitoAnalyzer:
        return ElitoAnalyzer(title)

    def build_weighted_matrix(self, title: str) -> WeightedMatrixBuilder:
        return WeightedMatrixBuilder(title)

    # ── 能力7: 研究计划 ──

    def generate_research_plan(self, title: str,
                               background: str = "") -> ResearchPlanBuilder:
        builder = ResearchPlanBuilder(title)
        if background:
            builder.set_background(background)
        return builder

    # ── 能力8: 研究报告 ──

    def generate_report(self, title: str,
                        summary: str = "") -> ReportBuilder:
        builder = ReportBuilder(title)
        builder.set_project(self.product)
        if summary:
            builder.set_summary(summary)
        return builder

    # ── 知识库查询 ──

    def search_knowledge(self, keyword: str) -> Dict[str, List[str]]:
        return search_knowledge(keyword)

    def get_method_info(self, method_id: int) -> Optional[Dict]:
        return get_method(method_id)

    def find_method(self, name: str) -> Optional[Dict]:
        return find_method_by_name(name)

    def list_methods(self, phase: Optional[int] = None,
                     purpose: Optional[str] = None,
                     data_type: Optional[str] = None) -> str:
        methods = filter_methods(
            phases=[phase] if phase else None,
            purpose=purpose, data_type=data_type)
        return format_methods_table(methods)

    # ── CEO 视角方法 (3 个) ──

    def add_method_roi(self, methods: Optional[List[Dict]] = None) -> str:
        """
        CEO 决策方法 1: 添加方法 ROI 评估

        为推荐的研究方法添加 ROI 评估，帮助 CEO 理解每种方法的投资回报。

        Args:
            methods: 方法列表，每项包含 name, cost, time, value, roi_score, confidence 等。
                     若不传入则使用通用默认值作为参考基线。

        Returns:
            Markdown 格式的 ROI 评估报告

        Example::

            skill = UDMSkill("用户体验研究")
            roi = skill.add_method_roi([
                {"name": "用户访谈", "cost": "低", "time": "2 周", "value": "高", "roi_score": 8.5, "confidence": "高"},
                {"name": "问卷调查", "cost": "中", "time": "1 周", "value": "中", "roi_score": 7.5, "confidence": "中"},
            ])
        """
        default_methods = [
            {"name": "深度用户访谈", "cost": "中 (5-10 人天)", "time": "2-3 周", "value": "高 - 深度洞察", "roi_score": 8.5, "confidence": "高"},
            {"name": "可用性测试", "cost": "低 (3-5 人天)", "time": "1-2 周", "value": "高 - 问题发现", "roi_score": 9.0, "confidence": "高"},
            {"name": "问卷调查", "cost": "低 (1-2 人天)", "time": "1 周", "value": "中 - 量化验证", "roi_score": 7.5, "confidence": "中"},
            {"name": "日记研究", "cost": "高 (4-6 周)", "time": "4-6 周", "value": "中高 - 行为追踪", "roi_score": 6.5, "confidence": "中"},
            {"name": "A/B 测试", "cost": "中 (开发资源)", "time": "2-4 周", "value": "高 - 因果验证", "roi_score": 8.0, "confidence": "高"},
        ]
        methods_list = methods if methods else default_methods

        lines = [
            "## 💰 研究方法 ROI 评估",
            "",
            f"**项目**: {self.product} | **评估维度**: 成本/时间/价值/ROI",
            "",
            "### ROI 矩阵",
            "",
            "| 方法 | 成本 | 时间 | 价值 | ROI 评分 | 把握度 |",
            "|------|------|------|------|---------|--------|",
        ]

        for m in methods_list:
            name = m.get("name", "-")
            cost = m.get("cost", "-")
            time = m.get("time", "-")
            value = m.get("value", "-")
            roi = m.get("roi_score", "-")
            conf = m.get("confidence", "-")
            roi_emoji = "🟢" if isinstance(roi, (int, float)) and roi >= 8 else "🟡" if isinstance(roi, (int, float)) and roi >= 6 else "🟠"
            lines.append(f"| {name} | {cost} | {time} | {value} | {roi_emoji} {roi} | {conf} |")

        roi_scores = [m.get("roi_score", 0) for m in methods_list if isinstance(m.get("roi_score"), (int, float))]
        avg_roi = sum(roi_scores) / len(roi_scores) if roi_scores else 0

        lines.extend([
            "",
            "### ROI 分析",
            "",
            f"**平均 ROI 评分**: {avg_roi:.1f}/10",
            f"**最高 ROI**: {max(roi_scores) if roi_scores else 'N/A'} - {[m['name'] for m in methods_list if m.get('roi_score') == max(roi_scores)][0] if roi_scores else 'N/A'}",
            f"**最低 ROI**: {min(roi_scores) if roi_scores else 'N/A'} - {[m['name'] for m in methods_list if m.get('roi_score') == min(roi_scores)][0] if roi_scores else 'N/A'}",
            "",
            "### 投资建议",
            "",
            "| 优先级 | 方法 | 理由 |",
            "|--------|------|------|",
        ])

        sorted_methods = sorted(methods_list, key=lambda x: x.get("roi_score", 0), reverse=True)
        for i, m in enumerate(sorted_methods[:3], 1):
            priority = "P0 - 必做" if i == 1 else "P1 - 推荐" if i == 2 else "P2 - 可选"
            lines.append(f"| {priority} | {m['name']} | ROI={m.get('roi_score', 'N/A')}, {m.get('value', '')} |")

        lines.extend([
            "",
            "### CEO 决策提示",
            "",
            f"1. **优先投入**: 前 2 个方法贡献约 70% 的洞察价值",
            f"2. **预算建议**: 总预算的 60% 投入 P0/P1 方法",
            f"3. **时间窗口**: 高 ROI 方法应在项目早期执行（前 2 周）",
            "",
        ])

        return "\n".join(lines)

    def generate_decision_outputs(self, research_question: str = "") -> str:
        """
        CEO 决策方法 2: 生成预期决策产出

        明确研究项目完成后，CEO 可以获得哪些决策依据和行动指引。

        Args:
            research_question: 核心研究问题，默认为通用体验优化问题

        Returns:
            Markdown 格式的决策产出说明

        Example::

            skill = UDMSkill("用户体验研究")
            outputs = skill.generate_decision_outputs("如何提升预订转化率？")
        """
        rq = research_question or "如何提升用户体验？"

        lines = [
            "## 📋 预期决策产出",
            "",
            f"**项目**: {self.product}",
            f"**核心研究问题**: {rq}",
            "",
            "### 决策产出清单",
            "",
            "| 产出类型 | 具体内容 | 决策用途 | 交付时间 |",
            "|----------|----------|----------|----------|",
            "| 🔍 问题诊断 | Top 5 用户体验问题清单 | 确定优化优先级 | T+1 周 |",
            "| 📊 量化数据 | 关键指标基线 + 目标值 | 设定 OKR | T+2 周 |",
            "| 👤 用户洞察 | 用户画像 + 痛点地图 | 产品定位校准 | T+2 周 |",
            "| 💡 机会识别 | 3-5 个高价值改进机会 | 路线图规划 | T+3 周 |",
            "| ✅ 验证报告 | 方案 A/B 测试结果 | Go/No-Go 决策 | T+4 周 |",
            "",
            "### 关键决策点",
            "",
            "| 决策点 | 所需数据 | 负责人 | 截止 |",
            "|--------|----------|--------|------|",
            "| 是否投入优化 | 问题严重性 + ROI 估算 | CEO | T+2 周 |",
            "| 优先级排序 | 影响力/可行性矩阵 | 产品 VP | T+2 周 |",
            "| 资源分配 | 各方案成本/回报对比 | CFO | T+3 周 |",
            "| 上线决策 | A/B 测试显著性 | CTO | T+4 周 |",
            "",
            "### 决策质量标准",
            "",
            "| 标准 | 要求 | 验证方式 |",
            "|------|------|----------|",
            "| 数据充分 | 样本量≥统计显著 | 统计检验 |",
            "| 洞察可行动 | 每条洞察对应具体行动 | 行动映射 |",
            "| 风险透明 | 关键风险已识别 + 缓解方案 | 风险清单 |",
            "| ROI 清晰 | 投入/回报有量化估算 | 商业论证 |",
            "",
            "### CEO 使用说明",
            "",
            "1. **T+1 周**: 审查问题诊断，确认方向正确",
            "2. **T+2 周**: 基于量化数据设定 OKR，批准优先级",
            "3. **T+3 周**: 审批资源分配，确认商业论证",
            "4. **T+4 周**: 基于验证报告做出 Go/No-Go 决策",
            "",
            "**决策依据充分度**: 🟢 高（量化 + 定性双重验证）",
            "",
        ]

        return "\n".join(lines)

    def generate_resource_allocation(self, budget: Optional[Dict] = None) -> str:
        """
        CEO 决策方法 3: 生成资源分配建议

        为 CEO 提供研究项目的资源分配建议，包括人力、预算、时间维度。
        传入实际预算信息可获得更精准的分配方案，否则使用通用默认值。

        Args:
            budget: 预算信息，包含 total, headcount, timeline, currency 等

        Returns:
            Markdown 格式的资源分配建议

        Example::

            skill = UDMSkill("用户体验研究")
            allocation = skill.generate_resource_allocation({
                "total": 500000,
                "headcount": 5,
                "timeline": "8 周"
            })
        """
        budget_info = budget or {
            "total": 300000,
            "headcount": 3,
            "timeline": "6 周",
            "currency": "CNY",
        }

        total = budget_info.get("total", 300000)
        headcount = budget_info.get("headcount", 3)
        timeline = budget_info.get("timeline", "6 周")
        currency = budget_info.get("currency", "CNY")

        allocation = {
            "研究执行": 0.40,
            "用户招募": 0.15,
            "工具/平台": 0.10,
            "分析/报告": 0.20,
            "应急储备": 0.15,
        }

        lines = [
            "## 💼 资源分配建议",
            "",
            f"**项目**: {self.product}",
            f"**总预算**: {total:,.0f} {currency} | **团队**: {headcount}人 | **周期**: {timeline}",
            "",
            "### 预算分配",
            "",
            "| 类别 | 比例 | 金额 | 用途 |",
            "|------|------|------|------|",
        ]

        for category, ratio in allocation.items():
            amount = total * ratio
            usage = {
                "研究执行": "访谈/测试执行，研究员人力",
                "用户招募": "用户招募激励，招募平台费用",
                "工具/平台": "调研工具订阅，测试平台",
                "分析/报告": "数据分析，报告撰写，可视化",
                "应急储备": "需求变更，额外迭代",
            }.get(category, "")
            lines.append(f"| {category} | {ratio*100:.0f}% | {amount:,.0f} | {usage} |")

        lines.extend([
            "",
            "### 人力分配",
            "",
            "| 角色 | 人数 | 投入比例 | 主要职责 |",
            "|------|------|----------|----------|",
            f"| 用研负责人 | 1 | 100% | 研究设计，执行，报告 |",
            f"| 数据分析师 | {max(1, headcount//3):.0f} | 50% | 数据分析，统计检验 |",
            f"| 用户招募 | {max(1, headcount//3):.0f} | 30% | 用户招募，排期协调 |",
            f"| 产品代表 | 1 | 20% | 需求对齐，洞察转化 |",
            "",
            "### 时间分配",
            "",
            "| 阶段 | 周期 | 关键产出 | 资源峰值 |",
            "|------|------|----------|----------|",
            "| 研究设计 | 第 1 周 | 研究计划，访谈提纲 | 低 |",
            "| 用户招募 | 第 1-2 周 | 用户名单，排期确认 | 中 |",
            "| 数据收集 | 第 2-4 周 | 访谈记录，测试数据 | 高 |",
            "| 分析洞察 | 第 4-5 周 | 洞察报告，机会清单 | 高 |",
            "| 报告汇报 | 第 5-6 周 | 最终报告，决策建议 | 中 |",
            "",
            "### 资源风险",
            "",
            "| 风险 | 概率 | 影响 | 缓解措施 |",
            "|------|------|------|----------|",
            "| 用户招募延期 | 中 | 高 | 提前启动，准备备选渠道 |",
            "| 关键人员冲突 | 低 | 高 | 预留备份人选，交叉培训 |",
            "| 需求变更 | 中 | 中 | 冻结研究范围，变更需审批 |",
            "| 预算超支 | 低 | 中 | 每周审查支出，启用应急储备需 CEO 审批 |",
            "",
            "### CEO 审批建议",
            "",
            f"1. **预算批准**: {total:,.0f} {currency}（含 15% 应急储备）",
            f"2. **人力确认**: {headcount}人专职团队，{timeline}周期",
            f"3. **关键里程碑**: 第 2/4/6 周审查进展",
            f"4. **变更阈值**: 预算变更>10% 或时间延期>1 周需 CEO 审批",
            "",
        ])

        return "\n".join(lines)


__all__ = [
    "UDMSkill",
    "AnalysisConfig", "METHODS_INDEX", "DESIGN_PHASES",
    "NIELSEN_HEURISTICS", "SUS_QUESTIONS", "KANO_CATEGORIES",
    "load_knowledge", "load_all_knowledge", "search_knowledge",
    "get_method", "find_method_by_name", "search_methods",
    "filter_methods", "format_method_card", "format_methods_table",
    "InterviewBuilder", "InterviewGuide",
    "ObservationBuilder", "ObservationSession",
    "UsabilityTestBuilder", "HeuristicEvaluator",
    "calculate_sus", "interpret_sus", "calculate_sus_batch",
    "SurveyBuilder", "Survey",
    "classify_kano", "analyze_kano_results", "calculate_nps",
    "AffinityDiagramBuilder", "PersonaBuilder", "JourneyMapBuilder",
    "ElitoAnalyzer", "WeightedMatrixBuilder",
    "MethodRecommender", "ResearchPlan",
    "ResearchPlanBuilder", "ResearchPlanDoc",
    "ReportBuilder", "InsightReport",
]
