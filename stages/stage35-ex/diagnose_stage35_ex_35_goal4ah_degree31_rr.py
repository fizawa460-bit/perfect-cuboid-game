#!/usr/bin/env python3
from __future__ import annotations
import json,runpy
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4ag_degree25_residual.py'
AA=ROOT/'stages/stage35-ex/35ex-35/goal4aa-second-class-qi-cyclic-linear-hyperplane-blocker.json'
Z=ROOT/'stages/stage35-ex/35ex-35/goal4z-one-explicit-biquaternion-second-qi-principalization.json'
PERMS=ROOT/'stages/stage33/33-07/galois-known-class-permutations.json'

base=runpy.run_path(str(BASE))
H=[int(x) for x in list(base['H'])]
Pc=[int(x) for x in list(base['Pc'])]
known=[[int(x) for x in r] for r in base['known']]
gram=base['gram']
aa=json.loads(AA.read_text()); z=json.loads(Z.read_text()); p=json.loads(PERMS.read_text())
cc=[int(x) for x in p['cc_permutation_1based']]
ct=[int(x) for x in p['ct_permutation_1based']]
assert len(known)==140 and len(H)==len(Pc)==64
assert p['canonical_sha256']=='e5db20f41948b73168ad5b62acb2f4b48a344e0543d2204c0d5ffdc3cae7cf30'

formal=[0]*140
for k,v in z['class_B']['picard_lift_cc_indlist_coefficients'].items():
    i=int(k); c=int(v); formal[i-1]+=c; formal[cc[i-1]-1]+=c
for k,v in aa['class_B_principalization_target']['simplified_boundary_divisor_E_B'].items():
    formal[int(k)-1]-=int(v)
P=[max(x,0) for x in formal]; N=[max(-x,0) for x in formal]
assert sum(x!=0 for x in formal)==69

def permute_coeff(v,perm):
    out=[0]*len(v)
    for j,c in enumerate(v): out[perm[j]-1]+=c
    return out
formal_cc=formal==permute_coeff(formal,cc); formal_ct=formal==permute_coeff(formal,ct)
P_cc=P==permute_coeff(P,cc); P_ct=P==permute_coeff(P,ct)
N_cc=N==permute_coeff(N,cc); N_ct=N==permute_coeff(N,ct)

G=[[int(gram[i,j]) for j in range(64)] for i in range(64)]
def transform(v): return [sum(v[i]*G[i][j] for i in range(64)) for j in range(64)]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def q(a,b): return dot(transform(a),b)
tknown=[transform(r) for r in known]
pairmat=[[dot(tknown[j],known[k]) for k in range(140)] for j in range(140)]
Hpair=[q(H,r) for r in known]; Ppair=[q(Pc,r) for r in known]
assert q(H,H)==16
assert all(pairmat[j][j]==-4 for j in range(92))
assert all(pairmat[j][j]==-2 for j in range(92,140))
assert all(Hpair[j] in (2,4) for j in range(92))
assert all(Hpair[j]==0 for j in range(92,140))

# Exact d=31 replay only.
d=31
D=[d*H[u]-Pc[u] for u in range(64)]
ints=[d*Hpair[k]-Ppair[k] for k in range(140)]
counts=[0]*140; hd=16*d-396; steps=0
while True:
    neg=[j for j,x in enumerate(ints) if x<0]
    if not neg: break
    j=min(neg,key=lambda t:(ints[t],t))
    D=[D[u]-known[j][u] for u in range(64)]
    ints=[ints[k]-pairmat[j][k] for k in range(140)]
    hd-=Hpair[j]; counts[j]+=1; steps+=1
    if steps>20000: raise SystemExit('d31 strip step cap')
assert hd==96 and q(D,D)==212 and steps==325
assert all(x>=0 for x in ints)
counts_cc=counts==permute_coeff(counts,cc); counts_ct=counts==permute_coeff(counts,ct)

