#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,time
from pathlib import Path
from z3 import Or,sat,unknown,unsat,get_version_string
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x60_packet as x60parent
HERE=Path(__file__).resolve().parent
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
COLD=HERE/"MB104-000707-GEN25-ADAPTIVE-AFFINE-COLD.json"
SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_PACKET_V1"

def cold():
    d=json.loads(COLD.read_text())
    assert d["schema"]=="STAGE32_MB104_000707_GEN25_ADAPTIVE_AFFINE_COLD_V1"
    assert d["canonical_sha256_without_this_field"]=="6daaaef5e82aaefab0b676c24392b08894e7ecf63b6a930f0327d74ffd48a1d7"
    assert int(d["carried_complete_x60_singletons"])==281
    assert int(d["residual_timeout_leaf_count"])==30
    assert int(d["summary"]["necessary_condition_empty_leaf_count"])==14
    assert int(d["summary"]["split_leaf_count"])==16
    assert int(d["summary"]["total_interval_child_count"])==128
    return d

def key_from_leaf(r):
    return (int(r["primary_value"]),int(r["secondary_residue"]),int(r["fixed_x61_value"]),int(r["x60_residue"]),int(r["fixed_x60_value"]))

def split_rows():
    out={}
    for r in cold()["leaves"]:
        if r["status"]!="ADAPTIVE_AFFINE_CONDITIONED_SPLIT":
            continue
        key=key_from_leaf(r)
        assert key not in out
        assert int(r["selected_coordinate"]["coordinate_0based"])==58
        iv=[list(map(int,q)) for q in r["intervals"]]
        assert len(iv)==8 and int(r["interval_child_count"])==8
        lo=int(r["selected_coordinate"]["bound"][0]); hi=int(r["selected_coordinate"]["bound"][1])
        flat=[v for a,b in iv for v in range(a,b+1)]
        assert flat==list(range(lo,hi+1))
        out[key]={"intervals":iv,"bound":[lo,hi],"source_canonical_sha256":r["source_canonical_sha256"]}
    assert len(out)==16
    return out

def empty_rows():
    out={}
    for r in cold()["leaves"]:
        if r["status"]!="REAL_EMPTY_NORM_PLUS_P_NECESSARY_CONDITION":
            continue
        key=key_from_leaf(r)
        assert key not in out and int(r["conditioned_residual_energy"][0])<0
        out[key]={"conditioned_residual_energy":list(map(int,r["conditioned_residual_energy"])),"source_canonical_sha256":r["source_canonical_sha256"]}
    assert len(out)==14
    return out

def semantic_source_locks():
    sl=json.loads(RUNKEY.read_text())["source_locks"]
    fields=[
        "local_exact_engine_git_blob","x60_packet_runner_git_blob",
        "gen19_carry_manifest_git_blob","recovery_runner_git_blob",
        "gen23_carry_source_git_blob","gen23_carry_index_git_blob","gen23_carry_verifier_git_blob",
        "gen24_residual_git_blob","gen25_successor_design_spec_git_blob",
        "gen25_successor_cold_diagnostic_git_blob","gen25_successor_cold_verifier_git_blob",
        "gen25_adaptive_cold_output_git_blob",
        "adaptive_x58_preflight_git_blob","adaptive_x58_packet_runner_git_blob",
        "adaptive_x58_packet_verifier_git_blob","adaptive_x58_aggregate_git_blob",
        "adaptive_x58_aggregate_verifier_git_blob",
        "workflow_git_blob","runner_git_blob","stage33_stoll_helper_blob",
        "stage33_picard_marking_blob","stage33_picard_base_rows_blob",
        "hperp_integral_adapter_blob","pairing_prefix_engine_blob"
    ]
    return {f:sl[f] for f in fields}

def build_solver(p,s,x61,r60,x60,interval_index,timeout_ms):
    key=(int(p),int(s),int(x61),int(r60),int(x60))
    rows=split_rows()
    if key not in rows:
        raise ValueError("not Gen25 adaptive split leaf")
    solver,x,y,f,*_=x60parent.build_solver(p,s,x61,r60,timeout_ms)
    solver.add(x[60]==int(x60))
    lo,hi=rows[key]["intervals"][int(interval_index)]
    solver.add(x[58]>=lo,x[58]<=hi)
    return solver,x,y,f,lo,hi

