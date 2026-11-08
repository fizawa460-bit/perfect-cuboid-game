#!/usr/bin/env python3
"""Exact preflight for algebraic bridge true Sel2 -> fake x-theta quotient.
The validity of the long exact Galois-cohomology sequence, BHN theorem, and local
x-theta evaluation are standard mathematical theorems stated/proved-by-reference
in the proof, not magically verified by this finite script.
"""
import json,hashlib,subprocess,sys
from pathlib import Path
P=Path(__file__).resolve().parent
C=json.loads((P/'true_fake_bridge_351_certificate.json').read_text())
for name,expected in C['parent_SHA256'].items():
    got=hashlib.sha256((P/name).read_bytes()).hexdigest()
    assert got==expected,(name,got,expected)
print('PASS exact SHA256 parent data row343, row350, rank6 and prior verifiers')
old=subprocess.run([sys.executable,str(P/'verify_real_narrow_and_fake_350_stdlib.py')],cwd=P,capture_output=True,text=True,timeout=120)
assert old.returncode==0,(old.stdout[-1500:],old.stderr[-1500:])
assert 'NEW_SCOPED_THEOREM' in old.stdout
assert 'PASS exact four real unit signatures' in old.stdout
assert 'PASS fixed old row349 unit-index13' in old.stdout
print('PASS full old row350 + row349 + row347 exact replay, fake space <=31+c_S')
pre=json.loads((P/'signed18_c2_2descent_preflight_certificate.json').read_text())
r6=json.loads((P/'signed18_genus17_rank6_certificate.json').read_text())
r350=json.loads((P/'row350_certificate.json').read_text())
h=pre['h2_coefficients_ascending'];n=len(h)-1
assert n==36 and pre['Galois_group']=='S_36' and h[0]==h[-1]==1
assert r350['h2_coefficients_ascending']==h and r6['h2_coefficients_ascending']==h
assert (n-2)//2==17 and n-1==35 and n-2==34
assert (C['n_branch_points'],C['genus'],C['T_F2_dimension'],C['M_T_mod_diagonal_F2_dimension'],C['J2_F2_dimension'])==(36,17,36,35,34)
assert C['S36_invariant_M_dimension']==0
# A vector fixed modulo all-one by EACH adjacent transposition satisfies
# v_i=v_(i+1): the difference is supported on <=2 coordinates and cannot
# equal the all-ones vector (n=36). Compute rank of these 35 linear conditions.
rows=[(1<<i)|(1<<(i+1)) for i in range(n-1)]
def gf2_rank(v):
    piv={}
    for a in v:
        while a:
            k=a.bit_length()-1
            if k in piv:a^=piv[k]
            else:piv[k]=a;break
    return len(piv)
assert gf2_rank(rows)==n-1==35
assert n-gf2_rank(rows)==1  # all constant vectors before diagonal quotient
assert C['H1_J2_to_H1_M_kernel_F2_dimension']==1
assert C['true_selmer_to_fake_kernel_dimension_upper']==1
print('PASS S_36 invariants of M=F2^36/<all-one> vanish, exact H1 kernel has F2 dimension one')
assert 'J2(Q)[2]=0' in r6['torsion']
assert r350['fake_real_and_square_norm_dimension_upper_expression']=='31+c_S'
assert r350['global_true_selmer_bound_proved'] is False
assert C['true_Sel2_F2_dimension_upper']=='32+c_S'
assert C['MW_rank_upper']=='32+c_S' and C['MW_rank_lower_old']==6
assert C['true_Sel2_upper16_proved'] is False
assert C['genuine_signed18_original_source_exclusions_new']==0
assert C['Branch_B']=='OPEN' and C['R3_07']=='OPEN'
print('PASS new numerical-bookkeeping consequence (31+c_S)+1=32+c_S, old J(Q)[2]=0 and rank>=6')
print('STANDARD-THEOREM INPUT (not code-checkable): local x-theta Kummer lift and BHN injection eliminate global Br obstruction')
print('THEOREM: dim_F2 true Sel^2(J2/Q)<=32+c_S and 6<=rank(J2(Q))<=32+c_S; c_S UNKNOWN')
print('NOT PROVED: rank upper<=16, Cl_K[2], Cl_S[2], full 19/40 unit generators, all-place Sel2 intersection, p163 Coleman, original source exclusion.')
