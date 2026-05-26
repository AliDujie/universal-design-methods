#!/usr/bin/env python3
"""UDM Example 01: Research Method Recommendation / 研究方法推荐

Demonstrates the method recommendation capability for a realistic scenario.
演示针对真实场景的研究方法推荐能力。

Run: python 01_method_recommend.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from udm import UDMSkill

# ── Scenario: E-commerce app needs user needs research ──
# 场景：电商应用需要用户需求研究
print("=" * 60)
print("UDM Example 01: Research Method Recommendation")
print("示例 01：研究方法推荐")
print("=" * 60)

skill = UDMSkill("FreshMart 生鲜电商App")

# Goal 1: Explore user needs for a new product
print("\n📋 Research Goal: Explore user needs for grocery delivery")
print("📋 研究目标：探索生鲜配送用户需求")
print("-" * 50)
result = skill.recommend_methods("探索用户生鲜配送需求", phase=1)
print(result[:500])
print("...\n")

# Goal 2: Evaluate checkout flow usability
print("\n📋 Research Goal: Evaluate checkout flow usability")
print("📋 研究目标：评估结账流程可用性")
print("-" * 50)
result2 = skill.recommend_methods("评估结账流程可用性", phase=4)
print(result2[:500])
print("...\n")

print("✅ Tip: Use these recommendations to plan your research strategy.")
print("✅ 提示：使用这些推荐来规划你的研究策略。")
