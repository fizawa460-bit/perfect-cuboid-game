#!/usr/bin/env python3
"""Exact Burnside/canonical-augmentation reduction of k=3 lift sections.

The source leaf reduces the Q8- and forced-cc-compatible k=3 branch to 189
integral coordinate-symmetry orbits of (P,W) skeletons.  Over a fixed skeleton
the remaining order-four lift sections form an affine F2 space of dimension
21 or 22.  Brute enumeration would revisit 7,927,234,560 structural H.

For every skeleton representative this leaf computes its exact stabilizer in
the retained order-288 integral symmetry, derives the induced affine action on
the 24 lift coordinates (including the binary-addition carry), and applies
Burnside's lemma.  Fixed-section counts are obtained by exact F2 elimination;
no lift section is sampled or enumerated individually.

This quotients only by proved integral ambient symmetries.  It does not impose
the remaining full Q[4], finite-q, or integral cc/ct compatibility and does not
identify the actual glue.
"""
import hashlib
import json
import runpy
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKELETON_LOCK = 'd01faf0f252da478f2ec36d02027b7db4bd74b6bcf6e93a3b5f12169460b3505'

ns = runpy.run_path(str(HERE / 'certify_nonelementary_k3_q8_skeleton_orbits.py'))
source = json.loads((HERE / 'nonelementary-k3-q8-skeleton-orbits.json').read_text())
if source.get('canonical_sha256') != SKELETON_LOCK:
    raise SystemExit('k3 skeleton-orbit source lock moved')

canon = ns['canon']
rank = ns['rank']
complement = ns['complement']
symmetry = ns['symmetry']
transport_vector = ns['transport_vector']
transport_skeleton = ns['transport_skeleton']
X_MASK = (1 << 10) - 1
NVAR = 24


def affine_rank(rows, variable_count=NVAR):
    """Return (coefficient rank, consistent) for (mask,rhs) F2 equations."""
    pivots = {}
    for mask, rhs in rows:
        value = int(mask) | ((int(rhs) & 1) << variable_count)
        coefficient = value & ((1 << variable_count) - 1)
        while coefficient:
            pivot = coefficient.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
                coefficient = value & ((1 << variable_count) - 1)
            else:
                pivots[pivot] = value
                break
        if not coefficient and ((value >> variable_count) & 1):
            return len(pivots), False
    return len(pivots), True


def span_coordinate_map(basis):
    coordinates = {0: 0}
    for i, vector in enumerate(basis):
        additions = {value ^ vector: mask | (1 << i) for value, mask in coordinates.items()}
        if any(value in coordinates for value in additions):
            raise SystemExit('dependent coordinate basis')
        coordinates.update(additions)
    return coordinates


def dot_parity(a, b):
    return (int(a) & int(b)).bit_count() & 1


