#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

def text(rel):
    p = ROOT / rel
    assert p.exists(), rel
    return p.read_text(encoding="utf-8")

def data(rel):
    return json.loads(text(rel))

reg = data("stages/stage25/25-reentry-30/mask-registry.json")
back = data("stages/stage25/25-reentry-30/backflow-proposals.json")
ctrl = data("stages/stage25/25-reentry-controller.json")
res = text("stages/stage25/25-reentry-30/result.md")
disc = text("stages/stage25/25-reentry-30/discovery-ledger.md")
weap = text("stages/stage25/25-reentry-30/weapon-delta.md")
st13 = text("stages/stage13/final.md")
st17 = text("stages/stage17/final.md")
st23_bundle = text("stages/stage23/23-70/self-contained-bundle.md")
st19 = text("stages/stage19/post-stage25-50-supersession.md")
r008 = text("stages/stage25/25-reentry-r008a/audit.md")

assert reg["task_id"] == "Stage25-u23-r003a"
assert reg["phase"] == 30
assert reg["authorization"]["r008a_pr"] == 1004
assert reg["authorization"]["r008a_merge_commit"] == "11075adf8e30c73e5058790ee6ed6e2a9b6c9e2b"
assert "AUDIT_VERDICT=PASS" in r008

# Bind to Stage13 raw-mask definitions.
for marker in ("A_{ab,ac}=", "A_{ab,bc}=", "A_{ac,bc}=", "A_3=", "I_{ab}I_{ac}I_{bc}"):
    assert marker in st13, marker
assert "N_1(B)\\sim\\frac{\\kappa}{24\\pi}B(\\log B)^3" in st17
assert "CURRENT_LOWER=N2(B)>>B^(1/4)" in st19

m = reg["masks"]
assert m["a"]["identity"] == "N2,a=A_ab,ac-A3"
assert m["b"]["identity"] == "N2,b=A_ab,bc-A3"
assert m["c"]["identity"] == "N2,c=A_ac,bc-A3"
assert reg["sum_identity"] == "N2=A_ab,ac+A_ab,bc+A_ac,bc-3*A3"
assert len(reg["triple_free_contrasts"]) == 3

# Truth-table check for every three-face mask.
for ab in (0,1):
    for ac in (0,1):
        for bc in (0,1):
            a3 = ab*ac*bc
            naa = ab*ac*(1-bc)
            nbb = ab*bc*(1-ac)
            ncc = ac*bc*(1-ab)
            assert ab*ac - a3 == naa
            assert ab*bc - a3 == nbb
            assert ac*bc - a3 == ncc
            assert (ab*ac + ab*bc + ac*bc) - 3*a3 == naa+nbb+ncc
            assert (ab*ac-ab*bc) == (naa-nbb)
            assert (ab*ac-ac*bc) == (naa-ncc)
            assert (ab*bc-ac*bc) == (nbb-ncc)

# Stage23 ratio semantics are adjacent-stratum, never literal subset survival.
assert "The two strata are disjoint" in st23_bundle
assert "not a literal survival probability" in st23_bundle
assert reg["directional_stage23"]["ratio_semantics"] == "MATCHED_ADJACENT_STRATUM_POPULATION_SIZE_RATIO_NOT_LITERAL_SURVIVAL"
assert reg["directional_stage23"]["N2j_subset_of_N1"] is False
assert reg["directional_stage23"]["N1_and_N2j_disjoint_exact_face_strata"] is True
assert reg["directional_stage23"]["unbounded_target_chambers"] is True
assert reg["scope_firewall"]["literal_subset_survival_interpretation"] is False
assert "DIRECTIONAL_STAGE23_RATIO_SEMANTICS=ADJACENT_STRATUM_POPULATION_SIZE_NOT_LITERAL_SURVIVAL" in res
assert "LITERAL_N2J_SUBSET_OF_N1=false" in res

