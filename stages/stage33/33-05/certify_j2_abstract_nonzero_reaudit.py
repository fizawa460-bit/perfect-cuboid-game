#!/usr/bin/env python3
"""Exact R1 hostile re-audit of abstract J2 nonzero survival.

This verifier intentionally does not use the revoked concrete ell_J2 as a
nonzero witness.  It checks only the finite F2 presentation retained from the
geometric Creutz--Viray quotient computation.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-abstract-nonzero-reaudit.json"


def rank2(rows):
    a = [[int(x) & 1 for x in r] for r in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    rr = 0
    for c in range(n):
        pivot = next((i for i in range(rr, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[rr], a[pivot] = a[pivot], a[rr]
        for i in range(m):
            if i != rr and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[rr])]
        rr += 1
    return rr


cert = json.loads(CERT.read_text(encoding="utf-8"))
assert cert["schema"] == "STAGE33_05_J2_ABSTRACT_NONZERO_REAUDIT_V1"
assert cert["basis_order"] == ["J1", "J2", "q1", "q2", "q3"]
assert cert["LcE_dimension"] == 5
assert cert["geometric_Br2_dimension"] == 2
assert cert["xalpha_image_dimension"] == 3
assert cert["exact_conclusion"]["revoked_ell_J2_used_as_nonzero_witness"] is False

J2 = [0, 1, 0, 0, 0]
expected = []
for b in (0, 1):
    for d in (0, 1):
        rows = [
            [1, 0, 0, 0, 0],
            [0, b, 1, 1, 0],
            [0, d, 1, 1, 1],
        ]
        r = rank2(rows)
        rj = rank2(rows + [J2])
        assert r == 3
        assert rj == 4
        expected.append({
            "b": b,
            "d": d,
            "rank_image": r,
            "rank_image_plus_J2": rj,
            "J2_in_image": False,
        })

assert cert["case_results"] == expected
assert cert["exact_conclusion"]["J2_nonzero_in_LcE_mod_im_xalpha_for_all_undetermined_b_d"] is True
assert cert["exact_conclusion"]["abstract_J2_survival_reaudit"] == "ABSTRACT_J2_NONZERO_CONFIRMED"
assert cert["exact_conclusion"]["current_promoted_ell_J2_restored"] is False
assert cert["repair_transition"]["R1"] == "DONE_ABSTRACT_J2_NONZERO_CONFIRMED"
assert cert["repair_transition"]["R2"].startswith("RELEASED_")
assert all(v is False for v in cert["firewalls"].values())

print(json.dumps({
    "success": True,
    "R1": "DONE_ABSTRACT_J2_NONZERO_CONFIRMED",
    "cases_checked": 4,
    "J2_nonzero_all_cases": True,
    "revoked_ell_used": False,
    "next": cert["repair_transition"]["next_exact_leaf"],
}, sort_keys=True))
