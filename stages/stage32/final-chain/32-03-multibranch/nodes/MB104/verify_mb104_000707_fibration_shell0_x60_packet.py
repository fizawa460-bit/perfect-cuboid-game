#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x60_packet as runner

def validate_certificate(path,primary,secondary_residue,x61_value):
    d=json.loads(Path(path).read_text()); assert d["schema"]==runner.SCHEMA
    claimed=d["canonical_sha256_without_this_field"]; body=dict(d); body.pop("canonical_sha256_without_this_field"); assert parent.csha(body)==claimed
    key=(int(primary),int(secondary_residue),int(x61_value)); assert key in set(runner.residual_leaves())
    p=d["partition"]; assert (int(p["primary_value"]),int(p["secondary_residue"]),int(p["fixed_x61_value"]))==key
    contract=runner.x60_contract(); assert p["coordinate_0based"]==60 and p["bound"]==[-20,20] and p["intervals"]==contract["intervals"] and p["coverage_is_exact_disjoint"] is True
    assert d["semantic_source_locks"]==runner.semantic_source_locks() and len(d["children"])==8
    sx=set(); sf=set(); all_complete=True
    for r,child in enumerate(d["children"]):
        cc=child["canonical_sha256_without_this_field"]; cb=dict(child); cb.pop("canonical_sha256_without_this_field"); assert parent.csha(cb)==cc
        assert child["x60_residue"]==r and child["x60_interval"]==contract["intervals"][r]
        complete=child["result"]["complete"]; all_complete=all_complete and complete
        if complete:
            assert child["status"]=="COMPLETE_EXACT_X60_INTERVAL_ZERO_CREDIT" and child["solver"]["final_solver_result"]=="unsat" and child["solver"]["reason"] is None
        else:
            assert child["status"] in {"PARTIAL_UNKNOWN_NO_CREDIT","PARTIAL_PACKET_WALL_NO_CREDIT","PARTIAL_MODEL_CAP_NO_CREDIT","NOT_RUN_PACKET_WALL_NO_CREDIT"}
        lo,hi=child["x60_interval"]
        for rec in child["result"]["primitive_known140_nonnegative_candidates"]:
            replay=parent.replay_solution(0,[int(v) for v in rec["x_hperp_coordinates"]]); assert replay==rec
            assert rec["x_hperp_coordinates"][62]==key[0] and rec["x_hperp_coordinates"][61]==key[2] and lo<=rec["x_hperp_coordinates"][60]<=hi
            xk=tuple(rec["x_hperp_coordinates"]); fk=tuple(rec["picard_basis_coordinates"]); assert xk not in sx and fk not in sf; sx.add(xk); sf.add(fk)
    assert d["result"]["complete"] is all_complete and d["result"]["complete_child_count"]==sum(1 for c in d["children"] if c["result"]["complete"]) and d["result"]["child_count"]==8
    assert d["result"]["primitive_known140_nonnegative_candidate_count"]==len(sx)
    assert d["status"]==("COMPLETE_EXACT_X60_INTERVAL_PACKET_ZERO_CREDIT" if all_complete else "PARTIAL_X60_INTERVAL_PACKET_NO_CREDIT")
    assert all(v is False for v in d["credit_firewall"].values()); return d

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--certificate",type=Path,required=True); ap.add_argument("--primary-value",type=int,required=True); ap.add_argument("--secondary-residue",type=int,required=True); ap.add_argument("--x61-value",type=int,required=True); a=ap.parse_args()
    d=validate_certificate(a.certificate,a.primary_value,a.secondary_residue,a.x61_value)
    print(json.dumps({"success":True,"complete":d["result"]["complete"],"complete_children":d["result"]["complete_child_count"],"child_count":8,"canonical":d["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__": main()
