#!/usr/bin/env python3
"""Exact symmetry reduction of the surviving k=3 Q8-admissible skeletons.

The preceding certificate counts 24,838,668,288 structural subgroups of type

    (Z/4)^3 + (Z/2)^3.

For k=3 the lift-section fibre has size 2^22 when t=1 and 2^21 when t=2.
This leaf first materializes the exact 7,236 underlying (P,W) skeletons, then quotients them
by the integral coordinate symmetry which preserves all source species:

  * arbitrary permutation of the three Kb pieces;
  * independent exchange of the two equal-modulus coordinates in each Kb;
  * arbitrary permutation of the three Ka pieces;
  * Kc fixed.

The group has order 6*8*6=288.  It preserves the ambient diagonal quadratic
module, the seven coordinate-sign actions as a set, and the retained Kb/Kc/Ka
cc/ct action-choice species.  No lift section f is quotiented or rejected here.
The output is a compact orbit certificate, not an actual-glue identification.
"""
import hashlib
import itertools
import json
import runpy
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
STRUCTURAL_LOCK = '235298bd303c0f21d946f6ca537ca30d42e049a6739c1ef106ecef760499c9e9'
Q8_LOCK = '4a5c84ad765f93442f08991ffdcea0bab6f1ae5a3ab6561157201bba262f75ee'

base = json.loads((HERE / 'nonelementary-sign-target-q2-structural-reduction.json').read_text())
q8 = json.loads((HERE / 'nonelementary-target-q8-exponent-reduction.json').read_text())
if base.get('canonical_sha256') != STRUCTURAL_LOCK:
    raise SystemExit('E7 structural source lock moved')
if q8.get('canonical_sha256') != Q8_LOCK:
    raise SystemExit('target-Q8 source lock moved')

ns = runpy.run_path(str(HERE / 'certify_nonelementary_sign_q2_structural_reduction.py'))
subspaces = ns['subspaces']
span = ns['span']
rank = ns['rank']
canon = ns['canon']
red_to_full = ns['red_to_full']
eqrc = ns['eq_rank_and_consistency']


def contains(basis, vector):
    return rank(list(basis) + [vector]) == len(basis)


def complement(base_basis, whole_basis):
    current = list(canon(base_basis))
    result = []
    for vector in canon(whole_basis):
        if rank(current + [vector]) > len(current):
            current.append(vector)
            result.append(vector)
    return tuple(result)


def perp(basis, dimension):
    return canon(
        vector for vector in range(1, 1 << dimension)
        if all((vector & row).bit_count() % 2 == 0 for row in basis)
    )


def rref_subspaces(dimension, subdimension):
    if subdimension == 0:
        yield ()
        return
    for pivots in itertools.combinations(range(dimension), subdimension):
        pivot_set = set(pivots)
        free = [j for j in range(dimension) if j not in pivot_set]
        slots = [(row, j) for j in free for row, pivot in enumerate(pivots) if pivot < j]
        for mask in range(1 << len(slots)):
            rows = [1 << pivot for pivot in pivots]
            for bit, (row, j) in enumerate(slots):
                if (mask >> bit) & 1:
                    rows[row] |= 1 << j
            yield canon(rows)


coisotropic_y = []
for u in range(2, 5):
    for basis in rref_subspaces(4, u):
        if all(contains(basis, vector) for vector in perp(basis, 4)):
            coisotropic_y.append(basis)
if Counter(map(len, coisotropic_y)) != Counter({2: 3, 3: 7, 4: 1}):
    raise SystemExit('coisotropic Y census regression')


def ambient_subspaces_containing(base_basis, ambient_basis, target_dimension):
    base_basis = canon(base_basis)
    quotient_basis = complement(base_basis, ambient_basis)
    need = target_dimension - len(base_basis)
    for abstract in rref_subspaces(len(quotient_basis), need):
        lifted = []
        for row in abstract:
            vector = 0
            for j, basis_vector in enumerate(quotient_basis):
                if (row >> j) & 1:
                    vector ^= basis_vector
            lifted.append(vector)
        result = canon(base_basis + tuple(lifted))
        if len(result) != target_dimension:
            raise SystemExit('ambient subspace lift rank regression')
        yield result


def graph_skeletons(dx, r_basis, u_basis):
    r_complement = complement(dx, r_basis)
    y_complement = complement(u_basis, canon(1 << j for j in range(4)))
    slots = [(i, j) for i in range(len(r_complement)) for j in range(len(y_complement))]
    for mask in range(1 << len(slots)):
        graph_rows = list(dx) + [row << 10 for row in u_basis]
        for i, xrow in enumerate(r_complement):
            yrow = 0
            for bit, (ii, j) in enumerate(slots):
                if ii == i and (mask >> bit) & 1:
                    yrow ^= y_complement[j]
            graph_rows.append(xrow | (yrow << 10))
        result = canon(graph_rows)
        if len(result) != 6:
            raise SystemExit('W graph rank regression')
        yield result


