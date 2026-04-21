"""UDM Skill 完整测试套件

覆盖 UDMSkill 全部 8 大执行能力，每个测试独立运行。
"""

import sys
import os

# 确保能导入 udm 包
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from udm import (
    UDMSkill,
    JourneyMapBuilder,
    ResearchPlanBuilder,
    ReportBuilder,
)


def test_recommend_methods():
    """测试能力1: 智能方法推荐"""
    skill = UDMSkill("测试产品")
    result = skill.recommend_methods("了解用户需求", phase=1)

    assert isinstance(result, str), "返回值应为字符串"
    assert len(result) > 100, "推荐结果不应为空"
    assert "方法推荐方案" in result, "应包含标题"
    assert "研究目标" in result, "应包含研究目标"
    assert "三角测量" in result, "应包含三角测量说明"
    assert "核心" in result, "应包含核心推荐方法"

    # 测试不同资源级别
    r2 = skill.recommend_methods("评估可用性", phase=4, resource_level="minimal")
    assert isinstance(r2, str) and len(r2) > 50

    r3 = skill.recommend_methods("创意发散", phase=3, resource_level="extensive")
    assert isinstance(r3, str) and len(r3) > 50

    print("✅ test_recommend_methods passed")


def test_generate_interview():
    """测试能力2: 访谈提纲生成"""
    skill = UDMSkill("测试产品")

    # 测试脉络访查
    guide = skill.generate_interview("用户访谈", "contextual", context="酒店预订体验")
    assert isinstance(guide, str), "返回值应为字符串"
    assert "用户访谈" in guide, "应包含标题"
    assert "脉络访查" in guide, "应包含访谈类型"
    assert "酒店预订体验" in guide, "应包含背景信息"
    assert "开场白" in guide, "应包含开场白"
    assert "访谈问题" in guide, "应包含问题列表"
    assert "访谈技巧" in guide, "应包含技巧提示"

    # 测试阶梯法
    guide2 = skill.generate_interview("深度访谈", "laddering", duration=45)
    assert "阶梯法" in guide2, "应包含阶梯法类型"
    assert "45" in guide2, "应包含自定义时长"

    # 测试关键事件法
    guide3 = skill.generate_interview("事件访谈", "critical_incident")
    assert isinstance(guide3, str) and len(guide3) > 100

    print("✅ test_generate_interview passed")


def test_generate_observation():
    """测试能力3: 观察记录与行为分析"""
    skill = UDMSkill("测试产品")

    # 测试影形观察
    obs = skill.generate_observation("门店观察", "shadowing", setting="旅行社门店")
    assert isinstance(obs, str), "返回值应为字符串"
    assert "门店观察" in obs, "应包含标题"
    assert "影形" in obs, "应包含观察类型"
    assert "旅行社门店" in obs, "应包含场景信息"

    # 测试隐蔽观察
    obs2 = skill.generate_observation("用户行为观察", "fly_on_wall")
    assert "隐蔽观察" in obs2

    # 测试 AEIOU 模板
    tpl = skill.generate_aeiou_template()
    assert "AEIOU" in tpl, "应包含AEIOU标题"
    assert "活动" in tpl, "应包含Activities"
    assert "环境" in tpl, "应包含Environments"
    assert "交互" in tpl, "应包含Interactions"
    assert "物品" in tpl, "应包含Objects"
    assert "用户" in tpl, "应包含Users"

    print("✅ test_generate_observation passed")


def test_generate_usability_test():
    """测试能力4: 可用性测试与评估"""
    skill = UDMSkill("测试App")

    # 测试计划生成
    test = skill.generate_usability_test("预订流程测试", "formative")
    assert isinstance(test, str), "返回值应为字符串"
    assert "预订流程测试" in test, "应包含标题"
    assert "形成性测试" in test, "应包含测试类型"
    assert "测试App" in test, "应包含产品名"

    # 测试启发性评估检查清单
    cl = skill.generate_heuristic_checklist()
    assert "启发性评估" in cl, "应包含标题"
    assert "系统状态可见性" in cl, "应包含尼尔森第1条"
    assert "帮助和文档" in cl, "应包含尼尔森第10条"

    # 测试 SUS 计算
    sus = skill.calculate_sus([4, 2, 5, 1, 4, 2, 5, 1, 4, 2])
    assert sus["grade"] == "A", f"SUS应为A级，实际: {sus['grade']}"
    assert sus["score"] == "85.0", f"SUS应为85.0，实际: {sus['score']}"

    sus_low = skill.calculate_sus([2, 4, 2, 4, 2, 4, 2, 4, 2, 4])
    assert sus_low["grade"] in ("D", "F"), "低分SUS应为D或F级"

    # 测试 SUS 批量计算
    batch = skill.calculate_sus_batch([
        [4, 2, 5, 1, 4, 2, 5, 1, 4, 2],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    ])
    assert batch["count"] == 2, "批量计算应包含2个结果"
    assert batch["average"] > 0, "平均分应大于0"

    # 测试 NPS 计算
    nps = skill.calculate_nps([9, 10, 8, 7, 10, 6, 9, 8, 10, 5])
    assert nps["nps"] == 30.0, f"NPS应为30.0，实际: {nps['nps']}"
    assert nps["promoters"] == 5
    assert nps["detractors"] == 2

    print("✅ test_generate_usability_test passed")


