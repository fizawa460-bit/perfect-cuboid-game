#!/usr/bin/env python3
"""V91C1W v2: source-bind all eight strict divisor schemes to Picard64.

The six multi-match objects are reduced divisor schemes.  Their exact class is
obtained only after proving ideal-intersection equality with the observed
known92 components; the 33-11d `scheme_multiplicity_in_carrier` is retained as
provenance and is deliberately not reinterpreted as the divisor coefficient
of that reduced scheme.

The two zero-match objects form a swap23 pair.  The retained member is the sole
multiplicity-one strict component of one linear carrier, so its resolved
strict-transform class is solved from the carrier total transform with the
same exceptional valuation rule used by V91C1S; the acted member is checked
both by its acted carrier and by the exact Picard swap23 action.
"""
from __future__ import annotations
import json, runpy
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
vns=runpy.run_path(str(HERE/'diagnose_e3_v91c1v_actual_prime_known140_locator.py'))
sns=vns['sns']; kns=vns['kns']; ens=sns['ens']; variables=sns['variables']
needed=sorted(sns['strict_package_difference']); matches=vns['matches']
known_generators=vns['known_generators']; known=kns['known']; hyperplane=kns['hyperplane']; actions=kns['actions']
old_to_canonical=sns['old_to_canonical']; canonical_generators=sns['canonical_generators']; prime_records=sns['prime_records']; prime_action=sns['prime_action']
carrier_refinements=sns['e11']['prime_inventory']['carrier_refinements']; inventory=sns['inventory']; WORD=sns['WORD']
assert len(needed)==8 and WORD==['swap12','swap13','swap12'] and len(known)==140
canonical_to_old={}
for old,cid in old_to_canonical.items(): canonical_to_old.setdefault(cid,[]).append(old)
for x in canonical_to_old.values(): x.sort()

def add(*rows):
 out=[0]*64
 for r in rows:
  for j,x in enumerate(r): out[j]+=int(x)
 return out

def scale(a,r): return [int(a)*int(x) for x in r]
def sub(a,b): return [int(x)-int(y) for x,y in zip(a,b)]
def act(r):
 for A in (actions[0],actions[1],actions[0]): r=kns['row_times_matrix'](r,A)
 return r

def cid(gens): return ens['canonical_ideal'](gens,variables)[0]
def intersect2(I,J,tag):
 t=sp.Symbol('_v91c1w2_'+tag)
 G=sp.groebner([t*f for f in I]+[(1-t)*g for g in J],t,*variables,order='lex',extension=sp.I)
 return [sp.expand(p.as_expr()) for p in G.polys if not p.as_expr().has(t)]
def intersect_all(gs,tag):
 I=list(gs[0])
 for k,J in enumerate(gs[1:],1): I=intersect2(I,J,f'{tag}_{k}')
 return I

def erow(eids):
 rows=[]
 for eid in eids:
  j=int(eid.split('_')[1]); rows.append(known[91+j])
 return add(*rows) if rows else [0]*64

def carrier_eids(sig):
 form=[sns['qi'](z) for z in sig]
 return sorted(eid for eid,p in sns['node_points'].items() if sns['dot'](form,p)==sns['zero'])

class_rows={}; direct={}
direct_ids=[p for p in needed if matches[p]]; zero_ids=[p for p in needed if not matches[p]]
assert len(direct_ids)==6 and len(zero_ids)==2
for p in direct_ids:
 olds=canonical_to_old.get(p,[]); assert len(olds)==1
 rec=prime_records[olds[0]]; assert rec['kind']=='AUDITED_33_11D_DIRECT_PRIME_SUPPORT'
 comps=matches[p]; component_gens=[known_generators[j-1] for j in comps]
 component_ids=[cid(g) for g in component_gens]; assert len(set(component_ids))==len(component_ids)
 inter=intersect_all(component_gens,p[:10]); inter_id=cid(inter)
 if inter_id!=p: raise SystemExit(f'decomposition not exhaustive {p}: {inter_id}')
 row=add(*(known[j-1] for j in comps)); class_rows[p]=row
 direct[p]={
  'known140_class_indices_1based':comps,
  'component_count':len(comps),
  'component_multiplicities':[1]*len(comps),
  'exact_ideal_intersection_equals_target':True,
  'decomposition_exhaustive':True,
  'decomposition_reduced':True,
  'picard64_row':row,
  'source_carrier_id':rec['carrier_id'],
  'scheme_multiplicity_in_carrier_recorded_not_reinterpreted_as_reduced_divisor_coefficient':int(rec['scheme_multiplicity_in_carrier'])}

