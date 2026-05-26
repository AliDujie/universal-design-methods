#!/usr/bin/env python3
"""Example: UDM Method Recommendation for a real product scenario.

Scenario: A travel booking app sees high drop-off during the checkout flow.
The UX team wants to understand why and fix it.
"""
from udm import UDMSkill

# Initialize UDM for your product
udm = UDMSkill("Travel Booking App")

# Research goal: understand checkout abandonment
research_goal = "Understand why users abandon the booking flow at the payment step"

# Get method recommendations
print("=" * 60)
print(f"Research Goal: {research_goal}")
print("=" * 60)

methods = udm.recommend_methods(research_goal, phase=2)
print(methods)

# Generate an interview guide for the top recommendation
print("\n" + "=" * 60)
print("Interview Guide for Contextual Inquiry")
print("=" * 60)

guide = udm.generate_interview(
    "Checkout Flow Experience",
    "contextual",
    context="Users abandon during payment on travel booking app"
)
print(guide)
