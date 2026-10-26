#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess,sys,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
REPO=HERE.parents[5]
RUNKEY=HERE/'runkeys'/'000707-FIBRATION-ISOTROPIC-SHELLS-V1.json'
DERIVE=HERE/'derive_mb104_000707_gen30_adaptive_affine_cold.py'
CERT=HERE/'MB104-000707-GEN30-ADAPTIVE-AFFINE-COLD.json'
RESIDUAL=HERE/'MB104-000707-GEN30-X58-SINGLETON-RESIDUAL49.json'
CARRY_SOURCE=HERE/'MB104-000707-GEN29-X58-SINGLETON-CARRY-SOURCE.json'
CARRY_INDEX=HERE/'MB104-000707-GEN29-X58-SINGLETON-CARRY-INDEX.json'
CARRY_VERIFIER=HERE/'verify_mb104_000707_gen29_x58_singleton_carry.py'
SCHEMA='STAGE32_MB104_000707_GEN30_ADAPTIVE_AFFINE_COLD_V1'
def blob(p): return subprocess.check_output(['git','hash-object',str(p)],cwd=REPO,text=True).strip()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--certificate',type=Path,default=CERT); a=ap.parse_args()
 k=json.loads(RUNKEY.read_text()); sl=k['source_locks']
 for f,p in {'gen29_x58_singleton_carry_source_git_blob':CARRY_SOURCE,'gen29_x58_singleton_carry_index_git_blob':CARRY_INDEX,'gen29_x58_singleton_carry_verifier_git_blob':CARRY_VERIFIER,'gen30_residual49_git_blob':RESIDUAL,'gen30_adaptive_affine_deriver_git_blob':DERIVE}.items():
  got=blob(p)
  if got!=sl[f]: raise SystemExit(f'source-lock mismatch: {f}: {got} != {sl[f]}')
 if int(k['generation'])!=30 or k['mode']!='COLD' or k['armed'] is not False: raise SystemExit('Gen30 COLD/unarmed contract drift')
 if k['execution_gate']['automatic_execution_authorized'] is not False or k['execution_gate']['current_head_execution_blocked'] is not True: raise SystemExit('Gen30 execution gate is not fail-closed')
 d=json.loads(a.certificate.read_text())
 if d['schema']!=SCHEMA or d['status']!='COLD_ADAPTIVE_AFFINE_SUCCESSOR_DESIGNED_NO_HEAVY_EXECUTION_NO_CREDIT': raise SystemExit('certificate identity')
 if d['source_generation']!=29 or d['source_execution_head']!='090cf1ce97819736f9be09a9a96fb6421349acad' or d['source_workflow_run_id']!=36092356653: raise SystemExit('source execution identity drift')
 if [d['carried_complete_x60_singletons'],d['necessary_condition_empty_leaf_count_from_gen25'],d['carried_complete_x58_intervals_from_gen27'],d['carried_complete_x58_singletons_from_gen29'],d['residual_timeout_singleton_count']]!=[281,14,74,111,49]: raise SystemExit('population drift')
 if d['fixed_coordinates_0based']!=[62,61,60,58] or d['forbidden_split_coordinates_0based']!=[58,59,60,61,62] or len(d['leaves'])!=49: raise SystemExit('conditioned partition contract drift')
 if d['heavy_surface_present'] or d['heavy_armed'] or d['execution_authorized'] or any(bool(v) for v in d['credit_firewall'].values()): raise SystemExit('credit/heavy firewall')
 total=0; hist={}; identities=set()
 for leaf in d['leaves']:
  ident=(int(leaf['primary_value']),int(leaf['secondary_residue']),int(leaf['fixed_x61_value']),int(leaf['x60_residue']),int(leaf['fixed_x60_value']),int(leaf['fixed_x58_value']),leaf['source_canonical_sha256'])
  if ident in identities: raise SystemExit('duplicate residual singleton')
  identities.add(ident)
  if leaf['status']=='ADAPTIVE_AFFINE_CONDITIONED_SPLIT':
   sel=leaf['selected_coordinate']; j=int(sel['coordinate_0based'])
   if j in {58,59,60,61,62}: raise SystemExit('forbidden successor coordinate')
   lo,hi=map(int,sel['bound'])
   if int(sel['domain_size'])!=hi-lo+1: raise SystemExit('domain mismatch')
   ints=leaf['intervals']
   if not ints or int(ints[0][0])!=lo or int(ints[-1][1])!=hi: raise SystemExit('endpoint coverage')
   for left,right in zip(ints,ints[1:]):
    if int(left[1])+1!=int(right[0]): raise SystemExit('gap/overlap')
   if int(leaf['interval_child_count'])!=len(ints): raise SystemExit('interval count mismatch')
   total+=len(ints); hist[str(j)]=hist.get(str(j),0)+1
  elif leaf['selected_coordinate'] is not None or leaf['intervals'] or int(leaf['interval_child_count'])!=0: raise SystemExit('empty-leaf encoding')
 s=d['summary']
 if int(s['split_leaf_count'])+int(s['necessary_condition_empty_leaf_count'])!=49 or int(s['total_interval_child_count'])!=total or total>392 or s['selected_coordinate_histogram']!=hist: raise SystemExit('summary mismatch')
 if hist!={'56':49} or int(s['split_leaf_count'])!=49 or int(s['necessary_condition_empty_leaf_count'])!=0 or total!=392 or int(s['maximum_conditional_domain'])!=37 or s['median_conditional_domain']!=19: raise SystemExit('retained Gen30 result drift')
 with tempfile.TemporaryDirectory() as td:
  out=Path(td)/'replay.json'
  subprocess.run([sys.executable,str(DERIVE),'--output',str(out)],cwd=HERE,text=True,capture_output=True,check=True)
  if d!=json.loads(out.read_text()): raise SystemExit('deterministic exact replay mismatch')
 print(json.dumps({'success':True,'generation':30,'residual_timeout_singletons':49,'selected_coordinate_histogram':hist,'total_interval_child_count':total,'heavy_authorized':False,'credit':False},sort_keys=True))
if __name__=='__main__': main()
