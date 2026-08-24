#!/usr/bin/env python3
"""Certify that the proper geometric Brauer group has no odd-primary G_Q invariants.

This is the odd-primary arithmetic-HS repair for Stage33-07.

The audited Stage29 global eigenspace adapter identifies the rank-14 proper
transcendental H^2 representation of the cuboid surface as

    3*V_h16 + V_h32 + 3*V_h8.

The audited finite-field oracle gives exact CM coefficient formulae for h16,
h8, and h32=chi_2*h8.  On H^2(1), for a weight-three newform constituent with
nebentype epsilon, the characteristic polynomial at a good prime p is

    X^2 - (a_p/p) X + epsilon(p),

so

    det(Frob_p - 1) = (p*(1+epsilon(p)) - a_p)/p.

At p=17 and p=41 all three nebentypes are +1.  The full rank-14 determinant
numerators are powers of 2.  Therefore for every odd prime ell, one of these
two good Frobenii has det(Frob-1) an ell-adic unit (use p=41 only for ell=17).
Hence the ell-torsion of the proper geometric Brauer group has no G_Q-fixed
vector.  It follows that the entire odd-primary invariant subgroup is zero.

Consequently, any Q-defined odd-primary class on the physical open whose
boundary residues are purely constant-field characters becomes unramified and
zero after base change to Qbar, hence is algebraic.  Stage33-03 already gives
the complete algebraic open Brauer group and Stage33-07 proves its boundary
map is injective.  Thus the globally liftable odd constant-character boundary
image is exactly rho(BR0B_odd); the odd constant cokernel contributes no new
global Q-defined class.
"""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
ROOT = S33.parent.parent


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


hs = load(HERE / "arithmetic-hs-descent-problem.json")
br0b = load(S33 / "33-03" / "audit-state.json")
br0g = load(S33 / "33-04" / "audit-state.json")
fullinj = load(HERE / "full-br0b-boundary-injection.json")
s08 = load(S33 / "33-08" / "audit-state.json")

assert hs["repair_kernel"] == "R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT"
assert hs["geometric_lift_fiber"]["proper_transcendental_rank"] == 14
assert br0b["unit_status"] == "CLOSED" and br0b["br0b"] == "DISCHARGED"
assert br0g["unit_status"] == "CLOSED" and br0g["br0g"] == "DISCHARGED"
assert fullinj["full_br0b_boundary_map_injective"] is True
assert s08["theorem_scope_regression"]["geometric_global_residue_lift_over_qbar_repaired"] is True

# Exact CM coefficient formulas are copied from the audited Stage29-02e
# finite-field oracle, whose global identification is independently supplied
# by global-k3-eigenspace-adapter.md.  We recompute the two coefficients here
# rather than importing a Python module with an expensive point-count main.
def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return -1 if r == p - 1 else r


def chi2(p):
    return legendre(2, p)


def ap_h16(p):
    # CM by Q(i): p=x^2+y^2, choose the odd coordinate x.
    if p % 4 == 3:
        return 0
    for x in range(1, int(p**0.5) + 1):
        y2 = p - x * x
        y = int(y2**0.5)
        if y * y == y2:
            if x % 2 == 1:
                return 2 * (x * x - y * y)
            if y % 2 == 1:
                return 2 * (y * y - x * x)
    raise AssertionError(("no Q(i) CM representation", p))


def ap_h8(p):
    # CM by Q(sqrt(-2)): p=x^2+2y^2, choose odd x.
    if p % 8 in (5, 7):
        return 0
    for x in range(1, int(p**0.5) + 1):
        rem = p - x * x
        if rem >= 0 and rem % 2 == 0:
            y2 = rem // 2
            y = int(y2**0.5)
            if y * y == y2 and x % 2 == 1:
                return 2 * (x * x - 2 * y * y)
    raise AssertionError(("no Q(sqrt(-2)) CM representation", p))


def ap_h32(p):
    # Horie--Yamauchi / audited Stage29: V_h8 = chi_2 tensor V_h32.
    return chi2(p) * ap_h8(p)


def v2(n):
    if n == 0:
        raise ValueError("v2(0)")
    n = abs(n)
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e, n


records = []
for p in (17, 41):
    # p == 1 mod 8, so chi4(p)=chi8(p)=+1 for all three weight-3 forms.
    if p % 8 != 1:
        raise SystemExit("chosen Frobenius prime lost p=1 mod 8")
    a16 = ap_h16(p)
    a8 = ap_h8(p)
    a32 = ap_h32(p)
    if chi2(p) != 1 or a32 != a8:
        raise SystemExit("h32 quadratic-twist specialization regression")
    m16 = 2 * p - a16
    m8 = 2 * p - a8
    m32 = 2 * p - a32
    e16, o16 = v2(m16)
    e8, o8 = v2(m8)
    e32, o32 = v2(m32)
    if (o16, o8, o32) != (1, 1, 1):
        raise SystemExit("selected Frobenius determinant numerator acquired odd factor")
    # T(S) = 3*h16 + 1*h32 + 3*h8, total rank 14.
    full_e = 3 * e16 + e32 + 3 * e8
    full_num = (m16**3) * m32 * (m8**3)
    if full_num != 2**full_e:
        raise SystemExit("full determinant numerator is not the certified 2-power")
    records.append({
        "p": p,
        "chi4_p": 1,
        "chi8_p": 1,
        "chi2_p": 1,
        "a_p_h16": a16,
        "a_p_h32": a32,
        "a_p_h8": a8,
        "det_Frob_minus_1_numerator_h16": m16,
        "det_Frob_minus_1_numerator_h32": m32,
        "det_Frob_minus_1_numerator_h8": m8,
        "full_rank14_det_Frob_minus_1_numerator": full_num,
        "full_rank14_det_Frob_minus_1_v2": full_e,
        "full_rank14_det_Frob_minus_1_denominator": p**14,
        "odd_part_of_full_numerator": 1,
    })

