"""UDM Skill 配置模块 - 100种通用设计方法的完整索引与全局配置"""
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

KNOWLEDGE_BASE_DIR = Path(__file__).parent.parent / "references"

KNOWLEDGE_FILES: Dict[str, str] = {
    "exploration": "methods-exploration.md",
    "generative": "methods-generative.md",
    "evaluative": "methods-evaluative.md",
    "synthesis": "methods-synthesis.md",
    "communication": "methods-communication.md",
    "templates": "execution-templates.md",
    "decision": "decision-framework.md",
}

DESIGN_PHASES: Dict[int, Dict[str, str]] = {
    1: {"name": "规划与定义", "en": "Planning & Scoping", "goal": "探索和定义项目边界"},
    2: {"name": "探索与综合", "en": "Exploration & Synthesis", "goal": "推断设计影响"},
    3: {"name": "概念生成", "en": "Concept Generation", "goal": "衍生性设计活动"},
    4: {"name": "评估与细化", "en": "Evaluation & Refinement", "goal": "评估、细化和生产"},
    5: {"name": "启动与监控", "en": "Launch & Monitoring", "goal": "全程审查与修正"},
}

METHOD_PURPOSES = ("exploration", "generative", "evaluative", "synthesis")
DATA_TYPES = ("quantitative", "qualitative", "mixed")
PARTICIPANT_ROLES = ("participatory", "observational", "self_report", "expert_review", "design_process")

