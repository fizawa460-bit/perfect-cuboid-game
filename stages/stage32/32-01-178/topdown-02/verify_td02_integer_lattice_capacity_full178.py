#!/usr/bin/env python3
from __future__ import annotations

import bisect
import hashlib
import json
import types
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

LOCKS = {
    "integer_kernel": (
        "stages/stage32/32-01-178/topdown-02/verify_td02_grf04_integer_lattice_kernel.py",
        "d51a8edbfc4fb2c8e46dc9ea788ca43a7587f054",
    ),
    "bounded_capacity": (
        "stages/stage32/32-01-178/topdown-02/verify_td02_integer_lattice_capacity_bounded.py",
        "ce9be3fa28c68f8f3f06177a0dc72ca7a107b14a",
    ),
    "bounded_checkpoint": (
        "stages/stage32/32-01-178/topdown-02/TD02-INTEGER-LATTICE-CAPACITY-BOUNDED-CHECKPOINT.json",
        "5dd8f37b3c46f3dc7c89ce3c915dc6b327b674b3",
    ),
    "td01_envelope": (
        "stages/stage32/32-01-178/topdown-01/EXACT-X4-ENVELOPE-BOUND.json",
        "51271c11078459ad9171138c4fb6121d7a665c39",
    ),
}

FULL_HMAX = 96
D_MIN = -15 * FULL_HMAX
D_MAX = FULL_HMAX
EXPECTED_F_CONVEX_INTERIORS = 893_856
EXPECTED_PREFIX_H4 = 24_010
EXPECTED_PREFIX_H16 = 1_264_565_349
EXPECTED_PREFIX_H96 = 27_398_914_615_401_945
BOUNDED_ENVELOPE = 11_531_305_094_786
BOUNDED_EXPECTED_FLOOR = 394_813_297_087
FULL_ENVELOPE = 6_703_403_803_993_209_250_491
LIVE_MAIN_V36_SNAPSHOT = 195_603_649_074_545_538_415


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def checked_raw(rel: str, expected: str) -> bytes:
    path = ROOT / rel
    req(path.is_file(), f"missing source {rel}")
    raw = path.read_bytes()
    req(git_blob(raw) == expected, f"source drift {rel}")
    return raw


