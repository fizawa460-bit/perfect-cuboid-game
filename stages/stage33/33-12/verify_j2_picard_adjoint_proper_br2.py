#!/usr/bin/env python3
"""Network-free replay verifier for the J2 Picard-adjoint proper-Br2 certificate."""
from __future__ import annotations
from fractions import Fraction
import hashlib, itertools, json, runpy
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
CERT=HERE/'j2-picard-adjoint-proper-br2.json'
SEM=HERE/'j2-semantic-kc-picard-basis.json'
KC2=HERE/'j2-semantic-kc-discriminant-2torsion-target.json'
U1=HERE/'j2-semantic-u1-full-surface-smith-source.json'
U2=HERE/'j2-semantic-u2-full-surface-at2.json'
PROPER=S33/'33-07'/'proper-brauer2-from-discriminant.json'
TARGET=HERE/'full-surface-pic2-kummer-target.json'
OLD_BASE=S33/'33-07'/'picard_base_rows_retained.py'
LOCKS={
 CERT:'066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8',
 SEM:'c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0',
 KC2:'0b5d7dfdefbb0f2b7c37396ada35c0bee462dfeb625eb18262be0e862205d8df',
 U1:'ae5a9b45e4e4d9b50d8685d1c4649725dadf4956f246e18b33cb601aef94a2ec',
 U2:'60b6d058459f7745f6fa3f9b6d3b44f1610e12ff46c42e3133ec574f71613039',
 PROPER:'c86f6e838d072816426e4a2b0eb738f44e8632dd1ab4f3e6fdccd161ec41b5bf',
 TARGET:'384b7c9cb06e993c147fa89b30f93efcd454fe1a1773892ac70f463d07af9890',
}
OLD_BASE_SHA='d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c'

def csha(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def locked(p):
 x=json.loads(p.read_text()); b=dict(x); h=b.pop('canonical_sha256'); assert h==LOCKS[p]==csha(b),p; return x
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a): return [list(x) for x in zip(*a)]
def inv(a):
 n=len(a); m=[[Fraction(a[i][j]) for j in range(n)]+[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
 for c in range(n):
  p=next(r for r in range(c,n) if m[r][c]); m[c],m[p]=m[p],m[c]; q=m[c][c]; m[c]=[x/q for x in m[c]]
  for r in range(n):
   if r!=c and m[r][c]:
    q=m[r][c]; m[r]=[m[r][j]-q*m[c][j] for j in range(2*n)]
 return [r[n:] for r in m]
def rowmul(v,m): return [sum(v[k]*m[k][j] for k in range(len(v))) for j in range(len(m[0]))]
def rowf2(v,m): return [sum((v[i]&1)*(m[i][j]&1) for i in range(len(v)))&1 for j in range(len(m[0]))]
def solve10(basis,target):
 for bits in itertools.product((0,1),repeat=10):
  v=[0]*14
  for bit,row in zip(bits,basis):
   if bit: v=[a^(int(b)&1) for a,b in zip(v,row)]
  if v==target:return list(bits)
 return None

c=locked(CERT); sem=locked(SEM); kc=locked(KC2); u1=locked(U1); u2=locked(U2); proper=locked(PROPER); target=locked(TARGET)
base=runpy.run_path(str(OLD_BASE))['load'](); assert base['canonical_sha256']==OLD_BASE_SHA
D=c['degree2_picard_adjoint']; P=D['picard_pullback_matrix_P_20x64']; Gs=base['picard_gram_64x64']; Gk=D['source_picard_gram_Gk_equals_PGsPt_over_2_20x20']
raw=mm(mm(P,Gs),tr(P)); assert all(x%2==0 for r in raw for x in r); assert [[x//2 for x in r] for r in raw]==Gk
Gi=inv(Gk); zbs=D['target_AT2_basis_picard_covectors_zS_14x64']; decoded=D['decoded_target_basis_columns']
u1n=kc['semantic_half_lattice_basis'][0]['numerator_mod2']; u2n=kc['semantic_half_lattice_basis'][1]['numerator_mod2']
combo={tuple([0]*20):[0,0],tuple(u1n):[1,0],tuple(u2n):[0,1],tuple(a^b for a,b in zip(u1n,u2n)):[1,1]}
coords=[]
for a,zs in enumerate(zbs):
 zk=[sum(zs[k]*P[j][k] for k in range(64)) for j in range(20)]
 assert zk==decoded[a]['source_picard_dual_covector_zK']
 x=rowmul(zk,Gi); two=[2*q for q in x]; assert all(q.denominator==1 for q in two)
 v=tuple(int(q)&1 for q in two); assert v in combo
 assert combo[v]==decoded[a]['source_T_mod_2_coordinate_f2']; coords.append(combo[v])
beta1=[x[0] for x in coords]; beta2=[x[1] for x in coords]; p=c['proper_brauer2_pullback']
assert beta1==p['proper_Br2_14D_coordinate_f2']==[1,0,0,1,1,0,0,0,0,0,0,0,0,0]
assert beta2==p['companion_beta2_proper_Br2_14D_coordinate_f2']
assert rowf2(beta1,proper['proper_Br2_cc_action_f2'])==beta1 and rowf2(beta1,proper['proper_Br2_ct_action_f2'])==beta1
basis=target['proper_invariant_domain']['basis_rows_original_proper_br2_coordinates_f2']; assert solve10(basis,beta1)==p['retained_10D_coordinate_f2']==[0,1,1,0,0,0,0,0,0,0]
assert solve10(basis,beta2)==p['companion_beta2_retained_10D_coordinate_f2']
assert c['promotion_firewall']['first_75D_matrix_column_materialized'] is False
print(json.dumps({'success':True,'canonical_sha256':LOCKS[CERT],'proper14':beta1,'retained10':p['retained_10D_coordinate_f2']},sort_keys=True))
