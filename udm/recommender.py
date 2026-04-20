"""UDM 方法推荐引擎

根据项目阶段、研究目标、资源约束等条件智能推荐方法组合，
遵循三角测量原则确保研究严谨性。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .config import METHODS_INDEX, DESIGN_PHASES


GOAL_METHOD_MAP: Dict[str, List[int]] = {
    "了解用户需求": [20, 48, 30, 27, 59, 52],
    "探索用户行为": [57, 42, 76, 6, 59, 27],
    "评估可用性": [94, 46, 87, 13, 68, 93],
    "测试原型": [66, 36, 94, 99, 29, 87],
    "信息架构": [10, 16, 55, 84, 3, 49],
    "竞品分析": [15, 96, 4, 53, 74, 11],
    "用户画像": [63, 95, 48, 30, 20, 27],
    "创意发散": [8, 7, 45, 21, 14, 47],
    "数据驱动": [1, 97, 40, 5, 78, 51],
    "情感体验": [24, 54, 29, 75, 37, 64],
    "协同设计": [28, 61, 60, 26, 65, 71],
    "快速验证": [68, 79, 99, 1, 67, 83],
}

RESOURCE_LEVELS = {
    "minimal": {"max_methods": 2, "max_participants": 5, "max_days": 3,
                "label": "最小资源（1-2种方法，3天内）"},
    "moderate": {"max_methods": 4, "max_participants": 15, "max_days": 14,
                 "label": "中等资源（3-4种方法，2周内）"},
    "extensive": {"max_methods": 8, "max_participants": 50, "max_days": 60,
                  "label": "充足资源（5-8种方法，2个月内）"},
}


@dataclass
class MethodRecommendation:
    """单个方法推荐"""
    method_id: int
    name: str
    en: str
    reason: str
    priority: int = 1  # 1=核心, 2=推荐, 3=可选
    data_type: str = ""
    estimated_days: int = 1


@dataclass
class ResearchPlan:
    """推荐的研究计划"""
    goal: str
    phase: int
    resource_level: str
    recommendations: List[MethodRecommendation] = field(default_factory=list)
    triangulation_note: str = ""
    sequence_note: str = ""


class MethodRecommender:
    """方法推荐引擎

    用法::
        rec = MethodRecommender()
        plan = rec.recommend(
            goal="了解用户需求",
            phase=1,
            resource_level="moderate"
        )
        print(MethodRecommender.render_markdown(plan))
    """

    def __init__(self):
        pass

    def recommend(self, goal: str, phase: int = 0,
                  resource_level: str = "moderate",
                  data_preference: str = "") -> ResearchPlan:
        if resource_level not in RESOURCE_LEVELS:
            raise ValueError(f"未知资源级别: {resource_level}")

        res = RESOURCE_LEVELS[resource_level]
        max_methods = res["max_methods"]

        # 1. 从目标映射获取候选方法
        candidate_ids: List[int] = []
        for key, ids in GOAL_METHOD_MAP.items():
            if key in goal or goal in key:
                candidate_ids = ids
                break

        # 若无精确匹配，用关键词模糊匹配
        if not candidate_ids:
            goal_lower = goal.lower()
            for mid, info in METHODS_INDEX.items():
                if (any(kw in info["name"] for kw in goal_lower) or
                        any(kw in info["en"].lower() for kw in goal_lower.split())):
                    candidate_ids.append(mid)

        # 若仍无结果，按阶段推荐
        if not candidate_ids:
            target_phase = phase if phase else 1
            candidate_ids = [
                mid for mid, info in METHODS_INDEX.items()
                if target_phase in info["phases"]
            ]

        # 2. 按阶段过滤
        if phase:
            filtered = [mid for mid in candidate_ids
                        if phase in METHODS_INDEX.get(mid, {}).get("phases", [])]
            if filtered:
                candidate_ids = filtered

        # 3. 数据偏好过滤
        if data_preference:
            filtered = [mid for mid in candidate_ids
                        if METHODS_INDEX.get(mid, {}).get("data") == data_preference]
            if filtered:
                candidate_ids = filtered

        # 4. 截取并构建推荐
        candidate_ids = candidate_ids[:max_methods * 2]
        recommendations: List[MethodRecommendation] = []
        has_qual = False
        has_quant = False

        for i, mid in enumerate(candidate_ids[:max_methods]):
            info = METHODS_INDEX.get(mid, {})
            if not info:
                continue
            priority = 1 if i < 2 else (2 if i < 4 else 3)
            rec = MethodRecommendation(
                method_id=mid, name=info["name"], en=info["en"],
                reason=self._generate_reason(info, goal),
                priority=priority, data_type=info.get("data", ""),
            )
            recommendations.append(rec)
            if info.get("data") == "qualitative":
                has_qual = True
            if info.get("data") == "quantitative":
                has_quant = True

        # 5. 三角测量补充
        tri_note = ""
        if recommendations and not (has_qual and has_quant):
            missing = "quantitative" if not has_quant else "qualitative"
            label = "定量" if missing == "quantitative" else "定性"
            supplement = [
                mid for mid, info in METHODS_INDEX.items()
                if info["data"] == missing and mid not in candidate_ids
            ]
            if supplement and len(recommendations) < max_methods:
                sup_info = METHODS_INDEX[supplement[0]]
                recommendations.append(MethodRecommendation(
                    method_id=supplement[0], name=sup_info["name"],
                    en=sup_info["en"],
                    reason=f"三角测量补充：提供{label}数据视角",
                    priority=2, data_type=missing,
                ))
            tri_note = f"已补充{label}方法以满足三角测量原则"
        elif has_qual and has_quant:
            tri_note = "方法组合已满足三角测量原则（含定性+定量）"

        return ResearchPlan(
            goal=goal, phase=phase, resource_level=resource_level,
            recommendations=recommendations,
            triangulation_note=tri_note,
            sequence_note=self._suggest_sequence(recommendations),
        )

    def _generate_reason(self, info: Dict, goal: str) -> str:
        purpose_map = {
            "exploration": "探索性研究，帮助发现未知需求",
            "generative": "衍生性方法，激发创意和新概念",
            "evaluative": "评估性方法，验证设计方案有效性",
            "synthesis": "综合分析，整合多源数据形成洞察",
        }
        return purpose_map.get(info.get("purpose", ""), f"适用于{goal}场景")

    def _suggest_sequence(self, recs: List[MethodRecommendation]) -> str:
        if not recs:
            return ""
        purpose_order = {"exploration": 1, "generative": 2,
                         "evaluative": 3, "synthesis": 4}
        sorted_recs = sorted(recs, key=lambda r: purpose_order.get(
            METHODS_INDEX.get(r.method_id, {}).get("purpose", ""), 5))
        names = [r.name for r in sorted_recs]
        return "建议执行顺序: " + " → ".join(names)

    @staticmethod
    def render_markdown(plan: ResearchPlan) -> str:
        res_info = RESOURCE_LEVELS.get(plan.resource_level, {})
        lines = [f"# 方法推荐方案\n"]
        lines.append(f"**研究目标:** {plan.goal}")
        if plan.phase:
            phase_info = DESIGN_PHASES.get(plan.phase, {})
            lines.append(f"**设计阶段:** {phase_info.get('name', '')} ({phase_info.get('en', '')})")
        lines.append(f"**资源级别:** {res_info.get('label', plan.resource_level)}")
        if plan.triangulation_note:
            lines.append(f"**三角测量:** {plan.triangulation_note}")
        lines.append("")

        priority_labels = {1: "🔴 核心", 2: "🟡 推荐", 3: "🟢 可选"}
        data_labels = {"quantitative": "定量", "qualitative": "定性", "mixed": "混合"}

        for rec in plan.recommendations:
            p_label = priority_labels.get(rec.priority, "")
            d_label = data_labels.get(rec.data_type, "")
            lines.append(f"## {p_label} #{rec.method_id} {rec.name} ({rec.en})\n")
            lines.append(f"- **数据类型:** {d_label}")
            lines.append(f"- **推荐理由:** {rec.reason}")
            lines.append("")

        if plan.sequence_note:
            lines.append(f"---\n📋 {plan.sequence_note}")
        return "\n".join(lines)
