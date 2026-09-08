#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
LANES = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"
STATE = ROOT / "stages/stage32-ex2/MAIN-STATE.json"
STATE_VERIFY = ROOT / "stages/stage32-ex2/verify_main_state.py"

CLAIM_ID = "S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1"
CERT_PATH = "stages/stage32-ex2/EX2-03/known140-zero-curve-omission-witnesses.json"
CERT_BLOB = "a4b9396790b6c3b026a4a624247a48b1148a6d36"
CERT_CANONICAL = "60f6b4010549485282fab8d78da0e863e4746b07a83a9a0e33ddb2e175330330"
VERIFY_PATH = "stages/stage32-ex2/verify_ex2_03c_omission_witnesses.py"
VERIFY_BLOB = "4895f30c746684d20e9397bc18f496cc0c970023"
CURRENT_MAIN = "f2a89e613cdf91191a0aada9e90c9fc93373a6c6"
ANCESTRY_SYNC = "52c420ba29bbbdc3f5b7034c53577172ee377596"

CORE_KEYS = [
    "claim_id", "kind", "statement", "scope_key", "scope", "proves",
    "does_not_prove", "requires", "bridges", "source_locks", "replay_verifier",
]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def write_json(path: Path, obj: object) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")


def claim() -> dict:
    c = {
        "claim_id": CLAIM_ID,
        "kind": "mathematical_claim",
        "statement": "EX2-03C constructs exact nonnegative known-140 effective V6 divisors omitting retained zero-intersection curves C17 and C98 respectively; therefore C17 and C98 are not divisorial fixed components of |V6|, while labels [21,24,25,30,31] remain unresolved.",
        "scope_key": "S32.EX2.V6_LINEAR_SYSTEM",
        "scope": {
            "field": "Qbar",
            "lane": "EX2",
            "picard_class": "V6",
            "population": "retained known-140 effective-divisor monoid",
            "target_zero_labels_1based": [17, 21, 24, 25, 30, 31, 98],
            "unit": "EX2-03C",
        },
        "proves": [
            "Exact effective divisors linearly equivalent to V6 exist in the retained known-140 monoid with coefficient 0 at curve 17 and, separately, coefficient 0 at curve 98.",
            "Retained curves 17 and 98 are not divisorial fixed components of the complete linear system |V6|.",
        ],
        "does_not_prove": [
            "Any of retained zero-intersection curves 21,24,25,30,31 is a fixed component.",
            "The fixed part of |V6| is fully classified or empty.",
            "The retained known-140 monoid equals the complete linear system |V6|.",
            "A complete basis or exact dimension of H^0(S,O_S(V6)).",
            "An integral irreducible geometric-genus-1 V6 member.",
            "Population-wide nonexistence of such members.",
            "Stage32 MAIN, Q602, O210, receiver, theorem, endpoint, or Perfect Cuboid credit.",
        ],
        "requires": ["S32.EX2.LANE_CONTRACT.V3", "S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1"],
        "source_locks": [
            {"blob_sha1": CERT_BLOB, "canonical_sha256": CERT_CANONICAL, "path": CERT_PATH},
            {"blob_sha1": VERIFY_BLOB, "path": VERIFY_PATH},
        ],
        "replay_verifier": VERIFY_PATH,
        "authority_status": "PROVISIONAL",
        "audit_receipt": None,
    }
    c["claim_core_sha256"] = csha({k: c[k] for k in CORE_KEYS if k in c})
    assert c["claim_core_sha256"] == "21a66ba1f556fb8692c2c7bee40ea2ead2d7e3c21be9c8547d4a54e76f17a897"
    return c


def sync_registry() -> None:
    r = json.loads(REGISTRY.read_text())
    ids = [x["claim_id"] for x in r["claims"]]
    if CLAIM_ID not in ids:
        r["claims"].append(claim())
    else:
        existing = next(x for x in r["claims"] if x["claim_id"] == CLAIM_ID)
        assert existing == claim()
    write_json(REGISTRY, r)


