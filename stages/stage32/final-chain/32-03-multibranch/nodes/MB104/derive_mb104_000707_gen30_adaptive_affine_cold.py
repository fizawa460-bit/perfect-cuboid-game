#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib,json,subprocess
from fractions import Fraction
from pathlib import Path
from sympy import Matrix

HERE=Path(__file__).resolve().parent
REPO=HERE.parents[5]
RESIDUAL=HERE/'MB104-000707-GEN30-X58-SINGLETON-RESIDUAL49.json'
CARRY_SOURCE=HERE/'MB104-000707-GEN29-X58-SINGLETON-CARRY-SOURCE.json'
CARRY_INDEX=HERE/'MB104-000707-GEN29-X58-SINGLETON-CARRY-INDEX.json'
CARRY_VERIFIER=HERE/'verify_mb104_000707_gen29_x58_singleton_carry.py'
PARENT=HERE/'run_mb104_000707_fibration_shell_local_exact.py'
RETAINED=HERE/'run_mb104_000707_fibration_isotropic_shells.py'
SCHEMA='STAGE32_MB104_000707_GEN30_ADAPTIVE_AFFINE_COLD_V1'
FIXED=(62,61,60,58)
FORBIDDEN_SPLIT={58,59,60,61,62}
MAX_SHARDS=8
EXPECTED={
 'gen29_carry_source_git_blob':'8eb2dfff63eddc6b96a75e0491a0379846f1fd43',
 'gen29_carry_index_git_blob':'17698edea9440fb32e6d3a1768e574407ac80713',
 'gen29_carry_verifier_git_blob':'3dd5f1d9115a20491215b6fa53be384bbc9dc58a',
 'gen30_residual49_git_blob':'d73ebdbc925bd6d2d522c81d2ce1c3c8f4d33563',
 'local_exact_engine_git_blob':'ee651d257ddec5d606033651cf3d4ae1e773f52a',
 'runner_git_blob':'cae7d170990128bbf1a80ed840b4c0b4a2b84cd4',
}
PATHS={
 'gen29_carry_source_git_blob':CARRY_SOURCE,
 'gen29_carry_index_git_blob':CARRY_INDEX,
 'gen29_carry_verifier_git_blob':CARRY_VERIFIER,
 'gen30_residual49_git_blob':RESIDUAL,
 'local_exact_engine_git_blob':PARENT,
 'runner_git_blob':RETAINED,
}

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def frac(v): return Fraction(int(v.p),int(v.q)) if hasattr(v,'p') else Fraction(int(v),1)
def fpair(v): return [int(v.numerator),int(v.denominator)]
def git_blob(path): return subprocess.check_output(['git','hash-object',str(path)],cwd=REPO,text=True).strip()

def lock_before_exec():
 verified={}
 for field,path in PATHS.items():
  got=git_blob(path); want=EXPECTED[field]
  if got!=want: raise SystemExit(f'source-lock mismatch before exec: {field}: {got} != {want}')
  verified[field]=got
 return verified

def residual_rows():
 carry=importlib.import_module('verify_mb104_000707_gen29_x58_singleton_carry')
 carry.decode_carry()
 raw=json.loads(RESIDUAL.read_text())
 assert raw['schema']=='STAGE32_MB104_000707_GEN30_X58_SINGLETON_RESIDUAL49_V1'
 assert raw['source_generation']==29 and raw['source_execution_head']=='090cf1ce97819736f9be09a9a96fb6421349acad' and raw['source_workflow_run_id']==36092356653
 assert raw['complete_singleton_child_count']==111 and raw['residual_timeout_singleton_count']==49
 assert raw['prior_carried_complete_x60_singleton_count']==281 and raw['prior_necessary_condition_empty_leaf_count']==14 and raw['prior_carried_complete_x58_interval_count']==74
 rows=raw['residual_singletons']; assert len(rows)==49
 seen=set()
 for row in rows:
  assert row['solver_result']=='unknown' and row['reason']=='timeout'
  k=(int(row['primary_value']),int(row['secondary_residue']),int(row['fixed_x61_value']),int(row['x60_residue']),int(row['fixed_x60_value']),int(row['fixed_x58_value']))
  assert k not in seen; seen.add(k)
 return rows

