"""UDM 研究计划生成器

提供完整研究计划的结构化生成，包括研究目标、方法选择、
参与者招募、时间规划、预算估算等。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .config import METHODS_INDEX, DESIGN_PHASES
from .templates import RESEARCH_PLAN_TEMPLATE


@dataclass
class ResearchObjective:
    """研究目标"""
    question: str
    priority: int = 1  # 1=主要, 2=次要


@dataclass
class MethodSelection:
    """选定的研究方法"""
    method_id: int
    name: str
    rationale: str = ""
    participants_needed: int = 0
    duration_days: int = 1
    cost_estimate: float = 0


@dataclass
class TimelineItem:
    """时间线条目"""
    phase: str
    activity: str
    duration: str
    deliverable: str = ""


@dataclass
class ResearchPlanDoc:
    """完整研究计划文档"""
    title: str
    background: str = ""
    objectives: List[ResearchObjective] = field(default_factory=list)
    methods: List[MethodSelection] = field(default_factory=list)
    participant_criteria: List[str] = field(default_factory=list)
    sample_size: int = 0
    recruit_channels: List[str] = field(default_factory=list)
    timeline: List[TimelineItem] = field(default_factory=list)
    deliverables: List[str] = field(default_factory=list)
    team_roles: Dict[str, str] = field(default_factory=dict)
    budget_items: Dict[str, float] = field(default_factory=dict)
    risks: Dict[str, str] = field(default_factory=dict)


class ResearchPlanBuilder:
    """研究计划构建器

    用法::
        builder = ResearchPlanBuilder("飞猪酒店预订体验研究")
        builder.set_background("用户反馈酒店预订流程复杂...")
        builder.add_objective("了解用户预订酒店的核心痛点", priority=1)
        builder.add_method(48, "访谈", "深入了解用户动机", participants=10)
        builder.add_method(94, "可用性测试", "评估现有流程", participants=8)
        builder.add_participant_criteria("过去3个月预订过酒店")
        builder.add_timeline_item("准备", "招募与材料准备", "1周")
        plan = builder.build()
        print(ResearchPlanBuilder.render_markdown(plan))
    """

    def __init__(self, title: str):
        self.title = title
        self._bg = ""
        self._objectives: List[ResearchObjective] = []
        self._methods: List[MethodSelection] = []
        self._criteria: List[str] = []
        self._sample = 0
        self._channels: List[str] = []
        self._timeline: List[TimelineItem] = []
        self._deliverables: List[str] = []
        self._team: Dict[str, str] = {}
        self._budget: Dict[str, float] = {}
        self._risks: Dict[str, str] = {}

    def set_background(self, bg: str) -> "ResearchPlanBuilder":
        self._bg = bg
        return self

    def add_objective(self, question: str, priority: int = 1) -> "ResearchPlanBuilder":
        self._objectives.append(ResearchObjective(question=question, priority=priority))
        return self

    def add_method(self, method_id: int, name: str = "",
                   rationale: str = "", participants: int = 0,
                   days: int = 1, cost: float = 0) -> "ResearchPlanBuilder":
        if not name and method_id in METHODS_INDEX:
            name = METHODS_INDEX[method_id]["name"]
        self._methods.append(MethodSelection(
            method_id=method_id, name=name, rationale=rationale,
            participants_needed=participants, duration_days=days,
            cost_estimate=cost))
        self._sample = max(self._sample, participants)
        return self

    def add_participant_criteria(self, criteria: str) -> "ResearchPlanBuilder":
        self._criteria.append(criteria)
        return self

    def set_sample_size(self, n: int) -> "ResearchPlanBuilder":
        self._sample = n
        return self

    def add_recruit_channel(self, channel: str) -> "ResearchPlanBuilder":
        self._channels.append(channel)
        return self

    def add_timeline_item(self, phase: str, activity: str,
                          duration: str, deliverable: str = "") -> "ResearchPlanBuilder":
        self._timeline.append(TimelineItem(
            phase=phase, activity=activity,
            duration=duration, deliverable=deliverable))
        return self

    def add_deliverable(self, d: str) -> "ResearchPlanBuilder":
        self._deliverables.append(d)
        return self

    def add_team_role(self, role: str, person: str) -> "ResearchPlanBuilder":
        self._team[role] = person
        return self

    def add_budget_item(self, item: str, cost: float) -> "ResearchPlanBuilder":
        self._budget[item] = cost
        return self

    def add_risk(self, risk: str, mitigation: str) -> "ResearchPlanBuilder":
        self._risks[risk] = mitigation
        return self

    def build(self) -> ResearchPlanDoc:
        return ResearchPlanDoc(
            title=self.title, background=self._bg,
            objectives=self._objectives, methods=self._methods,
            participant_criteria=self._criteria, sample_size=self._sample,
            recruit_channels=self._channels, timeline=self._timeline,
            deliverables=self._deliverables, team_roles=self._team,
            budget_items=self._budget, risks=self._risks)

    @staticmethod
    def render_markdown(plan: ResearchPlanDoc) -> str:
        lines = [f"# {plan.title}\n"]

        lines.append("## 1. 研究背景\n")
        lines.append(plan.background or "（待填写）")
        lines.append("")

        lines.append("## 2. 研究目标\n")
        for i, obj in enumerate(plan.objectives, 1):
            tag = "🔴 主要" if obj.priority == 1 else "🟡 次要"
            lines.append(f"{i}. [{tag}] {obj.question}")
        lines.append("")

        lines.append("## 3. 研究方法\n")
        for m in plan.methods:
            info = METHODS_INDEX.get(m.method_id, {})
            lines.append(f"### {m.name} ({info.get('en', '')})\n")
            if m.rationale:
                lines.append(f"- **选择理由:** {m.rationale}")
            if m.participants_needed:
                lines.append(f"- **参与人数:** {m.participants_needed}")
            lines.append(f"- **预计天数:** {m.duration_days}")
            if m.cost_estimate:
                lines.append(f"- **预估费用:** ¥{m.cost_estimate:,.0f}")
            lines.append("")

        lines.append("## 4. 参与者\n")
        if plan.participant_criteria:
            lines.append("**招募标准:**")
            for c in plan.participant_criteria:
                lines.append(f"- {c}")
        lines.append(f"\n**样本量:** {plan.sample_size}人")
        if plan.recruit_channels:
            lines.append("\n**招募渠道:**")
            for ch in plan.recruit_channels:
                lines.append(f"- {ch}")
        lines.append("")

        if plan.timeline:
            lines.append("## 5. 时间计划\n")
            lines.append("| 阶段 | 活动 | 时长 | 交付物 |")
            lines.append("|------|------|------|--------|")
            for t in plan.timeline:
                lines.append(f"| {t.phase} | {t.activity} | {t.duration} | {t.deliverable} |")
            lines.append("")

        if plan.deliverables:
            lines.append("## 6. 预期产出\n")
            for d in plan.deliverables:
                lines.append(f"- {d}")
            lines.append("")

        if plan.team_roles:
            lines.append("## 7. 团队分工\n")
            for role, person in plan.team_roles.items():
                lines.append(f"- **{role}:** {person}")
            lines.append("")

        if plan.budget_items:
            lines.append("## 8. 预算\n")
            lines.append("| 项目 | 费用 |")
            lines.append("|------|------|")
            total = 0.0
            for item, cost in plan.budget_items.items():
                lines.append(f"| {item} | ¥{cost:,.0f} |")
                total += cost
            lines.append(f"| **合计** | **¥{total:,.0f}** |")
            lines.append("")

        if plan.risks:
            lines.append("## 9. 风险与应对\n")
            lines.append("| 风险 | 应对措施 |")
            lines.append("|------|---------|")
            for risk, mit in plan.risks.items():
                lines.append(f"| {risk} | {mit} |")

        return "\n".join(lines)