def sync_lanes() -> None:
    obj = json.loads(LANES.read_text())
    lane = next(x for x in obj["lanes"] if x["lane"] == "EX2")
    refs = lane["claim_refs"]
    if CLAIM_ID not in refs:
        insert_at = refs.index("S32.ADAPTER.EX_TO_MAIN_PROMOTION_BOUNDARY.V3")
        refs.insert(insert_at, CLAIM_ID)
    lane["notes"] = (
        "EX2 attacks actual-member reconstruction and complete-linear-system nonexistence. "
        "EX2-00 is a retained typed source-lock boundary; EX2-01 is a PROVISIONAL one-dimensional abstract section-subspace result; "
        "EX2-02 is a PROVISIONAL bounded known-140 negative-intersection scan; EX2-03C is a PROVISIONAL exact omission-witness result certifying retained zero curves 17 and 98 are not divisorial fixed components. "
        "Labels 21,24,25,30,31 remain unresolved; bounded known140 UNSAT is not fixedness. None grants member, full fixed-part, or MAIN credit."
    )
    write_json(LANES, obj)


def sync_state() -> None:
    s = json.loads(STATE.read_text())
    s["schema"] = "STAGE32EX2_MAIN_COMPACT_STATE_V8_EX2_03C_TWO_ZERO_CURVES_NONFIXED_EX2_03D_ACTIVE"
    a = s["authority"]
    a.update({
        "EX2_03C_omission_witnesses": CERT_PATH,
        "EX2_03C_artifact_blob_sha1": CERT_BLOB,
        "EX2_03C_artifact_canonical_sha256": CERT_CANONICAL,
        "EX2_03C_verifier_blob_sha1": VERIFY_BLOB,
        "EX2_03C_candidate_claim_id": CLAIM_ID,
        "EX2_03C_claim_status": "PROVISIONAL_CLAIM_DAG_SYNCHRONIZED_NOT_HOSTILE_AUDITED",
    })
    f = s["freshness"]
    f.update({
        "last_reconciled_current_main_sha": CURRENT_MAIN,
        "ancestry_sync_commit": ANCESTRY_SYNC,
        "current_main_observed_sha": CURRENT_MAIN,
        "unreconciled_main_commit_count": 0,
        "intervening_main_commit_scope": "STAGE32_MAIN_STARTUP_ROLE_AND_EX_OWNERSHIP_PRECEDENCE_ONLY",
        "intervening_main_confirms_EX2_ownership_of_actual_member_linear_system_fixed_moving": True,
        "stage32ex2_source_drift_in_intervening_main_commit": False,
        "freshness_sync_deferred_until_retained_promotion_checkpoint": False,
        "promotion_requires_recheck_current_main": True,
    })
    cs = s["claim_sync"]
    cs.update({
        "candidate_claim_id": CLAIM_ID,
        "checkpoint_claim_dag_complete": True,
        "claim_dag_integrity_verifier_passed": True,
        "active_frontier_verifier_passed": True,
        "current_main_reconciliation_required": False,
        "mathematical_frontier_semantics_changed": False,
        "promotion_attempted": False,
        "reason": "EX2-03C adds a narrow provisional mathematical claim: exact alternate effective V6 divisors omit retained zero curves 17 and 98, certifying those two curves nonfixed. Current main f2a89e6 is an ancestor of the EX2 branch; MAIN authority/frontier is unchanged.",
        "reconciled_current_main_sha": CURRENT_MAIN,
        "required_verification_run": None,
        "shared_claim_files_written_from_stale_branch": False,
        "stage32_main_authority_changed": False,
        "status": "COMPLETE_CURRENT_MAIN_RECONCILED_LOCAL_DAG_VERIFIERS_PASS_EXACT_HEAD_CI_REQUIRED_BEFORE_AUDIT",
        "trigger": "RETAINED_CONSOLIDATION",
        "triggered_for_EX2_03C": True,
    })
    c = s["credit"]
    c["level"] = "CERTIFIED_1D_ABSTRACT_SECTION_SUBSPACE_PLUS_EXACT_BOUNDED_KNOWN140_NEGATIVE_SCAN_PLUS_TWO_ZERO_CURVES_CERTIFIED_NONFIXED_NO_MEMBER_CREDIT"
    c["zero_curve_nonfixedness_certified_count"] = 2
    cur = s["current"]
    cur.update({
        "leaf": "EX2-03D_REMAINING_FIVE_ZERO_CURVE_RESTRICTION_OR_OUTSIDE_KNOWN140_MEMBER_PREFLIGHT",
        "status": "EX2_03C_TWO_ZERO_CURVES_CERTIFIED_NONFIXED_REMAINING_FIVE_UNRESOLVED",
        "subroute": "REMAINING_FIVE_ZERO_CURVE_FIXEDNESS_WITHOUT_KNOWN140_UNSAT_PROMOTION",
        "objective": "Resolve retained V6-zero labels [21,24,25,30,31] using a source-bound restriction/base-locus adapter or an effective V6 divisor outside the bounded known140 monoid. The exact known140 solver UNSAT diagnostics for these five labels are not fixedness proofs.",
        "next_route_on_success": "RETAIN_ANY_NEW_EXACT_FIXEDNESS_OR_NONFIXEDNESS_WITNESS_WITH_EXPLICIT_SCOPE",
        "next_route_on_block": "MOVE_TO_A_DISTINCT_LEGAL_EX2_SECTION_COORDINATE_OR_IDEAL_SYZYGY_LANE_WITHOUT_TREATING_THE_FIVE_CURVES_AS_FIXED",
    })
    fr = s["frontier"]
    fr.update({
        "EX2_03_zero_curve_fixedness_classified_count": 0,
        "EX2_03_zero_curve_nonfixedness_classified_count": 2,
        "EX2_03C_alternate_known140_decomposition_preflight_active": False,
        "EX2_03C_complete": True,
        "EX2_03C_certified_nonfixed_zero_labels_1based": [17, 98],
        "EX2_03C_unresolved_zero_labels_1based": [21, 24, 25, 30, 31],
        "EX2_03C_exact_omission_witness_count": 2,
        "EX2_03D_remaining_five_zero_curve_preflight_active": True,
        "fixed_part_fully_classified": False,
        "moving_system_structure_classified": False,
        "full_target_closure": False,
    })
    s["firewalls"]["remaining_five_known140_unsat_promoted_to_fixedness"] = False
    s["current_leaf_working_set"] = [
        CERT_PATH,
        VERIFY_PATH,
        "stages/stage32-ex2/EX2-03/zero-intersection-restriction-adapter-gap.json",
        "stages/stage32-ex2/verify_ex2_03_restriction_gap.py",
        "stages/stage32-ex2/EX2-02/exact-fixed-component-extraction.json",
        "stages/stage32-ex2/verify_ex2_02_fixed_components.py",
        "stages/stage32-ex2/EX2-01/section-source-inventory.json",
        "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json",
        "stages/stage32-ex2/stage32-ex2.md",
        "stages/stage32/32-21/post1473-v6-witness-body-recovered.json",
        "stages/stage32/residual-32-01-production/post1648ag-v6-known140-basis-elimination.json",
    ]
    write_json(STATE, s)


