#!/usr/bin/env python3
"""Dependency-free exact verifier for the Stage33-12 batch-3 class-2 go/no-go."""
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def p_add(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def p_neg(a):
    return trim([-x for x in a])


def p_sub(a, b):
    return p_add(a, p_neg(b))


def p_scale(a, c):
    return trim([c * x for x in a])


def p_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def p_pow(a, n):
    out = (1,)
    for _ in range(n):
        out = p_mul(out, a)
    return out


def xtrim(a):
    a = [trim(c) for c in a]
    while len(a) > 1 and a[-1] == (0,):
        a.pop()
    return tuple(a)


def x_add(a, b):
    n = max(len(a), len(b))
    zero = (0,)
    return xtrim([p_add(a[i] if i < len(a) else zero, b[i] if i < len(b) else zero) for i in range(n)])


def x_neg(a):
    return xtrim([p_neg(c) for c in a])


def x_sub(a, b):
    return x_add(a, x_neg(b))


def x_mul(a, b):
    zero = (0,)
    out = [zero for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = p_add(out[i + j], p_mul(x, y))
    return xtrim(out)


def x_const(a):
    return (trim(a),)


def x_scale(a, c):
    return xtrim([p_scale(v, c) for v in a])


c = load("j2-class2-batch3-go-no-go.json")
assert c["schema"] == "STAGE33_12_J2_CLASS2_BATCH3_GO_NO_GO_V1"
assert c["status"] == "CLASS2_GO_NO_GO_FAILED_PENDING_BATCH4_CLASS3_ESCALATION_AUDIT"
assert c["class2_budget_batch"] == 3
assert c["class2_budget_total"] == 4

batch2 = load("j2-named-cv-special-brauer-pairing-orbit.json")
assert batch2["schema"] == "STAGE33_12_J2_NAMED_CV_SPECIAL_BRAUER_PAIRING_ORBIT_V1"
assert batch2["weil_pairing_evaluation"]["selected_orbit_invariant"] == [1, 0]
assert batch2["firewalls"]["pairing_orbit_bits_equal_marked_brauer_bits"] is False

edge = load("j2-brauer-to-sha-leray-edge-interface.json")
assert edge["j2_brauer_to_sha_leray_edge_materialized"] is False
assert edge["exact_conclusion"]["brauer_to_sha_edge_target_fixed"] is True

pic2 = load("full-surface-pic2-kummer-target.json")
assert pic2["exact_information_boundary"]["kummer_extension_class_missing"] is True
assert pic2["exact_information_boundary"]["integral_bockstein_target_quotient_materialized"] is False

kernels = load("j2-brauer-kernel-lattice-fingerprints.json")
assert kernels["kernel_lattices"]["0,1"]["minimum_norm"] == 4
assert kernels["kernel_lattices"]["1,0"]["minimum_norm"] == 8
assert kernels["kernel_lattices"]["1,1"]["minimum_norm"] == 12

# t-polynomials, constant coefficient first.
t2 = (0, 0, 1)
t4 = (0, 0, 0, 0, 1)
one = (1,)
r = (1, 0, -2, 0, 1)                       # (t^2-1)^2
q = (1, 0, -6, 0, 1)                       # t^4-6t^2+1
four_t2 = (0, 0, 4)
H = (1, 0, -4, 0, 1)
S = p_add(r, q)
assert p_sub(r, q) == four_t2

# Discriminant factor and geometric elliptic-lattice arithmetic.
Delta = p_scale(p_mul(p_pow(t2, 2), p_mul(p_pow(r, 2), p_pow(q, 2))), 256)
assert Delta == p_scale(p_mul((0, 0, 0, 0, 1), p_mul(p_pow(r, 2), p_pow(q, 2))), 256)
root_disc = (4 ** 4) * (2 ** 4)
assert root_disc == 4096
rho = 2 + 4 * (4 - 1) + 4 * (2 - 1) + 2
assert rho == 20
ns_abs_disc = Fraction(root_disc, 1) * Fraction(1, 2) / (8 ** 2)
assert ns_abs_disc == 32
assert c["kc_elliptic_lattice_crosscheck"]["NS_abs_discriminant_from_elliptic_data"] == 32
assert c["kc_elliptic_lattice_crosscheck"]["matches_semantic_PicK_abs_discriminant"] is True

# Exact Hermite determinant identity for all three choices of the middle root.
# If root_k is the selected root, a2=root_k-S/3 and
# M has determinant (root_k-X)*(A-(2X+root_k-S)^2).
zero = (0,)
roots = [zero, r, q]
As = [p_scale(t4, 16), p_pow(q, 2), p_pow(r, 2)]
X = ((0,), (1,))
XmR = (p_neg(r), (1,))
XmQ = (p_neg(q), (1,))
target = x_scale(x_mul(X, x_mul(XmR, XmQ)), 4)
for root, A in zip(roots, As):
    root_minus_X = (root, (-1,))
    B = (p_sub(root, S), (2,))
    det = x_mul(root_minus_X, x_sub(x_const(A), x_mul(B, B)))
    assert det == target

# Middle-component double-cover squareclasses.
n0 = p_scale(H, -2)                         # 3*a2 for C0
nr = p_pow((1, 0, 1), 2)                    # 3*a2 for Cr
nq = (1, 0, -10, 0, 1)                      # 3*a2 for Cq
assert p_sub(p_pow(n0, 2), As[0]) == p_scale(p_mul(r, q), 4)
assert p_sub(p_pow(nr, 2), As[1]) == p_scale(p_mul(t2, r), 16)
assert p_sub(p_pow(nq, 2), As[2]) == p_scale(p_mul(t2, q), -16)

# Cr-middle canonical inverse forced by the [q,1,q] squareclasses.
# w^2=q(v^4+1)+2(t^2+1)^2*v^2 has the rational point
# v=1, w=2(t^2-1).
tplus1_sq = p_pow((1, 0, 1), 2)
rhs_v1 = p_add(p_scale(q, 2), p_scale(tplus1_sq, 2))
assert rhs_v1 == p_scale(r, 4)

hermite = c["canonical_even_hermite_inverse_test"]
assert hermite["required_component_fingerprint"] == ["q", "1", "q"]
assert len(hermite["cases"]) == 3
assert hermite["all_three_canonical_even_inverses_have_a_Qbar_t_point"] is True
assert hermite["all_three_canonical_even_inverses_are_zero_in_Sha"] is True

scope = c["batch2_scope_correction"]
assert scope["named_branch_admissible_cover_orbit_selected"] is True
assert scope["selected_orbit"] == [1, 0]
for key in [
    "K3_mu2_special_brauer_lift_materialized",
    "PGL2_splitting_modules_materialized",
    "relative_picard_local_trivializations_materialized",
    "relative_picard_overlap_cocycle_materialized",
    "brauer_to_sha_leray_edge_materialized",
]:
    assert scope[key] is False

breadth = c["post_orbit_breadth_audit"]
assert breadth["exhaustive_view_audit"] is True
assert breadth["blind_rediscovery"] is True
assert breadth["live_class2_routes_after_audit"] == 0
assert breadth["mathematical_impossibility_claimed"] is False

verdict = c["class2_go_no_go"]
assert verdict["verdict"] == "NO_GO_AFTER_BATCH3"
assert verdict["class3_promoted_now"] is False
assert verdict["class3_escalation_pending_batch4"] is True

fw = c["firewalls"]
for key in [
    "j2_marked_brauer_coordinate_selected",
    "j2_twisted_transcendental_kernel_identified",
    "j2_explicit_torsor_surface_materialized",
    "j2_torsor_picard_lattice_materialized",
    "stage33_12_closed_exact",
    "stage33_13_released",
    "heavy_actions_authorized",
    "theorem_credit",
    "receiver_credit",
    "endpoint_credit",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert fw[key] is False

print(json.dumps({
    "success": True,
    "class2_batch": "3/4",
    "named_branch_orbit": [1, 0],
    "canonical_even_hermite_inverses_tested": 3,
    "canonical_even_hermite_all_sha_trivial": True,
    "kc_ns_abs_discriminant_crosscheck": 32,
    "class2_go_no_go": "NO_GO_AFTER_BATCH3",
    "class3_escalation_pending_batch4": True,
    "next_exact_leaf": c["next_exact_leaf"],
}, indent=2, sort_keys=True))