def run_interval(p,s,x61,r60,x60,interval_index,timeout_ms,model_cap,deadline):
    key=(int(p),int(s),int(x61),int(r60),int(x60))
    lo,hi=split_rows()[key]["intervals"][int(interval_index)]
    if time.monotonic()>=deadline:
        d={"status":"NOT_RUN_PACKET_WALL_NO_CREDIT","interval_index":int(interval_index),"x58_interval":[lo,hi],
           "solver":{"engine":"Z3_QF_NIA","z3_version":get_version_string(),"solver_timeout_ms":0,"solver_checks":0,
                     "final_solver_result":None,"reason":"packet wall reached before interval start","model_cap":model_cap,"floating_point_used":False},
           "result":{"complete":False,"integral_known140_nonnegative_solution_count":0,
                     "primitive_known140_nonnegative_candidate_count":0,"primitive_known140_nonnegative_candidates":[]}}
        d["canonical_sha256_without_this_field"]=parent.csha(d)
        return d
    timeout=min(int(timeout_ms),max(1000,int((deadline-time.monotonic())*1000)))
    solver,x,y,f,lo,hi=build_solver(p,s,x61,r60,x60,interval_index,timeout)
    models=0; prim=[]; checks=0; status="PARTIAL_NOT_STARTED"; final=None; reason=None
    while True:
        if time.monotonic()>=deadline:
            status="PARTIAL_PACKET_WALL_NO_CREDIT"; reason="packet wall reached before exhaustive UNSAT"; break
        if models>=model_cap:
            status="PARTIAL_MODEL_CAP_NO_CREDIT"; reason="model cap reached before exhaustive UNSAT"; break
        checks+=1
        res=solver.check()
        if res==unsat:
            status="COMPLETE_EXACT_ADAPTIVE_X58_INTERVAL_ZERO_CREDIT"; final="unsat"; break
        if res==unknown:
            status="PARTIAL_UNKNOWN_NO_CREDIT"; final="unknown"; reason=solver.reason_unknown(); break
        assert res==sat
        m=solver.model()
        xv=[int(m.eval(z,model_completion=True).as_long()) for z in x]
        rec=parent.replay_solution(0,xv)
        assert xv[62]==int(p) and xv[61]==int(x61) and xv[60]==int(x60) and lo<=xv[58]<=hi
        assert [int(m.eval(z,model_completion=True).as_long()) for z in f]==rec["picard_basis_coordinates"]
        models+=1
        if rec["primitive"]:
            prim.append(rec)
        solver.add(Or(*[x[j]!=xv[j] for j in range(63)]))
    prim.sort(key=lambda q:tuple(q["picard_basis_coordinates"]))
    d={"status":status,"interval_index":int(interval_index),"x58_interval":[lo,hi],
       "solver":{"engine":"Z3_QF_NIA","z3_version":get_version_string(),"solver_timeout_ms":timeout,"solver_checks":checks,
                 "final_solver_result":final,"reason":reason,"model_cap":model_cap,"floating_point_used":False},
       "result":{"complete":status=="COMPLETE_EXACT_ADAPTIVE_X58_INTERVAL_ZERO_CREDIT",
                 "integral_known140_nonnegative_solution_count":models,
                 "primitive_known140_nonnegative_candidate_count":len(prim),
                 "primitive_known140_nonnegative_candidates":prim}}
    d["canonical_sha256_without_this_field"]=parent.csha(d)
    return d

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--primary-value",type=int,required=True)
    ap.add_argument("--secondary-residue",type=int,required=True)
    ap.add_argument("--x61-value",type=int,required=True)
    ap.add_argument("--x60-residue",type=int,required=True)
    ap.add_argument("--x60-value",type=int,required=True)
    ap.add_argument("--solver-timeout-ms",type=int,default=300000)
    ap.add_argument("--packet-wall-seconds",type=int,default=2400)
    ap.add_argument("--model-cap",type=int,default=10000)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    key=(a.primary_value,a.secondary_residue,a.x61_value,a.x60_residue,a.x60_value)
    rows=split_rows()
    assert key in rows
    deadline=time.monotonic()+a.packet_wall_seconds
    children=[run_interval(*key,i,a.solver_timeout_ms,a.model_cap,deadline) for i in range(8)]
    complete=all(c["result"]["complete"] for c in children)
    prim=[]; sx=set(); sf=set()
    for c in children:
        for rec in c["result"]["primitive_known140_nonnegative_candidates"]:
            xk=tuple(rec["x_hperp_coordinates"]); fk=tuple(rec["picard_basis_coordinates"])
            assert xk not in sx and fk not in sf
            sx.add(xk); sf.add(fk); prim.append(rec)
    prim.sort(key=lambda q:tuple(q["picard_basis_coordinates"]))
    k=json.loads(RUNKEY.read_text())
    out={"schema":SCHEMA,
         "status":"COMPLETE_EXACT_ADAPTIVE_X58_PACKET_ZERO_CREDIT" if complete else "PARTIAL_ADAPTIVE_X58_PACKET_NO_CREDIT",
         "provenance":{"producing_generation":int(k["generation"]),"producing_mode":k["mode"],
                       "gen25_cold_canonical_sha256":cold()["canonical_sha256_without_this_field"]},
         "semantic_source_locks":semantic_source_locks(),
         "partition":{"primary_value":a.primary_value,"secondary_residue":a.secondary_residue,
                      "fixed_x61_value":a.x61_value,"x60_residue":a.x60_residue,"fixed_x60_value":a.x60_value,
                      "refinement_coordinate_0based":58,"x58_bound":rows[key]["bound"],
                      "x58_intervals":rows[key]["intervals"],"coverage_is_exact_disjoint":True,
                      "source_canonical_sha256":rows[key]["source_canonical_sha256"]},
         "children":children,
         "result":{"complete":complete,"child_count":8,
                   "complete_child_count":sum(c["result"]["complete"] for c in children),
                   "integral_known140_nonnegative_solution_count":sum(c["result"]["integral_known140_nonnegative_solution_count"] for c in children),
                   "primitive_known140_nonnegative_candidate_count":len(prim),
                   "primitive_known140_nonnegative_candidates":prim},
         "credit_firewall":{"numerical_fibration_shell_credit":False,"effectivity_credit":False,"semiampleness_credit":False,
                            "global_fibration_optimum_credit":False,"MB104_complete":False,"receiver_credit":False,
                            "theorem_credit":False,"endpoint_credit":False,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=parent.csha(out)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":out["status"],"children":8,"complete_children":out["result"]["complete_child_count"],
                      "canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))
    raise SystemExit(0 if complete else 2)

if __name__=="__main__":
    main()
