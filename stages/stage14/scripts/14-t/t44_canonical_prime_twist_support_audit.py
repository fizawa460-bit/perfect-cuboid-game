#!/usr/bin/env python3
"""Stage14-t44: canonical-prime cross-support routing for generic twisted-Kummer incidence."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T43_DATA = ROOT / "stages/stage14/data/14-t43/low_degree_kummer_transversality.json"
OUT = ROOT / "stages/stage14/data/14-t44/canonical_prime_twist_support.json"
B = 10_000
HEAVY_THRESHOLD = 20


def vp(n: int, p: int) -> int:
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def direction_delta(s) -> int:
    a, b = s["a"], s["b"]
    return 2 * a * b * (b * b - a * a) * (a * a + b * b)


def main():
    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    t43 = json.loads(T43_DATA.read_text())
    assert t43["stage"] == "14-t43"
    assert t43["decision"]["GENERIC_TWISTED_KUMMER_REMAINS_PRIMARY"] is True

    states = t36["build_frozen_states"]()
    reps = t42["reciprocal_quotient"](states)
    cross_kernel = t42["cross_kernel"]
    assert len(reps) == 560

    own_val = Counter()
    for s in reps:
        v = vp(s["F"], s["ell"])
        own_val[(s["branch"], v)] += 1
        if s["branch"] == "invisible":
            assert v == 0
        else:
            assert v == 2

    by_kernel = defaultdict(list)
    for s in reps:
        by_kernel[s["kernel"]].append(s)
    principal = Counter()
    principal_rows = []
    for ker, members in by_kernel.items():
        if len(members) != 2:
            continue
        x, y = members
        same_ell = x["ell"] == y["ell"]
        vx_y = vp(y["F"], x["ell"])
        vy_x = vp(x["F"], y["ell"])
        if same_ell:
            principal["same_ell"] += 1
        else:
            principal["distinct_ell"] += 1
            assert vx_y == 0 and vy_x == 0
            principal["distinct_ell_cross_good"] += 1
            assert direction_delta(y) % x["ell"] != 0
            assert direction_delta(x) % y["ell"] != 0
        principal_rows.append({
            "kernel": ker,
            "ell_pair": sorted([x["ell"], y["ell"]]),
            "same_ell": same_ell,
            "cross_valuations": [vx_y, vy_x],
        })
    assert len(principal_rows) == 16

    conv = Counter()
    heavy_rows = defaultdict(lambda: Counter())
    routing_checks = 0
    offdir_pairs = 0
    cross_bad_pairs = 0
    same_ell_pairs = 0
    distinct_ell_cross_good_pairs = 0

    for x in reps:
        dx = (x["a"], x["b"])
        for y in reps:
            tau = cross_kernel(x["kernel"], y["kernel"])
            conv[tau] += 1
            if dx == (y["a"], y["b"]):
                continue
            offdir_pairs += 1
            same_ell = x["ell"] == y["ell"]
            if same_ell:
                same_ell_pairs += 1
                classif = "same_ell"
            else:
                vx_y = vp(y["F"], x["ell"])
                vy_x = vp(x["F"], y["ell"])
                if vx_y:
                    assert vx_y == 1
                    assert tau % x["ell"] == 0
                    routing_checks += 1
                if vy_x:
                    assert vy_x == 1
                    assert tau % y["ell"] == 0
                    routing_checks += 1
                if vx_y or vy_x:
                    cross_bad_pairs += 1
                    classif = "distinct_ell_cross_bad"
                else:
                    distinct_ell_cross_good_pairs += 1
                    classif = "distinct_ell_cross_good"
            if tau != 1:
                heavy_rows[tau][classif] += 1

    assert conv[1] == 592
    heavy = {tau: m for tau, m in conv.items() if tau != 1 and m > HEAVY_THRESHOLD}
    heavy_summary = Counter()
    top = []
    for tau, mult in sorted(heavy.items(), key=lambda kv: (-kv[1], kv[0])):
        row = heavy_rows[tau]
        for k, v in row.items():
            heavy_summary[k] += v
        exposed = sorted({s["ell"] for s in reps if tau % s["ell"] == 0})
        top.append({
            "tau": tau,
            "multiplicity": mult,
            "offdir_same_ell": row["same_ell"],
            "offdir_cross_bad": row["distinct_ell_cross_bad"],
            "offdir_cross_good": row["distinct_ell_cross_good"],
            "observed_exposed_canonical_primes": exposed,
        })

    safe_tau_bound = (256 * B**4) ** 2
    max_super_sqrt_prime_count = 0
    observed_ells = {s["ell"] for s in reps if s["ell"] > 2 * isqrt(B)}
    for tau in conv:
        cnt = len({ell for ell in observed_ells if tau % ell == 0})
        max_super_sqrt_prime_count = max(max_super_sqrt_prime_count, cnt)
        assert tau <= safe_tau_bound

    report = {
        "stage": "14-t44-probe",
        "own_canonical_valuation": {f"{k[0]}_v{k[1]}": v for k, v in sorted(own_val.items())},
        "principal": {
            "counts": dict(principal),
            "blocks": sorted(principal_rows, key=lambda r: r["kernel"]),
        },
        "all_offdirection": {
            "pairs": offdir_pairs,
            "same_ell": same_ell_pairs,
            "distinct_ell_cross_good": distinct_ell_cross_good_pairs,
            "distinct_ell_cross_bad": cross_bad_pairs,
            "twist_support_routing_checks": routing_checks,
        },
        "heavy_nonprincipal": {
            "threshold": HEAVY_THRESHOLD,
            "kernel_count": len(heavy),
            "pair_mass": sum(heavy.values()),
            "offdirection_class_mass": dict(heavy_summary),
            "top20": top[:20],
        },
        "support_ledger": {
            "safe_tau_bound": "2^16*B^8",
            "foreign_super_sqrt_prime_dividing_partner_F_is_exposed_in_tau": True,
            "principal_distinct_ell_cross_bad_impossible": True,
            "observed_max_exposed_canonical_primes_per_tau": max_super_sqrt_prime_count,
        },
        "boundary": {
            "CANONICAL_OWN_VALUATION_EVEN": True,
            "PRINCIPAL_DISTINCT_ELL_CROSS_SUPPORT_GOOD": True,
            "NONPRINCIPAL_CROSS_BAD_PRIME_ROUTES_INTO_TWIST": True,
            "GENERIC_CROSS_GOOD_KUMMER_INCIDENCE_BOUND_PROVED": False,
            "CROSS_BAD_HEAVY_MASS_POWER_SAVING_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
