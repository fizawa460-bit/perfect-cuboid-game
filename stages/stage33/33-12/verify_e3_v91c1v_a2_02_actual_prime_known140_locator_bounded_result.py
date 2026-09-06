#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
CERT=HERE/"e3-v91c1v-a2-02-actual-prime-known140-locator-bounded-result.json"
DIAG=HERE/"diagnose_e3_v91c1v_actual_prime_known140_locator.py"
U=HERE/"e3-v91c1u-a2-02-known140-locator-preflight.json"
KNOWN=S33/"33-07"/"certify_two_coordinate_swap_picard_rows.py"
SIDE=S33/"33-07"/"certify_boundary_side_p1_crossing_coordinates.py"
HELPER=S33/"33-07"/"stoll_cuboid_source.py"

CERT_SHA="555c6d966ebca22536173839fda3100f2ea1fac1c10912b6a45c8833d5c0c293"
U_SHA="7480d0d77cc70762cb80e08081f49a5895bb21a46a99dfd699fe63980a977a34"
EXPECTED_MATCHES={"3f129d2be07133cdb60a167d2a199790a6fcdc95ae0b066eda2400bb0d2aa8c9":[10,12,14,16],"67c6a26f2b3d76d4659f5d7a04cc076f1ffdf95856508d26d34805f66367202e":[37,38],"8353da8852818df4bc17a94369d69e658aa8b2897cf073dfb18f2e6c26318bdc":[],"95524417ccf00758f884a4f1c70f29be551965a922afaacce78a5d5399ea4ad2":[18,20,22,24],"b22fc5b3b8096029b2d5b5930b30045b7eec7ec5aa5fc38f064569d9ab8ccf39":[41,42],"c452f68857bb9f03cacc1e774162c4c909ffb2aa1ad064e64527c0e8cb2d7de8":[43,44],"e5235f980a52e408098a096dfeb1c428babf7af9bf61d7b737d5b38a297a81d2":[],"f57b48e51f1e4162dc464579951ffbf930a4b8b4295292a0aecdf4d77537f03c":[39,40]}
UNMATCHED=["8353da8852818df4bc17a94369d69e658aa8b2897cf073dfb18f2e6c26318bdc","e5235f980a52e408098a096dfeb1c428babf7af9bf61d7b737d5b38a297a81d2"]

def csha(o):
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def blob_sha(path):
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def load(path,expected):
    o=json.loads(path.read_text(encoding="utf-8"))
    b=dict(o); q=b.pop("canonical_sha256")
    assert q==expected==csha(b),path
    return o

def main():
    ca=load(CERT,CERT_SHA)
    load(U,U_SHA)
    assert ca["entry_authority"]["authority_certificate_sha256"]==U_SHA
    assert ca["entry_authority"]["exact_audited_head"]=="4f9b6643081b32256e7cef2696bfba2dc1ece1b9"
    assert ca["entry_authority"]["hostile_audit_review"]==5124997953
    assert ca["entry_authority"]["merge_commit"]=="f8522bd1a38fa551186ad370f51d17c73c7927e2"
    locks=ca["source_locks"]
    assert blob_sha(DIAG)==locks["v91c1v_diagnostic_blob_sha1"]
    assert blob_sha(KNOWN)==locks["known140_reconstruction_script_blob_sha1"]
    assert blob_sha(SIDE)==locks["side_crossing_producer_blob_sha1"]
    assert blob_sha(HELPER)==locks["pinned_source_helper_blob_sha1"]
    helper=HELPER.read_text(encoding="utf-8")
    assert locks["pinned_upstream_commit"] in helper
    assert locks["pinned_upstream_blob_sha1"] in helper
    side=SIDE.read_text(encoding="utf-8")
    assert "Position(pts,p)" in side and "p in Cs[j]" in side
    assert "upstream_C1s_index_1based" in side
    ns=runpy.run_path(str(DIAG))
    r=ns["result"]
    assert r["success"] is True and r["credit"] is False
    assert r["pinned_known_curve_count"]==92
    assert r["strict_difference_prime_count"]==8
    assert r["strict_difference_prime_known_component_matches"]==EXPECTED_MATCHES
    assert r["match_count_histogram"]=={"0":2,"2":4,"4":2}
    assert r["all_needed_primes_have_known_components"] is False
    assert sorted(p for p,v in EXPECTED_MATCHES.items() if not v)==UNMATCHED
    x=ca["exact_result"]
    assert x["strict_difference_prime_known_component_matches"]==EXPECTED_MATCHES
    assert x["matched_strict_prime_count"]==6
    assert x["unmatched_strict_prime_count"]==2
    assert x["unmatched_strict_prime_ids"]==UNMATCHED
    assert x["exceptional_locator_materialized"] is True
    assert x["strict_locator_complete"] is False
    assert x["actual_divisor_to_picard64_adapter_materialized"] is False
    q=ca["exact_consequence"]
    assert q["a2_02_swap23_exceptional_id_to_known140_locator_materialized"] is True
    assert q["a2_02_swap23_strict_prime_to_known140_locator_materialized"] is False
    assert q["pic2_cech_difference_class_computed"] is False
    assert q["a2_02_swap23_seed_fixed_mod_pic2"] is False
    assert q["a2_02_marked_brauer_image_computed"] is False
    assert q["a2_02_marked_brauer_image_excluded_from_mask20"] is False
    assert ca["credit_firewall"]["merge_allowed"] is False
    print(json.dumps({"success":True,"marker":"V91C1V_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT","certificate_sha256":CERT_SHA,"matched_strict_primes":6,"unmatched_strict_primes":2,"next_exact_leaf":ca["next_exact_leaf"]},sort_keys=True))

if __name__=="__main__":
    main()
