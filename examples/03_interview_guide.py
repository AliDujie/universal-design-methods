#!/usr/bin/env python3
"""UDM Example 03: Interview Guide Generation / 访谈提纲生成

Demonstrates interview guide generation with structured question types.
演示结构化访谈提纲生成。

Run: python 03_interview_guide.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from udm import UDMSkill

print("=" * 60)
print("UDM Example 03: Interview Guide Generation")
print("示例 03：访谈提纲生成")
print("=" * 60)

skill = UDMSkill("FreshMart")

# ── Contextual Interview Guide ──
print("\n🎙️ Contextual Interview: Grocery Shopping Behavior")
print("🎙️ 脉络访谈：生鲜购物行为")
print("-" * 50)
guide = skill.generate_interview("生鲜购物行为访谈", "contextual")
print(guide[:400])
print("...\n")

# ── Semi-structured Interview Guide ──
print("\n🎙️ Semi-structured Interview: App Feedback")
print("🎙️ 半结构化访谈：应用反馈")
print("-" * 50)
guide2 = skill.generate_interview("应用使用体验反馈", "semi_structured")
print(guide2[:400])
print("...\n")

print("✅ Tip: Customize interview type based on research phase.")
print("✅ 提示：根据研究阶段定制访谈类型。")
