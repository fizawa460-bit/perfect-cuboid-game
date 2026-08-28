#!/usr/bin/env python3
"""Materialize the five raw-order2 smallest directions as MAIN working columns.

The raw-order2/naturality profile is exact.  This version also requires the
new direct exceptional-valuation certificate for all five directions.  MAIN
therefore pins only the remaining strict-transform/off-boundary purity
correction; none of these columns is promoted to audited Stage33-11 closure.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROFILE_SCRIPT = HERE / "profile_stage33_11_smallest_block_target_images.py"
LOCAL = HERE / "stage33-11-smallest-direct-exceptional-valuations.json"
A26_WORKING = HERE / "stage33-11-a2-26-main-working-column.json"
OUT = HERE / "stage33-11-smallest-main-working-columns.json"
EXPECTED_PROFILE = "45e42d6f3577654df7a4126cad5e2eee651c38fdce3c5cf8289b5f96707f2edc"
SMALLEST = [2, 3, 24, 25, 26]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_checked(path):
    obj=json.loads(path.read_text(encoding="utf-8")); body=dict(obj); claimed=body.pop("canonical_sha256")
    if csha(body)!=claimed: raise SystemExit(f"canonical hash mismatch for {path.name}")
    return obj


ns={"__name__":"__main__","__file__":str(PROFILE_SCRIPT)}
exec(compile(PROFILE_SCRIPT.read_text(encoding="utf-8"),str(PROFILE_SCRIPT),"exec"),ns)
profile=ns["cert"]; source_records=ns["source_records"]
if profile.get("canonical_sha256")!=EXPECTED_PROFILE: raise SystemExit("smallest-block target profile moved")
if [r["source_direction_1based"] for r in profile["smallest_direction_records"]]!=SMALLEST: raise SystemExit("smallest direction ordering moved")
local=load_checked(LOCAL)
if local.get("schema")!="STAGE33_11_SMALLEST_DIRECT_EXCEPTIONAL_VALUATIONS_V1": raise SystemExit("smallest local valuation schema moved")
if local.get("directions")!=[f"A2_{i:02d}" for i in SMALLEST]: raise SystemExit("smallest local valuation directions moved")
if local.get("exact_local_consequence",{}).get("coverage")!="5/5": raise SystemExit("smallest exceptional valuation coverage incomplete")
if local.get("exact_local_consequence",{}).get("all_five_exceptional_locus_differences")!="ZERO_EXACT": raise SystemExit("smallest exceptional locus difference moved")
local_records={r["source_direction"]:r for r in local["records"]}
a26=load_checked(A26_WORKING)
if a26.get("schema")!="STAGE33_11_A2_26_MAIN_WORKING_COLUMN_V2": raise SystemExit("A2_26 working-column schema moved")
if a26.get("main_working_convention",{}).get("absolute_connecting_class_working_value")!="ZERO": raise SystemExit("A2_26 working value moved")
records=[]
for idx1 in SMALLEST:
    src=source_records[idx1-1]
    prof=next(r for r in profile["smallest_direction_records"] if r["source_direction_1based"]==idx1)
    name=f"A2_{idx1:02d}"; loc=local_records[name]
    if src.get("source_basis_name")!=name or prof.get("source_basis_name")!=name: raise SystemExit(f"source ordering moved at {idx1}")
    if not src.get("raw_order2_first_residue_function_liftable"): raise SystemExit(f"{name} is no longer raw-order2 liftable")
    if loc["summary"].get("exceptional_locus_galois_difference_before_purity_correction")!="ZERO_EXACT": raise SystemExit(f"{name} exceptional difference moved")
    records.append({
        "source_direction_1based":idx1,"source_basis_name":name,"exact_raw_order2_first_residue_function_liftable":True,
        "exact_K_naturality_allowed_dimension_f2":prof["K_factor_allowed_value_subspace_dimension_f2"],
        "exact_finite_H1_naturality_allowed_dimension_f2":prof["finite_H1_factor_allowed_value_subspace_dimension_f2"],
        "exact_joint_cc_ct_restriction_rank_f2":prof["finite_H1_allowed_values_joint_restriction_rank_f2"],
        "exact_joint_cc_ct_restriction_kernel_dimension_f2":prof["finite_H1_allowed_values_joint_restriction_kernel_dimension_f2"],
        "exact_all_48_blowup_centers_evaluated":True,"exact_exceptional_locus_galois_difference":"ZERO_EXACT",
        "main_working_global_lift_convention":"PIN_ONLY_REMAINING_STRICT_TRANSFORM_PURITY_CORRECTION_Q_DEFINED_V4_FIXED_PENDING_AUDIT",
        "main_working_absolute_connecting_class":"ZERO","main_working_column_materialized":True,"exact_audited_column_materialized":False,"audit_required":True,
    })
cert={
    "schema":"STAGE33_11_SMALLEST_MAIN_WORKING_COLUMNS_V2","stage":"33-11","branch":"33-11c_SMALLEST_RAW_ORDER2_MAIN_WORKING_COLUMNS_LOCAL_VALUATIONS_DONE",
    "source_locks":{"smallest_block_target_profile_sha256":EXPECTED_PROFILE,"smallest_direct_exceptional_valuations_sha256":local["canonical_sha256"],"a2_26_main_working_column_sha256":a26["canonical_sha256"]},
    "working_columns":records,
    "progress":{"main_working_columns_materialized":5,"main_working_progress":"5/26","exact_audited_columns_materialized":0,"exact_exit_progress":"0/26","exact_local_exceptional_valuation_coverage":"5/5","remaining_main_directions":21,"next_main_task":"REMAINING_21_MIXED_ORDER_BLOCK_ORBIT_PRODUCTION"},
    "audit_debt":{"required":True,"directions":[f"A2_{i:02d}" for i in SMALLEST],"narrowed_to":"strict-transform/off-boundary height-one decomposition plus legitimacy of the pinned Q-defined/V4-fixed purity correction","failure_action":"replace only failing working columns before exact Stage33-11 closure"},
    "firewalls":{"stage33_11_closed_exact":False,"stage33_12_released":False,"stage33_08_released":False,"theorem_credit":False,"endpoint_credit":False},
}
cert["canonical_sha256"]=csha(cert)
OUT.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"success":True,"main_working_progress":"5/26","exact_local_exceptional_valuation_coverage":"5/5","exact_exit_progress":"0/26","directions":[r["source_basis_name"] for r in records],"next":cert["progress"]["next_main_task"],"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
