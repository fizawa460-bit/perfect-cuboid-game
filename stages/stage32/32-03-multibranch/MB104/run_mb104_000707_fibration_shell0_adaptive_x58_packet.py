#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,time
from pathlib import Path
from z3 import Or,sat,unknown,unsat,get_version_string
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_x60_packet as x60parent
HERE=Path(__file__).resolve().parent
RUNKEY=HERE/'runkeys'/'000707-FIBRATION-ISOTROPIC-SHELLS-V1.json'
RESIDUAL=HERE/'MB104-000707-GEN28-ADAPTIVE-X58-RESIDUAL54.json'
SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_SINGLETON_PACKET_V1'

def residual():
 d=json.loads(RESIDUAL.read_text()); assert d['schema']=='STAGE32_MB104_000707_GEN28_ADAPTIVE_X58_RESIDUAL54_V1'
 assert d['source_generation']==27 and d['source_execution_head']=='1f69a43a49d05b3e8c5fa87c812efe974c9b20e5' and d['source_workflow_run_id']==36066791252
 assert d['complete_child_count']==74 and d['residual_timeout_child_count']==54 and d['credit'] is False
 assert len(d['residual_children'])==54
 return d

def row_key(r):
 return (int(r['primary_value']),int(r['secondary_residue']),int(r['fixed_x61_value']),int(r['x60_residue']),int(r['fixed_x60_value']),int(r['x58_interval'][0]),int(r['x58_interval'][1]))

def residual_rows():
 out={}
 for r in residual()['residual_children']:
  k=row_key(r); assert k not in out and r['solver_result']=='unknown' and r['reason']=='timeout'; out[k]=r
 assert len(out)==54 and sum(k[6]-k[5]+1 for k in out)==160
 return out

def semantic_source_locks():
 sl=json.loads(RUNKEY.read_text())['source_locks']
 fields=['local_exact_engine_git_blob','x60_packet_runner_git_blob','gen23_carry_source_git_blob','gen23_carry_index_git_blob','gen23_carry_verifier_git_blob','gen25_adaptive_cold_output_git_blob','gen27_adaptive_carry_source_git_blob','gen27_adaptive_carry_index_git_blob','gen27_adaptive_carry_verifier_git_blob','gen28_adaptive_x58_residual_git_blob','adaptive_x58_preflight_git_blob','adaptive_x58_packet_runner_git_blob','adaptive_x58_packet_verifier_git_blob','adaptive_x58_aggregate_git_blob','adaptive_x58_aggregate_verifier_git_blob','workflow_git_blob','runner_git_blob','stage33_stoll_helper_blob','stage33_picard_marking_blob','stage33_picard_base_rows_blob','hperp_integral_adapter_blob','pairing_prefix_engine_blob']
 return {f:sl[f] for f in fields}

def build_solver(p,s,x61,r60,x60,x58,timeout_ms):
 solver,x,y,f,*_=x60parent.build_solver(p,s,x61,r60,timeout_ms); solver.add(x[60]==int(x60),x[58]==int(x58)); return solver,x,y,f

def run_value(p,s,x61,r60,x60,x58,timeout_ms,model_cap,deadline):
 if time.monotonic()>=deadline:
  status='NOT_RUN_PACKET_WALL_NO_CREDIT'; final=None; reason='packet wall reached before singleton start'; checks=models=0; prim=[]; timeout=0
 else:
  timeout=min(int(timeout_ms),max(1000,int((deadline-time.monotonic())*1000))); solver,x,y,f=build_solver(p,s,x61,r60,x60,x58,timeout); models=checks=0; prim=[]; status='PARTIAL_NOT_STARTED'; final=reason=None
  while True:
   if time.monotonic()>=deadline: status='PARTIAL_PACKET_WALL_NO_CREDIT'; reason='packet wall reached before exhaustive UNSAT'; break
   if models>=model_cap: status='PARTIAL_MODEL_CAP_NO_CREDIT'; reason='model cap reached before exhaustive UNSAT'; break
   checks+=1; res=solver.check()
   if res==unsat: status='COMPLETE_EXACT_X58_SINGLETON_ZERO_CREDIT'; final='unsat'; break
   if res==unknown: status='PARTIAL_UNKNOWN_NO_CREDIT'; final='unknown'; reason=solver.reason_unknown(); break
   assert res==sat
   m=solver.model(); xv=[int(m.eval(z,model_completion=True).as_long()) for z in x]; rec=parent.replay_solution(0,xv)
   assert xv[62]==int(p) and xv[61]==int(x61) and xv[60]==int(x60) and xv[58]==int(x58)
   assert [int(m.eval(z,model_completion=True).as_long()) for z in f]==rec['picard_basis_coordinates']; models+=1
   if rec['primitive']: prim.append(rec)
   solver.add(Or(*[x[j]!=xv[j] for j in range(63)]))
 prim.sort(key=lambda q:tuple(q['picard_basis_coordinates']))
 d={'status':status,'x58_value':int(x58),'solver':{'engine':'Z3_QF_NIA','z3_version':get_version_string(),'solver_timeout_ms':timeout,'solver_checks':checks,'final_solver_result':final,'reason':reason,'model_cap':model_cap,'floating_point_used':False},'result':{'complete':status=='COMPLETE_EXACT_X58_SINGLETON_ZERO_CREDIT','integral_known140_nonnegative_solution_count':models,'primitive_known140_nonnegative_candidate_count':len(prim),'primitive_known140_nonnegative_candidates':prim}}
 d['canonical_sha256_without_this_field']=parent.csha(d); return d

