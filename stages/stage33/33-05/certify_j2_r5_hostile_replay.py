#!/usr/bin/env python3
"""Network-free hostile replay for Stage33-05 J2 repair R1--R4.

This verifier intentionally does not restore Q-descent credit.  It independently
replays the load-bearing finite/algebraic checks and verifies that the retained
R4 integral-kernel adapter is geometric-only.  Stage33-05 remains reopened
until a corrected Q-defined arithmetic representative/descent datum is proved.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

HERE = Path(__file__).resolve().parent
R1 = HERE / "j2-abstract-nonzero-reaudit.json"
R2 = HERE / "j2-corrected-full-l-representative.json"
R3 = HERE / "j2-corrected-cv-e2-cocycle.json"
R4 = HERE / "j2-r4-translation-quotient-lattice.json"
R4H = HERE / "j2-r4-hostile-torsor-brauer-kernel-verification.json"
R5 = HERE / "j2-r5-hostile-replay.json"


def rank2(rows):
    a = [r[:] for r in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(rank, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for j in range(len(a)):
            if j != rank and a[j][col]:
                a[j] = [x ^ y for x, y in zip(a[j], a[rank])]
        rank += 1
    return rank


def main():
    r1 = json.loads(R1.read_text())
    r2 = json.loads(R2.read_text())
    r3 = json.loads(R3.read_text())
    r4 = json.loads(R4.read_text())
    r4h = json.loads(R4H.read_text())
    r5 = json.loads(R5.read_text())

    # R1: independent F2 replay for all four undetermined image normal forms.
    j1 = [1,0,0,0,0]
    j2 = [0,1,0,0,0]
    cases = []
    for b in (0,1):
        for d in (0,1):
            image = [j1, [0,b,1,1,0], [0,d,1,1,1]]
            cases.append([b,d,rank2(image),rank2(image+[j2])])
    assert cases == [[0,0,3,4],[0,1,3,4],[1,0,3,4],[1,1,3,4]]
    assert r1["exact_conclusion"]["J2_nonzero_in_LcE_mod_im_xalpha_for_all_undetermined_b_d"] is True

    t = sp.symbols("t")
    s2 = sp.sqrt(2)
    q = t**4 - 6*t**2 + 1
    roots = [1+s2, -(1+s2), s2-1, 1-s2]
    assert sp.expand(sp.prod(t-r for r in roots) - q) == 0
    f2 = sp.cancel((t+1+s2)/(t-1+s2))
    assert sp.cancel(f2/q - 1/((t-roots[0])*(t-roots[2])*(t-roots[3])**2)) == 0
    assert r2["full_quotient_zero_test"]["corrected_pair_zero"] is False
    assert r2["Q_defined_descent_credit_restored"] is False

    # R3: verify the retained exact square identity on E.
    X, Y = sp.symbols("X Y")
    r = (t**2-1)**2
    sc = 2*t*X/Y
    gp = t*(1-sc**2) + sp.I*sc*(1-t**2)
    lhs = (-1/(t*r))*gp/(X-r)
    rhs = (1/(X-r)+sp.I*Y/((t**2-1)*(X-r)*(X-q)))**2
    num = sp.fraction(sp.together(lhs-rhs))[0]
    relation = X*(X-r)*(X-q)
    poly = sp.Poly(sp.expand(num), Y)
    rem = 0
    for (k,), coeff in poly.terms():
        rem += coeff * Y**(k % 2) * relation**(k // 2)
    assert sp.expand(rem) == 0
    assert r3["cv_lemma_4_6"]["xi_rho"] == "Tr"

    # R4: independent algebra and Mobius/Legendre replay.
    a = (t**2+1)**2
    b = (2*t*(t**2-1))**2
    dp = t**2-2*t-1
    dm = t**2+2*t-1
    assert sp.expand(a*a-4*b-q*q) == 0
    assert sp.expand(a-4*t*(t**2-1)-dp**2) == 0
    assert sp.expand(a+4*t*(t**2-1)-dm**2) == 0
    assert sp.expand(dm**2-dp**2-8*t*(t**2-1)) == 0
    u = -(1+s2)*(t+s2-1)/(t-1-s2)
    assert sp.cancel(q.subs(t,u)/(u**2-1)**2 - (dm**2-dp**2)/dm**2) == 0
    assert r4["lattice_conclusion"]["torsor_transcendental_gram"] == [[8,0],[0,16]]
    assert r4["lattice_conclusion"]["minimum_norm"] == 8
    assert r4["lattice_conclusion"]["marked_brauer_coordinate"] == [1,0]

    # Hostile theorem/application adapter must explicitly certify integral scope.
    assert r4h["status"] == "PASS_HOSTILE_R4_INTEGRAL_KERNEL_IDENTIFICATION"
    assert r4h["hostile_checks"]["mere_rational_hodge_isometry_rejected"] is True
    assert r4h["hostile_checks"]["integral_pairing_verified"] is True
    assert r4h["hostile_checks"]["torsor_class_equals_named_corrected_J2_verified"] is True
    assert r4h["hostile_checks"]["smooth_projective_k3_model_verified"] is True
    assert r4h["verdict"]["Q_defined_descent_credit_restored"] is False

    # R5 credit firewall: geometric repair passes; old arithmetic descent is not inherited.
    assert r5["r5_exit"]["hostile_replay_R1_R4"] == "PASS"
    assert r5["credit_reconciliation"]["corrected_J2_Q_defined_arithmetic_representative_materialized"] is False
    assert r5["credit_reconciliation"]["corrected_J2_Q_descent_certified"] is False
    assert r5["r5_exit"]["stage33_05_reclosed"] is False
    assert r5["r5_exit"]["stage33_12_closed_exact"] is False
    assert r5["r5_exit"]["stage33_13_released"] is False
    assert r5["r5_exit"]["stage33_progress"] == "5/11"

    print(json.dumps({
        "status": "PASS_HOSTILE_REPLAY_R1_TO_R4_GEOMETRIC_ONLY",
        "R1_cases": cases,
        "R4_gram": [[8,0],[0,16]],
        "R4_minimum_norm": 8,
        "R4_marked_J2": [1,0],
        "Q_descent_restored": False,
        "next": r5["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
