#!/usr/bin/env python3
"""Exact structural pre-presentation certificate for Stage33-05.

This does NOT materialize the Creutz--Viray x-alpha matrix or Brauer symbols.
It certifies the finite dimensions and matrix target shape forced by the
specific K_c ruled model and the source formulas.
"""
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent

t, s = sp.symbols("t s")
i = sp.I
sqrt2 = sp.sqrt(2)

A1 = 1 - t**2
A2 = 1 - s**2
X = t * A2
Y = s * A1
F = sp.expand(X**2 + Y**2)
Gplus = sp.expand(X + i * Y)
Gminus = sp.expand(X - i * Y)

# Relative to the first ruling W=P1_t, each branch component is quadratic in s.
# Their discriminants agree up to the constant square -1 and define the same
# quadratic function-field extension K(sqrt(q))/K.
q = sp.expand(t**4 - 6*t**2 + 1)
disc_plus = sp.factor(sp.discriminant(Gplus, s))
disc_minus = sp.factor(sp.discriminant(Gminus, s))
assert sp.simplify(disc_plus + q) == 0
assert sp.simplify(disc_minus + q) == 0

roots = [
    1 + sqrt2,
    -(1 + sqrt2),
    sqrt2 - 1,
    -(sqrt2 - 1),
]
assert sp.expand(sp.prod(t - r for r in roots) - q) == 0
assert len({sp.srepr(sp.simplify(r)) for r in roots}) == 4
for r in roots:
    assert sp.simplify(sp.diff(q, t).subs(t, r)) != 0

# q is squarefree and non-square in kbar(t): four distinct simple zeros.
assert sp.gcd(q, sp.diff(q, t)) == 1

# Generic double-cover equation as a quartic in s. Its leading coefficient is
# t^2, so after y=w/t the hyperelliptic constant c may be chosen as 1.
poly_F_s = sp.Poly(F, s)
assert poly_F_s.degree() == 4
assert sp.expand(poly_F_s.LC() - t**2) == 0
c_square = True

