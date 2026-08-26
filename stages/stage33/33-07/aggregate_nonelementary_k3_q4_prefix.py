#!/usr/bin/env python3
"""Aggregate the complete exact-prefix k=3 target-Q[4] census.

This aggregator reconstructs the expected 4,608 six-bit prefix tasks directly
from the manifest and requires exact set equality with the sixteen shard
outputs.  It also reconstructs the expected assignment count in every prefix,
so duplicate, missing, or partially traversed prefixes cannot receive credit.

If every t=1 representative section fails the exact target theta-image rank
condition, the proved integral order-288 symmetry transports that rejection to
every skeleton in its orbit.  The t=2 fibres are already rejected by the
section-independent rank-3 theta subgroup versus target rank 2.  Only then is
the entire k=3 abstract type certified impossible.
"""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHARD_DIR = HERE / 'q4-prefix-shards'
MANIFEST = json.loads((HERE / 'nonelementary-k3-q4-prefix-manifest.json').read_text())
EXPECTED_PRED = 'c18334f94a9b71fc611b7bfdc3c0291125aee09a67ce7267882ae62713847b1b'
SHARD_COUNT = 16
PREFIX_BITS = 6

if MANIFEST.get('schema') != 'STAGE33_07_NONELEMENTARY_K3_Q4_PREFIX_MANIFEST_V1':
    raise SystemExit('k3 Q4 prefix manifest schema regression')
if MANIFEST.get('source_integral_cc_ct_sha256') != EXPECTED_PRED:
    raise SystemExit('k3 integral cc/ct predecessor lock moved')
if not MANIFEST.get('prefix_sharding_disjointness_and_coverage_required'):
    raise SystemExit('manifest completeness firewall disabled')
if MANIFEST.get('fast_or_heuristic_traversal_used'):
    raise SystemExit('fast/heuristic traversal forbidden')
if MANIFEST.get('canonical_augmentation_completeness_claimed'):
    raise SystemExit('canonical augmentation completeness must remain false')

expected_tasks = {}
t1_records = sorted(
    (record for record in MANIFEST['records'] if int(record['t']) == 1),
    key=lambda record: int(record['skeleton_orbit_index']),
)
t2_records = [record for record in MANIFEST['records'] if int(record['t']) == 2]
if len(t1_records) != 72 or len(t2_records) != 117:
    raise SystemExit('k3 t-profile manifest regression')
for record in t1_records:
    skeleton = int(record['skeleton_orbit_index'])
    dimension = int(record['integral_cc_ct_lift_dimension'])
    if dimension < PREFIX_BITS:
        raise SystemExit('prefix longer than affine fibre dimension')
    per_prefix = 1 << (dimension - PREFIX_BITS)
    for prefix in range(1 << PREFIX_BITS):
        task_id = f'{skeleton}:{prefix}'
        if task_id in expected_tasks:
            raise SystemExit('duplicate expected prefix task')
        expected_tasks[task_id] = per_prefix
if len(expected_tasks) != 4608:
    raise SystemExit('expected prefix task-count regression')
if sum(expected_tasks.values()) != 7471104:
    raise SystemExit('expected t1 representative-section count regression')

files = sorted(SHARD_DIR.glob('nonelementary-k3-q4-prefix-shard-*.json'))
if len(files) != SHARD_COUNT:
    raise SystemExit(f'expected {SHARD_COUNT} shard files, found {len(files)}')
seen_indexes = set()
seen_tasks = {}
assignments_checked = 0
obstruction_one_count = 0
obstruction_zero_count = 0
fallback_histogram = {}
survivors = []
shard_locks = {}
for path in files:
    shard = json.loads(path.read_text())
    if shard.get('schema') != 'STAGE33_07_NONELEMENTARY_K3_Q4_PREFIX_SHARD_V1':
        raise SystemExit(f'shard schema regression: {path.name}')
    if shard.get('manifest_sha256') != MANIFEST['canonical_sha256']:
        raise SystemExit(f'manifest SHA mismatch: {path.name}')
    if int(shard.get('shard_count', -1)) != SHARD_COUNT:
        raise SystemExit(f'shard-count regression: {path.name}')
    index = int(shard['shard_index'])
    if index in seen_indexes or not (0 <= index < SHARD_COUNT):
        raise SystemExit('duplicate/invalid shard index')
    seen_indexes.add(index)
    shard_locks[str(index)] = shard['canonical_sha256']
    tasks = shard['task_ids']
    task_counts = shard['task_assignment_counts']
    if len(tasks) != int(shard['task_count']) or len(tasks) != 288:
        raise SystemExit(f'per-shard task-count regression shard {index}')
    if set(tasks) != set(task_counts):
        raise SystemExit(f'shard task/count key mismatch shard {index}')
    if int(shard['assignments_checked']) != sum(int(x) for x in task_counts.values()):
        raise SystemExit(f'partial prefix traversal shard {index}')
    if (int(shard['obstruction_one_count']) + int(shard['obstruction_zero_count'])
            != int(shard['assignments_checked'])):
        raise SystemExit(f'obstruction accounting regression shard {index}')
    for task_id in tasks:
        if task_id in seen_tasks:
            raise SystemExit(f'duplicate executed prefix task {task_id}')
        seen_tasks[task_id] = int(task_counts[task_id])
    assignments_checked += int(shard['assignments_checked'])
    obstruction_one_count += int(shard['obstruction_one_count'])
    obstruction_zero_count += int(shard['obstruction_zero_count'])
    for rank_value, count in shard['fallback_full_theta_rank_histogram'].items():
        fallback_histogram[rank_value] = fallback_histogram.get(rank_value, 0) + int(count)
    survivors.extend(shard['q4_survivors'])

