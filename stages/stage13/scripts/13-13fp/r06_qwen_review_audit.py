#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[4]
base = root / "stages/stage13/13-13fp"
qwen = (base / "qwen-r06-verdict.md").read_text(encoding="utf-8")
ledger = (base / "r06-review-ledger.md").read_text(encoding="utf-8")
result = (base / "result.md").read_text(encoding="utf-8")
locks = (base / "locks.txt").read_text(encoding="utf-8")

for token in [
    "QWEN_R06_VERDICT=CLOSED",
    "QWEN_R06_REVIEWER_LABEL=CLOSED_WITH_DOCUMENTATION_NOTES",
    "QWEN_NEW_INDEPENDENT_BLOCKER_COUNT=0",
    "R07_BLOCKER_A_FIXED_TWIST_CONTRACT=true",
    "R07_BLOCKER_B_CONCRETE_FIXED_S_RESIDUE_MODEL=true",
]:
    assert token in qwen, token

for text in (ledger, result, locks):
    assert "QWEN_R06_VERDICT=CLOSED" in text
    assert "R06_EXTERNAL_REVIEWS_RECORDED=3" in text
    assert "R06_INDEPENDENT_CLOSED_VERDICTS=1" in text
    assert "R06_REQUIRED_INDEPENDENT_CLOSED_VERDICTS=2" in text
    assert "R06_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=3" in text
    assert "R07_REQUIRED=true" in text
    assert "PROMOTE_TO_13_13G=false" in text
    assert "NEXT=13-13fq" in text

assert "SUM_IQ_ANALYTIC_IDENTITY_REOPEN_REQUIRED=false" in ledger
assert "WIENER_CONSTANTS_REOPEN_REQUIRED=false" in ledger

print("STAGE13_13FP_QWEN_AUDIT=PASS")
print("QWEN_CLOSED_VOTE_COUNTED=1")
print("R06_PROMOTION_ALLOWED=false")
print("DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY")
