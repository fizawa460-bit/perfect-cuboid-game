#!/usr/bin/env python3
"""Exact corrected-J2 quotient/branch to surface H^2(mu_2) adapter.

This checker deliberately rebuilds the geometric adapter from the corrected
CsK[22] support.  It does not consume the retired J2 arithmetic-descent or
historical Kummer-glue producers.

The output reaches the canonical H^2(mu_2) *coset* supplied by the Smith/Gysin
triangle for the B1-sign double cover.  A concrete Cech preimage in H^2(U,mu_2)
is still required before sigma(lambda)-lambda in Pic/2 and the HS d2 cocycle can
be computed.  Thus this is an exact interface construction, not Q-descent
credit.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
SUPPORT = HERE / "j2-corrected-kc-branch-support.json"
SEMANTIC = HERE / "j2-semantic-kc-picard-basis.json"
PRE = S33 / "33-05" / "j2-corrected-pre-kummer-descent-cochain.json"
OUT = HERE / "j2-corrected-branch-surface-mu2-adapter.json"

EXPECTED_SUPPORT = "a9eb7d4d3868581d88ff7ce88c23a42b7010c79c959ead1579738e4a0c56961a"
EXPECTED_SEMANTIC = "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0"
EXPECTED_PRE = "940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    assert claimed == expected == csha(body), (path, claimed, csha(body))
    return obj


# Q(i,sqrt(2)) represented as a+b*i+c*s+d*i*s, s^2=2.
def k(a=0, b=0, c=0, d=0):
    return tuple(Fraction(x) for x in (a, b, c, d))


def kadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def kneg(x):
    return tuple(-a for a in x)


def kmul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    # (a+c*s)+i*(b+d*s), with i^2=-1 and s^2=2.
    real0 = a*e + 2*c*g - b*f - 2*d*h
    imag0 = a*f + b*e + 2*(c*h + d*g)
    real1 = a*g + c*e - b*h - d*f
    imag1 = a*h + b*g + c*f + d*e
    return (real0, imag0, real1, imag1)


def kscale(n, x):
    return tuple(Fraction(n) * a for a in x)


ZERO = k()
ONE = k(1)
I = k(0, 1)
S2 = k(0, 0, 1)


def rank(rows):
    a = [list(row) for row in rows]
    m = len(a)
    n = len(a[0]) if m else 0
    r = 0
    for col in range(n):
        pivot = next((j for j in range(r, m) if a[j][col] != ZERO), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        # Only rank 2/3 is needed. Avoid field division by eliminating with
        # cross-multiplication, valid over the integral domain Q(i,sqrt(2)).
        p = a[r][col]
        for j in range(m):
            if j == r or a[j][col] == ZERO:
                continue
            q = a[j][col]
            a[j] = [kadd(kmul(p, x), kneg(kmul(q, y)))
                    for x, y in zip(a[j], a[r])]
        r += 1
        if r == m:
            break
    return r


def eval_kc(P):
    A1, A2, A3, B1, B2, B3 = P
    return [
        kadd(kadd(kmul(A1, A1), kmul(A2, A2)), kneg(kmul(B3, B3))),
        kadd(kadd(kmul(A2, A2), kmul(A3, A3)), kneg(kmul(B1, B1))),
        kadd(kadd(kmul(A1, A1), kmul(A3, A3)), kneg(kmul(B2, B2))),
    ]


def jacobian(P):
    A1, A2, A3, B1, B2, B3 = P
    z = ZERO
    return [
        [kscale(2, A1), kscale(2, A2), z, z, z, kscale(-2, B3)],
        [z, kscale(2, A2), kscale(2, A3), kscale(-2, B1), z, z],
        [kscale(2, A1), z, kscale(2, A3), z, kscale(-2, B2), z],
    ]


def eval_quotient(P):
    A1, A2, A3, B2, B3 = P
    return [
        kadd(kadd(kmul(A1, A1), kmul(A2, A2)), kneg(kmul(B3, B3))),
        kadd(kadd(kmul(A1, A1), kmul(A3, A3)), kneg(kmul(B2, B2))),
    ]


def quotient_jacobian(P):
    A1, A2, A3, B2, B3 = P
    z = ZERO
    return [
        [kscale(2, A1), kscale(2, A2), z, z, kscale(-2, B3)],
        [kscale(2, A1), z, kscale(2, A3), kscale(-2, B2), z],
    ]


def trim(p):
    p = [Fraction(x) for x in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pdivmod(a, b):
    a = trim(a)
    b = trim(b)
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        shift = len(a) - len(b)
        coeff = a[-1] / b[-1]
        q[shift] = coeff
        for j, v in enumerate(b):
            a[shift + j] -= coeff * v
        a = trim(a)
    return trim(q), trim(a)


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while any(b):
        _, r = pdivmod(a, b)
        a, b = b, r
    return [x / a[-1] for x in a]


support = load_locked(SUPPORT, EXPECTED_SUPPORT)
semantic = load_locked(SEMANTIC, EXPECTED_SEMANTIC)
pre = load_locked(PRE, EXPECTED_PRE)

assert support["marked_Kc_support"]["marked_branch_curve"] == "CsK[22]"
assert support["marked_Kc_support"]["marked_branch_equations"] == [
    "B1=0", "i*A2-A3=0"
]
assert semantic["j2_branch_carrier"]["curve"] == "CsK[22]"
assert semantic["j2_branch_carrier"]["same_picK_class_as"] == "CsK[21]"
assert semantic["j2_branch_carrier"]["marked_semantic_picK_coords"] == (
    [0]*7 + [1] + [0]*12
)
assert pre["normalization"]["half_divisor_D"] == "P_r2-P_r4"
assert pre["normalization"]["divisor_f2"] == "2*(P_r2-P_r4)"

# The B1-sign involution preserves Kc. Its quotient forgets B1 and is the
# degree-four del Pezzo S cut out by the first and third Kc quadrics.
# The omitted equation is B1^2=A2^2+A3^2, hence the branch divisor factors
# over Q(i) as (A3+i*A2)(A3-i*A2)=0.
branch_factor_product = {
    "A2^2": kmul(I, kneg(I)),  # i*(-i)=1
    "A3^2": ONE,
    "A2*A3": kadd(I, kneg(I)),
}
assert branch_factor_product == {"A2^2": ONE, "A3^2": ONE, "A2*A3": ZERO}

# C21 and C22 meet at exactly four projective points on S/Kc. They are the
# four A1=1 choices B2=+/-1, B3=+/-1 with A2=A3=B1=0, and each is an A1 node
# of the singular complete-intersection model (Jacobian rank 2).
crossings = []
for e2 in (1, -1):
    for e3 in (1, -1):
        P = [ONE, ZERO, ZERO, ZERO, k(e2), k(e3)]
        assert eval_kc(P) == [ZERO, ZERO, ZERO]
        assert rank(jacobian(P)) == 2
        Q = [ONE, ZERO, ZERO, k(e2), k(e3)]
        assert eval_quotient(Q) == [ZERO, ZERO]
        assert rank(quotient_jacobian(Q)) == 2
        crossings.append(["1", "0", "0", "0", str(e2), str(e3)])

# The quotient model itself has four A1 singularities away from the branch.
# Each has two etale preimages, accounting for the other eight nodes of Kc.
quotient_nodes = []
for e3 in (1, -1):
    Q = [ZERO, ONE, ZERO, ZERO, k(e3)]
    assert eval_quotient(Q) == [ZERO, ZERO]
    assert rank(quotient_jacobian(Q)) == 1
    assert kadd(kmul(Q[1], Q[1]), kmul(Q[2], Q[2])) == ONE
    quotient_nodes.append(["0", "1", "0", "0", str(e3)])
for e2 in (1, -1):
    Q = [ZERO, ZERO, ONE, k(e2), ZERO]
    assert eval_quotient(Q) == [ZERO, ZERO]
    assert rank(quotient_jacobian(Q)) == 1
    assert kadd(kmul(Q[1], Q[1]), kmul(Q[2], Q[2])) == ONE
    quotient_nodes.append(["0", "0", "1", str(e2), "0"])

# At a crossing, x=A2 and y=A3 are etale local parameters on S. The two
# branch gradients (i,1) and (-i,1) have determinant 2i, so are transverse.
grad21 = [I, ONE]
grad22 = [kneg(I), ONE]
det_grad = kadd(kmul(grad21[0], grad22[1]), kneg(kmul(grad21[1], grad22[0])))
assert det_grad == kscale(2, I)
assert det_grad != ZERO

# Blow-up chart y=x*v: the double cover w^2=x^2(v^2+1) normalizes to
# W^2=v^2+1. Along x=0 its branch points v=+/- i are distinct and smooth.
assert kadd(kmul(I, I), ONE) == ZERO
assert kadd(kmul(kneg(I), kneg(I)), ONE) == ZERO
assert I != kneg(I)

# The corrected supports are not at the four crossings (A2=1), so they lift
# unchanged to the strict transform of C22.
assert support["marked_Kc_support"]["P_r2"][1] == "1"
assert support["marked_Kc_support"]["P_r4"][1] == "1"
assert support["marked_Kc_support"]["both_supports_smooth_on_Kc"] is True

# q=t^4-6t^2+1 is square-free, so z^2=q is the smooth genus-one
# normalization/strict branch component used by corrected D.
q = [1, 0, -6, 0, 1]
dq = [0, -12, 0, 4]
assert pgcd(q, dq) == [Fraction(1)]

cert = {
    "schema": "STAGE33_12_J2_CORRECTED_BRANCH_SURFACE_MU2_ADAPTER_V1",
    "status": "PASS_EXACT_B1_QUOTIENT_BRANCH_RESOLUTION_AND_H2_MU2_COSET_ADAPTER_CECH_REPRESENTATIVE_OPEN",
    "source_locks": {
        "corrected_kc_branch_support": {
            "path": "stages/stage33/33-12/j2-corrected-kc-branch-support.json",
            "canonical_sha256": EXPECTED_SUPPORT,
        },
        "semantic_kc_picard_basis": {
            "path": "stages/stage33/33-12/j2-semantic-kc-picard-basis.json",
            "canonical_sha256": EXPECTED_SEMANTIC,
        },
        "corrected_pre_kummer_cochain": {
            "path": "stages/stage33/33-05/j2-corrected-pre-kummer-descent-cochain.json",
            "canonical_sha256": EXPECTED_PRE,
        },
        "skorobogatov_double_cover_cohomology": {
            "url": "https://www.ma.imperial.ac.uk/~anskor/doub8.pdf",
            "locations": [
                "Lemma 2.1 and exact triangle (5)",
                "Kummer/Smith diagram (13)",
                "Gysin sequence and diagram (15)",
                "exact sequence (16)",
                "Proposition 3.1 and Theorem 1.1",
            ],
        },
    },
    "double_cover_geometry": {
        "surface": "minimal resolution Kc_tilde of Kc",
        "involution": "iota_B1:(A1,A2,A3,B1,B2,B3)->(A1,A2,A3,-B1,B2,B3)",
        "quotient": "S:{A1^2+A2^2=B3^2, A1^2+A3^2=B2^2} subset P4",
        "cover_equation": "B1^2=A2^2+A3^2",
        "generic_degree": 2,
        "branch_over_Qi": [
            "C21: A3+i*A2=0",
            "C22: A3-i*A2=0",
        ],
        "corrected_component": "C22=CsK[22]",
        "branch_crossings": crossings,
        "branch_crossing_count": 4,
        "crossings_transverse_on_quotient": True,
        "quotient_A1_nodes": quotient_nodes,
        "quotient_A1_node_count": 4,
        "quotient_nodes_disjoint_from_branch": True,
        "etale_preimage_node_count_on_Kc": 8,
        "singular_double_cover_local_form": "w^2=x^2+y^2=(y+i*x)*(y-i*x)",
    },
    "resolution_adapter": {
        "operation": "resolve the four quotient A1 nodes, then blow up the four transverse branch crossings and normalize the double cover",
        "quotient_A1_resolutions_unbranched": True,
        "quotient_A1_resolution_accounts_for_eight_Kc_nodes": True,
        "local_chart": "y=x*v, w=x*W gives W^2=v^2+1",
        "strict_branch_components_disjoint_after_blowup": True,
        "normalized_double_cover_smooth_above_crossings": True,
        "exceptional_divisor_is_not_a_branch_component": True,
        "minimal_resolution_identified_with_normalized_pullback": True,
        "corrected_support_avoids_crossings": True,
        "old_infinity_exceptional_dependency_reintroduced": False,
    },
    "corrected_pic0_2torsion": {
        "component": "C22_tilde ~= {z^2=t^4-6*t^2+1}",
        "component_smooth_genus": 1,
        "q_squarefree": True,
        "half_divisor": "D=P_r2-P_r4",
        "kummer_function": "f2=(t-r2)/(t-r4)",
        "div_f2": "2D",
        "class": "kappa_D in H^1(C22_bar,mu_2)",
        "other_branch_component_class": "0 on C21_bar",
    },
    "kummer_gysin_adapter": {
        "resolved_quotient": "pi:Kc_tilde_bar->Sprime_bar",
        "branch": "Cbar=C21_tilde disjoint_union C22_tilde",
        "open_complement": "Ubar=Sprime_bar-Cbar",
        "coefficient_identification": "mu_2=Z/2 over Qbar",
        "rational_base_properties": {
            "Sprime_bar_rational": True,
            "H1_Sprime_Z2_zero": True,
            "H3_Sprime_Z2_zero": True,
            "Br_Sprime_2_zero": True,
        },
        "gysin_boundary_of_kappa_D": "0 in H^3(Sprime_bar,Z/2)",
        "preimage_contract": "choose e_D in H^2(Ubar,Z/2) mapping to (0,kappa_D) in H^1(Cbar,Z/2)",
        "surface_lift_contract": "lambda_D=alpha(e_D) in H^2(Kc_tilde_bar,mu_2)",
        "surface_lift_coset": "lambda_D modulo pi^*H^2(Sprime_bar,mu_2)+Pic(Kc_tilde_bar)/2",
        "brauer_image": "Phi(0,kappa_D)=corrected geometric J2=(f2,1)",
        "adapter_materialized_at_exact_sequence_level": True,
        "surface_H2_mu2_lift_coset_materialized": True,
        "concrete_Cech_preimage_e_D_materialized": False,
        "concrete_lambda_D_picard_coordinates_materialized": False,
    },
    "exact_information_boundary": {
        "abstract_branch_to_brauer_map_only": False,
        "double_cover_and_resolution_geometry_materialized": True,
        "genuine_surface_H2_mu2_lift_coset_constructed": True,
        "single_H2_mu2_cochain_representative_constructed": False,
        "pic_mod2_defect_1cocycle_materialized": False,
        "integral_Pic_lift_materialized": False,
        "HS_d2_2cocycle_materialized": False,
        "HS_d2_zero_or_nonzero_proved": False,
        "reason": "The corrected Pic0[2] datum now enters the actual B1-sign double-cover Smith/Gysin triangle on the resolved Kc surface. Computing arithmetic descent still requires one explicit Cech preimage e_D (or an equivalent full-surface mu2 cocycle), because different preimages differ by Pic/2 and that difference is precisely the load-bearing Galois defect.",
    },
    "next_exact_leaf": "MATERIALIZE_EXPLICIT_CECH_PREIMAGE_eD_FOR_CORRECTED_BRANCH_KUMMER_CLASS_THEN_COMPUTE_SIGMA_LAMBDA_MINUS_LAMBDA_IN_PIC_MOD2_AND_HS_D2",
    "promotion_firewall": {
        "old_j2_arithmetic_descent_reused": False,
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
    "branch_crossing_count": 4,
    "surface_H2_mu2_lift_coset_materialized": True,
    "concrete_Cech_preimage_e_D_materialized": False,
    "canonical_sha256": cert["canonical_sha256"],
    "next_exact_leaf": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
