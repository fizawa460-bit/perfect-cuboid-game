#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,time
from pathlib import Path
from z3 import Or,sat,unknown,unsat,get_version_string
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x60_packet as x60parent
HERE=Path(__file__).resolve().parent
RUNKEY=HERE/"runkeys"/"000707-FIBRATION-ISOTROPIC-SHELLS-V1.json"
MANIFEST=HERE/"MB104-000707-GEN21-X60-PACKET-CARRY-MANIFEST.json"
SCHEMA="STAGE32_MB104_000707_FIBRATION_SHELL0_X60_SINGLETON_PACKET_V1"
def manifest():
    m=json.loads(MANIFEST.read_text()); assert m["schema"]=="STAGE32_MB104_000707_GEN21_X60_PACKET_CARRY_MANIFEST_V1"; assert int(m["complete_interval_child_count"])==122 and int(m["incomplete_interval_child_count"])==62 and int(m["next_x60_singleton_child_count"])==311; return m
def incomplete_intervals():
    return [(int(r["primary_value"]),int(r["secondary_residue"]),int(r["fixed_x61_value"]),int(r["x60_residue"]),tuple(map(int,r["x60_interval"]))) for r in manifest()["incomplete_children"]]
def child_values(p,s,x61,r60):
    rows=[r for r in incomplete_intervals() if r[:4]==(int(p),int(s),int(x61),int(r60))]; assert len(rows)==1
    lo,hi=rows[0][4]; vals=list(range(lo,hi+1)); assert len(vals) in {5,6}; return vals
def semantic_source_locks():
    sl=json.loads(RUNKEY.read_text())["source_locks"]; fields=["local_exact_engine_git_blob","carry_manifest_git_blob","carry_verifier_git_blob","gen15_carry_bundle_git_blob","rehydrate_gen15_carry_git_blob","recovery_runner_git_blob","gen17_carry_manifest_git_blob","gen17_carry_bundle_git_blob","gen17_carry_verifier_git_blob","rehydrate_gen17_carry_git_blob","gen19_carry_manifest_git_blob","gen19_carry_bundle_git_blob","gen19_carry_verifier_git_blob","rehydrate_gen19_carry_git_blob","gen21_carry_manifest_git_blob","gen21_carry_bundle_git_blob","gen21_carry_verifier_git_blob","rehydrate_gen21_carry_git_blob","x60_packet_runner_git_blob","x60_packet_verifier_git_blob","x60_singleton_runner_git_blob","x60_singleton_verifier_git_blob","x60_singleton_aggregate_git_blob","x60_singleton_aggregate_verifier_git_blob","x60_singleton_preflight_git_blob","workflow_git_blob","runner_git_blob","stage33_stoll_helper_blob","stage33_picard_marking_blob","stage33_picard_base_rows_blob","hperp_integral_adapter_blob","pairing_prefix_engine_blob"]; return {f:sl[f] for f in fields}