def test_generate_survey():
    """测试能力5: 问卷与量表设计"""
    skill = UDMSkill("测试产品")

    # 卡诺问卷
    kano = skill.generate_survey("需求调研", "kano", features=["智能推荐", "价格日历"])
    assert "卡诺问卷" in kano, "应包含问卷类型"
    assert "智能推荐" in kano, "应包含功能名"
    assert "价格日历" in kano, "应包含功能名"
    assert "我喜欢这样" in kano, "应包含卡诺选项"

    # NPS 问卷
    nps_s = skill.generate_survey("满意度", "nps")
    assert "NPS" in nps_s, "应包含NPS类型"
    assert "推荐" in nps_s, "应包含推荐关键词"

    # 语义差异量表
    sd = skill.generate_survey("品牌感知", "semantic_differential")
    assert "语义差异" in sd

    # SUS 问卷
    sus_s = skill.generate_survey("可用性评估", "sus")
    assert "SUS" in sus_s or "可用性" in sus_s

    # 卡诺分析计算
    from udm import analyze_kano_results
    results = analyze_kano_results({
        "功能A": [("like", "neutral"), ("like", "dislike")],
        "功能B": [("expect", "dislike"), ("expect", "dislike")],
    })
    assert results["功能A"]["classification"] == "attractive"
    assert results["功能B"]["classification"] == "must_be"

    print("✅ test_generate_survey passed")


def test_build_journey_map():
    """测试能力6: 综合分析（体验历程图+角色画像+加权矩阵+Elito+亲和图）"""
    skill = UDMSkill("测试产品")

    # 体验历程图
    jm = skill.build_journey_map("预订体验", persona="用户小李")
    jm.add_stage("搜索", actions=["打开App"], emotions=4,
                 pain_points=["排序差"], opportunities=["智能排序"])
    jm.add_stage("比价", actions=["切换App"], emotions=2,
                 pain_points=["太耗时"])
    jm.add_stage("入住", actions=["到达酒店"], emotions=5)
    journey = jm.build()
    md = JourneyMapBuilder.render_markdown(journey)
    assert "预订体验" in md, "应包含标题"
    assert "小李" in md, "应包含角色"
    assert "😟" in md, "应包含低情绪emoji"
    assert "😄" in md, "应包含高情绪emoji"
    assert "排序差" in md, "应包含痛点"
    assert "智能排序" in md, "应包含机会"

    # 角色画像
    from udm import PersonaBuilder
    pb = skill.build_persona("小王")
    pb.set_demographics(30, "设计师")
    pb.set_bio("资深UX设计师")
    pb.add_goal("提升产品体验")
    pb.add_pain_point("缺乏用户数据")
    pb.set_quote("数据驱动设计")
    persona_md = PersonaBuilder.render_markdown(pb.build())
    assert "小王" in persona_md and "设计师" in persona_md

    # 加权矩阵
    wm = skill.build_weighted_matrix("方案对比")
    wm.add_criterion("体验", weight=0.5)
    wm.add_criterion("成本", weight=0.5)
    wm.add_option("A", {"体验": 5, "成本": 3})
    wm.add_option("B", {"体验": 3, "成本": 5})
    wm_md = wm.render_markdown()
    assert "推荐方案" in wm_md, "应包含推荐结果"

    # Elito 方法
    elito = skill.build_elito("洞察转化")
    elito.add_row(observation="用户反复比价", judgment="比价效率低",
                  value="一站式比价", concept="聚合比价")
    elito_md = elito.render_markdown()
    assert "Elito" in elito_md and "用户反复比价" in elito_md

    # 亲和图
    ad = skill.build_affinity_diagram("数据分析")
    ad.add_note("比价耗时", source="P1")
    ad.add_note("照片不真实", source="P2")
    ad.create_group("信任问题", ["照片不真实"], insight="用户缺乏信任")
    from udm import AffinityDiagramBuilder
    ad_md = AffinityDiagramBuilder.render_markdown(ad.build())
    assert "信任问题" in ad_md and "照片不真实" in ad_md

    print("✅ test_build_journey_map passed")


