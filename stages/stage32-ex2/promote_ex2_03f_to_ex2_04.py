#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
STATE=HERE/"MAIN-STATE.json"
ART=HERE/"EX2-03/corrected-adjoint-known140-scan.json"
VER=HERE/"verify_ex2_03f_corrected_adjoint_known140.py"
DIAG=HERE/"diagnose_ex2_03f_corrected_adjoint_known140.py"
EXPECTED_STATE_SCHEMA="STAGE32EX2_MAIN_COMPACT_STATE_V9_EX2_03D_FIVE_CONIC_RESTRICTION_REDUCTION_EX2_03E_ACTIVE"
EXPECTED_ART_BLOB="f5e8c5dbf7d01bf9e71cde7c13924de0d66e3007"
EXPECTED_ART_CANONICAL="d55e804b062ca30163451563ad14cbe2797d5c48a44d8ec044be149aba0007a7"
EXPECTED_VER_BLOB="9975ba1d418f341dbb8fe82153c473d1c5f8fc51"
EXPECTED_DIAG_BLOB="636140991684704a5ba2d282094b9ab4bba386b8"
TARGETS=[21,24,25,30,31]
NEG=[17,26,28]

def blob(path: Path) -> str:
    return subprocess.check_output(["git","hash-object",str(path.relative_to(ROOT))],cwd=ROOT,text=True).strip()

def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

assert blob(ART)==EXPECTED_ART_BLOB
assert blob(VER)==EXPECTED_VER_BLOB
assert blob(DIAG)==EXPECTED_DIAG_BLOB
art=json.loads(ART.read_text())
stored=art.pop("canonical_sha256_without_this_field")
assert stored==EXPECTED_ART_CANONICAL and csha(art)==EXPECTED_ART_CANONICAL
assert art["target_labels_1based"]==TARGETS
assert [r["target_label_1based"] for r in art["rows"]]==TARGETS
for r in art["rows"]:
    assert r["bounded_known140_nonnegative"] is False
    assert r["negative_count"]==3
    assert r["negative_labels_1based"]==NEG

s=json.loads(STATE.read_text())
assert s["schema"]==EXPECTED_STATE_SCHEMA
assert s["current"]["leaf"]=="EX2-03E_FIVE_CONIC_RESTRICTION_EVALUATION_OR_H1_JUMP_PREFLIGHT"
assert s["bootstrap"]["merge_authorized"] is False
assert s["freshness"]["unreconciled_main_commit_count"]==0

A=s["authority"]
A.update({
    "EX2_03E_adjoint_blocker":"stages/stage32-ex2/EX2-03/adjoint-nef-blocker-preflight.json",
    "EX2_03E_artifact_blob_sha1":"3c93705c2515346853b58e337add31fa0ad83e93",
    "EX2_03E_claim_status":"TYPED_ROUTE_BLOCKER_NO_MATHEMATICAL_CLAIM_NO_CLAIM_DAG_ENTRY",
    "EX2_03F_corrected_adjoint_scan":"stages/stage32-ex2/EX2-03/corrected-adjoint-known140-scan.json",
    "EX2_03F_artifact_blob_sha1":EXPECTED_ART_BLOB,
    "EX2_03F_artifact_canonical_sha256":EXPECTED_ART_CANONICAL,
    "EX2_03F_diagnostic_blob_sha1":EXPECTED_DIAG_BLOB,
    "EX2_03F_verifier_blob_sha1":EXPECTED_VER_BLOB,
    "EX2_03F_claim_status":"TYPED_ROUTE_BLOCKER_NO_MATHEMATICAL_CLAIM_NO_CLAIM_DAG_ENTRY",
})

s["credit"]["level"]="CERTIFIED_1D_ABSTRACT_SECTION_SUBSPACE_PLUS_BOUNDED_NEGATIVE_SCAN_PLUS_TWO_ZERO_CURVES_NONFIXED_PLUS_FIVE_CONIC_RESTRICTION_REDUCTION_PLUS_CORRECTED_ADJOINT_KNOWN140_BLOCKER_NO_MEMBER_CREDIT"
s["current"]={
    "leaf":"EX2-04_FINITE_DIMENSIONAL_SECTION_RECONSTRUCTION",
    "next_route_on_block":"ROUTE_TO_DISTINCT_EX2_04_SECTION_LANE_WITH_EXACT_ADAPTER_GAP",
    "next_route_on_success":"RETAIN_EXPLICIT_SECTION_VECTORS_AND_ROUTE_TO_EX2_05_MEMBER_MATERIALIZATION",
    "objective":"Convert at least one source-bound V6 section lane into an explicit finite linear-algebra reconstruction (ambient/projective forms, graded ideal/syzygy, enlargement beyond the known140 product span, or exact restriction/gluing). State exactly whether the output is complete H0, a certified subspace, or only candidates.",
    "status":"EX2_03F_NATURAL_CORRECTED_ADJOINT_STILL_NEGATIVE_ON_KNOWN140_EX2_04_ACTIVE",
    "stop_semantics":"LEAF_GATE_ONLY_NOT_STAGE_EXHAUSTION",
    "subroute":"FINITE_DIMENSIONAL_SECTION_RECONSTRUCTION_OUTSIDE_KNOWN140_MONOID",
}
s["current_leaf_working_set"]=[
    "stages/stage32-ex2/EX2-03/corrected-adjoint-known140-scan.json",
    "stages/stage32-ex2/verify_ex2_03f_corrected_adjoint_known140.py",
    "stages/stage32-ex2/diagnose_ex2_03f_corrected_adjoint_known140.py",
    "stages/stage32-ex2/EX2-01/section-source-inventory.json",
    "stages/stage32-ex2/verify_ex2_01_section_sources_v2.py",
    "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json",
    "stages/stage32-ex2/stage32-ex2.md",
    "stages/stage32/32-21/post1473-v6-witness-body-recovered.json",
]
F=s["frontier"]
F.update({
    "EX2_03D_remaining_five_zero_curve_preflight_active":False,
    "EX2_03E_five_conic_evaluation_preflight_active":False,
    "EX2_03E_naive_adjoint_nef_route_blocked":True,
    "EX2_03F_corrected_adjoint_known140_scan_complete":True,
    "EX2_03F_corrected_adjoint_known140_negative_labels_1based":NEG,
    "EX2_03F_corrected_adjoint_known140_negative_count_each":3,
    "EX2_03F_corrected_adjoint_global_nef_proved":False,
    "EX2_03F_H1_vanishing_proved":False,
    "EX2_04_finite_dimensional_section_reconstruction_active":True,
})
s["firewalls"].update({
    "corrected_adjoint_known140_scan_promoted_to_global_nef":False,
    "h1_vanishing_inferred_from_blocked_nef_route":False,
    "nef_route_blocker_promoted_to_fixedness":False,
})
s["claim_sync"]["reason"]="EX2-03F is a typed local route blocker only: the natural corrected adjoint remains negative on retained known140 labels 17,26,28 for every target conic. No new theorem claim or Stage32 MAIN authority is created; EX2 routes to finite-dimensional section reconstruction."
s["claim_sync"]["mathematical_frontier_semantics_changed"]=False
s["schema"]="STAGE32EX2_MAIN_COMPACT_STATE_V10_EX2_03F_CORRECTED_ADJOINT_BLOCKED_EX2_04_ACTIVE"
STATE.write_text(json.dumps(s,indent=2,sort_keys=True)+"\n")
print("PROMOTED EX2-03F blocker -> EX2-04 finite-dimensional section reconstruction")
