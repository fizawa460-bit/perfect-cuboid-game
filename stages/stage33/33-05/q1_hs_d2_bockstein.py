#!/usr/bin/env python3
"""Stage33-05: identify the q1 obstruction with Hochschild--Serre d2.

This script is now deliberately q1-only.  The historical tail that combined
this valid q1 obstruction with the revoked old J2 arithmetic-descent producer
has been removed.

For X=K_c and G=<ct>, Kummer gives

  0 -> Pic(Xbar)/2 -> H^2_et(Xbar,mu_2) -> Br(Xbar)[2] -> 0.

For q1 the independently materialized presentation/Kummer defect is J1, with
an actual integral Picard lift D=Cb+E_P0.  q1_ns_lift_parity.py proves D is
ct-invariant and not a cyclic norm by an odd intersection with a ct-invariant
test conic.  The normalized Bockstein therefore has value D at (ct,ct), so
q1 has nonzero restricted, hence nonzero global, Hochschild--Serre d2.

Nothing in this script proves anything about the corrected J2 arithmetic
descent.  In particular it MUST NOT produce Q-surviving-basis or Stage33-05
closure credit.  Corrected J2 remains blocked on an actual surface mu_2 lift,
Pic/2 defect and HS d2 computation.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

pair = json.loads((ROOT / "xalpha-pair-galois-repair.json").read_text())
front = json.loads((ROOT / "descent-presentation-cocycle.json").read_text())
ns = json.loads((ROOT / "q1-ns-lift-cyclic-parity.json").read_text())

assert pair["full_pair_galois_action_exact"] is True
assert pair["geometric_Br2_GQ_invariant_dimension"] == 2
assert pair["explicit_brauer_quotient_basis"] == ["J2", "q1"]
assert front["presentation_connecting_cocycle"]["q1"]["ct"] == "J1"
assert ns["J1_integral_NS_lift_materialized"] is True
assert ns["D_ct_invariant"] is True
assert ns["D_test_intersection"] == 1
assert ns["D_nonzero_in_H2_C2_Pic"] is True

G = (0, 1)
J = {0: 0, 1: 1}

def act(g, coeff):
    return coeff

def coboundary_J(g, h):
    return act(g, J[h]) - J[(g + h) & 1] + J[g]

dJ = {(g, h): coboundary_J(g, h) for g in G for h in G}
assert dJ == {(0,0):0, (0,1):0, (1,0):0, (1,1):2}
assert all(v % 2 == 0 for v in dJ.values())
bockstein = {k: v // 2 for k, v in dJ.items()}
assert bockstein == {(0,0):0, (0,1):0, (1,0):0, (1,1):1}

def b(g, h):
    return bockstein[(g, h)]

for g in G:
    for h in G:
        for k in G:
            db = act(g, b(h,k)) - b((g+h)&1,k) + b(g,(h+k)&1) - b(g,h)
            assert db == 0

assert ns["D_is_cyclic_norm"] is False

cert = {
    "schema": "STAGE33_05_Q1_HS_D2_BOCKSTEIN_V2_Q1_ONLY",
    "status": "PASS_EXACT_Q1_HS_D2_NONZERO_NO_J2_SURVIVAL_CREDIT",
    "source_lock": {
        "kummer": "Stacks Project tag 03PK, Lemma 59.28.1 and its long exact sequence",
        "leray": "Stacks Project tag 03QA / Proposition 59.54.2",
        "cv_surface": "Creutz--Viray, On Brauer groups of double covers of ruled surfaces, Theorem 2.5 and Theorem I",
        "cv_curve_hs": "Creutz--Viray, Two torsion in the Brauer group of a hyperelliptic curve, Remark 3.1 and Proposition 3.2",
        "cv_curve_chain": "same paper, Lemmas 3.4--3.5: divisor coboundary and corestriction/cup-product cocycle",
        "pic_torsion_free": "K3 Picard group is Neron--Severi and torsion-free; Stage33/Testa--Stoll PicK rank-20 lattice source lock"
    },
    "effective_subgroup": "C2=<ct>",
    "geometric_brauer_basis_context_only": ["J2", "q1"],
    "q1_kummer_defect": "J1 = D mod 2",
    "D_integral_NS_lift": ns["J1_integral_NS_lift"],
    "D_ct_invariant": True,
    "D_test_intersection": ns["D_test_intersection"],
    "D_nonzero_in_H2_C2_Pic": True,
    "normalized_integral_1cochain_coefficients": {"e":0, "ct":1},
    "integral_coboundary_coefficients_on_D": {"e,e":0, "e,ct":0, "ct,e":0, "ct,ct":2},
    "bockstein_2cocycle_coefficients_on_D": {"e,e":0, "e,ct":0, "ct,e":0, "ct,ct":1},
    "HS_d2_restricted_to_C2_equals_D_class": True,
    "HS_d2_q1_restriction_nonzero": True,
    "HS_d2_q1_global_nonzero": True,
    "q1_Q_descent": False,
    "j2_arithmetic_descent_consumed": False,
    "J2_Q_descent_certified": False,
    "Q_relevant_surviving_dimension_certified": False,
    "all_stage33_05_descent_unknowns_resolved": False,
    "current_J2_blocker": "MATERIALIZE_CORRECTED_J2_SURFACE_MU2_LIFT_PIC_MOD2_DEFECT_AND_HS_D2",
    "next_exact_leaf": "L33-05-CORRECTED-J2-SURFACE-MU2-AND-HS-D2",
    "theorem_credit": False,
    "receiver_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_existence_claim": False,
    "perfect_cuboid_nonexistence_claim": False
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "q1-hs-d2-bockstein.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(cert, indent=2, sort_keys=True))
