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
