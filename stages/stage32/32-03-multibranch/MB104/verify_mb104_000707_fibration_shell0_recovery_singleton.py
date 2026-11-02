#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_recovery_singleton as recovery
def validate_certificate(path,primary_value,secondary_residue):
    d=json.loads(Path(path).read_text()); assert d["schema"]==recovery.SCHEMA
    claimed=d["canonical_sha256_without_this_field"]; body=dict(d); body.pop("canonical_sha256_without_this_field"); assert claimed==parent.csha(body)
    assert d["semantic_source_locks"]==recovery.semantic_source_locks(); p=d["partition"]; sec=recovery.secondary_contract(); contract=parent.split_contract(0,8)
    assert p["primary_value"]==primary_value and p["residual_primary_values"]==recovery.PRIMARY_VALUES and p["gen15_complete_values"]==recovery.GEN15_COMPLETE_VALUES
    pres=recovery.parent_residue_for_value(primary_value); assert p["parent_shard_residue"]==pres and p["parent_shard_interval"]==contract["intervals"][pres]
    for key in ("secondary_coordinate_0based","secondary_coordinate_bound","secondary_shard_count","secondary_intervals","selection_method"): assert p[key]==sec[key]
    assert p["secondary_residue"]==secondary_residue and p["secondary_interval"]==sec["secondary_intervals"][secondary_residue]
    cands=d["result"]["primitive_known140_nonnegative_candidates"]; assert d["result"]["primitive_known140_nonnegative_candidate_count"]==len(cands)
    j=sec["secondary_coordinate_0based"]; lo,hi=sec["secondary_intervals"][secondary_residue]
    for rec in cands:
        assert parent.replay_solution(0,[int(v) for v in rec["x_hperp_coordinates"]])==rec and rec["primitive"] is True
        assert rec["x_hperp_coordinates"][62]==primary_value and lo<=rec["x_hperp_coordinates"][j]<=hi
    if d["result"]["complete"]: assert d["status"]=="COMPLETE_EXACT_SECONDARY_RECOVERY_ZERO_CREDIT" and d["solver"]["final_solver_result"]=="unsat" and d["solver"]["reason"] is None
    else: assert d["status"] in {"PARTIAL_UNKNOWN_NO_CREDIT","PARTIAL_WALL_NO_CREDIT","PARTIAL_MODEL_CAP_NO_CREDIT","PARTIAL_NOT_STARTED"} and d["solver"]["final_solver_result"]!="unsat"
    assert d["solver"]["floating_point_used"] is False and all(v is False for v in d["credit_firewall"].values()); return d
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--certificate",type=Path,required=True); ap.add_argument("--primary-value",type=int,required=True,choices=recovery.PRIMARY_VALUES); ap.add_argument("--secondary-residue",type=int,required=True,choices=range(8)); a=ap.parse_args(); d=validate_certificate(a.certificate,a.primary_value,a.secondary_residue)
    print(json.dumps({"success":True,"primary_value":a.primary_value,"secondary_residue":a.secondary_residue,"complete":d["result"]["complete"],"candidate_count":d["result"]["primitive_known140_nonnegative_candidate_count"],"canonical":d["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__": main()