INDLIST=[1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,33,34,35,37,38,41,45,49,53,69,93,94,95,96,97,98,99,101,102,103,104,105,106,107,109,110,111,113,117,118,119,120,121,125,126,127,129,133,135]
def action_matrix(perm):
    return [known[perm[j-1]-1] for j in INDLIST]
def row_times(v,A):
    return [sum(v[i]*A[i][j] for i in range(64)) for j in range(64)]
Acc=action_matrix(cc); Act=action_matrix(ct)
H_cc=row_times(H,Acc)==H; H_ct=row_times(H,Act)==H
Pc_cc=row_times(Pc,Acc)==Pc; Pc_ct=row_times(Pc,Act)==Pc
D_cc=row_times(D,Acc)==D; D_ct=row_times(D,Act)==D

# Smooth minimal resolution S: four-quadric complete intersection in P^6 with
# rational double points. Adjunction gives K_S=H; complete-intersection
# cohomology plus rational-singularity invariance gives chi(O_S)=8.
K2=q(H,H); KD=q(H,D); D2=q(D,D); chi_O=8
chi_D=chi_O+(D2-KD)//2
K_minus_D_Hdeg=K2-KD
assert (D2-KD)%2==0
assert K2==16 and KD==96 and D2==212
assert chi_D==66 and K_minus_D_Hdeg==-80
# H is the pullback of an ample hyperplane class, hence nef. Negative H-degree
# excludes effectivity of K-D. By Serre duality h2(D)=0 and RR gives h0(D)>=66.
h2_zero=K_minus_D_Hdeg<0
h0_lower_bound=chi_D if h2_zero else None
q_defined=(formal_cc and formal_ct and P_cc and P_ct and N_cc and N_ct and counts_cc and counts_ct and H_cc and H_ct and Pc_cc and Pc_ct and D_cc and D_ct)

out={
 'schema':'STAGE35_EX_GOAL4AH_DEGREE31_RR_EFFECTIVITY_DIAGNOSTIC_V1',
 'formal_target_galois_invariant':{'cc':formal_cc,'ct':formal_ct},
 'positive_part_galois_invariant':{'cc':P_cc,'ct':P_ct},
 'negative_part_galois_invariant':{'cc':N_cc,'ct':N_ct},
 'forced_multiplicities_galois_invariant':{'cc':counts_cc,'ct':counts_ct},
 'hyperplane_class_galois_invariant':{'cc':H_cc,'ct':H_ct},
 'positive_picard_class_galois_invariant':{'cc':Pc_cc,'ct':Pc_ct},
 'stripped_residual_class_galois_invariant':{'cc':D_cc,'ct':D_ct},
 'q_defined_strip_data':q_defined,
 'degree':31,
 'strip_steps':steps,
 'forced_support_count':sum(x!=0 for x in counts),
 'forced_strict_multiplicity_sum':sum(counts[:92]),
 'forced_exceptional_multiplicity_sum':sum(counts[92:]),
 'stripped_residual_H_degree':KD,
 'stripped_residual_square':D2,
 'surface_K_square':K2,
 'surface_chi_O':chi_O,
 'surface_canonical_class_equals_H':True,
 'chi_O_D':chi_D,
 'H_dot_K_minus_D':K_minus_D_Hdeg,
 'H_nef':True,
 'h2_D_zero':h2_zero,
 'h0_D_lower_bound':h0_lower_bound,
 'degree31_stripped_residual_effective_over_Q':bool(q_defined and h2_zero and h0_lower_bound and h0_lower_bound>0),
 'degree31_original_residual_effective_over_Q':bool(q_defined and h2_zero and h0_lower_bound and h0_lower_bound>0),
 'degree31_homogeneous_principalization_existence_from_effective_residual':False,
 'explicit_F_B_materialized':False,
 'local_evaluations_computed':False,
 'brauer_manin_obstruction_obtained':False,
 'E1_proved':False,
 'stage35_closed':False,
 'theorem_credit':False,
 'endpoint_credit':False,
}
print('GOAL4AH_RR_JSON='+json.dumps(out,sort_keys=True,separators=(',',':')))
