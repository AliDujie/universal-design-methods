"""UDM 研究报告生成器

提供可用性报告、洞察报告、优先级矩阵等研究产出的
结构化生成工具。
"""

from dataclasses import dataclass, field
from typing import Dict, List

from .config import METHODS_INDEX


@dataclass
class Finding:
    """研究发现"""
    title: str
    description: str
    evidence: str = ""
    severity: int = 2  # 1-4
    category: str = ""
    recommendation: str = ""


@dataclass
class InsightReport:
    """洞察报告"""
    title: str
    project: str = ""
    methods_used: List[str] = field(default_factory=list)
    participant_count: int = 0
    duration: str = ""
    executive_summary: str = ""
    findings: List[Finding] = field(default_factory=list)
    personas_summary: str = ""
    journey_summary: str = ""
    recommendations_high: List[str] = field(default_factory=list)
    recommendations_medium: List[str] = field(default_factory=list)
    recommendations_low: List[str] = field(default_factory=list)


class ReportBuilder:
    """研究报告构建器

    用法::
        builder = ReportBuilder("酒店预订体验研究报告")
        builder.set_project("我的App")
        builder.set_summary("本次研究发现用户在预订流程中...")
        builder.add_finding("比价困难", "用户需要在多个平台间切换比价",
                           severity=3, recommendation="增加一键比价功能")
        builder.add_high_recommendation("优化搜索结果排序算法")
        report = builder.build()
        print(ReportBuilder.render_markdown(report))
    """

    def __init__(self, title: str):
        self.title = title
        self._project = ""
        self._methods: List[str] = []
        self._participants = 0
        self._duration = ""
        self._summary = ""
        self._findings: List[Finding] = []
        self._personas = ""
        self._journey = ""
        self._high: List[str] = []
        self._medium: List[str] = []
        self._low: List[str] = []

    def set_project(self, project: str) -> "ReportBuilder":
        self._project = project
        return self

    def add_method(self, method: str) -> "ReportBuilder":
        self._methods.append(method)
        return self

    def set_participants(self, count: int) -> "ReportBuilder":
        self._participants = count
        return self

    def set_duration(self, duration: str) -> "ReportBuilder":
        self._duration = duration
        return self

    def set_summary(self, summary: str) -> "ReportBuilder":
        self._summary = summary
        return self

    def add_finding(self, title: str, description: str,
                    evidence: str = "", severity: int = 2,
                    category: str = "",
                    recommendation: str = "") -> "ReportBuilder":
        self._findings.append(Finding(
            title=title, description=description, evidence=evidence,
            severity=severity, category=category,
            recommendation=recommendation))
        return self

    def set_personas_summary(self, s: str) -> "ReportBuilder":
        self._personas = s
        return self

    def set_journey_summary(self, s: str) -> "ReportBuilder":
        self._journey = s
        return self

    def add_high_recommendation(self, r: str) -> "ReportBuilder":
        self._high.append(r)
        return self

    def add_medium_recommendation(self, r: str) -> "ReportBuilder":
        self._medium.append(r)
        return self

    def add_low_recommendation(self, r: str) -> "ReportBuilder":
        self._low.append(r)
        return self

    def build(self) -> InsightReport:
        return InsightReport(
            title=self.title, project=self._project,
            methods_used=self._methods,
            participant_count=self._participants,
            duration=self._duration,
            executive_summary=self._summary,
            findings=self._findings,
            personas_summary=self._personas,
            journey_summary=self._journey,
            recommendations_high=self._high,
            recommendations_medium=self._medium,
            recommendations_low=self._low)

    @staticmethod
    def render_markdown(report: InsightReport) -> str:
        lines = [f"# {report.title}\n"]

        # 执行摘要
        if report.executive_summary:
            lines.append("## 执行摘要\n")
            lines.append(report.executive_summary)
            lines.append("")

        # 研究概述
        lines.append("## 研究概述\n")
        if report.project:
            lines.append(f"- **项目:** {report.project}")
        if report.methods_used:
            lines.append(f"- **研究方法:** {', '.join(report.methods_used)}")
        if report.participant_count:
            lines.append(f"- **参与人数:** {report.participant_count}")
        if report.duration:
            lines.append(f"- **研究周期:** {report.duration}")
        lines.append("")

        # 关键发现
        if report.findings:
            lines.append("## 关键发现\n")
            sev_labels = {4: "🔴 严重", 3: "🟠 重要", 2: "🟡 中等", 1: "🟢 轻微"}
            sorted_findings = sorted(report.findings,
                                     key=lambda f: f.severity, reverse=True)
            for i, f in enumerate(sorted_findings, 1):
                sev = sev_labels.get(f.severity, "")
                lines.append(f"### {i}. {f.title} {sev}\n")
                lines.append(f"{f.description}\n")
                if f.evidence:
                    lines.append(f"**证据:** {f.evidence}\n")
                if f.recommendation:
                    lines.append(f"**建议:** {f.recommendation}\n")

        # 设计建议
        lines.append("## 设计建议\n")
        if report.recommendations_high:
            lines.append("### 🔴 优先级高（立即行动）\n")
            for r in report.recommendations_high:
                lines.append(f"1. {r}")
            lines.append("")
        if report.recommendations_medium:
            lines.append("### 🟡 优先级中（计划执行）\n")
            for r in report.recommendations_medium:
                lines.append(f"1. {r}")
            lines.append("")
        if report.recommendations_low:
            lines.append("### 🟢 优先级低（持续关注）\n")
            for r in report.recommendations_low:
                lines.append(f"1. {r}")

        return "\n".join(lines)

    @staticmethod
    def render_json(report: InsightReport) -> Dict:
        return {
            "title": report.title,
            "project": report.project,
            "methods": report.methods_used,
            "participants": report.participant_count,
            "findings": [
                {"title": f.title, "description": f.description,
                 "severity": f.severity, "recommendation": f.recommendation}
                for f in report.findings
            ],
            "recommendations": {
                "high": report.recommendations_high,
                "medium": report.recommendations_medium,
                "low": report.recommendations_low,
            },
        }