def load_module(name: str, rel: str, raw: bytes):
    mod = types.ModuleType(name)
    mod.__file__ = str(ROOT / rel)
    exec(compile(raw, str(ROOT / rel), "exec"), mod.__dict__)
    return mod


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def prefix_total(bc: list[list[int]], h: int) -> int:
    ac = sum((a + 1) * (a + 2) // 2 for a in range(h + 1))
    bcc = sum(bc[b][c] for b in range(h + 1) for c in range(h + 1))
    return ac * bcc


def fixed_t_profile(kernel, b: int, c: int) -> list[int]:
    return [kernel.fixed_t_min_fast(b, c, t) for t in range(b + c + 1)]


def check_fixed_t_convexity(kernel) -> dict[str, int]:
    interiors = 0
    min_second = None
    strict = 0
    for b in range(FULL_HMAX + 1):
        for c in range(FULL_HMAX + 1):
            f = fixed_t_profile(kernel, b, c)
            for t in range(1, len(f) - 1):
                second = f[t - 1] - 2 * f[t] + f[t + 1]
                req(second >= 1, f"fixed-t discrete convexity {(b,c,t,second)}")
                interiors += 1
                strict += int(second > 0)
                min_second = second if min_second is None else min(min_second, second)
    req(interiors == EXPECTED_F_CONVEX_INTERIORS, f"fixed-t interior count {interiors}")
    req(min_second == 1, f"fixed-t minimum second difference {min_second}")
    return {"interiors": interiors, "strict": strict, "min_second_difference": min_second}


def squared_infimal_profile(f: list[int], dmin: int, dmax: int) -> list[int]:
    """Exact min_t 6*f(t)+(D-t)^2 over every integer D in [dmin,dmax].

    The verified strict discrete convexity of f makes the adjacent difference
    in t strictly increasing. Therefore an argmin is monotone in D. We find the
    exact minimizer at the left endpoint by brute force once, then advance it
    monotonically. No terminal state is enumerated.
    """
    m = len(f) - 1
    six = [6 * v for v in f]

    def value(D: int, t: int) -> int:
        return six[t] + (D - t) * (D - t)

    t = min(range(m + 1), key=lambda z: value(dmin, z))
    out = []
    for D in range(dmin, dmax + 1):
        while t < m and value(D, t + 1) <= value(D, t):
            t += 1
        out.append(value(D, t))

    # Exact endpoint/center brute regressions for every (b,c) caller.
    for D in (dmin, 0, dmax):
        idx = D - dmin
        brute = min(value(D, z) for z in range(m + 1))
        req(out[idx] == brute, f"infimal profile brute regression {(D,out[idx],brute)}")
    return out


def profile_convexity(profile: list[int]) -> int:
    minimum = None
    for i in range(1, len(profile) - 1):
        second = profile[i - 1] - 2 * profile[i] + profile[i + 1]
        req(second >= 0, f"bcmin profile lost convexity {(i,second)}")
        minimum = second if minimum is None else min(minimum, second)
    return 0 if minimum is None else minimum


def interval_cap_from_convex_values(vals: list[int], threshold: int) -> int:
    """max(even-x4 count, odd-x4 count) on the exact convex sublevel set."""
    m = min(range(len(vals)), key=vals.__getitem__)
    if vals[m] > threshold:
        return 0
    left_neg = [-v for v in vals[: m + 1]]  # increasing
    right = vals[m:]                         # increasing
    L = bisect.bisect_left(left_neg, -threshold)
    R = m + bisect.bisect_right(right, threshold) - 1
    req(0 <= L <= m <= R < len(vals), f"sublevel interval {(L,m,R,len(vals))}")
    # A contiguous integer x4 interval contains parity classes differing by <=1.
    return (R - L + 2) // 2


def solve_exact_fractional_lp(bins: dict[tuple[int, int], int], envelope: int) -> dict:
    items = sorted(
        ((Fraction(s, B), cap, s, B) for (s, B), cap in bins.items()),
        key=lambda z: z[0],
        reverse=True,
    )
    remaining = envelope
    value = Fraction(0, 1)
    used = 0
    cutoff = None
    for ratio, capacity, s, B in items:
        if remaining <= 0:
            break
        take = min(remaining, capacity)
        value += ratio * take
        remaining -= take
        used += 1
        if take < capacity:
            cutoff = (s, B, take, capacity)
            break
    req(remaining == 0, "positive-ratio capacity does not cover envelope")
    req(cutoff is not None, "fractional LP cutoff missing")
    return {
        "value": value,
        "upper_floor": value.numerator // value.denominator,
        "remainder": value.numerator % value.denominator,
        "positive_capacity": sum(bins.values()),
        "bin_count": len(items),
        "used_bin_count": used,
        "cutoff": cutoff,
    }


def capacity_scaleout(kernel, bounded, *, HMAX: int, g_hmax: tuple[tuple[int, int], ...], envelope: int) -> dict:
    bounded.HMAX = HMAX
    bc = bounded.build_bc_counts()
    req(prefix_total(bc, 4) == EXPECTED_PREFIX_H4, "h4 canonical prefix fixture")
    if HMAX >= 16:
        req(prefix_total(bc, 16) == EXPECTED_PREFIX_H16, "h16 canonical prefix fixture")
    if HMAX == FULL_HMAX:
        req(prefix_total(bc, 96) == EXPECTED_PREFIX_H96, "h96 canonical prefix fixture")

    hists: dict[tuple[int, int], list[list[int]]] = {}
    for g, hmax in g_hmax:
        for h in range(4, hmax + 1):
            hists[(g, h)] = [[0] * (3 * h + 1) for _ in range(h + 2)]

    q3six = [6 * kernel.qmin3(a) for a in range(HMAX + 1)]
    profile_states = profile_second_states = aggregate_cells = nonzero_cells = 0
    profile_min_second = None

    dmin = -15 * HMAX
    dmax = HMAX
    for b in range(HMAX + 1):
        for c in range(HMAX + 1):
            bc_count = bc[b][c]
            if not bc_count:
                continue
            f = fixed_t_profile(kernel, b, c)
            profile = squared_infimal_profile(f, dmin, dmax)
            profile_states += len(profile)
            pmin = profile_convexity(profile)
            profile_second_states += max(0, len(profile) - 2)
            profile_min_second = pmin if profile_min_second is None else min(profile_min_second, pmin)

            h0 = max(4, b, c)
            for g, hmax in g_hmax:
                if h0 > hmax:
                    continue
                for h in range(h0, hmax + 1):
                    d = 2 * h
                    r4 = (3 * d * d + 48 * d + 96 - 96 * g) // 4
                    n_min = 8 * h
                    vals = [profile[h - 2 * x4 - dmin] for x4 in range(n_min + 1)]
                    hist = hists[(g, h)]
                    for a in range(h + 1):
                        aggregate_cells += 1
                        threshold = r4 - q3six[a]
                        cap = interval_cap_from_convex_values(vals, threshold)
                        if not cap:
                            continue
                        nonzero_cells += 1
                        req(cap < len(hist), f"survivor cap overflow {(g,h,a,b,c,cap)}")
                        a_count = (a + 1) * (a + 2) // 2
                        hist[cap][a + b + c] += a_count * bc_count

    bins: dict[tuple[int, int], int] = defaultdict(int)
    row_summaries = []
    for g, hmax in g_hmax:
        for h in range(4, hmax + 1):
            d = 2 * h
            legacy = 8 if g == 0 else 4
            K = ceil_div(d - 16 * g + 16, 4)
            e_lower = max(legacy, K, d - 4 * g + 4)
            if e_lower & 1:
                e_lower += 1
            e_upper = 3 * d
            hist = hists[(g, h)]
            row_capacity = 0
            active_bins = 0
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
                    active_bins += 1
            row_summaries.append({"g": g, "d": d, "positive_survivor_capacity": row_capacity, "active_bins": active_bins})

    lp = solve_exact_fractional_lp(bins, envelope)
    row_stream = hashlib.sha256()
    for row in row_summaries:
        row_stream.update(json.dumps(row, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    return {
        "HMAX": HMAX,
        "g_hmax": [list(v) for v in g_hmax],
        "envelope": envelope,
        "profile_states": profile_states,
        "profile_second_difference_states": profile_second_states,
        "profile_min_second_difference": profile_min_second,
        "aggregate_cells": aggregate_cells,
        "nonzero_aggregate_cells": nonzero_cells,
        "lp": lp,
        "row_stream_sha256": row_stream.hexdigest(),
    }


def serializable(result: dict) -> dict:
    out = dict(result)
    lp = dict(out["lp"])
    value = lp.pop("value")
    lp["exact_num"] = value.numerator
    lp["exact_den"] = value.denominator
    lp["cutoff"] = list(lp["cutoff"])
    out["lp"] = lp
    return out


def main() -> None:
    raws = {name: checked_raw(rel, sha) for name, (rel, sha) in LOCKS.items()}
    kernel = load_module("td02_integer_kernel", LOCKS["integer_kernel"][0], raws["integer_kernel"])
    bounded = load_module("td02_bounded_capacity", LOCKS["bounded_capacity"][0], raws["bounded_capacity"])

    checkpoint = json.loads(raws["bounded_checkpoint"])
    req(checkpoint["audit_boundary"]["prior_integer_kernel_hostile_audit"] == "PASS", "predecessor kernel audit")
    req(checkpoint["ci_evidence"]["run_id"] == 35047280381, "bounded CI run")
    req(checkpoint["ci_evidence"]["job_id"] == 104639749121, "bounded CI job")
    req(checkpoint["ci_evidence"]["conclusion"] == "SUCCESS", "bounded CI conclusion")
    req(checkpoint["result"]["integer_lattice_lp_exact"]["floor"] == BOUNDED_EXPECTED_FLOOR, "bounded checkpoint floor")

    td01 = json.loads(raws["td01_envelope"])
    deriv = td01["exact_envelope_derivation"]
    req(deriv["hpadj08_exact_square_survivor_envelope"] == FULL_ENVELOPE, "FULL178 envelope")
    req(deriv["x4_complete_after_hpadj08"] is True, "FULL178 x4-complete envelope")
    req(td01["parity_bound"]["required_character"] == "x4 == x0+x8+x10 (mod 2)", "completion character")

    convex = check_fixed_t_convexity(kernel)

    # First replay the hostile-audited d<=32 boundary through the new convex
    # interval engine. This is the exact regression gate before FULL178.
    bounded_fast = capacity_scaleout(
        kernel, bounded,
        HMAX=16,
        g_hmax=((0, 16), (1, 16)),
        envelope=BOUNDED_ENVELOPE,
    )
    req(bounded_fast["lp"]["upper_floor"] == BOUNDED_EXPECTED_FLOOR, f"bounded fast-engine floor {bounded_fast['lp']['upper_floor']}")
    req(bounded_fast["lp"]["value"] == Fraction(82_515_979_091_245, 209), "bounded fast-engine exact LP")

    full = capacity_scaleout(
        kernel, bounded,
        HMAX=FULL_HMAX,
        g_hmax=((0, 88), (1, 96)),
        envelope=FULL_ENVELOPE,
    )
    req(full["lp"]["upper_floor"] <= LIVE_MAIN_V36_SNAPSHOT, "FULL178 integer strengthening failed to improve/equal live V36 snapshot")

    result = {
        "schema": "STAGE32_32_01_178_TD02_INTEGER_LATTICE_CAPACITY_FULL178_V1",
        "scope": {
            "rows_total": 178,
            "g0_d_even": [8, 176],
            "g1_d_even": [8, 192],
            "terminal_enumeration": False,
        },
        "source_blobs": {name: sha for name, (_rel, sha) in LOCKS.items()},
        "convexity_certificate": convex,
        "bounded_replay": serializable(bounded_fast),
        "full178": serializable(full),
        "comparison": {
            "live_main_v36_snapshot": LIVE_MAIN_V36_SNAPSHOT,
            "full178_integer_lattice_upper_floor": full["lp"]["upper_floor"],
            "potential_tightening_vs_v36_snapshot": LIVE_MAIN_V36_SNAPSHOT - full["lp"]["upper_floor"],
            "composition": "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING",
            "main_authority_mutated": False,
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
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    (HERE / "TD02-INTEGER-LATTICE-CAPACITY-FULL178-RESULT.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({
        "fixed_t_convexity": convex,
        "bounded_replay_upper_floor": bounded_fast["lp"]["upper_floor"],
        "full178_upper_exact": f"{full['lp']['value'].numerator}/{full['lp']['value'].denominator}",
        "full178_upper_floor": full["lp"]["upper_floor"],
        "full178_remainder": full["lp"]["remainder"],
        "potential_tightening_vs_v36_snapshot": LIVE_MAIN_V36_SNAPSHOT - full["lp"]["upper_floor"],
        "full178_bin_count": full["lp"]["bin_count"],
        "full178_used_bin_count": full["lp"]["used_bin_count"],
        "full178_cutoff": list(full["lp"]["cutoff"]),
        "full178_profile_states": full["profile_states"],
        "full178_aggregate_cells": full["aggregate_cells"],
        "full178_row_stream_sha256": full["row_stream_sha256"],
        "canonical_sha256_without_this_field": result["canonical_sha256_without_this_field"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
