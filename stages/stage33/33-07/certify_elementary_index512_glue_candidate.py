#!/usr/bin/env python3
"""Certify one explicit elementary order-512 glue candidate.

This is a necessary-filter witness, NOT an identification of the actual
endpoint transcendental glue.  It proves that the elementary hypothesis
H ~= (Z/2)^9 is not eliminated by:
  * index/order and isotropy,
  * target Smith invariants,
  * extension-independent arithmetic action on A_L0[2],
  * the forced deeper Kc/Ka commutator becoming trivial on H^perp/H,
  * exact quadratic-value distributions on A[2], 2A, and 4A.
Full finite quadratic-module isometry and simultaneous endpoint action
conjugacy remain required before any actual-glue credit.
"""
import hashlib,itertools,json
from collections import Counter
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_decomp

HERE=Path(__file__).resolve().parent
TGT=json.loads((HERE/'picard-discriminant-compact.json').read_text())
ACT=json.loads((HERE/'coordinate-k3-scaled-action-retained.json').read_text())
if TGT['canonical_sha256']!='4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0':
    raise SystemExit('target discriminant source lock moved')
if ACT['canonical_sha256']!='017bd4072fcacf7aa59d60cad9fc979cc37637b098919db726ea3998bfbfb720':
    raise SystemExit('scaled action source lock moved')
mods=[int(x) for x in TGT['discriminant_moduli']]
if mods!=[2]*4+[4]*6+[8]*4: raise SystemExit('target Smith regression')

# Sorted L0 coordinates: ten <8> coordinates first, then four <16>.
# Piece pairing is Kb1=(0,1), Kb2=(2,3), Kb3=(4,5),
# Kc=(6,10), Ka1=(7,11), Ka2=(8,12), Ka3=(9,13).
C5=[
 [1,1,0,0,1,1,0,0,0,0],
 [1,0,0,0,0,1,1,0,1,0],
 [0,0,1,0,1,0,0,0,0,0],
 [1,1,1,1,0,0,0,0,0,0],
 [0,1,0,0,0,1,0,1,0,1],
]
C=[r+[0]*4 for r in C5]
for j in range(4):
    r=[0]*14; r[10+j]=1; C.append(r)

def bits(row):
    return sum((int(v)&1)<<i for i,v in enumerate(row))
def gf2_rank(rows):
    piv={}
    for row in rows:
        x=row if isinstance(row,int) else bits(row)
        while x:
            p=x.bit_length()-1
            if p in piv: x^=piv[p]
            else: piv[p]=x; break
    return len(piv)
def in_span(x,basis):
    piv={}
    for b in basis:
        y=b
        while y:
            p=y.bit_length()-1
            if p in piv:y^=piv[p]
            else:piv[p]=y;break
    while x:
        p=x.bit_length()-1
        if p not in piv:return False
        x^=piv[p]
    return True
Cb=[bits(r) for r in C]
if gf2_rank(Cb)!=9: raise SystemExit('candidate code rank regression')

# Every order-two vector of A_L0 is isotropic: for <8>, q(4e)=2;
# for <16>, q(8e)=4, both zero in Q/2Z.
elementary_isotropic=True

# Extension-independent arithmetic A[2] action: only Kb cc swaps its two
# coordinates; all Kc/Ka actions and ct are identity on A[2].
perm=list(range(14))
for a,b in ((0,1),(2,3),(4,5)): perm[a],perm[b]=b,a
def pbits(x):
    y=0
    for i,j in enumerate(perm):
        if (x>>i)&1:y|=1<<j
    return y
if not all(in_span(pbits(b),Cb) for b in Cb):
    raise SystemExit('candidate not stable under extension-independent cc action')
if ACT['pieces']['kb']['A2_cc_action_f2']!=[[0,1],[1,0]]:
    raise SystemExit('Kb A2 cc source regression')
for k in ('kc','ka'):
    if ACT['pieces'][k]['A2_cc_action_f2']!=[[1,0],[0,1]] or ACT['pieces'][k]['A2_ct_action_f2']!=[[1,0],[0,1]]:
        raise SystemExit(f'{k} A2 source regression')

# H^perp is characterized by parity vectors p in C^perp.  For each mixed
# (8,16) piece the forced commutator J=[[1,8],[4,1]] has
# (J-I)(x_8,x_16)=(4*x_16,8*x_8).  In order-two coordinates this swaps the
# two parity bits.  Verify exhaustively that this difference lies in H for
# every parity vector in C^perp, hence J is trivial on H^perp/H.
Cperp=[]
for x in range(1<<14):
    if all((x&b).bit_count()%2==0 for b in Cb): Cperp.append(x)
if len(Cperp)!=32: raise SystemExit('candidate C-perp dimension regression')
def comm_half_bits(p):
    out=0
    for i in range(6,10):
        j=10+i-6
        if (p>>j)&1: out|=1<<i
        if (p>>i)&1: out|=1<<j
    return out
if not all(in_span(comm_half_bits(p),Cb) for p in Cperp):
    raise SystemExit('forced commutator survives candidate quotient')
for k in ('kc','ka'):
    if ACT['pieces'][k]['forced_commutator']!=[[1,8],[4,1]] or not ACT['pieces'][k]['commutator_forced_independent_of_extension']:
        raise SystemExit(f'{k} forced commutator source regression')

