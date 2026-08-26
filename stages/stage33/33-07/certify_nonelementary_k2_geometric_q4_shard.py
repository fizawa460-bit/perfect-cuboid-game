#!/usr/bin/env python3
"""Exhaust one shard of the pure-geometric k=2 full-Q[4] census."""
import hashlib
import json
import os
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'nonelementary-k2-geometric-q4-manifest.json'
NVAR = 14

shard_index = int(os.environ.get('SHARD_INDEX', '0'))
shard_count = int(os.environ.get('SHARD_COUNT', '32'))
if shard_count <= 0 or not (0 <= shard_index < shard_count):
    raise SystemExit('invalid shard index/count')

manifest = json.loads(MANIFEST.read_text())
if manifest.get('schema') != 'STAGE33_07_NONELEMENTARY_K2_GEOMETRIC_Q4_MANIFEST_V1':
    raise SystemExit('manifest schema regression')
if manifest.get('arithmetic_generators_used') != []:
    raise SystemExit('manifest crossed arithmetic firewall')
if manifest.get('orbit_count') != 1496 or manifest.get('representative_section_count') != 15548416:
    raise SystemExit('manifest universe regression')


def canon(rows):
    pivots = {}
    for raw in rows:
        value = int(raw)
        for pivot in sorted(pivots, reverse=True):
            if (value >> pivot) & 1:
                value ^= pivots[pivot]
        if not value:
            continue
        pivot = value.bit_length() - 1
        for old in list(pivots):
            if (pivots[old] >> pivot) & 1:
                pivots[old] ^= value
        pivots[pivot] = value
    return tuple(pivots[p] for p in sorted(pivots, reverse=True))


def rank(rows):
    return len(canon(rows))


def complement(base, whole):
    current = list(canon(base))
    result = []
    for vector in canon(whole):
        if rank(current + [vector]) > len(current):
            current.append(vector)
            result.append(vector)
    return tuple(result)


def free_variables(reduced):
    pivots = set()
    for value in reduced:
        coefficient = int(value) & ((1 << NVAR) - 1)
        if not coefficient:
            raise SystemExit('zero affine row')
        pivots.add(coefficient.bit_length() - 1)
    return tuple(i for i in range(NVAR) if i not in pivots)


def solution_from_free(reduced, free, free_mask):
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
    return solution


def add_mod4(left, right):
    return tuple((int(a) + int(b)) % 4 for a, b in zip(left, right))


def add_selected_rows(rows, coefficient_mask):
    result = (0,) * 14
    for i, row in enumerate(rows):
        if (int(coefficient_mask) >> i) & 1:
            result = add_mod4(result, row)
    return result


def kernel_coefficients(p_basis):
    k = len(p_basis)
    return canon(
        coefficient for coefficient in range(1, 1 << k)
        if all(
            sum(((coefficient >> i) & 1) * ((int(p_basis[i]) >> coordinate) & 1)
                for i in range(k)) % 2 == 0
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


def functional_mask_even(root, h_generators):
    mask = 0
    for generator, h in enumerate(h_generators):
        value = sum(int(root[i]) * int(h[i]) for i in range(14)) % 4
        if value % 2:
            raise SystemExit('theta image lost exponent two')
        if (value // 2) & 1:
            mask |= 1 << generator
    return mask


def h_generators(p_basis, w_basis, quotient_basis, solution):
    k = len(p_basis)
    q = len(quotient_basis)
    if k != 2 or q != 7:
        raise SystemExit('k2 generator shape regression')
    order_four = []
    for generator, p in enumerate(p_basis):
        correction = 0
        for bit, vector in enumerate(quotient_basis):
            if (int(solution) >> (q * generator + bit)) & 1:
                correction ^= int(vector)
        order_four.append(tuple(
            (((int(p) >> coordinate) & 1) + 2 * ((correction >> coordinate) & 1)) % 4
            for coordinate in range(14)
        ))
    w_complement = complement(p_basis, w_basis)
    if len(w_complement) != 5:
        raise SystemExit('k2 W/P complement rank regression')
    order_two = [
        tuple(2 * ((int(w) >> coordinate) & 1) for coordinate in range(14))
        for w in w_complement
    ]
    h = tuple(order_four + order_two)
    if len(h) != 7:
        raise SystemExit('k2 H generator count regression')
    return h


def full_theta_masks(p_basis, w_basis, quotient_basis, solution):
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
        u = add_selected_rows(h[:2], coefficients)
        masks.append(functional_mask_even(root_mod4(u), h))
    return tuple(masks)

records_out = []
total_checked = 0
total_survivors = 0
for record in manifest['records']:
    orbit_index = int(record['orbit_index'])
    p_basis = tuple(map(int, record['P_basis_bits']))
    w_basis = tuple(map(int, record['W_basis_bits']))
    quotient_basis = tuple(map(int, record['quotient_basis_bits']))
    reduced = tuple(map(int, record['base_affine_rref_augmented']))
    dimension = int(record['affine_dimension'])
    target_rank = int(record['target_theta_image_rank'])
    expected_total = 1 << dimension
    free = free_variables(reduced)
    if len(free) != dimension:
        raise SystemExit('affine dimension/free-variable regression')
    checked = 0
    survivors = 0
    rank_hist = Counter()
    first_survivors = []
    for free_mask in range(shard_index, expected_total, shard_count):
        solution = solution_from_free(reduced, free, free_mask)
        theta_rank = rank(full_theta_masks(p_basis, w_basis, quotient_basis, solution))
        rank_hist[theta_rank] += 1
        checked += 1
        if theta_rank == target_rank:
            survivors += 1
            if len(first_survivors) < 4:
                first_survivors.append(int(free_mask))
    expected_checked = (expected_total + shard_count - 1 - shard_index) // shard_count
    if checked != expected_checked:
        raise SystemExit('modulo shard coverage regression')
    total_checked += checked
    total_survivors += survivors
    records_out.append({
        'orbit_index': orbit_index,
        'orbit_size': int(record['orbit_size']),
        't': int(record['t']),
        'target_theta_image_rank': target_rank,
        'affine_dimension': dimension,
        'assignments_checked': checked,
        'theta_rank_histogram': {str(k): v for k, v in sorted(rank_hist.items())},
        'representative_section_survivors': survivors,
        'first_survivor_free_masks': first_survivors,
    })

certificate = {
    'schema': 'STAGE33_07_NONELEMENTARY_K2_GEOMETRIC_Q4_SHARD_V1',
    'manifest_sha256': manifest['canonical_sha256'],
    'arithmetic_generators_used': [],
    'shard_index': shard_index,
    'shard_count': shard_count,
    'coverage_rule': 'free_mask mod shard_count == shard_index independently in each of 1496 orbit fibres',
    'records': records_out,
    'representative_sections_checked': total_checked,
    'representative_section_survivors': total_survivors,
    'all_owned_sections_checked_exactly_once': True,
    'fast_or_heuristic_traversal_used': False,
    'canonical_augmentation_used_inside_fibre': False,
    'full_Q4_condition_certified_globally': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
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
out = HERE / f'nonelementary-k2-geometric-q4-shard-{shard_index}.json'
out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + '\n')
print(json.dumps({
    'success': True,
    'shard_index': shard_index,
    'checked': total_checked,
    'survivors': total_survivors,
    'certificate_sha256': certificate['canonical_sha256'],
}, indent=2, sort_keys=True))
