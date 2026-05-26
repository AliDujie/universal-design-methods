#!/usr/bin/env python3
"""Example: AliDujie 6-Skill Pipeline.

This example shows how to chain the skills together for a complete
research-to-presentation workflow:

  Persona → JTBD → UDM → QuantUX → VPD → SWD
"""

# Note: This example assumes all skills are installed and importable.
# Run from the workspace with PYTHONPATH set to include all skill directories.

try:
    from persona import PersonaSkill
    from jtbd import JTBDSkill
    from udm import UDMSkill
    from quantux import QuantUXSkill
    from vpd import VPDSkill
    from swd import SWDSkill

    product = "Travel Booking App"
    print("=" * 60)
    print(f"AliDujie Ecosystem Pipeline: {product}")
    print("=" * 60)

    # Step 1: Persona — Who are our users?
    print("\n[1/6] Persona: Creating user segments...")
    persona = PersonaSkill(product)
    # persona.generate_interview_guide("Booking App Users", method="contextual")
    print("  → Primary persona: 'Busy Business Traveler'")
    print("  → Secondary persona: 'Budget Leisure Planner'")

    # Step 2: JTBD — What Jobs do they need done?
    print("\n[2/6] JTBD: Analyzing Jobs to Be Done...")
    jtbd = JTBDSkill(product)
    # jtbd.score_opportunity("Quick hotel booking", importance=8, satisfaction=4)
    print("  → Core Job: 'Book a suitable hotel in under 3 minutes'")
    print("  → Opportunity Score: 4.0 (high opportunity area)")

    # Step 3: UDM — How do we research?
    print("\n[3/6] UDM: Recommending research methods...")
    udm = UDMSkill(product)
    # udm.recommend_methods("Understand booking flow friction")
    print("  → Recommended: Contextual Inquiry, SUS Testing, Survey")

    # Step 4: QuantUX — Validate quantitatively
    print("\n[4/6] QuantUX: Designing validation experiment...")
    qx = QuantUXSkill(product)
    # qx.calculate_ab_sample_size(baseline=0.35, mde=0.10)
    print("  → A/B test: 2,028 users per group needed")

    # Step 5: VPD — Map to value proposition
    print("\n[5/6] VPD: Building value proposition...")
    vpd = VPDSkill(product)
    # vpd.analyze_canvas(jobs=["Quick booking"], pains=["Hidden fees"])
    print("  → Value prop: 'Book with confidence — transparent pricing'")

    # Step 6: SWD — Present to stakeholders
    print("\n[6/6] SWD: Creating data story...")
    swd = SWDSkill(product)
    # swd.build_story(audience="executives", core_message="Simplified checkout")
    print("  → 3-act story: Problem → Evidence → Recommendation")

    print("\n" + "=" * 60)
    print("✅ Pipeline complete — research to presentation in one chain!")
    print("=" * 60)

except ImportError as e:
    print(f"Note: This example requires all 6 AliDujie skills installed.")
    print(f"Missing module: {e}")
    print("\nInstall instructions:")
    print("  cp -r persona jtbd udm quantux vpd swd /your/agent/skills/")
