#!/usr/bin/env python3
from __future__ import annotations
import argparse, collections, hashlib, json, pathlib

PROFILE_SCHEMA='STAGE32_D8_MATERIALIZATION_SCHEDULE_PROFILE_V1'
TIER_SCHEMA='STAGE32_D8_MATERIALIZED_PARENT_TIER_EXHAUSTIVE_V1'
CELL_SCHEMA='STAGE32_D8_MATERIALIZED_CELL_EXHAUSTIVE_NUMERICAL_V1'
OUT_SCHEMA='STAGE32_D8_E8_A36_FULL_PARENT_NUMERICAL_CENSUS_V1'
PROFILE_SHA='97608b176d7a91677f63cd293502f7042a9a9f6ad30904631260c9d560b7be17'
TIER_SHA='d043aa870efaff6baf25188c5eac0eb94a3ae10490295a719007d16b3eeb10a5'
REPAIR_SHA='7550900e558a47d07c41164dcb1547901b2849ba53e72f4882b7d15d4ce62384'
REPAIR_CELL_INDEX=39

def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--tier',type=pathlib.Path,required=True); ap.add_argument('--profile',type=pathlib.Path,required=True); ap.add_argument('--repair',type=pathlib.Path,required=True); ap.add_argument('--tail-dir',type=pathlib.Path,required=True); ap.add_argument('--output',type=pathlib.Path,required=True); a=ap.parse_args()
 tier=json.loads(a.tier.read_text()); prof=json.loads(a.profile.read_text()); rep=json.loads(a.repair.read_text())
 assert prof['schema']==PROFILE_SCHEMA and prof['canonical_sha256_without_this_field']==PROFILE_SHA
 assert prof['degree']==8 and prof['genus']==0 and prof['exceptional_mass']==8 and prof['curve_group_mass']==36 and prof['signature_cell_count']==53
 assert tier['schema']==TIER_SCHEMA and tier['deterministic_sha256_without_runtime']==TIER_SHA
 assert tier['parameters']=={'branch_threshold':65536,'curve_group_mass':36,'degree':8,'exceptional_mass':8,'genus':0,'node_limit_per_branch':1000000}
 assert tier['tier_complete_numerical_enumeration'] is True and tier['unknown_cell_count']==0 and tier['tier_inventory']['selected_cell_count']==44
 assert tier['parent_inventory']['signature_cell_count']==53 and tier['parent_inventory']['cell_inventory_sha256']=='e1507e58a2c0b3ae8a5a42c46d0ec68d6172829b21434b337a45040c1831f4e1'
 assert rep['canonical_sha256_without_this_field']==REPAIR_SHA and rep['all_timeout_cells_exactly_partitioned_and_complete'] is True
 rows={int(r['cell_index']):r for r in prof['cells_sorted_by_branch_count']}; assert len(rows)==53
 tier_idx=set(map(int,tier['tier_inventory']['selected_cell_indices'])); assert tier_idx=={i for i,r in rows.items() if int(r['materialized_branch_count'])<=65536}
 tail_idx=set(rows)-tier_idx; assert tail_idx=={3,12,32,34,39,42,44,45,51}
 cell_summaries=[]; survivors=[]; total_branches=0
 for c in tier['cells']:
  idx=int(c['cell_index']); assert idx in tier_idx and c['complete_numerical_enumeration'] is True and int(c['executed_branch_count'])==int(c['materialized_branch_count'])==int(rows[idx]['materialized_branch_count'])
  assert c['cell_id']==rows[idx]['cell_id']; total_branches+=int(c['executed_branch_count'])
  cell_summaries.append({'cell_index':idx,'cell_id':c['cell_id'],'branch_count':int(c['executed_branch_count']),'solver_result':c['solver_result'],'exact_numerical_survivor_count':int(c['exact_numerical_survivor_count']),'source':'stage32-10-tier65536'})
 for s in tier['confirmed_numerical_survivors']:
  q=dict(s); q.setdefault('source_cell_index',int(s['source_cell_index'])); q.setdefault('source_cell_id',s['source_cell_id']); survivors.append(q)
 seen_tail=set()
 for f in sorted(a.tail_dir.glob('*/cell.json')):
  d=json.loads(f.read_text()); assert d['schema']==CELL_SCHEMA
  p=d['parameters']; idx=int(p['cell_index']); assert idx in tail_idx-{REPAIR_CELL_INDEX}; assert idx not in seen_tail; seen_tail.add(idx)
  assert p['degree']==8 and p['genus']==0 and p['exceptional_mass']==8 and p['curve_group_mass']==36 and p['cell_id']==rows[idx]['cell_id']
  assert d['complete_numerical_enumeration'] is True and d['solver_result'] in ('UNSAT','SAT_EXHAUSTED')
  assert int(d['executed_branch_count'])==int(d['materialization']['total_branch_count'])==int(rows[idx]['materialized_branch_count'])
  assert len(d['branches'])==int(d['executed_branch_count']) and all(b['search']['complete_numerical_enumeration'] and not b['search']['node_budget_exhausted'] for b in d['branches'])
  total_branches+=int(d['executed_branch_count'])
  cell_summaries.append({'cell_index':idx,'cell_id':p['cell_id'],'branch_count':int(d['executed_branch_count']),'solver_result':d['solver_result'],'exact_numerical_survivor_count':int(d['exact_numerical_survivor_count']),'source':'stage32-11-run32689063120','deterministic_sha256_without_runtime':d['deterministic_sha256_without_runtime']})
  for s in d['numerical_survivors']:
   q=dict(s); q['source_cell_index']=idx; q['source_cell_id']=p['cell_id']; survivors.append(q)
 assert seen_tail==tail_idx-{REPAIR_CELL_INDEX}
 rc=next(c for c in rep['cell_summaries'] if int(c['exceptional_mass'])==8 and int(c['curve_group_mass'])==36 and int(c['cell_index'])==REPAIR_CELL_INDEX)
 assert rc['branch_partition_complete'] is True and int(rc['unknown_branch_count'])==0 and int(rc['total_branch_count'])==int(rows[REPAIR_CELL_INDEX]['materialized_branch_count']) and rc['cell_id']==rows[REPAIR_CELL_INDEX]['cell_id']
 total_branches+=int(rc['total_branch_count']); cell_summaries.append({'cell_index':REPAIR_CELL_INDEX,'cell_id':rc['cell_id'],'branch_count':int(rc['total_branch_count']),'solver_result':rc['solver_result'],'exact_numerical_survivor_count':int(rc['exact_numerical_survivor_count']),'source':'stage32-11-repair-run32694939071','shard_set_sha256':rc['shard_set_sha256']})
 for s in rc['numerical_survivors']:
  q=dict(s); q['source_cell_index']=REPAIR_CELL_INDEX; q['source_cell_id']=rc['cell_id']; survivors.append(q)
 assert len(cell_summaries)==53 and {x['cell_index'] for x in cell_summaries}==set(range(53))
 assert total_branches==int(prof['total_materialized_branch_count'])==1783951
 cell_summaries.sort(key=lambda x:x['cell_index']); survivors.sort(key=lambda x:tuple(x['basis_coordinates']))
 keys=[tuple(s['basis_coordinates']) for s in survivors]; assert len(keys)==len(set(keys))
 assert all(s['degree']==8 and s['exceptional_mass']==8 and s['curve_group_mass']==36 for s in survivors)
 sq=collections.Counter(int(s['self_intersection']) for s in survivors)
 report={'schema':OUT_SCHEMA,'source_locks':{'profile_sha':PROFILE_SHA,'tier65536_sha':TIER_SHA,'timeout_repair_sha':REPAIR_SHA,'stage32_11_run':32689063120,'stage32_11_repair_run':32694939071},'parameters':{'degree':8,'genus':0,'exceptional_mass':8,'curve_group_mass':36,'node_limit_per_branch':1000000},'parent_inventory':{'signature_cell_count':53,'total_materialized_branch_count':total_branches,'cell_inventory_sha256':'e1507e58a2c0b3ae8a5a42c46d0ec68d6172829b21434b337a45040c1831f4e1'},'cell_summaries':cell_summaries,'exact_numerical_survivor_count':len(survivors),'self_intersection_distribution':{str(k):v for k,v in sorted(sq.items())},'numerical_survivors':survivors,'e8_a36_parent_complete':True,'effectivity_classification_complete':False,'actual_curve_existence_claim':False,'theorem_credit':False,'audit_status':'PENDING','receiver_credit':False,'FULL_D8_G0_ROW_COMPLETE':False,'FULL_D176_D192_NUMERICAL_ORBIT_CENSUS':False,'R29_LG2_NUMERICAL_COMPONENT_COMPLETE':False,'R29_LG2':'NOT_DISCHARGED','R29_LG2_EFF':'NOT_DISCHARGED','R29_LG2_MB':'NOT_DISCHARGED','G10_LOWGENUS_PICARD':'AMBER'}
 report['canonical_sha256_without_this_field']=csha(report); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'cells':53,'branches':total_branches,'survivors':len(survivors),'squares':report['self_intersection_distribution'],'sha':report['canonical_sha256_without_this_field']},sort_keys=True))
if __name__=='__main__': main()
