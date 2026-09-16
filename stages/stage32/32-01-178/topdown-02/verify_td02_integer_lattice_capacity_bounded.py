#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import types
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

LOCKS = {
    "integer_kernel": (
        "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_integer_lattice_kernel.py",
        "d51a8edbfc4fb2c8e46dc9ea788ca43a7587f054",
    ),
    "bounded_exact": (
        "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_bc_envelope_bounded.py",
        "3ce709a2afe9d1acb573cb7c4c1b2e7bff4b53ae",
    ),
    "kernel_checkpoint": (
        "stages/stage32/32-01-178/topdown-02/TD02-GRF04-INTEGER-LATTICE-KERNEL-CHECKPOINT.json",
        "9f18fe769d3312c15dc719c0a51814bf8d4c170b",
    ),
}

HMAX = 16
ENVELOPE = 11_531_305_094_786
EXPECTED_PREFIX_H4 = 24_010
EXPECTED_PREFIX_H16 = 1_264_565_349

EXPECTED_REAL_NUM = 131_821_350_753_414
EXPECTED_REAL_DEN = 331
EXPECTED_REAL_FLOOR = 398_251_814_964
EXPECTED_REAL_REM = 330
EXPECTED_REAL_POS_CAP = 35_873_480_533_857
EXPECTED_REAL_BINS = 2_003
EXPECTED_REAL_USED_BINS = 1_222
EXPECTED_REAL_CUTOFF = (8, 331, 619_202_155, 42_915_879_806)

EXPECTED_INT_NUM = 82_515_979_091_245
EXPECTED_INT_DEN = 209
EXPECTED_INT_FLOOR = 394_813_297_087
EXPECTED_INT_REM = 62
EXPECTED_INT_POS_CAP = 35_586_230_187_107
EXPECTED_INT_BINS = 1_852
EXPECTED_INT_USED_BINS = 1_070
EXPECTED_INT_CUTOFF = (5, 209, 14_149_900_971, 79_016_894_385)

EXPECTED_IMPROVEMENT_NUM = 237_873_228_261_431
EXPECTED_IMPROVEMENT_DEN = 69_179
EXPECTED_FLOOR_IMPROVEMENT = 3_438_517_877


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def checked_raw(rel: str, expected: str) -> bytes:
    p = ROOT / rel
    req(p.is_file(), f"missing source {rel}")
    raw = p.read_bytes()
    req(git_blob(raw) == expected, f"source drift {rel}")
    return raw


def load_module(name: str, rel: str, raw: bytes):
    mod = types.ModuleType(name)
    mod.__file__ = str(ROOT / rel)
    exec(compile(raw, str(ROOT / rel), "exec"), mod.__dict__)
    return mod


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def count_parity_upto(limit: int, parity: int) -> int:
    if limit < parity:
        return 0
    return (limit - parity) // 2 + 1


def build_bc_counts() -> list[list[int]]:
    B = [[0, 0] for _ in range(HMAX + 1)]
    C = [[0, 0] for _ in range(HMAX + 1)]
    for m in range(HMAX + 1):
        for x9 in range(m + 1):
            B[m][x9 & 1] += 1
        for x8 in range(m + 1):
            for x10 in range(m - x8 + 1):
                C[m][(x8 + x10) & 1] += 1

    pb = [[0] * (HMAX + 1) for _ in range(2)]
    for p in (0, 1):
        total = 0
        for m in range(HMAX + 1):
            total += B[m][p]
            pb[p][m] = total

    def sum_b(p: int, lo: int, hi: int) -> int:
        if lo > hi:
            return 0
        return pb[p][hi] - (pb[p][lo - 1] if lo else 0)

    eq_first = [[[0] * (HMAX + 1) for _ in range(HMAX + 1)] for __ in range(2)]
    eq_second = [[[0] * (HMAX + 1) for _ in range(HMAX + 1)] for __ in range(2)]
    for tp in (0, 1):
        for rb in range(HMAX + 1):
            for rc in range(HMAX + 1):
                total = 0
                for delta in range(1, rc + 1):
                    last_x5 = min(rb, rc - delta)
                    p = (tp + rb + delta) & 1
                    top = rc - delta
                    total += sum_b(p, top - last_x5, top)
                eq_first[tp][rb][rc] = total

                need_x10 = (tp + rb) & 1
                total = 0
                for u in range(min(rb, rc) + 1):
                    x9 = rb - u
                    rem = rc - u
                    limit_x6 = min(x9, rem)
                    need_x6 = (rem - need_x10) & 1
                    total += count_parity_upto(limit_x6, need_x6)
                eq_second[tp][rb][rc] = total

    bc = [[0] * (HMAX + 1) for _ in range(HMAX + 1)]
    for x0 in range(HMAX + 1):
        for x1 in range(x0 + 1, HMAX + 1):
            px1 = x1 & 1
            for b in range(x1, HMAX + 1):
                g2 = b - x1
                b0, b1 = B[g2]
                for c in range(x0, HMAX + 1):
                    c0, c1 = C[c - x0]
                    bc[b][c] += b0 * (c1 if px1 else c0) + b1 * (c0 if px1 else c1)

    for t in range(HMAX + 1):
        tp = t & 1
        for b in range(t, HMAX + 1):
            rb = b - t
            for c in range(t, HMAX + 1):
                rc = c - t
                bc[b][c] += eq_first[tp][rb][rc] + eq_second[tp][rb][rc]
    return bc


