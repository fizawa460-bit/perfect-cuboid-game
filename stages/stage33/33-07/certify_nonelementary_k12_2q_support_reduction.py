#!/usr/bin/env python3
"""Exact type-wide 2Q quadratic-support reduction for non-elementary k=1,2.

This continues certify_nonelementary_k12_q2_support_reduction.py.  Let
K=H^perp and let V be the parity image of K.  The Q8 predecessor proves
V=W^perp.  The endpoint 2Q quadratic profile, like Q[2], is supported only at
numerators 0 and 8 modulo 16.

For x in K with parity vector v, the class 2x in 2Q has quadratic numerator

  4*wt_X(v) + 2*wt_Y(v)  (mod 16).

Hence every v in V=W^perp must satisfy

  qbar(v) := 2*wt_X(v) + wt_Y(v) = 0 (mod 4).

Write U=W cap Y, T=U^perp, and R=pr_X(W).  Q8 already gives T<=U.  The kernel
S=V cap X is R^perp.  Vanishing qbar on S forces S to be even-weight, hence
the all-ones X vector j lies in R.  The preceding Q[2]-support leaf already
forces R to lie in the even-weight hyperplane, equivalently j lies in S.

For t in T, choose (x_t,t) in V.  Since S is even, parity(x_t) is well-defined
modulo S.  Orthogonality to the graph W gives

  parity(x_t) = x_t.j = t.phi(j).

The condition qbar(x_t,t)=0 is therefore

  t.phi(j) = wt(t)/2 (mod 2)  for all t in T.

Because pairing Y/U with T is perfect, this fixes exactly one coset
phi(j) mod U.  Thus, for each predecessor (P,U), the Q[2]-support W count

  [9-t-dX choose r-dX]_2 * 2^((r-dX)(4-u))

is reduced exactly to

  [8-t-dX choose r-dX-1]_2 * 2^((r-dX-1)(4-u)),

with zero count when r<dX+1.  No raw H enumeration is used.
"""
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
Q8_LOCK = '4a5c84ad765f93442f08991ffdcea0bab6f1ae5a3ab6561157201bba262f75ee'
q2_ns = runpy.run_path(str(HERE / 'certify_nonelementary_k12_q2_support_reduction.py'))
q2 = json.loads((HERE / 'nonelementary-k12-q2-support-reduction.json').read_text())
if q2.get('schema') != 'STAGE33_07_NONELEMENTARY_K12_Q2_SUPPORT_REDUCTION_V1':
    raise SystemExit('Q2-support predecessor schema regression')
if q2.get('source_Q8_sha256') != Q8_LOCK:
    raise SystemExit('Q2-support predecessor source lock moved')

ns = runpy.run_path(str(HERE / 'certify_nonelementary_target_q8_exponent_reduction.py'))
base = json.loads((HERE / 'nonelementary-target-q8-exponent-reduction.json').read_text())
if base.get('canonical_sha256') != Q8_LOCK:
    raise SystemExit('Q8 predecessor source lock moved')
subspaces = ns['subspaces']
span = ns['span']
rank = ns['rank']
eqrc = ns['eqrc']
qbinom2 = ns['qbinom2']
coisotropic = ns['coisotropic']
contains = ns['contains']

summary = {}
grand_before = 0
grand_after = 0
for k in (1, 2):
    wdim = 9 - k
    before = after = 0
    p_after = 0
    by_t_after = {}
    for B in subspaces[k]:
        supp = 0
        for x in span(B):
            supp |= x
        d = supp.bit_count()
        if d > wdim:
            continue
        t = rank([x & 0b111 for x in B])
        eqrank, ok = eqrc(B)
        if not ok or t > 2:
            continue
        dX = (supp & 0b111).bit_count()
        y_support = [1 << j for j in range(4) if (supp >> (3 + j)) & 1]
        nF = 1 << (k * (5 + k) - eqrank)
        nW_q2 = 0
        nW_2q = 0
        for U in coisotropic:
            u = len(U)
            if any(not contains(U, e) for e in y_support):
                continue
            r = wdim - u
            if not (dX <= r <= 10 - t):
                continue
            nW_q2 += qbinom2(9 - t - dX, r - dX) * (1 << ((r - dX) * (4 - u)))
            if r >= dX + 1:
                nW_2q += qbinom2(8 - t - dX, r - dX - 1) * (1 << ((r - dX - 1) * (4 - u)))
        before += nW_q2 * nF
        if nW_2q:
            p_after += 1
            after += nW_2q * nF
            by_t_after[str(t)] = by_t_after.get(str(t), 0) + nW_2q * nF

    q2_before = q2['summary_by_number_of_Z4_factors'][str(k)]['structural_H_after_endpoint_Q2_support_necessary_condition']
    if before != q2_before:
        raise SystemExit(f'k{k} Q2 predecessor reconstruction mismatch: {before} != {q2_before}')
    summary[str(k)] = {
        'group_type': f'(Z/4)^{k} direct_sum (Z/2)^{9-2*k}',
        'structural_H_before_2Q_support': before,
        'structural_H_after_endpoint_2Q_support_necessary_condition': after,
        'rejected_structural_H': before - after,
        'P_with_at_least_one_2Q_support_admissible_W': p_after,
        'by_t_after': dict(sorted(by_t_after.items())),
        'raw_H_enumerated': False,
    }
    grand_before += before
    grand_after += after

