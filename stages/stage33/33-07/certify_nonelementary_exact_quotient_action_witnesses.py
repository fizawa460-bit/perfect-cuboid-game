#!/usr/bin/env python3
"""Exact quotient/action witnesses for two surviving non-elementary E7 types.

The preceding E7, target-Q[4]-rank, and target-exponent-eight certificates are
necessary-condition censuses.  This leaf guards against treating those filters
as if they were already complete: for k=1 and k=2 it supplies an explicit
order-512 totally isotropic subgroup H of

    A0 = (Z/8)^10 direct_sum (Z/16)^4

which is stable under all seven coordinate-sign actions and under one retained
scaled cc/ct lift pair, and for which H^perp/H has *exactly* the endpoint
abelian invariant factors

    (Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4.

The quotient is computed as an integral-lattice kernel followed by an exact
Smith decomposition.  This does not identify the actual index-512 glue and it
does not certify an isometry of finite quadratic modules or conjugacy to the
endpoint actions.
"""
import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp

from picard_coordinate_sign_rows_retained import load as load_sign_bundle

HERE = Path(__file__).resolve().parent
MODS0 = [8] * 10 + [16] * 4
QDIAG = [2] * 10 + [1] * 4
TARGET = [2] * 4 + [4] * 6 + [8] * 4
PIECES = [(0, 1), (2, 3), (4, 5), (6, 10), (7, 11), (8, 12), (9, 13)]
PIECE_NAMES = ['kb', 'kb', 'kb', 'kc', 'ka', 'ka', 'ka']

STRUCTURAL_LOCK = '235298bd303c0f21d946f6ca537ca30d42e049a6739c1ef106ecef760499c9e9'
Q4_LOCK = '8eb225add746b5dcf1dcb3407b22d2b5ccfc6e6637b6e94b69d41edf30e8a6f3'
Q8_LOCK = '4a5c84ad765f93442f08991ffdcea0bab6f1ae5a3ab6561157201bba262f75ee'
ACTION_LOCK = 'a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20'
SIGN_BUNDLE_LOCK = '5cd64ca89ee9f3ec76d275bc4082349764ac8a5cb4647a9bb9a4eaf267b76ab9'
TARGET_Q_LOCK = '4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0'

SOURCES = {
    'nonelementary-sign-target-q2-structural-reduction.json': STRUCTURAL_LOCK,
    'nonelementary-target-q4-rank-obstruction.json': Q4_LOCK,
    'nonelementary-target-q8-exponent-reduction.json': Q8_LOCK,
}
for name, lock in SOURCES.items():
    source = json.loads((HERE / name).read_text())
    if source.get('canonical_sha256') != lock:
        raise SystemExit(f'source lock moved: {name}')

actions = json.loads((HERE / 'coordinate-k3-scaled-action-choices-retained.json').read_text())
if actions.get('canonical_sha256') != ACTION_LOCK:
    raise SystemExit('scaled action source lock moved')
if load_sign_bundle().get('canonical_sha256') != SIGN_BUNDLE_LOCK:
    raise SystemExit('coordinate-sign retained bundle lock moved')
target_q = json.loads((HERE / 'picard-discriminant-compact.json').read_text())
if target_q.get('canonical_sha256') != TARGET_Q_LOCK:
    raise SystemExit('endpoint finite-q source lock moved')
TARGET_B8 = [[
    -int(x) % (16 if i == j else 8) for j, x in enumerate(row)
] for i, row in enumerate(target_q['discriminant_bilinear_numerator_over_8_reduced'])]

# Rows are actual A0 coordinates.  The first k rows have order four and the
# remaining rows order two.  They are deliberately explicit audit witnesses,
# not representatives claimed to be unique or actual transcendental glue.
WITNESSES = {
    'k1_Z4_plus_Z2_7': {
        'orders': [4] + [2] * 7,
        'rows': [
            [0,0,0,0,0,0,0,0,0,0,4,4,4,4],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,8],
            [0,0,0,0,0,0,0,0,0,0,0,0,8,0],
            [0,0,0,0,0,0,0,0,0,0,0,8,0,0],
            [0,0,4,0,4,0,4,0,4,0,0,0,0,0],
            [4,0,4,4,0,0,0,4,0,0,0,0,0,0],
            [0,0,4,4,4,4,0,0,0,0,0,0,0,0],
            [4,4,0,0,0,0,0,0,0,0,0,0,0,0],
        ],
    },
    'k2_Z4_2_plus_Z2_5': {
        'orders': [4, 4] + [2] * 5,
        'rows': [
            [0,0,0,0,0,0,0,0,0,0,4,4,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,4,4],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,8],
            [0,0,0,0,0,0,0,0,0,0,0,8,0,0],
            [0,0,0,0,4,4,0,0,0,0,0,0,0,0],
            [0,0,4,4,0,0,0,0,0,0,0,0,0,0],
            [4,4,0,0,0,0,0,0,0,0,0,0,0,0],
        ],
    },
}

