#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_adaptive_x58_packet as runner

def validate_certificate(path,p,s,x61,r60,x60,lo,hi):
 d=json.loads(Path(path).read_text()); assert d['schema']==runner.SCHEMA; cl=d['canonical_sha256_without_this_field']; b=dict(d); b.pop('canonical_sha256_without_this_field'); assert parent.csha(b)==cl
 key=tuple(map(int,(p,s,x61,r60,x60,lo,hi))); rows=runner.residual_rows(); assert key in rows; q=d['partition']; assert (int(q['primary_value']),int(q['secondary_residue']),int(q['fixed_x61_value']),int(q['x60_residue']),int(q['fixed_x60_value']),int(q['parent_x58_interval'][0]),int(q['parent_x58_interval'][1]))==key
 vals=list(range(key[5],key[6]+1)); assert q['x58_singleton_values']==vals and q['coverage_is_exact_disjoint'] is True and int(q['refinement_coordinate_0based'])==58; assert d['semantic_source_locks']==runner.semantic_source_locks(); assert d['provenance']['gen27_residual_parent_canonical_sha256']==rows[key]['canonical_sha256']; assert len(d['children'])==len(vals)
 allc=True; integral=0; prim=[]; sx=set(); sf=set()
 for child,v in zip(d['children'],vals):
  ch=child['canonical_sha256_without_this_field']; cb=dict(child); cb.pop('canonical_sha256_without_this_field'); assert parent.csha(cb)==ch and int(child['x58_value'])==v; allc=allc and child['result']['complete']; rr=child['result']; cs=rr['primitive_known140_nonnegative_candidates']; assert rr['primitive_known140_nonnegative_candidate_count']==len(cs); integral+=int(rr['integral_known140_nonnegative_solution_count'])
  if rr['complete']: assert child['status']=='COMPLETE_EXACT_X58_SINGLETON_ZERO_CREDIT' and child['solver']['final_solver_result']=='unsat' and child['solver']['reason'] is None
  else: assert child['status'] in {'PARTIAL_UNKNOWN_NO_CREDIT','PARTIAL_PACKET_WALL_NO_CREDIT','PARTIAL_MODEL_CAP_NO_CREDIT','NOT_RUN_PACKET_WALL_NO_CREDIT'}
  for rec in cs:
   replay=parent.replay_solution(0,[int(x) for x in rec['x_hperp_coordinates']]); assert replay==rec and replay['primitive'] is True; xv=rec['x_hperp_coordinates']; assert int(xv[62])==key[0] and int(xv[61])==key[2] and int(xv[60])==key[4] and int(xv[58])==v; xk=tuple(xv); fk=tuple(rec['picard_basis_coordinates']); assert xk not in sx and fk not in sf; sx.add(xk); sf.add(fk); prim.append(rec)
 prim.sort(key=lambda r:tuple(r['picard_basis_coordinates'])); assert d['result']['primitive_known140_nonnegative_candidates']==prim; assert d['result']['primitive_known140_nonnegative_candidate_count']==len(prim); assert d['result']['integral_known140_nonnegative_solution_count']==integral; assert d['result']['complete'] is allc; assert d['result']['complete_child_count']==sum(c['result']['complete'] for c in d['children']); assert d['result']['child_count']==len(vals); assert d['status']==('COMPLETE_EXACT_X58_SINGLETON_PACKET_ZERO_CREDIT' if allc else 'PARTIAL_X58_SINGLETON_PACKET_NO_CREDIT'); assert all(v is False for v in d['credit_firewall'].values()); return d

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--certificate',type=Path,required=True)
 for n in ('primary-value','secondary-residue','x61-value','x60-residue','x60-value','x58-lo','x58-hi'): ap.add_argument('--'+n,type=int,required=True)
 a=ap.parse_args(); d=validate_certificate(a.certificate,a.primary_value,a.secondary_residue,a.x61_value,a.x60_residue,a.x60_value,a.x58_lo,a.x58_hi); print(json.dumps({'success':True,'complete':d['result']['complete'],'complete_children':d['result']['complete_child_count'],'child_count':d['result']['child_count'],'primitive_candidates':d['result']['primitive_known140_nonnegative_candidate_count'],'canonical':d['canonical_sha256_without_this_field']},sort_keys=True))
if __name__=='__main__': main()
