#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x61_packet as runner

def validate_certificate(path,primary,secondary_residue):
    d=json.loads(Path(path).read_text())
    assert d["schema"]==runner.SCHEMA
    claimed=d["canonical_sha256_without_this_field"]; body=dict(d); body.pop("canonical_sha256_without_this_field"); assert parent.csha(body)==claimed
    assert (int(primary),int(secondary_residue)) in set(runner.incomplete_cells())
    assert d["partition"]["primary_value"]==int(primary) and d["partition"]["secondary_residue"]==int(secondary_residue)
    vals=runner.child_values(int(primary),int(secondary_residue)); assert d["partition"]["x61_singleton_values"]==vals
    assert d["partition"]["parent_secondary_interval"]==runner.manifest()["secondary_intervals"][int(secondary_residue)]
    assert d["partition"]["coverage_is_exact_disjoint"] is True and d["semantic_source_locks"]==runner.semantic_source_locks()
    assert [c["fixed_x61_value"] for c in d["children"]]==vals and len(d["children"])==len(vals)
    sx=set(); sf=set(); all_complete=True
    for child in d["children"]:
        cc=child["canonical_sha256_without_this_field"]; cb=dict(child); cb.pop("canonical_sha256_without_this_field"); assert parent.csha(cb)==cc
        complete=child["result"]["complete"]; all_complete=all_complete and complete
        if complete:
            assert child["status"]=="COMPLETE_EXACT_X61_SINGLETON_ZERO_CREDIT" and child["solver"]["final_solver_result"]=="unsat" and child["solver"]["reason"] is None
        else:
            assert child["status"] in {"PARTIAL_UNKNOWN_NO_CREDIT","PARTIAL_PACKET_WALL_NO_CREDIT","PARTIAL_MODEL_CAP_NO_CREDIT","NOT_RUN_PACKET_WALL_NO_CREDIT"}
        for rec in child["result"]["primitive_known140_nonnegative_candidates"]:
            replay=parent.replay_solution(0,[int(v) for v in rec["x_hperp_coordinates"]]); assert replay==rec
            assert rec["x_hperp_coordinates"][62]==int(primary) and rec["x_hperp_coordinates"][61]==child["fixed_x61_value"]
            xk=tuple(rec["x_hperp_coordinates"]); fk=tuple(rec["picard_basis_coordinates"]); assert xk not in sx and fk not in sf; sx.add(xk); sf.add(fk)
    assert d["result"]["complete"] is all_complete
    assert d["result"]["complete_child_count"]==sum(1 for c in d["children"] if c["result"]["complete"])
    assert d["result"]["child_count"]==len(vals)
    assert d["result"]["primitive_known140_nonnegative_candidate_count"]==len(sx)
    assert d["status"]==("COMPLETE_EXACT_X61_SINGLETON_PACKET_ZERO_CREDIT" if all_complete else "PARTIAL_X61_SINGLETON_PACKET_NO_CREDIT")
    assert all(v is False for v in d["credit_firewall"].values())
    return d

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--certificate",type=Path,required=True); ap.add_argument("--primary-value",type=int,required=True); ap.add_argument("--secondary-residue",type=int,required=True); a=ap.parse_args()
    d=validate_certificate(a.certificate,a.primary_value,a.secondary_residue)
    print(json.dumps({"success":True,"complete":d["result"]["complete"],"primary_value":a.primary_value,"secondary_residue":a.secondary_residue,"complete_children":d["result"]["complete_child_count"],"child_count":d["result"]["child_count"],"canonical":d["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__": main()
