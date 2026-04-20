"""UDM 观察记录生成器

支持AEIOU框架观察、行为地图、隐蔽观察、参与观察、影形等
多种观察方法的结构化记录工具。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .templates import AEIOU_FRAMEWORK, OBSERVATION_TYPES


@dataclass
class ObservationNote:
    """单条观察记录"""
    timestamp: str = ""
    category: str = ""  # A/E/I/O/U
    description: str = ""
    participant_id: str = ""
    location: str = ""
    emotion: str = ""
    photo_ref: str = ""
    insight: str = ""


@dataclass
class BehaviorMapEntry:
    """行为地图条目"""
    location: str
    behavior: str
    frequency: int = 1
    duration_minutes: float = 0
    notes: str = ""


@dataclass
class ObservationSession:
    """完整的观察会话"""
    title: str
    observation_type: str
    setting: str = ""
    date: str = ""
    duration_minutes: int = 60
    observer: str = ""
    notes: List[ObservationNote] = field(default_factory=list)
    behavior_map: List[BehaviorMapEntry] = field(default_factory=list)
    key_insights: List[str] = field(default_factory=list)
    follow_up_questions: List[str] = field(default_factory=list)


class ObservationBuilder:
    """观察记录构建器

    用法::
        builder = ObservationBuilder("咖啡店用户行为观察", "fly_on_wall")
        builder.set_setting("星巴克门店，周六下午2-4点")
        builder.add_note("14:05", "A", "用户在柜台前反复查看菜单板")
        builder.add_note("14:10", "I", "用户向店员询问推荐饮品")
        builder.add_behavior("柜台区", "查看菜单", frequency=8)
        builder.add_insight("大部分用户在菜单前停留超过30秒")
        session = builder.build()
        print(ObservationBuilder.render_markdown(session))
    """

    def __init__(self, title: str, obs_type: str = "fly_on_wall"):
        if obs_type not in OBSERVATION_TYPES:
            valid = ", ".join(OBSERVATION_TYPES.keys())
            raise ValueError(f"未知观察类型: {obs_type}，可选: {valid}")
        self.title = title
        self.obs_type = obs_type
        self._setting = ""
        self._date = ""
        self._duration = 60
        self._observer = ""
        self._notes: List[ObservationNote] = []
        self._behaviors: List[BehaviorMapEntry] = []
        self._insights: List[str] = []
        self._follow_ups: List[str] = []

    def set_setting(self, setting: str) -> "ObservationBuilder":
        self._setting = setting
        return self

    def set_date(self, date: str) -> "ObservationBuilder":
        self._date = date
        return self

    def set_duration(self, minutes: int) -> "ObservationBuilder":
        self._duration = minutes
        return self

    def set_observer(self, name: str) -> "ObservationBuilder":
        self._observer = name
        return self

    def add_note(self, timestamp: str, category: str, description: str,
                 participant_id: str = "", emotion: str = "",
                 insight: str = "") -> "ObservationBuilder":
        if category and category not in "AEIOU":
            raise ValueError(f"AEIOU分类应为A/E/I/O/U之一，收到: {category}")
        self._notes.append(ObservationNote(
            timestamp=timestamp, category=category,
            description=description, participant_id=participant_id,
            emotion=emotion, insight=insight,
        ))
        return self

    def add_behavior(self, location: str, behavior: str,
                     frequency: int = 1, duration: float = 0,
                     notes: str = "") -> "ObservationBuilder":
        self._behaviors.append(BehaviorMapEntry(
            location=location, behavior=behavior,
            frequency=frequency, duration_minutes=duration, notes=notes,
        ))
        return self

    def add_insight(self, insight: str) -> "ObservationBuilder":
        self._insights.append(insight)
        return self

    def add_follow_up(self, question: str) -> "ObservationBuilder":
        self._follow_ups.append(question)
        return self

    def build(self) -> ObservationSession:
        return ObservationSession(
            title=self.title,
            observation_type=self.obs_type,
            setting=self._setting,
            date=self._date,
            duration_minutes=self._duration,
            observer=self._observer,
            notes=self._notes,
            behavior_map=self._behaviors,
            key_insights=self._insights,
            follow_up_questions=self._follow_ups,
        )

    @staticmethod
    def render_markdown(session: ObservationSession) -> str:
        info = OBSERVATION_TYPES.get(session.observation_type, {})
        lines = [f"# {session.title}", ""]
        lines.append(f"**观察类型:** {info.get('name', session.observation_type)}")
        if session.setting:
            lines.append(f"**观察场景:** {session.setting}")
        if session.date:
            lines.append(f"**日期:** {session.date}")
        lines.append(f"**时长:** {session.duration_minutes} 分钟")
        if session.observer:
            lines.append(f"**观察者:** {session.observer}")
        lines.append("")

        # AEIOU记录
        if session.notes:
            lines.append("## 观察记录 (AEIOU)\n")
            lines.append("| 时间 | 类别 | 观察内容 | 情绪 | 洞察 |")
            lines.append("|------|------|---------|------|------|")
            for n in session.notes:
                cat_label = AEIOU_FRAMEWORK.get(n.category, {}).get("label", n.category)
                lines.append(
                    f"| {n.timestamp} | {cat_label} | {n.description} "
                    f"| {n.emotion} | {n.insight} |")
            lines.append("")

        # 行为地图
        if session.behavior_map:
            lines.append("## 行为地图\n")
            lines.append("| 位置 | 行为 | 频次 | 时长(分钟) | 备注 |")
            lines.append("|------|------|------|-----------|------|")
            for b in session.behavior_map:
                lines.append(
                    f"| {b.location} | {b.behavior} | {b.frequency} "
                    f"| {b.duration_minutes} | {b.notes} |")
            lines.append("")

        if session.key_insights:
            lines.append("## 关键洞察\n")
            for i, ins in enumerate(session.key_insights, 1):
                lines.append(f"{i}. {ins}")
            lines.append("")

        if session.follow_up_questions:
            lines.append("## 后续问题\n")
            for q in session.follow_up_questions:
                lines.append(f"- {q}")

        return "\n".join(lines)

    @staticmethod
    def generate_aeiou_template() -> str:
        """生成空白AEIOU观察模板。"""
        lines = ["# AEIOU 观察记录模板\n"]
        for key, info in AEIOU_FRAMEWORK.items():
            lines.append(f"## {key} - {info['label']}\n")
            lines.append(f"*{info['description']}*\n")
            lines.append("**观察提示:**")
            for p in info["prompts"]:
                lines.append(f"- {p}")
            lines.append("\n**记录:**\n- \n")
        return "\n".join(lines)
