#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[4]
base = root / "stages/stage13/13-13fp"
claude = (base / "claude-r06-verdict.md").read_text(encoding="utf-8")
ledger = (base / "r06-review-ledger.md").read_text(encoding="utf-8")
plan = (base / "r07-repair-plan.md").read_text(encoding="utf-8")

for token in [
    "CLAUDE_R06_VERDICT=OPEN",
    "CLAUDE_R06_REVIEWER_LABEL=REPAIRABLE",
    "CLAUDE_SUM_IQ_CHECK=PASS",
    "CLAUDE_WIENER_CONSTANT_CHECK=PASS",
    "CLAUDE_GATE_C_LOCAL_TEST_CONCERN=ACCEPTED_CORROBORATION",
    "CLAUDE_HECKE_STRIP_GROWTH_CONCERN=ACCEPTED_CORROBORATION",
    "CLAUDE_NEW_INDEPENDENT_BLOCKER_COUNT=0",
]:
    assert token in claude, token

for token in [
    "DEEPSEEK_R06_VERDICT=OPEN",
    "CLAUDE_R06_VERDICT=OPEN",
    "QWEN_R06_VERDICT=CLOSED",
    "R06_EXTERNAL_REVIEWS_RECORDED=3",
    "R06_INDEPENDENT_CLOSED_VERDICTS=1",
    "R06_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=3",
    "R07_BLOCKER_A_FIXED_TWIST_CONTRACT=true",
    "R07_BLOCKER_B_CONCRETE_FIXED_S_RESIDUE_MODEL=true",
    "R07_BLOCKER_C_CURVED_REGION_SELF_CONTAINED_CLOSURE=true",
    "NEXT=13-13fq",
]:
    assert token in ledger, token

assert "R07_FIXED_TWIST_PRIMARY_CONTRACT_VERIFIED=true" in plan
assert "R07_ACTUAL_RESIDUE_COORDINATES_EXPLICIT=true" in plan
assert "PROMOTE_TO_13_13G=false" in plan

print("STAGE13_13FP_CLAUDE_AUDIT=PASS")
print("CLAUDE_R06_VERDICT=OPEN")
print("INTEGRATED_CLOSED_VERDICTS=1")
print("R06_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=3")
print("DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY")
