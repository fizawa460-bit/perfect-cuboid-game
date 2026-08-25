#!/usr/bin/env python3
"""Exact integral cc/ct filter on every surviving k=3 affine fibre.

The predecessor reconstructs the complete 2,628-skeleton universe and counts
all 7,927,234,560 lift sections before quotienting.  This leaf does not use a
fast or pruned representative traversal.  For each of the 189 exact skeleton
orbits it:

* expands every retained scaled integral cc choice (1,024 global choices) and
  ct choice (128 global choices) on the normalized (Z/4)^14 module;
* derives the exact affine F2 stability equations, including mod-four carry;
* proves all choices of a given involution have the same stability locus;
* proves ct adds no equation and cc leaves an affine fibre of dimension
  16, 18, 19, or 21;
* checks the retained action sets are closed under the full order-288 integral
  coordinate symmetry; and
* applies Burnside to the filtered affine fibres using exact F2 elimination.

The complete predecessor count, every skeleton orbit, every raw action choice,
and every stabilizer element are consumed.  Hence this compression cannot lose
objects through canonical-augmentation pruning.  It remains only an integral
action-stability filter: full Q[4], endpoint finite-q/action conjugacy, and the
actual index-512 glue are not certified.
"""
import hashlib
import itertools
import json
import runpy
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
LIFT_LOCK = '19c37c310ab6a5494817be64ef860e135c8314273ff3f0e1f61dad0db7165fdb'
ACTION_LOCK = 'a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20'

ns = runpy.run_path(str(HERE / 'certify_nonelementary_k3_lift_section_orbits.py'))
predecessor = json.loads((HERE / 'nonelementary-k3-lift-section-orbits.json').read_text())
source = json.loads((HERE / 'nonelementary-k3-q8-skeleton-orbits.json').read_text())
actions = json.loads((HERE / 'coordinate-k3-scaled-action-choices-retained.json').read_text())
if predecessor.get('canonical_sha256') != LIFT_LOCK:
    raise SystemExit('k3 affine-lift predecessor lock moved')
if actions.get('canonical_sha256') != ACTION_LOCK:
    raise SystemExit('scaled action-choice lock moved')

canon = ns['canon']
complement = ns['complement']
span_coordinate_map = ns['span_coordinate_map']
section_equations = ns['section_equations']
affine_rank = ns['affine_rank']
affine_action = ns['affine_action']
verify_affine_inverse = ns['verify_affine_inverse']
verify_affine_solution_preservation = ns['verify_affine_solution_preservation']
symmetry = ns['symmetry']
transport_skeleton = ns['transport_skeleton']

NVAR = 24
MASK = (1 << NVAR) - 1
PIECES = ((0, 1), (2, 3), (4, 5), (6, 10), (7, 11), (8, 12), (9, 13))
NAMES = ('kb', 'kb', 'kb', 'kc', 'ka', 'ka', 'ka')
SCALES = (2,) * 10 + (4,) * 4


def affine_rref(rows):
    """Canonical augmented RREF, or None for an inconsistent system."""
    pivots = {}
    for mask, rhs in rows:
        value = int(mask) | ((int(rhs) & 1) << NVAR)
        coefficient = value & MASK
        while coefficient:
            pivot = coefficient.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
                coefficient = value & MASK
            else:
                for old_pivot in list(pivots):
                    if (pivots[old_pivot] >> pivot) & 1:
                        pivots[old_pivot] ^= value
                pivots[pivot] = value
                break
        if not coefficient and ((value >> NVAR) & 1):
            return None
    return tuple(pivots[pivot] for pivot in sorted(pivots, reverse=True))


def decode_rref(reduced):
    return [(value & MASK, (value >> NVAR) & 1) for value in reduced]


def canonical_solution(reduced):
    """Solve canonical RREF with every free variable set to zero."""
    solution = 0
    for value in reversed(reduced):
        coefficient = value & MASK
        pivot = coefficient.bit_length() - 1
        rhs = ((value >> NVAR) & 1) ^ ((coefficient & solution).bit_count() & 1)
        if rhs:
            solution |= 1 << pivot
    for mask, rhs in decode_rref(reduced):
        if ((mask & solution).bit_count() & 1) != rhs:
            raise SystemExit('canonical affine solution regression')
    return solution