if records[0]["a_p_h16"] != -30 or records[0]["a_p_h8"] != 2:
    raise SystemExit("p=17 coefficient regression")
if records[1]["a_p_h16"] != 18 or records[1]["a_p_h8"] != -46:
    raise SystemExit("p=41 coefficient regression")
if records[0]["full_rank14_det_Frob_minus_1_v2"] != 38:
    raise SystemExit("p=17 full determinant exponent regression")
if records[1]["full_rank14_det_Frob_minus_1_v2"] != 46:
    raise SystemExit("p=41 full determinant exponent regression")

odd_target = br0g["accepted_exact_boundary_kernel"]["odd_primary_boundary_character_module"]
odd_br0b = br0b["accepted_inventory"]["odd_primary"]
assert odd_target == "Hom_cont(G_Q,Q/Z)_odd^48 direct_sum Hom_cont(G_Q(i),Q/Z)_odd^12"
assert odd_br0b == "Hom_cont(G_Q,Q/Z)_odd^14"

cert = {
    "schema": "STAGE33_07_PROPER_BRAUER_ODD_GQ_INVARIANTS_ZERO_V1",
    "stage": "33",
    "unit": "33-07",
    "source_locks": {
        "stage29_global_k3_eigenspace_adapter": "stages/stage29/29-02e/global-k3-eigenspace-adapter.md",
        "stage29_exact_cm_trace_oracle": "stages/stage29/29-02e/k3_trace_check.py",
        "horie_yamauchi": "arXiv:2512.22520v3, Proposition 4.2 and Theorem 4.4",
        "transcendental_decomposition": "T(S)_Ql^ss = 3*V_h16 + V_h32 + 3*V_h8",
        "twist_relation": "V_h8 = chi_2 tensor V_h32",
        "stage33_03_audit_state": "stages/stage33/33-03/audit-state.json",
        "stage33_04_audit_state": "stages/stage33/33-04/audit-state.json",
        "full_br0b_boundary_injection_sha256": fullinj["canonical_sha256"],
        "arithmetic_hs_problem_sha256": hs["canonical_sha256"],
    },
    "proper_transcendental_rank": 14,
    "proper_geometric_brauer_l_primary_divisible_rank": 14,
    "galois_action_integral_lattice_not_assumed_trivial": True,
    "frobenius_certificates": records,
    "frobenius_elimination_logic": {
        "for_every_odd_ell_except_17_use_p": 17,
        "for_ell_17_use_p": 41,
        "denominator_is_ell_unit_condition": "p != ell",
        "det_Frob_minus_1_is_ell_adic_unit": True,
        "therefore_no_nonzero_Frob_fixed_ell_torsion_vector": True,
        "therefore_no_nonzero_G_Q_fixed_ell_torsion_vector": True,
    },
    "proper_geometric_brauer_odd_galois_invariants_zero": True,
    "proper_geometric_brauer_odd_primary_galois_invariants": "0",
    "odd_primary_constant_boundary_target": odd_target,
    "known_global_algebraic_odd_subgroup": "rho(" + odd_br0b + ")",
    "constant_odd_global_image_equals_br0b_odd_image": True,
    "constant_odd_boundary_cokernel_globally_liftable_part": "0",
    "constant_odd_boundary_cokernel_contributes_new_q_defined_brauer_classes": False,
    "reason": (
        "A Q-defined odd-primary class with constant-field boundary residues has zero geometric residues after base change. "
        "Its geometric class therefore lies in Br(Sbar)[odd]^G_Q=0, hence the class is algebraic and already belongs to Stage33-03 BR0B."
    ),
    "repair_reduced_to_two_primary": True,
    "remaining_finite_two_primary_hs_unknown": hs["exact_reduction"]["remaining_finite_group"],
    "remaining_two_primary_constant_unknown": hs["boundary_candidates_not_yet_promoted_to_global_q_classes"]["constant_two_primary"]["exact_unknown_quotient"],
    "new_residual_kernel": "R33-BR2A-TWO-PRIMARY-HS-OBSTRUCTION-ON-CONSTANT-COKERNEL-AND-Z2_23_Z4_3",
    "next_exact_leaf": "L33-07-COMPUTE-2PRIMARY-DELTA_LOC-AND-d2-ON-CONSTANT-COKERNEL-AND-Z2_23-Z4_3",
    "unit_status": "RUNNING_REPAIR",
    "unit_closed": False,
    "downstream_released": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "stage33_09_released": False,
    "unresolved_unknown_in_scope": 1,
    "theorem_credit": True,
    "theorem_credit_scope": "Horie--Yamauchi proper transcendental decomposition + audited Stage29 CM coefficient formulas; Frobenius unit argument",
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
}

raw = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(raw).hexdigest()
(HERE / "proper-brauer-odd-invariants-zero.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)

print(json.dumps({
    "success": True,
    "p17_full_det_numerator": records[0]["full_rank14_det_Frob_minus_1_numerator"],
    "p17_v2": records[0]["full_rank14_det_Frob_minus_1_v2"],
    "p41_full_det_numerator": records[1]["full_rank14_det_Frob_minus_1_numerator"],
    "p41_v2": records[1]["full_rank14_det_Frob_minus_1_v2"],
    "proper_Br_odd_GQ_invariants": 0,
    "odd_constant_cokernel_new_global_classes": 0,
    "repair_reduced_to_two_primary": True,
    "remaining_kernel": cert["new_residual_kernel"],
    "next_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
