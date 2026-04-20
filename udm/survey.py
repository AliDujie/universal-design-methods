"""UDM 问卷生成器

支持卡诺问卷、语义差异量表、NPS问卷、期望值测试等
多种问卷类型的自动生成。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Tuple

from .config import KANO_CATEGORIES
from .templates import (
    SURVEY_TYPES, SEMANTIC_DIFFERENTIAL_PAIRS,
    DESIRABILITY_WORDS, NPS_CATEGORIES,
)


@dataclass
class SurveyQuestion:
    """单个问卷题目"""
    question_format: str  # single_choice/multiple_choice/scale/ranking/open_ended/paired
    text: str
    options: List[str] = field(default_factory=list)
    scale_labels: Dict[int, str] = field(default_factory=dict)
    required: bool = True


@dataclass
class Survey:
    """完整问卷"""
    title: str
    survey_type: str
    description: str = ""
    target_audience: str = ""
    estimated_time: str = ""
    questions: List[SurveyQuestion] = field(default_factory=list)
    closing_text: str = "感谢您的参与！您的反馈将帮助我们改进产品。"


# ─────────────────────────────────────────────
# 卡诺分析引擎
# ─────────────────────────────────────────────

KANO_MATRIX: Dict[Tuple[str, str], str] = {
    ("like", "like"): "questionable",
    ("like", "expect"): "attractive",
    ("like", "neutral"): "attractive",
    ("like", "live_with"): "attractive",
    ("like", "dislike"): "one_dimensional",
    ("expect", "like"): "reverse",
    ("expect", "expect"): "indifferent",
    ("expect", "neutral"): "indifferent",
    ("expect", "live_with"): "indifferent",
    ("expect", "dislike"): "must_be",
    ("neutral", "like"): "reverse",
    ("neutral", "expect"): "indifferent",
    ("neutral", "neutral"): "indifferent",
    ("neutral", "live_with"): "indifferent",
    ("neutral", "dislike"): "must_be",
    ("live_with", "like"): "reverse",
    ("live_with", "expect"): "indifferent",
    ("live_with", "neutral"): "indifferent",
    ("live_with", "live_with"): "indifferent",
    ("live_with", "dislike"): "must_be",
    ("dislike", "like"): "reverse",
    ("dislike", "expect"): "reverse",
    ("dislike", "neutral"): "reverse",
    ("dislike", "live_with"): "reverse",
    ("dislike", "dislike"): "questionable",
}

KANO_ANSWER_OPTIONS = ["like", "expect", "neutral", "live_with", "dislike"]
KANO_ANSWER_LABELS = {
    "like": "我喜欢这样",
    "expect": "理应如此",
    "neutral": "无所谓",
    "live_with": "勉强接受",
    "dislike": "我不喜欢这样",
}


def classify_kano(functional: str, dysfunctional: str) -> str:
    """根据功能型和反功能型回答分类需求。"""
    return KANO_MATRIX.get((functional, dysfunctional), "questionable")


def analyze_kano_results(features: Dict[str, List[Tuple[str, str]]]) -> Dict[str, Dict]:
    """批量分析卡诺问卷结果。

    Args:
        features: 功能名 -> [(functional_answer, dysfunctional_answer), ...]

    Returns:
        每个功能的分类统计和最终分类。
    """
    results = {}
    for feature, responses in features.items():
        counts: Dict[str, int] = {}
        for func, dysfunc in responses:
            cat = classify_kano(func, dysfunc)
            counts[cat] = counts.get(cat, 0) + 1
        # 最终分类取最多票数
        final = max(counts, key=lambda k: counts[k]) if counts else "indifferent"
        results[feature] = {
            "counts": counts,
            "total": len(responses),
            "classification": final,
            "label": KANO_CATEGORIES.get(final, final),
        }
    return results


# ─────────────────────────────────────────────
# NPS 计算引擎
# ─────────────────────────────────────────────

def calculate_nps(scores: List[int]) -> Dict:
    """计算NPS净推荐值。

    Args:
        scores: 0-10分的推荐意愿评分列表。

    Returns:
        包含NPS分数、各类别人数和占比的字典。
    """
    if not scores:
        return {"nps": 0, "promoters": 0, "passives": 0, "detractors": 0}
    total = len(scores)
    promoters = sum(1 for s in scores if s >= 9)
    detractors = sum(1 for s in scores if s <= 6)
    passives = total - promoters - detractors
    nps = round((promoters - detractors) / total * 100, 1)

    if nps >= 50:
        level = "优秀"
    elif nps >= 0:
        level = "良好"
    else:
        level = "需要改进"

    return {
        "nps": nps, "level": level,
        "promoters": promoters, "promoter_pct": round(promoters/total*100, 1),
        "passives": passives, "passive_pct": round(passives/total*100, 1),
        "detractors": detractors, "detractor_pct": round(detractors/total*100, 1),
        "total": total,
    }


# ─────────────────────────────────────────────
# 问卷构建器
# ─────────────────────────────────────────────

class SurveyBuilder:
    """问卷构建器

    用法::
        builder = SurveyBuilder("飞猪功能需求调研", "kano")
        builder.set_target("过去3个月使用过飞猪的用户")
        builder.set_features(["智能推荐", "价格日历", "AR看房"])
        survey = builder.build()
        print(SurveyBuilder.render_markdown(survey))
    """

    def __init__(self, title: str, survey_type: str):
        if survey_type not in SURVEY_TYPES:
            valid = ", ".join(SURVEY_TYPES.keys())
            raise ValueError(f"未知问卷类型: {survey_type}，可选: {valid}")
        self.title = title
        self.survey_type = survey_type
        self._target = ""
        self._product = ""
        self._features: List[str] = []
        self._custom_questions: List[SurveyQuestion] = []

    def set_target(self, target: str) -> "SurveyBuilder":
        self._target = target
        return self

    def set_product(self, product: str) -> "SurveyBuilder":
        self._product = product
        return self

    def set_features(self, features: List[str]) -> "SurveyBuilder":
        self._features = features
        return self

    def add_question(self, q: SurveyQuestion) -> "SurveyBuilder":
        self._custom_questions.append(q)
        return self

    def _build_kano(self) -> List[SurveyQuestion]:
        questions: List[SurveyQuestion] = []
        opts = [KANO_ANSWER_LABELS[k] for k in KANO_ANSWER_OPTIONS]
        for feat in self._features:
            questions.append(SurveyQuestion(
                question_format="single_choice",
                text=f"如果{self._product or '产品'}提供「{feat}」功能，你觉得怎样？",
                options=opts,
            ))
            questions.append(SurveyQuestion(
                question_format="single_choice",
                text=f"如果{self._product or '产品'}不提供「{feat}」功能，你觉得怎样？",
                options=opts,
            ))
        return questions

    def _build_semantic(self) -> List[SurveyQuestion]:
        questions: List[SurveyQuestion] = []
        for left, right in SEMANTIC_DIFFERENTIAL_PAIRS:
            questions.append(SurveyQuestion(
                question_format="scale",
                text=f"{left} ←→ {right}",
                scale_labels={1: left, 4: "中性", 7: right},
            ))
        return questions

    def _build_nps(self) -> List[SurveyQuestion]:
        product = self._product or "该产品"
        return [
            SurveyQuestion(
                question_format="scale",
                text=f"你有多大可能向朋友或同事推荐{product}？",
                scale_labels={0: "完全不可能", 5: "中立", 10: "极有可能"},
            ),
            SurveyQuestion(
                question_format="open_ended",
                text="请问您给出这个分数的主要原因是什么？",
                required=False,
            ),
        ]

    def _build_sus(self) -> List[SurveyQuestion]:
        from .config import SUS_QUESTIONS
        questions = []
        for q_text in SUS_QUESTIONS:
            questions.append(SurveyQuestion(
                question_format="scale", text=q_text,
                scale_labels={1: "非常不同意", 3: "中立", 5: "非常同意"},
            ))
        return questions

    def _build_desirability(self) -> List[SurveyQuestion]:
        return [
            SurveyQuestion(
                question_format="multiple_choice",
                text="请从以下词汇中选择5个最能描述你使用该产品感受的词：",
                options=DESIRABILITY_WORDS,
            ),
            SurveyQuestion(
                question_format="open_ended",
                text="请解释你为什么选择这些词？",
            ),
        ]

    def build(self) -> Survey:
        builders = {
            "kano": self._build_kano,
            "semantic_differential": self._build_semantic,
            "nps": self._build_nps,
            "sus": self._build_sus,
            "desirability": self._build_desirability,
        }
        questions = builders[self.survey_type]()
        questions.extend(self._custom_questions)
        q_count = len(questions)
        estimated = f"{max(3, q_count)}~{q_count * 2}分钟"

        return Survey(
            title=self.title, survey_type=self.survey_type,
            description=SURVEY_TYPES[self.survey_type]["description"],
            target_audience=self._target,
            estimated_time=estimated,
            questions=questions,
        )

    @staticmethod
    def render_markdown(survey: Survey) -> str:
        info = SURVEY_TYPES.get(survey.survey_type, {})
        lines = [f"# {survey.title}\n"]
        lines.append(f"**问卷类型:** {info.get('name', survey.survey_type)}")
        lines.append(f"**说明:** {survey.description}")
        if survey.target_audience:
            lines.append(f"**目标人群:** {survey.target_audience}")
        lines.append(f"**预计时长:** {survey.estimated_time}\n---\n")

        for i, q in enumerate(survey.questions, 1):
            lines.append(f"**Q{i}.** {q.text}")
            if q.options:
                for opt in q.options:
                    prefix = "- [ ]" if q.question_format == "multiple_choice" else "-"
                    lines.append(f"   {prefix} {opt}")
            if q.scale_labels:
                parts = [f"{k}={v}" for k, v in sorted(q.scale_labels.items())]
                lines.append(f"   ({' / '.join(parts)})")
            if not q.required:
                lines.append("   *（选填）*")
            lines.append("")

        lines.append("---")
        lines.append(f"\n{survey.closing_text}")
        return "\n".join(lines)
