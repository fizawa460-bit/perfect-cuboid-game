#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[4]
result = (root / "stages/stage13/13-13fp/result.md").read_text(encoding="utf-8")
verdict = (root / "stages/stage13/13-13fp/deepseek-r06-verdict.md").read_text(encoding="utf-8")
plan = (root / "stages/stage13/13-13fp/r07-repair-plan.md").read_text(encoding="utf-8")

required_result = [
    "DEEPSEEK_R06_VERDICT=OPEN",
    "R06_INDEPENDENT_CLOSED_VERDICTS=0",
    "R06_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=3",
    "R07_REQUIRED=true",
    "NEXT=13-13fq",
]
for token in required_result:
    assert token in result, token

required_verdict = [
    "DEEPSEEK_GATE_A_OBJECTION=REJECTED_FALSE_POSITIVE",
    "R07_BLOCKER_A_FIXED_TWIST_CONTRACT=true",
    "R07_BLOCKER_B_CONCRETE_FIXED_S_RESIDUE_MODEL=true",
    "R07_BLOCKER_C_CURVED_REGION_SELF_CONTAINED_CLOSURE=true",
    "DEEPSEEK_NONPRINCIPAL_SUM_RESTORES_POLE=REJECTED_FALSE_POSITIVE",
    "DEEPSEEK_TAGGED_INJECTION_OBJECTION=REJECTED_ALREADY_PROVED",
]
for token in required_verdict:
    assert token in verdict, token

assert 3465625 < 529 * 6561
assert 529 * 6561 == 3470769
assert 10799919009 < 432 * 25000000
assert 432 * 25000000 == 10800000000

required_plan = [
    "R07_FIXED_TWIST_PRIMARY_CONTRACT_VERIFIED=true",
    "R07_REDUCED_POLE_SIGNATURE_WELL_DEFINED=true",
    "R07_CURVED_REGION_FULL_LEMMA_IN_REVIEW_TARGET=true",
    "SUM_IQ_ANALYTIC_IDENTITY_REOPEN_REQUIRED=false",
    "PROMOTE_TO_13_13G=false",
]
for token in required_plan:
    assert token in plan, token

print("STAGE13_13FP_AUDIT=PASS")
print("DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY")
