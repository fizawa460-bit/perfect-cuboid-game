#!/usr/bin/env python3
"""Deterministic static feasibility census for the post-B16 Stage32 gate.

No search is performed here.  This script only expands the already-audited
Stage29 genus/degree windows and exact H^perp norm formulas, then counts the
coarse positive-dual strata inherited from Stage32-01.
"""
from __future__ import annotations

import hashlib
import json
import math


def audited_rows():
    for genus, lo, hi in ((0, 2, 176), (1, 4, 192)):
        for degree in range(lo, hi + 1, 2):
            r = math.gcd(degree, 16)
            m = 16 // r
            num = m * m * (
                degree * degree
                + 16 * degree
                + (32 if genus == 0 else 0)
            )
            assert num % 16 == 0
            yield {
                "genus": genus,
                "degree": degree,
                "r": r,
                "m": m,
                "hperp_norm_bound": num // 16,
            }


rows = list(audited_rows())
assert len(rows) == 183
assert sum(r["genus"] == 0 for r in rows) == 88
assert sum(r["genus"] == 1 for r in rows) == 95

d16g0 = next(r for r in rows if r["genus"] == 0 and r["degree"] == 16)
assert d16g0["hperp_norm_bound"] == 34

max_row = max(rows, key=lambda r: r["hperp_norm_bound"])
assert max_row == {
    "genus": 1,
    "degree": 190,
    "r": 2,
    "m": 8,
    "hperp_norm_bound": 156560,
}

m_classes = {}
for m in sorted({r["m"] for r in rows}):
    block = [r for r in rows if r["m"] == m]
    top = max(block, key=lambda r: r["hperp_norm_bound"])
    m_classes[str(m)] = {
        "row_count": len(block),
        "max_hperp_norm_bound": top["hperp_norm_bound"],
        "max_row": {"genus": top["genus"], "degree": top["degree"]},
    }

# Stage32-01's positive-dual identity gives one coarse exceptional-mass
# stratum for every e in [0, floor(19d/5)].
raw_exceptional_mass_strata = sum((19 * r["degree"]) // 5 + 1 for r in rows)
assert raw_exceptional_mass_strata == 65249

# Testa--Stoll classifies degree <= 6.  For the residual higher-degree
# unibranch population the audited necessary exceptional-incidence lower
# bounds are e>=8 for genus-0 nonconics and e>=4 for genus 1.
residual_rows = [r for r in rows if r["degree"] > 6]
assert len(residual_rows) == 178
assert sum(r["genus"] == 0 for r in residual_rows) == 85
assert sum(r["genus"] == 1 for r in residual_rows) == 93

filtered_exceptional_mass_strata = 0
filtered_by_genus = {}
for genus, emin in ((0, 8), (1, 4)):
    block = [r for r in residual_rows if r["genus"] == genus]
    count = sum(
        max(0, (19 * r["degree"]) // 5 - emin + 1)
        for r in block
    )
    filtered_by_genus[str(genus)] = {
        "row_count": len(block),
        "exceptional_mass_lower_bound": emin,
        "coarse_stratum_count": count,
    }
    filtered_exceptional_mass_strata += count
assert filtered_exceptional_mass_strata == 64111

payload = {
    "schema": "STAGE32_POST_B16_RESIDUAL_FEASIBILITY_STATIC_V1",
    "audited_window": {
        "row_count": len(rows),
        "g0_row_count": 88,
        "g1_row_count": 95,
        "g0_degree_max": 176,
        "g1_degree_max": 192,
    },
    "norm_geometry": {
        "d16_g0_full_norm_bound": d16g0["hperp_norm_bound"],
        "d16_g0_audited_b16_bound": 16,
        "rows_with_norm_bound_gt_34": sum(
            r["hperp_norm_bound"] > 34 for r in rows
        ),
        "rows_with_norm_bound_gt_10000": sum(
            r["hperp_norm_bound"] > 10000 for r in rows
        ),
        "max_row": max_row,
        "m_classes": m_classes,
    },
    "positive_dual_partition": {
        "raw_exceptional_mass_strata": raw_exceptional_mass_strata,
        "known_degree_le_6_rows_consumed_from_audited_classification": 5,
        "residual_row_count": len(residual_rows),
        "filtered_exceptional_mass_strata": filtered_exceptional_mass_strata,
        "filtered_by_genus": filtered_by_genus,
    },
    "feasibility_conclusions": {
        "direct_norm_shell_continuation_is_full_window_driver": False,
        "one_actions_job_per_exceptional_mass_stratum_is_safe_driver": False,
        "production_requires_exact_intersection_coordinate_branch_and_bound": True,
        "production_requires_lattice_membership_congruence_pruning": True,
        "production_requires_aut_canonical_augmentation": True,
        "heavy_run_authorized_by_this_static_analyzer": False,
    },
}
raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
payload["payload_sha256"] = hashlib.sha256(raw).hexdigest()
print(json.dumps(payload, indent=2, sort_keys=True))