skeletons = set()
profile = Counter()
for reduced_p in sorted(subspaces[3]):
    support = 0
    for vector in span(reduced_p):
        support |= vector
    if support.bit_count() > 6:
        continue
    t = rank([vector & 0b111 for vector in reduced_p])
    equation_rank, consistent = eqrc(reduced_p)
    if t > 2 or not consistent or equation_rank not in (2, 3):
        continue
    p = canon(red_to_full(vector) for vector in reduced_p)
    px = canon(vector & ((1 << 10) - 1) for vector in p)
    x0 = perp(px, 10)
    dx = canon(
        (1 << (2 * j)) | (1 << (2 * j + 1))
        for j in range(3) if (support >> j) & 1
    )
    dy = canon(1 << j for j in range(4) if (support >> (3 + j)) & 1)
    for u_basis in coisotropic_y:
        if any(not contains(u_basis, vector) for vector in dy):
            continue
        r_dimension = 6 - len(u_basis)
        if not (len(dx) <= r_dimension <= len(x0)):
            continue
        for r_basis in ambient_subspaces_containing(dx, x0, r_dimension):
            for w in graph_skeletons(dx, r_basis, u_basis):
                if any(not contains(w, vector) for vector in p):
                    raise SystemExit('P not contained in W')
                key = (p, w)
                if key in skeletons:
                    raise SystemExit('duplicate (P,W) skeleton')
                skeletons.add(key)
                profile[(t, len(u_basis), support.bit_count(), equation_rank)] += 1

if len(skeletons) != 7236:
    raise SystemExit(f'k3 skeleton census regression: {len(skeletons)}')
structural_h_reconstructed = sum(
    count * (1 << (24 - equation_rank))
    for (_, _, _, equation_rank), count in profile.items()
)
if structural_h_reconstructed != 24838668288:
    raise SystemExit('k3 lift-fibre product regression')


def coordinate_permutations():
    for kb_perm in itertools.permutations(range(3)):
        for kb_swap_mask in range(8):
            for ka_perm in itertools.permutations(range(3)):
                permutation = list(range(14))
                for old_piece in range(3):
                    new_piece = kb_perm[old_piece]
                    swap = (kb_swap_mask >> old_piece) & 1
                    permutation[2 * old_piece] = 2 * new_piece + swap
                    permutation[2 * old_piece + 1] = 2 * new_piece + (1 - swap)
                permutation[6] = 6
                permutation[10] = 10
                for old_piece in range(3):
                    new_piece = ka_perm[old_piece]
                    permutation[7 + old_piece] = 7 + new_piece
                    permutation[11 + old_piece] = 11 + new_piece
                yield tuple(permutation)


symmetry = tuple(coordinate_permutations())
if len(symmetry) != 288 or len(set(symmetry)) != 288:
    raise SystemExit('integral coordinate symmetry order regression')


def transport_vector(vector, permutation):
    result = 0
    for old, new in enumerate(permutation):
        if (vector >> old) & 1:
            result |= 1 << new
    return result


def transport_skeleton(skeleton, permutation):
    p, w = skeleton
    return (
        canon(transport_vector(vector, permutation) for vector in p),
        canon(transport_vector(vector, permutation) for vector in w),
    )


unseen = set(skeletons)
orbit_sizes = []
orbit_representatives = []
representative_digest = hashlib.sha256()
while unseen:
    seed = min(unseen)
    orbit = {transport_skeleton(seed, permutation) for permutation in symmetry}
    if not orbit <= skeletons:
        raise SystemExit('skeleton set is not stable under source-species symmetry')
    unseen.difference_update(orbit)
    representative = min(orbit)
    orbit_sizes.append(len(orbit))
    orbit_representatives.append({
        'P_basis_bits': list(representative[0]),
        'W_basis_bits': list(representative[1]),
        'orbit_size': len(orbit),
    })
    representative_digest.update(json.dumps(representative, separators=(',', ':')).encode())

orbit_sizes.sort()
orbit_histogram = Counter(orbit_sizes)
certificate = {
    'schema': 'STAGE33_07_NONELEMENTARY_K3_Q8_SKELETON_ORBITS_V1',
    'source_structural_sha256': STRUCTURAL_LOCK,
    'source_target_Q8_sha256': Q8_LOCK,
    'abstract_H_type': '(Z/4)^3 direct_sum (Z/2)^3',
    'exact_P_W_skeleton_count': len(skeletons),
    'lift_section_affine_fibre_size_by_t': {'1': 1 << 22, '2': 1 << 21},
    'structural_H_count_reconstructed': structural_h_reconstructed,
    'symmetry_description': 'S3(Kb pieces) semidirect (S2)^3(Kb swaps) times S3(Ka pieces), Kc fixed',
    'symmetry_order': len(symmetry),
    'symmetry_preserves_ambient_q_and_source_species': True,
    'exact_orbit_count': len(orbit_sizes),
    'orbit_size_histogram': {str(size): count for size, count in sorted(orbit_histogram.items())},
    'orbit_size_sum': sum(orbit_sizes),
    'representative_sequence_sha256': representative_digest.hexdigest(),
    'orbit_representatives': orbit_representatives,
    'profile_by_t_u_support': {
        f't={t},u={u},support={support},eqrank={equation_rank}': count
        for (t, u, support, equation_rank), count in sorted(profile.items())
    },
    'lift_sections_quotiented_or_rejected': False,
    'endpoint_finite_q_certified': False,
    'endpoint_full_action_conjugacy_certified': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'next_exact_leaf': 'L33-07-SOLVE-K3-Q4-AND-FINITE-Q-LIFT-SECTION-FIBRES-OVER-EXACT-SKELETON-ORBITS',
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
(HERE / 'nonelementary-k3-q8-skeleton-orbits.json').write_text(
    json.dumps(certificate, indent=2, sort_keys=True) + '\n'
)
print(json.dumps({
    'success': True,
    'skeletons': certificate['exact_P_W_skeleton_count'],
    'orbits': certificate['exact_orbit_count'],
    'orbit_histogram': certificate['orbit_size_histogram'],
    'structural_H_reconstructed': certificate['structural_H_count_reconstructed'],
    'certificate_sha256': certificate['canonical_sha256'],
    'next': certificate['next_exact_leaf'],
}, indent=2, sort_keys=True))
