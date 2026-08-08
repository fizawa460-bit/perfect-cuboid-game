#!/usr/bin/env python3
from __future__ import annotations

import bisect
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

OUT = Path("stages/stage14/data/14-e9/gcd_lcm_local_statistics.json")
CUTOFFS = [2000, 10000, 50000, 200000]
CUTOFF_SQUARES = [B * B for B in CUTOFFS]
PRIMES = [2, 3, 5, 7, 11, 13]
LOCKED_E2 = {
    2000: (4833, 4812, (1342, 2136, 1334), 7),
    10000: (41720, 41666, (12464, 18198, 11004), 18),
    50000: (331857, 331731, (103892, 142403, 85436), 42),
    200000: (1896751, 1896505, (612678, 805875, 477952), 82),
}
RATIO_KEYS = ["1", "[1/2,1)", "[1/10,1/2)", "[1/100,1/10)", "[1/1000,1/100)", "<1/1000"]
LOCAL_STATES = ["none", "G", "U", "V", "GU", "GV"]


def is_square(n: int) -> bool:
    r = math.isqrt(n)
    return r * r == n


def pythagorean_neighbors(hyp_limit: int):
    nbr = defaultdict(set)
    m = 2
    while m * m + 1 <= hyp_limit:
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            a, b, h = m * m - n * n, 2 * m * n, m * m + n * n
            if h > hyp_limit:
                continue
            for k in range(1, hyp_limit // h + 1):
                A, C = k * a, k * b
                nbr[A].add(C)
                nbr[C].add(A)
        m += 1
    return nbr


def direction(e: int, x: int, y: int) -> str:
    assert x < y
    if e < x:
        return "a"
    if e < y:
        return "b"
    return "c"


def ratio_bin(g: int, e: int) -> str:
    if g == e:
        return "1"
    if 2 * g >= e:
        return "[1/2,1)"
    if 10 * g >= e:
        return "[1/10,1/2)"
    if 100 * g >= e:
        return "[1/100,1/10)"
    if 1000 * g >= e:
        return "[1/1000,1/100)"
    return "<1/1000"


def local_state(g: int, u: int, v: int, p: int) -> str:
    G = g % p == 0
    U = u % p == 0
    V = v % p == 0
    assert not (U and V)
    state = ("G" if G else "") + ("U" if U else "") + ("V" if V else "")
    assert state in LOCAL_STATES or state == ""
    return state or "none"


def empty_bucket():
    return {
        "raw_total": 0,
        "exactly_two_total": 0,
        "third_square_incidence_count": 0,
        "raw_directions": Counter(),
        "exact_directions": Counter(),
        "exact_g_counts": Counter(),
        "third_g_counts": Counter(),
        "raw_ratio_bins": Counter(),
        "exact_ratio_bins": Counter(),
        "third_ratio_bins": Counter(),
        "raw_local": {p: Counter() for p in PRIMES},
        "exact_local": {p: Counter() for p in PRIMES},
        "third_local": {p: Counter() for p in PRIMES},
        "p2_G_blocked": 0,
        "p3_G_blocked": 0,
        "p2_or_p3_G_blocked": 0,
        "third_square_blocked": 0,
    }


def add_bucket(dst, src):
    for key in ("raw_total", "exactly_two_total", "third_square_incidence_count", "p2_G_blocked", "p3_G_blocked", "p2_or_p3_G_blocked", "third_square_blocked"):
        dst[key] += src[key]
    for key in ("raw_directions", "exact_directions", "exact_g_counts", "third_g_counts", "raw_ratio_bins", "exact_ratio_bins", "third_ratio_bins"):
        dst[key].update(src[key])
    for p in PRIMES:
        dst["raw_local"][p].update(src["raw_local"][p])
        dst["exact_local"][p].update(src["exact_local"][p])
        dst["third_local"][p].update(src["third_local"][p])


def census():
    Bmax = CUTOFFS[-1]
    nbr = pythagorean_neighbors(Bmax)
    buckets = [empty_bucket() for _ in CUTOFFS]
    directional_max = {q: {"raw_count": 0, "exact_count": 0, "g_eq_1": 0, "g_counts": Counter(), "exact_ratio_bins": Counter(), "p2_or_p3_G_blocked": 0} for q in "abc"}

    for e, others in nbr.items():
        vals = sorted(others)
        gcd_with_e = {z: math.gcd(e, z) for z in vals}
        for i, x in enumerate(vals):
            ex = e * e + x * x
            if ex >= CUTOFF_SQUARES[-1]:
                continue
            y_max = math.isqrt(CUTOFF_SQUARES[-1] - ex)
            dx = gcd_with_e[x]
            for y in vals[i + 1 :]:
                if y > y_max:
                    break
                if math.gcd(dx, y) != 1:
                    continue
                h2 = ex + y * y
                bucket_index = bisect.bisect_left(CUTOFF_SQUARES, h2)
                if bucket_index == len(CUTOFFS):
                    continue

                dy = gcd_with_e[y]
                u, v = dx, dy
                assert math.gcd(u, v) == 1
                assert e % (u * v) == 0
                g = e // (u * v)
                S1, S2 = e // u, e // v
                assert math.gcd(S1, S2) == g
                assert S1 == g * v
                assert S2 == g * u
                assert math.lcm(S1, S2) == e

                q = direction(e, x, y)
                rb = ratio_bin(g, e)
                states = {p: local_state(g, u, v, p) for p in PRIMES}
                blocker2 = states[2] == "G"
                blocker3 = states[3] == "G"
                blocked = blocker2 or blocker3

                b = buckets[bucket_index]
                b["raw_total"] += 1
                b["raw_directions"][q] += 1
                b["raw_ratio_bins"][rb] += 1
                for p in PRIMES:
                    b["raw_local"][p][states[p]] += 1
                b["p2_G_blocked"] += int(blocker2)
                b["p3_G_blocked"] += int(blocker3)
                b["p2_or_p3_G_blocked"] += int(blocked)

                d = directional_max[q]
                d["raw_count"] += 1
                d["p2_or_p3_G_blocked"] += int(blocked)

                if is_square(x * x + y * y):
                    b["third_square_incidence_count"] += 1
                    b["third_g_counts"][g] += 1
                    b["third_ratio_bins"][rb] += 1
                    for p in PRIMES:
                        b["third_local"][p][states[p]] += 1
                    b["third_square_blocked"] += int(blocked)
                    # p=2 state G => e even and x,y odd, so x^2+y^2=2 mod 4.
                    # p=3 state G => 3|e and 3 does not divide x*y, so x^2+y^2=2 mod 3.
                    assert not blocked
                    continue

                b["exactly_two_total"] += 1
                b["exact_directions"][q] += 1
                b["exact_g_counts"][g] += 1
                b["exact_ratio_bins"][rb] += 1
                for p in PRIMES:
                    b["exact_local"][p][states[p]] += 1
                d["exact_count"] += 1
                d["g_eq_1"] += int(g == 1)
                d["g_counts"][g] += 1
                d["exact_ratio_bins"][rb] += 1

    cumulative = empty_bucket()
    rows = []
    for B, b in zip(CUTOFFS, buckets):
        add_bucket(cumulative, b)
        expected_raw, expected_exact, expected_dirs, expected_bricks = LOCKED_E2[B]
        exact_dirs = tuple(cumulative["exact_directions"][q] for q in "abc")
        assert (cumulative["raw_total"], cumulative["exactly_two_total"], exact_dirs) == (expected_raw, expected_exact, expected_dirs)
        assert cumulative["third_square_incidence_count"] == 3 * expected_bricks
        assert cumulative["raw_total"] - cumulative["exactly_two_total"] == cumulative["third_square_incidence_count"]
        assert cumulative["third_square_blocked"] == 0
        rows.append({
            "B": B,
            "raw_total": cumulative["raw_total"],
            "exactly_two_total": cumulative["exactly_two_total"],
            "third_square_incidence_count": cumulative["third_square_incidence_count"],
            "euler_brick_object_count": expected_bricks,
            "raw_directional": [cumulative["raw_directions"][q] for q in "abc"],
            "exactly_two_directional": list(exact_dirs),
            "distinct_exact_g_values": len(cumulative["exact_g_counts"]),
            "exact_g_eq_1": cumulative["exact_g_counts"][1],
            "top_exact_g": [[g, c] for g, c in cumulative["exact_g_counts"].most_common(12)],
            "top_third_square_g": [[g, c] for g, c in cumulative["third_g_counts"].most_common(12)],
            "exact_g_over_lcm_bins": {k: cumulative["exact_ratio_bins"][k] for k in RATIO_KEYS},
            "completion_by_g_over_lcm_bin": {k: {"raw": cumulative["raw_ratio_bins"][k], "third_square": cumulative["third_ratio_bins"][k]} for k in RATIO_KEYS},
            "local_prime_support_exact": {str(p): {s: cumulative["exact_local"][p][s] for s in LOCAL_STATES} for p in PRIMES},
            "local_prime_support_third_square": {str(p): {s: cumulative["third_local"][p][s] for s in LOCAL_STATES} for p in PRIMES},
            "rigorous_local_blockers": {
                "p2_state_G": cumulative["p2_G_blocked"],
                "p3_state_G": cumulative["p3_G_blocked"],
                "p2_or_p3_state_G_union": cumulative["p2_or_p3_G_blocked"],
                "third_square_incidence_in_union": cumulative["third_square_blocked"],
            },
        })

    directional_report = {}
    for q in "abc":
        d = directional_max[q]
        directional_report[q] = {
            "raw_count": d["raw_count"],
            "exact_count": d["exact_count"],
            "g_eq_1": d["g_eq_1"],
            "top_exact_g": [[g, c] for g, c in d["g_counts"].most_common(8)],
            "exact_g_over_lcm_bins": {k: d["exact_ratio_bins"][k] for k in RATIO_KEYS},
            "p2_or_p3_state_G_blocked": d["p2_or_p3_G_blocked"],
        }
    return rows, directional_report


def main():
    rows, directional = census()
    report = {
        "metadata": {"stage": "14-e9", "track": "gcd/lcm and finite-local control after e8", "height": "D_R=sqrt(e^2+x^2+y^2)<=B", "max_B": CUTOFFS[-1], "uses_stage14_e8_gap": True},
        "exact_reconstruction": {
            "u": "gcd(e,x)=beta=S2/g", "v": "gcd(e,y)=alpha=S1/g", "coprime": "gcd(u,v)=1", "g": "e/(u*v)=gcd(S1,S2)", "S1": "e/u=g*v", "S2": "e/v=g*u", "lcm": "lcm(S1,S2)=e",
            "prime_state_meaning": {"none": "vp(S1)=vp(S2)=0", "U": "vp(S2)>0=vp(S1)", "V": "vp(S1)>0=vp(S2)", "G": "vp(S1)=vp(S2)>0", "GU": "vp(S2)>vp(S1)>0", "GV": "vp(S1)>vp(S2)>0"},
            "impossible_support_states": ["UV", "GUV"],
        },
        "rigorous_completion_blockers": {
            "p2_G": "state G at p=2 implies e even and x,y odd, hence x^2+y^2=2 mod 4 is not a square",
            "p3_G": "state G at p=3 implies 3|e and 3 does not divide x*y, hence x^2+y^2=2 mod 3 is not a square",
            "scope": "necessary local blockers for the third-face-square/Euler-brick completion",
        },
        "cutoffs": rows,
        "directional_at_max_B": directional,
        "interpretation_boundary": {"finite_g_distribution_only": True, "limiting_g_distribution_proved": False, "prime_state_independence_proved": False, "fixed_relative_euler_brick_saving_from_e9_proved": False, "novelty_by_search_absence": False},
        "status": {
            "STAGE14_E9": "COMPLETE_GCD_LCM_LOCAL_CONTROL_AND_2_3_BLOCKERS",
            "EXACT_GCD_LCM_INVERSE_LOCKED": True,
            "LOCAL_PRIME_STATE_DECOMPOSITION_LOCKED": True,
            "P2_STATE_G_EULER_COMPLETION_BLOCKED": True,
            "P3_STATE_G_EULER_COMPLETION_BLOCKED": True,
            "FINITE_CENSUS_REGENERATES_E2_LOCKS": True,
            "MAX_LOCAL_AUDIT_B": CUTOFFS[-1],
            "ASYMPTOTIC_GCD_LCM_DISTRIBUTION_PROVED": False,
            "FIXED_RELATIVE_EULER_BRICK_SAVING_PROVED": False,
            "NEXT_E9_REFINEMENT": "explicit adelic masses and stronger residue-state sieve if needed",
        },
        "pass": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
