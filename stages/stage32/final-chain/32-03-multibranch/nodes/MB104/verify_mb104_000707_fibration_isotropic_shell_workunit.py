#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

EXPECTED = [
    (10, 30, 10, 8, 5, 400, -320),
    (10, 34, 9, 8, 5, 400, -288),
    (10, 38, 8, 8, 5, 400, -256),
    (12, 36, 12, 4, 3, 144, -192),
]
COMPACT = [0, 1, 2, 3, 8, 9, 10, 11, 24, 25, 26, 32, 33, 34]


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def gcd_all(xs: list[int]) -> int:
    g = 0
    for x in xs:
        g = math.gcd(g, abs(x))
    return g


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certificate", required=True)
    ap.add_argument("--shell-index", type=int, required=True, choices=range(4))
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

    ex = d["execution"]
    assert ex["support_request_count"] == 1
    assert ex["shell_count"] == 1
    assert ex["rank_before_P_pairing_reduction"] == 63
    assert ex["rank_after_P_pairing_reduction"] == 62
    assert ex["raw_artifact_persisted"] is False

    s = d["support"]
    assert s["mask"] == "000707000f0f"
    assert s["orbit_size"] == 768
    assert s["compact_indices_0based"] == COMPACT
    mp = s["compact_to_stoll_pts_1based"]
    assert sorted(mp) == list(range(1, 49))
    assert s["support_stoll_pts_1based"] == [mp[i] for i in COMPACT]
    assert s["kernel_rank"] == 62
    assert len(s["shells"]) == 1

    sh = s["shells"][0]
    got = (
        sh["degree"],
        sh["p_intersection"],
        sh["support_mass"],
        sh["scale_a"],
        sh["scale_b"],
        sh["hperp_norm"],
        sh["hperp_p_pairing"],
    )
    assert got == EXPECTED[args.shell_index]
    e, pf, sm, aa, bb, nrm, pc = got
    assert pc == aa * pf - bb * 112
    assert 7 * e - 4 * sm == pf
    assert sh["raw_affine_close_vector_count"] >= sh["integral_picard_class_count"]
    assert sh["integral_picard_class_count"] >= sh["known140_nonnegative_count"]
    assert sh["known140_nonnegative_count"] >= sh["primitive_known140_nonnegative_candidate_count"]
    cands = sh["primitive_known140_nonnegative_candidates"]
    assert sh["primitive_known140_nonnegative_candidate_count"] == len(cands)

    seen = set()
    for rec in cands:
        coords = rec["picard_basis_coordinates"]
        assert len(coords) == 64
        assert gcd_all(coords) == 1
        assert rec["minimum_known140_pairing"] >= 0
        zeros = rec["zero_known140_indices_1based"]
        assert zeros == sorted(set(zeros))
        assert all(1 <= j <= 140 for j in zeros)
        key = tuple(coords)
        assert key not in seen
        seen.add(key)

    summary = d["summary"]
    n = len(cands)
    assert summary["total_primitive_known140_nonnegative_candidate_count"] == n
    assert summary["degree10_primitive_known140_nonnegative_candidate_count"] == (n if e == 10 else 0)
    assert summary["degree12_primitive_known140_nonnegative_candidate_count"] == (n if e == 12 else 0)
    assert summary["fibration_improvement_shells_numerically_empty_candidate"] == (n == 0)
    assert summary["geometric_effectivity_or_semiampleness_proved"] is False
    assert summary["global_min_P_dot_F_40_proved"] is False
    assert all(v is False for v in d["credit_firewall"].values())

    print(json.dumps({
        "success": True,
        "shell_index": args.shell_index,
        "canonical": claimed,
        "candidate_count": n,
        "raw_affine_close_vector_count": sh["raw_affine_close_vector_count"],
        "integral_picard_class_count": sh["integral_picard_class_count"],
        "known140_nonnegative_count": sh["known140_nonnegative_count"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
