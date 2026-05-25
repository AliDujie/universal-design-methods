#!/usr/bin/env python3
"""Example: Building an Experience Journey Map.

Scenario: Mapping a user's hotel booking experience to identify pain points.
"""
from udm import UDMSkill
from udm.synthesis import JourneyMapBuilder

udm = UDMSkill("Travel Booking App")

# Build a journey map for hotel booking
jm = udm.build_journey_map("Hotel Booking", persona="First-time Traveler")

# Add stages with emotions and pain points
jm.add_stage(
    "Search",
    actions=["Open app", "Enter destination"],
    emotions=4,
    pain_points=["Too many filter options — don't know where to start"]
)
jm.add_stage(
    "Compare",
    actions=["Switch between apps", "Read reviews"],
    emotions=2,
    pain_points=["Inconsistent rating scales across platforms", "Fake reviews"]
)
jm.add_stage(
    "Book",
    actions=["Enter payment", "Confirm booking"],
    emotions=3,
    pain_points=["Hidden fees revealed at payment", "No price comparison visible"]
)

# Render as markdown
print("=" * 60)
print("Hotel Booking — Experience Journey Map")
print("=" * 60)
print(JourneyMapBuilder.render_markdown(jm.build()))
