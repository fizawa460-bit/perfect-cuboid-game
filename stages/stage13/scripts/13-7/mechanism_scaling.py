#!/usr/bin/env python3
"""Stage13-7b: mechanism-resolved scaling through B=1,000,000.

Recompute the Stage13-3e representation-density diagnostics at 100k-spaced
cutoffs without retaining millions of incidence rows.  For each outer shell
S=(p,z,d), enumerate all positive unordered face representations x<y with
x^2+y^2=p^2, retain primitive strict-order incidences, and accumulate:

  raw            : one unit per surviving incidence,
  G-neutral      : weight 1/R_all(p),
  shell-neutral  : weight 1/R_prim(S),
  G-neutral OE/EE parity strata.

For ac/bc, define the exact finite multiplicative diagnostic chain

  r_raw = r_G * F_prim * F_shell,
  F_prim  = r_shell / r_G,
  F_shell = r_raw / r_shell.

This is a finite mechanism diagnostic, not an asymptotic factorization theorem.
"""
from __future__ import annotations

import argparse
import bisect
import json
import math
from collections import defaultdict
from pathlib import Path

BOUNDS = tuple(range(100_000, 1_000_001, 100_000))
OUT = Path("stages/stage13/data/13-7/mechanism_scaling_report.json")
STAGE7A = Path("stages/stage13/data/13-7/deviation_scaling_report.json")
CATS = ("ab", "ac", "bc")
LOCK_RAW_100K = (84_212, 43_236, 40_760)
LOCK_RAW_1M = (1_237_105, 636_722, 589_898)