def build_context(parent):
 p=parent.problem_payload(0,8); q=p['q']; prow=p['prow']
 free=[j for j in range(63) if j not in FIXED]; pos={j:k for k,j in enumerate(free)}
 A=Matrix([[int(q[i][j]) for j in free] for i in free]); Ainv=A.inv()
 a=Matrix([int(prow[i]) for i in free]); ainv=Ainv*a; s=frac((a.T*ainv)[0])
 if s<=0: raise SystemExit('nonpositive affine dual norm')
 linear=p['linear']; weights={j:sum(abs(int(linear[r][j])) for r in range(140)) for j in range(63)}
 return {'p':p,'q':q,'prow':prow,'free':free,'pos':pos,'Ainv':Ainv,'a':a,'ainv':ainv,'s':s,'weights':weights,'global_bounds':p['contract']['coordinate_bounds'],'norm':int(p['shell']['hperp_norm']),'pc':int(p['pc'])}

def exact_leaf_contract(ctx,row):
 q=ctx['q']; prow=ctx['prow']; free=ctx['free']; pos=ctx['pos']; Ainv=ctx['Ainv']; a=ctx['a']; ainv=ctx['ainv']; s=ctx['s']
 fixed={62:int(row['primary_value']),61:int(row['fixed_x61_value']),60:int(row['fixed_x60_value']),58:int(row['fixed_x58_value'])}
 d=Matrix([sum(int(q[i][f])*fixed[f] for f in FIXED) for i in free])
 c=sum(fixed[i]*int(q[i][j])*fixed[j] for i in FIXED for j in FIXED)
 rhs=ctx['pc']-sum(int(prow[f])*fixed[f] for f in FIXED)
 dinv=Ainv*d; R=Fraction(ctx['norm']-c,1)+frac((d.T*dinv)[0]); h=Fraction(rhs,1)+frac((a.T*dinv)[0])
 residual_energy=R-h*h/s; base_center=-dinv+ainv*(h/s)
 identity={
  'primary_value':fixed[62],'secondary_residue':int(row['secondary_residue']),'fixed_x61_value':fixed[61],
  'x60_residue':int(row['x60_residue']),'fixed_x60_value':fixed[60],'fixed_x58_value':fixed[58],
  'source_canonical_sha256':row['canonical_sha256']
 }
 if residual_energy<0:
  return {**identity,'status':'REAL_EMPTY_NORM_PLUS_P_NECESSARY_CONDITION','conditioned_residual_energy':fpair(residual_energy),'selected_coordinate':None,'intervals':[],'interval_child_count':0}
 candidates=[]
 for j in free:
  if j in FORBIDDEN_SPLIT: continue
  k=pos[j]; variance=frac(Ainv[k,k])-frac(ainv[k])*frac(ainv[k])/s
  if variance<0: raise SystemExit(f'negative conditioned variance at x{j}')
  radius2=residual_energy*variance; center=frac(base_center[k]); glo,ghi=map(int,ctx['global_bounds'][j])
  values=[v for v in range(glo,ghi+1) if (Fraction(v,1)-center)**2<=radius2]
  if values:
   candidates.append({'coordinate_0based':j,'bound':[values[0],values[-1]],'domain_size':len(values),'all140_weight':ctx['weights'][j],'center':fpair(center),'radius_squared':fpair(radius2)})
 if not candidates:
  return {**identity,'status':'INTEGER_PROJECTION_EMPTY_NORM_PLUS_P_NECESSARY_CONDITION','conditioned_residual_energy':fpair(residual_energy),'selected_coordinate':None,'intervals':[],'interval_child_count':0}
 chosen=min(candidates,key=lambda z:(z['domain_size'],-z['all140_weight'],z['coordinate_0based']))
 lo,hi=chosen['bound']; n=hi-lo+1; shard_count=min(MAX_SHARDS,n)
 intervals=[[lo+(n*r)//shard_count,lo+(n*(r+1))//shard_count-1] for r in range(shard_count)]
 assert intervals[0][0]==lo and intervals[-1][1]==hi
 for left,right in zip(intervals,intervals[1:]): assert left[1]+1==right[0]
 return {**identity,'status':'ADAPTIVE_AFFINE_CONDITIONED_SPLIT','conditioned_residual_energy':fpair(residual_energy),'selected_coordinate':chosen,'intervals':intervals,'interval_child_count':len(intervals)}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,required=True); a=ap.parse_args()
 verified=lock_before_exec(); rows=residual_rows()
 parent=importlib.import_module('run_mb104_000707_fibration_shell_local_exact'); ctx=build_context(parent)
 leaves=[exact_leaf_contract(ctx,row) for row in rows]; split=[r for r in leaves if r['status']=='ADAPTIVE_AFFINE_CONDITIONED_SPLIT']; empty=[r for r in leaves if r['status']!='ADAPTIVE_AFFINE_CONDITIONED_SPLIT']
 hist={}; domains=[]; total_children=0
 for row in split:
  j=str(int(row['selected_coordinate']['coordinate_0based'])); hist[j]=hist.get(j,0)+1
  domains.append(int(row['selected_coordinate']['domain_size'])); total_children+=int(row['interval_child_count'])
 domains.sort(); median=None
 if domains:
  m=len(domains); median=domains[m//2] if m%2 else [domains[m//2-1],domains[m//2]]
 out={
  'schema':SCHEMA,'status':'COLD_ADAPTIVE_AFFINE_SUCCESSOR_DESIGNED_NO_HEAVY_EXECUTION_NO_CREDIT',
  'source_generation':29,'source_execution_head':'090cf1ce97819736f9be09a9a96fb6421349acad','source_workflow_run_id':36092356653,
  'carried_complete_x60_singletons':281,'necessary_condition_empty_leaf_count_from_gen25':14,'carried_complete_x58_intervals_from_gen27':74,'carried_complete_x58_singletons_from_gen29':111,
  'residual_timeout_singleton_count':49,'recompute_carried_complete_regions':False,'fixed_coordinates_0based':list(FIXED),'retired_successor_coordinate_0based':59,
  'forbidden_split_coordinates_0based':sorted(FORBIDDEN_SPLIT),'method':'PER_LEAF_AFFINE_CONDITIONED_DUAL_ELLIPSOID_AFTER_X58_SINGLETONIZATION',
  'selection_rule':'MIN_EXACT_AFFINE_CONDITIONAL_INTEGER_DOMAIN__MAX_ALL140_ABS_LINEAR_WEIGHT__MIN_INDEX__EXCLUDING_X58_X59_X60_X61_X62',
  'source_locks_verified_before_parent_import':verified,'residual_file_sha256':hashlib.sha256(RESIDUAL.read_bytes()).hexdigest(),'leaves':leaves,
  'summary':{'split_leaf_count':len(split),'necessary_condition_empty_leaf_count':len(empty),'selected_coordinate_histogram':hist,'total_interval_child_count':total_children,'maximum_interval_child_count':49*8,'maximum_conditional_domain':max(domains) if domains else 0,'median_conditional_domain':median,'planned_effective_heavy_concurrency_after_future_audit':8},
  'heavy_surface_present':False,'heavy_armed':False,'execution_authorized':False,
  'credit_firewall':{'numerical_fibration_shell_credit':False,'effectivity_credit':False,'semiampleness_credit':False,'global_fibration_optimum_credit':False,'MB104_complete':False,'stage32_03_complete':False,'receiver_credit':False,'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_existence_claim':False,'perfect_cuboid_nonexistence_claim':False,'merge_authorized':False}
 }
 assert len(leaves)==49 and len(split)+len(empty)==49 and total_children<=49*8
 out['canonical_sha256_without_this_field']=csha(out); a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':out['status'],'split_leaves':len(split),'necessary_condition_empty_leaves':len(empty),'selected_coordinate_histogram':hist,'total_interval_children':total_children,'max_conditional_domain':out['summary']['maximum_conditional_domain'],'canonical':out['canonical_sha256_without_this_field']},sort_keys=True))

if __name__=='__main__': main()
