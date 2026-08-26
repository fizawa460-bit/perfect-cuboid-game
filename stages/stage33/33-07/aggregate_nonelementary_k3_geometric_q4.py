#!/usr/bin/env python3
"""Aggregate all pure-geometric k=3 full-Q[4] shards exactly."""
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHARD_COUNT = 32
MANIFEST = HERE / 'nonelementary-k3-geometric-q4-manifest.json'
shard_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE
manifest = json.loads(MANIFEST.read_text())
if manifest.get('schema') != 'STAGE33_07_NONELEMENTARY_K3_GEOMETRIC_Q4_MANIFEST_V1':
    raise SystemExit('manifest schema regression')
if manifest.get('weighted_structural_H_count') != 113246208:
    raise SystemExit('manifest weighted universe moved')

files = sorted(shard_dir.glob('nonelementary-k3-geometric-q4-shard-*.json'))
if len(files) != SHARD_COUNT:
    raise SystemExit(f'expected {SHARD_COUNT} shard files, found {len(files)}')
seen = set()
by_orbit = {
    int(record['orbit_index']): {
        'orbit_size': int(record['orbit_size']),
        't': int(record['t']),
        'target_theta_image_rank': int(record['target_theta_image_rank']),
        'representative_section_count': int(record['representative_section_count']),
        'checked': 0,
        'survivors': 0,
        'rank_hist': Counter(),
        'first_survivors': [],
    }
    for record in manifest['records']
}
manifest_hash = manifest['canonical_sha256']
for path in files:
    shard = json.loads(path.read_text())
    if shard.get('schema') != 'STAGE33_07_NONELEMENTARY_K3_GEOMETRIC_Q4_SHARD_V1':
        raise SystemExit(f'shard schema regression: {path}')
    if shard.get('manifest_sha256') != manifest_hash or shard.get('shard_count') != SHARD_COUNT:
        raise SystemExit(f'shard source/count regression: {path}')
    if shard.get('arithmetic_generators_used') != []:
        raise SystemExit(f'arithmetic firewall crossed: {path}')
    index = int(shard['shard_index'])
    if index in seen or not (0 <= index < SHARD_COUNT):
        raise SystemExit('duplicate/invalid shard index')
    seen.add(index)
    for record in shard['records']:
        orbit = int(record['orbit_index'])
        if orbit not in by_orbit:
            raise SystemExit('unknown orbit in shard')
        out = by_orbit[orbit]
        if int(record['orbit_size']) != out['orbit_size'] or int(record['t']) != out['t']:
            raise SystemExit('orbit metadata moved across shard')
        out['checked'] += int(record['assignments_checked'])
        out['survivors'] += int(record['representative_section_survivors'])
        for key, value in record['theta_rank_histogram'].items():
            out['rank_hist'][int(key)] += int(value)
        for free_mask in record.get('first_survivor_free_masks', []):
            if len(out['first_survivors']) < 64:
                out['first_survivors'].append({'shard_index': index, 'free_mask': int(free_mask)})

if seen != set(range(SHARD_COUNT)):
    raise SystemExit('shard index coverage incomplete')

records = []
representative_checked = 0
representative_survivors = 0
weighted_checked = 0
weighted_survivors = 0
for orbit in sorted(by_orbit):
    out = by_orbit[orbit]
    if out['checked'] != out['representative_section_count']:
        raise SystemExit(f'orbit {orbit} section coverage incomplete')
    representative_checked += out['checked']
    representative_survivors += out['survivors']
    weighted_checked += out['orbit_size'] * out['checked']
    weighted_survivors += out['orbit_size'] * out['survivors']
    records.append({
        'orbit_index': orbit,
        'orbit_size': out['orbit_size'],
        't': out['t'],
        'target_theta_image_rank': out['target_theta_image_rank'],
        'representative_sections_checked': out['checked'],
        'representative_section_survivors': out['survivors'],
        'weighted_H_checked': out['orbit_size'] * out['checked'],
        'weighted_H_survivors': out['orbit_size'] * out['survivors'],
        'theta_rank_histogram': {str(k): v for k, v in sorted(out['rank_hist'].items())},
        'first_survivors': out['first_survivors'],
    })

if representative_checked != 12582912:
    raise SystemExit('aggregate representative coverage regression')
if weighted_checked != 113246208:
    raise SystemExit('aggregate weighted-H coverage regression')

certificate = {
    'schema': 'STAGE33_07_NONELEMENTARY_K3_GEOMETRIC_FULL_Q4_AGGREGATE_V1',
    'source_manifest_sha256': manifest_hash,
    'arithmetic_generators_used': [],
    'firewall': 'NO_ARITHMETIC_CC_CT_USED_IN_PREDECESSOR_MANIFEST_SHARDS_OR_AGGREGATE',
    'shard_count': SHARD_COUNT,
    'orbit_count': 4,
    'representative_sections_checked': representative_checked,
    'representative_section_survivors': representative_survivors,
    'weighted_structural_H_checked': weighted_checked,
    'weighted_structural_H_survivors': weighted_survivors,
    'records': records,
    'all_four_orbit_affine_sections_exhausted': True,
    'full_Q4_condition_certified_for_k3': True,
    'k3_abstract_type_rejected': weighted_survivors == 0,
    'non_elementary_abstract_types_after_k3_geometric_Q4': 2 if weighted_survivors == 0 else 3,
    'remaining_non_elementary_types_if_k3_rejected': [
        'Z/4 direct_sum (Z/2)^7',
        '(Z/4)^2 direct_sum (Z/2)^5',
    ] if weighted_survivors == 0 else None,
    'actual_index512_glue_identified': False,
    'endpoint_finite_q_certified': False,
    'endpoint_full_action_certified': False,
    'arithmetic_HS_closed': False,
    'next_exact_leaf': (
        'L33-07-PURE-GEOMETRIC-FULL-Q4-ON-K1-K2-SUPPORT-SURVIVORS'
        if weighted_survivors == 0 else
        'L33-07-FINITE-Q-REFINE-K3-GEOMETRIC-Q4-SURVIVORS'
    ),
    'unit_status': 'RUNNING_REPAIR',
    'stage33_progress': '6/11',
    'stage33_08_released': False,
    'stage33_09_released': False,
    'theorem_credit': False,
    'endpoint_credit': False,
    'perfect_cuboid_nonexistence_claim': False,
}
raw = json.dumps(certificate, sort_keys=True, separators=(',', ':')).encode()
certificate['canonical_sha256'] = hashlib.sha256(raw).hexdigest()
out_path = HERE / 'nonelementary-k3-geometric-full-q4-aggregate.json'
out_path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + '\n')
print(json.dumps({
    'success': True,
    'representative_checked': representative_checked,
    'weighted_checked': weighted_checked,
    'representative_survivors': representative_survivors,
    'weighted_survivors': weighted_survivors,
    'k3_rejected': certificate['k3_abstract_type_rejected'],
    'certificate_sha256': certificate['canonical_sha256'],
}, indent=2, sort_keys=True))
