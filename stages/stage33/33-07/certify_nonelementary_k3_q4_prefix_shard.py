#!/usr/bin/env python3
"""Exact prefix shard for the k=3 full target-Q[4] image-order condition.

Consumes the complete manifest produced by
``prepare_nonelementary_k3_q4_prefix_manifest.py``.  Only t=1 fibres require
section enumeration: t=2 is already rejected by a section-independent theta
image of rank 3 while the endpoint target rank is 2.

The t=1 universe consists of 72 exact skeleton-orbit representatives.  Each
filtered affine fibre is partitioned by the first six free variables into 64
disjoint prefixes.  Across all shards this covers all 4,608 prefixes and all
7,471,104 representative sections exactly once.

For every section the manifest supplies a theta generator and a functional on
Hom(H,F2) annihilating the fixed rank-3 theta subgroup.  If that obstruction
bit is one, the section cannot have target theta rank 3.  If the bit is ever
zero, this shard falls back to constructing the complete theta image and
computing its exact F2 rank, so correctness does not depend on the selector
being constant on a fibre.

No canonical augmentation, sampling, or heuristic traversal is used.
"""
import hashlib
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'nonelementary-k3-q4-prefix-manifest.json'
NVAR = 24
PREFIX_BITS = 6
X_MASK = (1 << 10) - 1

shard_index = int(os.environ.get('SHARD_INDEX', '0'))
shard_count = int(os.environ.get('SHARD_COUNT', '16'))
if shard_count <= 0 or not (0 <= shard_index < shard_count):
    raise SystemExit('invalid shard index/count')

manifest = json.loads(MANIFEST.read_text())
if manifest.get('schema') != 'STAGE33_07_NONELEMENTARY_K3_Q4_PREFIX_MANIFEST_V1':
    raise SystemExit('k3 Q4 prefix manifest schema regression')
if manifest.get('source_integral_cc_ct_sha256') != 'c18334f94a9b71fc611b7bfdc3c0291125aee09a67ce7267882ae62713847b1b':
    raise SystemExit('k3 Q4 prefix predecessor lock moved')
if manifest.get('prefix_bits') != PREFIX_BITS or manifest.get('t1_prefix_task_count') != 4608:
    raise SystemExit('prefix-universe regression')
if manifest.get('t1_representative_section_count') != 7471104:
    raise SystemExit('t1 section-universe regression')


def canon(rows):
    pivots = {}
    for value in rows:
        x = int(value)
        for pivot in sorted(pivots, reverse=True):
            if (x >> pivot) & 1:
                x ^= pivots[pivot]
        if not x:
            continue
        pivot = x.bit_length() - 1
        for old in list(pivots):
            if (pivots[old] >> pivot) & 1:
                pivots[old] ^= x
        pivots[pivot] = x
    return tuple(pivots[p] for p in sorted(pivots, reverse=True))


def rank(rows):
    return len(canon(rows))


def complement(base_basis, whole_basis):
    current = list(canon(base_basis))
    result = []
    for vector in canon(whole_basis):
        if rank(current + [vector]) > len(current):
            current.append(vector)
            result.append(vector)
    return tuple(result)


def free_variables(reduced):
    pivots = set()
    for value in reduced:
        coefficient = int(value) & ((1 << NVAR) - 1)
        if not coefficient:
            raise SystemExit('zero row in canonical affine RREF')
        pivots.add(coefficient.bit_length() - 1)
    return tuple(i for i in range(NVAR) if i not in pivots)


def solution_from_free(reduced, free_mask):
    free = free_variables(reduced)
    if int(free_mask) >= (1 << len(free)):
        raise SystemExit('free assignment exceeds affine dimension')
    solution = 0
    for j, variable in enumerate(free):
        if (int(free_mask) >> j) & 1:
            solution |= 1 << variable
    for value in reversed(reduced):
        coefficient = int(value) & ((1 << NVAR) - 1)
        pivot = coefficient.bit_length() - 1
        rhs = ((int(value) >> NVAR) & 1) ^ ((coefficient & solution).bit_count() & 1)
        if rhs:
            solution |= 1 << pivot
    for value in reduced:
        coefficient = int(value) & ((1 << NVAR) - 1)
        rhs = (int(value) >> NVAR) & 1
        if ((coefficient & solution).bit_count() & 1) != rhs:
            raise SystemExit('affine solution reconstruction regression')
    return solution


