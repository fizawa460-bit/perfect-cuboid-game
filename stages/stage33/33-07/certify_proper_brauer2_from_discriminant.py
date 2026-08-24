#!/usr/bin/env python3
"""Derive the exact proper geometric Br(Sbar)[2] V4-module.

This leaf uses only the retained endpoint discriminant certificate.  It does
NOT identify Br[4], does NOT compute the localization connecting map, and does
NOT promote any boundary residue to a Q-defined Brauer class.

Because every Smith invariant of T(S) is divisible by 2, the integral pairing
on T is even.  Hence x mod 2T -> x/2 mod T is a Galois-equivariant isomorphism

    T/2T  ~=  A_T[2].

The proper geometric Br[2]=Hom(T,Z/2) is therefore the F2-dual of the exact
A_T[2] module.  The Picard discriminant action is source-locked through the
V4 splitting field Q(i,sqrt(2)).
"""
import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
src=json.loads((HERE/'picard-discriminant-compact.json').read_text())
claimed=src['canonical_sha256']
chk=dict(src); chk.pop('canonical_sha256',None)
if hashlib.sha256(json.dumps(chk,sort_keys=True,separators=(',',':')).encode()).hexdigest()!=claimed:
    raise SystemExit('compact discriminant canonical hash regression')
if claimed!='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0':
    raise SystemExit('compact discriminant source lock moved')
mods=[int(x) for x in src['discriminant_moduli']]
if mods != [2]*4+[4]*6+[8]*4:
    raise SystemExit('endpoint discriminant moduli regression')
cc=[[int(x) for x in r] for r in src['cc_action_mixed_moduli']]
ct=[[int(x) for x in r] for r in src['ct_action_mixed_moduli']]
N=14

# A_T[2] coordinates: generator i is (mods[i]/2)*e_i.  Restrict the mixed
# modulus row action to these order-two generators.
def restrict_two(M):
    scales=[m//2 for m in mods]
    out=[]
    for i in range(N):
        row=[]
        for j in range(N):
            num=scales[i]*M[i][j]
            if num%scales[j]:
                raise SystemExit('A_T[2] restriction integrality failed')
            row.append((num//scales[j])&1)
        out.append(row)
    return out

A_cc=restrict_two(cc); A_ct=restrict_two(ct)
I=[[1 if i==j else 0 for j in range(N)] for i in range(N)]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(N))&1 for j in range(N)] for i in range(N)]
if mm(A_cc,A_cc)!=I or mm(A_ct,A_ct)!=I or mm(A_cc,A_ct)!=mm(A_ct,A_cc):
    raise SystemExit('restricted A_T[2] V4 action regression')

# Br[2] is the dual module.  Since the generators are involutions, the dual
# row-action matrices are simply the transposes.
B_cc=[list(r) for r in zip(*A_cc)]
B_ct=[list(r) for r in zip(*A_ct)]
if mm(B_cc,B_cc)!=I or mm(B_ct,B_ct)!=I or mm(B_cc,B_ct)!=mm(B_ct,B_cc):
    raise SystemExit('dual Br[2] V4 action regression')