def main():
 ap=argparse.ArgumentParser()
 for n in ('primary-value','secondary-residue','x61-value','x60-residue','x60-value','x58-lo','x58-hi'): ap.add_argument('--'+n,type=int,required=True)
 ap.add_argument('--solver-timeout-ms',type=int,default=300000); ap.add_argument('--packet-wall-seconds',type=int,default=2400); ap.add_argument('--model-cap',type=int,default=10000); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
 key=(a.primary_value,a.secondary_residue,a.x61_value,a.x60_residue,a.x60_value,a.x58_lo,a.x58_hi); rows=residual_rows(); assert key in rows
 deadline=time.monotonic()+a.packet_wall_seconds; vals=list(range(a.x58_lo,a.x58_hi+1)); children=[run_value(*key[:5],v,a.solver_timeout_ms,a.model_cap,deadline) for v in vals]
 complete=all(c['result']['complete'] for c in children); prim=[]; sx=set(); sf=set()
 for c in children:
  for rec in c['result']['primitive_known140_nonnegative_candidates']:
   xk=tuple(rec['x_hperp_coordinates']); fk=tuple(rec['picard_basis_coordinates']); assert xk not in sx and fk not in sf; sx.add(xk); sf.add(fk); prim.append(rec)
 prim.sort(key=lambda q:tuple(q['picard_basis_coordinates'])); k=json.loads(RUNKEY.read_text())
 out={'schema':SCHEMA,'status':'COMPLETE_EXACT_X58_SINGLETON_PACKET_ZERO_CREDIT' if complete else 'PARTIAL_X58_SINGLETON_PACKET_NO_CREDIT','provenance':{'producing_generation':int(k['generation']),'producing_mode':k['mode'],'gen27_residual_parent_canonical_sha256':rows[key]['canonical_sha256']},'semantic_source_locks':semantic_source_locks(),'partition':{'primary_value':key[0],'secondary_residue':key[1],'fixed_x61_value':key[2],'x60_residue':key[3],'fixed_x60_value':key[4],'refinement_coordinate_0based':58,'parent_x58_interval':[key[5],key[6]],'x58_singleton_values':vals,'coverage_is_exact_disjoint':True},'children':children,'result':{'complete':complete,'child_count':len(children),'complete_child_count':sum(c['result']['complete'] for c in children),'integral_known140_nonnegative_solution_count':sum(c['result']['integral_known140_nonnegative_solution_count'] for c in children),'primitive_known140_nonnegative_candidate_count':len(prim),'primitive_known140_nonnegative_candidates':prim},'credit_firewall':{'numerical_fibration_shell_credit':False,'effectivity_credit':False,'semiampleness_credit':False,'global_fibration_optimum_credit':False,'MB104_complete':False,'receiver_credit':False,'theorem_credit':False,'endpoint_credit':False,'merge_authorized':False}}
 out['canonical_sha256_without_this_field']=parent.csha(out); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps({'status':out['status'],'children':len(children),'complete_children':out['result']['complete_child_count'],'canonical':out['canonical_sha256_without_this_field']},sort_keys=True)); raise SystemExit(0 if complete else 2)
if __name__=='__main__': main()