def add(a, b):
    return tuple((int(x) + int(y)) % m for x, y, m in zip(a, b, MODS0))


def scale(c, a):
    return tuple((int(c) * int(x)) % m for x, m in zip(a, MODS0))


def q32(a):
    return sum(c * int(x) * int(x) for c, x in zip(QDIAG, a)) % 32


def b16(a, b):
    return sum(c * int(x) * int(y) for c, x, y in zip(QDIAG, a, b)) % 16


def apply(a, matrix):
    return tuple(
        sum(int(a[i]) * int(matrix[i][j]) for i in range(14)) % MODS0[j]
        for j in range(14)
    )


def compose(a, b):
    return [[
        sum(int(a[i][k]) * int(b[k][j]) for k in range(14)) % MODS0[j]
        for j in range(14)
    ] for i in range(14)]


def identity():
    return [[int(i == j) for j in range(14)] for i in range(14)]


def global_action(kind):
    matrix = identity()
    for (a, b), name in zip(PIECES, PIECE_NAMES):
        local = actions['pieces'][name][kind + '_actions'][0]
        for ii, u in enumerate((a, b)):
            for jj, v in enumerate((a, b)):
                matrix[u][v] = int(local[ii][jj]) % MODS0[v]
    return matrix


def sign_action(piece):
    # The retained coordinate-sign convention is +1 on its rank-two piece and
    # -1 on the other six pieces.
    matrix = [[0] * 14 for _ in range(14)]
    for j, modulus in enumerate(MODS0):
        matrix[j][j] = 1 if j in piece else modulus - 1
    return matrix


def verify_ambient_isometry(matrix, label):
    for i, mi in enumerate(MODS0):
        for j, mj in enumerate(MODS0):
            if mi * int(matrix[i][j]) % mj:
                raise SystemExit(f'{label}: action is not well-defined')
    if compose(matrix, matrix) != identity():
        raise SystemExit(f'{label}: action is not an involution')
    rows = [tuple(row) for row in matrix]
    for i in range(14):
        if q32(rows[i]) != QDIAG[i] % 32:
            raise SystemExit(f'{label}: diagonal q regression')
        for j in range(i):
            if b16(rows[i], rows[j]):
                raise SystemExit(f'{label}: off-diagonal pairing regression')


def enumerate_subgroup(rows, orders, label):
    seen = set()
    for coeffs in itertools.product(*[range(order) for order in orders]):
        x = (0,) * 14
        for coefficient, row in zip(coeffs, rows):
            x = add(x, scale(coefficient, row))
        if x in seen:
            raise SystemExit(f'{label}: witness generators are not independent')
        seen.add(x)
    if len(seen) != 512:
        raise SystemExit('witness subgroup order regression')
    if any(q32(x) for x in seen):
        raise SystemExit('witness subgroup is not totally isotropic')
    return seen


