#!/usr/bin/env python3
"""Aggregate exact K1 seven-sign evidence: 32-way for P!=7 and 128-way rescue for P=7."""
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLD = HERE / 'k1-geometric-sign-fixed-old32-subshards'
NEW = HERE / 'k1-geometric-sign-fixed-p7-rescue128-subshards'


def rehash(doc):
    d = dict(doc)
    stored = d.pop('canonical_sha256', None)
    got = hashlib.sha256(json.dumps(d, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return stored, got


def load_dir(root, *, rescued_p7):
    out = []
    for f in sorted(root.glob('nonelementary-k1-geometric-sign-fixed-p*-s*.json')):
        d = json.loads(f.read_text())
        p = int(d.get('p_orbit_index', -1))
        if rescued_p7 and p != 7:
            raise SystemExit(f'non-P7 file in rescue128 directory: {f.name}')
        if not rescued_p7 and p == 7:
            continue
        out.append((f, d))
    return out

old_docs = load_dir(OLD, rescued_p7=False)
new_docs = load_dir(NEW, rescued_p7=True)
expected_old = {(p, q) for p in range(15) if p != 7 for q in range(32)}
expected_new = {(7, q) for q in range(128)}

seen_old = set()
seen_new = set()
reject = Counter()
checked = weighted = surv = wsurv = group_match = 0
support_locks = {}
endpoint_lock = None
perp = defaultdict(lambda: {
    'subshards': 0,
    'owned_records': 0,
    'owned_pairs': 0,
    'checked': 0,
    'weighted': 0,
    'survivors': 0,
    'weighted_survivors': 0,
})

for rescued_p7, docs in ((False, old_docs), (True, new_docs)):
    for f, d in docs:
        stored, got = rehash(d)
        if stored != got:
            raise SystemExit(f'subshard hash regression: {f.name}')
        if d.get('schema') != 'STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SIGN_FIXED_SUBSHARD_V1':
            raise SystemExit(f'subshard schema regression: {f.name}')
        if d.get('arithmetic_generators_used') != []:
            raise SystemExit(f'arithmetic-generator firewall regression: {f.name}')

        p = int(d['p_orbit_index'])
        q = int(d['record_shard_index'])
        n = int(d['record_shard_count'])
        want_n = 128 if p == 7 else 32
        if n != want_n or not (0 <= p < 15) or not (0 <= q < n):
            raise SystemExit(f'partition identity regression: {f.name}')
        if rescued_p7 != (p == 7):
            raise SystemExit(f'partition source regression: {f.name}')
        seen = seen_new if p == 7 else seen_old
        if (p, q) in seen:
            raise SystemExit(f'duplicate subshard {(p, q)}')
        seen.add((p, q))

        support_locks.setdefault(str(p), d['source_support_sha256'])
        if support_locks[str(p)] != d['source_support_sha256']:
            raise SystemExit(f'support lock inconsistent in P{p}')
        endpoint_lock = endpoint_lock or d['source_endpoint_sha256']
        if endpoint_lock != d['source_endpoint_sha256']:
            raise SystemExit('endpoint lock inconsistent')

        if d.get('target_fixed_Q2_log2') != [12] * 7 or d.get('target_fixed_Q4_log2') != [14] * 7:
            raise SystemExit(f'endpoint filtration regression: {f.name}')
        if d.get('target_quotient_power_torsion_log2') != {'2': 14, '4': 24, '8': 28}:
            raise SystemExit(f'endpoint group-type target regression: {f.name}')
        if not d.get('endpoint_finite_group_type_filter_enforced') or not d.get('all_survivors_have_endpoint_finite_group_type'):
            raise SystemExit(f'endpoint group-type firewall regression: {f.name}')
        if not d.get('all_owned_lift_sections_decided_exactly_once') or d.get('fast_or_heuristic_traversal_used'):
            raise SystemExit(f'exactness regression: {f.name}')
        if d.get('actual_index512_glue_identified') or d.get('arithmetic_HS_closed') or d.get('stage33_progress') != '6/11':
            raise SystemExit(f'Stage33 promotion firewall regression: {f.name}')

        checked += int(d['representative_lift_sections_checked'])
        weighted += int(d['weighted_H_checked'])
        surv += int(d['representative_section_survivors'])
        wsurv += int(d['weighted_H_survivors'])
        group_match += int(d['endpoint_finite_group_type_matches_before_signs'])
        reject.update({k: int(v) for k, v in d['rejection_counts'].items()})

        z = perp[p]
        z['subshards'] += 1
        z['owned_records'] += int(d['owned_record_count'])
        z['owned_pairs'] += int(d['owned_pair_skeleton_count'])
        z['checked'] += int(d['representative_lift_sections_checked'])
        z['weighted'] += int(d['weighted_H_checked'])
        z['survivors'] += int(d['representative_section_survivors'])
        z['weighted_survivors'] += int(d['weighted_H_survivors'])
        z.setdefault('source_records', int(d['source_fixed_P_W_orbit_count']))
        z.setdefault('source_pairs', int(d['source_full_pair_skeletons_covered']))
        z.setdefault('source_weighted', int(d['source_weighted_structural_H_covered']))
        if (z['source_records'], z['source_pairs'], z['source_weighted']) != (
            int(d['source_fixed_P_W_orbit_count']),
            int(d['source_full_pair_skeletons_covered']),
            int(d['source_weighted_structural_H_covered']),
        ):
            raise SystemExit(f'source P metadata inconsistent in P{p}')

if seen_old != expected_old:
    missing = sorted(expected_old - seen_old)[:20]
    extra = sorted(seen_old - expected_old)[:20]
    raise SystemExit(f'old32 coverage regression missing={missing} extra={extra}')
if seen_new != expected_new:
    missing = sorted(expected_new - seen_new)[:20]
    extra = sorted(seen_new - expected_new)[:20]
    raise SystemExit(f'P7 rescue128 coverage regression missing={missing} extra={extra}')

support_orbits = pair_total = source_weighted_total = 0
for p in range(15):
    z = perp[p]
    want = 128 if p == 7 else 32
    if z['subshards'] != want:
        raise SystemExit(f'P{p} subshard-count regression {z}')
    if z['owned_records'] != z['source_records'] or z['owned_pairs'] != z['source_pairs']:
        raise SystemExit(f'P{p} record/pair partition regression {z}')
    if z['checked'] != 64 * z['source_records']:
        raise SystemExit(f'P{p} representative-section coverage regression')
    if z['weighted'] != z['source_weighted'] or z['source_weighted'] != 64 * z['source_pairs']:
        raise SystemExit(f'P{p} weighted coverage regression')
    support_orbits += z['source_records']
    pair_total += z['source_pairs']
    source_weighted_total += z['source_weighted']

if pair_total != 20487593 or source_weighted_total != 1311205952:
    raise SystemExit(f'global predecessor coverage regression {(pair_total, source_weighted_total)}')
if checked != 64 * support_orbits or weighted != source_weighted_total:
    raise SystemExit('global section/weight accounting regression')
if sum(reject.values()) + surv != checked or group_match < surv:
    raise SystemExit('global rejection/survivor accounting regression')

zero = surv == 0 and wsurv == 0
group_rejections = sum(v for k, v in reject.items() if k.startswith('GROUP_TYPE_'))
sign_only_zero = zero and group_rejections == 0
cert = {
    'schema': 'STAGE33_07_NONELEMENTARY_K1_GEOMETRIC_SIGN_FIXED_MIXED_RESCUE_CENSUS_V1',
    'partition_count_by_P_orbit': {str(p): (128 if p == 7 else 32) for p in range(15)},
    'rescued_P_orbit_index': 7,
    'source_rescue32_workflow_run_id_for_P_not_7': 33004278066,
    'source_support_shard_sha256': support_locks,
    'source_endpoint_sha256': endpoint_lock,
    'arithmetic_generators_used': [],
    'geometric_coordinate_sign_family_enforced': 7,
    'eligible_rank_one_E7_P_count': 63,
    'exact_P_orbit_count': 15,
    'support_skeleton_count': pair_total,
    'exact_support_skeleton_orbit_count': support_orbits,
    'representative_lift_sections_checked': checked,
    'weighted_H_checked': weighted,
    'endpoint_finite_group_type_matches_before_signs': group_match,
    'target_quotient_power_torsion_log2': {'2': 14, '4': 24, '8': 28},
    'endpoint_finite_group_type_filter_certified': True,
    'rejection_counts': dict(sorted(reject.items())),
    'finite_group_type_rejection_count': group_rejections,
    'representative_section_survivors': surv,
    'weighted_H_survivors': wsurv,
    'all_14x32_old_and_P7x128_rescue_subshards_present_exactly_once': True,
    'all_support_orbit_representative_lifts_checked_exactly_once': True,
    'all_1311205952_weighted_structural_H_covered_exactly': weighted == 1311205952,
    'full_affine_fixed_filtration_census_certified': True,
    'all_survivors_have_endpoint_finite_group_type': True,
    'k1_nonelementary_type_rejected_by_geometric_sign_fixed_filtration_alone': sign_only_zero,
    'k1_nonelementary_type_rejected_by_endpoint_group_type_or_geometric_sign_fixed_filtration': zero,
    'k1_nonelementary_type_rejected': zero,
    'full_finite_q_isometry_certified': False,
    'endpoint_full_action_certified': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'next_exact_leaf': (
        'L33-07-INTEGRATE-K1-K2-K3-GEOMETRIC-REJECTIONS-WITH-INDEX512-GLUE-BRIDGE'
        if zero else
        'L33-07-FULL-FINITE-Q-PLUS-SEVEN-SIGN-CONJUGACY-ON-K1-SURVIVORS'
    ),
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
out = HERE / 'nonelementary-k1-geometric-sign-fixed-p7-rescue128-census.json'
out.write_text(json.dumps(cert, indent=2, sort_keys=True) + '\n')
print(json.dumps({
    'success': True,
    'partition_count_P7': 128,
    'partition_count_other_P': 32,
    'representative_sections_checked': checked,
    'weighted_H_checked': weighted,
    'survivors': surv,
    'weighted_survivors': wsurv,
    'k1_rejected': zero,
    'sha256': cert['canonical_sha256'],
    'next': cert['next_exact_leaf'],
}, indent=2, sort_keys=True))
