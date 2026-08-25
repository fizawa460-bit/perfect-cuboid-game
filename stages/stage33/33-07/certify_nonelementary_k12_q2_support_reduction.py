#!/usr/bin/env python3
"""Exact type-wide Q[2]-quadratic-support reduction for non-elementary k=1,2.

After the E7 / target-Q4-rank / target-Q8 reductions, write

  H ~= (Z/4)^k + (Z/2)^(9-2k),  k=1,2,
  H[2] = 2W,  dim W = 9-k.

The endpoint finite quadratic module has exact Q[2] value profile supported
only at numerators 0 and 8 modulo 16.  For w in W, the order-two element 2w
has a half in the ambient discriminant module.  In the normalized coordinates
of certify_nonelementary_sign_q2_structural_reduction.py its quadratic
numerator modulo 16 is

  4*wt_X(w) + 8*wt_Y(w).

Hence any odd X-weight vector w would force a Q[2] value 4 or 12, impossible
for the endpoint.  Therefore a necessary type-wide condition is

  pr_X(W) <= E_X := {x in F2^10 : wt(x) even}.

The Q8 predecessor parameterizes W by U=W cap Y and an X projection R inside
X0=P_X^perp.  Because every P_X row has even weight, the all-ones functional
is nonzero on X0 and dim(X0 cap E_X)=9-t.  The exact predecessor W count

  [10-t-dX choose r-dX]_2 * 2^((r-dX)(4-u))

therefore becomes

  [9-t-dX choose r-dX]_2 * 2^((r-dX)(4-u)).

This script recomputes the complete E7/Q8 census and applies exactly that
necessary condition without enumerating raw H.  It grants no full finite-q,
action-conjugacy, actual-glue, HS, endpoint, or theorem credit.
"""
import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
Q8_LOCK = '4a5c84ad765f93442f08991ffdcea0bab6f1ae5a3ab6561157201bba262f75ee'
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
    p_before = p_after = 0
    by_t_before = {}
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
        nW_before = 0
        nW_after = 0
        for U in coisotropic:
            u = len(U)
            if any(not contains(U, e) for e in y_support):
                continue
            r = wdim - u
            if not (dX <= r <= 10 - t):
                continue
            graph = 1 << ((r - dX) * (4 - u))
            nW_before += qbinom2(10 - t - dX, r - dX) * graph
            # Q[2]-support condition pr_X(W) <= E_X.  The allowed X ambient
            # space has dimension 9-t instead of 10-t.
            nW_after += qbinom2(9 - t - dX, r - dX) * graph
        if not nW_before:
            continue
        p_before += 1
        before += nW_before * nF
        by_t_before[str(t)] = by_t_before.get(str(t), 0) + nW_before * nF
        if nW_after:
            p_after += 1
            after += nW_after * nF
            by_t_after[str(t)] = by_t_after.get(str(t), 0) + nW_after * nF

    expected_before = base['summary_by_number_of_Z4_factors'][str(k)]['structural_H_after_t_le_2_and_Q8_exponent']
    if before != expected_before:
        raise SystemExit(f'k{k} predecessor reconstruction mismatch: {before} != {expected_before}')
    summary[str(k)] = {
        'group_type': f'(Z/4)^{k} direct_sum (Z/2)^{9-2*k}',
        'Q8_structural_H_before_Q2_support': before,
        'structural_H_after_endpoint_Q2_support_necessary_condition': after,
        'rejected_structural_H': before - after,
        'Q8_admissible_P_before': p_before,
        'P_with_at_least_one_Q2_support_admissible_W': p_after,
        'by_t_before': dict(sorted(by_t_before.items())),
        'by_t_after': dict(sorted(by_t_after.items())),
        'raw_H_enumerated': False,
    }
    grand_before += before
    grand_after += after

expected_after = {
    '1': 42731821376,
    '2': 55386308608,
}
for k, want in expected_after.items():
    got = summary[k]['structural_H_after_endpoint_Q2_support_necessary_condition']
    if got != want:
        raise SystemExit(f'k{k} Q2-support census regression: {got} != {want}')
if grand_before != 1813181679936:
    raise SystemExit('combined k1/k2 predecessor total regression')
if grand_after != 98118129984:
    raise SystemExit('combined k1/k2 Q2-support total regression')

cert = {
    'schema': 'STAGE33_07_NONELEMENTARY_K12_Q2_SUPPORT_REDUCTION_V1',
    'source_Q8_sha256': Q8_LOCK,
    'endpoint_Q2_quadratic_value_support_mod16': [0, 8],
    'half_of_2w_q_formula_mod16': '4*wt_X(w)+8*wt_Y(w)',
    'necessary_condition': 'pr_X(W) lies in the even-weight hyperplane of F2^10',
    'exact_W_count_before': 'qbinom2(10-t-dX,r-dX)*2^((r-dX)*(4-u))',
    'exact_W_count_after': 'qbinom2(9-t-dX,r-dX)*2^((r-dX)*(4-u))',
    'summary_by_number_of_Z4_factors': summary,
    'combined_structural_H_before': grand_before,
    'combined_structural_H_after': grand_after,
    'raw_H_enumerated': False,
    'full_Q4_condition_certified_for_k1_k2': False,
    'endpoint_finite_q_certified': False,
    'endpoint_full_action_certified': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'next_exact_leaf': 'L33-07-COMPRESS-K1-K2-Q2-SUPPORT-SURVIVORS-BY-THETA-Q4-RANK-AND-2Q-PROFILE',
    'new_residual_kernel': 'R33-BR2A-INDEX512-ELEMENTARY-ONE-INTEGRAL-ORBIT-PLUS-NONELEMENTARY-K1K2-98118129984-Q2SUPPORT-CANDIDATES',
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
(HERE / 'nonelementary-k12-q2-support-reduction.json').write_text(json.dumps(cert, indent=2, sort_keys=True) + '\n')
print(json.dumps({
    'success': True,
    'k1_before': summary['1']['Q8_structural_H_before_Q2_support'],
    'k1_after': summary['1']['structural_H_after_endpoint_Q2_support_necessary_condition'],
    'k2_before': summary['2']['Q8_structural_H_before_Q2_support'],
    'k2_after': summary['2']['structural_H_after_endpoint_Q2_support_necessary_condition'],
    'combined_after': grand_after,
    'certificate_sha256': cert['canonical_sha256'],
    'next': cert['next_exact_leaf'],
}, indent=2, sort_keys=True))