# Build the actual integral overlattice represented by C.  If K is generated
# by 2Z^14 and C in Z^14, then (1/2)K is the corresponding overlattice of L0.
D0=sp.diag(*([8]*10+[16]*4))
gens=sp.Matrix(2*sp.eye(14)).col_join(sp.Matrix(C))
Kbasis=hermite_normal_form(gens.T).T
B=Kbasis/2
G=sp.simplify(B*D0*B.T)
if any(v.q!=1 for v in G): raise SystemExit('candidate Gram not integral')
if any(int(G[i,i])%2 for i in range(14)): raise SystemExit('candidate Gram not even')
if abs(int(G.det()))!=2**28: raise SystemExit('candidate determinant regression')
D,S,T=smith_normal_decomp(G,domain=ZZ)
smith=[abs(int(D[i,i])) for i in range(14)]
if smith!=[2]*4+[4]*6+[8]*4: raise SystemExit(f'candidate Smith mismatch {smith}')

# Transport the candidate discriminant quadratic form to Smith coordinates.
Sinv=S.inv(); B8c=sp.simplify(8*(Sinv.T*G.inv()*Sinv))
if any(v.q!=1 for v in B8c): raise SystemExit('candidate B8 not integral')
def red_b8(M):
    return [[int(M[i,j])%(16 if i==j else 8) for j in range(14)] for i in range(14)]
B8c=red_b8(B8c)
B8t=red_b8(-sp.Matrix(TGT['discriminant_bilinear_numerator_over_8_reduced']))

def qnum(x,B8):
    return sum(x[i]*B8[i][j]*x[j] for i in range(14) for j in range(14))%16
def values(kind):
    if kind=='A2': return [[0,m//2] for m in mods]
    if kind=='2A': return [list(range(0,m,2)) for m in mods]
    if kind=='4A': return [list(range(0,m,4)) for m in mods]
    raise ValueError(kind)
def qdist(B8,kind):
    c=Counter()
    for x in itertools.product(*values(kind)): c[qnum(x,B8)]+=1
    return {str(k):int(v) for k,v in sorted(c.items())}
filters={}
for kind in ('A2','2A','4A'):
    ca=qdist(B8c,kind); ta=qdist(B8t,kind)
    if ca!=ta: raise SystemExit(f'{kind} quadratic distribution mismatch {ca} != {ta}')
    filters[kind]={'candidate':ca,'target':ta,'match':True}

cert={
 'schema':'STAGE33_07_ELEMENTARY_INDEX512_GLUE_CANDIDATE_V1',
 'source_locks':{
   'target_picard_discriminant_sha256':TGT['canonical_sha256'],
   'scaled_coordinate_k3_action_sha256':ACT['canonical_sha256'],
   'scaled_coordinate_k3_full_source_sha256':ACT['source_full_certificate_canonical_sha256'],
 },
 'ambient_L0':'<8>^10 direct_sum <16>^4',
 'ambient_discriminant_group':'(Z/8)^10 direct_sum (Z/16)^4',
 'candidate_H_type':'(Z/2)^9',
 'candidate_H_order':512,
 'candidate_code_basis_f2':C,
 'candidate_code_rank_f2':9,
 'candidate_isotropic':elementary_isotropic,
 'candidate_arithmetic_A2_stable_for_all_scaled_extensions':True,
 'candidate_forced_commutator_trivial_on_Hperp_mod_H':True,
 'candidate_overlattice_gram_14x14':[[int(G[i,j]) for j in range(14)] for i in range(14)],
 'candidate_overlattice_even':True,
 'candidate_overlattice_determinant_abs':abs(int(G.det())),
 'candidate_overlattice_smith':smith,
 'target_smith':[2]*4+[4]*6+[8]*4,
 'candidate_discriminant_B8_smith_coords':B8c,
 'target_transcendental_B8_smith_coords':B8t,
 'quadratic_filtration_value_distributions':filters,
 'necessary_filters_passed':[
   'ORDER_2^9_ISOTROPIC','TARGET_SMITH','EXTENSION_INDEPENDENT_A2_GALOIS_STABILITY',
   'FORCED_DEEPER_COMMUTATOR_KILLED','A2_Q_VALUE_DISTRIBUTION','2A_Q_VALUE_DISTRIBUTION','4A_Q_VALUE_DISTRIBUTION'
 ],
 'elementary_glue_hypothesis_eliminated':False,
 'actual_index512_glue_identified':False,
 'full_finite_quadratic_form_isometry_certified':False,
 'simultaneous_endpoint_cc_ct_action_conjugacy_certified':False,
 'candidate_promoted_to_endpoint_T_lattice':False,
 'next_exact_leaf':'L33-07-DECIDE-FULL-FINITE-QUADRATIC-MODULE-ISOMETRY-AND-SIMULTANEOUS-ENDPOINT-ACTION-CONJUGACY',
 'unit_status':'RUNNING_REPAIR','unit_closed':False,'stage33_progress':'6/11','stage33_08_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'elementary-index512-glue-candidate.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({
 'success':True,'candidate_H_type':cert['candidate_H_type'],'candidate_H_order':512,
 'target_smith_match':True,'A2_q_distribution':filters['A2']['candidate'],
 'twoA_q_distribution':filters['2A']['candidate'],'fourA_q_distribution':filters['4A']['candidate'],
 'forced_commutator_killed':True,'actual_glue_identified':False,
 'next':cert['next_exact_leaf'],'certificate_sha256':cert['canonical_sha256']
},indent=2,sort_keys=True))
