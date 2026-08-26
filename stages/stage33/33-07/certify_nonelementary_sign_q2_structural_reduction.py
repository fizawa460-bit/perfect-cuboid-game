#!/usr/bin/env python3
"""Exact structural reduction for the four exponent<=4 non-elementary glue types.

After the coordinate-sign exponent reduction, normalize the exponent<=4 part of
A0=(Z/8)^10 +(Z/16)^4 as M=(Z/4)^14 by

  y |-> (2*y_0,...,2*y_9,4*y_10,...,4*y_13).

For H ~= (Z/4)^k +(Z/2)^(9-2k), k=1..4, let

  P = H mod 2M, dim P = k,
  W = {w in M/2M : 2w in H}, dim W = 9-k.

Seven coordinate-sign stability is equivalent to D(P)<=W, where D(P) is the
span of all seven rank-two piece projections of P.

The endpoint quotient has 14 cyclic factors, so |Q[2]|=2^14.  Since every
h in H has 2^14 halves in A0, this maximal value is equivalent to every half
of H lying in H^perp.  In normalized coordinates this gives

  C(y,z)=sum_X y_i z_i + 2 sum_Y y_i z_i = 0 mod 4

for all y,z representing H.  Pairing an order-four lift p+2f with 2w gives
p_X.w_X=0, hence W <= U(P)=P_X^perp.  Combining D(P)<=W with this condition
forces each Kb pair projection to be 0 or <11>, and forces the X coordinate of
each mixed Kc/Ka piece to vanish.  Thus P is exactly a k-subspace of the
7-bit even-weight code E7: three bits for the Kb pair values and four bits for
the mixed-piece Y coordinates.  dim D(P) is then the support size of P and
must be <=9-k.

For each such P this script exactly counts:
  * admissible W: Gaussian binomial [dim U(P)-d choose (9-k)-d]_2;
  * order-four lift sections f:P->V/W satisfying the remaining C-pairing
    equations.  The equation rank is computed over F2 exactly, so the number
    of lift sections is 2^(k*(5+k)-rank).

No endpoint-q or full-action credit is granted by this structural census.
"""
import hashlib,json
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
LR=json.loads((HERE/'index512-abstract-glue-types-lr-retained.json').read_text())
LR_LOCK='dd14ecc255244db71a0a1fdcc8af7a5d9a8e957857dec7c879ed8c51d756746a'
if LR.get('canonical_sha256')!=LR_LOCK:
    raise SystemExit('LR source lock moved')

PIECES=((0,1),(2,3),(4,5),(6,10),(7,11),(8,12),(9,13))
EXPECTED_TYPES={
  1:(2,1,1,1,1,1,1,1),
  2:(2,2,1,1,1,1,1),
  3:(2,2,2,1,1,1),
  4:(2,2,2,2,1),
}
all_types={tuple(x) for x in LR['abstract_H_types_after_two_exact_sequence_LR_filter']}
if any(t not in all_types for t in EXPECTED_TYPES.values()):
    raise SystemExit('expected exponent-four types missing from LR source')

