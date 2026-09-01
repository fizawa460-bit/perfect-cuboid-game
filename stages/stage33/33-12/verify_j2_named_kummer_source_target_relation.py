#!/usr/bin/env python3
"""Network-free verifier for the exact named J2 Kummer source-target relation."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
CERT=HERE/'j2-named-kummer-source-target-relation.json'
ADJ=HERE/'j2-picard-adjoint-proper-br2.json'
TARGET=HERE/'j2-named-v4-h1-target-before-source-orientation.json'
DOMAIN=HERE/'full-surface-pic2-kummer-target.json'
EXPECTED={ADJ:'066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8',TARGET:'4625b6d3ea19ec0e4d8a51471c7f60c0c1219de4672d84c64779c4213306f3b3',DOMAIN:'384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890'}
def csha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,expected=None):
 x=json.loads(p.read_text()); b=dict(x); h=b.pop('canonical_sha256'); assert h==csha(b)
 if expected is not None: assert h==expected
 return x,h
c,h=load(CERT); a,_=load(ADJ,EXPECTED[ADJ]); t,_=load(TARGET,EXPECTED[TARGET]); d,_=load(DOMAIN,EXPECTED[DOMAIN])
s=c['source']; rel=c['exact_linear_relation']; img=c['target']['coordinates_f2']
assert s['retained_10D_coordinate_f2']==a['proper_brauer2_pullback']['retained_10D_coordinate_f2']==[0,1,1,0,0,0,0,0,0,0]
assert s['proper_Br2_14D_coordinate_f2']==a['proper_brauer2_pullback']['proper_Br2_14D_coordinate_f2']
assert img==t['retained_H1_projection']['coordinates_f2'] and len(img)==75 and sum(img)==15
basis=d['proper_invariant_domain']['basis_rows_original_proper_br2_coordinates_f2']; rec=[0]*14
for bit,row in zip(s['retained_10D_coordinate_f2'],basis):
 if bit:rec=[x^(int(y)&1) for x,y in zip(rec,row)]
assert rec==s['proper_Br2_14D_coordinate_f2']
assert rel['standard_column_equation_1based']=='C2 + C3 = h_J2'
assert rel['source_relation_rank_contribution_f2']==1
assert rel['standard_basis_columns_individually_determined_by_this_relation']==[]
assert rel['standard_basis_columns_materialized_total_after_this_relation']==0
assert rel['first_exact_standard_basis_column_materialized'] is False
assert c['promotion_firewall']['finite_v4_kummer_standard_columns_materialized']==0
print(json.dumps({'success':True,'canonical_sha256':h,'source10':s['retained_10D_coordinate_f2'],'target_weight':sum(img)},sort_keys=True))
