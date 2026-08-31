#!/usr/bin/env python3
"""Materialize the semantic Kc u2=t2/2 order-2 class on full-surface A_T[2]."""
from __future__ import annotations
import ast, hashlib, json, re, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
LEGACY=S33/'33-07'
U1=HERE/'j2-semantic-u1-full-surface-smith-source.json'
OUT=HERE/'j2-semantic-u2-full-surface-at2.json'
SOURCE_BLOB='0422b69847f2afb97cb7b3ed02ebef91279f61b1'
U1_SHA='ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec'
MODS=[2]*4+[4]*6+[8]*4


def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def locked(p,h):
    x=json.loads(p.read_text()); b=dict(x); got=b.pop('canonical_sha256'); assert got==h==csha(b); return x
u1=locked(U1,U1_SHA)
sys.path.insert(0,str(LEGACY))
from stoll_cuboid_source import load_pinned_source, run_magma
text,core,blob,source_attempt=load_pinned_source(); assert blob==SOURCE_BLOB
start='// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6.'
end='// action of sign change of c'
kcore=text[text.index(start):text.index(end,text.index(start))]
extra=r'''
targets33:=[52,54];
D33,_,V33:=SmithForm(pmPic); ds33:=[Abs(Integers()!D33[j,j]):j in [1..64]];
pos33:=[j:j in [1..64]|ds33[j] gt 1]; mods33:=[ds33[j]:j in pos33];
assert mods33 eq [2:j in [1..4]] cat [4:j in [1..6]] cat [8:j in [1..4]];
n233:=&+[Vector(Integers(),Eltseq(preimsinPic[j])):j in targets33]; prod233:=n233*pmPic;
printf "STAGE33_12_U2_BEGIN\n"; printf "MODS=%o\n",mods33;
for j in targets33 do printf "PIC_ROW_%o=%o\n",j,Eltseq(preimsinPic[j]); end for;
for j in [1..64] do printf "C_%o=%o\n",j,[Integers()!V33[j,pos33[b]] mod 8:b in [1..14]]; end for;
printf "N2=%o\n",Eltseq(n233); printf "PROD2=%o\n",Eltseq(prod233);
printf "STAGE33_12_U2_END\n";
'''
code='SetColumns(0);\nquick := true;\n'+core+'\n'+kcore+'\n'+extra
stdout,magma_attempt=run_magma(code,360,'Stage33-12 semantic u2 full-surface AT2','perfect-cuboid-stage33/4.4-u2-at2')
if 'STAGE33_12_U2_END' not in stdout or any(x in stdout for x in ('Runtime error','Internal error','User error','Assertion failed')):
    print(stdout); raise SystemExit('u2 extraction failed')
def grab(name,n=None):
    m=re.search(rf'^{re.escape(name)}=(.+)$',stdout,re.M); assert m
    v=[int(x) for x in ast.literal_eval(m.group(1))]
    if n is not None: assert len(v)==n
    return v
mods=grab('MODS',14); assert mods==MODS
C=[[x%8 for x in grab(f'C_{j}',14)] for j in range(1,65)]
assert C==u1['retained_common_smith_source']['v_nontrivial_columns_mod8_64x14']
rows={j:grab(f'PIC_ROW_{j}',64) for j in (52,54)}
n2=grab('N2',64); assert n2==[a+b for a,b in zip(rows[52],rows[54])]
prod=grab('PROD2',64); integral=all(x%2==0 for x in prod); assert integral
z=[x//2 for x in prod]
y=[sum(z[k]*C[k][j] for k in range(64))%MODS[j] for j in range(14)]
bits=[]
for v,m in zip(y,MODS):
    assert v in (0,m//2); bits.append(1 if v==m//2 else 0)
b8=u1['retained_common_smith_source']['discriminant_bilinear_numerator_over_8_reduced']
qnum=sum(y[i]*y[j]*int(b8[i][j]) for i in range(14) for j in range(14))%16
u1y=u1['exact_normalization']['nontrivial_smith_coordinates_mixed_moduli']
cross_num=sum(u1y[i]*y[j]*int(b8[i][j]) for i in range(14) for j in range(14))%8
out={
 'schema':'STAGE33_12_SEMANTIC_U2_FULL_SURFACE_AT2_V1','stage':'33-12','status':'PASS_EXACT_U2_AT2_MATERIALIZED',
 'source_locks':{'stoll_commit':'51233ed5ef2bf228fac9416c66db9adc0ebcaadd','stoll_git_blob_sha1':blob,'submitted_magma_code_sha256':hashlib.sha256(code.encode()).hexdigest(),'semantic_u1_full_surface_smith_source_sha256':U1_SHA},
 'semantic_u2_pullback':{'BigK_support_1based':[52,54],'historical_Magma_rows':rows,'integral_dual_quotient_representative_z':z,'mixed_smith_coordinates':y,'full_surface_A_T_2_coordinates_f2':bits,'quadratic_numerator_mod16_for_q_equals_num_over_8':qnum,'cross_bilinear_with_u1_numerator_mod8_for_b_equals_num_over_8':cross_num},
 'execution':{'source_fetch_attempt':source_attempt,'magma_request_attempt':magma_attempt,'planned_jobs':1,'effective_heavy_concurrency':1,'retention_days':1},
 'promotion_firewall':{'proper_Br2_14D_coordinate_materialized':False,'retained_10D_coordinate_materialized':False,'first_75D_matrix_column_materialized':False,'stage33_12_closed_exact':False,'stage33_13_released':False,'theorem_credit':False,'receiver_credit':False,'endpoint_credit':False}
}
out['canonical_sha256']=csha(out); OUT.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'u2_at2':bits,'mixed':y,'qnum':qnum,'cross_u1_num8':cross_num,'canonical_sha256':out['canonical_sha256']},sort_keys=True))
