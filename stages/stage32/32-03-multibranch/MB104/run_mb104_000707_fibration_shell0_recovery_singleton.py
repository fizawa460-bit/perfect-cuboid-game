#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,time
from pathlib import Path
from z3 import Or,get_version_string,sat,unknown,unsat
import run_mb104_000707_fibration_shell_local_exact as parent
SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_RESIDUAL_SECONDARY_V2"
HERE=Path(__file__).resolve().parent
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
PRIMARY_VALUES=[-14,-12,-8,0,4,8,12]
GEN15_COMPLETE_VALUES=[-15,-13,-11,-10,-9,-7,-6,-5,-4,-3,-2,-1,1,2,3,5,6,7,9,10,11,13,14,15,16,17,18,19,20]
SECONDARY_SHARD_COUNT=8
GEN13_CARRIED_INTERVAL=[-20,-16]
def semantic_source_locks():
    sl=json.loads(RUNKEY.read_text())["source_locks"]
    return {"parent_local_exact_engine_git_blob":sl["local_exact_engine_git_blob"],"recovery_runner_git_blob":sl["recovery_runner_git_blob"],"recovery_verifier_git_blob":sl["recovery_verifier_git_blob"],"recovery_aggregate_git_blob":sl["recovery_aggregate_git_blob"],"carry_verifier_git_blob":sl["carry_verifier_git_blob"],"carry_manifest_git_blob":sl["carry_manifest_git_blob"],"workflow_git_blob":sl["workflow_git_blob"],"retained_runner_git_blob":sl["runner_git_blob"],"stoll_cuboids_blob":sl["stoll_cuboids_blob"],"stage33_stoll_helper_blob":sl["stage33_stoll_helper_blob"],"stage33_picard_marking_blob":sl["stage33_picard_marking_blob"],"stage33_picard_base_rows_blob":sl["stage33_picard_base_rows_blob"],"hperp_integral_adapter_blob":sl["hperp_integral_adapter_blob"],"pairing_prefix_engine_blob":sl["pairing_prefix_engine_blob"]}
def parent_residue_for_value(value):
    if value not in PRIMARY_VALUES: raise ValueError("primary")
    for r,(lo,hi) in enumerate(parent.split_contract(0,8)["intervals"]):
        if lo<=value<=hi:
            if r==0: raise ValueError("overlap carry")
            return r
    raise ValueError("coverage")
