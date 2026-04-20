"""UDM 访谈框架生成器

支持脉络访查、半结构化访谈、阶梯法、关键事件法、引导性叙事等
多种访谈类型的定制化问题列表生成。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .templates import INTERVIEW_QUESTIONS, INTERVIEW_TYPES, INTERVIEW_TIPS


@dataclass
class InterviewQuestion:
    """单个访谈问题"""
    dimension: str
    question: str
    is_custom: bool = False
    priority: int = 1
    follow_up: str = ""
    probe: str = ""


@dataclass
class InterviewGuide:
    """完整的访谈指南"""
    title: str
    interview_type: str
    context: str = ""
    duration_minutes: int = 60
    participant_criteria: str = ""
    questions: List[InterviewQuestion] = field(default_factory=list)
    warm_up: List[str] = field(default_factory=list)
    wrap_up: List[str] = field(default_factory=list)
    tips: List[str] = field(default_factory=list)
    materials: List[str] = field(default_factory=list)

    def get_by_dimension(self, dimension: str) -> List[InterviewQuestion]:
        return [q for q in self.questions if q.dimension == dimension]

    def count_questions(self) -> int:
        return len(self.questions)


DEFAULT_WARM_UP = [
    "感谢您参与本次访谈，您的反馈对我们非常重要。",
    "本次访谈大约需要{duration}分钟，过程中您可以随时休息或终止。",
    "没有对错之分，我们只是想了解您的真实想法和体验。",
    "请问我可以录音吗？录音仅用于研究分析，不会公开。",
    "在开始之前，请简单介绍一下您自己。",
]

DEFAULT_WRAP_UP = [
    "还有什么我们没有聊到但您觉得重要的内容吗？",
    "对于我们今天讨论的话题，您还有什么想补充的？",
    "感谢您宝贵的时间和真诚的分享！",
]


class InterviewBuilder:
    """访谈框架构建器

    用法示例::

        builder = InterviewBuilder("旅行预订用户访谈", "contextual")
        builder.set_context("针对过去3个月使用过竞品的用户")
        builder.set_duration(45)
        builder.add_custom_question("contextual", "你最近一次订酒店的完整过程是怎样的？", priority=3)
        guide = builder.build()
        print(InterviewBuilder.render_markdown(guide))
    """

    def __init__(self, title: str, interview_type: str = "semi_structured"):
        if interview_type not in INTERVIEW_TYPES:
            valid = ", ".join(INTERVIEW_TYPES.keys())
            raise ValueError(f"未知访谈类型: {interview_type}，可选: {valid}")
        self.title = title
        self.interview_type = interview_type
        self._context = ""
        self._duration = 60
        self._participant_criteria = ""
        self._dimensions: List[str] = [interview_type]
        self._custom_questions: List[InterviewQuestion] = []
        self._extra_tips: List[str] = []
        self._materials: List[str] = []

    def set_context(self, context: str) -> "InterviewBuilder":
        self._context = context
        return self

    def set_duration(self, minutes: int) -> "InterviewBuilder":
        self._duration = minutes
        return self

    def set_participant_criteria(self, criteria: str) -> "InterviewBuilder":
        self._participant_criteria = criteria
        return self

    def include_dimensions(self, dimensions: List[str]) -> "InterviewBuilder":
        self._dimensions = dimensions
        return self

    def add_custom_question(self, dimension: str, question: str,
                            priority: int = 1, follow_up: str = "",
                            probe: str = "") -> "InterviewBuilder":
        self._custom_questions.append(InterviewQuestion(
            dimension=dimension, question=question,
            is_custom=True, priority=priority,
            follow_up=follow_up, probe=probe,
        ))
        return self

    def add_tip(self, tip: str) -> "InterviewBuilder":
        self._extra_tips.append(tip)
        return self

    def add_material(self, material: str) -> "InterviewBuilder":
        self._materials.append(material)
        return self

    def build(self) -> InterviewGuide:
        questions: List[InterviewQuestion] = []
        for dim in self._dimensions:
            template_qs = INTERVIEW_QUESTIONS.get(dim, [])
            for q_text in template_qs:
                questions.append(InterviewQuestion(
                    dimension=dim, question=q_text, priority=1))
        for cq in self._custom_questions:
            questions.append(cq)

        warm_up = [s.format(duration=self._duration) for s in DEFAULT_WARM_UP]
        tips = list(INTERVIEW_TIPS) + self._extra_tips

        return InterviewGuide(
            title=self.title,
            interview_type=self.interview_type,
            context=self._context,
            duration_minutes=self._duration,
            participant_criteria=self._participant_criteria,
            questions=questions,
            warm_up=warm_up,
            wrap_up=list(DEFAULT_WRAP_UP),
            tips=tips,
            materials=self._materials,
        )

    @staticmethod
    def render_markdown(guide: InterviewGuide) -> str:
        type_label = INTERVIEW_TYPES.get(guide.interview_type, guide.interview_type)
        lines = [f"# {guide.title}", ""]
        lines.append(f"**访谈类型:** {type_label}")
        lines.append(f"**预计时长:** {guide.duration_minutes} 分钟")
        if guide.context:
            lines.append(f"**访谈背景:** {guide.context}")
        if guide.participant_criteria:
            lines.append(f"**参与者标准:** {guide.participant_criteria}")
        if guide.materials:
            lines.append(f"**所需材料:** {', '.join(guide.materials)}")
        lines.append("")

        lines.append("## 开场白\n")
        for s in guide.warm_up:
            lines.append(f"- {s}")
        lines.append("")

        lines.append("## 访谈问题\n")
        dims_in_order = []
        seen = set()
        for q in guide.questions:
            if q.dimension not in seen:
                dims_in_order.append(q.dimension)
                seen.add(q.dimension)

        for dim in dims_in_order:
            label = INTERVIEW_TYPES.get(dim, dim)
            lines.append(f"### {label}\n")
            dim_qs = [q for q in guide.questions if q.dimension == dim]
            for i, q in enumerate(dim_qs, 1):
                marker = " ⭐" if q.priority >= 3 else ""
                custom_tag = " [自定义]" if q.is_custom else ""
                lines.append(f"{i}. {q.question}{marker}{custom_tag}")
                if q.follow_up:
                    lines.append(f"   - 追问: {q.follow_up}")
                if q.probe:
                    lines.append(f"   - 探针: {q.probe}")
            lines.append("")

        lines.append("## 结束语\n")
        for s in guide.wrap_up:
            lines.append(f"- {s}")
        lines.append("")

        if guide.tips:
            lines.append("## 访谈技巧\n")
            for tip in guide.tips:
                lines.append(f"- {tip}")

        return "\n".join(lines)

    @staticmethod
    def render_json(guide: InterviewGuide) -> Dict:
        return {
            "title": guide.title,
            "type": guide.interview_type,
            "context": guide.context,
            "duration": guide.duration_minutes,
            "questions": [
                {"dimension": q.dimension, "question": q.question,
                 "priority": q.priority, "is_custom": q.is_custom}
                for q in guide.questions
            ],
            "tips": guide.tips,
        }
