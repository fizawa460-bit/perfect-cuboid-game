#!/usr/bin/env python3
from __future__ import annotations
import argparse, collections, hashlib, json, pathlib
from sympy import Matrix
CORE_SCHEMA='STAGE32_PICARD_CORE_INDLIST_V1'; ACTION_SCHEMA='STAGE32_AUT_PERM_SOURCELOCK_V1'; PARENT_SCHEMA='STAGE32_D8_E8_A36_FULL_PARENT_NUMERICAL_CENSUS_V1'; OUT_SCHEMA='STAGE32_D8_E8_A36_FULL_PARENT_AUT_ORBIT_PARTITION_V1'; EXPECTED_BLOB='0422b69847f2afb97cb7b3ed02ebef91279f61b1'; EXPECTED_GROUP_ORDER=1536
SELECTED_ROWS=list(range(92,140))+[0,1,2,3,4,8,9,12,16,17,24,32,44,48,52,68]; EXPECTED_SELECTED_DET=274877906944

def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def compose(p,q): return tuple(q[p[i]] for i in range(len(p)))
def invert(p):
 r=[0]*len(p)
 for i,j in enumerate(p): r[j]=i
 return tuple(r)
def close(gens):
 ident=tuple(range(140)); seen={ident}; q=collections.deque([ident])
 while q:
  cur=q.popleft()
  for g in gens:
   n=compose(cur,g)
   if n not in seen: seen.add(n); q.append(n); assert len(seen)<=EXPECTED_GROUP_ORDER
 assert len(seen)==EXPECTED_GROUP_ORDER; return sorted(seen)
def verify_core(core):
 assert core['schema']==CORE_SCHEMA and core['source']['git_blob_sha1']==EXPECTED_BLOB and core['rank']==64 and core['known_class_count']==140 and core['h2']==16
 u=dict(core); claimed=u.pop('canonical_sha256_without_this_field'); assert csha(u)==claimed