def normalized_global_action(choice, kind):
    """Transport a retained A0 action to row action on normalized (Z/4)^14."""
    matrix = [[int(i == j) for j in range(14)] for i in range(14)]
    for (a, b), name, local_index in zip(PIECES, NAMES, choice):
        local = actions['pieces'][name][kind + '_actions'][local_index]
        for ii, old in enumerate((a, b)):
            for jj, new in enumerate((a, b)):
                numerator = SCALES[old] * int(local[ii][jj])
                if numerator % SCALES[new]:
                    raise SystemExit('scaled action does not descend to normalized module')
                matrix[old][new] = (numerator // SCALES[new]) % 4
    return tuple(tuple(row) for row in matrix)


def all_global_actions(kind):
    ranges = [range(len(actions['pieces'][name][kind + '_actions'])) for name in NAMES]
    matrices = tuple(normalized_global_action(choice, kind) for choice in itertools.product(*ranges))
    return matrices


def conjugate_by_permutation(matrix, permutation):
    result = [[0] * 14 for _ in range(14)]
    for old_i, new_i in enumerate(permutation):
        for old_j, new_j in enumerate(permutation):
            result[new_i][new_j] = matrix[old_i][old_j]
    return tuple(tuple(row) for row in result)


def action_mod4(vector, matrix):
    return tuple(
        sum(((int(vector) >> i) & 1) * matrix[i][j] for i in range(14)) % 4
        for j in range(14)
    )


def action_mod4_coordinates(vector, matrix):
    return tuple(
        sum(int(vector[i]) * matrix[i][j] for i in range(14)) % 4
        for j in range(14)
    )


def add_mod4(left, right):
    return tuple((int(a) + int(b)) % 4 for a, b in zip(left, right))


def bits_mod2(coordinates):
    return sum((int(value) & 1) << j for j, value in enumerate(coordinates))


def stability_equations(p_basis, quotient_basis, quotient_coordinates, matrix):
    """Affine equations for matrix(H)=H on lift-section coordinates."""
    p_coordinates = span_coordinate_map(p_basis)
    transported_quotient = [bits_mod2(action_mod4(vector, matrix)) for vector in quotient_basis]
    rows = []
    for input_generator, p in enumerate(p_basis):
        transported_p4 = action_mod4(p, matrix)
        transported_p2 = bits_mod2(transported_p4)
        combination = p_coordinates.get(transported_p2)
        if combination is None:
            return None

        selected_sum = [
            sum((p_basis[j] >> coordinate) & 1
                for j in range(3) if (combination >> j) & 1)
            for coordinate in range(14)
        ]
        carry = 0
        for coordinate in range(14):
            difference = (transported_p4[coordinate] - selected_sum[coordinate]) % 4
            if difference & 1:
                raise SystemExit('integral action carry parity regression')
            if difference == 2:
                carry |= 1 << coordinate
        carry_q = quotient_coordinates[carry] >> 6

        for output_bit in range(8):
            mask = 0
            for input_bit, transported in enumerate(transported_quotient):
                if (quotient_coordinates[transported] >> (6 + output_bit)) & 1:
                    mask ^= 1 << (8 * input_generator + input_bit)
            for j in range(3):
                if (combination >> j) & 1:
                    mask ^= 1 << (8 * j + output_bit)
            rows.append((mask, (carry_q >> output_bit) & 1))
    return rows


cc_matrices = all_global_actions('cc')
ct_matrices = all_global_actions('ct')
if len(cc_matrices) != 1024 or len(ct_matrices) != 128:
    raise SystemExit('raw global action-choice count regression')

# Exact closure means representative-level filtering is invariant under the
# entire proved integral symmetry; no orbit can disappear between reps.
cc_set = set(cc_matrices)
ct_set = set(ct_matrices)
cc_multiplicities = Counter(cc_matrices)
ct_multiplicities = Counter(ct_matrices)
if (len(cc_set) != 8 or set(cc_multiplicities.values()) != {128}
        or len(ct_set) != 1 or set(ct_multiplicities.values()) != {128}):
    raise SystemExit('normalized action-choice multiplicity regression')
for permutation in symmetry:
    if {conjugate_by_permutation(matrix, permutation) for matrix in cc_matrices} != cc_set:
        raise SystemExit('cc action set is not symmetry-closed')
    if {conjugate_by_permutation(matrix, permutation) for matrix in ct_matrices} != ct_set:
        raise SystemExit('ct action set is not symmetry-closed')

cc_dimension_histogram = Counter()
cc_dimension_weighted_skeleton_histogram = Counter()
stabilizer_histogram = Counter()
fixed_log_histogram = Counter()
records = []
predecessor_reconstructed = 0
after_integral_cc_ct = 0
full_symmetry_orbits = 0

for index, representative in enumerate(source['orbit_representatives']):
    p_basis = tuple(int(x) for x in representative['P_basis_bits'])
    w_basis = tuple(int(x) for x in representative['W_basis_bits'])
    skeleton = (p_basis, w_basis)
    orbit_size = int(representative['orbit_size'])
    quotient_basis = complement(w_basis, canon(1 << j for j in range(14)))
    quotient_coordinates = span_coordinate_map(w_basis + quotient_basis)
    base_equations = section_equations(p_basis, quotient_basis)
    base_rref = affine_rref(base_equations)
    if base_rref is None:
        raise SystemExit('predecessor affine fibre became inconsistent')
    base_dimension = NVAR - len(base_rref)
    predecessor_reconstructed += orbit_size * (1 << base_dimension)

    cc_systems = set()
    for matrix in cc_matrices:
        extra = stability_equations(p_basis, quotient_basis, quotient_coordinates, matrix)
        if extra is None:
            raise SystemExit('cc mod-two action does not stabilize P')
        reduced = affine_rref(base_equations + extra)
        if reduced is None:
            raise SystemExit('a retained cc choice has no stable lift section')
        cc_systems.add(reduced)
    if len(cc_systems) != 1:
        raise SystemExit('retained cc choices have different stability loci')
    cc_rref = next(iter(cc_systems))
    cc_equations = decode_rref(cc_rref)
    cc_dimension = NVAR - len(cc_rref)

    for matrix in ct_matrices:
        extra = stability_equations(p_basis, quotient_basis, quotient_coordinates, matrix)
        if extra is None:
            raise SystemExit('ct mod-two action does not stabilize P')
        if affine_rref(base_equations + extra) != base_rref:
            raise SystemExit('retained ct choice unexpectedly changes the affine fibre')

    # Independent direct witness firewall: reconstruct one actual order-512
    # subgroup in (Z/4)^14, enumerate it without affine equations, and verify
    # total isotropy plus stability under every raw retained cc/ct choice.
    solution = canonical_solution(cc_rref)
    order_four_rows = []
    for generator, p in enumerate(p_basis):
        correction = 0
        for bit, vector in enumerate(quotient_basis):
            if (solution >> (8 * generator + bit)) & 1:
                correction ^= vector
        order_four_rows.append(tuple(
            (((p >> coordinate) & 1) + 2 * ((correction >> coordinate) & 1)) % 4
            for coordinate in range(14)
        ))
    w_complement = complement(p_basis, w_basis)
    if len(w_complement) != 3:
        raise SystemExit('W/P complement rank regression')
    order_two_rows = [tuple(2 * ((w >> coordinate) & 1) for coordinate in range(14))
                      for w in w_complement]
    subgroup = set()
    for coefficients in itertools.product(range(4), range(4), range(4),
                                           range(2), range(2), range(2)):
        value = (0,) * 14
        for coefficient, row in zip(coefficients, order_four_rows + order_two_rows):
            for _ in range(coefficient):
                value = add_mod4(value, row)
        subgroup.add(value)
    if len(subgroup) != 512:
        raise SystemExit('direct witness subgroup order regression')
    if any((8 * sum(x * x for x in value[:10])
            + 16 * sum(x * x for x in value[10:])) % 32 for value in subgroup):
        raise SystemExit('direct witness subgroup isotropy regression')
    generators = order_four_rows + order_two_rows
    for kind, matrices in (('cc', cc_matrices), ('ct', ct_matrices)):
        for matrix in matrices:
            if any(action_mod4_coordinates(row, matrix) not in subgroup for row in generators):
                raise SystemExit(f'direct witness {kind} stability regression')

    stabilizer = [
        permutation for permutation in symmetry
        if transport_skeleton(skeleton, permutation) == skeleton
    ]
    if len(stabilizer) * orbit_size != len(symmetry):
        raise SystemExit('filtered orbit-stabilizer regression')
    stabilizer_histogram[len(stabilizer)] += 1

    fixed_counts = []
    local_fixed_logs = Counter()
    identity_fixed_count = None
    for permutation in stabilizer:
        linear_rows, constant_mask = affine_action(
            p_basis, w_basis, quotient_basis, quotient_coordinates, permutation
        )
        verify_affine_inverse(
            p_basis, w_basis, quotient_basis, quotient_coordinates,
            permutation, linear_rows, constant_mask,
        )
        verify_affine_solution_preservation(cc_equations, linear_rows, constant_mask)
        fixed_equations = list(cc_equations) + [
            (linear_rows[output_bit] ^ (1 << output_bit),
             (constant_mask >> output_bit) & 1)
            for output_bit in range(NVAR)
        ]
        fixed_rank, fixed_consistent = affine_rank(fixed_equations)
        fixed_count = (1 << (NVAR - fixed_rank)) if fixed_consistent else 0
        fixed_counts.append(fixed_count)
        if permutation == tuple(range(14)):
            identity_fixed_count = fixed_count
        local_fixed_logs[-1 if fixed_count == 0 else fixed_count.bit_length() - 1] += 1

    # The identity fixes the entire filtered affine fibre.  This guards the
    # exact-universe reconstruction independently of Burnside divisibility.
    expected_solution_count = 1 << cc_dimension
    if identity_fixed_count != expected_solution_count or max(fixed_counts) != expected_solution_count:
        raise SystemExit('identity/full-fibre fixed-count firewall failed')
    burnside_sum = sum(fixed_counts)
    if burnside_sum % len(stabilizer):
        raise SystemExit('filtered Burnside divisibility regression')
    fibre_orbits = burnside_sum // len(stabilizer)

    after_integral_cc_ct += orbit_size * expected_solution_count
    full_symmetry_orbits += fibre_orbits
    cc_dimension_histogram[cc_dimension] += 1
    cc_dimension_weighted_skeleton_histogram[cc_dimension] += orbit_size
    fixed_log_histogram.update(local_fixed_logs)
    records.append({
        'skeleton_orbit_index': index,
        'skeleton_orbit_size': orbit_size,
        'stabilizer_order': len(stabilizer),
        'predecessor_lift_dimension': base_dimension,
        'integral_cc_ct_lift_dimension': cc_dimension,
        'integral_cc_ct_lift_count': expected_solution_count,
        'exact_filtered_fibre_orbit_count': fibre_orbits,
        'fixed_count_log2_histogram_minus1_is_zero': {
            str(log): count for log, count in sorted(local_fixed_logs.items())
        },
    })

if predecessor_reconstructed != 7927234560:
    raise SystemExit('complete predecessor reconstruction firewall failed')
if cc_dimension_histogram != Counter({18: 111, 16: 66, 21: 6, 19: 6}):
    raise SystemExit(f'cc affine-dimension profile regression: {cc_dimension_histogram}')
if after_integral_cc_ct != 572522496:
    raise SystemExit('integral cc/ct structural-H count regression')
if full_symmetry_orbits != 17146944:
    raise SystemExit('integral cc/ct full-symmetry orbit-count regression')
if len(records) != 189 or sum(cc_dimension_weighted_skeleton_histogram.values()) != 2628:
    raise SystemExit('complete skeleton-orbit consumption firewall failed')

certificate = {
    'schema': 'STAGE33_07_NONELEMENTARY_K3_INTEGRAL_CC_CT_ORBITS_V1',
    'source_affine_lift_orbits_sha256': LIFT_LOCK,
    'source_scaled_action_choices_sha256': ACTION_LOCK,
    'compression_kind': 'complete affine F2 elimination plus exact Burnside; no pruned traversal',
    'predecessor_exact_skeleton_count': 2628,
    'predecessor_exact_skeleton_orbit_count': 189,
    'predecessor_structural_H_count': 7927234560,
    'predecessor_structural_H_count_reconstructed': predecessor_reconstructed,
    'integral_symmetry_order': len(symmetry),
    'retained_action_sets_closed_under_full_symmetry': True,
    'raw_global_cc_action_choice_count': len(cc_matrices),
    'raw_global_ct_action_choice_count': len(ct_matrices),
    'distinct_normalized_global_cc_action_count': len(cc_set),
    'distinct_normalized_global_ct_action_count': len(ct_set),
    'raw_multiplicity_per_normalized_cc_action': 128,
    'raw_multiplicity_per_normalized_ct_action': 128,
    'all_cc_choices_checked_on_every_skeleton_orbit': True,
    'all_ct_choices_checked_on_every_skeleton_orbit': True,
    'cc_stability_locus_count_per_skeleton_orbit': 1,
    'ct_stability_locus_equals_predecessor_fibre_for_every_orbit': True,
    'integral_cc_ct_lift_dimension_histogram_over_skeleton_orbits': {
        str(dimension): count for dimension, count in sorted(cc_dimension_histogram.items())
    },
    'integral_cc_ct_lift_dimension_histogram_over_all_skeletons': {
        str(dimension): count
        for dimension, count in sorted(cc_dimension_weighted_skeleton_histogram.items())
    },
    'structural_H_count_after_integral_cc_ct': after_integral_cc_ct,
    'structural_H_rejected_by_integral_cc': predecessor_reconstructed - after_integral_cc_ct,
    'exact_full_symmetry_orbit_count_after_integral_cc_ct': full_symmetry_orbits,
    'stabilizer_order_histogram': {
        str(order): count for order, count in sorted(stabilizer_histogram.items())
    },
    'fixed_count_log2_histogram_minus1_is_zero': {
        str(log): count for log, count in sorted(fixed_log_histogram.items())
    },
    'identity_full_fibre_firewall_checked_for_every_orbit': True,
    'direct_order512_isotropic_action_stable_witness_checked_for_every_skeleton_orbit': True,
    'burnside_exact': True,
    'fast_or_heuristic_traversal_used': False,
    'canonical_augmentation_completeness_claimed': False,
    'skeleton_orbit_records': records,
    'full_Q4_condition_certified': False,
    'endpoint_finite_q_certified': False,
    'endpoint_full_action_conjugacy_certified': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'next_exact_leaf': 'L33-07-IMPOSE-EXACT-Q4-IMAGE-ORDER-AND-ENDPOINT-FINITE-Q-ACTION-ON-17146944-K3-INTEGRAL-SYMMETRY-ORBITS',
    'new_residual_kernel': 'R33-BR2A-NONELEMENTARY-K3-572522496-INTEGRAL-CC-CT-H-IN-17146944-EXACT-SYMMETRY-ORBITS',
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
(HERE / 'nonelementary-k3-integral-cc-ct-orbits.json').write_text(
    json.dumps(certificate, indent=2, sort_keys=True) + '\n'
)
print(json.dumps({
    'success': True,
    'predecessor_structural_H': predecessor_reconstructed,
    'after_integral_cc_ct_structural_H': after_integral_cc_ct,
    'after_integral_cc_ct_full_symmetry_orbits': full_symmetry_orbits,
    'cc_dimension_histogram': certificate['integral_cc_ct_lift_dimension_histogram_over_skeleton_orbits'],
    'certificate_sha256': certificate['canonical_sha256'],
    'next': certificate['next_exact_leaf'],
}, indent=2, sort_keys=True))
