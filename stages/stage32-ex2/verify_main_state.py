#!/usr/bin/env python3
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
