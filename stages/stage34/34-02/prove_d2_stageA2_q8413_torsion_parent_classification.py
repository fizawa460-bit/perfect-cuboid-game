#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
from fractions import Fraction
from math import gcd, isqrt

ROOT = pathlib.Path(__file__).resolve().parent
RANKZERO = ROOT / "d2-stageA2-q8413-two-quotient-rankzero-preaudit-certificate.json"
QLOCK = ROOT / "d2-stageA2-remaining-three-gaussian-elliptic-quotient-lock.json"
OUT = ROOT / "d2-stageA2-q8413-torsion-parent-classification-certificate.json"

def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])

def gneg(z):
    return (-z[0], -z[1])

def gmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])

def eval_gaussian_mod(z, p, iroot):
    return (z[0] + z[1] * iroot) % p

def curve_count_mod_p(p, iroot, a2, a4):
    a2p = eval_gaussian_mod(a2, p, iroot)
    a4p = eval_gaussian_mod(a4, p, iroot)
    total = 1
    for x in range(p):
        rhs = (x * x * x + a2p * x * x + a4p * x) % p
        if rhs == 0:
            total += 1
        elif pow(rhs, (p - 1) // 2, p) == 1:
            total += 2
    return total

def is_square_q(q):
    q = Fraction(q)
    if q < 0:
        return False
    return isqrt(q.numerator) ** 2 == q.numerator and isqrt(q.denominator) ** 2 == q.denominator

def sqrt_q(q):
    q = Fraction(q)
    assert is_square_q(q)
    return Fraction(isqrt(q.numerator), isqrt(q.denominator))

def curve_rhs(model_id, x):
    if model_id == 38:
        return Fraction(-6887) * x * (x - 1) * (x + 1) * (6 * x + 7) * (7 * x - 6)
    if model_id == 165:
        return Fraction(6887) * x * (x - 1) * (x + 1) * (x + 13) * (13 * x - 1)
    raise AssertionError(model_id)

def classify_parent(model_id, x, delta):
    a, b = 84, 13
    U = x * x - 1
    V = 2 * x
    A = a * U + b * V
    B = b * U + a * V
    vals = [U, V, A, B]
    square_flags = [is_square_q(vals[j] / Fraction(delta[j])) for j in range(4)]
    rhs = curve_rhs(model_id, x)
    c_point = is_square_q(rhs)
    receiver_degenerate = any(z == 0 for z in vals)
    full_parent = c_point and all(square_flags)
    return {
        "x": str(x),
        "U": str(U),
        "V": str(V),
        "A": str(A),
        "B": str(B),
        "C_rhs": str(rhs),
        "C_point": c_point,
        "square_flags_U_V_A_B": square_flags,
        "full_parent": full_parent,
        "receiver_degenerate": receiver_degenerate,
        "nondegenerate_full_parent": full_parent and not receiver_degenerate,
    }

rankzero = json.loads(RANKZERO.read_text())
assert rankzero["schema"] == "STAGE34_02C_D2_STAGEA2_Q8413_TWO_QUOTIENT_RANKZERO_PREAUDIT_CERTIFICATE_V1"
assert rankzero["status"] == "PASS_EXACT_Q8413_QUOTIENT_RANKZERO_PREAUDIT_NO_BRANCH_CLOSURE"
assert rankzero["model38"]["mordell_weil_rank"] == 0
assert rankzero["model165"]["mordell_weil_rank"] == 0
assert rankzero["model38"]["two_torsion_invariants"] == [2, 2]

qlock = json.loads(QLOCK.read_text())
targets = {int(t["model_id"]): t for t in qlock["targets"] if t["q"] == "84/13"}
assert set(targets) == {38, 165}

models = {
    38: {
        "branch_id": "40dc8f63e92a8a3a65e8",
        "sign_partner": "8a374a057daf5f92a87e",
        "a2": (-89531, 578508),
        "a4": (0, -51794399748),
        "roots": [(0, 0), (89531, 0), (0, -578508)],
        "alpha": -289254,
        "delta": [13, -21, 1880151, -6887],
    },
    165: {
        "branch_id": "7a7ef1a67e794fe1651f",
        "sign_partner": "98b42307b3aa398f1e0c",
        "a2": (1157016, -179062),
        "a4": (0, -207177598992),
        "roots": [(0, 0), (-1157016, 0), (0, 179062)],
        "alpha": 89531,
        "delta": [42, -26, 13774, -3760302],
    },
}
prime_embeddings = [(29, 12), (37, 6)]
records = []

for model_id in (38, 165):
    m = models[model_id]
    t = targets[model_id]
    assert t["branch_id"] == m["branch_id"]
    assert t["sign_partner"] == m["sign_partner"]
    assert int(t["alpha"]) == m["alpha"]
    assert list(map(int, t["delta"])) == m["delta"]

    r0, r1, r2 = m["roots"]
    assert r0 == (0, 0)
    assert gneg(gadd(r1, r2)) == m["a2"]
    assert gmul(r1, r2) == m["a4"]

    reductions = []
    counts = []
    for p, iroot in prime_embeddings:
        assert (iroot * iroot + 1) % p == 0
        roots_mod = [eval_gaussian_mod(r, p, iroot) for r in m["roots"]]
        assert len(set(roots_mod)) == 3
        n = curve_count_mod_p(p, iroot, m["a2"], m["a4"])
        reductions.append({"p": p, "i_mod_p": iroot, "roots_mod_p": roots_mod, "group_order": n})
        counts.append(n)

    torsion_upper = gcd(*counts)
    assert torsion_upper == 4
    torsion_order = 4
    assert torsion_order == torsion_upper

    rational_X = sorted(Fraction(z[0]) for z in m["roots"] if z[1] == 0)
    inverse = []
    reconstructed = []
    for X in rational_X:
        u = X / Fraction(m["alpha"])
        disc = u * u + 4
        assert is_square_q(disc)
        sd = sqrt_q(disc)
        xs = sorted(set([(u + sd) / 2, (u - sd) / 2]))
        inverse.append({"X": str(X), "u": str(u), "u2_plus_4": str(disc), "rational_x": [str(x) for x in xs]})
        reconstructed.extend(xs)
    reconstructed = sorted(set(reconstructed))
    classifications = [classify_parent(model_id, x, m["delta"]) for x in reconstructed]
    assert all(r["C_point"] for r in classifications)
    assert all(r["receiver_degenerate"] for r in classifications)
    assert not any(r["nondegenerate_full_parent"] for r in classifications)

    rec = {
        "model_id": model_id,
        "branch_id": m["branch_id"],
        "sign_partner": m["sign_partner"],
        "mordell_weil_rank": 0,
        "good_reduction_torsion_bound": {
            "principle": "For good reduction at a prime of residue characteristic >2, torsion injects into the reduced elliptic curve; two good reductions therefore bound the torsion order by the gcd of their group orders.",
            "reductions": reductions,
            "gcd_group_orders": torsion_upper,
            "known_C2xC2_order": 4,
            "torsion_group": "C2 x C2",
        },
        "all_torsion_X_over_Qi": ["infinity"] + [f"{a}{'+' if b >= 0 else ''}{b}*i" for a, b in m["roots"]],
        "finite_rational_quotient_X": [str(x) for x in rational_X],
        "quotient_infinity_receiver_degenerate": True,
        "inverse_reconstruction": inverse,
        "reconstructed_rational_x": [str(x) for x in reconstructed],
        "parent_classification": classifications,
        "nondegenerate_full_parent_lift_count": sum(bool(r["nondegenerate_full_parent"]) for r in classifications),
        "direct_branch_closure_candidate": True,
    }
    records.append(rec)

assert [r["nondegenerate_full_parent_lift_count"] for r in records] == [0, 0]

payload = {
    "schema": "STAGE34_02C_D2_STAGEA2_Q8413_TORSION_PARENT_CLASSIFICATION_CERTIFICATE_V1",
    "status": "PASS_EXACT_Q8413_TWO_REPRESENTATIVE_TORSION_PARENT_CLASSIFICATION_PREAUDIT",
    "source_script": "prove_d2_stageA2_q8413_torsion_parent_classification.py",
    "source_rankzero_certificate": RANKZERO.name,
    "source_quotient_lock": QLOCK.name,
    "method": "Use exact rank zero plus an exact good-reduction torsion bound to enumerate every Q(i)-point on each elliptic quotient. Filter the complete torsion list by rational quotient X, invert u=x-1/x over Q, then exact-test the genus-two equation, U/V/A/B square conditions, and receiver degeneracy.",
    "representative_records": records,
    "representative_closure_candidates": [r["branch_id"] for r in records],
    "sign_transfer_candidates": [r["sign_partner"] for r in records],
    "authoritative_effect_before_hostile_audit": "NONE",
    "next_gate": "Independent hostile audit must verify the good-reduction torsion injection hypotheses/counts, complete rational-X list, inverse reconstruction, parent-square tests, exceptional quotient infinity, and exact sign-transfer applicability before reducing authoritative remaining branches from 4 to 0.",
    "firewalls": {
        "rank_zero_used": True,
        "torsion_pointset_complete": True,
        "rational_X_classified": True,
        "parent_pullback_classified": True,
        "direct_representatives_closed_authoritatively": False,
        "sign_partners_closed_authoritatively": False,
        "hostile_audit_passed": False,
        "authoritative_remaining_branches": 4,
        "authoritative_remaining_sign_orbits": 2,
        "D2_all_factor_branches_closed": False,
        "R29_EXT_CHANG_C_closed": False,
        "perfect_cuboid_nonexistence_claim": False
    }
}
OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "status": payload["status"],
    "representatives": payload["representative_closure_candidates"],
    "sign_transfer_candidates": payload["sign_transfer_candidates"],
    "authoritative_remaining_branches": 4
}, sort_keys=True))
