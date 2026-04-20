"""UDM 可用性测试引擎

提供可用性测试脚本生成、SUS评分计算、启发性评估、
严重性评级、可用性报告生成等完整工具。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .config import NIELSEN_HEURISTICS, SUS_QUESTIONS
from .templates import (
    USABILITY_TEST_TYPES, TASK_DIFFICULTY_SCALE,
    SEVERITY_RATINGS, USABILITY_METRICS,
)


@dataclass
class TestTask:
    """可用性测试任务"""
    task_id: int
    description: str
    scenario: str = ""
    success_criteria: str = ""
    max_time_seconds: int = 300
    difficulty: int = 3


@dataclass
class TaskResult:
    """单个任务的测试结果"""
    task_id: int
    participant_id: str
    completed: bool = False
    time_seconds: float = 0
    errors: int = 0
    assists: int = 0
    satisfaction: int = 3
    notes: str = ""


@dataclass
class HeuristicIssue:
    """启发性评估发现的问题"""
    heuristic_id: int
    location: str
    description: str
    severity: int = 2
    recommendation: str = ""
    screenshot_ref: str = ""


@dataclass
class UsabilityTestPlan:
    """可用性测试计划"""
    title: str
    test_type: str
    product: str = ""
    objectives: List[str] = field(default_factory=list)
    tasks: List[TestTask] = field(default_factory=list)
    participant_criteria: str = ""
    participant_count: int = 5
    facilitator_script: str = ""


@dataclass
class UsabilityReport:
    """可用性测试报告"""
    title: str
    test_type: str
    product: str = ""
    participant_count: int = 0
    tasks: List[TestTask] = field(default_factory=list)
    results: List[TaskResult] = field(default_factory=list)
    heuristic_issues: List[HeuristicIssue] = field(default_factory=list)
    sus_scores: List[float] = field(default_factory=list)
    key_findings: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)


# ─────────────────────────────────────────────
# SUS 计算引擎
# ─────────────────────────────────────────────

def calculate_sus(responses: List[int]) -> float:
    """计算SUS（系统可用性量表）得分。

    Args:
        responses: 10个问题的评分列表，每个1-5分。

    Returns:
        SUS总分(0-100)。

    Raises:
        ValueError: 当响应数量不为10或分数超范围时。
    """
    if len(responses) != 10:
        raise ValueError(f"SUS需要10个回答，收到{len(responses)}个")
    for i, r in enumerate(responses):
        if not 1 <= r <= 5:
            raise ValueError(f"第{i+1}题评分{r}超出1-5范围")

    total = 0
    for i, r in enumerate(responses):
        if i % 2 == 0:  # 奇数题(正向): 得分 = 原始分 - 1
            total += r - 1
        else:  # 偶数题(反向): 得分 = 5 - 原始分
            total += 5 - r
    return total * 2.5


def interpret_sus(score: float) -> Dict[str, str]:
    """解读SUS得分。"""
    if score >= 80.3:
        grade, adj, desc = "A", "优秀", "用户体验优秀，超越大多数产品"
    elif score >= 68:
        grade, adj, desc = "B", "良好", "用户体验良好，高于平均水平"
    elif score >= 51:
        grade, adj, desc = "C", "一般", "用户体验一般，有改进空间"
    elif score >= 25:
        grade, adj, desc = "D", "较差", "用户体验较差，需要重大改进"
    else:
        grade, adj, desc = "F", "极差", "用户体验极差，需要彻底重新设计"
    return {"score": f"{score:.1f}", "grade": grade,
            "adjective": adj, "description": desc}


def calculate_sus_batch(all_responses: List[List[int]]) -> Dict:
    """批量计算多个参与者的SUS得分。"""
    scores = [calculate_sus(r) for r in all_responses]
    avg = sum(scores) / len(scores) if scores else 0
    return {
        "individual_scores": scores,
        "average": round(avg, 1),
        "min": min(scores) if scores else 0,
        "max": max(scores) if scores else 0,
        "interpretation": interpret_sus(avg),
        "count": len(scores),
    }


# ─────────────────────────────────────────────
# 任务完成率计算
# ─────────────────────────────────────────────

def calculate_task_metrics(results: List[TaskResult]) -> Dict:
    """计算任务级别的可用性指标。"""
    if not results:
        return {}
    total = len(results)
    completed = sum(1 for r in results if r.completed)
    times = [r.time_seconds for r in results if r.completed]
    errors = [r.errors for r in results]
    sats = [r.satisfaction for r in results]

    return {
        "completion_rate": round(completed / total * 100, 1),
        "avg_time": round(sum(times) / len(times), 1) if times else 0,
        "avg_errors": round(sum(errors) / total, 1),
        "avg_satisfaction": round(sum(sats) / total, 1),
        "total_participants": total,
    }


# ─────────────────────────────────────────────
# 启发性评估引擎
# ─────────────────────────────────────────────

class HeuristicEvaluator:
    """尼尔森十大启发性评估工具

    用法::
        evaluator = HeuristicEvaluator("飞猪App首页")
        evaluator.add_issue(1, "首页", "加载状态无反馈", severity=3,
                           recommendation="添加骨架屏或加载动画")
        evaluator.add_issue(4, "搜索结果", "筛选标签样式不一致", severity=2)
        report = evaluator.render_markdown()
    """

    def __init__(self, product: str):
        self.product = product
        self.issues: List[HeuristicIssue] = []

    def add_issue(self, heuristic_id: int, location: str,
                  description: str, severity: int = 2,
                  recommendation: str = "") -> HeuristicIssue:
        if not 1 <= heuristic_id <= 10:
            raise ValueError(f"启发性原则编号应在1-10之间，收到: {heuristic_id}")
        if severity not in SEVERITY_RATINGS:
            raise ValueError(f"严重性应在0-4之间，收到: {severity}")
        issue = HeuristicIssue(
            heuristic_id=heuristic_id, location=location,
            description=description, severity=severity,
            recommendation=recommendation,
        )
        self.issues.append(issue)
        return issue

    def get_by_severity(self, min_severity: int = 3) -> List[HeuristicIssue]:
        return [i for i in self.issues if i.severity >= min_severity]

    def get_by_heuristic(self, heuristic_id: int) -> List[HeuristicIssue]:
        return [i for i in self.issues if i.heuristic_id == heuristic_id]

    def severity_summary(self) -> Dict[int, int]:
        summary: Dict[int, int] = {s: 0 for s in SEVERITY_RATINGS}
        for issue in self.issues:
            summary[issue.severity] = summary.get(issue.severity, 0) + 1
        return summary

    def render_markdown(self) -> str:
        lines = [f"# 启发性评估报告 — {self.product}\n"]
        summary = self.severity_summary()
        lines.append("## 问题概览\n")
        lines.append(f"- **总问题数:** {len(self.issues)}")
        for sev, count in sorted(summary.items(), reverse=True):
            if count > 0:
                lines.append(f"- **{SEVERITY_RATINGS[sev]}:** {count}个")
        lines.append("")

        # 按严重性分组
        for sev in sorted(SEVERITY_RATINGS.keys(), reverse=True):
            issues = [i for i in self.issues if i.severity == sev]
            if not issues:
                continue
            lines.append(f"## {SEVERITY_RATINGS[sev]} (共{len(issues)}个)\n")
            for issue in issues:
                h_name = NIELSEN_HEURISTICS[issue.heuristic_id - 1]
                lines.append(f"### [{h_name}] {issue.location}\n")
                lines.append(f"**问题:** {issue.description}\n")
                if issue.recommendation:
                    lines.append(f"**建议:** {issue.recommendation}\n")
        return "\n".join(lines)

    def render_checklist(self) -> str:
        """生成空白启发性评估检查清单。"""
        lines = [f"# 启发性评估检查清单 — {self.product}\n"]
        for i, h in enumerate(NIELSEN_HEURISTICS, 1):
            lines.append(f"## {i}. {h}\n")
            lines.append("- [ ] 是否符合该原则？")
            lines.append("- 问题描述: ")
            lines.append("- 严重性(0-4): ")
            lines.append("- 位置: ")
            lines.append("- 建议: \n")
        return "\n".join(lines)


# ─────────────────────────────────────────────
# 测试脚本生成器
# ─────────────────────────────────────────────

class UsabilityTestBuilder:
    """可用性测试计划构建器

    用法::
        builder = UsabilityTestBuilder("飞猪酒店预订可用性测试", "formative")
        builder.set_product("飞猪App")
        builder.add_objective("评估酒店搜索流程的易用性")
        builder.add_task("搜索并预订一家杭州西湖附近的酒店",
                        scenario="你计划下周去杭州出差...",
                        success_criteria="成功到达订单确认页")
        plan = builder.build()
        print(UsabilityTestBuilder.render_markdown(plan))
    """

    def __init__(self, title: str, test_type: str = "formative"):
        if test_type not in USABILITY_TEST_TYPES:
            valid = ", ".join(USABILITY_TEST_TYPES.keys())
            raise ValueError(f"未知测试类型: {test_type}，可选: {valid}")
        self.title = title
        self.test_type = test_type
        self._product = ""
        self._objectives: List[str] = []
        self._tasks: List[TestTask] = []
        self._participant_criteria = ""
        self._participant_count = int(
            USABILITY_TEST_TYPES[test_type].get("participants", "5").split("-")[0]
        )
        self._task_counter = 0

    def set_product(self, product: str) -> "UsabilityTestBuilder":
        self._product = product
        return self

    def add_objective(self, objective: str) -> "UsabilityTestBuilder":
        self._objectives.append(objective)
        return self

    def set_participant_criteria(self, criteria: str) -> "UsabilityTestBuilder":
        self._participant_criteria = criteria
        return self

    def set_participant_count(self, count: int) -> "UsabilityTestBuilder":
        self._participant_count = count
        return self

    def add_task(self, description: str, scenario: str = "",
                 success_criteria: str = "", max_time: int = 300,
                 difficulty: int = 3) -> "UsabilityTestBuilder":
        self._task_counter += 1
        self._tasks.append(TestTask(
            task_id=self._task_counter, description=description,
            scenario=scenario, success_criteria=success_criteria,
            max_time_seconds=max_time, difficulty=difficulty,
        ))
        return self

    def build(self) -> UsabilityTestPlan:
        return UsabilityTestPlan(
            title=self.title, test_type=self.test_type,
            product=self._product, objectives=self._objectives,
            tasks=self._tasks,
            participant_criteria=self._participant_criteria,
            participant_count=self._participant_count,
        )

    @staticmethod
    def render_markdown(plan: UsabilityTestPlan) -> str:
        info = USABILITY_TEST_TYPES.get(plan.test_type, {})
        lines = [f"# {plan.title}\n"]
        lines.append(f"**测试类型:** {info.get('name', plan.test_type)}")
        lines.append(f"**产品:** {plan.product}")
        lines.append(f"**参与人数:** {plan.participant_count}")
        if plan.participant_criteria:
            lines.append(f"**参与者标准:** {plan.participant_criteria}")
        lines.append("")

        if plan.objectives:
            lines.append("## 研究目标\n")
            for i, obj in enumerate(plan.objectives, 1):
                lines.append(f"{i}. {obj}")
            lines.append("")

        lines.append("## 测试任务\n")
        for task in plan.tasks:
            diff = TASK_DIFFICULTY_SCALE.get(task.difficulty, "")
            lines.append(f"### 任务 {task.task_id}\n")
            lines.append(f"**描述:** {task.description}")
            if task.scenario:
                lines.append(f"\n**场景:** {task.scenario}")
            if task.success_criteria:
                lines.append(f"\n**成功标准:** {task.success_criteria}")
            lines.append(f"\n**最大时间:** {task.max_time_seconds}秒")
            lines.append(f"**难度:** {task.difficulty}/5 ({diff})\n")

        lines.append("## 主持人脚本\n")
        lines.append("### 开场\n")
        lines.append("感谢您参加今天的测试。我们正在测试产品，不是测试您。")
        lines.append("没有对错之分，请像平时一样操作，并尽量说出您的想法。\n")
        lines.append("### 结束\n")
        lines.append("测试结束，感谢您的参与！您的反馈对我们非常有价值。")

        return "\n".join(lines)
