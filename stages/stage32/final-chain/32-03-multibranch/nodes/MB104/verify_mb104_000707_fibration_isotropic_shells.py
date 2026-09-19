#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

SUPPORT_MASK = "000707000f0f"
COMPACT = [0, 1, 2, 3, 8, 9, 10, 11, 24, 25, 26, 32, 33, 34]
SHELLS = [
    (10, 30, 10, 8, 5, 400, -320),
    (10, 34, 9, 8, 5, 400, -288),
    (10, 38, 8, 8, 5, 400, -256),
    (12, 36, 12, 4, 3, 144, -192),
]


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def gcd_all(xs: list[int]) -> int:
    g = 0
    for x in xs:
        g = math.gcd(g, abs(x))
    return g


ap = argparse.ArgumentParser()
ap.add_argument("--certificate", required=True)
args = ap.parse_args()

d = json.loads(Path(args.certificate).read_text(encoding="utf-8"))
assert d["schema"] == "STAGE32_MB104_000707_FIBRATION_ISOTROPIC_SHELLS_V1"
claimed = d["canonical_sha256_without_this_field"]
body = dict(d)
body.pop("canonical_sha256_without_this_field")
assert claimed == csha(body)

src = d["source_locks"]
assert src["stoll_commit"] == "51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
assert src["stoll_cuboids_blob"] == "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
assert src["stage33_stoll_helper_blob"] == "010db3767b8f932c71ac5722b50ccb64a8c79f9d"
assert src["stage33_picard_marking_blob"] == "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"
assert src["stage32_picard_core_sha256"] == "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"

scope = d["mathematical_scope"]
assert scope["support_mask"] == SUPPORT_MASK
assert scope["P2"] == 336
assert scope["H_dot_P"] == 112
assert scope["degree10"]["P_dot_F_values"] == [30, 34, 38]
assert scope["degree10"]["support_mass_values"] == [10, 9, 8]
assert scope["degree10"]["minus_x2"] == 400
assert scope["degree12"]["P_dot_F_values"] == [36]
assert scope["degree12"]["support_mass_values"] == [12]
assert scope["degree12"]["minus_y2"] == 144

ex = d["execution"]
assert ex["support_request_count"] == 1
assert ex["shell_count"] == 4
assert ex["rank_before_P_pairing_reduction"] == 63
assert ex["rank_after_P_pairing_reduction"] == 62
assert ex["max_hperp_norm"] == 400
assert ex["raw_artifact_persisted"] is False

s = d["support"]
assert s["mask"] == SUPPORT_MASK
assert s["orbit_size"] == 768
assert s["compact_indices_0based"] == COMPACT
mp = s["compact_to_stoll_pts_1based"]
assert sorted(mp) == list(range(1, 49))
assert s["support_stoll_pts_1based"] == [mp[i] for i in COMPACT]
assert len(set(s["support_stoll_pts_1based"])) == 14
assert s["kernel_rank"] == 62

got = []
deg10 = deg12 = 0
seen_coords: set[tuple[int, ...]] = set()
for sh in s["shells"]:
    tup = (
        sh["degree"],
        sh["p_intersection"],
        sh["support_mass"],
        sh["scale_a"],
        sh["scale_b"],
        sh["hperp_norm"],
        sh["hperp_p_pairing"],
    )
    got.append(tup)
    e, pf, sm, aa, bb, nrm, pc = tup
    assert pc == aa * pf - bb * 112
    assert 7 * e - 4 * sm == pf
    assert sh["raw_affine_close_vector_count"] >= sh["integral_picard_class_count"]
    assert sh["integral_picard_class_count"] >= sh["known140_nonnegative_count"]
    assert sh["known140_nonnegative_count"] >= sh["primitive_known140_nonnegative_candidate_count"]
    assert sh["primitive_known140_nonnegative_candidate_count"] == len(sh["primitive_known140_nonnegative_candidates"])
    for rec in sh["primitive_known140_nonnegative_candidates"]:
        coords = rec["picard_basis_coordinates"]
        assert len(coords) == 64
        assert gcd_all(coords) == 1
        assert rec["minimum_known140_pairing"] >= 0
        zeros = rec["zero_known140_indices_1based"]
        assert zeros == sorted(set(zeros))
        assert all(1 <= j <= 140 for j in zeros)
        key = tuple(coords)
        assert key not in seen_coords
        seen_coords.add(key)
    if e == 10:
        deg10 += sh["primitive_known140_nonnegative_candidate_count"]
    elif e == 12:
        deg12 += sh["primitive_known140_nonnegative_candidate_count"]
    else:
        raise AssertionError("unexpected degree")

assert got == SHELLS
summary = d["summary"]
assert summary["degree10_primitive_known140_nonnegative_candidate_count"] == deg10
assert summary["degree12_primitive_known140_nonnegative_candidate_count"] == deg12
assert summary["total_primitive_known140_nonnegative_candidate_count"] == deg10 + deg12
assert summary["fibration_improvement_shells_numerically_empty_candidate"] == (deg10 + deg12 == 0)
assert summary["geometric_effectivity_or_semiampleness_proved"] is False
assert summary["global_min_P_dot_F_40_proved"] is False
assert all(v is False for v in d["credit_firewall"].values())

print(
    json.dumps(
        {
            "success": True,
            "canonical": claimed,
            "degree10_candidates": deg10,
            "degree12_candidates": deg12,
            "total_candidates": deg10 + deg12,
        },
        sort_keys=True,
    )
)
