#!/usr/bin/env python3
"""Exact target-exponent-eight reduction after the E7 and Q[4] rank filters.

Use the notation of ``certify_nonelementary_sign_q2_structural_reduction``.
For H of type (Z/4)^k + (Z/2)^(9-2k), let W be the binary space with

    H[2] = 2W,   dim W = 9-k,

and put U=W cap Y, where Y is the four-dimensional binary space coming from
the four Z/16 coordinates of A0.  Reduction modulo two shows

    8(H^perp) = U^perp  inside 8A0 = Y.

Indeed the parity vectors of elements of H^perp are W^perp; projecting W^perp
to Y gives U^perp.  The order-four congruences lift every such parity vector:
their mod-two compatibility is P<=W and the dot-pairing map onto P* is
surjective.  Since H cap 8A0=U, the quotient H^perp/H has exponent at most
eight exactly when U^perp<=U.

This script counts all W with that property without enumerating them.  If
D(P)=D_X direct_sum D_Y, X0=P_X^perp, u=dim U and r=dim pr_X(W)=9-k-u, then
for a fixed coisotropic U containing D_Y the exact number is

  [dim(X0)-dim(D_X) choose r-dim(D_X)]_2
       * 2^((r-dim(D_X))*(4-u)).

The first factor chooses the X projection and the second chooses its graph in
Y/U, forced to vanish on D_X.  The already-proved target-Q[4] necessary bound
t=dim P_X<=2 is imposed simultaneously.  No full Q[4] image-order, finite-q,
Galois-action, actual-glue, or endpoint credit is claimed.
"""
import hashlib
import itertools
import json
import runpy
from pathlib import Path

HERE=Path(__file__).resolve().parent
ns=runpy.run_path(str(HERE/'certify_nonelementary_sign_q2_structural_reduction.py'))
base=json.loads((HERE/'nonelementary-sign-target-q2-structural-reduction.json').read_text())
if base.get('canonical_sha256')!='235298bd303c0f21d946f6ca537ca30d42e049a6739c1ef106ecef760499c9e9':
    raise SystemExit('E7 structural source lock moved')
q4=json.loads((HERE/'nonelementary-target-q4-rank-obstruction.json').read_text())
Q4_LOCK='8eb225add746b5dcf1dcb3407b22d2b5ccfc6e6637b6e94b69d41edf30e8a6f3'
if q4.get('canonical_sha256')!=Q4_LOCK:
    raise SystemExit('target-Q4 rank-obstruction source lock moved')

subspaces=ns['subspaces']
span=ns['span']
rank=ns['rank']
canon=ns['canon']
eqrc=ns['eq_rank_and_consistency']
qbinom2=ns['qbinom2']

def contains(B,x):
    return rank(list(B)+[x])==len(B)

def rref_subspaces(n,k):
    if k==0:
        yield ()
        return
    for pivots in itertools.combinations(range(n),k):
        ps=set(pivots)
        free=[j for j in range(n) if j not in ps]
        slots=[(r,j) for j in free for r,p in enumerate(pivots) if p<j]
        for mask in range(1<<len(slots)):
            rows=[1<<p for p in pivots]
            for z,(r,j) in enumerate(slots):
                if (mask>>z)&1:
                    rows[r]|=1<<j
            yield canon(rows)

def perp(B,n):
    return canon(
        x for x in range(1,1<<n)
        if all((x&b).bit_count()%2==0 for b in B)
    )

coisotropic=[]
for u in range(2,5):
    for U in rref_subspaces(4,u):
        if all(contains(U,x) for x in perp(U,4)):
            coisotropic.append(U)
if {u:sum(len(U)==u for U in coisotropic) for u in (2,3,4)}!={2:3,3:7,4:1}:
    raise SystemExit('Y coisotropic-subspace census regression')