assert reg["scope_firewall"]["A3_quarter_power_control_proved"] is False
assert reg["scope_firewall"]["perfect_cuboid_existence_proved"] is False
assert reg["scope_firewall"]["perfect_cuboid_nonexistence_proved"] is False
assert reg["scope_firewall"]["global_N2_exponent_upgraded"] is False

for marker in (
    "N2,a = A_ab,ac - A3",
    "N2,b = A_ab,bc - A3",
    "N2,c = A_ac,bc - A3",
    "DIRECTIONAL_STAGE23_RATIO_LIMIT=0",
    "PERFECT_CUBOID_CONCLUSION=NONE",
):
    assert marker in res, marker
assert "D30-03" in disc and "A3" in disc
assert "S25R-W30-02" in weap

assert back["queued_derived_routes"] == ["Stage25-um-r009a"]
assert back["phase40_blocked_until_parent_audit_and_backflow_resolution"] is True
assert ctrl["current_phase"] == 30
assert ctrl["phases"]["20"]["status"] == "AUDITED_PASS_MERGED_BACKFLOW_AUDITED_PASS_MERGED"
assert ctrl["phases"]["40"]["status"] == "BLOCKED_UNTIL_PHASE30_BACKFLOW"
assert ctrl["stage26_gate"]["stage26_allowed"] is False
assert ctrl["propagation_queue"][-1]["route_id"] == "Stage25-um-r009a"

# Lifecycle-aware submission/audit states.
if ctrl["status"] == "PHASE30_SUBMITTED_PENDING_FRESH_AUDIT":
    assert reg["status"] == "SUBMITTED_PENDING_FRESH_AUDIT"
    assert ctrl["phases"]["30"]["status"] == "SUBMITTED_PENDING_AUDIT"
    assert ctrl["phase30_submission"]["audit_status"] == "PENDING"
    assert ctrl["phase30_submission"]["advance_allowed"] is False
    assert ctrl["phase30_submission"]["merge_allowed"] is False
    assert back["status"] == "QUEUED_PENDING_PARENT_AUDIT"
    assert ctrl["propagation_queue"][-1]["status"] == "QUEUED_UNTIL_PHASE30_AUDIT_PASS"
    assert ctrl["next_expected_command"] == "Stage25-reentry-audit"
elif ctrl["status"] == "PHASE30_AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW":
    assert reg["status"] == "AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW"
    assert ctrl["phases"]["30"]["status"] == "AUDITED_PASS_AWAITING_MERGE_AND_BACKFLOW"
    p30 = ctrl["phase30_submission"]
    assert p30["audit_status"] == "PASS"
    assert p30["advance_allowed"] is True
    assert p30["merge_allowed"] is True
    assert p30["stronger_result_proved"] is True
    assert p30["new_reusable_weapon_proved"] is True
    assert p30["ratio_semantics"] == "ADJACENT_STRATUM_POPULATION_SIZE_NOT_LITERAL_SURVIVAL"
    assert "AUDIT_VERDICT=PASS" in text(p30["audit_record"])
    assert back["status"] == "AUTHORIZED_BY_PARENT_AUDIT_AWAITING_PARENT_MERGE"
    assert ctrl["propagation_queue"][-1]["status"] == "AUTHORIZED_BY_PHASE30_AUDIT_AWAITING_PARENT_MERGE"
    assert ctrl["next_expected_command"] == "merge PR #1005; then Stage25-reentry-main-batch"
else:
    raise AssertionError(f"unexpected phase30 lifecycle: {ctrl['status']}")

print("STAGE25_REENTRY_PHASE30_MASK_TRUTH_TABLE=PASS")
print("STAGE25_REENTRY_PHASE30_SOURCE_BINDING=PASS")
print("STAGE25_REENTRY_PHASE30_ADJACENT_STRATUM_SEMANTICS=PASS")
print("STAGE25_REENTRY_PHASE30_DIRECTIONAL_NORMALIZATION=PASS")
print("STAGE25_REENTRY_PHASE30_BACKFLOW_QUEUE=PASS")
print("STAGE26_GATE=BLOCKED_VALID")