def secondary_contract():
    p=parent.problem_payload(0,8); bounds=p["contract"]["coordinate_bounds"]; domains=[hi-lo+1 for lo,hi in bounds]
    cand=[j for j,n in enumerate(domains) if j!=62 and n>1]
    j=min(cand,key=lambda i:(domains[i],-sum(abs(int(p["linear"][r][i])) for r in range(140)),i))
    lo,hi=map(int,bounds[j]); n=hi-lo+1; intervals=[]
    for r in range(8): intervals.append([lo+(n*r)//8,lo+(n*(r+1))//8-1])
    assert intervals[0][0]==lo and intervals[-1][1]==hi
    for a,b in zip(intervals,intervals[1:]): assert a[1]+1==b[0]
    return {"secondary_coordinate_0based":j,"secondary_coordinate_bound":[lo,hi],"secondary_shard_count":8,"secondary_intervals":intervals,"selection_method":"MIN_DOMAIN_THEN_MAX_ALL140_LINEAR_WEIGHT_EXCLUDING_PRIMARY_X62"}
def build_solver(primary_value,secondary_residue,timeout_ms):
    pres=parent_residue_for_value(primary_value); solver,x,y,f,payload=parent.build_solver(0,pres,shard_count=8,timeout_ms=timeout_ms)
    solver.add(x[62]==primary_value); sec=secondary_contract(); j=sec["secondary_coordinate_0based"]; lo,hi=sec["secondary_intervals"][secondary_residue]
    solver.add(x[j]>=lo,x[j]<=hi); return solver,x,y,f,payload,pres,sec
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--primary-value",type=int,required=True,choices=PRIMARY_VALUES); ap.add_argument("--secondary-residue",type=int,required=True,choices=range(8)); ap.add_argument("--solver-timeout-ms",type=int,default=300000); ap.add_argument("--wall-seconds",type=int,default=2400); ap.add_argument("--model-cap",type=int,default=10000); ap.add_argument("--output",type=Path,required=True); a=ap.parse_args()
    k=json.loads(RUNKEY.read_text()); started=time.monotonic(); solver,x,y,f,payload,pres,sec=build_solver(a.primary_value,a.secondary_residue,a.solver_timeout_ms)
    models=0; primitive=[]; status="PARTIAL_NOT_STARTED"; reason=None; final=None; checks=0
    while True:
        if time.monotonic()-started>=a.wall_seconds: status="PARTIAL_WALL_NO_CREDIT"; reason="local wall reached before exhaustive UNSAT"; break
        if models>=a.model_cap: status="PARTIAL_MODEL_CAP_NO_CREDIT"; reason="model cap reached before exhaustive UNSAT"; break
        checks+=1; res=solver.check()
        if res==unsat: status="COMPLETE_EXACT_SECONDARY_RECOVERY_ZERO_CREDIT"; final="unsat"; break
        if res==unknown: status="PARTIAL_UNKNOWN_NO_CREDIT"; final="unknown"; reason=solver.reason_unknown(); break
        if res!=sat: raise RuntimeError(str(res))
        model=solver.model(); xv=[int(model.eval(v,model_completion=True).as_long()) for v in x]; rec=parent.replay_solution(0,xv)
        j=sec["secondary_coordinate_0based"]; lo,hi=sec["secondary_intervals"][a.secondary_residue]; assert rec["x_hperp_coordinates"][62]==a.primary_value and lo<=rec["x_hperp_coordinates"][j]<=hi
        assert [int(model.eval(v,model_completion=True).as_long()) for v in f]==rec["picard_basis_coordinates"]; models+=1
        if rec["primitive"]: primitive.append(rec)
        solver.add(Or(*[x[t]!=xv[t] for t in range(63)]))
    primitive.sort(key=lambda rec:tuple(rec["picard_basis_coordinates"]))
    out={"schema":SCHEMA,"status":status,"shell_index":0,"provenance":{"producing_generation":int(k["generation"]),"producing_mode":k["mode"]},"semantic_source_locks":semantic_source_locks(),"solver":{"engine":"Z3_QF_NIA","z3_version":get_version_string(),"solver_timeout_ms":a.solver_timeout_ms,"wall_seconds":a.wall_seconds,"model_cap":a.model_cap,"solver_checks":checks,"final_solver_result":final,"reason":reason,"floating_point_used":False},"partition":{"primary_coordinate_0based":62,"primary_value":a.primary_value,"residual_primary_values":PRIMARY_VALUES,"gen15_complete_values":GEN15_COMPLETE_VALUES,"gen13_carried_interval":GEN13_CARRIED_INTERVAL,"parent_shard_count":8,"parent_shard_residue":pres,"parent_shard_interval":payload["contract"]["intervals"][pres],**sec,"secondary_residue":a.secondary_residue,"secondary_interval":sec["secondary_intervals"][a.secondary_residue]},"result":{"complete":status=="COMPLETE_EXACT_SECONDARY_RECOVERY_ZERO_CREDIT","integral_known140_nonnegative_solution_count":models,"primitive_known140_nonnegative_candidate_count":len(primitive),"primitive_known140_nonnegative_candidates":primitive},"credit_firewall":{"numerical_fibration_shell_credit":False,"effectivity_credit":False,"semiampleness_credit":False,"global_fibration_optimum_credit":False,"MB104_complete":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=parent.csha(out); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":status,"primary_value":a.primary_value,"secondary_residue":a.secondary_residue,"secondary_interval":sec["secondary_intervals"][a.secondary_residue],"secondary_coordinate_0based":sec["secondary_coordinate_0based"],"models":models,"primitive_candidates":len(primitive),"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True)); raise SystemExit(0 if out["result"]["complete"] else 2)
if __name__=="__main__": main()
