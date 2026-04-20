"""UDM Skill 工具函数模块

提供知识库加载、方法搜索、方法筛选、格式化输出等通用工具。
"""

from typing import Dict, List, Optional
from .config import KNOWLEDGE_BASE_DIR, KNOWLEDGE_FILES, METHODS_INDEX, DESIGN_PHASES


def load_knowledge(topic: str) -> str:
    """加载指定主题的知识库内容。

    Args:
        topic: 主题标识符，对应 config.KNOWLEDGE_FILES 的键。
               可选值: exploration, generative, evaluative, synthesis,
               communication, templates, decision

    Returns:
        知识库文件的完整文本内容。

    Raises:
        KeyError: 当 topic 不在已知主题列表中时。
        FileNotFoundError: 当知识库文件不存在时。
    """
    if topic not in KNOWLEDGE_FILES:
        available = ", ".join(sorted(KNOWLEDGE_FILES.keys()))
        raise KeyError(f"未知主题 '{topic}'，可选主题: {available}")

    file_path = KNOWLEDGE_BASE_DIR / KNOWLEDGE_FILES[topic]
    if not file_path.exists():
        raise FileNotFoundError(f"知识库文件不存在: {file_path}")

    return file_path.read_text(encoding="utf-8")


def load_all_knowledge() -> Dict[str, str]:
    """加载全部知识库内容。

    Returns:
        字典，键为主题标识符，值为对应文件内容。
    """
    result: Dict[str, str] = {}
    for topic in KNOWLEDGE_FILES:
        try:
            result[topic] = load_knowledge(topic)
        except FileNotFoundError:
            result[topic] = ""
    return result


def search_knowledge(keyword: str, topics: Optional[List[str]] = None) -> Dict[str, List[str]]:
    """在知识库中搜索包含关键词的段落。

    Args:
        keyword: 搜索关键词（大小写不敏感）。
        topics: 限定搜索的主题列表，为 None 时搜索全部。

    Returns:
        字典，键为主题标识符，值为包含关键词的段落列表。
    """
    search_topics = topics if topics else list(KNOWLEDGE_FILES.keys())
    results: Dict[str, List[str]] = {}

    for topic in search_topics:
        try:
            content = load_knowledge(topic)
        except (KeyError, FileNotFoundError):
            continue

        paragraphs = content.split("\n\n")
        matched = [p.strip() for p in paragraphs if keyword.lower() in p.lower()]
        if matched:
            results[topic] = matched

    return results


def get_method(method_id: int) -> Optional[Dict]:
    """根据ID获取方法详情。

    Args:
        method_id: 方法编号(1-100)。

    Returns:
        方法信息字典，包含 name, en, cat, phases, purpose, data 字段。
    """
    return METHODS_INDEX.get(method_id)


def find_method_by_name(name: str) -> Optional[Dict]:
    """根据中文名或英文名模糊查找方法。

    Args:
        name: 方法名称（中文或英文，大小写不敏感）。

    Returns:
        匹配的方法信息字典（含 id 字段），未找到返回 None。
    """
    name_lower = name.lower()
    for mid, info in METHODS_INDEX.items():
        if name_lower in info["name"].lower() or name_lower in info["en"].lower():
            return {**info, "id": mid}
    return None


def search_methods(keyword: str) -> List[Dict]:
    """根据关键词搜索方法（匹配名称）。

    Args:
        keyword: 搜索关键词。

    Returns:
        匹配的方法列表，每个元素含 id 字段。
    """
    keyword_lower = keyword.lower()
    results = []
    for mid, info in METHODS_INDEX.items():
        if (keyword_lower in info["name"].lower()
                or keyword_lower in info["en"].lower()):
            results.append({**info, "id": mid})
    return results


def filter_methods(
    phases: Optional[List[int]] = None,
    purpose: Optional[str] = None,
    data_type: Optional[str] = None,
    category: Optional[str] = None,
) -> List[Dict]:
    """按条件筛选方法。

    Args:
        phases: 设计阶段列表(1-5)，方法需覆盖其中至少一个阶段。
        purpose: 方法目的 (exploration/generative/evaluative/synthesis)。
        data_type: 数据类型 (quantitative/qualitative/mixed)。
        category: 方法分类 (exploration/generative/evaluative/synthesis/communication)。

    Returns:
        符合条件的方法列表，每个元素含 id 字段。
    """
    results = []
    for mid, info in METHODS_INDEX.items():
        if phases:
            if not any(p in info["phases"] for p in phases):
                continue
        if purpose and info["purpose"] != purpose:
            continue
        if data_type and info["data"] != data_type:
            continue
        if category and info["cat"] != category:
            continue
        results.append({**info, "id": mid})
    return results


def get_methods_for_phase(phase: int) -> List[Dict]:
    """获取指定设计阶段可用的所有方法。

    Args:
        phase: 设计阶段编号(1-5)。

    Returns:
        该阶段可用的方法列表。
    """
    if phase not in range(1, 6):
        raise ValueError(f"未知阶段: {phase}，应在1-5之间")
    return filter_methods(phases=[phase])


def get_phase_info(phase: int) -> Dict[str, str]:
    """获取设计阶段的详细信息。

    Args:
        phase: 阶段编号(1-5)。

    Returns:
        包含 name, en, goal 的字典。
    """
    if phase not in DESIGN_PHASES:
        raise ValueError(f"未知阶段: {phase}，应在1-5之间")
    return DESIGN_PHASES[phase]


