"""UDM 综合分析引擎

提供亲和图、角色画像、体验历程图、Elito方法、加权矩阵等
综合分析工具的结构化执行支持。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class AffinityNote:
    """亲和图便利贴"""
    content: str
    source: str = ""
    participant_id: str = ""


@dataclass
class AffinityGroup:
    """亲和图分组"""
    title: str
    notes: List[AffinityNote] = field(default_factory=list)
    insight: str = ""

    @property
    def count(self) -> int:
        return len(self.notes)


@dataclass
class AffinityDiagram:
    """完整亲和图"""
    title: str
    groups: List[AffinityGroup] = field(default_factory=list)
    ungrouped: List[AffinityNote] = field(default_factory=list)

    @property
    def total_notes(self) -> int:
        return sum(g.count for g in self.groups) + len(self.ungrouped)


class AffinityDiagramBuilder:
    """亲和图构建器

    用法::
        builder = AffinityDiagramBuilder("用户访谈数据分析")
        builder.add_note("找酒店要花很长时间比价", source="P1")
        builder.add_note("不确定照片是否真实", source="P2")
        builder.add_note("价格经常变动很烦", source="P3")
        builder.create_group("价格痛点", ["价格经常变动很烦"])
        builder.create_group("信任问题", ["不确定照片是否真实"])
        diagram = builder.build()
        print(AffinityDiagramBuilder.render_markdown(diagram))
    """

    def __init__(self, title: str):
        self.title = title
        self._notes: List[AffinityNote] = []
        self._groups: List[AffinityGroup] = []

    def add_note(self, content: str, source: str = "",
                 participant_id: str = "") -> "AffinityDiagramBuilder":
        self._notes.append(AffinityNote(
            content=content, source=source, participant_id=participant_id))
        return self

    def add_notes_batch(self, notes: List[str], source: str = "") -> "AffinityDiagramBuilder":
        for n in notes:
            self._notes.append(AffinityNote(content=n, source=source))
        return self

    def create_group(self, title: str, note_contents: List[str],
                     insight: str = "") -> "AffinityDiagramBuilder":
        matched = [n for n in self._notes if n.content in note_contents]
        self._groups.append(AffinityGroup(
            title=title, notes=matched, insight=insight))
        return self

    def build(self) -> AffinityDiagram:
        grouped_contents = set()
        for g in self._groups:
            for n in g.notes:
                grouped_contents.add(n.content)
        ungrouped = [n for n in self._notes if n.content not in grouped_contents]
        return AffinityDiagram(
            title=self.title, groups=self._groups, ungrouped=ungrouped)

    @staticmethod
    def render_markdown(diagram: AffinityDiagram) -> str:
        lines = [f"# 亲和图: {diagram.title}\n"]
        lines.append(f"**总数据点:** {diagram.total_notes} | **分组数:** {len(diagram.groups)}\n")
        for i, g in enumerate(diagram.groups, 1):
            lines.append(f"## 主题{i}: {g.title} ({g.count}条)\n")
            if g.insight:
                lines.append(f"**洞察:** {g.insight}\n")
            for n in g.notes:
                src = f" [{n.source}]" if n.source else ""
                lines.append(f"- {n.content}{src}")
            lines.append("")
        if diagram.ungrouped:
            lines.append(f"## 未分组 ({len(diagram.ungrouped)}条)\n")
            for n in diagram.ungrouped:
                lines.append(f"- {n.content}")
        return "\n".join(lines)


# ─────────────────────────────────────────────
# 角色画像
# ─────────────────────────────────────────────

@dataclass
class Persona:
    """用户角色画像"""
    name: str
    age: int = 0
    occupation: str = ""
    bio: str = ""
    goals: List[str] = field(default_factory=list)
    pain_points: List[str] = field(default_factory=list)
    behaviors: List[str] = field(default_factory=list)
    tech_level: str = ""
    quote: str = ""
    scenarios: List[str] = field(default_factory=list)


class PersonaBuilder:
    """角色画像构建器

    用法::
        builder = PersonaBuilder("小李")
        builder.set_demographics(28, "产品经理")
        builder.set_bio("在互联网公司工作3年，经常出差")
        builder.add_goal("快速找到性价比高的酒店")
        builder.add_pain_point("比价耗时太长")
        builder.set_quote("我只想5分钟内搞定住宿")
        persona = builder.build()
        print(PersonaBuilder.render_markdown(persona))
    """

    def __init__(self, name: str):
        self._persona = Persona(name=name)

    def set_demographics(self, age: int, occupation: str) -> "PersonaBuilder":
        self._persona.age = age
        self._persona.occupation = occupation
        return self

    def set_bio(self, bio: str) -> "PersonaBuilder":
        self._persona.bio = bio
        return self

    def add_goal(self, goal: str) -> "PersonaBuilder":
        self._persona.goals.append(goal)
        return self

    def add_pain_point(self, pain: str) -> "PersonaBuilder":
        self._persona.pain_points.append(pain)
        return self

    def add_behavior(self, behavior: str) -> "PersonaBuilder":
        self._persona.behaviors.append(behavior)
        return self

    def set_tech_level(self, level: str) -> "PersonaBuilder":
        self._persona.tech_level = level
        return self

    def set_quote(self, quote: str) -> "PersonaBuilder":
        self._persona.quote = quote
        return self

    def add_scenario(self, scenario: str) -> "PersonaBuilder":
        self._persona.scenarios.append(scenario)
        return self

    def build(self) -> Persona:
        return self._persona

    @staticmethod
    def render_markdown(persona: Persona) -> str:
        lines = [f"# 角色画像: {persona.name}\n"]
        if persona.age or persona.occupation:
            lines.append(f"**年龄:** {persona.age} | **职业:** {persona.occupation}")
        if persona.tech_level:
            lines.append(f"**技术水平:** {persona.tech_level}")
        if persona.bio:
            lines.append(f"\n> {persona.bio}\n")
        if persona.quote:
            lines.append(f'💬 *"{persona.quote}"*\n')
        if persona.goals:
            lines.append("## 目标\n")
            for g in persona.goals:
                lines.append(f"- 🎯 {g}")
            lines.append("")
        if persona.pain_points:
            lines.append("## 痛点\n")
            for p in persona.pain_points:
                lines.append(f"- 😣 {p}")
            lines.append("")
        if persona.behaviors:
            lines.append("## 行为模式\n")
            for b in persona.behaviors:
                lines.append(f"- {b}")
            lines.append("")
        if persona.scenarios:
            lines.append("## 典型场景\n")
            for i, s in enumerate(persona.scenarios, 1):
                lines.append(f"{i}. {s}")
        return "\n".join(lines)


# ─────────────────────────────────────────────
# 体验历程图
# ─────────────────────────────────────────────

EMOTION_ICONS = {5: "😄", 4: "🙂", 3: "😐", 2: "😟", 1: "😡"}


@dataclass
class JourneyStage:
    """历程图的一个阶段"""
    name: str
    actions: List[str] = field(default_factory=list)
    touchpoints: List[str] = field(default_factory=list)
    thoughts: List[str] = field(default_factory=list)
    emotions: int = 3  # 1-5
    pain_points: List[str] = field(default_factory=list)
    opportunities: List[str] = field(default_factory=list)


@dataclass
class JourneyMap:
    """完整体验历程图"""
    title: str
    persona: str = ""
    scenario: str = ""
    stages: List[JourneyStage] = field(default_factory=list)


class JourneyMapBuilder:
    """体验历程图构建器

    用法::
        builder = JourneyMapBuilder("酒店预订体验历程")
        builder.set_persona("商旅用户小李")
        builder.add_stage("搜索", actions=["打开App", "输入目的地"],
                         touchpoints=["首页", "搜索栏"],
                         emotions=4, pain_points=["默认排序不合理"])
        journey = builder.build()
        print(JourneyMapBuilder.render_markdown(journey))
    """

    def __init__(self, title: str):
        self.title = title
        self._persona = ""
        self._scenario = ""
        self._stages: List[JourneyStage] = []

    def set_persona(self, persona: str) -> "JourneyMapBuilder":
        self._persona = persona
        return self

    def set_scenario(self, scenario: str) -> "JourneyMapBuilder":
        self._scenario = scenario
        return self

    def add_stage(self, name: str, actions: Optional[List[str]] = None,
                  touchpoints: Optional[List[str]] = None,
                  thoughts: Optional[List[str]] = None,
                  emotions: int = 3,
                  pain_points: Optional[List[str]] = None,
                  opportunities: Optional[List[str]] = None) -> "JourneyMapBuilder":
        self._stages.append(JourneyStage(
            name=name, actions=actions or [], touchpoints=touchpoints or [],
            thoughts=thoughts or [], emotions=emotions,
            pain_points=pain_points or [], opportunities=opportunities or [],
        ))
        return self

    def build(self) -> JourneyMap:
        return JourneyMap(
            title=self.title, persona=self._persona,
            scenario=self._scenario, stages=self._stages)

    @staticmethod
    def render_markdown(journey: JourneyMap) -> str:
        lines = [f"# 体验历程图: {journey.title}\n"]
        if journey.persona:
            lines.append(f"**角色:** {journey.persona}")
        if journey.scenario:
            lines.append(f"**场景:** {journey.scenario}")
        lines.append("")

        # 情绪曲线
        if journey.stages:
            lines.append("## 情绪曲线\n")
            emojis = [EMOTION_ICONS.get(s.emotions, "😐") for s in journey.stages]
            names = [s.name for s in journey.stages]
            lines.append("| " + " | ".join(names) + " |")
            lines.append("|" + "|".join(["---"] * len(names)) + "|")
            lines.append("| " + " | ".join(emojis) + " |")
            lines.append("")

        for i, stage in enumerate(journey.stages, 1):
            icon = EMOTION_ICONS.get(stage.emotions, "😐")
            lines.append(f"## 阶段{i}: {stage.name} {icon}\n")
            if stage.actions:
                lines.append("**行为:** " + " → ".join(stage.actions))
            if stage.touchpoints:
                lines.append("**接触点:** " + ", ".join(stage.touchpoints))
            if stage.thoughts:
                lines.append("**想法:**")
                for t in stage.thoughts:
                    lines.append(f'- 💭 "{t}"')
            if stage.pain_points:
                lines.append("**痛点:**")
                for p in stage.pain_points:
                    lines.append(f"- ❌ {p}")
            if stage.opportunities:
                lines.append("**机会:**")
                for o in stage.opportunities:
                    lines.append(f"- 💡 {o}")
            lines.append("")
        return "\n".join(lines)


# ─────────────────────────────────────────────
# Elito 方法
# ─────────────────────────────────────────────

@dataclass
class ElitoRow:
    """Elito方法的一行"""
    observation: str
    judgment: str = ""
    value: str = ""
    concept: str = ""
    key_metaphor: str = ""


class ElitoAnalyzer:
    """Elito方法分析器

    用法::
        analyzer = ElitoAnalyzer("用户研究洞察转化")
        analyzer.add_row(
            observation="用户在比价时会打开3-4个App反复切换",
            judgment="比价过程碎片化且低效",
            value="用户需要一站式比价能力",
            concept="智能比价聚合功能",
            key_metaphor="一站式购物中心"
        )
        print(analyzer.render_markdown())
    """

    def __init__(self, title: str):
        self.title = title
        self.rows: List[ElitoRow] = []

    def add_row(self, observation: str, judgment: str = "",
                value: str = "", concept: str = "",
                key_metaphor: str = "") -> ElitoRow:
        row = ElitoRow(observation=observation, judgment=judgment,
                       value=value, concept=concept, key_metaphor=key_metaphor)
        self.rows.append(row)
        return row

    def render_markdown(self) -> str:
        lines = [f"# Elito分析: {self.title}\n"]
        lines.append("| 观察 | 判断 | 价值 | 概念 | 关键隐喻 |")
        lines.append("|------|------|------|------|---------|")
        for r in self.rows:
            lines.append(
                f"| {r.observation} | {r.judgment} | {r.value} "
                f"| {r.concept} | {r.key_metaphor} |")
        return "\n".join(lines)


# ─────────────────────────────────────────────
# 加权矩阵
# ─────────────────────────────────────────────

@dataclass
class WeightedCriterion:
    """加权矩阵的评估标准"""
    name: str
    weight: float = 1.0


@dataclass
class WeightedOption:
    """加权矩阵的候选方案"""
    name: str
    scores: Dict[str, int] = field(default_factory=dict)

    def weighted_score(self, criteria: List[WeightedCriterion]) -> float:
        total = 0.0
        for c in criteria:
            total += self.scores.get(c.name, 0) * c.weight
        return round(total, 2)


class WeightedMatrixBuilder:
    """加权矩阵构建器

    用法::
        builder = WeightedMatrixBuilder("设计方案评估")
        builder.add_criterion("用户满意度", weight=0.3)
        builder.add_criterion("开发成本", weight=0.25)
        builder.add_criterion("技术可行性", weight=0.25)
        builder.add_criterion("创新性", weight=0.2)
        builder.add_option("方案A", {"用户满意度": 4, "开发成本": 3,
                                     "技术可行性": 5, "创新性": 2})
        builder.add_option("方案B", {"用户满意度": 5, "开发成本": 2,
                                     "技术可行性": 3, "创新性": 4})
        print(builder.render_markdown())
    """

    def __init__(self, title: str):
        self.title = title
        self.criteria: List[WeightedCriterion] = []
        self.options: List[WeightedOption] = []

    def add_criterion(self, name: str, weight: float = 1.0) -> "WeightedMatrixBuilder":
        self.criteria.append(WeightedCriterion(name=name, weight=weight))
        return self

    def add_option(self, name: str, scores: Dict[str, int]) -> "WeightedMatrixBuilder":
        self.options.append(WeightedOption(name=name, scores=scores))
        return self

    def ranked(self) -> List[WeightedOption]:
        return sorted(self.options,
                      key=lambda o: o.weighted_score(self.criteria), reverse=True)

    def render_markdown(self) -> str:
        lines = [f"# 加权矩阵: {self.title}\n"]
        # 表头
        c_names = [c.name for c in self.criteria]
        header = "| 方案 | " + " | ".join(c_names) + " | 加权总分 |"
        sep = "|------|" + "|".join(["------"] * len(c_names)) + "|--------|"
        lines.append(header)
        lines.append(sep)

        # 权重行
        weights = [f"{c.weight:.0%}" for c in self.criteria]
        lines.append("| *权重* | " + " | ".join(weights) + " | — |")

        for opt in self.ranked():
            scores = [str(opt.scores.get(c.name, 0)) for c in self.criteria]
            total = opt.weighted_score(self.criteria)
            lines.append(f"| **{opt.name}** | " + " | ".join(scores) + f" | **{total}** |")

        winner = self.ranked()[0] if self.options else None
        if winner:
            lines.append(f"\n🏆 **推荐方案:** {winner.name} "
                         f"(加权总分: {winner.weighted_score(self.criteria)})")
        return "\n".join(lines)
