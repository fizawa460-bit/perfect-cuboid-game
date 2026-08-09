#!/usr/bin/env python3
"""Deterministic Stage14-4aj Shimada-lattice interface audit.

This audit checks the exact algebraic/lattice identities that can be locked before
Shimada's large S0S3/Borcherds data files are ingested.  It intentionally does
not claim that the remaining M-degree-4 root locus is empty or nonempty.
"""

from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "stages/stage14/data/14-4/shimada_lattice_interface_audit.json"


def rank_q(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = a[r][c]
        a[r] = [x / z for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                z = a[i][c]
                a[i] = [x - z * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


# Monomial order r^i s^j, 0<=i,j<=2.
MONS = [(i, j) for i in range(3) for j in range(3)]


def vec(terms):
    d = {m: Fraction(c) for m, c in terms.items()}
    return [d.get(m, Fraction(0)) for m in MONS]


# Complete bidegree-(2,2) corner-vanishing anticanonical basis.
V = [
    vec({(2, 0): 1, (0, 0): -1}),
    vec({(0, 2): 1, (0, 0): -1}),
    vec({(2, 2): 1, (0, 0): -1}),
    vec({(1, 2): 1, (1, 0): -1}),
    vec({(2, 1): 1, (0, 1): -1}),
]
CORNERS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
EVAL = []
for r, s in CORNERS:
    EVAL.append([Fraction(r) ** i * Fraction(s) ** j for i, j in MONS])

assert rank_q(EVAL) == 4
assert rank_q(V) == 5
for basis_vector in V:
    for row in EVAL:
        assert sum(x * y for x, y in zip(basis_vector, row)) == 0

# Deck involution on E_t: y^2=x(x-1)(x+t^2).
# delta(x,y)=(-t^2/x,-t^2*y/x^2).  We test exact rational identities
# without choosing square roots for y.
for t in [Fraction(1, 2), Fraction(2, 3), Fraction(3, 5), Fraction(5, 4)]:
    for x in [Fraction(2), Fraction(3, 2), Fraction(-2), Fraction(5, 3)]:
        y2 = x * (x - 1) * (x + t * t)
        xp = -(t * t) / x
        yp2 = (t ** 4) * y2 / (x ** 4)
        assert yp2 == xp * (xp - 1) * (xp + t * t)

        # x'/y' = x/y, so q=x/(s0*y) is fixed.
        ratio_multiplier = xp / (-(t * t) / (x * x))
        assert ratio_multiplier == x

        # delta^2=id.
        xpp = -(t * t) / xp
        assert xpp == x
        y_coefficient = (-t * t / (xp * xp)) * (-t * t / (x * x))
        assert y_coefficient == 1

# Split-root complement identities.
M2, MC, C2 = 8, 4, -2
complement_square = M2 - 2 * MC + C2
C_dot_complement = MC - C2
assert complement_square == -2
assert C_dot_complement == 6

# Intrinsic Stage14 polarization formula
# M=2 f_r+2 f_s-sum e_j,
# with f_r^2=f_s^2=0, f_r.f_s=2, e_j^2=-2, and all indicated
# ruling/corner cross terms zero.
M_intrinsic_square = 8 * 2 + 4 * (-2)
M_dot_fr = 2 * 2
M_dot_fs = 2 * 2
assert M_intrinsic_square == 8
assert M_dot_fr == M_dot_fs == 4

REPORT = {
    "stage": "14-4aj",
    "status": "SHIMADA_LATTICE_INTERFACE_LOCKED",
    "anticanonical_system": {
        "projective_dimension": 4,
        "basis": [
            "r^2-1",
            "s^2-1",
            "r^2*s^2-1",
            "r*(s^2-1)",
            "s*(r^2-1)",
        ],
        "corner_conditions_rank": 4,
        "basis_rank": 5,
        "basis_spans_corner_vanishing_bidegree_22_system": True,
    },
    "deck_involution": {
        "elliptic_model": "y^2=x(x-1)(x+t^2)",
        "physical_second_half_angle": "q=x/(s*y)",
        "formula": "delta(x,y)=(-t^2/x,-t^2*y/x^2)",
        "group_law": "delta(P)=(0,0)-P = tau_(0,0) o [-1]",
        "preserves_curve": True,
        "fixes_q": True,
        "is_involution": True,
        "shimada_search_space": (
            "three nonzero order-2 MW labels; deck=tau_T o iotasigmaz"
        ),
    },
    "split_root_equivalence": {
        "necessary_lattice_conditions": [
            "C^2=-2",
            "M.C=4",
            "C+delta(C)=M",
        ],
        "complement_square": complement_square,
        "C_dot_deltaC": C_dot_complement,
        "note": (
            "effectivity, irreducible image, Q-descent, and physical-open tests "
            "remain mandatory"
        ),
    },
    "physical_M_fingerprint": {
        "intrinsic_formula": "M=2*f_r+2*f_s-e_++-e_+--e_-+-e_--",
        "M_square": M_intrinsic_square,
        "M_dot_f_r": M_dot_fr,
        "M_dot_f_s": M_dot_fs,
        "M_null_boundary_roots": 8,
        "r_boundary_fibers": ["0", "infinity"],
        "s_boundary_sections": (
            "four order-4 torsion sections halving the visible (1,0) two-torsion"
        ),
        "candidate_order2_label_pairs": 6,
    },
    "full_shimada_enumeration_executed": False,
    "physical_Q_rational_M4_bisection_existence_resolved": False,
    "next": (
        "ingest S0S3.txt and Borcherds.txt; identify "
        "(f_s,T_deck,T_boundary), compute M vector, enumerate effective roots"
    ),
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(REPORT, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(REPORT, indent=2, sort_keys=True))