def add_mod4(left, right):
    return tuple((int(a) + int(b)) % 4 for a, b in zip(left, right))


def add_selected_rows(rows, coefficient_mask):
    result = (0,) * 14
    for i, row in enumerate(rows):
        if (int(coefficient_mask) >> i) & 1:
            result = add_mod4(result, row)
    return result


def h_generators(p_basis, w_basis, quotient_basis, solution):
    order_four = []
    for generator, p in enumerate(p_basis):
        correction = 0
        for bit, vector in enumerate(quotient_basis):
            if (int(solution) >> (8 * generator + bit)) & 1:
                correction ^= int(vector)
        order_four.append(tuple(
            (((int(p) >> coordinate) & 1) + 2 * ((correction >> coordinate) & 1)) % 4
            for coordinate in range(14)
        ))
    w_complement = complement(p_basis, w_basis)
    if len(w_complement) != 3:
        raise SystemExit('k3 W/P complement rank regression')
    order_two = [tuple(2 * ((int(w) >> coordinate) & 1) for coordinate in range(14))
                 for w in w_complement]
    return tuple(order_four + order_two)


def kernel_coefficients(p_basis):
    return canon(
        coefficient for coefficient in range(1, 1 << 3)
        if all(
            sum(((coefficient >> i) & 1) * ((int(p_basis[i]) >> coordinate) & 1)
                for i in range(3)) % 2 == 0
            for coordinate in range(10)
        )
    )


