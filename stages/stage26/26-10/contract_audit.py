from fractions import Fraction
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[3]
base = root / "stages/stage26/26-10"
result = (base / "result.md").read_text()
ledger = (base / "discovery-ledger.md").read_text()
lattice = (base / "comparison-lattice.md").read_text()
ctl = json.loads((root / "stages/stage26/26-controller.json").read_text())
entry = json.loads((root / "stages/stage25/25-reentry-controller.json").read_text())

assert entry["status"] == "CLOSED_AUDITED_PASS_MERGED_STAGE26_HANDOFF_READY"
assert entry["stage26_gate"]["stage26_allowed"] is True
assert entry["next_expected_command"] == "Stage26-main-batch"

for marker in [
    "LITERAL_SUBSET_TRANSITION=false",
    "RATIO_SEMANTICS=MATCHED_ADJACENT_STRATUM_SIZE_RATIO",
    "EXACT_MEASURE_BRIDGE=true",
    "THETA_EQUALS_3PHI_OVER_1PLUS2PHI",
    "M_2(B)\\sim C_{M_2}B(\\log B)^5",
    "B^{1/6}\\ll M_3(B)\\ll_\\eta B(\\log B)^{5-\\eta}",
    "K3_FIREWALL=ACTIVE",
    "REPO_REUSE_PREFLIGHT=PASS",
    "DISCOVERY_AUDIT_VERDICT=PASS",
    "MATHEMATICAL_AUDIT_VERDICT=PENDING",
    "NEXT_EXPECTED_COMMAND=Stage26-audit",
]:
    assert marker in result, marker

for marker in [
    "ATTACK_MAP_RECORDS_SCANNED=824",
    "BROAD_STAGE26_CANDIDATE_MATCHES=122",
    "S1415-ATTACK-0215",
    "S1415-ATTACK-0225",
    "S20-W01",
    "S25-W06",
    "arXiv:2111.01509",
    "arXiv:2405.13061",
    "arXiv:2605.00573",
    "NO_GLOBAL_LITERATURE_EXHAUSTIVENESS_CLAIM=true",
]:
    assert marker in ledger, marker

for marker in [
    "NOMINAL_ENDPOINTS_DISJOINT=true",
    "RAW_PAIR_MULTIPLICITY_OF_M3=3",
    "EXACT_MEASURE_TRANSLATION=true",
    "SPACE_DIAGONAL_IMPORTED=false",
]:
    assert marker in lattice, marker

for r in [Fraction(1, 100), Fraction(1, 3), Fraction(2, 1), Fraction(17, 5)]:
    phi = r / (1 + r)
    theta = 3 * r / (1 + 3 * r)
    assert theta == 3 * phi / (1 + 2 * phi)
    assert phi == theta / (3 - 2 * theta)

assert ctl["stage"] == "Stage26"
assert ctl["transition"] == "Stage18 -> Stage20"
assert ctl["literal_subset_transition"] is False
assert ctl["checkpoint10"]["discovery_audit"] == "PASS_BY_CODEX"

# Lifecycle-aware checkpoint10: its mathematics stays immutable after audit and merge.
c10 = ctl["checkpoint10"]
if c10["mathematical_audit"] == "PENDING":
    assert ctl["checkpoint_status"]["10"] == "PROVED_SUBMITTED_PENDING_AUDIT"
    assert ctl["state"]["CURRENT_CHECKPOINT"] == 10
    assert ctl["state"]["AUDIT_STATUS"] == "PENDING"
    assert ctl["state"]["ADVANCE_ALLOWED"] is False
    assert ctl["state"]["MERGE_ALLOWED"] is False
elif c10["mathematical_audit"] == "PASS":
    assert (base / "audit.md").exists()
    assert "AUDIT_VERDICT=PASS" in (base / "audit.md").read_text()
    if ctl["checkpoint_status"]["10"] == "PROVED_AUDITED_PASS_AWAITING_MERGE":
        assert ctl["state"]["CURRENT_CHECKPOINT"] == 10
        assert ctl["state"]["AUDIT_STATUS"] == "PASS"
        assert ctl["state"]["ADVANCE_ALLOWED"] is True
        assert ctl["state"]["MERGE_ALLOWED"] is True
        assert ctl["state"]["NEXT_CHECKPOINT"] == 20
        assert ctl["next_expected_command"] == "merge PR #1014; then Stage26-main-batch"
    elif ctl["checkpoint_status"]["10"] == "PROVED_AUDITED_PASS_MERGED":
        assert c10["pr"] == 1014
        assert c10["merge_commit"] == "03ad11b0df214f95c4c077a3b22d12ffe391d160"
        assert ctl["state"]["CURRENT_CHECKPOINT"] >= 20
        assert ctl["checkpoint_status"]["20"] in (
            "SUBMITTED_PENDING_FRESH_AUDIT",
            "PROVED_AUDITED_PASS_AWAITING_MERGE",
            "PROVED_AUDITED_PASS_MERGED",
        )
    else:
        raise AssertionError(ctl["checkpoint_status"]["10"])
else:
    raise AssertionError(c10["mathematical_audit"])

bad_math = re.compile(r"M_[23]\\?\(B\\?\)(?:ll|sim)|(?:^|[^\\])(asymp|zeta|pi)(?:\{|\(|\\b)")
for path in [base / "result.md", base / "comparison-lattice.md", base / "discovery-ledger.md"]:
    assert not bad_math.search(path.read_text()), f"damaged LaTeX in {path}"

print("Stage26-10 contract/reuse/discovery audit: PASS")
print(f"STAGE26_10_LIFECYCLE={ctl['checkpoint_status']['10']}")