expected_after = {'1': 1311205952, '2': 988553216}
for k, want in expected_after.items():
    got = summary[k]['structural_H_after_endpoint_2Q_support_necessary_condition']
    if got != want:
        raise SystemExit(f'k{k} 2Q-support census regression: {got} != {want}')
if grand_before != 98118129984:
    raise SystemExit('combined Q2-support predecessor total regression')
if grand_after != 2299759168:
    raise SystemExit('combined 2Q-support total regression')

cert = {
    'schema': 'STAGE33_07_NONELEMENTARY_K12_2Q_SUPPORT_REDUCTION_V1',
    'source_Q8_sha256': Q8_LOCK,
    'source_Q2_support_sha256': q2['canonical_sha256'],
    'endpoint_2Q_quadratic_value_support_mod16': [0, 8],
    'double_class_q_formula_mod16': '4*wt_X(v)+2*wt_Y(v) for v in W^perp',
    'necessary_parity_quadratic_condition': '2*wt_X(v)+wt_Y(v)=0 mod 4 for every v in W^perp',
    'Q2_support_condition_reused': 'R=pr_X(W) lies in the even-weight hyperplane',
    'new_conditions': ['all-ones X vector j lies in R', 'phi(j) mod U is the unique coset representing t -> wt(t)/2 on T=U^perp'],
    'exact_W_count_before': 'qbinom2(9-t-dX,r-dX)*2^((r-dX)*(4-u))',
    'exact_W_count_after': 'qbinom2(8-t-dX,r-dX-1)*2^((r-dX-1)*(4-u))',
    'summary_by_number_of_Z4_factors': summary,
    'combined_structural_H_before': grand_before,
    'combined_structural_H_after': grand_after,
    'raw_H_enumerated': False,
    'full_Q4_condition_certified_for_k1_k2': False,
    'endpoint_finite_q_certified': False,
    'endpoint_full_action_certified': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'next_exact_leaf': 'L33-07-COMPRESS-2299759168-K1K2-SURVIVORS-BY-THETA-Q4-RANK-THEN-FULL-Q',
    'new_residual_kernel': 'R33-BR2A-INDEX512-ELEMENTARY-ONE-INTEGRAL-ORBIT-PLUS-NONELEMENTARY-K1K2-2299759168-Q2-2Q-SUPPORT-CANDIDATES',
    'unit_status': 'RUNNING_REPAIR',
    'stage33_progress': '6/11',
    'stage33_08_released': False,
    'stage33_09_released': False,
    'theorem_credit': False,
    'endpoint_credit': False,
    'perfect_cuboid_nonexistence_claim': False,
}
raw = json.dumps(cert, sort_keys=True, separators=(',', ':')).encode()
cert['canonical_sha256'] = hashlib.sha256(raw).hexdigest()
(HERE / 'nonelementary-k12-2q-support-reduction.json').write_text(json.dumps(cert, indent=2, sort_keys=True) + '\n')
print(json.dumps({
    'success': True,
    'k1_before': summary['1']['structural_H_before_2Q_support'],
    'k1_after': summary['1']['structural_H_after_endpoint_2Q_support_necessary_condition'],
    'k2_before': summary['2']['structural_H_before_2Q_support'],
    'k2_after': summary['2']['structural_H_after_endpoint_2Q_support_necessary_condition'],
    'combined_after': grand_after,
    'certificate_sha256': cert['canonical_sha256'],
    'next': cert['next_exact_leaf'],
}, indent=2, sort_keys=True))