summary={}
grand=0
for k in range(1,5):
    wdim=9-k
    before_q4=after_q4=after_q8=0
    P_before=P_after_q4=P_after_q8=0
    q8_profile={}
    for B in subspaces[k]:
        supp=0
        for x in span(B):
            supp|=x
        d=supp.bit_count()
        if d>wdim:
            continue
        t=rank([x&0b111 for x in B])
        eqrank,ok=eqrc(B)
        if not ok:
            continue
        nF=1 << (k*(5+k)-eqrank)
        nW=qbinom2(14-t-d,wdim-d)
        before_q4+=nW*nF
        P_before+=1
        if t>2:
            continue
        after_q4+=nW*nF
        P_after_q4+=1

        dX=(supp&0b111).bit_count()
        y_support=[1<<j for j in range(4) if (supp>>(3+j))&1]
        nW8=0
        by_u={}
        for U in coisotropic:
            u=len(U)
            if any(not contains(U,e) for e in y_support):
                continue
            r=wdim-u
            if not (dX<=r<=10-t):
                continue
            n=(qbinom2(10-t-dX,r-dX)
               * (1<<((r-dX)*(4-u))))
            nW8+=n
            by_u[u]=by_u.get(u,0)+n
        if nW8>nW:
            raise SystemExit('coisotropic W count exceeds all W')
        if nW8:
            P_after_q8+=1
            after_q8+=nW8*nF
            key=f'dX={dX},dY={len(y_support)},t={t},eqrank={eqrank}'
            q8_profile[key]=q8_profile.get(key,0)+nW8*nF

    summary[str(k)]={
        'group_type':f'(Z/4)^{k} direct_sum (Z/2)^{9-2*k}',
        'structural_H_before_Q4_rank':before_q4,
        'structural_H_after_t_le_2':after_q4,
        'structural_H_after_t_le_2_and_Q8_exponent':after_q8,
        'P_before_Q4_rank':P_before,
        'P_after_t_le_2':P_after_q4,
        'P_with_at_least_one_Q8_admissible_W':P_after_q8,
        'Q8_profile':dict(sorted(q8_profile.items())),
    }
    grand+=after_q8

expected={
 '1':(91996493167936,91996493167936,1375727569216,63,63,63),
 '2':(8985668747264,8985668747264,437454110720,647,647,647),
 '3':(490213474304,462724005888,24838668288,752,540,396),
 '4':(6442450944,0,0,6,0,0),
}
for k,want in expected.items():
    z=summary[k]
    got=(z['structural_H_before_Q4_rank'],z['structural_H_after_t_le_2'],
         z['structural_H_after_t_le_2_and_Q8_exponent'],z['P_before_Q4_rank'],
         z['P_after_t_le_2'],z['P_with_at_least_one_Q8_admissible_W'])
    if got!=want:
        raise SystemExit(f'Q8 exponent census regression k={k}: {got}')
if grand!=1838020348224:
    raise SystemExit('combined Q4-rank/Q8 grand-total regression')

cert={
 'schema':'STAGE33_07_NONELEMENTARY_TARGET_Q8_EXPONENT_REDUCTION_V1',
 'source_structural_sha256':base['canonical_sha256'],
 'source_Q4_rank_sha256':Q4_LOCK,
 'ambient_A0':'(Z/8)^10 direct_sum (Z/16)^4',
 'target_group':'(Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4',
 'theorem':'8(H^perp)=U^perp and H cap 8A0=U for U=W cap Y; target exponent <=8 iff U^perp<=U',
 'coisotropic_Y_subspace_count_by_dimension':{'2':3,'3':7,'4':1},
 'exact_W_count_formula':'qbinom2(10-t-dX,9-k-u-dX)*2^((9-k-u-dX)*(4-u)), summed over coisotropic U containing D_Y',
 'target_Q4_rank_bound_t_le_2_imposed':True,
 'summary_by_number_of_Z4_factors':summary,
 'total_structural_H_after_Q4_rank_and_Q8_exponent':grand,
 'reduction_factor_denominator_before':base['total_structural_H_after_sign_and_target_Q2'],
 'reduction_factor_numerator_after':grand,
 'non_elementary_abstract_types_before':4,
 'non_elementary_abstract_types_after':3,
 'rejected_type':'(Z/4)^4 direct_sum Z/2',
 'full_target_Q4_condition_certified':False,
 'endpoint_finite_q_certified':False,
 'endpoint_full_action_certified':False,
 'actual_index512_glue_identified':False,
 'next_exact_leaf':'L33-07-IMPOSE-EXACT-Q4-IMAGE-ORDER-THEN-ENDPOINT-FINITE-Q-AND-CC-CT-ACTION-ON-THREE-NONELEMENTARY-E7-TYPES',
 'new_residual_kernel':'R33-BR2A-INDEX512-ELEMENTARY-3-INTEGRAL-ORBITS-PLUS-NONELEMENTARY-1838020348224-Q4Q8-STRUCTURAL-CANDIDATES',
 'unit_status':'RUNNING_REPAIR','stage33_progress':'6/11',
 'stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,
 'perfect_cuboid_nonexistence_claim':False,
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode()
cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-target-q8-exponent-reduction.json').write_text(
    json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({
 'success':True,
 'types_after':3,
 'structural_H_after':{k:v['structural_H_after_t_le_2_and_Q8_exponent'] for k,v in summary.items()},
 'grand_total_after':grand,
 'certificate_sha256':cert['canonical_sha256'],
 'next':cert['next_exact_leaf'],
},indent=2,sort_keys=True))
