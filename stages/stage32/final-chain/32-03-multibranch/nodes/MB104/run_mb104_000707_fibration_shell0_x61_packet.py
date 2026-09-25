#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,time
from pathlib import Path
from z3 import Or,sat,unknown,unsat,get_version_string
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_recovery_singleton as secondary

HERE=Path(__file__).resolve().parent
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
GEN17_MANIFEST=HERE/"MB104-000707-GEN17-SECONDARY-CARRY-MANIFEST.json"
SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_X61_SINGLETON_PACKET_V1"

def manifest():
    m=json.loads(GEN17_MANIFEST.read_text())
    assert m["schema"]=="STAGE32_MB104_000707_GEN17_SECONDARY_CARRY_MANIFEST_V1"
    return m

def incomplete_cells():
    return [tuple(map(int,x)) for x in manifest()["incomplete_cells"]]

def semantic_source_locks():
    sl=json.loads(RUNKEY.read_text())["source_locks"]
    fields=["local_exact_engine_git_blob","carry_manifest_git_blob","carry_verifier_git_blob","gen15_carry_bundle_git_blob","rehydrate_gen15_carry_git_blob","recovery_runner_git_blob","gen17_carry_manifest_git_blob","gen17_carry_bundle_git_blob","gen17_carry_verifier_git_blob","rehydrate_gen17_carry_git_blob","x61_packet_runner_git_blob","x61_packet_verifier_git_blob","x61_packet_aggregate_git_blob","x61_packet_aggregate_verifier_git_blob","x61_packet_preflight_git_blob","workflow_git_blob","runner_git_blob","stage33_stoll_helper_blob","stage33_picard_marking_blob","stage33_picard_base_rows_blob","hperp_integral_adapter_blob","pairing_prefix_engine_blob"]
    return {f:sl[f] for f in fields}

def child_values(primary,secondary_residue):
    if (primary,secondary_residue) not in set(incomplete_cells()): raise ValueError("not Gen17 incomplete cell")
    lo,hi=map(int,manifest()["secondary_intervals"][secondary_residue])
    return list(range(lo,hi+1))

