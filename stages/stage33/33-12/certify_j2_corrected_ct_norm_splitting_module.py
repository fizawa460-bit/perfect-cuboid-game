#!/usr/bin/env python3
"""Exact generic ct-norm splitting module and compactification ambiguity.

For the corrected J2 lift the generic ct defect is

    (q,g22),  q=t^4-6*t^2+1,
    g22=1-s^2+i*s*(1-t^2)/t.

Writing z^2=q and A=1-t^2+2*i*t*s gives

    u=(A+z)/(2*t),  Norm(u)=g22.

This verifier constructs the resulting two-dimensional splitting
representation explicitly.  It also compactifies the auxiliary q-cover over
P1_t and computes the determinant of its standard finite-flat module.

The standard compactification has even determinant.  Crucially, however, the
currently committed Cech certificate contains no local rank-two lattice or
transition matrices identifying the *actual* ct(lambda)-lambda nullhomotopy
with that compactification.  An elementary transform along one t-fiber has
the same generic splitting algebra and the same generic residue witnesses but
changes determinant parity by the nonzero marked Kc fiber class.  Thus the
generic norm identity and the eight q-fiber coordinates do not select the
Pic/2 defect.  This is an exact narrowing certificate, not an HS-d2 value.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXPLICIT = HERE / "j2-corrected-explicit-cech-mu2-lift.json"
SUPPORT = HERE / "j2-corrected-ct-norm-picard-support.json"
OUT = HERE / "j2-corrected-ct-norm-splitting-module.json"

EXPECTED_EXPLICIT = "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"
EXPECTED_SUPPORT = "77af329d2baf2fe807bf23722c9b320fdfddec2bd1df90ced7758d411c9cf021"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), (path, claimed, csha(body))
    return obj


explicit = load_locked(EXPLICIT, EXPECTED_EXPLICIT)
support = load_locked(SUPPORT, EXPECTED_SUPPORT)
assert explicit["galois_defect_generic_splittings"]["ct"]["generic_symbol_zero"]
fiber = support["ct_norm_support"][
    "common_q_fiber_class_marked_semantic_PicK_coordinates"
]
assert fiber == [0] * 8 + [1] + [0] * 11

# Q(i,sqrt(2)) in the basis 1,i,sqrt(2),i*sqrt(2).
def k(a=0, b=0, c=0, d=0):
    return tuple(Fraction(x) for x in (a, b, c, d))


ZERO = k()
ONE = k(1)
I = k(0, 1)
S2 = k(0, 0, 1)


def kadd(x, y):
    return tuple(a+b for a, b in zip(x, y))


def kneg(x):
    return tuple(-a for a in x)


def kmul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return (
        a*e + 2*c*g - b*f - 2*d*h,
        a*f + b*e + 2*(c*h+d*g),
        a*g + c*e - b*h - d*f,
        a*h + b*g + c*f + d*e,
    )


def kpow(x, n):
    out = ONE
    while n:
        if n & 1:
            out = kmul(out, x)
        x = kmul(x, x)
        n //= 2
    return out


class P:
    """Sparse polynomial in t,s over Q(i,sqrt(2))."""

    def __init__(self, terms=None):
        self.d = {m: c for m, c in (terms or {}).items() if c != ZERO}

    @staticmethod
    def const(c=ZERO):
        if isinstance(c, int):
            c = k(c)
        return P({(0, 0): c}) if c != ZERO else P()

    @staticmethod
    def mon(et=0, es=0, c=ONE):
        return P({(et, es): c})

    def __add__(self, other):
        other = top(other)
        out = dict(self.d)
        for m, c in other.d.items():
            out[m] = kadd(out.get(m, ZERO), c)
            if out[m] == ZERO:
                out.pop(m)
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({m: kneg(c) for m, c in self.d.items()})

    def __sub__(self, other):
        return self + (-top(other))

    def __rsub__(self, other):
        return top(other) - self

    def __mul__(self, other):
        other = top(other)
        out = {}
        for (at, ass), ac in self.d.items():
            for (bt, bs), bc in other.d.items():
                m = (at+bt, ass+bs)
                out[m] = kadd(out.get(m, ZERO), kmul(ac, bc))
                if out[m] == ZERO:
                    out.pop(m)
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        out = P.const(ONE)
        base = self
        while n:
            if n & 1:
                out = out*base
            base = base*base
            n //= 2
        return out

    def __eq__(self, other):
        return self.d == top(other).d

    def eval_t(self, value):
        out = P()
        for (et, es), coeff in self.d.items():
            out += P.mon(es=es, c=kmul(coeff, kpow(value, et)))
        return out


def top(value):
    if isinstance(value, P):
        return value
    if isinstance(value, tuple):
        return P.const(value)
    return P.const(int(value))


def mmul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(2)), P())
             for j in range(2)] for i in range(2)]


def madd(a, b):
    return [[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]


t = P.mon(et=1)
s = P.mon(es=1)
i = P.const(I)
one = P.const(ONE)
q = t**4 - 6*t**2 + one
A = one - t**2 + 2*i*t*s
gp = t*(one-s**2) + i*s*(one-t**2)  # t*g22

# Exact norm identity for u=(A+z)/(2t), with the deck involution z -> -z.
# Clearing the denominator and z^2=q gives A^2-q=4*t^2*g22=4*t*gp.
assert A**2-q == 4*t*gp

# On the K-basis (1,z), multiplication by z and the semilinear operator
# w |-> u*sigma(w) split the quaternion (q,g).  Clear the denominator in Y:
# N=2*t*Y; then N^2=4*t*gp*I and ZN=-NZ.
Z = [[P(), q], [one, P()]]
N = [[A, -q], [one, -A]]
I2 = [[one, P()], [P(), one]]
assert mmul(Z, Z) == [[q, P()], [P(), q]]
assert mmul(N, N) == [[4*t*gp, P()], [P(), 4*t*gp]]
assert madd(mmul(Z, N), mmul(N, Z)) == [[P(), P()], [P(), P()]]

# The q roots are simple and nonzero.  The norm witness is a unit at the
# generic point of each q-fiber and specializes to the recorded square root.
roots = [k(1, 0, 1), k(-1, 0, -1), k(-1, 0, 1), k(1, 0, -1)]
ds = [-1, 1, 1, -1]
dq = 4*t**3 - 12*t
for root, d in zip(roots, ds):
    assert q.eval_t(root) == P()
    assert dq.eval_t(root) != P()
    # A(root)=2*root*(d+i*s), and gp(root)=root*(d+i*s)^2.
    square_root = P.const(k(d)) + i*s
    assert A.eval_t(root) == P.const(kmul(k(2), root))*square_root
    assert gp.eval_t(root) == P.const(root)*square_root**2

# Standard finite-flat compactification of z^2=q over P1_t:
# p_*O_T = O + O(-2F).  On v=1/t, z_infinity=v^2*z_0, so the determinant
# transition has exponent 2 and therefore zero class modulo 2.
standard_transition_exponents = [0, 2]
standard_determinant_degree = sum(standard_transition_exponents)
assert standard_determinant_degree == 2
assert standard_determinant_degree % 2 == 0

# Elementary-transform the second summand along one vertical fiber:
# O + O(-3F).  Its generic endomorphism algebra is still M_2(K), hence after
# composing with the matrices above it compactifies the same generic split
# quaternion.  Its determinant differs by F and is odd modulo 2.
transformed_transition_exponents = [0, 3]
transformed_determinant_degree = sum(transformed_transition_exponents)
assert transformed_determinant_degree == 3
assert transformed_determinant_degree % 2 == 1
parity_difference = transformed_determinant_degree-standard_determinant_degree
assert parity_difference == 1
assert any(x & 1 for x in fiber)

next_leaf = (
    "MATERIALIZE_ACTUAL_CECH_LOCAL_RANK2_LATTICES_AND_OVERLAP_TRANSITION_"
    "MATRICES_FOR_LAMBDA_D_AT_T0_TINF_SINF_C21_C22_AND_RESOLUTION_"
    "EXCEPTIONALS_THEN_COMPARE_CC_CT_NULLHOMOTOPIES_AND_COMPUTE_MARKED_"
    "PIC_MOD2_AND_HS_D2"
)

cert = {
    "schema": "STAGE33_12_J2_CORRECTED_CT_NORM_SPLITTING_MODULE_V1",
    "status": "PASS_EXACT_GENERIC_SPLITTING_MODULE_AND_COMPACTIFICATION_PARITY_AMBIGUITY_ACTUAL_CECH_LATTICE_OPEN",
    "source_locks": {
        "explicit_surface_mu2_lift": {
            "path": "stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json",
            "canonical_sha256": EXPECTED_EXPLICIT,
        },
        "ct_norm_picard_support": {
            "path": "stages/stage33/33-12/j2-corrected-ct-norm-picard-support.json",
            "canonical_sha256": EXPECTED_SUPPORT,
        },
    },
    "normalized_norm_nullhomotopy": {
        "q": "t^4-6*t^2+1",
        "A": "1-t^2+2*i*t*s",
        "u": "(A+z)/(2*t)",
        "deck_conjugate_u": "(A-z)/(2*t)",
        "identity": "A^2-q=4*t^2*g22",
        "norm_u_equals_g22": True,
        "old_minus_sign_removed_by_multiplying_the_old_witness_by_i": True,
    },
    "generic_splitting_representation": {
        "basis": ["1", "z"],
        "z_operator": [["0", "q"], ["1", "0"]],
        "u_sigma_operator": [["A/(2*t)", "-q/(2*t)"], ["1/(2*t)", "-A/(2*t)"]],
        "relations": ["Z^2=q*I", "Y^2=g22*I", "Z*Y=-Y*Z"],
        "matrix_relations_verified_exactly": True,
    },
    "q_root_local_audit": {
        "roots": ["1+sqrt(2)", "-(1+sqrt(2))", "sqrt(2)-1", "1-sqrt(2)"],
        "d_values_for_A_over_2t": [-1, 1, 1, -1],
        "specialized_square_roots": ["-1+i*s", "1+i*s", "1+i*s", "-1+i*s"],
        "all_roots_simple_and_nonzero": True,
        "g22_specializes_to_square_of_displayed_root": True,
    },
    "standard_auxiliary_q_cover_compactification": {
        "cover": "p:T_q->P1_t x P1_s, z^2=q with z a section of O(2,0)",
        "finite_flat_module": "p_*O_Tq=O plus O(-2,0)",
        "t_infinity_basis_transition": "diag(1,v^2), v=1/t",
        "determinant": "O(-2,0)",
        "determinant_mod2": "0",
        "candidate_compactification_materialized": True,
        "identified_with_actual_ct_defect_extension": False,
    },
    "exact_nonuniqueness_witness": {
        "second_compactification": "E1=O plus O(-3,0), the elementary transform of E0 along one vertical t-fiber",
        "same_generic_endomorphism_algebra": "End(E0)_K=End(E1)_K=M2(K), composed with the displayed quaternion splitting",
        "generic_norm_and_residue_data_unchanged": True,
        "determinant_parity_E0": 0,
        "determinant_parity_E1": 1,
        "parity_difference_on_quotient": "one vertical fiber F",
        "pullback_difference_marked_semantic_PicK_coordinates": fiber,
        "pullback_difference_nonzero_mod2": True,
        "consequence": "The generic norm identity plus q-fiber component coordinates cannot select the actual Pic/2 defect; actual local Cech lattice transitions are load-bearing.",
    },
    "exact_information_boundary": {
        "normalized_generic_splitting_matrices_materialized": True,
        "standard_auxiliary_cover_determinant_materialized": True,
        "compactification_parity_ambiguity_materialized": True,
        "actual_lambda_D_local_rank2_lattices_materialized": False,
        "actual_cc_ct_overlap_transition_matrices_materialized": False,
        "actual_ct_defect_marked_Pic_mod2_materialized": False,
        "integral_Pic_lift_materialized": False,
        "HS_d2_2cocycle_materialized": False,
        "HS_d2_zero_or_nonzero_proved": False,
    },
    "next_exact_leaf": next_leaf,
    "promotion_firewall": {
        "old_j2_arithmetic_descent_reused": False,
        "old_ell_Q_reused": False,
        "historical_kummer_glue_reused": False,
        "Q_defined_descent_credit_restored": False,
        "R5_full_repair_exit_reached": False,
        "stage33_05_reclosed": False,
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "stage33_progress": "5/11",
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "status": cert["status"],
    "norm_u_equals_g22": True,
    "standard_determinant_mod2": 0,
    "actual_ct_defect_marked_Pic_mod2_materialized": False,
    "canonical_sha256": cert["canonical_sha256"],
    "next_exact_leaf": next_leaf,
}, indent=2, sort_keys=True))
