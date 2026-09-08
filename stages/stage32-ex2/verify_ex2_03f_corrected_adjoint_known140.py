#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
ART=HERE/"EX2-03/corrected-adjoint-known140-scan.json"
DIAG=HERE/"diagnose_ex2_03f_corrected_adjoint_known140.py"
EXPECTED_ART_BLOB="f5e8c5dbf7d01bf9e71cde7c13924de0d66e3007"
EXPECTED_DIAG_BLOB="636140991684704a5ba2d282094b9ab4bba386b8"
EXPECTED_CANONICAL="d55e804b062ca30163451563ad14cbe2797d5c48a44d8ec044be149aba0007a7"
TARGETS=[21,24,25,30,31]
NEG=[17,26,28]

def blob(path: Path) -> str:
    return subprocess.check_output(["git","hash-object",str(path.relative_to(ROOT))],cwd=ROOT,text=True).strip()

def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

assert blob(ART)==EXPECTED_ART_BLOB
assert blob(DIAG)==EXPECTED_DIAG_BLOB
x=json.loads(ART.read_text())
assert x["schema"]=="STAGE32EX2_EX2_03F_CORRECTED_ADJOINT_KNOWN140_DIAGNOSTIC_V1"
assert x["status"]=="EXACT_BOUNDED_KNOWN140_CORRECTED_ADJOINT_SCAN_COMPLETE"
assert x["target_labels_1based"]==TARGETS
stored=x.pop("canonical_sha256_without_this_field")
assert stored==EXPECTED_CANONICAL and csha(x)==EXPECTED_CANONICAL
rows=x["rows"]
assert [r["target_label_1based"] for r in rows]==TARGETS
for r in rows:
    assert r["bounded_known140_nonnegative"] is False
    assert r["negative_count"]==3
    assert r["negative_labels_1based"]==NEG
    assert r["target_self_twoP_dot"]==4
    assert all(v==0 for v in r["other_four_target_twoP_dots"].values())
assert x["correction_semantics"]["global_nef_inference_allowed"] is False
assert "EX2-04" in x["decision"]["fallback"]
for k in ["known140_nonnegative_promoted_to_global_nef","corrected_adjoint_promoted_to_nef","H1_vanishing_proved","restriction_evaluation_computed","remaining_five_fixedness_classified","complete_H0_reconstructed","integral_irreducible_genus1_member_constructed","stage32_main_credit","Q602_excluded","O210_excluded","receiver_credit","theorem_credit","endpoint_credit","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim"]:
    assert x["firewalls"][k] is False, k
print("PASS EX2-03F corrected-adjoint known140 blocker")
print("targets=21,24,25,30,31 negative_known140_labels=17,26,28")
print("global_nef=false H1_vanishing=false route=EX2-04")