def write_state_verifier() -> None:
    text = r'''#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
CERT = HERE / "EX2-03/known140-zero-curve-omission-witnesses.json"
CERT_VERIFY = HERE / "verify_ex2_03c_omission_witnesses.py"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
LANES = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()
def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))
s = json.loads(STATE.read_text())
cert = json.loads(CERT.read_text())
r = json.loads(REGISTRY.read_text())
l = json.loads(LANES.read_text())
assert s["schema"] == "STAGE32EX2_MAIN_COMPACT_STATE_V8_EX2_03C_TWO_ZERO_CURVES_NONFIXED_EX2_03D_ACTIVE"
assert s["stage"] == "32EX2"
assert s["bootstrap"]["active_work_pr"] == 1709 and s["bootstrap"]["merge_authorized"] is False
assert s["audit"]["status"] == "NOT_READY_INTERMEDIATE_LEAF_ONLY"
a = s["authority"]
assert a["EX2_03C_omission_witnesses"] == "stages/stage32-ex2/EX2-03/known140-zero-curve-omission-witnesses.json"
assert a["EX2_03C_artifact_blob_sha1"] == blob(CERT) == "a4b9396790b6c3b026a4a624247a48b1148a6d36"
assert a["EX2_03C_artifact_canonical_sha256"] == cert["canonical_sha256_without_this_field"] == "60f6b4010549485282fab8d78da0e863e4746b07a83a9a0e33ddb2e175330330"
assert a["EX2_03C_verifier_blob_sha1"] == blob(CERT_VERIFY) == "4895f30c746684d20e9397bc18f496cc0c970023"
assert a["EX2_03C_candidate_claim_id"] == "S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1"
assert a["EX2_03C_claim_status"] == "PROVISIONAL_CLAIM_DAG_SYNCHRONIZED_NOT_HOSTILE_AUDITED"
assert cert["certified_nonfixed_zero_labels_1based"] == [17,98]
assert cert["unresolved_zero_labels_1based"] == [21,24,25,30,31]
assert cert["inference"]["curve_17_nonfixed_divisorial_component"] is True
assert cert["inference"]["curve_98_nonfixed_divisorial_component"] is True
f=s["freshness"]
assert f["last_reconciled_current_main_sha"] == "f2a89e613cdf91191a0aada9e90c9fc93373a6c6"
assert f["ancestry_sync_commit"] == "52c420ba29bbbdc3f5b7034c53577172ee377596"
assert f["unreconciled_main_commit_count"] == 0
assert f["stage32ex2_source_drift_in_intervening_main_commit"] is False
cs=s["claim_sync"]
assert cs["triggered_for_EX2_03C"] is True
assert cs["candidate_claim_id"] == "S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1"
assert cs["checkpoint_claim_dag_complete"] is True
assert cs["current_main_reconciliation_required"] is False
assert cs["stage32_main_authority_changed"] is False
assert cs["promotion_attempted"] is False
cur=s["current"]
assert cur["leaf"] == "EX2-03D_REMAINING_FIVE_ZERO_CURVE_RESTRICTION_OR_OUTSIDE_KNOWN140_MEMBER_PREFLIGHT"
assert cur["subroute"] == "REMAINING_FIVE_ZERO_CURVE_FIXEDNESS_WITHOUT_KNOWN140_UNSAT_PROMOTION"
fr=s["frontier"]
assert fr["EX2_03C_complete"] is True
assert fr["EX2_03_zero_curve_nonfixedness_classified_count"] == 2
assert fr["EX2_03C_certified_nonfixed_zero_labels_1based"] == [17,98]
assert fr["EX2_03C_unresolved_zero_labels_1based"] == [21,24,25,30,31]
assert fr["EX2_03D_remaining_five_zero_curve_preflight_active"] is True
assert fr["fixed_part_fully_classified"] is False
assert fr["explicit_V6_genus1_member_verified"] is False
assert fr["full_target_closure"] is False
claims={x["claim_id"]:x for x in r["claims"]}
c=claims["S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1"]
assert c["authority_status"] == "PROVISIONAL"
assert c["requires"] == ["S32.EX2.LANE_CONTRACT.V3","S32.EX2.FIXED_COMPONENT_NEGATIVE_SCAN.V1"]
assert c["replay_verifier"] == "stages/stage32-ex2/verify_ex2_03c_omission_witnesses.py"
assert claims["S32.EX1.CANDIDATE_THROUGH_05H.V3"]["authority_status"] == "AUDITED"
assert claims["S32.EX1.CANDIDATE_THROUGH_05H.V3"]["audit_receipt"]["review_id"] == 5136931113
lane={x["lane"]:x for x in l["lanes"]}["EX2"]
assert "S32.EX2.ZERO_CURVE_NONFIXEDNESS_17_98.V1" in lane["claim_refs"]
credit=s["credit"]
assert credit["zero_curve_nonfixedness_certified_count"] == 2
assert credit["fixed_part_fully_classified"] is False
assert credit["genuine_v6_genus1_member_established"] is False
assert credit["stage32_main_credit"] is False
for key in ["remaining_five_known140_unsat_promoted_to_fixedness","alternate_known140_solver_miss_promoted_to_full_fixedness","stage32_main_credit","Q602_excluded","O210_excluded","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:
    assert s["firewalls"][key] is False, key
for rel in s["current_leaf_working_set"]:
    assert (ROOT / rel).exists(), rel
print("Stage32EX2 MAIN state: PASS; EX2-03C certifies zero curves 17 and 98 nonfixed at provisional scope, preserves five unresolved zero curves and all MAIN/member firewalls, and routes EX2-03D.")
'''
    STATE_VERIFY.write_text(text)


def run_checks() -> None:
    cmds = [
        ["python", "stages/stage32/proof/verify_stage32_claim_dag.py", "--integrity"],
        ["python", "stages/stage32/proof/verify_stage32_active_frontier.py"],
        ["python", "stages/stage32-ex2/verify_ex2_03c_omission_witnesses.py"],
        ["python", "stages/stage32-ex2/verify_main_state.py"],
    ]
    for cmd in cmds:
        subprocess.check_call(cmd, cwd=ROOT)


def main() -> None:
    sync_registry()
    sync_lanes()
    sync_state()
    write_state_verifier()
    run_checks()
    print("PASS EX2-03C claim-sync working tree")

if __name__ == "__main__":
    main()