def recommend_methods(
    goal: str,
    phases: Optional[List[int]] = None,
    max_results: int = 5,
    require_triangulation: bool = True,
) -> List[Dict]:
    """根据研究目标智能推荐方法组合。

    基于三角测量原则，推荐至少包含定性+定量的方法组合。

    Args:
        goal: 研究目标描述。
        phases: 限定设计阶段。
        max_results: 最大推荐数量。
        require_triangulation: 是否要求三角测量（混合定性+定量）。

    Returns:
        推荐的方法列表。
    """
    # 基于目标关键词匹配方法
    goal_lower = goal.lower()
    scored: List[tuple] = []

    # 目标关键词到方法目的的映射
    goal_purpose_map = {
        "探索": "exploration", "了解": "exploration", "发现": "exploration",
        "理解": "exploration", "调研": "exploration",
        "创意": "generative", "设计": "generative", "创新": "generative",
        "原型": "generative", "概念": "generative",
        "评估": "evaluative", "测试": "evaluative", "验证": "evaluative",
        "优化": "evaluative", "改进": "evaluative",
        "分析": "synthesis", "综合": "synthesis", "整理": "synthesis",
        "归纳": "synthesis",
    }

    inferred_purpose = None
    for kw, purp in goal_purpose_map.items():
        if kw in goal_lower:
            inferred_purpose = purp
            break

    candidates = filter_methods(phases=phases, purpose=inferred_purpose)
    if not candidates:
        candidates = filter_methods(phases=phases)

    # 评分：名称匹配+阶段覆盖度
    for m in candidates:
        score = 0
        if any(kw in m["name"] for kw in goal_lower):
            score += 3
        if any(kw in m["en"].lower() for kw in goal_lower.split()):
            score += 2
        score += len(m["phases"])  # 阶段覆盖度加分
        scored.append((score, m))

    scored.sort(key=lambda x: x[0], reverse=True)
    results = [m for _, m in scored[:max_results * 2]]

    if require_triangulation and len(results) >= 2:
        # 确保包含不同数据类型
        has_qual = any(m["data"] == "qualitative" for m in results)
        has_quant = any(m["data"] == "quantitative" for m in results)
        if not has_qual:
            qual = [m for m in filter_methods(phases=phases) if m["data"] == "qualitative"]
            if qual:
                results.insert(1, qual[0])
        if not has_quant:
            quant = [m for m in filter_methods(phases=phases) if m["data"] == "quantitative"]
            if quant:
                results.insert(2, quant[0])

    return results[:max_results]


def extract_sections(content: str, level: int = 2) -> Dict[str, str]:
    """从 Markdown 文本中按标题级别提取章节。

    Args:
        content: Markdown 文本内容。
        level: 标题级别（2 表示 ##，3 表示 ###）。

    Returns:
        字典，键为标题文本，值为该章节的正文内容。
    """
    prefix = "#" * level + " "
    sections: Dict[str, str] = {}
    current_title: Optional[str] = None
    current_lines: List[str] = []

    for line in content.split("\n"):
        if line.startswith(prefix):
            if current_title is not None:
                sections[current_title] = "\n".join(current_lines).strip()
            current_title = line[len(prefix):].strip()
            current_lines = []
        elif current_title is not None:
            current_lines.append(line)

    if current_title is not None:
        sections[current_title] = "\n".join(current_lines).strip()

    return sections


def format_method_card(method: Dict) -> str:
    """将方法信息格式化为Markdown卡片。

    Args:
        method: 方法信息字典（含 id, name, en, cat, phases, purpose, data）。

    Returns:
        格式化的Markdown字符串。
    """
    mid = method.get("id", "?")
    phases_str = ", ".join(
        DESIGN_PHASES[p]["name"] for p in method["phases"] if p in DESIGN_PHASES
    )
    data_labels = {"quantitative": "定量", "qualitative": "定性", "mixed": "混合"}
    purpose_labels = {
        "exploration": "探索性", "generative": "衍生性",
        "evaluative": "评估性", "synthesis": "综合性",
    }

    lines = [
        f"### #{mid} {method['name']} ({method['en']})",
        f"- **类型:** {purpose_labels.get(method['purpose'], method['purpose'])}",
        f"- **数据:** {data_labels.get(method['data'], method['data'])}",
        f"- **适用阶段:** {phases_str}",
    ]
    return "\n".join(lines)


def format_methods_table(methods: List[Dict]) -> str:
    """将方法列表格式化为Markdown表格。

    Args:
        methods: 方法信息列表。

    Returns:
        格式化的Markdown表格字符串。
    """
    data_labels = {"quantitative": "定量", "qualitative": "定性", "mixed": "混合"}
    purpose_labels = {
        "exploration": "探索", "generative": "衍生",
        "evaluative": "评估", "synthesis": "综合",
    }

    lines = ["| # | 方法名称 | 英文名 | 类型 | 数据 | 适用阶段 |"]
    lines.append("|---|---------|--------|------|------|---------|")
    for m in methods:
        mid = m.get("id", "?")
        phases = ",".join(str(p) for p in m["phases"])
        lines.append(
            f"| {mid} | {m['name']} | {m['en']} "
            f"| {purpose_labels.get(m['purpose'], m['purpose'])} "
            f"| {data_labels.get(m['data'], m['data'])} "
            f"| {phases} |"
        )
    return "\n".join(lines)