if seen_indexes != set(range(SHARD_COUNT)):
    raise SystemExit('shard-index coverage regression')
if set(seen_tasks) != set(expected_tasks):
    missing = sorted(set(expected_tasks) - set(seen_tasks))[:10]
    extra = sorted(set(seen_tasks) - set(expected_tasks))[:10]
    raise SystemExit(f'prefix task-set coverage failure missing={missing} extra={extra}')
for task_id, expected in expected_tasks.items():
    if seen_tasks[task_id] != expected:
        raise SystemExit(f'prefix assignment-count mismatch {task_id}')
if assignments_checked != 7471104:
    raise SystemExit('global t1 assignment coverage regression')
if obstruction_one_count + obstruction_zero_count != assignments_checked:
    raise SystemExit('global obstruction accounting regression')

# t=2 requires no section traversal: the exact fixed theta subgroup has rank 3
# on every fibre while target rank is 2.  The manifest reconstructs the full
# predecessor counts with skeleton-orbit weights.
t2_weighted = int(MANIFEST['t2_weighted_structural_H_count'])
t1_weighted = int(MANIFEST['t1_weighted_structural_H_count'])
if t2_weighted != 463994880 or t1_weighted != 108527616:
    raise SystemExit('weighted k3 predecessor profile regression')
if t1_weighted + t2_weighted != 572522496:
    raise SystemExit('weighted k3 predecessor total regression')

survivor_count = len(survivors)
k3_rejected = survivor_count == 0
certificate = {
    'schema': 'STAGE33_07_NONELEMENTARY_K3_FULL_Q4_PREFIX_CENSUS_V1',
    'manifest_sha256': MANIFEST['canonical_sha256'],
    'source_integral_cc_ct_sha256': EXPECTED_PRED,
    'shard_certificate_sha256': dict(sorted(shard_locks.items(), key=lambda x: int(x[0]))),
    'shard_count': SHARD_COUNT,
    'prefix_bits': PREFIX_BITS,
    'expected_prefix_task_count': len(expected_tasks),
    'executed_prefix_task_count': len(seen_tasks),
    'prefix_task_sets_exactly_equal': True,
    'prefixes_pairwise_disjoint': True,
    't1_representative_sections_expected': 7471104,
    't1_representative_sections_checked': assignments_checked,
    't1_all_representative_sections_checked_exactly_once': True,
    't1_obstruction_one_count': obstruction_one_count,
    't1_obstruction_zero_fallback_count': obstruction_zero_count,
    'fallback_full_theta_rank_histogram': dict(sorted(fallback_histogram.items())),
    't1_q4_survivor_count': survivor_count,
    't1_q4_survivors': survivors,
    't2_skeleton_orbits_rejected_by_fixed_rank3_vs_target_rank2': 117,
    't2_weighted_structural_H_rejected': t2_weighted,
    't1_weighted_structural_H_predecessor': t1_weighted,
    'k3_predecessor_structural_H': 572522496,
    'k3_predecessor_full_symmetry_orbits': 17146944,
    'integral_order_288_symmetry_transports_Q4_condition': True,
    'full_target_Q4_condition_certified_for_k3': True,
    'k3_abstract_type_rejected': k3_rejected,
    'non_elementary_abstract_types_before_k3_Q4': 3,
    'non_elementary_abstract_types_after_k3_Q4': 2 if k3_rejected else 3,
    'surviving_non_elementary_types': [
        'Z/4 direct_sum (Z/2)^7',
        '(Z/4)^2 direct_sum (Z/2)^5',
    ] + ([] if k3_rejected else ['(Z/4)^3 direct_sum (Z/2)^3']),
    'fast_or_heuristic_traversal_used': False,
    'canonical_augmentation_completeness_claimed': False,
    'representatives_materialized_count_claimed': False,
    'endpoint_finite_q_certified_for_remaining_types': False,
    'endpoint_full_action_conjugacy_certified_for_remaining_types': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'stage33_progress': '6/11',
    'stage33_08_released': False,
    'stage33_09_released': False,
    'endpoint_credit': False,
    'perfect_cuboid_nonexistence_claim': False,
    'next_exact_leaf': (
        'L33-07-DERIVE-TYPE-WIDE-Q4-Q-FILTRATION-OBSTRUCTIONS-FOR-K1-K2'
        if k3_rejected else
        'L33-07-ANALYZE-EXACT-K3-Q4-SURVIVORS-BEFORE-FINITE-Q-ACTION'
    ),
}
raw = json.dumps(certificate, sort_keys=True, separators=(',', ':')).encode()
certificate['canonical_sha256'] = hashlib.sha256(raw).hexdigest()
(HERE / 'nonelementary-k3-full-q4-prefix-census.json').write_text(
    json.dumps(certificate, indent=2, sort_keys=True) + '\n')
print(json.dumps({
    'success': True,
    'prefix_tasks': len(seen_tasks),
    't1_sections_checked': assignments_checked,
    'obstruction_zero_fallbacks': obstruction_zero_count,
    'q4_survivors': survivor_count,
    'k3_abstract_type_rejected': k3_rejected,
    'certificate_sha256': certificate['canonical_sha256'],
    'next': certificate['next_exact_leaf'],
}, indent=2, sort_keys=True))
