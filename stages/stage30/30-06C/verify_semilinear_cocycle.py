#!/usr/bin/env python3
"""Independent exact verifier for Stage30-06C.

This program does not import or execute the Stage30-06 generator checker.  It
reconstructs PSL2(Z/4), the source-derived diagonal X(8) quotient action, the
24 projective endpoint representatives, theta, the V4 sign-deck intersection,
and every semilinear identity using rational Gaussian arithmetic.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
COORDS = ("a1", "a2", "a3", "b1", "b2", "b3", "c")
QCOORDS = ("U", "V", "W", "X", "Y", "T", "Z")
N = len(COORDS)

SPEC_PATH = ROOT / "stages/stage30/30-06/semilinear-spec.json"
ACTION_PATH = ROOT / "stages/stage30/30-02C/action-tables.json"
AUDIT_STATE_PATH = ROOT / "stages/stage30/30-06/audit-state.json"
COMMON_ANCHOR_PATH = ROOT / "stages/stage30/30-05/common-anchor.json"
CERTIFICATE_PATH = HERE / "semilinear-certificate.json"
RESULT_PATH = HERE / "result.md"
MANIFEST_PATH = HERE / "repro-manifest.json"

MANIFEST_INPUTS = (
    "stages/stage30/30-06/source-lock.md",
    "stages/stage30/30-06/cocycle-derivation.md",
    "stages/stage30/30-06/source-action-lift-audit-repair.md",
    "stages/stage30/30-06/semilinear-spec.json",
    "stages/stage30/30-06/check_frozen_generators.py",
    "stages/stage30/30-06/audit.md",
    "stages/stage30/30-06/audit-state.json",
    "stages/stage30/30-05/audit.md",
    "stages/stage30/30-05/common-anchor.json",
    "stages/stage30/30-05/verify_common_anchor.py",
    "stages/stage30/30-02C/action-tables.json",
    "stages/stage29/29-02ha/exact-sign-cover-model.md",
    "stages/stage29/29-02g/exact-q-moduli-adapter.md",
    "stages/stage29/29-15/bounded-execution.md",
    "stages/stage30/ownership-amendment-2026-08-22.md",
    "stages/stage30/codex-handoff-contract.md",
    "stages/stage30/controller.json",
    "stages/stage30/handoffs/codex-task-C-30-06C-semilinear-verification.md",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


@dataclass(frozen=True)
class QI:
    """An exact element of Q(i)."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __init__(self, a=0, b=0):
        object.__setattr__(self, "a", Fraction(a))
        object.__setattr__(self, "b", Fraction(b))

    def __add__(self, other):
        other = qi(other)
        return QI(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return QI(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-qi(other))

    def __rsub__(self, other):
        return qi(other) - self

    def __mul__(self, other):
        other = qi(other)
        return QI(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = qi(other)
        denominator = other.a * other.a + other.b * other.b
        require(denominator != 0, "division by zero in Q(i)")
        return QI(
            (self.a * other.a + self.b * other.b) / denominator,
            (self.b * other.a - self.a * other.b) / denominator,
        )

    def conjugate(self):
        return QI(self.a, -self.b)

    def is_zero(self):
        return self.a == 0 and self.b == 0


def qi(value) -> QI:
    return value if isinstance(value, QI) else QI(value)


ZERO = QI(0)
ONE = QI(1)
I = QI(0, 1)
UNIT_BY_EXP = (ONE, I, QI(-1), QI(0, -1))
EXP_BY_UNIT = {unit: exponent for exponent, unit in enumerate(UNIT_BY_EXP)}


def zmat(rows: int, columns: int):
    return [[ZERO for _ in range(columns)] for _ in range(rows)]


def identity_matrix(size: int):
    matrix = zmat(size, size)
    for index in range(size):
        matrix[index][index] = ONE
    return matrix


def matrix_multiply(left, right):
    require(len(left[0]) == len(right), "matrix dimension mismatch")
    result = zmat(len(left), len(right[0]))
    for row in range(len(left)):
        for column in range(len(right[0])):
            result[row][column] = sum(
                (left[row][k] * right[k][column] for k in range(len(right))),
                ZERO,
            )
    return result


def matrix_equal(left, right):
    return left == right


def matrix_to_monomial(matrix):
    result = []
    used_columns = set()
    for row in matrix:
        nonzero = [(column, value) for column, value in enumerate(row) if not value.is_zero()]
        require(len(nonzero) == 1, "endpoint action is not monomial")
        column, value = nonzero[0]
        require(value in EXP_BY_UNIT, "endpoint coefficient is not a power of i")
        require(column not in used_columns, "endpoint action is not a permutation matrix")
        used_columns.add(column)
        result.append((EXP_BY_UNIT[value], column))
    require(len(used_columns) == N, "endpoint action misses a coordinate")
    return tuple(result)


def monomial_identity():
    return tuple((0, index) for index in range(N))


def monomial_compose(left, right):
    """Multiply pullback monomial maps in the displayed group order."""
    output = []
    for left_unit, left_column in left:
        right_unit, right_column = right[left_column]
        output.append(((left_unit + right_unit) % 4, right_column))
    return tuple(output)


def monomial_inverse(action):
    output = [None] * N
    for row, (unit, column) in enumerate(action):
        output[column] = ((-unit) % 4, row)
    return tuple(output)


def monomial_conjugate(action):
    return tuple(((-unit) % 4, column) for unit, column in action)


def pgl_normalize(action):
    candidates = [
        tuple(((unit + shift) % 4, column) for unit, column in action)
        for shift in range(4)
    ]
    return min(candidates)


def pgl_equal(left, right):
    return pgl_normalize(left) == pgl_normalize(right)


def pgl_power(action, exponent):
    result = monomial_identity()
    for _ in range(exponent):
        result = monomial_compose(result, action)
    return pgl_normalize(result)


def pgl_order(action):
    for exponent in range(1, 97):
        if pgl_equal(pgl_power(action, exponent), monomial_identity()):
            return exponent
    raise AssertionError("projective order exceeded the finite safety bound")


def diag_sign(negated):
    negated = set(negated)
    return tuple((2 if name in negated else 0, index) for index, name in enumerate(COORDS))


def unit_text(exponent: int, variable: str):
    return (variable, f"i*{variable}", f"-{variable}", f"-i*{variable}")[exponent]


def endpoint_json(action):
    action = pgl_normalize(action)
    return {COORDS[row]: unit_text(unit, COORDS[column]) for row, (unit, column) in enumerate(action)}


def parse_spec_action(mapping):
    parsed = []
    patterns = (
        ("-i*", 3),
        ("i*", 1),
        ("-", 2),
        ("", 0),
    )
    for name in COORDS:
        expression = mapping[name]
        for prefix, exponent in patterns:
            if expression.startswith(prefix):
                variable = expression[len(prefix):]
                if variable in COORDS:
                    parsed.append((exponent, COORDS.index(variable)))
                    break
        else:
            raise AssertionError(f"invalid frozen generator expression: {expression}")
    return tuple(parsed)


def derive_source_endpoint_generators():
    """Derive S_hat,T_hat from the one-factor X(8) formulas and invariants."""

    # Squared-polynomial basis is (x^2, xy, y^2).  These checks use only
    # sqrt(2)^2=2 and zeta_8^2=i, hence remain exact over Q(i).
    x2, xy, y2 = (ONE, ZERO, ZERO), (ZERO, ONE, ZERO), (ZERO, ZERO, ONE)
    u2 = tuple(QI(2) * entry for entry in xy)
    v2 = tuple(a - b for a, b in zip(x2, y2))
    w2 = tuple(a + b for a, b in zip(x2, y2))
    s_x2 = (QI(Fraction(1, 2)), QI(-1), QI(Fraction(1, 2)))
    s_y2 = (QI(Fraction(1, 2)), QI(1), QI(Fraction(1, 2)))
    s_xy = (QI(Fraction(-1, 2)), ZERO, QI(Fraction(1, 2)))
    s_u2 = tuple(QI(-1) * entry for entry in v2)  # (i v)^2
    s_v2 = tuple(QI(-1) * entry for entry in u2)  # (i u)^2
    s_w2 = w2
    require(s_u2 == tuple(QI(2) * entry for entry in s_xy), "S failed u^2=2xy")
    require(s_v2 == tuple(a - b for a, b in zip(s_x2, s_y2)),
            "S failed v^2=x^2-y^2")
    require(s_w2 == tuple(a + b for a, b in zip(s_x2, s_y2)),
            "S failed w^2=x^2+y^2")

    t_x2 = (QI(-1), ZERO, ZERO)
    t_y2 = (ZERO, ZERO, ONE)
    t_xy = tuple(I * entry for entry in xy)
    t_u2 = tuple(I * entry for entry in u2)       # (zeta_8 u)^2
    t_v2 = tuple(QI(-1) * entry for entry in w2) # (i w)^2
    t_w2 = tuple(QI(-1) * entry for entry in v2) # (i v)^2
    require(t_u2 == tuple(QI(2) * entry for entry in t_xy), "T failed u^2=2xy")
    require(t_v2 == tuple(a - b for a, b in zip(t_x2, t_y2)),
            "T failed v^2=x^2-y^2")
    require(t_w2 == tuple(a + b for a, b in zip(t_x2, t_y2)),
            "T failed w^2=x^2+y^2")

    # Bridge from endpoint coordinates to (U,V,W,X,Y,T,Z).
    bridge = zmat(7, 7)
    bridge[0][3] = QI(2)               # U=2b1
    bridge[1][4] = QI(2)               # V=2b2
    bridge[2][5] = QI(2)               # W=2b3
    bridge[3][0], bridge[3][6] = ONE, ONE
    bridge[4][0], bridge[4][6] = QI(-1), ONE
    bridge[5][1], bridge[5][2] = ONE, I
    bridge[6][1], bridge[6][2] = ONE, -I

    inverse_bridge = zmat(7, 7)
    half = QI(Fraction(1, 2))
    inverse_bridge[0][3], inverse_bridge[0][4] = half, -half
    inverse_bridge[1][5], inverse_bridge[1][6] = half, half
    inverse_bridge[2][5], inverse_bridge[2][6] = -I * half, I * half
    inverse_bridge[3][0] = half
    inverse_bridge[4][1] = half
    inverse_bridge[5][2] = half
    inverse_bridge[6][3], inverse_bridge[6][4] = half, half
    require(matrix_equal(matrix_multiply(inverse_bridge, bridge), identity_matrix(7)),
            "source invariant bridge is not invertible")

    s_quotient = zmat(7, 7)
    s_quotient[0][1] = QI(-1)          # U'=-V
    s_quotient[1][0] = QI(-1)          # V'=-U
    s_quotient[2][2] = ONE             # W'=W
    # The 1/2 factors are exactly the diagonal cancellation of sqrt(2)^2.
    for column, coefficient in ((3, half), (4, half), (5, -half), (6, -half)):
        s_quotient[3][column] = coefficient
    for column in (3, 4, 5, 6):
        s_quotient[4][column] = half
    for column, coefficient in ((3, -half), (4, half), (5, -half), (6, half)):
        s_quotient[5][column] = coefficient
    for column, coefficient in ((3, -half), (4, half), (5, half), (6, -half)):
        s_quotient[6][column] = coefficient

    t_quotient = zmat(7, 7)
    t_quotient[0][0] = I               # zeta_8^2 U=iU
    t_quotient[1][2] = QI(-1)          # V'=-W
    t_quotient[2][1] = QI(-1)          # W'=-V
    t_quotient[3][3] = QI(-1)          # X'=-X
    t_quotient[4][4] = ONE             # Y'=Y
    t_quotient[5][5] = I               # T'=iT
    t_quotient[6][6] = I               # Z'=iZ

    def product_of_linear_forms(left, right):
        output = {}
        for j, a in enumerate(left):
            for k, b in enumerate(right):
                monomial = tuple(sorted((j, k)))
                output[monomial] = output.get(monomial, ZERO) + a * b
        return {monomial: value for monomial, value in output.items() if not value.is_zero()}

    def relation_image(action):
        xy_image = product_of_linear_forms(action[3], action[4])
        tz_image = product_of_linear_forms(action[5], action[6])
        output = dict(xy_image)
        for monomial, value in tz_image.items():
            output[monomial] = output.get(monomial, ZERO) - value
            if output[monomial].is_zero():
                del output[monomial]
        return output

    quotient_relation = {(3, 4): ONE, (5, 6): QI(-1)}
    negative_quotient_relation = {monomial: -value for monomial, value in quotient_relation.items()}
    require(relation_image(s_quotient) in (quotient_relation, negative_quotient_relation),
            "S diagonal quotient does not preserve XY=TZ")
    require(relation_image(t_quotient) in (quotient_relation, negative_quotient_relation),
            "T diagonal quotient does not preserve XY=TZ")

    s_endpoint_matrix = matrix_multiply(inverse_bridge, matrix_multiply(s_quotient, bridge))
    t_endpoint_matrix = matrix_multiply(inverse_bridge, matrix_multiply(t_quotient, bridge))
    return matrix_to_monomial(s_endpoint_matrix), matrix_to_monomial(t_endpoint_matrix)


def mod_matrix_multiply(left, right):
    return tuple(
        tuple(sum(left[row][k] * right[k][column] for k in range(2)) % 4 for column in range(2))
        for row in range(2)
    )


def mod_negate(matrix):
    return tuple(tuple((-entry) % 4 for entry in row) for row in matrix)


def mod_canonical(matrix):
    return min(matrix, mod_negate(matrix))


def mod_inverse(matrix):
    determinant = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 4
    require(determinant in (1, 3), "matrix is not invertible modulo 4")
    inverse_determinant = determinant
    return (
        (matrix[1][1] * inverse_determinant % 4, -matrix[0][1] * inverse_determinant % 4),
        (-matrix[1][0] * inverse_determinant % 4, matrix[0][0] * inverse_determinant % 4),
    )


def reconstruct_modular_group(action_data):
    sl2 = [
        ((a, b), (c, d))
        for a, b, c, d in product(range(4), repeat=4)
        if (a * d - b * c) % 4 == 1
    ]
    group = sorted({mod_canonical(matrix) for matrix in sl2})
    require(len(sl2) == 48, "SL2(Z/4) does not have 48 elements")
    require(len(group) == 24, "PSL2(Z/4) does not have 24 elements")
    index = {matrix: position for position, matrix in enumerate(group)}
    multiplication = [
        [index[mod_canonical(mod_matrix_multiply(left, right))] for right in group]
        for left in group
    ]
    identity = index[((1, 0), (0, 1))]
    inverses = []
    orders = []
    for g in range(24):
        inverse_hits = [h for h in range(24) if multiplication[g][h] == identity and multiplication[h][g] == identity]
        require(len(inverse_hits) == 1, f"g{g:02d} has no unique inverse")
        inverses.append(inverse_hits[0])
        power_index = identity
        for order in range(1, 25):
            power_index = multiplication[power_index][g]
            if power_index == identity:
                orders.append(order)
                break
        else:
            raise AssertionError(f"g{g:02d} order exceeded 24")

    frozen_rows = action_data["modular"]["elements"]
    require([row["id"] for row in frozen_rows] == [f"g{i:02d}" for i in range(24)],
            "Task-A modular IDs are not contiguous")
    for position, row in enumerate(frozen_rows):
        frozen_matrix = tuple(tuple(entry for entry in line) for line in row["matrix"])
        require(frozen_matrix == group[position], f"Task-A matrix mismatch at g{position:02d}")
        require(row["order"] == orders[position], f"Task-A order mismatch at g{position:02d}")
        require(row["inverse"] == f"g{inverses[position]:02d}", f"Task-A inverse mismatch at g{position:02d}")
    return group, index, multiplication, identity, inverses, orders


def endpoint_quadrics():
    # Coefficients of q1,q2,q3,q4 in the diagonal monomial basis x_j^2.
    return (
        (ONE, ONE, ZERO, ZERO, ZERO, QI(-1), ZERO),
        (ONE, ZERO, ONE, ZERO, QI(-1), ZERO, ZERO),
        (ZERO, ONE, ONE, QI(-1), ZERO, ZERO, ZERO),
        (ONE, ONE, ONE, ZERO, ZERO, ZERO, QI(-1)),
    )


def exact_rank(rows):
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    pivot_row = 0
    for column in range(len(matrix[0])):
        pivot = next((row for row in range(pivot_row, len(matrix)) if not matrix[row][column].is_zero()), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_value = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / pivot_value for entry in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or matrix[row][column].is_zero():
                continue
            multiplier = matrix[row][column]
            matrix[row] = [a - multiplier * b for a, b in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def transform_diagonal_quadric(quadric, action):
    output = [ZERO] * N
    for row, coefficient in enumerate(quadric):
        unit, column = action[row]
        output[column] = output[column] + coefficient * UNIT_BY_EXP[(2 * unit) % 4]
    return tuple(output)


def preserves_cuboid_quadrics(action):
    quadrics = endpoint_quadrics()
    base_rank = exact_rank(quadrics)
    return all(exact_rank(quadrics + (transform_diagonal_quadric(q, action),)) == base_rank for q in quadrics)


def sign_pattern(action):
    require(all(column == row for row, (_, column) in enumerate(action)), "not a sign-deck element")
    shift = (-action[COORDS.index("c")][0]) % 4
    normalized = tuple(((unit + shift) % 4, column) for unit, column in action)
    require(all(unit in (0, 2) for unit, _ in normalized), "diagonal endpoint element is not a sign pattern")
    return [COORDS[row] for row, (unit, _) in enumerate(normalized) if unit == 2]


def reconstruct_certificate():
    for relative in MANIFEST_INPUTS:
        require((ROOT / relative).is_file(), f"mandatory source missing: {relative}")

    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    actions = json.loads(ACTION_PATH.read_text(encoding="utf-8"))
    audit_state = json.loads(AUDIT_STATE_PATH.read_text(encoding="utf-8"))
    common_anchor = json.loads(COMMON_ANCHOR_PATH.read_text(encoding="utf-8"))

    require(spec["schema"] == "STAGE30_06_SEMILINEAR_COCYCLE_SPEC_V2_SOURCE_DERIVED_LIFTS",
            "wrong semilinear specification version")
    require(audit_state["audit_verdict"] == "PASS_AFTER_BOUNDED_SOURCE_ACTION_LIFT_REPAIR",
            "Stage30-06 audit has not passed with the source-action repair")
    require(audit_state["codex_30_06c_prompt_audit_approved"] is True,
            "Stage30-06C prompt is not audit-approved")
    require(common_anchor["branch_squareclass_action"]["kernel_ids"] == ["g04", "g06", "g12", "g14"],
            "common-anchor V_mod mismatch")
    require(spec["endpoint_coordinate_order"] == list(COORDS), "endpoint coordinate order mismatch")
    require(spec["residual_group"]["V_mod_ids"] == ["g04", "g06", "g12", "g14"],
            "semilinear spec V_mod mismatch")
    require(spec["residual_group"]["S_mod"] == [[0, 3], [1, 0]], "frozen S_mod mismatch")
    require(spec["residual_group"]["T_mod"] == [[1, 1], [0, 1]], "frozen T_mod mismatch")
    require(spec["residual_group"]["D4"] == [[1, 0], [0, 3]], "frozen D4 mismatch")

    source_s, source_t = derive_source_endpoint_generators()
    frozen_s = parse_spec_action(spec["projective_generators"]["S_hat"])
    frozen_t = parse_spec_action(spec["projective_generators"]["T_hat"])
    require(source_s == frozen_s, "source-derived S_hat does not exactly match the frozen action")
    require(source_t == frozen_t, "source-derived T_hat does not exactly match the frozen action")
    require(preserves_cuboid_quadrics(source_s), "source-derived S_hat does not preserve cuboid quadrics")
    require(preserves_cuboid_quadrics(source_t), "source-derived T_hat does not preserve cuboid quadrics")

    group, index, multiplication, identity, inverses, orders = reconstruct_modular_group(actions)
    s_mod_matrix = ((0, 3), (1, 0))
    t_mod_matrix = ((1, 1), (0, 1))
    d4 = ((1, 0), (0, 3))
    s_mod = index[mod_canonical(s_mod_matrix)]
    t_mod = index[mod_canonical(t_mod_matrix)]
    require((s_mod, t_mod, identity) == (0, 8, 4), "Task-A generator or identity IDs changed")

    # Deterministic right-generator BFS establishes the concrete correspondence.
    endpoint_by_id = {identity: pgl_normalize(monomial_identity())}
    word_by_id = {identity: "1"}
    queue = [identity]
    for g in queue:
        for symbol, h, endpoint_h in (("S", s_mod, source_s), ("T", t_mod, source_t)):
            gh = multiplication[g][h]
            endpoint_gh = pgl_normalize(monomial_compose(endpoint_by_id[g], endpoint_h))
            word_gh = symbol if word_by_id[g] == "1" else word_by_id[g] + symbol
            if gh not in endpoint_by_id:
                endpoint_by_id[gh] = endpoint_gh
                word_by_id[gh] = word_gh
                queue.append(gh)
            else:
                require(endpoint_by_id[gh] == endpoint_gh,
                        f"endpoint representation is not well-defined at g{gh:02d}")
    require(len(endpoint_by_id) == 24, "endpoint representation does not cover all modular IDs")
    require(len(set(endpoint_by_id.values())) == 24, "duplicate endpoint projective representative")

    # Check the homomorphism exhaustively, not just along the BFS tree.
    for g in range(24):
        require(preserves_cuboid_quadrics(endpoint_by_id[g]), f"g{g:02d} fails cuboid-quadric preservation")
        for h in range(24):
            gh = multiplication[g][h]
            require(
                pgl_equal(monomial_compose(endpoint_by_id[g], endpoint_by_id[h]), endpoint_by_id[gh]),
                f"endpoint multiplication mismatch at g{g:02d}*g{h:02d}",
            )

    require(pgl_order(source_s) == 2, "S_hat projective order is not 2")
    require(pgl_order(source_t) == 4, "T_hat projective order is not 4")
    require(pgl_order(monomial_compose(source_s, source_t)) == 3, "S_hat*T_hat projective order is not 3")

    d4_inverse = mod_inverse(d4)
    theta = []
    for matrix in group:
        image = mod_canonical(mod_matrix_multiply(mod_matrix_multiply(d4, matrix), d4_inverse))
        require(image in index, "theta image is outside PSL2(Z/4)")
        theta.append(index[image])
    require(theta[s_mod] == s_mod, "theta(S) != S")
    require(theta[t_mod] == inverses[t_mod], "theta(T) != T^-1")
    for g in range(24):
        require(theta[theta[g]] == g, f"theta is not involutive at g{g:02d}")
        for h in range(24):
            require(theta[multiplication[g][h]] == multiplication[theta[g]][theta[h]],
                    f"theta is not a homomorphism at g{g:02d}*g{h:02d}")

    v_mod = [
        position
        for position, matrix in enumerate(group)
        if tuple(tuple(entry % 2 for entry in row) for row in matrix) == ((1, 0), (0, 1))
    ]
    require(v_mod == [4, 6, 12, 14], "independently reconstructed V_mod IDs are wrong")
    require(all(theta[v] == v for v in v_mod), "theta does not fix V_mod pointwise")

    sign_intersection = [
        g for g in range(24)
        if all(column == row for row, (_, column) in enumerate(endpoint_by_id[g]))
    ]
    require(sign_intersection == v_mod, "endpoint/sign-deck intersection is not exactly j(V_mod)")
    actual_patterns = {f"g{g:02d}": sign_pattern(endpoint_by_id[g]) for g in sign_intersection}
    expected_patterns = spec["v4_sign_deck_lift"]
    expected_patterns = {key: expected_patterns[key] for key in ("g04", "g06", "g12", "g14")}
    require(actual_patterns == expected_patterns, "V4 sign-deck patterns do not match the frozen lift")

    c_sigma = diag_sign(["a3"])
    require(spec["common_model_descent_cocycle"]["c_sigma"] == "delta_a3", "wrong frozen c_sigma")
    require(spec["common_model_descent_cocycle"]["negated_coordinates"] == ["a3"],
            "wrong frozen c_sigma coordinates")
    cocycle_product = monomial_compose(c_sigma, monomial_conjugate(c_sigma))
    require(pgl_equal(cocycle_product, monomial_identity()), "c_sigma*sigma(c_sigma) != 1")

    semilinear_pass = []
    for g in range(24):
        left = monomial_conjugate(endpoint_by_id[g])
        right = monomial_compose(
            monomial_compose(c_sigma, endpoint_by_id[theta[g]]),
            monomial_inverse(c_sigma),
        )
        semilinear_pass.append(pgl_equal(left, right))
    require(all(semilinear_pass), "one or more all-24 semilinear identities failed")

    modular_elements = []
    for g in range(24):
        modular_elements.append({
            "id": f"g{g:02d}",
            "matrix_mod_4": [list(row) for row in group[g]],
            "order": orders[g],
            "inverse_id": f"g{inverses[g]:02d}",
            "deterministic_word": word_by_id[g],
            "theta_id": f"g{theta[g]:02d}",
            "endpoint_representative": endpoint_json(endpoint_by_id[g]),
            "cuboid_quadrics_preserved": True,
            "semilinear_pass": semilinear_pass[g],
        })

    return {
        "schema": "STAGE30_06C_EXACT_SEMILINEAR_CERTIFICATE_V1",
        "task": "C_30_06C",
        "field": "Q(i)",
        "coordinate_order": list(COORDS),
        "exact_arithmetic_only": True,
        "input_source_lock_complete": True,
        "source_action_reconstruction": {
            "x8_factor_equations_verified": True,
            "diagonal_radicals_cancelled": ["sqrt(2)^2=2", "zeta_8^2=i"],
            "diagonal_quotient_defined_over_Qi": True,
            "S_hat": {COORDS[row]: unit_text(unit, COORDS[column]) for row, (unit, column) in enumerate(source_s)},
            "T_hat": {COORDS[row]: unit_text(unit, COORDS[column]) for row, (unit, column) in enumerate(source_t)},
            "frozen_generators_matched_exactly": True,
            "cuboid_quadrics_preserved": True,
        },
        "modular_group": {
            "name": "PSL2(Z/4)",
            "sl2_order": 48,
            "projective_order": 24,
            "canonicalization": "lexicographically least of M and -M modulo 4, row-major",
            "identity_id": "g04",
            "S_mod_id": "g00",
            "T_mod_id": "g08",
            "theta_definition": "D4*g*D4^-1",
            "D4": [[1, 0], [0, 3]],
            "theta_all24_verified": True,
            "elements": modular_elements,
        },
        "endpoint_projective_group": {
            "order": len(set(endpoint_by_id.values())),
            "correspondence_with_modular_ids_bijective": True,
            "multiplication_all_576_verified": True,
            "relations": {"S_order": 2, "T_order": 4, "ST_order": 3},
        },
        "v4_sign_deck": {
            "V_mod_ids": [f"g{g:02d}" for g in v_mod],
            "theta_fixes_pointwise": True,
            "intersection_ids": [f"g{g:02d}" for g in sign_intersection],
            "intersection_order": len(sign_intersection),
            "patterns_c_fixed_representative": actual_patterns,
            "verified": True,
        },
        "coordinate_cocycle": {
            "name": "delta_a3",
            "representative": {name: (f"-{name}" if name == "a3" else name) for name in COORDS},
            "q_defined": True,
            "sigma_image": "delta_a3",
            "quadratic_cocycle_identity_verified": True,
        },
        "semilinear_verification": {
            "identity": "sigma(alpha_hat(g))=c_sigma*alpha_hat(theta(g))*c_sigma^-1",
            "checked_element_count": 24,
            "passed_element_count": sum(semilinear_pass),
            "failed_element_count": 24 - sum(semilinear_pass),
            "all24_verified": all(semilinear_pass),
        },
        "scope_firewalls": {
            "k8_defect_classification_executed": False,
            "defect_elimination_count": 0,
            "new_theorem_assumed": False,
            "r29_kum5_discharged": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }


EXPECTED_RESULT = {
    "CODEX_TASK": "C_30_06C",
    "INPUT_SOURCE_LOCK_COMPLETE": "true",
    "EXACT_ARITHMETIC_ONLY": "true",
    "SOURCE_DERIVED_DIAGONAL_LIFTS_VERIFIED": "true",
    "MODULAR_GROUP_ORDER": "24",
    "MODULAR_ID_COVERAGE_COMPLETE": "true",
    "THETA_ALL24_VERIFIED": "true",
    "THETA_FIXES_V_MOD_POINTWISE": "true",
    "ENDPOINT_PROJECTIVE_GROUP_ORDER": "24",
    "V4_SIGN_DECK_INTERSECTION_VERIFIED": "true",
    "C_SIGMA": "delta_a3",
    "C_SIGMA_COCYCLE_VERIFIED": "true",
    "SEMILINEAR_ALL24_VERIFIED": "true",
    "FAILED_ELEMENT_COUNT": "0",
    "CHECKER_PRESENT": "true",
    "CHECKER_PASS": "true",
    "K8_DEFECT_CLASSIFICATION_EXECUTED": "false",
    "DEFECT_ELIMINATION_COUNT": "0",
    "NEW_THEOREM_ASSUMED": "false",
    "R29_KUM5_DISCHARGED": "false",
    "PERFECT_CUBOID_EXISTENCE_CLAIM": "false",
    "PERFECT_CUBOID_NONEXISTENCE_CLAIM": "false",
    "GALOIS_ACTION_CHECK": "PASS",
    "COCYCLE_IDENTITY_CHECK": "PASS",
    "SEMILINEAR_COMPATIBILITY_CHECK": "PASS",
    "CANDIDATE_ADAPTER_COUNT": "1",
    "CHECKED_CANDIDATE_COUNT": "1",
    "UNRESOLVED_ASSUMPTION_COUNT": "0",
}


def verify_result_file():
    require(RESULT_PATH.is_file(), "result.md is missing")
    observed = {}
    for line in RESULT_PATH.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([A-Z0-9_]+)=(.*)", line.strip())
        if match:
            key, value = match.groups()
            require(key not in observed, f"duplicate result key: {key}")
            observed[key] = value
    for key, expected in EXPECTED_RESULT.items():
        require(observed.get(key) == expected, f"result.md mismatch for {key}")


def sha256(path: Path):
    # read_text performs universal-newline conversion, so the manifest remains
    # reproducible across Git checkouts using LF or CRLF worktree endings.
    normalized_utf8 = path.read_text(encoding="utf-8").encode("utf-8")
    return hashlib.sha256(normalized_utf8).hexdigest()


def verify_manifest():
    require(MANIFEST_PATH.is_file(), "repro-manifest.json is missing")
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    require(manifest["schema"] == "STAGE30_06C_REPRO_MANIFEST_V1", "wrong manifest schema")
    require(manifest["task"] == "C_30_06C", "wrong manifest task")
    require(manifest["exact_arithmetic_only"] is True, "manifest does not require exact arithmetic")
    expected_inputs = set(MANIFEST_INPUTS)
    require(set(manifest["inputs_sha256"]) == expected_inputs, "manifest input set mismatch")
    for relative, digest in manifest["inputs_sha256"].items():
        require(sha256(ROOT / relative) == digest, f"input digest mismatch: {relative}")
    expected_outputs = {
        "stages/stage30/30-06C/semilinear-certificate.json",
        "stages/stage30/30-06C/verify_semilinear_cocycle.py",
        "stages/stage30/30-06C/result.md",
    }
    require(set(manifest["outputs_sha256"]) == expected_outputs, "manifest output set mismatch")
    for relative, digest in manifest["outputs_sha256"].items():
        require(sha256(ROOT / relative) == digest, f"output digest mismatch: {relative}")


def canonical_json(data):
    return json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-certificate",
        action="store_true",
        help="write the independently reconstructed deterministic certificate",
    )
    args = parser.parse_args()

    certificate = reconstruct_certificate()
    if args.write_certificate:
        CERTIFICATE_PATH.write_text(canonical_json(certificate), encoding="utf-8")
        print("CERTIFICATE_WRITTEN=" + CERTIFICATE_PATH.relative_to(ROOT).as_posix())
        return

    require(CERTIFICATE_PATH.is_file(), "semilinear-certificate.json is missing")
    stored = json.loads(CERTIFICATE_PATH.read_text(encoding="utf-8"))
    require(stored == certificate, "stored certificate does not equal independent reconstruction")
    verify_result_file()
    verify_manifest()

    print("CODEX_TASK=C_30_06C")
    print("EXACT_ARITHMETIC_ONLY=true")
    print("SOURCE_DERIVED_DIAGONAL_LIFTS_VERIFIED=true")
    print("MODULAR_GROUP_ORDER=24")
    print("ENDPOINT_PROJECTIVE_GROUP_ORDER=24")
    print("THETA_ALL24_VERIFIED=true")
    print("V4_SIGN_DECK_INTERSECTION_VERIFIED=true")
    print("C_SIGMA_COCYCLE_VERIFIED=true")
    print("SEMILINEAR_ALL24_VERIFIED=true")
    print("FAILED_ELEMENT_COUNT=0")
    print("CHECKER_PASS=true")


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, KeyError, ValueError, json.JSONDecodeError) as exc:
        print(f"CHECKER_PASS=false: {exc}", file=sys.stderr)
        raise SystemExit(1)
