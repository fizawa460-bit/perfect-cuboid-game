#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,time
from pathlib import Path
from z3 import Or,sat,unknown,unsat,get_version_string
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_recovery_singleton as secondary

HERE=Path(__file__).resolve().parent
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
GEN19_MANIFEST=HERE/"MB104-000707-GEN19-X61-PACKET-CARRY-MANIFEST.json"
SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_X60_INTERVAL_PACKET_V1"
X60_COORD=60
SHARDS=8

def manifest():
    m=json.loads(GEN19_MANIFEST.read_text())
    assert m["schema"]=="STAGE32_MB104_000707_GEN19_X61_PACKET_CARRY_MANIFEST_V1"
    assert int(m["complete_child_count"])==123 and int(m["incomplete_child_count"])==23
    return m

def residual_leaves():
    return [(int(r["primary_value"]),int(r["secondary_residue"]),int(r["fixed_x61_value"])) for r in manifest()["incomplete_children"]]

def x60_contract():
    p=parent.problem_payload(0,8)
    lo,hi=map(int,p["contract"]["coordinate_bounds"][X60_COORD])
    assert [lo,hi]==[-20,20]
    n=hi-lo+1
    intervals=[[lo+(n*r)//SHARDS,lo+(n*(r+1))//SHARDS-1] for r in range(SHARDS)]
    assert intervals==[[-20,-16],[-15,-11],[-10,-6],[-5,-1],[0,4],[5,9],[10,14],[15,20]]
    return {"coordinate_0based":X60_COORD,"bound":[lo,hi],"shard_count":SHARDS,"intervals":intervals,"coverage_is_exact_disjoint":True,"selection":"DETERMINISTIC_NEXT_MIN_DOMAIN_MAX_ALL140_WEIGHT_EXCLUDING_X62_X61"}

def semantic_source_locks():
    sl=json.loads(RUNKEY.read_text())["source_locks"]
    fields=[
      "local_exact_engine_git_blob","carry_manifest_git_blob","carry_verifier_git_blob","gen15_carry_bundle_git_blob","rehydrate_gen15_carry_git_blob",
      "recovery_runner_git_blob","gen17_carry_manifest_git_blob","gen17_carry_bundle_git_blob","gen17_carry_verifier_git_blob","rehydrate_gen17_carry_git_blob",
      "gen19_carry_manifest_git_blob","gen19_carry_bundle_git_blob","gen19_carry_verifier_git_blob","rehydrate_gen19_carry_git_blob",
      "x60_packet_runner_git_blob","x60_packet_verifier_git_blob","x60_packet_aggregate_git_blob","x60_packet_aggregate_verifier_git_blob","x60_packet_preflight_git_blob",
      "workflow_git_blob","runner_git_blob","stage33_stoll_helper_blob","stage33_picard_marking_blob","stage33_picard_base_rows_blob","hperp_integral_adapter_blob","pairing_prefix_engine_blob"
    ]
    return {f:sl[f] for f in fields}

def build_solver(primary,secondary_residue,x61_value,x60_residue,timeout_ms):
    if (primary,secondary_residue,x61_value) not in set(residual_leaves()): raise ValueError("not retained Gen19 timeout leaf")
    solver,x,y,f,payload,pres,sec=secondary.build_solver(primary,secondary_residue,timeout_ms)
    solver.add(x[61]==int(x61_value))
    contract=x60_contract(); lo,hi=contract["intervals"][int(x60_residue)]
    solver.add(x[X60_COORD]>=lo,x[X60_COORD]<=hi)
    return solver,x,y,f,payload,pres,sec,contract

def run_interval(primary,secondary_residue,x61_value,x60_residue,solver_timeout_ms,model_cap,deadline):
    now=time.monotonic()
    lo,hi=x60_contract()["intervals"][int(x60_residue)]
    if now>=deadline:
        out={"status":"NOT_RUN_PACKET_WALL_NO_CREDIT","x60_residue":int(x60_residue),"x60_interval":[lo,hi],"solver":{"engine":"Z3_QF_NIA","z3_version":get_version_string(),"solver_timeout_ms":0,"solver_checks":0,"final_solver_result":None,"reason":"packet wall reached before interval start","model_cap":model_cap,"floating_point_used":False},"result":{"complete":False,"integral_known140_nonnegative_solution_count":0,"primitive_known140_nonnegative_candidate_count":0,"primitive_known140_nonnegative_candidates":[]}}
        out["canonical_sha256_without_this_field"]=parent.csha(out); return out
    timeout=min(int(solver_timeout_ms),max(1000,int((deadline-now)*1000)))
    solver,x,y,f,payload,pres,sec,contract=build_solver(primary,secondary_residue,x61_value,x60_residue,timeout)
    models=0; primitive=[]; checks=0; status="PARTIAL_NOT_STARTED"; final=None; reason=None
    while True:
        if time.monotonic()>=deadline:
            status="PARTIAL_PACKET_WALL_NO_CREDIT"; reason="packet wall reached before exhaustive UNSAT"; break
        if models>=model_cap:
            status="PARTIAL_MODEL_CAP_NO_CREDIT"; reason="model cap reached before exhaustive UNSAT"; break
        checks+=1; res=solver.check()
        if res==unsat:
            status="COMPLETE_EXACT_X60_INTERVAL_ZERO_CREDIT"; final="unsat"; break
        if res==unknown:
            status="PARTIAL_UNKNOWN_NO_CREDIT"; final="unknown"; reason=solver.reason_unknown(); break
        if res!=sat: raise RuntimeError(str(res))
        model=solver.model(); xv=[int(model.eval(v,model_completion=True).as_long()) for v in x]
        rec=parent.replay_solution(0,xv)
        assert rec["x_hperp_coordinates"][62]==primary and rec["x_hperp_coordinates"][61]==x61_value and lo<=rec["x_hperp_coordinates"][60]<=hi
        assert [int(model.eval(v,model_completion=True).as_long()) for v in f]==rec["picard_basis_coordinates"]
        models+=1
        if rec["primitive"]: primitive.append(rec)
        solver.add(Or(*[x[t]!=xv[t] for t in range(63)]))
    primitive.sort(key=lambda r:tuple(r["picard_basis_coordinates"]))
    out={"status":status,"x60_residue":int(x60_residue),"x60_interval":[lo,hi],"solver":{"engine":"Z3_QF_NIA","z3_version":get_version_string(),"solver_timeout_ms":timeout,"solver_checks":checks,"final_solver_result":final,"reason":reason,"model_cap":model_cap,"floating_point_used":False},"result":{"complete":status=="COMPLETE_EXACT_X60_INTERVAL_ZERO_CREDIT","integral_known140_nonnegative_solution_count":models,"primitive_known140_nonnegative_candidate_count":len(primitive),"primitive_known140_nonnegative_candidates":primitive}}
    out["canonical_sha256_without_this_field"]=parent.csha(out); return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--primary-value",type=int,required=True); ap.add_argument("--secondary-residue",type=int,required=True); ap.add_argument("--x61-value",type=int,required=True); ap.add_argument("--solver-timeout-ms",type=int,default=300000); ap.add_argument("--packet-wall-seconds",type=int,default=2400); ap.add_argument("--model-cap",type=int,default=10000); ap.add_argument("--output",type=Path,required=True); a=ap.parse_args()
    key=(a.primary_value,a.secondary_residue,a.x61_value)
    if key not in set(residual_leaves()): raise SystemExit("leaf is not a retained Gen19 timeout")
    k=json.loads(RUNKEY.read_text()); started=time.monotonic(); deadline=started+a.packet_wall_seconds
    children=[run_interval(*key,r,a.solver_timeout_ms,a.model_cap,deadline) for r in range(SHARDS)]
    complete=all(c["result"]["complete"] for c in children); candidates=[]; sx=set(); sf=set()
    for c in children:
        for rec in c["result"]["primitive_known140_nonnegative_candidates"]:
            xk=tuple(rec["x_hperp_coordinates"]); fk=tuple(rec["picard_basis_coordinates"]); assert xk not in sx and fk not in sf; sx.add(xk); sf.add(fk); candidates.append(rec)
    candidates.sort(key=lambda r:tuple(r["picard_basis_coordinates"]))
    out={"schema":SCHEMA,"status":"COMPLETE_EXACT_X60_INTERVAL_PACKET_ZERO_CREDIT" if complete else "PARTIAL_X60_INTERVAL_PACKET_NO_CREDIT","provenance":{"producing_generation":int(k["generation"]),"producing_mode":k["mode"]},"semantic_source_locks":semantic_source_locks(),"partition":{"primary_coordinate_0based":62,"primary_value":a.primary_value,"secondary_coordinate_0based":61,"secondary_residue":a.secondary_residue,"fixed_x61_value":a.x61_value,**x60_contract()},"solver_policy":{"child_solver_timeout_ms":a.solver_timeout_ms,"packet_wall_seconds":a.packet_wall_seconds,"model_cap_per_child":a.model_cap},"children":children,"result":{"complete":complete,"child_count":len(children),"complete_child_count":sum(1 for c in children if c["result"]["complete"]),"integral_known140_nonnegative_solution_count":sum(int(c["result"]["integral_known140_nonnegative_solution_count"]) for c in children),"primitive_known140_nonnegative_candidate_count":len(candidates),"primitive_known140_nonnegative_candidates":candidates},"credit_firewall":{"numerical_fibration_shell_credit":False,"effectivity_credit":False,"semiampleness_credit":False,"global_fibration_optimum_credit":False,"MB104_complete":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=parent.csha(out); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":out["status"],"primary_value":a.primary_value,"secondary_residue":a.secondary_residue,"x61_value":a.x61_value,"children":len(children),"complete_children":out["result"]["complete_child_count"],"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))
    raise SystemExit(0 if complete else 2)
if __name__=="__main__": main()
