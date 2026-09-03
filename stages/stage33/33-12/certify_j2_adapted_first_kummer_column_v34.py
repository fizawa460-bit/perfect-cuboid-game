#!/usr/bin/env python3
"""V34: certify the first exact Kummer column in an explicit J2-adapted retained10 basis.

The locked standard retained10 basis remains unchanged.  V25 identifies named
J2 with standard mask 6=e2+e3, V32 gives its current 75D Kummer defect, and V33
proves its HS d2 nonzero.  Replacing the source basis by the explicit invertible
F2 basis [e2+e3,e3,e1,e4,...,e10] therefore makes J2 the first basis vector and
materializes one exact column without guessing either original standard column
2 or 3.
"""
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
V25=HERE/'j2-genuine-h2-mu2-kummer-adapter-v25.json'
V32=HERE/'j2-current-v4-pic2-cocycle-v32.json'
V33=HERE/'j2-current-hs-d2-nonzero-v33.json'
TARGET=HERE/'full-surface-pic2-kummer-target.json'
OUT=HERE/'j2-adapted-first-kummer-column-v34.json'
LOCKS={
 V25:'d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c',
 V32:'e91a7b701690efde3884ca1edc2182b25033a3ff6c7d89bcb8092d02f5a50a7e',
 V33:'59385430d2806fd600006b8bee1e02170f28d0a598912555d1e905e556c84b8f',
 TARGET:'384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890',
 OUT:'eb53bd545626efe3b32d407eccd2788e991494203acd718d88100ee7233b909e',
}
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def locked(path):
 o=json.loads(path.read_text(encoding='utf-8')); b=dict(o); claimed=b.pop('canonical_sha256'); expected=LOCKS[path]; assert claimed==expected==csha(b),(path.name,claimed,csha(b)); return o
def bits(mask,n): return [(mask>>i)&1 for i in range(n)]
def xor(a,b): return [x^y for x,y in zip(a,b)]
def rank(rows):
 a=[r[:] for r in rows]; rr=0
 for c in range(len(a[0]) if a else 0):
  p=next((i for i in range(rr,len(a)) if a[i][c]),None)
  if p is None: continue
  a[rr],a[p]=a[p],a[rr]
  for i in range(len(a)):
   if i!=rr and a[i][c]: a[i]=xor(a[i],a[rr])
  rr+=1
 return rr
def combine(mask,rows):
 out=[0]*len(rows[0])
 for i,row in enumerate(rows):
  if (mask>>i)&1: out=xor(out,row)
 return out
def main():
 v25=locked(V25); v32=locked(V32); v33=locked(V33); target=locked(TARGET); out=locked(OUT)
 retained=target['proper_invariant_domain']['basis_rows_original_proper_br2_coordinates_f2']; assert len(retained)==10 and all(len(r)==14 for r in retained) and rank(retained)==10
 src=v25['current_named_source']; assert src['source_coordinate_materialized'] is True and src['retained10_mask_decimal']==6 and src['proper14_mask_decimal']==25
 j2proper=bits(25,14); assert combine(6,retained)==j2proper
 masks=out['source_basis_change']['adapted_basis_masks_decimal']; assert masks==[6,4,1,8,16,32,64,128,256,512]
 coord_rows=[bits(m,10) for m in masks]; assert rank(coord_rows)==10
 assert combine(masks[0],retained)==j2proper
 assert out['source_basis_change']['basis_rank_f2']==10 and out['source_basis_change']['invertible'] is True and out['source_basis_change']['first_adapted_basis_vector_is_named_J2'] is True
 h1=v32['v4_1cocycle']['retained_H1_projection']['coordinates_f2']; assert len(h1)==75 and sum(h1)==15
 col=out['first_adapted_kummer_column']; assert col['column_1based']==1 and col['source_label']=='J2=e2+e3' and col['coordinates_75D_f2']==h1 and col['coordinate_weight']==15 and col['nonzero'] is True
 assert v33['kummer_hs_conclusion']['absolute_HS_d2_nonzero_by_restriction'] is True and col['absolute_HS_d2_nonzero'] is True
 rel=out['original_standard_basis_relation']; assert rel['standard_columns_in_relation_1based']==[2,3] and rel['rhs_coordinates_75D_f2']==h1 and rel['standard_col_2_materialized'] is False and rel['standard_col_3_materialized'] is False and rel['no_individual_standard_column_inferred'] is True
 boundary=out['exact_information_boundary']; assert boundary['adapted_kummer_columns_materialized']==1 and boundary['adapted_kummer_columns_total']==10 and boundary['original_standard_kummer_columns_materialized']==0 and boundary['stage33_12_closed_exact'] is False
 fw=out['promotion_firewall']; assert fw['standard_col2_guessed'] is False and fw['standard_col3_guessed'] is False and fw['full_matrix_guessed'] is False
 print(json.dumps({'success':True,'canonical_sha256':LOCKS[OUT],'adapted_source_basis_rank_f2':10,'first_source_standard_mask_decimal':6,'first_column_weight':15,'first_column_hs_d2_nonzero':True,'original_standard_relation':'col2 XOR col3 = J2-column','next_exact_leaf':out['next_exact_leaf'],'status':out['status']},sort_keys=True))
if __name__=='__main__': main()