def section_equations(p_basis, quotient_basis):
    rows = []
    for i in range(3):
        for j in range(i):
            mask = 0
            for a, vector in enumerate(quotient_basis):
                if dot_parity(vector & X_MASK, p_basis[j] & X_MASK):
                    mask ^= 1 << (8 * i + a)
                if dot_parity(vector & X_MASK, p_basis[i] & X_MASK):
                    mask ^= 1 << (8 * j + a)
            c_value = (
                (p_basis[i] & p_basis[j] & X_MASK).bit_count()
                + 2 * (p_basis[i] & p_basis[j] & ~X_MASK).bit_count()
            )
            if c_value & 1:
                raise SystemExit('P half-pairing parity regression')
            rows.append((mask, (c_value // 2) & 1))
    return rows


def affine_action(p_basis, w_basis, quotient_basis, quotient_coordinates, permutation):
    transported_p = tuple(transport_vector(vector, permutation) for vector in p_basis)
    transported_coordinates = span_coordinate_map(transported_p)
    linear_rows = [0] * NVAR
    constant_mask = 0
    for output_generator, target_p in enumerate(p_basis):
        combination = transported_coordinates.get(target_p)
        if combination is None:
            raise SystemExit('stabilizer does not preserve P')
        selected = [j for j in range(3) if (combination >> j) & 1]
        carry = 0
        for coordinate in range(14):
            total = sum((transported_p[j] >> coordinate) & 1 for j in selected)
            target_bit = (target_p >> coordinate) & 1
            if (total - target_bit) % 2:
                raise SystemExit('binary carry parity regression')
            if ((total - target_bit) // 2) & 1:
                carry |= 1 << coordinate
        carry_q = quotient_coordinates[carry] >> 6
        for output_bit in range(8):
            if (carry_q >> output_bit) & 1:
                constant_mask |= 1 << (8 * output_generator + output_bit)
        for input_generator in selected:
            for input_bit, vector in enumerate(quotient_basis):
                transported = transport_vector(vector, permutation)
                output_q = quotient_coordinates[transported] >> 6
                input_variable = 8 * input_generator + input_bit
                for output_bit in range(8):
                    if (output_q >> output_bit) & 1:
                        linear_rows[8 * output_generator + output_bit] ^= 1 << input_variable
    return linear_rows, constant_mask


def verify_affine_solution_preservation(equations, linear_rows, constant_mask):
    base_rank, consistent = affine_rank(equations)
    if not consistent:
        raise SystemExit('source lift-section equations inconsistent')
    for equation_mask, equation_rhs in equations:
        transformed_mask = 0
        transformed_constant = 0
        for output_bit in range(NVAR):
            if (equation_mask >> output_bit) & 1:
                transformed_mask ^= linear_rows[output_bit]
                transformed_constant ^= (constant_mask >> output_bit) & 1
        target_rhs = equation_rhs ^ transformed_constant
        new_rank, new_consistent = affine_rank(equations + [(transformed_mask, target_rhs)])
        if not new_consistent or new_rank != base_rank:
            raise SystemExit('stabilizer affine action does not preserve lift equations')


def inverse_permutation(permutation):
    inverse = [0] * len(permutation)
    for old, new in enumerate(permutation):
        inverse[new] = old
    return tuple(inverse)


def verify_affine_inverse(p_basis, w_basis, quotient_basis, quotient_coordinates,
                          permutation, linear_rows, constant_mask):
    inverse_rows, inverse_constant = affine_action(
        p_basis, w_basis, quotient_basis, quotient_coordinates,
        inverse_permutation(permutation),
    )
    for output_bit, inverse_row in enumerate(inverse_rows):
        composed_row = 0
        composed_constant = (inverse_constant >> output_bit) & 1
        for middle_bit in range(NVAR):
            if (inverse_row >> middle_bit) & 1:
                composed_row ^= linear_rows[middle_bit]
                composed_constant ^= (constant_mask >> middle_bit) & 1
        if composed_row != (1 << output_bit) or composed_constant:
            raise SystemExit('stabilizer affine inverse regression')


records = []
total_structural_h = 0
total_full_symmetry_orbits = 0
stabilizer_histogram = Counter()
solution_dimension_histogram = Counter()
fixed_log_histogram = Counter()

for index, representative in enumerate(source['orbit_representatives']):
    p_basis = tuple(int(x) for x in representative['P_basis_bits'])
    w_basis = tuple(int(x) for x in representative['W_basis_bits'])
    skeleton = (p_basis, w_basis)
    orbit_size = int(representative['orbit_size'])
    if len(p_basis) != 3 or len(w_basis) != 6:
        raise SystemExit('k3 skeleton rank regression')
    quotient_basis = complement(w_basis, canon(1 << j for j in range(14)))
    if len(quotient_basis) != 8:
        raise SystemExit('V/W quotient dimension regression')
    coordinate_basis = w_basis + quotient_basis
    quotient_coordinates = span_coordinate_map(coordinate_basis)
    if len(quotient_coordinates) != 1 << 14:
        raise SystemExit('V coordinate-map completeness regression')

    equations = section_equations(p_basis, quotient_basis)
    equation_rank, consistent = affine_rank(equations)
    if not consistent or equation_rank not in (2, 3):
        raise SystemExit('lift-section affine rank regression')
    solution_dimension = NVAR - equation_rank
    expected_dimension = 22 if rank([p & X_MASK for p in p_basis]) == 1 else 21
    if solution_dimension != expected_dimension:
        raise SystemExit('t/lift-dimension regression')

    stabilizer = [
        permutation for permutation in symmetry
        if transport_skeleton(skeleton, permutation) == skeleton
    ]
    if len(stabilizer) * orbit_size != len(symmetry):
        raise SystemExit('orbit-stabilizer regression')

    fixed_counts = []
    local_fixed_logs = Counter()
    for permutation in stabilizer:
        linear_rows, constant_mask = affine_action(
            p_basis, w_basis, quotient_basis, quotient_coordinates, permutation
        )
        if rank(linear_rows) != NVAR:
            raise SystemExit('stabilizer affine linear part is singular')
        verify_affine_inverse(
            p_basis, w_basis, quotient_basis, quotient_coordinates,
            permutation, linear_rows, constant_mask,
        )
        verify_affine_solution_preservation(equations, linear_rows, constant_mask)
        fixed_equations = list(equations)
        for output_bit in range(NVAR):
            fixed_equations.append((
                linear_rows[output_bit] ^ (1 << output_bit),
                (constant_mask >> output_bit) & 1,
            ))
        fixed_rank, fixed_consistent = affine_rank(fixed_equations)
        fixed_count = (1 << (NVAR - fixed_rank)) if fixed_consistent else 0
        fixed_counts.append(fixed_count)
        local_fixed_logs[-1 if fixed_count == 0 else fixed_count.bit_length() - 1] += 1

    burnside_sum = sum(fixed_counts)
    if burnside_sum % len(stabilizer):
        raise SystemExit('Burnside divisibility regression')
    fibre_orbits = burnside_sum // len(stabilizer)
    solution_count = 1 << solution_dimension
    total_structural_h += orbit_size * solution_count
    total_full_symmetry_orbits += fibre_orbits
    stabilizer_histogram[len(stabilizer)] += 1
    solution_dimension_histogram[solution_dimension] += 1
    fixed_log_histogram.update(local_fixed_logs)
    records.append({
        'skeleton_orbit_index': index,
        'skeleton_orbit_size': orbit_size,
        'stabilizer_order': len(stabilizer),
        'lift_equation_rank': equation_rank,
        'lift_solution_dimension': solution_dimension,
        'lift_solution_count': solution_count,
        'fixed_count_log2_histogram_minus1_is_zero': {
            str(log): count for log, count in sorted(local_fixed_logs.items())
        },
        'exact_stabilizer_fibre_orbit_count': fibre_orbits,
    })

if total_structural_h != source['structural_H_count_after_forced_cc_mod2']:
    raise SystemExit('full k3 structural-H reconstruction regression')

certificate = {
    'schema': 'STAGE33_07_NONELEMENTARY_K3_LIFT_SECTION_ORBITS_V1',
    'source_k3_skeleton_orbits_sha256': SKELETON_LOCK,
    'source_symmetry_order': len(symmetry),
    'source_skeleton_orbit_count': len(source['orbit_representatives']),
    'source_cc_compatible_skeleton_count': source['forced_cc_mod2_compatible_skeleton_count'],
    'source_structural_H_count': source['structural_H_count_after_forced_cc_mod2'],
    'affine_lift_coordinate_count': NVAR,
    'binary_carry_included_in_stabilizer_action': True,
    'fixed_sets_counted_by_exact_F2_elimination': True,
    'burnside_exact': True,
    'stabilizer_order_histogram': {str(k): v for k, v in sorted(stabilizer_histogram.items())},
    'solution_dimension_histogram': {str(k): v for k, v in sorted(solution_dimension_histogram.items())},
    'global_fixed_count_log2_histogram_minus1_is_zero': {
        str(k): v for k, v in sorted(fixed_log_histogram.items())
    },
    'structural_H_count_reconstructed': total_structural_h,
    'exact_full_symmetry_orbit_count': total_full_symmetry_orbits,
    'compression_denominator_before': total_structural_h,
    'compression_numerator_after': total_full_symmetry_orbits,
    'skeleton_orbit_records': records,
    'full_Q4_condition_certified': False,
    'endpoint_finite_q_certified': False,
    'endpoint_full_action_conjugacy_certified': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'next_exact_leaf': 'L33-07-IMPOSE-Q4-AND-INTEGRAL-CC-CT-ON-K3-AFFINE-ORBIT-REPRESENTATIVES',
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
(HERE / 'nonelementary-k3-lift-section-orbits.json').write_text(
    json.dumps(certificate, indent=2, sort_keys=True) + '\n'
)
print(json.dumps({
    'success': True,
    'skeleton_orbits': certificate['source_skeleton_orbit_count'],
    'structural_H': certificate['structural_H_count_reconstructed'],
    'full_symmetry_orbits': certificate['exact_full_symmetry_orbit_count'],
    'stabilizers': certificate['stabilizer_order_histogram'],
    'certificate_sha256': certificate['canonical_sha256'],
    'next': certificate['next_exact_leaf'],
}, indent=2, sort_keys=True))
