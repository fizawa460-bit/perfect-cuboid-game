#!/usr/bin/env python3
"""Exact pure-geometric compression of the non-elementary k=3 branch.

Starting from the complete Q8-admissible type

    H ~= (Z/4)^3 + (Z/2)^3,

this leaf materializes every exact (P,W) skeleton without using cc/ct.  It then
imposes two necessary endpoint finite-q support conditions directly:

* Q[2] support.  Endpoint Q[2] has only q-numerators 0,8 mod 16.  Therefore
  every w in W must have even X-weight.
* 2Q support.  For every v in V=W^perp the doubled-class numerator is
      4 wt_X(v) + 2 wt_Y(v) mod 16,
  so endpoint support {0,8} forces
      2 wt_X(v) + wt_Y(v) == 0 mod 4.

The endpoint supports are independently recomputed from the locked compact
Picard discriminant form.  The surviving skeletons are then quotiented only by
the order-288 integral coordinate symmetry preserving the seven source pieces.
No arithmetic cc/ct action is used anywhere in this leaf.
"""

import hashlib
import itertools
import json
import runpy
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
Q8_LOCK = '4a5c84ad765f93442f08991ffdcea0bab6f1ae5a3ab6561157201bba262f75ee'
TARGET_Q_LOCK = '4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'
X_MASK = (1 << 10) - 1

# Rebuild the exact structural/Q8 predecessor.  This route is independent of
# every retained arithmetic action-choice file.
q8_ns = runpy.run_path(str(HERE / 'certify_nonelementary_target_q8_exponent_reduction.py'))
q8 = json.loads((HERE / 'nonelementary-target-q8-exponent-reduction.json').read_text())
if q8.get('canonical_sha256') != Q8_LOCK:
    raise SystemExit('target-Q8 predecessor moved')

base_ns = runpy.run_path(str(HERE / 'certify_nonelementary_sign_q2_structural_reduction.py'))
subspaces = base_ns['subspaces']
span = base_ns['span']
rank = base_ns['rank']
canon = base_ns['canon']
red_to_full = base_ns['red_to_full']
eqrc = base_ns['eq_rank_and_consistency']

# Recompute endpoint Q[2] and 2Q supports from the compact finite quadratic form.
target = json.loads((HERE / 'picard-discriminant-compact.json').read_text())
if target.get('canonical_sha256') != TARGET_Q_LOCK:
    raise SystemExit('endpoint finite-q source moved')
mods = tuple(map(int, target['discriminant_moduli']))
raw_b = target['discriminant_bilinear_numerator_over_8_reduced']
b8 = tuple(
    tuple(-int(x) % (16 if i == j else 8) for j, x in enumerate(row))
    for i, row in enumerate(raw_b)
)

def target_qnum(vector):
    return sum(
        int(vector[i]) * b8[i][j] * int(vector[j])
        for i in range(14) for j in range(14)
    ) % 16