# Cross-check swap23 covariance for the six source-bound direct schemes.
for p in direct_ids:
 q=prime_action.get(p)
 if q in class_rows and act(class_rows[p])!=class_rows[q]: raise SystemExit(f'direct swap23 class mismatch {p}->{q}')

ret=[p for p in zero_ids if p in canonical_to_old]; out=[p for p in zero_ids if p not in canonical_to_old]
assert len(ret)==len(out)==1
z0,z1=ret[0],out[0]; olds=canonical_to_old[z0]; assert len(olds)==1
rec=prime_records[olds[0]]; assert rec['kind']=='EXACT_REDUCED_PRIME_IDEAL'
carriers=sorted({x['carrier_id'] for x in rec['transport_provenance']}); assert len(carriers)==1
carrier=carriers[0]; pieces=carrier_refinements[carrier]
assert len(pieces)==1 and old_to_canonical[pieces[0]['prime_id']]==z0 and int(pieces[0]['multiplicity'])==1
z0e=carrier_eids(inventory[carrier]); z0row=sub(hyperplane,erow(z0e)); class_rows[z0]=z0row
# This identity is definitional from the exact total-transform relation used here.
assert add(z0row,erow(z0e))==hyperplane
assert prime_action[z0]==z1
acted_sig=ens['apply_word_signature'](inventory[carrier],WORD); z1e=carrier_eids(acted_sig)
z1row=sub(hyperplane,erow(z1e)); z1act=act(z0row)
if z1row!=z1act: raise SystemExit('zero-match acted-carrier class != exact Picard action')
class_rows[z1]=z1row

assert set(class_rows)==set(needed)
strict=[0]*64
for p,a in sns['strict_package_difference'].items(): strict=add(strict,scale(a,class_rows[p]))
exc=[0]*64
for eid,a in sns['exceptional_package_difference'].items(): exc=add(exc,scale(a,erow([eid])))
full=add(strict,exc); mod2=[x%2 for x in full]; support=[i+1 for i,x in enumerate(mod2) if x]

result={
 'success':True,'credit':False,'marker':'V91C1W_ALL8_PICARD64_REDUCTION_V2',
 'strict_scheme_count':8,'strict_scheme_picard64_classes_materialized':True,
 'multi_match_exact_decomposition_count':6,'direct_decompositions':direct,
 'zero_match_direct_relation_count':2,
 'zero_match_relations':{
  z0:{'source_carrier_id':carrier,'single_strict_component':True,'component_multiplicity':1,'exceptional_ids':z0e,'picard64_row':z0row,'total_transform_relation':'H = strict + exceptional_sum'},
  z1:{'source':'swap23 acted carrier','exceptional_ids':z1e,'picard64_row':z1row,'agrees_with_exact_swap23_picard_action':True}},
 'all_eight_exact_decomposition_or_source_bound_relation':True,
 'strict_package_picard64_row':strict,'exceptional_package_picard64_row':exc,
 'complete_swap23_difference_picard64_row':full,
 'complete_swap23_difference_mod2_row':mod2,
 'complete_swap23_difference_mod2_support_one_based':support,
 'pic2_cech_difference_class_computed':True,
 'complete_swap23_difference_zero_mod2':not support,
 'a2_02_swap23_seed_fixed_mod_pic2_promoted':False,
 'a2_02_marked_brauer_image_excluded_from_mask20':False}
print(json.dumps(result,sort_keys=True))
