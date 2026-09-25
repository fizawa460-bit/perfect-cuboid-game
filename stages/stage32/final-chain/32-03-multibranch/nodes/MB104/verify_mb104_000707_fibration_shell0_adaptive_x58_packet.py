#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_adaptive_x58_packet as runner

def validate_certificate(path,p,s,x61,r60,x60):
    d=json.loads(Path(path).read_text())
    assert d["schema"]==runner.SCHEMA
    cl=d["canonical_sha256_without_this_field"]; b=dict(d); b.pop("canonical_sha256_without_this_field")
    assert parent.csha(b)==cl
    key=(int(p),int(s),int(x61),int(r60),int(x60))
    rows=runner.split_rows(); assert key in rows
    q=d["partition"]
    assert (int(q["primary_value"]),int(q["secondary_residue"]),int(q["fixed_x61_value"]),int(q["x60_residue"]),int(q["fixed_x60_value"]))==key
    assert int(q["refinement_coordinate_0based"])==58
    assert q["x58_bound"]==rows[key]["bound"] and q["x58_intervals"]==rows[key]["intervals"]
    assert q["coverage_is_exact_disjoint"] is True and q["source_canonical_sha256"]==rows[key]["source_canonical_sha256"]
    assert d["semantic_source_locks"]==runner.semantic_source_locks()
    assert d["provenance"]["gen25_cold_canonical_sha256"]==runner.cold()["canonical_sha256_without_this_field"]
    assert len(d["children"])==8
    allc=True; integral_sum=0; child_union=[]; sx=set(); sf=set()
    for i,(child,(lo,hi)) in enumerate(zip(d["children"],rows[key]["intervals"])):
        ch=child["canonical_sha256_without_this_field"]; cb=dict(child); cb.pop("canonical_sha256_without_this_field")
        assert parent.csha(cb)==ch and int(child["interval_index"])==i and child["x58_interval"]==[lo,hi]
        allc=allc and child["result"]["complete"]
        if child["result"]["complete"]:
            assert child["status"]=="COMPLETE_EXACT_ADAPTIVE_X58_INTERVAL_ZERO_CREDIT"
            assert child["solver"]["final_solver_result"]=="unsat" and child["solver"]["reason"] is None
        else:
            assert child["status"] in {"PARTIAL_UNKNOWN_NO_CREDIT","PARTIAL_PACKET_WALL_NO_CREDIT","PARTIAL_MODEL_CAP_NO_CREDIT","NOT_RUN_PACKET_WALL_NO_CREDIT"}
        rr=child["result"]
        candidates=rr["primitive_known140_nonnegative_candidates"]
        assert int(rr["primitive_known140_nonnegative_candidate_count"])==len(candidates)
        integral=int(rr["integral_known140_nonnegative_solution_count"])
        assert integral>=len(candidates)>=0
        integral_sum+=integral
        for rec in candidates:
            replay=parent.replay_solution(0,[int(v) for v in rec["x_hperp_coordinates"]])
            assert replay==rec and replay["primitive"] is True
            xv=rec["x_hperp_coordinates"]
            assert int(xv[62])==key[0] and int(xv[61])==key[2] and int(xv[60])==key[4] and lo<=int(xv[58])<=hi
            xk=tuple(int(v) for v in xv); fk=tuple(int(v) for v in rec["picard_basis_coordinates"])
            assert xk not in sx and fk not in sf
            sx.add(xk); sf.add(fk); child_union.append(rec)
    child_union.sort(key=lambda rec:tuple(rec["picard_basis_coordinates"]))
    packet_candidates=d["result"]["primitive_known140_nonnegative_candidates"]
    assert packet_candidates==child_union
    assert int(d["result"]["primitive_known140_nonnegative_candidate_count"])==len(child_union)==len(sx)==len(sf)
    assert int(d["result"]["integral_known140_nonnegative_solution_count"])==integral_sum
    assert d["result"]["complete"] is allc
    assert int(d["result"]["complete_child_count"])==sum(c["result"]["complete"] for c in d["children"])
    assert int(d["result"]["child_count"])==8
    assert d["status"]==("COMPLETE_EXACT_ADAPTIVE_X58_PACKET_ZERO_CREDIT" if allc else "PARTIAL_ADAPTIVE_X58_PACKET_NO_CREDIT")
    assert all(v is False for v in d["credit_firewall"].values())
    return d

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--certificate",type=Path,required=True)
    ap.add_argument("--primary-value",type=int,required=True)
    ap.add_argument("--secondary-residue",type=int,required=True)
    ap.add_argument("--x61-value",type=int,required=True)
    ap.add_argument("--x60-residue",type=int,required=True)
    ap.add_argument("--x60-value",type=int,required=True)
    a=ap.parse_args()
    d=validate_certificate(a.certificate,a.primary_value,a.secondary_residue,a.x61_value,a.x60_residue,a.x60_value)
    print(json.dumps({"success":True,"complete":d["result"]["complete"],"complete_children":d["result"]["complete_child_count"],
                      "integral_count":d["result"]["integral_known140_nonnegative_solution_count"],
                      "primitive_candidates":d["result"]["primitive_known140_nonnegative_candidate_count"],
                      "canonical":d["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__":
    main()