def triples(B: int):
    for m in range(2, math.isqrt(B) + 1):
        mm = m * m
        for n in range(1, m):
            if (m - n) % 2 == 0 or math.gcd(m, n) != 1:
                continue
            u, v, w = mm - n * n, 2 * m * n, mm + n * n
            if w > B:
                continue
            if u > v:
                u, v = v, u
            for k in range(1, B // w + 1):
                yield k * u, k * v, k * w


def vector_stats(v):
    total = sum(v)
    p = [x / total for x in v]
    return {
        "weight": dict(zip(CATS, v)),
        "total_weight": total,
        "ratio_bc": {"ab": v[0] / v[2], "ac": v[1] / v[2], "bc": 1.0},
        "proportion": dict(zip(CATS, p)),
        "alpha": p[0] - 0.5,
        "beta": (p[1] - p[2]) / 2,
    }


def add_into(dst, src):
    for i in range(3):
        dst[i] += src[i]


def cancellation(oe, ee):
    gap_oe = oe[1] - oe[2]
    gap_ee = ee[1] - ee[2]
    gap_total = gap_oe + gap_ee
    if gap_oe * gap_ee < 0:
        efficiency = 1.0 - abs(gap_total) / (abs(gap_oe) + abs(gap_ee))
    else:
        efficiency = 0.0
    return {
        "OE_ac_minus_bc": gap_oe,
        "EE_ac_minus_bc": gap_ee,
        "total_ac_minus_bc": gap_total,
        "opposite_signs": gap_oe * gap_ee < 0,
        "cancellation_efficiency": efficiency,
    }


def enumerate_bands(bounds):
    Bmax = bounds[-1]
    mark = bytearray(Bmax + 1)
    triple_count = 0
    for u, v, _ in triples(Bmax):
        mark[u] = mark[v] = 1
        triple_count += 1

    faces = defaultdict(list)
    indexed_face_pairs = 0
    for x, y, p in triples(Bmax):
        if mark[p]:
            faces[p].append((x, y))
            indexed_face_pairs += 1

    raw = [[0, 0, 0] for _ in bounds]
    Gneutral = [[0.0, 0.0, 0.0] for _ in bounds]
    shellneutral = [[0.0, 0.0, 0.0] for _ in bounds]
    G_OE = [[0.0, 0.0, 0.0] for _ in bounds]
    G_EE = [[0.0, 0.0, 0.0] for _ in bounds]

    glued_records = 0
    supported_shells = 0
    primitive_raw_incidences = 0

    for u, v, d in triples(Bmax):
        band = bisect.bisect_left(bounds, d)
        for p, z in ((u, v), (v, u)):
            reps = faces.get(p)
            if not reps:
                continue
            R_all = len(reps)
            surviving = []
            for x, y in reps:
                glued_records += 1
                if math.gcd(math.gcd(x, y), z) != 1:
                    continue
                a, b, c = sorted((x, y, z))
                if not a < b < c:
                    continue
                if x == a and y == b:
                    cat = 0
                elif x == a and y == c:
                    cat = 1
                elif x == b and y == c:
                    cat = 2
                else:
                    pair = {x, y}
                    if pair == {a, b}:
                        cat = 0
                    elif pair == {a, c}:
                        cat = 1
                    elif pair == {b, c}:
                        cat = 2
                    else:
                        raise ArithmeticError(("category", x, y, z, a, b, c))
                parity = "OE" if ((x ^ y) & 1) else "EE"
                surviving.append((cat, parity))

            R_prim = len(surviving)
            if not R_prim:
                continue
            supported_shells += 1
            for cat, parity in surviving:
                primitive_raw_incidences += 1
                raw[band][cat] += 1
                Gneutral[band][cat] += 1.0 / R_all
                shellneutral[band][cat] += 1.0 / R_prim
                (G_OE if parity == "OE" else G_EE)[band][cat] += 1.0 / R_all

    return {
        "raw": raw,
        "G": Gneutral,
        "shell": shellneutral,
        "G_OE": G_OE,
        "G_EE": G_EE,
        "diagnostics": {
            "integer_pythagorean_triples": triple_count,
            "indexed_face_pairs": indexed_face_pairs,
            "supported_outer_shells": supported_shells,
            "glued_records_before_primitive_strict_order_filters": glued_records,
            "primitive_raw_incidences": primitive_raw_incidences,
        },
    }


def make_row(B, raw, G, shell, G_OE, G_EE):
    sr, sg, ss = vector_stats(raw), vector_stats(G), vector_stats(shell)
    soe, see = vector_stats(G_OE), vector_stats(G_EE)
    r_raw = sr["ratio_bc"]["ac"]
    r_G = sg["ratio_bc"]["ac"]
    r_shell = ss["ratio_bc"]["ac"]
    return {
        "B": B,
        "raw": sr,
        "G_neutral": sg,
        "shell_neutral": ss,
        "ac_bc_factor_chain": {
            "r_G": r_G,
            "F_prim": r_shell / r_G,
            "F_shell": r_raw / r_shell,
            "product": r_G * (r_shell / r_G) * (r_raw / r_shell),
            "r_raw": r_raw,
        },
        "G_neutral_parity": {
            "OE": soe,
            "EE": see,
            "pair_gap_cancellation": cancellation(G_OE, G_EE),
        },
        "coordinate_transitions": {
            "G_to_shell": {
                "delta_alpha": ss["alpha"] - sg["alpha"],
                "delta_beta": ss["beta"] - sg["beta"],
            },
            "shell_to_raw": {
                "delta_alpha": sr["alpha"] - ss["alpha"],
                "delta_beta": sr["beta"] - ss["beta"],
            },
        },
    }


def build_report(bounds):
    q = enumerate_bands(bounds)
    cumulative = []
    annuli = []
    sums = {k: [0.0, 0.0, 0.0] for k in ("raw", "G", "shell", "G_OE", "G_EE")}

    for j, B in enumerate(bounds):
        band_vectors = {k: q[k][j] for k in sums}
        for k in sums:
            add_into(sums[k], band_vectors[k])
        cumulative.append(make_row(B, *(sums[k].copy() for k in ("raw", "G", "shell", "G_OE", "G_EE"))))
        annuli.append(make_row(B, *(band_vectors[k] for k in ("raw", "G", "shell", "G_OE", "G_EE"))))

    raw100 = tuple(int(cumulative[0]["raw"]["weight"][c]) for c in CATS)
    raw1m = tuple(int(cumulative[-1]["raw"]["weight"][c]) for c in CATS)
    if raw100 != LOCK_RAW_100K or raw1m != LOCK_RAW_1M:
        raise ArithmeticError(("raw lock", raw100, raw1m))

    outer_vectors = {}
    for k in sums:
        outer_vectors[k] = [sum(q[k][j][i] for j in range(5, 10)) for i in range(3)]
    outer = make_row(1_000_000, *(outer_vectors[k] for k in ("raw", "G", "shell", "G_OE", "G_EE")))
    outer["B_lo_exclusive"] = 500_000
    outer["B_hi_inclusive"] = 1_000_000

    first, last = cumulative[0], cumulative[-1]
    exact_one = None
    if STAGE7A.exists():
        old = json.loads(STAGE7A.read_text(encoding="utf-8"))
        e100 = old["cumulative"][0]["exact_one"]
        e1m = old["cumulative"][-1]["exact_one"]
        exact_one = {
            "B100000": {"alpha": e100["alpha"], "beta": e100["beta"], "ratio_bc": e100["ratio_bc"]},
            "B1000000": {"alpha": e1m["alpha"], "beta": e1m["beta"], "ratio_bc": e1m["ratio_bc"]},
            "raw_vs_exact_beta_difference_at_1m": e1m["beta"] - last["raw"]["beta"],
        }

    beta_G_growth = last["G_neutral"]["beta"] - first["G_neutral"]["beta"]
    beta_raw_growth = last["raw"]["beta"] - first["raw"]["beta"]
    c100 = first["G_neutral_parity"]["pair_gap_cancellation"]
    c1m = last["G_neutral_parity"]["pair_gap_cancellation"]

    return {
        "metadata": {
            "stage": "13-7b",
            "title": "Mechanism-resolved scaling of the Stage13 deviation through B=1,000,000",
            "bounds": list(bounds),
            "scope": "complete finite raw-incidence mechanism diagnostic; no asymptotic limit claim",
        },
        "definitions": {
            "r_raw": "raw ac/bc ratio",
            "r_G": "G-neutral ac/bc ratio after weight 1/R_all(p)",
            "F_prim": "r_shell_neutral/r_G; primitive-support correction",
            "F_shell": "r_raw/r_shell_neutral; restoration of supported-shell richness",
            "exact_identity": "r_raw = r_G * F_prim * F_shell at each finite cutoff",
            "warning": "The factor chain is a finite reweighting identity; it is not a proved asymptotic Euler-factor decomposition.",
        },
        "validation": {
            "raw_100k_lock": raw100,
            "raw_1m_lock_from_stage13_7a": raw1m,
            "matched": True,
            "enumeration_diagnostics": q["diagnostics"],
        },
        "cumulative": cumulative,
        "annuli_100k": annuli,
        "outer_half_500k_1m": outer,
        "exact_one_cross_check_from_7a": exact_one,
        "key_comparison_100k_to_1m": {
            "raw_beta": {"B100000": first["raw"]["beta"], "B1000000": last["raw"]["beta"], "change": beta_raw_growth},
            "G_neutral_beta": {"B100000": first["G_neutral"]["beta"], "B1000000": last["G_neutral"]["beta"], "change": beta_G_growth},
            "G_neutral_ac_bc": {"B100000": first["G_neutral"]["ratio_bc"]["ac"], "B1000000": last["G_neutral"]["ratio_bc"]["ac"]},
            "F_prim": {"B100000": first["ac_bc_factor_chain"]["F_prim"], "B1000000": last["ac_bc_factor_chain"]["F_prim"]},
            "F_shell": {"B100000": first["ac_bc_factor_chain"]["F_shell"], "B1000000": last["ac_bc_factor_chain"]["F_shell"]},
            "G_OE_ac_bc": {"B100000": first["G_neutral_parity"]["OE"]["ratio_bc"]["ac"], "B1000000": last["G_neutral_parity"]["OE"]["ratio_bc"]["ac"]},
            "G_EE_ac_bc": {"B100000": first["G_neutral_parity"]["EE"]["ratio_bc"]["ac"], "B1000000": last["G_neutral_parity"]["EE"]["ratio_bc"]["ac"]},
            "G_pair_cancellation_efficiency": {"B100000": c100["cancellation_efficiency"], "B1000000": c1m["cancellation_efficiency"]},
        },
        "conclusion": {
            "beta_drift_main_finite_source": "pure-G cross-stratum balance moves away from its accidental near-cancellation at B=100000",
            "evidence": (
                "G-neutral ac/bc rises from about 1.00202 at 100k to 1.03043 at 1m. "
                "The OE G-neutral gap remains slightly bc-heavy, but its negative magnitude becomes small relative to the EE ac-heavy gap; "
                "the opposite-sign cancellation efficiency drops from about 95.6% to about 19.3%."
            ),
            "primitive_support_explains_growth": False,
            "primitive_support_note": "F_prim weakens from about 1.05888 to 1.05098, so it cannot be the source of the increased ac/bc split over this decade.",
            "supported_shell_explains_growth": False,
            "supported_shell_note": "F_shell remains close to 1 and is about 0.99669 at 1m; shell restoration contributes only a small beta shift.",
            "outer_half_reproduces_mechanism": True,
            "outer_half_note": "For 500k<d<=1m, r_G is about 1.03392, F_prim about 1.05018 and F_shell about 1.000006, so the fresh half independently shows the same positive pure-G base plus primitive-support tilt.",
            "interpretation": (
                "The 100k near equality of ac and bc after pure-G deweighting was a finite cancellation sweet spot, not a stable balance across the next decade. "
                "By 1m the main new source of the larger beta is the deterioration of that OE/EE pure-G cancellation. Primitive support remains positive but slightly weakens, and supported-shell restoration stays nearly neutral for ac/bc."
            ),
            "asymptotic_limit_identified": False,
            "stage13_7_status": "ACTIVE_7B_COMPLETE_TO_B_1E6_MECHANISM_RESOLVED",
            "next": "Stage13-7c: test the pure-G OE/EE balance beyond 1m (2m-5m) and/or derive a secondary-term model for the parity-resolved G-neutral gaps.",
        },
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=OUT)
    a = ap.parse_args()
    report = build_report(BOUNDS)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["key_comparison_100k_to_1m"], indent=2))


if __name__ == "__main__":
    main()