def real_f0(h: int, g: int, b: int, c: int, x4: int) -> int:
    D = h - 2 * x4
    d = 2 * h
    r4 = (3 * d * d + 48 * d + 96 - 96 * g) // 4
    return 3 * (
        6 * D * D - 8 * D * b - 6 * D * c
        + 18 * b * b + 4 * b * c + 13 * c * c
    ) - 23 * r4


def real_survivor_caps(h: int, g: int, b: int, c: int) -> list[int]:
    n_min = 8 * h
    out = []
    for a in range(h + 1):
        raw = sum(
            real_f0(h, g, b, c, x4) + 46 * a * a <= 0
            for x4 in range(n_min + 1)
        )
        out.append((raw + 1) // 2)
    return out


def integer_survivor_caps(kernel, h: int, g: int, b: int, c: int) -> list[int]:
    d = 2 * h
    n_min = 8 * h
    r4 = (3 * d * d + 48 * d + 96 - 96 * g) // 4
    diff_even = [0] * (h + 2)
    diff_odd = [0] * (h + 2)
    q3 = [6 * kernel.qmin3(a) for a in range(h + 1)]

    @lru_cache(maxsize=None)
    def bcmin(D: int) -> int:
        return kernel.integer_bc_grf_min(b, c, D)

    for x4 in range(n_min + 1):
        D = h - 2 * x4
        room = r4 - bcmin(D)
        if room < 0:
            continue
        lo, hi = 0, h
        if q3[0] > room:
            continue
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if q3[mid] <= room:
                lo = mid
            else:
                hi = mid - 1
        amax = lo
        diff = diff_even if (x4 & 1) == 0 else diff_odd
        diff[0] += 1
        diff[amax + 1] -= 1

    ce = co = 0
    out = []
    for a in range(h + 1):
        ce += diff_even[a]
        co += diff_odd[a]
        out.append(max(ce, co))
    return out


def build_bins(kernel, bc: list[list[int]], mode: str):
    bins: dict[tuple[int, int], int] = defaultdict(int)
    rows = []
    for g in (0, 1):
        for h in range(4, HMAX + 1):
            d = 2 * h
            legacy = 8 if g == 0 else 4
            K = ceil_div(d - 16 * g + 16, 4)
            e_lower = max(legacy, K, d - 4 * g + 4)
            if e_lower & 1:
                e_lower += 1
            e_upper = 3 * d

            hist = [[0] * (3 * h + 1) for _ in range(h + 2)]
            for b in range(h + 1):
                for c in range(h + 1):
                    bc_count = bc[b][c]
                    if not bc_count:
                        continue
                    caps = (
                        integer_survivor_caps(kernel, h, g, b, c)
                        if mode == "integer"
                        else real_survivor_caps(h, g, b, c)
                    )
                    for a, s in enumerate(caps):
                        if not s:
                            continue
                        req(s < len(hist), f"survivor histogram overflow {(mode,g,h,b,c,a,s)}")
                        a_count = (a + 1) * (a + 2) // 2
                        hist[s][a + b + c] += a_count * bc_count

            row_capacity = 0
            row_full_survivors = 0
            for s in range(1, len(hist)):
                row = hist[s]
                if not any(row):
                    continue
                prefix = []
                acc = 0
                for value in row:
                    acc += value
                    prefix.append(acc)
                for e in range(e_lower, e_upper + 1, 2):
                    if g == 1 and d == 8 and e == 8:
                        continue
                    weight = prefix[min(e, 3 * h)]
                    if not weight:
                        continue
                    B = 19 * d - 5 * e + 1
                    req(B > 0, f"normal block {(g,d,e)}")
                    capacity = weight * B
                    bins[(s, B)] += capacity
                    row_capacity += capacity
                    row_full_survivors += weight * s
            rows.append({
                "g": g,
                "d": d,
                "positive_survivor_capacity": row_capacity,
                "full_capacity_survivor_sum": row_full_survivors,
            })
    return bins, rows


def solve_fractional_lp(bins: dict[tuple[int, int], int], envelope: int):
    items = sorted(
        ((Fraction(s, B), cap, s, B) for (s, B), cap in bins.items()),
        key=lambda z: z[0],
        reverse=True,
    )
    remaining = envelope
    value = Fraction(0, 1)
    used_bins = 0
    cutoff = None
    for ratio, capacity, s, B in items:
        if remaining <= 0:
            break
        take = min(remaining, capacity)
        value += ratio * take
        remaining -= take
        used_bins += 1
        if take < capacity:
            cutoff = (s, B, take, capacity)
            break
    req(remaining == 0, "positive-ratio capacity does not cover bounded HPADJ08 envelope")
    req(cutoff is not None, "missing LP cutoff")
    return {
        "value": value,
        "upper_floor": value.numerator // value.denominator,
        "remainder": value.numerator % value.denominator,
        "positive_capacity": sum(bins.values()),
        "bin_count": len(items),
        "used_bin_count": used_bins,
        "cutoff": cutoff,
    }


def row_sha(rows) -> str:
    h = hashlib.sha256()
    for row in rows:
        h.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode() + b"\n")
    return h.hexdigest()