def quotient_data(rows):
    # K is the full inverse image of H^perp in Z^14.  Pairing with each H row
    # is one congruence modulo 16; adjoining its slack variable gives an exact
    # integer kernel.  Zero Smith columns projected to the first 14 coordinates
    # are a row basis of K.
    count = len(rows)
    congruences = [[int(h[j]) * (16 // MODS0[j]) for j in range(14)] for h in rows]
    augmented = sp.Matrix([
        congruences[i] + [-16 * int(i == j) for j in range(count)]
        for i in range(count)
    ])
    diagonal, left, right = smith_normal_decomp(augmented, domain=ZZ)
    if left * augmented * right != diagonal:
        raise SystemExit('orthogonal-kernel Smith transform regression')
    rank = sum(diagonal[i, i] != 0 for i in range(min(diagonal.shape)))
    basis = sp.Matrix([
        [int(right[i, j]) for i in range(14)]
        for j in range(rank, right.cols)
    ])
    if basis.shape != (14, 14) or abs(int(basis.det())) != 512:
        raise SystemExit('orthogonal-kernel basis/index regression')
    basis_inverse = basis.inv()

    relation_rows = []
    for j, modulus in enumerate(MODS0):
        period = [0] * 14
        period[j] = modulus
        relation_rows.append(period)
    relation_rows.extend(rows)
    coordinates = []
    for relation in relation_rows:
        vector = sp.Matrix([relation]) * basis_inverse
        if any(x.q != 1 for x in vector):
            raise SystemExit('H/ambient relation is not integral in Hperp basis')
        coordinates.append([int(x) for x in vector])
    relations = sp.Matrix(coordinates)
    qdiag, qleft, qright = smith_normal_decomp(relations, domain=ZZ)
    if qleft * relations * qright != qdiag:
        raise SystemExit('quotient Smith transform regression')
    invariant_factors = [abs(int(qdiag[i, i])) for i in range(14)]

    # Transport the ambient pairing to the same Smith coordinates.  Its
    # numerator initially has denominator 16; evenness after transport gives
    # the standard numerator-over-8 convention used by the endpoint lock.
    pairing16 = sp.zeros(14)
    for a in range(14):
        for b in range(14):
            pairing16[a, b] = sum(
                (16 // MODS0[j]) * int(basis[a, j]) * int(basis[b, j])
                for j in range(14)
            )
    right_inverse = qright.inv()
    transported16 = right_inverse * pairing16 * right_inverse.T
    if any(int(transported16[i, j]) % 2 for i in range(14) for j in range(14)):
        raise SystemExit('quotient pairing denominator regression')
    pairing8 = [[
        int(transported16[i, j] // 2) % (16 if i == j else 8)
        for j in range(14)
    ] for i in range(14)]
    return invariant_factors, pairing8


def q_value_profile(pairing8, layer):
    profile = {0: 0, 4: 0, 8: 0, 12: 0}
    if layer == 'Q2':
        values = [[0, modulus // 2] for modulus in TARGET]
    elif layer == '2Q':
        values = [list(range(0, modulus, 2)) for modulus in TARGET]
    elif layer == '4Q':
        values = [list(range(0, modulus, 4)) for modulus in TARGET]
    else:
        raise ValueError(layer)
    for vector in itertools.product(*values):
        value = sum(
            vector[i] * pairing8[i][j] * vector[j]
            for i in range(14) for j in range(14)
        ) % 16
        if value not in profile:
            raise SystemExit('unexpected Q[2] quadratic value')
        profile[value] += 1
    return {str(k): v for k, v in profile.items() if v}


cc = global_action('cc')
ct = global_action('ct')
signs = [sign_action(piece) for piece in PIECES]
for label, matrix in [('cc_choice_0', cc), ('ct_choice_0', ct)] + [
    (f'coordinate_sign_{i}', matrix) for i, matrix in enumerate(signs)
]:
    verify_ambient_isometry(matrix, label)

records = {}
target_q2_profile = q_value_profile(TARGET_B8, 'Q2')
target_2q_profile = q_value_profile(TARGET_B8, '2Q')
target_4q_profile = q_value_profile(TARGET_B8, '4Q')
if target_q2_profile != {'0': 8192, '8': 8192}:
    raise SystemExit('endpoint Q[2] profile regression')
if target_2q_profile != {'0': 8192, '8': 8192} or target_4q_profile != {'0': 16}:
    raise SystemExit('endpoint 2Q/4Q profile regression')
for name, witness in WITNESSES.items():
    rows = [tuple(row) for row in witness['rows']]
    orders = witness['orders']
    subgroup = enumerate_subgroup(rows, orders, name)
    stability = {}
    for label, matrix in [('cc_choice_0', cc), ('ct_choice_0', ct)] + [
        (f'coordinate_sign_{i}', matrix) for i, matrix in enumerate(signs)
    ]:
        stable = all(apply(row, matrix) in subgroup for row in rows)
        if not stable:
            raise SystemExit(f'{name}: failed {label} stability')
        stability[label] = True
    factors, pairing8 = quotient_data(rows)
    if factors != TARGET:
        raise SystemExit(f'{name}: exact quotient invariant-factor regression {factors}')
    source_q2_profile = q_value_profile(pairing8, 'Q2')
    source_2q_profile = q_value_profile(pairing8, '2Q')
    source_4q_profile = q_value_profile(pairing8, '4Q')
    records[name] = {
        'abstract_H_orders': orders,
        'generator_rows_in_A0': witness['rows'],
        'all_512_elements_distinct_and_isotropic_verified': True,
        'action_stability': stability,
        'quotient_invariant_factors': factors,
        'target_Q2_log2': 14,
        'target_Q4_log2': 24,
        'target_exponent': 8,
        'source_quotient_B8_smith_coordinates': pairing8,
        'source_Q2_quadratic_value_profile_numerator_over_8': source_q2_profile,
        'endpoint_Q2_quadratic_value_profile_numerator_over_8': target_q2_profile,
        'Q2_profile_matches_endpoint': source_q2_profile == target_q2_profile,
        'source_2Q_quadratic_value_profile_numerator_over_8': source_2q_profile,
        'endpoint_2Q_quadratic_value_profile_numerator_over_8': target_2q_profile,
        'twoQ_profile_matches_endpoint': source_2q_profile == target_2q_profile,
        'source_4Q_quadratic_value_profile_numerator_over_8': source_4q_profile,
        'endpoint_4Q_quadratic_value_profile_numerator_over_8': target_4q_profile,
        'fourQ_profile_matches_endpoint': source_4q_profile == target_4q_profile,
    }

if records['k1_Z4_plus_Z2_7']['Q2_profile_matches_endpoint'] is not True:
    raise SystemExit('k1 Q2-profile regression')
if records['k2_Z4_2_plus_Z2_5']['Q2_profile_matches_endpoint'] is not False:
    raise SystemExit('k2 Q2-profile rejection regression')
if records['k1_Z4_plus_Z2_7']['twoQ_profile_matches_endpoint'] is not False:
    raise SystemExit('k1 2Q-profile rejection regression')
if records['k2_Z4_2_plus_Z2_5']['twoQ_profile_matches_endpoint'] is not False:
    raise SystemExit('k2 2Q-profile rejection regression')
if not all(r['fourQ_profile_matches_endpoint'] for r in records.values()):
    raise SystemExit('explicit witness 4Q-profile regression')

certificate = {
    'schema': 'STAGE33_07_NONELEMENTARY_EXACT_QUOTIENT_ACTION_WITNESSES_V1',
    'source_locks': {
        'E7_structural_sha256': STRUCTURAL_LOCK,
        'target_Q4_rank_sha256': Q4_LOCK,
        'target_Q8_exponent_sha256': Q8_LOCK,
        'scaled_action_choices_sha256': ACTION_LOCK,
        'coordinate_sign_bundle_sha256': SIGN_BUNDLE_LOCK,
        'endpoint_finite_q_sha256': TARGET_Q_LOCK,
    },
    'ambient_A0': '(Z/8)^10 direct_sum (Z/16)^4',
    'endpoint_abelian_target': '(Z/2)^4 direct_sum (Z/4)^6 direct_sum (Z/8)^4',
    'exact_witness_type_count': len(records),
    'exact_witness_types': list(records),
    'records': records,
    'consequence': 'exact quotient invariant factors plus seven-sign and one retained cc/ct-pair stability do not eliminate the k=1 or k=2 E7 branches',
    'specific_k2_witness_rejected_by_Q2_value_profile': True,
    'specific_k1_witness_Q2_profile_inconclusive': True,
    'specific_k1_witness_rejected_by_2Q_value_profile': True,
    'both_explicit_witnesses_rejected_by_q_filtration': True,
    'k3_exact_quotient_action_witness_certified': False,
    'endpoint_finite_q_certified': False,
    'endpoint_full_action_conjugacy_certified': False,
    'actual_index512_glue_identified': False,
    'arithmetic_HS_closed': False,
    'next_exact_leaf': 'L33-07-SEARCH-K1-K2-STRUCTURAL-BRANCHES-BEYOND-THE-TWO-REJECTED-EXPLICIT-WITNESSES-AND-CONSTRUCT-OR-REJECT-K3-EXACT-QUOTIENT-WITNESS',
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
(HERE / 'nonelementary-exact-quotient-action-witnesses.json').write_text(
    json.dumps(certificate, indent=2, sort_keys=True) + '\n'
)
print(json.dumps({
    'success': True,
    'exact_witness_types': list(records),
    'quotient_invariant_factors': TARGET,
    'certificate_sha256': certificate['canonical_sha256'],
    'next': certificate['next_exact_leaf'],
}, indent=2, sort_keys=True))