def root_mod4(u):
    root = [0] * 14
    for coordinate in range(10):
        if int(u[coordinate]) % 2:
            raise SystemExit('fourth-root X parity regression')
        root[coordinate] = (int(u[coordinate]) // 2) % 2
    for coordinate in range(10, 14):
        root[coordinate] = int(u[coordinate]) % 4
    return tuple(root)


def functional_mask_even(root, h):
    mask = 0
    for generator, row in enumerate(h):
        value = sum(int(root[i]) * int(row[i]) for i in range(14)) % 4
        # Maximal target Q[2] gives 2R <= H^perp, hence every theta value is
        # order at most two and this normalized numerator is even.
        if value % 2:
            raise SystemExit('theta image lost exponent two')
        if (value // 2) & 1:
            mask |= 1 << generator
    return mask


def selected_theta_mask(record, solution):
    p_basis = tuple(int(x) for x in record['P_basis_bits'])
    w_basis = tuple(int(x) for x in record['W_basis_bits'])
    quotient_basis = tuple(int(x) for x in record['quotient_basis_bits'])
    h = h_generators(p_basis, w_basis, quotient_basis, solution)
    index = int(record['selected_theta_generator_index'])
    if index < 10:
        root = [0] * 14
        root[index] = 2
        return functional_mask_even(tuple(root), h)
    if index < 16:
        w = w_basis[index - 10]
        u = tuple(2 * ((int(w) >> coordinate) & 1) for coordinate in range(14))
        return functional_mask_even(root_mod4(u), h)
    coefficients = kernel_coefficients(p_basis)
    local = index - 16
    if not (0 <= local < len(coefficients)):
        raise SystemExit('selected theta kernel-generator index regression')
    u = add_selected_rows(h[:3], coefficients[local])
    return functional_mask_even(root_mod4(u), h)


def full_theta_masks(record, solution):
    p_basis = tuple(int(x) for x in record['P_basis_bits'])
    w_basis = tuple(int(x) for x in record['W_basis_bits'])
    quotient_basis = tuple(int(x) for x in record['quotient_basis_bits'])
    h = h_generators(p_basis, w_basis, quotient_basis, solution)
    masks = []
    for coordinate in range(10):
        root = [0] * 14
        root[coordinate] = 2
        masks.append(functional_mask_even(tuple(root), h))
    for w in w_basis:
        u = tuple(2 * ((int(w) >> coordinate) & 1) for coordinate in range(14))
        masks.append(functional_mask_even(root_mod4(u), h))
    for coefficients in kernel_coefficients(p_basis):
        u = add_selected_rows(h[:3], coefficients)
        masks.append(functional_mask_even(root_mod4(u), h))
    return tuple(masks)


t1_records = [record for record in manifest['records'] if int(record['t']) == 1]
if len(t1_records) != 72:
    raise SystemExit('t1 skeleton-orbit count regression')

task_ids = []
assignments_checked = 0
obstruction_one_count = 0
obstruction_zero_count = 0
fallback_rank_histogram = {}
q4_survivors = []
task_assignment_counts = {}

# Deterministic global task order.  Modulo assignment gives disjoint shards and
# lets the aggregate reconstruct the complete expected task set independently.
global_task_index = 0
for record in sorted(t1_records, key=lambda x: int(x['skeleton_orbit_index'])):
    skeleton_index = int(record['skeleton_orbit_index'])
    reduced = tuple(int(x) for x in record['filtered_affine_rref_augmented'])
    dimension = int(record['integral_cc_ct_lift_dimension'])
    if dimension != len(free_variables(reduced)) or dimension < PREFIX_BITS:
        raise SystemExit('filtered affine dimension regression')
    suffix_bits = dimension - PREFIX_BITS
    per_prefix = 1 << suffix_bits
    for prefix in range(1 << PREFIX_BITS):
        task_id = f'{skeleton_index}:{prefix}'
        owner = global_task_index % shard_count
        global_task_index += 1
        if owner != shard_index:
            continue
        task_ids.append(task_id)
        task_assignment_counts[task_id] = per_prefix
        annihilator = int(record['selected_fixed_annihilator_mask'])
        target_rank = int(record['target_theta_image_rank'])
        if target_rank != 3:
            raise SystemExit('t1 target rank regression')
        for suffix in range(1 << suffix_bits):
            free_mask = prefix | (suffix << PREFIX_BITS)
            solution = solution_from_free(reduced, free_mask)
            selected = selected_theta_mask(record, solution)
            obstruction = (int(selected) & annihilator).bit_count() & 1
            assignments_checked += 1
            if obstruction:
                obstruction_one_count += 1
                continue
            obstruction_zero_count += 1
            theta_rank = rank(full_theta_masks(record, solution))
            fallback_rank_histogram[str(theta_rank)] = fallback_rank_histogram.get(str(theta_rank), 0) + 1
            if theta_rank == target_rank:
                q4_survivors.append({
                    'skeleton_orbit_index': skeleton_index,
                    'prefix': prefix,
                    'suffix': suffix,
                    'free_mask': free_mask,
                    'theta_rank': theta_rank,
                })

if global_task_index != 4608:
    raise SystemExit('global prefix task-count regression')
if len(task_ids) != 4608 // shard_count:
    raise SystemExit('per-shard prefix task-count regression')
if assignments_checked != sum(task_assignment_counts.values()):
    raise SystemExit('shard assignment coverage regression')

certificate = {
    'schema': 'STAGE33_07_NONELEMENTARY_K3_Q4_PREFIX_SHARD_V1',
    'manifest_sha256': manifest['canonical_sha256'],
    'source_integral_cc_ct_sha256': manifest['source_integral_cc_ct_sha256'],
    'shard_index': shard_index,
    'shard_count': shard_count,
    'prefix_bits': PREFIX_BITS,
    'task_ids': task_ids,
    'task_assignment_counts': task_assignment_counts,
    'task_count': len(task_ids),
    'assignments_checked': assignments_checked,
    'obstruction_one_count': obstruction_one_count,
    'obstruction_zero_count': obstruction_zero_count,
    'fallback_full_theta_rank_histogram': dict(sorted(fallback_rank_histogram.items())),
    'q4_survivor_count': len(q4_survivors),
    'q4_survivors': q4_survivors,
    'all_sections_in_owned_prefixes_checked': True,
    'prefixes_disjoint_by_modulo_owner': True,
    'fast_or_heuristic_traversal_used': False,
    'canonical_augmentation_completeness_claimed': False,
    'full_Q4_condition_certified_globally': False,
    'k3_abstract_type_rejected': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'stage33_progress': '6/11',
    'stage33_08_released': False,
    'stage33_09_released': False,
    'endpoint_credit': False,
    'perfect_cuboid_nonexistence_claim': False,
}
raw = json.dumps(certificate, sort_keys=True, separators=(',', ':')).encode()
certificate['canonical_sha256'] = hashlib.sha256(raw).hexdigest()
out = HERE / f'nonelementary-k3-q4-prefix-shard-{shard_index}.json'
out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + '\n')
print(json.dumps({
    'success': True,
    'shard_index': shard_index,
    'tasks': len(task_ids),
    'assignments_checked': assignments_checked,
    'obstruction_zero_count': obstruction_zero_count,
    'q4_survivor_count': len(q4_survivors),
    'certificate_sha256': certificate['canonical_sha256'],
}, indent=2, sort_keys=True))