# fmt: off
METHODS_INDEX: Dict[int, Dict] = {
    1:  {"name":"A/B测试","en":"A/B Testing","cat":"evaluative","phases":[4,5],"purpose":"evaluative","data":"quantitative"},
    2:  {"name":"AEIOU","en":"AEIOU","cat":"synthesis","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    3:  {"name":"亲和图","en":"Affinity Diagramming","cat":"synthesis","phases":[2,3],"purpose":"synthesis","data":"qualitative"},
    4:  {"name":"组件分析","en":"Artifact Analysis","cat":"exploration","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    5:  {"name":"自动远程研究","en":"Automated Remote Research","cat":"evaluative","phases":[4,5],"purpose":"evaluative","data":"quantitative"},
    6:  {"name":"行为地图","en":"Behavioral Mapping","cat":"exploration","phases":[1,2],"purpose":"exploration","data":"mixed"},
    7:  {"name":"身体风暴","en":"Bodystorming","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    8:  {"name":"头脑风暴图像组织法","en":"Brainwriting","cat":"generative","phases":[3],"purpose":"generative","data":"qualitative"},
    9:  {"name":"商业折纸","en":"Business Origami","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    10: {"name":"卡片分类","en":"Card Sorting","cat":"generative","phases":[2,3,4],"purpose":"generative","data":"mixed"},
    11: {"name":"案例研究","en":"Case Studies","cat":"exploration","phases":[1],"purpose":"exploration","data":"qualitative"},
    12: {"name":"认知图","en":"Cognitive Mapping","cat":"synthesis","phases":[2],"purpose":"exploration","data":"qualitative"},
    13: {"name":"认知过程浏览","en":"Cognitive Walkthrough","cat":"evaluative","phases":[4],"purpose":"evaluative","data":"qualitative"},
    14: {"name":"拼贴","en":"Collage","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    15: {"name":"竞争测试","en":"Competitive Testing","cat":"evaluative","phases":[1,4],"purpose":"evaluative","data":"mixed"},
    16: {"name":"概念图","en":"Concept Mapping","cat":"synthesis","phases":[2,3],"purpose":"synthesis","data":"qualitative"},
    17: {"name":"内容分析","en":"Content Analysis","cat":"synthesis","phases":[1,2,4],"purpose":"synthesis","data":"mixed"},
    18: {"name":"内容清单和内容审核","en":"Content Inventory & Audit","cat":"synthesis","phases":[1,4],"purpose":"evaluative","data":"mixed"},
    19: {"name":"脉络设计","en":"Contextual Design","cat":"synthesis","phases":[1,2,3,4],"purpose":"synthesis","data":"qualitative"},
    20: {"name":"脉络访查","en":"Contextual Inquiry","cat":"exploration","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    21: {"name":"创意工具包","en":"Creative Toolkits","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    22: {"name":"关键事件法","en":"Critical Incident Technique","cat":"communication","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    23: {"name":"群众外包","en":"Crowdsourcing","cat":"communication","phases":[1,2,3],"purpose":"exploration","data":"mixed"},
    24: {"name":"文化探寻","en":"Cultural Probes","cat":"exploration","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    25: {"name":"用户体验审核","en":"Customer Experience Audit","cat":"evaluative","phases":[1,4,5],"purpose":"evaluative","data":"qualitative"},
    26: {"name":"设计讨论组","en":"Design Charettes","cat":"communication","phases":[2,3],"purpose":"generative","data":"qualitative"},
    27: {"name":"设计人种学","en":"Design Ethnography","cat":"exploration","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    28: {"name":"协同设计","en":"Co-design","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    29: {"name":"期望值测试","en":"Desirability Testing","cat":"evaluative","phases":[4],"purpose":"evaluative","data":"mixed"},
    30: {"name":"日记研究","en":"Diary Studies","cat":"exploration","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    31: {"name":"引导性叙事","en":"Directed Storytelling","cat":"communication","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    32: {"name":"Elito方法","en":"Elito Method","cat":"synthesis","phases":[2,3],"purpose":"synthesis","data":"qualitative"},
    33: {"name":"人体工程学分析","en":"Ergonomic Analysis","cat":"evaluative","phases":[4],"purpose":"evaluative","data":"quantitative"},
    34: {"name":"评估性研究","en":"Evaluative Research","cat":"evaluative","phases":[4,5],"purpose":"evaluative","data":"mixed"},
    35: {"name":"实证设计","en":"Evidence-Based Design","cat":"communication","phases":[1,2,3,4,5],"purpose":"synthesis","data":"mixed"},
    36: {"name":"经验原型","en":"Experience Prototyping","cat":"generative","phases":[3,4],"purpose":"generative","data":"qualitative"},
    37: {"name":"经验取样法","en":"Experience Sampling","cat":"communication","phases":[1,2],"purpose":"exploration","data":"mixed"},
    38: {"name":"实验","en":"Experiments","cat":"evaluative","phases":[4],"purpose":"evaluative","data":"quantitative"},
    39: {"name":"探索性研究","en":"Exploratory Research","cat":"exploration","phases":[1],"purpose":"exploration","data":"qualitative"},
    40: {"name":"眼动追踪","en":"Eye Tracking","cat":"evaluative","phases":[4],"purpose":"evaluative","data":"quantitative"},
    41: {"name":"弹性建模","en":"Flexible Modeling","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    42: {"name":"隐蔽观察","en":"Fly-on-the-Wall Observation","cat":"exploration","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    43: {"name":"焦点小组","en":"Focus Groups","cat":"communication","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    44: {"name":"衍生性研究","en":"Generative Research","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    45: {"name":"涂鸦墙","en":"Graffiti Walls","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    46: {"name":"启发性评估","en":"Heuristic Evaluation","cat":"evaluative","phases":[4],"purpose":"evaluative","data":"qualitative"},
    47: {"name":"意向看板","en":"Image Boards","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    48: {"name":"访谈","en":"Interviews","cat":"exploration","phases":[1,2,3],"purpose":"exploration","data":"qualitative"},
    49: {"name":"KJ法","en":"KJ Technique","cat":"synthesis","phases":[2,3],"purpose":"synthesis","data":"qualitative"},
    50: {"name":"卡诺分析","en":"Kano Analysis","cat":"evaluative","phases":[1,4],"purpose":"evaluative","data":"quantitative"},
    51: {"name":"关键绩效指标","en":"KPI","cat":"synthesis","phases":[4,5],"purpose":"evaluative","data":"quantitative"},
    52: {"name":"阶梯法","en":"Laddering","cat":"exploration","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    53: {"name":"文献综述","en":"Literature Reviews","cat":"exploration","phases":[1],"purpose":"exploration","data":"mixed"},
    54: {"name":"情书与分手信","en":"Love Letter & Breakup Letter","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    55: {"name":"心智模式图","en":"Mental Model Diagrams","cat":"synthesis","phases":[2,3],"purpose":"synthesis","data":"qualitative"},
    56: {"name":"思维导图","en":"Mind Mapping","cat":"synthesis","phases":[2,3],"purpose":"generative","data":"qualitative"},
    57: {"name":"观察法","en":"Observation","cat":"exploration","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    58: {"name":"平行原型","en":"Parallel Prototyping","cat":"generative","phases":[3],"purpose":"generative","data":"qualitative"},
    59: {"name":"参与观察法","en":"Participant Observation","cat":"exploration","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    60: {"name":"参与式行动研究","en":"PAR","cat":"generative","phases":[1,2,3],"purpose":"generative","data":"qualitative"},
    61: {"name":"参与性设计","en":"Participatory Design","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    62: {"name":"个人清单","en":"Personal Inventories","cat":"communication","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    63: {"name":"角色分析","en":"Personas","cat":"synthesis","phases":[2,3],"purpose":"synthesis","data":"qualitative"},
    64: {"name":"照片研究","en":"Photo Studies","cat":"communication","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    65: {"name":"图像卡","en":"Picture Cards","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    66: {"name":"原型","en":"Prototyping","cat":"generative","phases":[3,4],"purpose":"generative","data":"mixed"},
    67: {"name":"问卷调查","en":"Questionnaires","cat":"evaluative","phases":[1,4,5],"purpose":"evaluative","data":"quantitative"},
    68: {"name":"快速反复测试与评估","en":"RITE","cat":"evaluative","phases":[4],"purpose":"evaluative","data":"qualitative"},
    69: {"name":"适度远程研究","en":"Moderated Remote Research","cat":"communication","phases":[4],"purpose":"evaluative","data":"qualitative"},
    70: {"name":"通过设计进行研究","en":"Research through Design","cat":"communication","phases":[2,3],"purpose":"generative","data":"qualitative"},
    71: {"name":"角色扮演","en":"Role Playing","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    72: {"name":"情景描述泳道图","en":"Scenario Description Swimlanes","cat":"synthesis","phases":[2,3],"purpose":"synthesis","data":"qualitative"},
    73: {"name":"情景法","en":"Scenarios","cat":"generative","phases":[2,3],"purpose":"generative","data":"qualitative"},
    74: {"name":"次级研究","en":"Secondary Research","cat":"exploration","phases":[1],"purpose":"exploration","data":"mixed"},
    75: {"name":"语义差异法","en":"Semantic Differential","cat":"evaluative","phases":[4],"purpose":"evaluative","data":"quantitative"},
    76: {"name":"影形","en":"Shadowing","cat":"exploration","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    77: {"name":"模拟练习","en":"Simulation Exercises","cat":"communication","phases":[3,4],"purpose":"generative","data":"qualitative"},
    78: {"name":"站内搜索分析","en":"Site Search Analytics","cat":"communication","phases":[4,5],"purpose":"evaluative","data":"quantitative"},
    79: {"name":"快速约会","en":"Speed Dating","cat":"communication","phases":[3,4],"purpose":"generative","data":"qualitative"},
    80: {"name":"利益相关者分析图","en":"Stakeholder Maps","cat":"synthesis","phases":[1],"purpose":"exploration","data":"qualitative"},
    81: {"name":"利益相关者浏览","en":"Stakeholder Walkthrough","cat":"communication","phases":[4],"purpose":"evaluative","data":"qualitative"},
    82: {"name":"故事板","en":"Storyboards","cat":"generative","phases":[2,3,4],"purpose":"generative","data":"qualitative"},
    83: {"name":"调查","en":"Surveys","cat":"evaluative","phases":[1,4,5],"purpose":"evaluative","data":"quantitative"},
    84: {"name":"任务分析","en":"Task Analysis","cat":"synthesis","phases":[1,2,4],"purpose":"synthesis","data":"qualitative"},
    85: {"name":"领域图","en":"Territory Maps","cat":"synthesis","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    86: {"name":"主题网络","en":"Thematic Networks","cat":"synthesis","phases":[2],"purpose":"synthesis","data":"qualitative"},
    87: {"name":"有声思维报告","en":"Think-Aloud Protocol","cat":"evaluative","phases":[4],"purpose":"evaluative","data":"qualitative"},
    88: {"name":"时间感知研究","en":"Time-Aware Research","cat":"communication","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    89: {"name":"试金石之旅","en":"Touchstone Tours","cat":"communication","phases":[1,2],"purpose":"exploration","data":"qualitative"},
    90: {"name":"三角比较法","en":"Triading","cat":"synthesis","phases":[2],"purpose":"exploration","data":"qualitative"},
    91: {"name":"三角测量","en":"Triangulation","cat":"synthesis","phases":[1,2,3,4,5],"purpose":"synthesis","data":"mixed"},
    92: {"name":"非干扰性测量","en":"Unobtrusive Measures","cat":"communication","phases":[1,4,5],"purpose":"evaluative","data":"quantitative"},
    93: {"name":"可用性报告","en":"Usability Report","cat":"evaluative","phases":[4,5],"purpose":"evaluative","data":"mixed"},
    94: {"name":"可用性测试","en":"Usability Testing","cat":"evaluative","phases":[4,5],"purpose":"evaluative","data":"mixed"},
    95: {"name":"客户体验历程图","en":"User Journey Maps","cat":"synthesis","phases":[2,4],"purpose":"synthesis","data":"qualitative"},
    96: {"name":"价值机会分析","en":"Value Opportunity Analysis","cat":"evaluative","phases":[1,4],"purpose":"evaluative","data":"mixed"},
    97: {"name":"网站分析","en":"Web Analytics","cat":"evaluative","phases":[4,5],"purpose":"evaluative","data":"quantitative"},
    98: {"name":"加权矩阵","en":"Weighted Matrix","cat":"synthesis","phases":[3,4],"purpose":"evaluative","data":"quantitative"},
    99: {"name":"幕后模拟","en":"Wizard of Oz","cat":"generative","phases":[3,4],"purpose":"generative","data":"qualitative"},
    100:{"name":"文字云","en":"Word Clouds","cat":"synthesis","phases":[2,4],"purpose":"synthesis","data":"mixed"},
}
# fmt: on

NIELSEN_HEURISTICS = (
    "系统状态可见性",
    "系统与现实世界的匹配",
    "用户控制和自由",
    "一致性和标准",
    "错误预防",
    "识别而非回忆",
    "使用的灵活性和效率",
    "美观和简约设计",
    "帮助用户识别、诊断和恢复错误",
    "帮助和文档",
)

SUS_QUESTIONS = (
    "我认为我会经常使用这个系统",
    "我觉得这个系统不必要地复杂",
    "我认为这个系统很容易使用",
    "我认为我需要技术人员的帮助才能使用这个系统",
    "我发现这个系统的各种功能整合得很好",
    "我认为这个系统有太多不一致的地方",
    "我认为大多数人能很快学会使用这个系统",
    "我觉得使用这个系统非常繁琐",
    "我使用这个系统时感到很有信心",
    "在使用这个系统之前，我需要学习很多东西",
)

KANO_CATEGORIES = {
    "must_be": "基本型（Must-be）",
    "one_dimensional": "期望型（One-dimensional）",
    "attractive": "兴奋型（Attractive）",
    "indifferent": "无关型（Indifferent）",
    "reverse": "反向型（Reverse）",
}

@dataclass
class AnalysisConfig:
    """分析任务的运行时配置"""
    include_phases: List[int] = field(default_factory=lambda: [1,2,3,4,5])
    output_format: str = "markdown"
    language: str = "zh"
    max_recommendations: int = 5

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        for p in self.include_phases:
            if p not in range(1, 6):
                raise ValueError(f"未知阶段: {p}，应在1-5之间")
