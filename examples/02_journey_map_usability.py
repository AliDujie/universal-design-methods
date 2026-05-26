#!/usr/bin/env python3
"""UDM Example 02: Usability Testing + SUS Scoring / 可用性测试 + SUS 评分

Generates a usability test script and calculates SUS scores.
生成可用性测试脚本并计算系统可用性量表分数。

Run: python 02_usability_test.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from udm import UDMSkill

print("=" * 60)
print("UDM Example 02: Usability Testing + SUS Scoring")
print("示例 02：可用性测试 + SUS 评分")
print("=" * 60)

skill = UDMSkill("FreshMart Checkout")

# ── Generate usability test script ──
print("\n📋 Generating usability test for checkout flow...")
print("📋 为结账流程生成可用性测试...")
print("-" * 50)
test = skill.generate_usability_test("结账流程可用性测试", "summative")
print(test[:400])
print("...\n")

# ── SUS scoring with sample responses ──
# Sample: 10 SUS questions, 5-point Likert scale
# 示例：10 道 SUS 问题，5 点李克特量表
print("\n📊 SUS Score Calculation / SUS 分数计算")
print("-" * 50)
# Simulated user responses (strong positive UX)
responses = [4, 2, 5, 1, 4, 2, 5, 1, 4, 2]
result = skill.calculate_sus(responses)
print(f"  SUS Score: {result['score']}")
print(f"  Grade:     {result['grade']}")
print(f"  Rating:    {result['adjective']}")
print(f"  {result['description']}")

# Average UX
print()
avg_responses = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
avg_result = skill.calculate_sus(avg_responses)
print(f"  Average UX SUS: {avg_result['score']} ({avg_result['grade']})")

print("\n✅ Tip: SUS ≥ 68 is above average; ≥ 80 is A-grade.")
print("✅ 提示：SUS ≥ 68 高于平均；≥ 80 为 A 级。")
