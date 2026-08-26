#!/usr/bin/env python3
"""Formally certify exhaustive full-Q[4] image-order filtering on k=1,2.

This deliberately reuses the exhaustive section enumerator: no canonical
augmentation, fast traversal, representative pruning inside an affine fibre,
or heuristic rank shortcut is introduced here.
"""
import hashlib, json, runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
INTEGRAL_CERT_SHA = '902e41ef8e816b57eeb631a293e499ba22d5fcc41ad6f8ddac2c11500b2e6f34'

# Independently rebuild and lock the formally certified predecessor.
runpy.run_path(str(HERE / 'certify_nonelementary_k12_integral_cc_ct.py'))
pre = json.loads((HERE / 'nonelementary-k12-integral-cc-ct-certified.json').read_text())
assert pre['canonical_sha256'] == INTEGRAL_CERT_SHA
assert pre['integral_cc_ct_certified']
assert pre['combined_H_after_integral_cc_ct'] == 14794944
assert pre['k1']['H_after_integral_cc_ct'] == 2928832
assert pre['k2']['H_after_integral_cc_ct'] == 11866112

# Exhaust every affine section using the already-audited exact theta-rank map.
runpy.run_path(str(HERE / 'profile_nonelementary_k12_full_q4.py'))
x = json.loads((HERE / 'nonelementary-k12-full-q4-scout.json').read_text())
assert x['all_affine_sections_exhausted']
assert not x['fast_or_canonical_traversal_used']
assert x['combined_representative_sections_checked'] == 1020880
assert x['combined_weighted_H_checked'] == 14794944
assert x['k1']['representative_sections_checked'] == 142032
assert x['k2']['representative_sections_checked'] == 878848
assert x['k1']['weighted_H_checked'] == 2928832
assert x['k2']['weighted_H_checked'] == 11866112

k1_surv = int(x['k1']['weighted_H_survivors'])
k2_surv = int(x['k2']['weighted_H_survivors'])
combined = k1_surv + k2_surv
assert combined == int(x['combined_weighted_H_survivors'])

cert = {
    'schema': 'STAGE33_07_NONELEMENTARY_K12_FULL_Q4_CERT_V1',
    'source_integral_cc_ct_certificate_sha256': INTEGRAL_CERT_SHA,
    'source_exhaustive_q4_profile_sha256': x['canonical_sha256'],
    'input_weighted_H': 14794944,
    'representative_sections_checked': 1020880,
    'k1': {
        'input_H': 2928832,
        'representative_sections_checked': 142032,
        'full_Q4_surviving_H': k1_surv,
        'type_eliminated_by_full_Q4': k1_surv == 0,
        'theta_rank_histogram': x['k1']['theta_rank_histogram'],
        'target_vs_rank_histogram': x['k1']['target_vs_rank_histogram'],
        'surviving_orbit_records': x['k1']['surviving_orbit_records'],
    },
    'k2': {
        'input_H': 11866112,
        'representative_sections_checked': 878848,
        'full_Q4_surviving_H': k2_surv,
        'type_eliminated_by_full_Q4': k2_surv == 0,
        'theta_rank_histogram': x['k2']['theta_rank_histogram'],
        'target_vs_rank_histogram': x['k2']['target_vs_rank_histogram'],
        'surviving_orbit_records': x['k2']['surviving_orbit_records'],
    },
    'combined_full_Q4_surviving_H': combined,
    'all_affine_sections_exhausted': True,
    'exact_weighted_coverage': True,
    'fast_or_canonical_traversal_used': False,
    'full_Q4_condition_certified': True,
    'all_remaining_nonelementary_types_eliminated_by_full_Q4': combined == 0,
    'endpoint_finite_q_certified': False,
    'endpoint_full_action_certified': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'stage33_progress': '6/11',
    'stage33_08_released': False,
    'stage33_09_released': False,
    'theorem_credit': False,
    'endpoint_credit': False,
    'perfect_cuboid_nonexistence_claim': False,
    'next': ('L33-07-RETURN-TO-ELEMENTARY-OR-ARITHMETIC-HS-RESIDUAL'
             if combined == 0 else
             'L33-07-IMPOSE-ENDPOINT-FINITE-Q-ON-K1K2-FULL-Q4-SURVIVORS'),
}
raw = json.dumps(cert, sort_keys=True, separators=(',', ':')).encode()
cert['canonical_sha256'] = hashlib.sha256(raw).hexdigest()
(HERE / 'nonelementary-k12-full-q4-certified.json').write_text(
    json.dumps(cert, indent=2, sort_keys=True) + '\n'
)
print(json.dumps({
    'success': True,
    'k1_survivors': k1_surv,
    'k2_survivors': k2_surv,
    'combined_survivors': combined,
    'certificate_sha256': cert['canonical_sha256'],
}, indent=2, sort_keys=True))