# Independent local regression behind the earlier exponent<=4 theorem.
def local_qnum(y,mods):
    # q-value numerator over 16 for the original A0 diagonal form.
    return sum((16//m)*a*a for a,m in zip(y,mods))%32
for mods in ((8,8),(8,16)):
    twotor=[tuple((m//2)*b for m,b in zip(mods,bits)) for bits in ((0,0),(1,0),(0,1),(1,1))]
    iso=[x for x in twotor if local_qnum(x,mods)==0]
    if len(iso)!=4:
        raise SystemExit(f'local 2-torsion isotropic census regression {mods}: {iso}')

# Canonical F2 row-space basis represented by bitmasks.
def canon(rows):
    piv={}
    for x in rows:
        y=int(x)
        for p in sorted(piv,reverse=True):
            if (y>>p)&1:
                y^=piv[p]
        if not y:
            continue
        p=y.bit_length()-1
        for q in list(piv):
            if (piv[q]>>p)&1:
                piv[q]^=y
        piv[p]=y
    return tuple(piv[p] for p in sorted(piv,reverse=True))

def span(B):
    out=[0]
    for b in B:
        out += [x^b for x in out]
    return out

def rank(rows):
    return len(canon(rows))

def qbinom2(n,r):
    if r<0 or r>n:
        return 0
    r=min(r,n-r)
    num=den=1
    for i in range(r):
        num*=2**(n-i)-1
        den*=2**(r-i)-1
    return num//den

# E7: even-weight code in F2^7, dimension 6.
E7=[x for x in range(1<<7) if x.bit_count()%2==0]
if len(E7)!=64:
    raise SystemExit('E7 size regression')

def red_to_full(r):
    # first three reduced bits become equal Kb-pair X bits; last four become
    # the Y coordinates of Kc,Ka1,Ka2,Ka3.  Mixed-piece X bits are zero.
    v=0
    for j in range(3):
        if (r>>j)&1:
            v|=(1<<(2*j))|(1<<(2*j+1))
    for j in range(4):
        if (r>>(3+j))&1:
            v|=1<<(10+j)
    return v

# Enumerate each E7 subspace once.
subspaces={0:{()}}
for k in range(1,5):
    nxt=set()
    for B in subspaces[k-1]:
        SB=set(span(B))
        for v in E7[1:]:
            if v in SB:
                continue
            C=canon(B+(v,))
            if len(C)==k:
                nxt.add(C)
    subspaces[k]=nxt

expected_all={1:63,2:651,3:1395,4:651}
if {k:len(subspaces[k]) for k in range(1,5)}!=expected_all:
    raise SystemExit('E7 Grassmann census regression')

def eq_rank_and_consistency(B):
    """Remaining half-orthogonality equations on lift corrections f_i.

    Variables are k*14 binary coordinates for f_i.  Only X coordinates occur.
    RHS is the ordinary dot product of the reduced E7 basis rows.
    """
    k=len(B); n=k*14
    P=[red_to_full(r) for r in B]
    rows=[];aug=[]
    for i in range(k):
        for j in range(i):
            mask=0
            for c in range(10):
                if (P[i]>>c)&1:
                    mask ^= 1<<(j*14+c)
                if (P[j]>>c)&1:
                    mask ^= 1<<(i*14+c)
            rhs=(B[i]&B[j]).bit_count()&1
            rows.append(mask)
            aug.append(mask|(rhs<<n))
    rr=rank(rows)
    return rr, rank(aug)==rr

summary={}
grand_total=0
for k in range(1,5):
    wdim=9-k
    good=[]
    profile=Counter()
    consistent=0
    structural_H_count=0
    for B in sorted(subspaces[k]):
        supp=0
        for x in span(B):
            supp|=x
        d=supp.bit_count()
        if d>wdim:
            continue
        # t = dim P_X = rank of the first three reduced Kb coordinates.
        t=rank([x&0b111 for x in B])
        eqrank,ok=eq_rank_and_consistency(B)
        good.append((B,d,t,eqrank,ok))
        if not ok:
            profile[(d,t,eqrank,'INCONSISTENT')]+=1
            continue
        consistent+=1
        dimU=14-t
        nW=qbinom2(dimU-d,wdim-d)
        # f is a linear map P -> V/W, domain dimension k*(14-wdim)=k*(5+k).
        nF=1 << (k*(5+k)-eqrank)
        structural_H_count += nW*nF
        profile[(d,t,eqrank,'CONSISTENT')]+=1
    summary[str(k)]={
      'group_type_partition':list(EXPECTED_TYPES[k]),
      'E7_subspaces_before_support_filter':len(subspaces[k]),
      'P_after_support_filter':len(good),
      'P_with_consistent_lift_pairing':consistent,
      'P_inconsistent_lift_pairing':len(good)-consistent,
      'structural_H_count_after_sign_and_target_Q2':structural_H_count,
      'profile_census':{
        f'd={d},t={t},eqrank={r},{s}':n
        for (d,t,r,s),n in sorted(profile.items())
      },
    }
    grand_total+=structural_H_count

expected={
 '1':(63,63,91996493167936),
 '2':(651,647,8985668747264),
 '3':(805,752,490213474304),
 '4':(21,6,6442450944),
}
for k,(np,nc,nh) in expected.items():
    z=summary[k]
    if (z['P_after_support_filter'],z['P_with_consistent_lift_pairing'],z['structural_H_count_after_sign_and_target_Q2'])!=(np,nc,nh):
        raise SystemExit(f'non-elementary structural census regression k={k}: {z}')
if grand_total!=101478817840448:
    raise SystemExit('grand structural H census regression')

cert={
 'schema':'STAGE33_07_NONELEMENTARY_SIGN_TARGET_Q2_STRUCTURAL_REDUCTION_V1',
 'source_lr_sha256':LR_LOCK,
 'ambient_A0':'(Z/8)^10 direct_sum (Z/16)^4',
 'normalized_exponent4_module':'(Z/4)^14',
 'coordinate_piece_order':['Kb1','Kb2','Kb3','Kc','Ka1','Ka2','Ka3'],
 'target_quotient_Q2_log2':14,
 'target_Q2_maximal_half_orthogonality_used':True,
 'coordinate_sign_stability_used':True,
 'forced_reduced_code':'E7 even-weight code in F2^7',
 'forced_Kb_pair_bits_equal':True,
 'forced_mixed_piece_X_bits_zero':True,
 'summary_by_number_of_Z4_factors':summary,
 'total_structural_H_after_sign_and_target_Q2':grand_total,
 'endpoint_full_invariant_factors_certified':False,
 'endpoint_finite_q_certified':False,
 'endpoint_full_coordinate_and_galois_action_certified':False,
 'actual_index512_glue_identified':False,
 'next_exact_leaf':'L33-07-FILTER-NONELEMENTARY-E7-STRUCTURAL-CANDIDATES-BY-Q4-Q8-AND-ENDPOINT-FINITE-Q-ACTION',
 'new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-3-INTEGRAL-ORBITS-PLUS-NONELEMENTARY-E7-STRUCTURAL-CENSUS',
 'unit_status':'RUNNING_REPAIR',
 'stage33_progress':'6/11',
 'stage33_08_released':False,
 'stage33_09_released':False,
 'theorem_credit':False,
 'endpoint_credit':False,
 'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode()
cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-sign-target-q2-structural-reduction.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({
 'success':True,
 'P_after_support_filter':{k:summary[str(k)]['P_after_support_filter'] for k in range(1,5)},
 'P_consistent':{k:summary[str(k)]['P_with_consistent_lift_pairing'] for k in range(1,5)},
 'structural_H_counts':{k:summary[str(k)]['structural_H_count_after_sign_and_target_Q2'] for k in range(1,5)},
 'grand_total':grand_total,
 'certificate_sha256':cert['canonical_sha256'],
 'next':cert['next_exact_leaf'],
},indent=2,sort_keys=True))