def run_child(p,s,x61,r60,v,timeout_ms,model_cap,deadline):
    if time.monotonic()>=deadline:
        d={"status":"NOT_RUN_PACKET_WALL_NO_CREDIT","fixed_x60_value":v,"solver":{"engine":"Z3_QF_NIA","z3_version":get_version_string(),"solver_timeout_ms":0,"solver_checks":0,"final_solver_result":None,"reason":"packet wall reached before singleton start","model_cap":model_cap,"floating_point_used":False},"result":{"complete":False,"integral_known140_nonnegative_solution_count":0,"primitive_known140_nonnegative_candidate_count":0,"primitive_known140_nonnegative_candidates":[]}}; d["canonical_sha256_without_this_field"]=parent.csha(d); return d
    timeout=min(timeout_ms,max(1000,int((deadline-time.monotonic())*1000))); solver,x,y,f,*_=x60parent.build_solver(p,s,x61,r60,timeout); solver.add(x[60]==v)
    models=0; prim=[]; checks=0; status="PARTIAL_NOT_STARTED"; final=None; reason=None
    while True:
        if time.monotonic()>=deadline: status="PARTIAL_PACKET_WALL_NO_CREDIT"; reason="packet wall reached before exhaustive UNSAT"; break
        if models>=model_cap: status="PARTIAL_MODEL_CAP_NO_CREDIT"; reason="model cap reached before exhaustive UNSAT"; break
        checks+=1; res=solver.check()
        if res==unsat: status="COMPLETE_EXACT_X60_SINGLETON_ZERO_CREDIT"; final="unsat"; break
        if res==unknown: status="PARTIAL_UNKNOWN_NO_CREDIT"; final="unknown"; reason=solver.reason_unknown(); break
        assert res==sat
        m=solver.model(); xv=[int(m.eval(z,model_completion=True).as_long()) for z in x]; rec=parent.replay_solution(0,xv); assert xv[62]==p and xv[61]==x61 and xv[60]==v and [int(m.eval(z,model_completion=True).as_long()) for z in f]==rec["picard_basis_coordinates"]; models+=1
        if rec["primitive"]: prim.append(rec)
        solver.add(Or(*[x[j]!=xv[j] for j in range(63)]))
    prim.sort(key=lambda q:tuple(q["picard_basis_coordinates"]))
    d={"status":status,"fixed_x60_value":v,"solver":{"engine":"Z3_QF_NIA","z3_version":get_version_string(),"solver_timeout_ms":timeout,"solver_checks":checks,"final_solver_result":final,"reason":reason,"model_cap":model_cap,"floating_point_used":False},"result":{"complete":status=="COMPLETE_EXACT_X60_SINGLETON_ZERO_CREDIT","integral_known140_nonnegative_solution_count":models,"primitive_known140_nonnegative_candidate_count":len(prim),"primitive_known140_nonnegative_candidates":prim}}; d["canonical_sha256_without_this_field"]=parent.csha(d); return d
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--primary-value",type=int,required=True); ap.add_argument("--secondary-residue",type=int,required=True); ap.add_argument("--x61-value",type=int,required=True); ap.add_argument("--x60-residue",type=int,required=True); ap.add_argument("--solver-timeout-ms",type=int,default=300000); ap.add_argument("--packet-wall-seconds",type=int,default=2400); ap.add_argument("--model-cap",type=int,default=10000); ap.add_argument("--output",type=Path,required=True); a=ap.parse_args()
    vals=child_values(a.primary_value,a.secondary_residue,a.x61_value,a.x60_residue); deadline=time.monotonic()+a.packet_wall_seconds; children=[run_child(a.primary_value,a.secondary_residue,a.x61_value,a.x60_residue,v,a.solver_timeout_ms,a.model_cap,deadline) for v in vals]; complete=all(c["result"]["complete"] for c in children); prim=[]; sx=set(); sf=set()
    for c in children:
        for rec in c["result"]["primitive_known140_nonnegative_candidates"]:
            xk=tuple(rec["x_hperp_coordinates"]); fk=tuple(rec["picard_basis_coordinates"]); assert xk not in sx and fk not in sf; sx.add(xk); sf.add(fk); prim.append(rec)
    k=json.loads(RUNKEY.read_text()); out={"schema":SCHEMA,"status":"COMPLETE_EXACT_X60_SINGLETON_PACKET_ZERO_CREDIT" if complete else "PARTIAL_X60_SINGLETON_PACKET_NO_CREDIT","provenance":{"producing_generation":int(k["generation"]),"producing_mode":k["mode"]},"semantic_source_locks":semantic_source_locks(),"partition":{"primary_value":a.primary_value,"secondary_residue":a.secondary_residue,"fixed_x61_value":a.x61_value,"x60_residue":a.x60_residue,"parent_x60_interval":[vals[0],vals[-1]],"x60_singleton_values":vals,"coverage_is_exact_disjoint":True},"children":children,"result":{"complete":complete,"child_count":len(children),"complete_child_count":sum(c["result"]["complete"] for c in children),"integral_known140_nonnegative_solution_count":sum(c["result"]["integral_known140_nonnegative_solution_count"] for c in children),"primitive_known140_nonnegative_candidate_count":len(prim),"primitive_known140_nonnegative_candidates":prim},"credit_firewall":{"numerical_fibration_shell_credit":False,"effectivity_credit":False,"semiampleness_credit":False,"global_fibration_optimum_credit":False,"MB104_complete":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"merge_authorized":False}}; out["canonical_sha256_without_this_field"]=parent.csha(out); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n"); print(json.dumps({"status":out["status"],"children":len(children),"complete_children":out["result"]["complete_child_count"],"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True)); raise SystemExit(0 if complete else 2)
if __name__=="__main__": main()
