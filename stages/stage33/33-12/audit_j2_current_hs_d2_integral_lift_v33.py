#!/usr/bin/env python3
"""V33: certify nonzero current named-J2 HS d2 by one ct-involution parity obstruction.

V25 materializes the genuine current full-surface H2(mu2) lift for named J2.
V32 materializes its current Pic/2 connecting cocycle with z(cc)=0 and
z(ct)=b.  If its Pic/2 class lifted to an integral Pic 1-cocycle, the ct
component would be w_ct=b+2*y for some arbitrary integral y and ct^2=1 would
force w_ct*(T+I)=0.  Coordinate 11 of that single equation is impossible:
the relevant column of T+I is entirely even, while b*(T+I) has value 2, so
it would require an even integer to equal -1.

This proves the finite-V4 Bockstein nonzero without choosing cc integral data,
without a full H2 2-cocycle table, and without reviving the historical
weight-15 artifact as a derivation source.  The locked finite-V4 target
contract states that nonzero restriction certifies absolute nonzero HS d2.
"""
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
S33=HERE.parent
PIC=S33/'33-07'/'retained-picard-base-sparse.json'
V25=HERE/'j2-genuine-h2-mu2-kummer-adapter-v25.json'
V32=HERE/'j2-current-v4-pic2-cocycle-v32.json'
TARGET=HERE/'full-surface-pic2-kummer-target.json'
OUT=HERE/'j2-current-hs-d2-nonzero-v33.json'
LOCKS={
 PIC:'e41df3f84760b941440035a388baac88602126c80140139ddf9c187bedf0bb49',
 V25:'d2f8e087939401e3427056d6deeffa5bdb3433ad6e1801993be4978c3baff65c',
 V32:'e91a7b701690efde3884ca1edc2182b25033a3ff6c7d89bcb8092d02f5a50a7e',
 TARGET:'384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890',
 OUT:'59385430d2806fd600006b8bee1e02170f28d0a598912555d1e905e556c84b8f',
}
N=64

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def locked(path):
 o=json.loads(path.read_text(encoding='utf-8')); b=dict(o); claimed=b.pop('canonical_sha256'); expected=LOCKS[path]; assert claimed==expected==csha(b),(path.name,claimed,csha(b)); return o
def expand_int(obj):
 rows=[]
 for sparse in obj['matrix_64x64_sparse_rows_1based']:
  row=[0]*N
  for col,value in sparse: assert 1<=col<=N and row[col-1]==0; row[col-1]=int(value)
  rows.append(row)
 assert len(rows)==N; return rows
def main():
 pic=locked(PIC); v25=locked(V25); v32=locked(V32); target=locked(TARGET); out=locked(OUT)
 genuine=v25['genuine_h2_mu2_adapter']; source=v25['current_named_source']
 assert genuine['full_surface_named_j2_h2_mu2_lift_materialized'] is True
 assert genuine['named_source_and_cech_lift_identified_by_same_marked_brauer_coordinate'] is True
 assert genuine['raw_weight15_h1_used_as_kummer_boundary'] is False
 assert source['source_coordinate_materialized'] is True and source['retained10_mask_decimal']==6
 assert target['exact_information_boundary']['finite_V4_nonzero_would_certify_absolute_nonzero_by_restriction'] is True
 b=v32['full_surface_pullback']['ct_fullPic64_f2']; assert v32['full_surface_pullback']['cc_fullPic64_f2']==[0]*N
 assert len(b)==N and all(x in (0,1) for x in b) and sum(b)==8
 t=expand_int(pic['objects']['ct']); j=10
 col=[t[i][j]+int(i==j) for i in range(N)]
 sparse=[[i+1,x] for i,x in enumerate(col) if x]
 expected_sparse=[[6,2],[7,2],[8,-2],[9,-2],[11,2],[14,2],[16,-2],[19,-2],[30,2],[43,2]]
 assert sparse==expected_sparse and all(x%2==0 for x in col)
 bdot=sum(b[i]*col[i] for i in range(N)); assert bdot==2
 # (b+2y)(T+I)_11=0 would require y dot col = -bdot/2 = -1.
 required=-(bdot//2); assert required==-1 and required%2==1
 # But every coefficient of col is even, so y dot col is even for every y in Z^64.
 cert=out['integral_lift_nonexistence']
 assert cert['selected_output_coordinate_1based']==11
 assert cert['T_plus_I_column_11_sparse_rows_1based']==sparse
 assert cert['all_selected_column_coefficients_even'] is True
 assert cert['b_times_T_plus_I_coordinate_11']==bdot
 assert cert['required_y_times_T_plus_I_coordinate_11']==required
 assert cert['arbitrary_integral_adjustment_y_allowed'] is True
 assert cert['cc_integral_component_unrestricted_and_irrelevant_to_this_obstruction'] is True
 assert cert['integral_Pic_1cocycle_lift_exists'] is False
 hs=out['kummer_hs_conclusion']
 assert hs['current_H1_Pic2_class_is_from_current_genuine_H2_mu2_lift'] is True
 assert hs['bockstein_H1_Pic2_to_H2_Pic_nonzero'] is True
 assert hs['finite_V4_restriction_nonzero'] is True
 assert hs['absolute_HS_d2_nonzero_by_restriction'] is True
 assert hs['named_J2_HS_d2_zero'] is False
 boundary=out['exact_information_boundary']
 assert boundary['current_hs_d2_nonzero_proved'] is True
 assert boundary['full_integral_H2_2cocycle_table_materialized'] is False
 assert boundary['standard_kummer_columns_materialized']==0 and boundary['stage33_12_closed_exact'] is False
 fw=out['promotion_firewall']; assert fw['historical_weight15_artifact_used_as_derivation_authority'] is False and fw['standard_kummer_column_promoted'] is False
 print(json.dumps({'success':True,'canonical_sha256':LOCKS[OUT],'ct_involution_coordinate_1based':11,'T_plus_I_column_all_even':True,'required_integral_dot_product':required,'hs_d2_nonzero':True,'retained10_named_j2_mask_decimal':source['retained10_mask_decimal'],'next_exact_leaf':out['next_exact_leaf'],'status':out['status']},sort_keys=True))
if __name__=='__main__': main()