def verify_action(core,act):
 assert act['schema']==ACTION_SCHEMA and act['source']['git_blob_sha1']==EXPECTED_BLOB and act['permutation_count']==9
 u=dict(act); claimed=u.pop('canonical_sha256_without_this_field'); assert csha(u)==claimed
 gens=[tuple(int(v)-1 for v in row) for row in act['permutations_1based']]; assert all(sorted(p)==list(range(140)) for p in gens); assert all(all(p[i]<92 for i in range(92)) and all(p[i]>=92 for i in range(92,140)) for p in gens)
 K=Matrix(core['known_classes']); G=Matrix(core['basis_gram']); I=Matrix(core['raw_cross_pairings_with_basis']); H=Matrix([core['hyperplane']]); assert K*G==I; kp=I*K.T; hk=H*G*K.T
 for p in gens:
  assert all(hk[0,p[i]]==hk[0,i] for i in range(140)); assert all(kp[p[i],p[j]]==kp[i,j] for i in range(140) for j in range(140))
 return close(gens)
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--core',type=pathlib.Path,required=True); ap.add_argument('--action',type=pathlib.Path,required=True); ap.add_argument('--parent',type=pathlib.Path,required=True); ap.add_argument('--output',type=pathlib.Path,required=True); a=ap.parse_args()
 core=json.loads(a.core.read_text()); act=json.loads(a.action.read_text()); parent=json.loads(a.parent.read_text()); verify_core(core); group=verify_action(core,act); invs=[invert(p) for p in group]
 assert parent['schema']==PARENT_SCHEMA and parent['e8_a36_parent_complete'] is True and parent['parent_inventory']['signature_cell_count']==53 and parent['parent_inventory']['total_materialized_branch_count']==1783951
 surv=parent['numerical_survivors']; assert len(surv)==parent['exact_numerical_survivor_count']
 G=Matrix(core['basis_gram']); I=Matrix(core['raw_cross_pairings_with_basis']); H=Matrix([core['hyperplane']]); known={tuple(map(int,r)) for r in core['known_classes']}
 input_map={}
 for s in surv:
  b=tuple(map(int,s['basis_coordinates'])); assert csha(list(b))==s['basis_coordinates_sha256']; x=Matrix(b); inter=tuple(int(v) for v in I*x); assert int((H*G*x)[0])==8 and int((x.T*G*x)[0])==int(s['self_intersection']); assert all(0<=v<=4 for v in inter[:92]) and all(0<=v<=2 for v in inter[92:]); assert sum(inter[92:])==8 and sum(inter[:46])==36 and sum(inter[:92])+5*sum(inter[92:])==152 and b not in known; assert inter not in input_map; input_map[inter]=s
 selected=Matrix([core['raw_cross_pairings_with_basis'][i] for i in SELECTED_ROWS]); assert abs(int(selected.det()))==EXPECTED_SELECTED_DET; sinv=selected.inv(); allI=I
 def recover(image):
  target=Matrix([image[i] for i in SELECTED_ROWS]); b=sinv*target; assert all(v.q==1 for v in b); out=tuple(int(v) for v in b); assert tuple(int(v) for v in allI*Matrix(out))==image; return out
 remaining=set(input_map); orbit_rows=[]; full_seen=set(); input_keys=set(input_map)
 while remaining:
  seed=min(remaining); orbit={tuple(seed[iv[j]] for j in range(140)) for iv in invs}; assert not (orbit & full_seen); full_seen|=orbit
  members=sorted(orbit & input_keys); assert members; remaining-=set(members)
  squares={int(input_map[m]['self_intersection']) for m in members}; assert len(squares)==1; square=next(iter(squares)); ad=collections.Counter(); source=collections.Counter(); basis_shas=[]
  for m in members: source[(int(input_map[m]['source_cell_index']),input_map[m]['source_cell_id'])]+=1
  for image in sorted(orbit):
   b=recover(image); x=Matrix(b); assert int((H*G*x)[0])==8 and int((x.T*G*x)[0])==square; assert all(0<=v<=4 for v in image[:92]) and all(0<=v<=2 for v in image[92:]); assert sum(image[92:])==8 and sum(image[:92])+5*sum(image[92:])==152 and b not in known; ad[sum(image[:46])]+=1; basis_shas.append(csha(list(b)))
  assert len(members)==ad[36]
  orbit_rows.append({'self_intersection':square,'input_a36_survivor_count':len(members),'full_aut_orbit_size':len(orbit),'stabilizer_order':EXPECTED_GROUP_ORDER//len(orbit),'a_distribution':{str(k):v for k,v in sorted(ad.items())},'input_source_cell_distribution':{f'{i}:{cid}':v for (i,cid),v in sorted(source.items())},'representative_intersection_sha256':csha(list(min(orbit))),'recovered_basis_set_sha256':csha(sorted(basis_shas)),'all_orbit_members_integral_picard_classes':True,'all_orbit_members_new_against_known_140':True})
 orbit_rows.sort(key=lambda r:(r['self_intersection'],r['full_aut_orbit_size'],r['representative_intersection_sha256']))
 assert any(r['self_intersection']==0 and r['full_aut_orbit_size']==6 and r['a_distribution']=={'32':1,'36':5} and r['input_a36_survivor_count']==5 for r in orbit_rows)
 assert any(r['self_intersection']==-4 and r['full_aut_orbit_size']==192 and r['a_distribution']=={'34':64,'36':128} and r['input_a36_survivor_count']==128 for r in orbit_rows)
 report={'schema':OUT_SCHEMA,'source_parent_sha':parent['canonical_sha256_without_this_field'],'source_lock':{'git_blob_sha1':EXPECTED_BLOB,'aut_generator_count':9,'independently_recomputed_aut_order':len(group),'orbit_partition_in_140_intersection_representation':True},'partition':{'input_a36_survivor_count':len(surv),'full_aut_orbit_count':len(orbit_rows),'full_aut_orbit_sizes':[r['full_aut_orbit_size'] for r in orbit_rows],'full_aut_orbit_union_size':sum(r['full_aut_orbit_size'] for r in orbit_rows),'orbits_pairwise_disjoint':True,'every_a36_orbit_member_present_in_parent':True,'orbits':orbit_rows},'scope':'E8_A36_FULL_PARENT_NUMERICAL_AUT_ORBIT_PARTITION_ONLY','effectivity_classification_complete':False,'actual_curve_existence_claim':False,'theorem_credit':False,'audit_status':'PENDING','receiver_credit':False,'FULL_D8_G0_ROW_COMPLETE':False,'FULL_D176_D192_NUMERICAL_ORBIT_CENSUS':False,'R29_LG2_NUMERICAL_COMPONENT_COMPLETE':False,'R29_LG2':'NOT_DISCHARGED','R29_LG2_EFF':'NOT_DISCHARGED','R29_LG2_MB':'NOT_DISCHARGED','G10_LOWGENUS_PICARD':'AMBER'}; report['canonical_sha256_without_this_field']=csha(report); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'input_survivors':len(surv),'orbit_count':len(orbit_rows),'orbit_sizes':report['partition']['full_aut_orbit_sizes'],'square_orbit_distribution':dict(collections.Counter(r['self_intersection'] for r in orbit_rows)),'sha':report['canonical_sha256_without_this_field']},sort_keys=True))
if __name__=='__main__': main()