def rank2(rows):
    a=[[int(x)&1 for x in row] for row in rows]
    if not a: return 0
    r=0; n=len(a[0])
    for c in range(n):
        p=next((i for i in range(r,len(a)) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        for i in range(len(a)):
            if i!=r and a[i][c]:
                a[i]=[x^y for x,y in zip(a[i],a[r])]
        r+=1
    return r

def sub(A,B): return [[A[i][j]^B[i][j] for j in range(N)] for i in range(N)]
def tr(A): return [list(r) for r in zip(*A)]
NA=sub(A_cc,I); NB=sub(A_ct,I)
NBA=sub(B_cc,I); NBB=sub(B_ct,I)
# row invariants x(M-I)=0 -> stacked transposed equations.
at_fixed_cc=N-rank2(tr(NA))
at_fixed_ct=N-rank2(tr(NB))
at_fixed_joint=N-rank2(tr(NA)+tr(NB))
br_fixed_cc=N-rank2(tr(NBA))
br_fixed_ct=N-rank2(tr(NBB))
br_fixed_joint=N-rank2(tr(NBA)+tr(NBB))
if (at_fixed_cc,at_fixed_ct,at_fixed_joint)!=(10,13,9):
    raise SystemExit('A_T[2] fixed-dimension regression')
if (br_fixed_cc,br_fixed_ct,br_fixed_joint)!=(10,13,10):
    raise SystemExit('proper Br[2] fixed-dimension regression')

# Finite quotient H^1(V4,Br[2]).  This is only the inflation term in absolute
# H^1(G_Q,Br[2]); no claim is made that absolute H^1 equals finite H^1.
Ng=NBA; Nh=NBB
# cocycle pair (a,b): aNg=0, bNh=0, aNh=bNg.
eq=[]
for j in range(N): eq.append([Ng[i][j] for i in range(N)]+[0]*N)
for j in range(N): eq.append([0]*N+[Nh[i][j] for i in range(N)])
for j in range(N): eq.append([Nh[i][j] for i in range(N)]+[Ng[i][j] for i in range(N)])
cocycle_dim=2*N-rank2(eq)
coboundary_rank=rank2([Ng[i]+Nh[i] for i in range(N)])
h1_v4_dim=cocycle_dim-coboundary_rank
if (cocycle_dim,coboundary_rank,h1_v4_dim)!=(20,4,16):
    raise SystemExit('finite V4 H1 regression')

cert={
 'schema':'STAGE33_07_PROPER_BRAUER2_FROM_DISCRIMINANT_V1',
 'source_locks':{'picard_discriminant_compact_sha256':claimed},
 'transcendental_rank':14,
 'target_smith_all_even':True,
 'transcendental_pairing_even':True,
 'equivariant_identification':'T/2T ~= A_T[2] via x mod 2T -> x/2 mod T',
 'A_T_two_torsion_dimension_f2':14,
 'A_T_two_torsion_cc_action_f2':A_cc,
 'A_T_two_torsion_ct_action_f2':A_ct,
 'A_T_two_torsion_fixed_dimensions':{'cc':at_fixed_cc,'ct':at_fixed_ct,'joint_v4':at_fixed_joint},
 'proper_geometric_Br2_dimension_f2':14,
 'proper_Br2_cc_action_f2':B_cc,
 'proper_Br2_ct_action_f2':B_ct,
 'proper_Br2_fixed_dimensions':{'cc':br_fixed_cc,'ct':br_fixed_ct,'joint_v4':br_fixed_joint},
 'proper_Br2_joint_v4_fixed_dimension_f2':10,
 'finite_v4_H1_proper_Br2':{
   'cocycle_dimension_f2':cocycle_dim,
   'coboundary_dimension_f2':coboundary_rank,
   'H1_dimension_f2':h1_v4_dim,
   'absolute_H1_identified_with_finite_H1':False,
   'role':'FINITE_QUOTIENT_LOCALIZATION_OBSTRUCTION_TARGET_DIAGNOSTIC'
 },
 'full_absolute_localization_connecting_map_computed':False,
 'order2_boundary_residual_promoted_to_global_q_classes':False,
 'proper_Br4_reconstructed':False,
 'actual_index512_k3_glue_identified':False,
 'new_reduction':'ORDER2_PROPER_BRAUER_GALOIS_MODULE_NO_LONGER_DEPENDS_ON_INDEX512_GLUE',
 'next_exact_leaf':'L33-07-COMPUTE-ORDER2-LOCALIZATION-EXTENSION-CLASS-USING-EXACT-BR2-V4-MODULE-AND-BOUNDARY-KUMMER-COMPLEX',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'proper-brauer2-from-discriminant.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'proper_Br2_joint_v4_fixed_dimension_f2':10,
 'finite_v4_H1_dimension_f2':16,'order2_glue_dependency_removed':True,
 'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