def run_child(primary,secondary_residue,x61_value,solver_timeout_ms,model_cap,deadline):
    now=time.monotonic()
    if now>=deadline:
        out={"status":"NOT_RUN_PACKET_WALL_NO_CREDIT","fixed_x61_value":x61_value,"solver":{"engine":"Z3_QF_NIA","z3_version":get_version_string(),"solver_timeout_ms":0,"solver_checks":0,"final_solver_result":None,"reason":"packet wall reached before child start","model_cap":model_cap,"floating_point_used":False},"result":{"complete":False,"integral_known140_nonnegative_solution_count":0,"primitive_known140_nonnegative_candidate_count":0,"primitive_known140_nonnegative_candidates":[]}}
        out["canonical_sha256_without_this_field"]=parent.csha(out); return out
    timeout=min(int(solver_timeout_ms),max(1000,int((deadline-now)*1000)))
    solver,x,y,f,payload,pres,sec=secondary.build_solver(primary,secondary_residue,timeout)
    solver.add(x[61]==int(x61_value))
    models=0; primitive=[]; checks=0; status="PARTIAL_NOT_STARTED"; final=None; reason=None
    while True:
        if time.monotonic()>=deadline:
            status="PARTIAL_PACKET_WALL_NO_CREDIT"; reason="packet wall reached before exhaustive UNSAT"; break
        if models>=model_cap:
            status="PARTIAL_MODEL_CAP_NO_CREDIT"; reason="model cap reached before exhaustive UNSAT"; break
        checks+=1; res=solver.check()
        if res==unsat:
            status="COMPLETE_EXACT_X61_SINGLETON_ZERO_CREDIT"; final="unsat"; break
        if res==unknown:
            status="PARTIAL_UNKNOWN_NO_CREDIT"; final="unknown"; reason=solver.reason_unknown(); break
        if res!=sat: raise RuntimeError(str(res))
        model=solver.model(); xv=[int(model.eval(v,model_completion=True).as_long()) for v in x]
        rec=parent.replay_solution(0,xv)
        assert rec["x_hperp_coordinates"][62]==primary and rec["x_hperp_coordinates"][61]==x61_value
        assert [int(model.eval(v,model_completion=True).as_long()) for v in f]==rec["picard_basis_coordinates"]
        models+=1
        if rec["primitive"]: primitive.append(rec)
        solver.add(Or(*[x[t]!=xv[t] for t in range(63)]))
    primitive.sort(key=lambda r:tuple(r["picard_basis_coordinates"]))
    out={"status":status,"fixed_x61_value":int(x61_value),"solver":{"engine":"Z3_QF_NIA","z3_version":get_version_string(),"solver_timeout_ms":timeout,"solver_checks":checks,"final_solver_result":final,"reason":reason,"model_cap":model_cap,"floating_point_used":False},"result":{"complete":status=="COMPLETE_EXACT_X61_SINGLETON_ZERO_CREDIT","integral_known140_nonnegative_solution_count":models,"primitive_known140_nonnegative_candidate_count":len(primitive),"primitive_known140_nonnegative_candidates":primitive}}
    out["canonical_sha256_without_this_field"]=parent.csha(out); return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--primary-value",type=int,required=True); ap.add_argument("--secondary-residue",type=int,required=True,choices=range(8)); ap.add_argument("--solver-timeout-ms",type=int,default=300000); ap.add_argument("--packet-wall-seconds",type=int,default=2400); ap.add_argument("--model-cap",type=int,default=10000); ap.add_argument("--output",type=Path,required=True); a=ap.parse_args()
    if (a.primary_value,a.secondary_residue) not in set(incomplete_cells()): raise SystemExit("cell is not a Gen17 UNKNOWN")
    k=json.loads(RUNKEY.read_text()); started=time.monotonic(); deadline=started+a.packet_wall_seconds
    vals=child_values(a.primary_value,a.secondary_residue); children=[]
    for v in vals: children.append(run_child(a.primary_value,a.secondary_residue,v,a.solver_timeout_ms,a.model_cap,deadline))
    complete=all(c["result"]["complete"] for c in children)
    candidates=[]; sx=set(); sf=set()
    for c in children:
        for rec in c["result"]["primitive_known140_nonnegative_candidates"]:
            xk=tuple(rec["x_hperp_coordinates"]); fk=tuple(rec["picard_basis_coordinates"])
            assert xk not in sx and fk not in sf; sx.add(xk); sf.add(fk); candidates.append(rec)
    candidates.sort(key=lambda r:tuple(r["picard_basis_coordinates"]))
    interval=manifest()["secondary_intervals"][a.secondary_residue]
    out={"schema":SCHEMA,"status":"COMPLETE_EXACT_X61_SINGLETON_PACKET_ZERO_CREDIT" if complete else "PARTIAL_X61_SINGLETON_PACKET_NO_CREDIT","provenance":{"producing_generation":int(k["generation"]),"producing_mode":k["mode"]},"semantic_source_locks":semantic_source_locks(),"partition":{"primary_coordinate_0based":62,"primary_value":a.primary_value,"secondary_coordinate_0based":61,"secondary_residue":a.secondary_residue,"parent_secondary_interval":interval,"x61_singleton_values":vals,"coverage_is_exact_disjoint":True},"solver_policy":{"child_solver_timeout_ms":a.solver_timeout_ms,"packet_wall_seconds":a.packet_wall_seconds,"model_cap_per_child":a.model_cap},"children":children,"result":{"complete":complete,"child_count":len(children),"complete_child_count":sum(1 for c in children if c["result"]["complete"]),"integral_known140_nonnegative_solution_count":sum(int(c["result"]["integral_known140_nonnegative_solution_count"]) for c in children),"primitive_known140_nonnegative_candidate_count":len(candidates),"primitive_known140_nonnegative_candidates":candidates},"credit_firewall":{"numerical_fibration_shell_credit":False,"effectivity_credit":False,"semiampleness_credit":False,"global_fibration_optimum_credit":False,"MB104_complete":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=parent.csha(out); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":out["status"],"primary_value":a.primary_value,"secondary_residue":a.secondary_residue,"children":len(children),"complete_children":out["result"]["complete_child_count"],"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))
    raise SystemExit(0 if complete else 2)
if __name__=="__main__": main()