def test_generate_research_plan():
    """测试能力7: 研究计划生成"""
    skill = UDMSkill("测试产品")

    rp = skill.generate_research_plan("体验研究", background="用户流失率上升")
    rp.add_objective("了解流失原因", priority=1)
    rp.add_objective("评估竞品体验", priority=2)
    rp.add_method(48, participants=10, days=5, rationale="深入了解动机")
    rp.add_method(94, participants=8, days=3)
    rp.add_participant_criteria("过去3个月活跃用户")
    rp.add_recruit_channel("用户社群")
    rp.add_timeline_item("准备", "招募与材料", "1周", "招募完成")
    rp.add_timeline_item("执行", "访谈与测试", "2周", "原始数据")
    rp.add_deliverable("研究报告")
    rp.add_team_role("研究员", "小李")
    rp.add_budget_item("参与者报酬", 5000)
    rp.add_risk("招募困难", "扩大渠道")

    plan = rp.build()
    md = ResearchPlanBuilder.render_markdown(plan)

    assert "体验研究" in md, "应包含标题"
    assert "用户流失率上升" in md, "应包含背景"
    assert "了解流失原因" in md, "应包含目标"
    assert "访谈" in md, "应包含方法"
    assert "过去3个月" in md, "应包含招募标准"
    assert "5,000" in md or "5000" in md, "应包含预算"
    assert "招募困难" in md, "应包含风险"

    print("✅ test_generate_research_plan passed")


def test_generate_report():
    """测试能力8: 研究报告生成"""
    skill = UDMSkill("测试产品")

    report = skill.generate_report("体验研究报告", summary="发现3个核心痛点")
    report.add_method("用户访谈")
    report.add_method("可用性测试")
    report.set_participants(18)
    report.set_duration("2周")
    report.add_finding("比价困难", "需要切换多个平台",
                       evidence="8/10用户反馈", severity=3,
                       recommendation="一键比价")
    report.add_finding("信息过载", "搜索结果太多",
                       severity=4, recommendation="智能筛选")
    report.add_finding("字体偏小", "部分文字不易阅读",
                       severity=1)
    report.add_high_recommendation("优化搜索排序")
    report.add_medium_recommendation("增加比价功能")
    report.add_low_recommendation("调整字体大小")

    rpt = report.build()
    md = ReportBuilder.render_markdown(rpt)

    assert "体验研究报告" in md, "应包含标题"
    assert "3个核心痛点" in md, "应包含摘要"
    assert "用户访谈" in md, "应包含方法"
    assert "18" in md, "应包含参与人数"
    assert "比价困难" in md, "应包含发现"
    assert "🔴 严重" in md or "🟠 重要" in md, "应包含严重性标记"
    assert "优先级高" in md, "应包含优先级分类"
    assert "优化搜索排序" in md, "应包含建议"

    # 验证 JSON 导出
    json_data = ReportBuilder.render_json(rpt)
    assert json_data["title"] == "体验研究报告"
    assert len(json_data["findings"]) == 3
    assert json_data["recommendations"]["high"] == ["优化搜索排序"]

    print("✅ test_generate_report passed")


# ─────────────────────────────────────────────
# 运行入口
# ─────────────────────────────────────────────

if __name__ == "__main__":
    tests = [
        test_recommend_methods,
        test_generate_interview,
        test_generate_observation,
        test_generate_usability_test,
        test_generate_survey,
        test_build_journey_map,
        test_generate_research_plan,
        test_generate_report,
    ]

    passed = 0
    failed = 0

    print("=" * 60)
    print("UDM Skill 测试套件")
    print("=" * 60)

    for test_fn in tests:
        try:
            test_fn()
            passed += 1
        except Exception as e:
            failed += 1
            print(f"❌ {test_fn.__name__} FAILED: {e}")

    print("=" * 60)
    print(f"结果: {passed} 通过 / {failed} 失败 / {len(tests)} 总计")
    if failed == 0:
        print("🎉 全部测试通过！")
    else:
        print("⚠️ 存在失败的测试")
        sys.exit(1)