def main() -> None:
    raws = {name: checked_raw(rel, sha) for name, (rel, sha) in LOCKS.items()}
    kernel = load_module("td02_integer_kernel", LOCKS["integer_kernel"][0], raws["integer_kernel"])
    bounded = load_module("td02_bounded_exact", LOCKS["bounded_exact"][0], raws["bounded_exact"])

    for _name, (rel, sha) in kernel.LOCKS.items():
        checked_raw(rel, sha)

    checkpoint = json.loads(raws["kernel_checkpoint"])
    req(checkpoint["ci_evidence"]["run_id"] == 35045220415, "kernel CI run")
    req(checkpoint["ci_evidence"]["job_id"] == 104633469055, "kernel CI job")
    req(checkpoint["ci_evidence"]["conclusion"] == "SUCCESS", "kernel CI conclusion")
    req(bounded.EXPECTED_HPADJ08_SURVIVORS == ENVELOPE, "bounded HPADJ08 envelope identity")

    bc = build_bc_counts()

    def prefix_total(h: int) -> int:
        ac = sum((a + 1) * (a + 2) // 2 for a in range(h + 1))
        bcc = sum(bc[b][c] for b in range(h + 1) for c in range(h + 1))
        return ac * bcc

    req(prefix_total(4) == EXPECTED_PREFIX_H4, "h4 prefix fixture")
    req(prefix_total(16) == EXPECTED_PREFIX_H16, "h16 prefix fixture")

    real_bins, real_rows = build_bins(kernel, bc, "real")
    int_bins, int_rows = build_bins(kernel, bc, "integer")
    real_lp = solve_fractional_lp(real_bins, ENVELOPE)
    int_lp = solve_fractional_lp(int_bins, ENVELOPE)

    req(real_lp["value"] == Fraction(EXPECTED_REAL_NUM, EXPECTED_REAL_DEN), f"real LP drift {real_lp['value']}")
    req(real_lp["upper_floor"] == EXPECTED_REAL_FLOOR, "real floor")
    req(real_lp["remainder"] == EXPECTED_REAL_REM, "real remainder")
    req(real_lp["positive_capacity"] == EXPECTED_REAL_POS_CAP, "real positive capacity")
    req(real_lp["bin_count"] == EXPECTED_REAL_BINS, "real bin count")
    req(real_lp["used_bin_count"] == EXPECTED_REAL_USED_BINS, "real used bins")
    req(real_lp["cutoff"] == EXPECTED_REAL_CUTOFF, f"real cutoff {real_lp['cutoff']}")

    req(int_lp["value"] == Fraction(EXPECTED_INT_NUM, EXPECTED_INT_DEN), f"integer LP drift {int_lp['value']}")
    req(int_lp["upper_floor"] == EXPECTED_INT_FLOOR, "integer floor")
    req(int_lp["remainder"] == EXPECTED_INT_REM, "integer remainder")
    req(int_lp["positive_capacity"] == EXPECTED_INT_POS_CAP, "integer positive capacity")
    req(int_lp["bin_count"] == EXPECTED_INT_BINS, "integer bin count")
    req(int_lp["used_bin_count"] == EXPECTED_INT_USED_BINS, "integer used bins")
    req(int_lp["cutoff"] == EXPECTED_INT_CUTOFF, f"integer cutoff {int_lp['cutoff']}")

    improvement = real_lp["value"] - int_lp["value"]
    req(improvement == Fraction(EXPECTED_IMPROVEMENT_NUM, EXPECTED_IMPROVEMENT_DEN), f"improvement drift {improvement}")
    req(EXPECTED_INT_FLOOR < EXPECTED_REAL_FLOOR, "no strict bounded LP gain")
    req(EXPECTED_REAL_FLOOR - EXPECTED_INT_FLOOR == EXPECTED_FLOOR_IMPROVEMENT, "floor improvement")

    result = {
        "schema": "STAGE32_32_01_178_TD02_INTEGER_LATTICE_CAPACITY_BOUNDED_V1",
        "status": "RESEARCH_ONLY_BOUNDED_EXACT_REGRESSION__NO_MAIN_CREDIT",
        "domain": {"g": [0, 1], "d_even": [8, 32], "hmax": HMAX},
        "bounded_hpadj08_x4_complete_envelope": ENVELOPE,
        "real_v35_semantics_bounded_lp": {
            "exact_value_num": real_lp["value"].numerator,
            "exact_value_den": real_lp["value"].denominator,
            "upper_floor": real_lp["upper_floor"],
            "remainder": real_lp["remainder"],
            "positive_capacity": real_lp["positive_capacity"],
            "bin_count": real_lp["bin_count"],
            "used_bin_count": real_lp["used_bin_count"],
            "cutoff": list(real_lp["cutoff"]),
            "row_stream_sha256": row_sha(real_rows),
        },
        "integer_lattice_bounded_lp": {
            "exact_value_num": int_lp["value"].numerator,
            "exact_value_den": int_lp["value"].denominator,
            "upper_floor": int_lp["upper_floor"],
            "remainder": int_lp["remainder"],
            "positive_capacity": int_lp["positive_capacity"],
            "bin_count": int_lp["bin_count"],
            "used_bin_count": int_lp["used_bin_count"],
            "cutoff": list(int_lp["cutoff"]),
            "row_stream_sha256": row_sha(int_rows),
        },
        "strict_gain": {
            "exact_num": improvement.numerator,
            "exact_den": improvement.denominator,
            "floor_upper_improvement": EXPECTED_FLOOR_IMPROVEMENT,
        },
        "semantics": {
            "allocation": "EXACT_CONTINUOUS_FRACTIONAL_CAPACITY_LP_BY_DESCENDING_EXACT_RATIONAL_s_over_B",
            "integer_strengthening": "AUDITED_INTEGER_NONNEGATIVE_(u,t)_GRF04_LOWER_BOUND_PLUS_EXACT_qmin3(a)",
            "completion_character": "FOR_EACH_AGGREGATE_PREFIX_USE_MAX(EVEN_X4_COUNT,ODD_X4_COUNT);_SAFE_WITHOUT_CONTIGUITY",
            "population": "BOUNDED_d<=32_REGRESSION_ONLY_NOT_FULL178",
            "composition": "INDEPENDENT_UPPER_BOUND_ONLY__NO_ADDITIVE_STACKING",
        },
        "external_main_reference": {
            "pr": 1808,
            "candidate_audited_exact_head": "6489e1fb9f35b8ecdc19c982301a816d956711e9",
            "candidate_blob_sha1": "1d669114e930951b9d5f9f82a6abb2b59cd43884",
            "v35_current_authority_bound_snapshot": 195_603_649_074_545_538_415,
            "authority_or_credit_inherited": False,
        },
        "source_blobs": {name: sha for name, (_rel, sha) in LOCKS.items()},
        "next_route": {
            "id": "TD02-INTEGER-LATTICE-CAPACITY-FULL178-SCALEOUT",
            "gate": "HOSTILE_AUDIT_OR_EXPLICIT_MAINBATCH_CONTINUATION_AFTER_BOUNDED_RESULT",
            "heavy_compute_armed": False,
        },
        "credit": {
            "main": False,
            "theorem": False,
            "effectivity": False,
            "receiver": False,
            "endpoint": False,
            "stage32_closed": False,
            "perfect_cuboid_existence": False,
            "perfect_cuboid_nonexistence": False,
            "merge": False,
        },
        "rows": {"real": real_rows, "integer": int_rows},
    }
    result["canonical_sha256_without_this_field"] = hashlib.sha256(
        json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    out = HERE / "TD02-INTEGER-LATTICE-CAPACITY-BOUNDED-RESULT.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "bounded_hpadj08_x4_complete_envelope": ENVELOPE,
        "real_lp_exact": f"{real_lp['value'].numerator}/{real_lp['value'].denominator}",
        "real_lp_upper_floor": real_lp["upper_floor"],
        "integer_lp_exact": f"{int_lp['value'].numerator}/{int_lp['value'].denominator}",
        "integer_lp_upper_floor": int_lp["upper_floor"],
        "floor_upper_improvement": EXPECTED_FLOOR_IMPROVEMENT,
        "integer_over_real_approx": float(int_lp["value"] / real_lp["value"]),
        "canonical_sha256_without_this_field": result["canonical_sha256_without_this_field"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