q2_profile = Counter(
    target_qnum(vector)
    for vector in itertools.product(*[(0, modulus // 2) for modulus in mods])
)
if q2_profile != Counter({0: 8192, 8: 8192}):
    raise SystemExit(f'endpoint Q2 profile regression: {q2_profile}')

double_coordinate_values = [tuple(sorted({(2 * x) % modulus for x in range(modulus)})) for modulus in mods]
twoq_profile = Counter(
    target_qnum(vector)
    for vector in itertools.product(*double_coordinate_values)
)
if set(twoq_profile) != {0, 8} or sum(twoq_profile.values()) != 16384:
    raise SystemExit(f'endpoint 2Q support regression: {twoq_profile}')


def contains(basis, vector):
    return rank(list(basis) + [int(vector)]) == len(basis)


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


# Materialize all 7,236 exact Q8-admissible k=3 skeletons.
skeletons = set()
p_metadata = {}
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
    p_metadata[p] = (t, equation_rank)
    px = canon(vector & X_MASK for vector in p)
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

if len(skeletons) != 7236:
    raise SystemExit(f'k3 skeleton census regression: {len(skeletons)}')

def lift_fibre_size(p):
    _, equation_rank = p_metadata[p]
    return 1 << (24 - equation_rank)

before_weighted = sum(lift_fibre_size(p) for p, _ in skeletons)
if before_weighted != 24838668288:
    raise SystemExit('Q8 structural-H reconstruction regression')


def q2_support_ok(w):
    # Linear parity makes basis checking sufficient, but enumerate W to keep
    # the certificate statement exactly aligned with the subgroup condition.
    return all((vector & X_MASK).bit_count() % 2 == 0 for vector in span(w))


def twoq_support_ok(w):
    v_basis = perp(w, 14)
    for vector in span(v_basis):
        wx = (vector & X_MASK).bit_count()
        wy = ((vector >> 10) & 0xF).bit_count()
        if (2 * wx + wy) % 4:
            return False
    return True

q2_survivors = {(p, w) for p, w in skeletons if q2_support_ok(w)}
twoq_survivors = {(p, w) for p, w in q2_survivors if twoq_support_ok(w)}
q2_weighted = sum(lift_fibre_size(p) for p, _ in q2_survivors)
twoq_weighted = sum(lift_fibre_size(p) for p, _ in twoq_survivors)
if (len(q2_survivors), q2_weighted) != (3780, 12759072768):
    raise SystemExit('k3 exact Q2-support reduction regression')
if (len(twoq_survivors), twoq_weighted) != (36, 113246208):
    raise SystemExit('k3 exact 2Q-support reduction regression')


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
    raise SystemExit('integral source symmetry order regression')


def transport_vector(vector, permutation):
    result = 0
    for old, new in enumerate(permutation):
        if (int(vector) >> old) & 1:
            result |= 1 << new
    return result


def transport_skeleton(skeleton, permutation):
    p, w = skeleton
    return (
        canon(transport_vector(vector, permutation) for vector in p),
        canon(transport_vector(vector, permutation) for vector in w),
    )

unseen = set(twoq_survivors)
orbits = []
while unseen:
    seed = min(unseen)
    orbit = {transport_skeleton(seed, permutation) for permutation in symmetry}
    if not orbit <= twoq_survivors:
        raise SystemExit('Q2/2Q support survivor set not symmetry-stable')
    unseen.difference_update(orbit)
    representative = min(orbit)
    t, equation_rank = p_metadata[representative[0]]
    orbits.append({
        'P_basis_bits': list(representative[0]),
        'W_basis_bits': list(representative[1]),
        'orbit_size': len(orbit),
        't': t,
        'section_equation_rank': equation_rank,
        'lift_section_fibre_size': 1 << (24 - equation_rank),
    })

orbits.sort(key=lambda record: (record['P_basis_bits'], record['W_basis_bits']))
if len(orbits) != 4 or Counter(record['orbit_size'] for record in orbits) != Counter({9: 4}):
    raise SystemExit(f'k3 support orbit census regression: {orbits}')
if Counter((record['t'], record['section_equation_rank']) for record in orbits) != Counter({(1, 2): 2, (2, 3): 2}):
    raise SystemExit('k3 support orbit fibre profile regression')

rep_digest = hashlib.sha256(
    json.dumps(orbits, sort_keys=True, separators=(',', ':')).encode()
).hexdigest()
certificate = {
    'schema': 'STAGE33_07_NONELEMENTARY_K3_GEOMETRIC_Q2_2Q_SUPPORT_ORBITS_V1',
    'source_target_Q8_sha256': Q8_LOCK,
    'source_endpoint_finite_q_sha256': TARGET_Q_LOCK,
    'arithmetic_generators_used': [],
    'firewall': 'NO_ARITHMETIC_CC_CT_USED_IN_THIS_CERTIFICATE',
    'endpoint_Q2_profile_numerator_over_8': {str(k): v for k, v in sorted(q2_profile.items())},
    'endpoint_2Q_profile_numerator_over_8': {str(k): v for k, v in sorted(twoq_profile.items())},
    'Q8_skeleton_count_before': len(skeletons),
    'Q8_structural_H_before': before_weighted,
    'Q2_support_surviving_skeleton_count': len(q2_survivors),
    'Q2_support_surviving_structural_H': q2_weighted,
    'Q2_2Q_support_surviving_skeleton_count': len(twoq_survivors),
    'Q2_2Q_support_surviving_structural_H': twoq_weighted,
    'source_integral_coordinate_symmetry_order': 288,
    'exact_support_survivor_orbit_count': len(orbits),
    'orbit_size_histogram': {'9': 4},
    'orbit_representatives_sha256': rep_digest,
    'orbit_representatives': orbits,
    'representative_lift_sections_for_next_exact_leaf': sum(record['lift_section_fibre_size'] for record in orbits),
    'full_target_Q4_condition_certified': False,
    'endpoint_finite_q_certified': False,
    'endpoint_full_action_certified': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'next_exact_leaf': 'L33-07-EXHAUST-K3-FOUR-GEOMETRIC-SUPPORT-ORBITS-BY-FULL-Q4-THETA-RANK',
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
(HERE / 'nonelementary-k3-geometric-q2-2q-support-orbits.json').write_text(
    json.dumps(certificate, indent=2, sort_keys=True) + '\n'
)
print(json.dumps({
    'success': True,
    'skeletons_before': len(skeletons),
    'q2_skeletons': len(q2_survivors),
    'q2_2q_skeletons': len(twoq_survivors),
    'weighted_H_after': twoq_weighted,
    'orbits': len(orbits),
    'orbit_sizes': [record['orbit_size'] for record in orbits],
    'representative_lift_sections_next': certificate['representative_lift_sections_for_next_exact_leaf'],
    'certificate_sha256': certificate['canonical_sha256'],
}, indent=2, sort_keys=True))
