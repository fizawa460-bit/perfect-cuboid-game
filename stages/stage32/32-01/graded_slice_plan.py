#!/usr/bin/env python3
"""Stage32-01 exact graded-slice checkpoint planner.

This does not claim candidate enumeration completeness.  It turns every audited
(genus, degree) row into immutable bounded strata using the exact positive dual
identity proved in the merged polytail unit:

    19 H.x = sum_{92 curves} D.x + 5 sum_{48 exceptional} E.x.

For fixed degree d and exceptional mass e=sum E.x, the nonexceptional mass is
exactly 19*d-5*e.  Each stratum is therefore finite and independently resumable.
"""
from __future__ import annotations

import hashlib
import json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "graded-slice-manifest.json"


def rows():
    # Audited windows: G0 even 2..176 and G1 even 4..192.
    for g, lo, hi in ((0, 2, 176), (1, 4, 192)):
        for d in range(lo, hi + 1, 2):
            r = math.gcd(d, 16)
            m = 16 // r
            n = d // r
            # Frozen Stage29 bounds for -y^2.
            if g == 0:
                qnum = m * m * (d * d + 16 * d + 32)
            else:
                qnum = m * m * (d * d + 16 * d)
            assert qnum % 16 == 0
            yield {
                "genus": g,
                "degree": d,
                "r": r,
                "m": m,
                "n": n,
                "hperp_norm_bound": qnum // 16,
            }


def stable_id(obj: dict) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()[:20]


all_rows = []
stratum_count = 0
for row in rows():
    d = row["degree"]
    total = 19 * d
    strata = []
    for e_mass in range(total // 5 + 1):
        curve_mass = total - 5 * e_mass
        key = {
            "g": row["genus"],
            "d": d,
            "exceptional_mass": e_mass,
            "nonexceptional_mass": curve_mass,
        }
        strata.append({
            "id": stable_id(key),
            "exceptional_mass": e_mass,
            "nonexceptional_mass": curve_mass,
            "status": "UNSTARTED",
        })
    row = dict(row)
    row.update({
        "positive_identity_total": total,
        "exceptional_coordinate_cap": total // 5,
        "nonexceptional_coordinate_cap": total,
        "stratum_count": len(strata),
        "strata": strata,
    })
    stratum_count += len(strata)
    all_rows.append(row)

assert len(all_rows) == 183
manifest = {
    "schema": "STAGE32_GRADED_SLICE_MANIFEST_V1",
    "stage": "32-01",
    "scope": "UNIBRANCH_NUMERICAL_CENSUS",
    "row_count": len(all_rows),
    "stratum_count": stratum_count,
    "identity": "19*(H.x)=sum_92_curve(D.x)+5*sum_48_exceptional(E.x)",
    "complete_census_claim": False,
    "rows": all_rows,
}
manifest["manifest_sha256"] = hashlib.sha256(
    json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
).hexdigest()
OUT.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "row_count": len(all_rows),
    "stratum_count": stratum_count,
    "manifest_sha256": manifest["manifest_sha256"],
    "max_degree_g0": 176,
    "max_degree_g1": 192,
}, sort_keys=True))