# Dual graph: two normalized branch components joined by eight nodal edges.
# Over F2 its cycle space has dimension 8-2+1=7.  The explicit basis is
# e_j+e_8 (j=1,...,7).
def rank_mod2(rows):
    a = [[x & 1 for x in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((u for u in range(r, m) if a[u][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        for u in range(m):
            if u != r and a[u][c]:
                a[u] = [x ^ y for x, y in zip(a[u], a[r])]
        r += 1
        if r == m:
            break
    return r

incidence = [[1] * 8, [1] * 8]
incidence_rank = rank_mod2(incidence)
assert incidence_rank == 1
cycle_basis = []
for j in range(7):
    v = [0] * 8
    v[j] = 1
    v[7] = 1
    cycle_basis.append(v)
assert rank_mod2(cycle_basis) == 7
for v in cycle_basis:
    assert all(sum(incidence[row][k] * v[k] for k in range(8)) % 2 == 0 for row in range(2))
b1 = 8 - incidence_rank
assert b1 == 7

# Normalization B=B+ disjoint_union B-.  Each (2,2) component has genus 1.
component_genera = [1, 1]
h0_B = 2
# Creutz--Viray convention for a disjoint union: g(B)=sum g_i + 1 - h0(B).
g_B = sum(component_genera) + 1 - h0_B
assert g_B == 1
jac2_dim = 2 * sum(component_genera)
assert jac2_dim == 4

# The two component function fields over K=kbar(t) are the same quadratic
# extension K(sqrt(q)); hence L=Fq x Fq.  For a non-square q, the kernel of
# K*/K*2 -> Fq*/Fq*2 is exactly <q>, dimension 1.
k_square_kernel_dim = 1

# Creutz--Viray define e(b/w) as the SUM of ramification indices over all
# normalization points above a singular point b.  Therefore the special set
# in their dimension formula contains TWO disjoint kinds of ruling values:
#
# (a) four smooth ramification fibers q(t)=0, where each branch component has
#     one point of ramification index 2;
# (b) four nodal fibers t=0,1,-1,infinity.  At each node the two normalization
#     branches are individually unramified (index 1), but e(b/w)=1+1=2.
#
# These eight fibers are pairwise distinct because q(0)=1 and q(+-1)=-4,
# and q has degree four so infinity is not a root.
ramification_fiber_count = 4
nodal_fiber_values = ["0", "1", "-1", "infinity"]
nodal_fiber_count = len(nodal_fiber_values)
assert sp.expand(q.subs(t, 0) - 1) == 0
assert sp.expand(q.subs(t, 1) + 4) == 0
assert sp.expand(q.subs(t, -1) + 4) == 0
special_even_ramification_fibers = ramification_fiber_count + nodal_fiber_count
assert special_even_ramification_fibers == 8

# Source dimension count (preprint proof of Theorem 10.1 / final §6):
# because c is square, ell_c adds no extra raw L*/L*2 dimension.
raw_generator_subspace_dim = -1 + 2 * g_B + 2 * h0_B + b1
assert raw_generator_subspace_dim == 12
kernel_to_K_times_squares_dim = (
    0  # 2*g(W), W=P1
    + special_even_ramification_fibers
    - k_square_kernel_dim
)
assert kernel_to_K_times_squares_dim == 7
LE_dim = raw_generator_subspace_dim - kernel_to_K_times_squares_dim
assert LE_dim == 5

# S=P1xP1 is rational, so Creutz--Viray gives L_{c,E}=L_E.
LcE_dim = LE_dim

# For a (4,4) double cover of P1xP1 with rank NS=20, the same source gives
# dim Br[2]=22-rank(NS)=2.  Therefore im(x-alpha) has exact dimension 3.
NS_rank = 20
Br2_dim = 22 - NS_rank
assert Br2_dim == 2
xalpha_image_dim = LcE_dim - Br2_dim
assert xalpha_image_dim == 3

# Explicit geometric Jac(B)[2] function skeleton: on z^2=q(t), ratios of
# t-r_i have divisor 2(P_i-P_j).  These are not yet the complete LcE basis.
jac_function_skeleton = [
    f"(t-({sp.sstr(roots[0])}))/(t-({sp.sstr(roots[1])}))",
    f"(t-({sp.sstr(roots[0])}))/(t-({sp.sstr(roots[2])}))",
]

certificate = {
    "schema": "STAGE33_05_CV_DIMENSION_SKELETON_V2_NODE_FIBERS_INCLUDED",
    "ruling_base": "P1_t",
    "branch_component_count": 2,
    "branch_component_genera": component_genera,
    "normalization_h0": h0_B,
    "cv_g_B_convention": g_B,
    "node_count": 8,
    "dual_graph_b1": b1,
    "cycle_basis_F2": cycle_basis,
    "jacobian_2torsion_dimension": jac2_dim,
    "common_quadratic_polynomial": sp.sstr(q),
    "common_quadratic_roots": [sp.sstr(r) for r in roots],
    "K_squareclass_kernel_dimension": k_square_kernel_dim,
    "generic_hyperelliptic_c_square": c_square,
    "smooth_ramification_fiber_count": ramification_fiber_count,
    "nodal_even_e_fibers": nodal_fiber_values,
    "nodal_even_e_fiber_count": nodal_fiber_count,
    "special_all_even_e_fiber_count": special_even_ramification_fibers,
    "raw_generator_subspace_dimension_mod_L_squares": raw_generator_subspace_dim,
    "kernel_to_KtimesL2_dimension": kernel_to_K_times_squares_dim,
    "LE_dimension": LE_dim,
    "LcE_equals_LE_because_base_is_rational": True,
    "LcE_dimension": LcE_dim,
    "NS_rank": NS_rank,
    "geometric_Br2_dimension": Br2_dim,
    "xalpha_image_dimension": xalpha_image_dim,
    "target_relation_matrix_shape": [xalpha_image_dim, LcE_dim],
    "jacobian_2torsion_function_skeleton_per_component": jac_function_skeleton,
    "explicit_LcE_basis_materialized": False,
    "explicit_xalpha_matrix_materialized": False,
    "Q_relevant_surviving_dimension_certified": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
certificate["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "cv-dimension-certificate.json").write_text(
    json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(certificate, indent=2, sort_keys=True))
