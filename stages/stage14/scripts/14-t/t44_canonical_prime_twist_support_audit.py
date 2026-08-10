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
        assert (s["branch"] == "invisible" and v == 0) or (s["branch"] == "visible" and v == 2)
    assert own_val == Counter({("invisible", 0): 419, ("visible", 2): 141})

    by_kernel = defaultdict(list)
    for s in reps:
        by_kernel[s["kernel"]].append(s)
    principal = Counter()
    for members in by_kernel.values():
        if len(members) != 2:
            continue
        x, y = members
        if x["ell"] == y["ell"]:
            principal["same_ell"] += 1
        else:
            principal["distinct_ell"] += 1
            assert vp(y["F"], x["ell"]) == 0 and vp(x["F"], y["ell"]) == 0
            assert direction_delta(y) % x["ell"] != 0
            assert direction_delta(x) % y["ell"] != 0
            principal["distinct_ell_cross_good"] += 1
    assert principal == Counter({"distinct_ell": 14, "distinct_ell_cross_good": 14, "same_ell": 2})

    conv = Counter()
    class_by_tau = defaultdict(Counter)
    routing_checks = 0
    offdir_pairs = 0
    same_ell_pairs = 0
    cross_good_pairs = 0
    cross_bad_pairs = 0

    for x in reps:
        dx = (x["a"], x["b"])
        for y in reps:
            tau = cross_kernel(x["kernel"], y["kernel"])
            conv[tau] += 1
            if dx == (y["a"], y["b"]):
                continue
            offdir_pairs += 1
            if x["ell"] == y["ell"]:
                same_ell_pairs += 1
                cls = "same_ell"
            else:
                vx_y = vp(y["F"], x["ell"])
                vy_x = vp(x["F"], y["ell"])
                if vx_y:
                    assert vx_y == 1 and tau % x["ell"] == 0
                    routing_checks += 1
                if vy_x:
                    assert vy_x == 1 and tau % y["ell"] == 0
                    routing_checks += 1
                if vx_y or vy_x:
                    cross_bad_pairs += 1
                    cls = "distinct_ell_cross_bad"
                else:
                    cross_good_pairs += 1
                    cls = "distinct_ell_cross_good"
            if tau != 1:
                class_by_tau[tau][cls] += 1

    assert conv[1] == 592
    assert (offdir_pairs, same_ell_pairs, cross_good_pairs, cross_bad_pairs, routing_checks) == (
        309906, 3490, 305334, 1082, 1084
    )

    heavy = {tau: m for tau, m in conv.items() if tau != 1 and m > HEAVY_THRESHOLD}
    heavy_class = Counter()
    for tau in heavy:
        heavy_class.update(class_by_tau[tau])
    heavy_pair_mass = sum(heavy.values())
    heavy_same_direction = heavy_pair_mass - sum(heavy_class.values())
    assert len(heavy) == 72 and heavy_pair_mass == 1834
    assert heavy_class == Counter({"distinct_ell_cross_good": 1816, "same_ell": 14})
    assert heavy_same_direction == 4
    assert heavy_class["distinct_ell_cross_bad"] == 0

    top8 = sorted(heavy.items(), key=lambda kv: (-kv[1], kv[0]))[:8]
    assert top8 == [(91, 40), (209, 38), (286, 34), (34034, 34), (41, 32), (329, 32), (4641, 32), (11, 30)]
    for tau, mult in top8:
        assert class_by_tau[tau]["distinct_ell_cross_bad"] == 0

    safe_tau_bound = (256 * B**4) ** 2
    observed_ells = {s["ell"] for s in reps if s["ell"] > 2 * isqrt(B)}
    max_exposed = 0
    for tau in conv:
        assert tau <= safe_tau_bound
        max_exposed = max(max_exposed, sum(tau % ell == 0 for ell in observed_ells))
    assert max_exposed == 4

    report = {
        "stage": "14-t44",
        "own_canonical_valuation": {
            "invisible_v0": own_val[("invisible", 0)],
            "visible_v2": own_val[("visible", 2)],
        },
        "principal": dict(principal),
        "all_offdirection": {
            "pairs": offdir_pairs,
            "same_ell": same_ell_pairs,
            "distinct_ell_cross_good": cross_good_pairs,
            "distinct_ell_cross_bad": cross_bad_pairs,
            "twist_support_routing_checks": routing_checks,
        },
        "heavy_nonprincipal": {
            "threshold": HEAVY_THRESHOLD,
            "kernel_count": len(heavy),
            "pair_mass": heavy_pair_mass,
            "distinct_ell_cross_good_mass": heavy_class["distinct_ell_cross_good"],
            "distinct_ell_cross_bad_mass": heavy_class["distinct_ell_cross_bad"],
            "same_ell_mass": heavy_class["same_ell"],
            "same_direction_mass": heavy_same_direction,
            "top8": [[tau, mult] for tau, mult in top8],
            "top8_cross_bad_mass_zero": True,
        },
        "support_ledger": {
            "safe_tau_bound": "2^16*B^8",
            "super_sqrt_prime_support_bound": "omega_{p>2sqrt(B)}(tau)<=16+o(1)",
            "observed_max_exposed_canonical_primes_per_tau": max_exposed,
            "principal_distinct_ell_cross_bad_impossible": True,
            "nonprincipal_foreign_canonical_prime_routes_into_tau": True,
        },
        "decision": {
            "STAGE14_T44": "COMPLETE_CANONICAL_PRIME_TWIST_SUPPORT_ROUTING_AND_GENERIC_CROSS_GOOD_REDUCTION",
            "CANONICAL_OWN_VALUATION_EVEN": True,
            "PRINCIPAL_DISTINCT_ELL_CROSS_SUPPORT_GOOD": True,
            "NONPRINCIPAL_CROSS_BAD_PRIME_ROUTES_INTO_TWIST": True,
            "FIXED_TWIST_SUPER_SQRT_EXPOSED_CANONICAL_PRIMES": "O(1)",
            "FROZEN_HEAVY_CROSS_BAD_MASS": 0,
            "GENERIC_CROSS_GOOD_KUMMER_REMAINS_PRIMARY": True,
            "CROSS_BAD_HEAVY_MASS_POWER_SAVING_PROVED": False,
            "GENERIC_CROSS_GOOD_KUMMER_INCIDENCE_BOUND_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "CANONICAL_PRIME_SUM_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": "Stage14-t45 attack the distinct-canonical-prime cross-good Kummer incidence by a two-canonical-prime quadratic-character/dispersion receiver; treat same-ell and tau-supported cross-bad pieces as exceptional slices",
        },
        "tH_reopen": {
            "needed": True,
            "suggested_stage": "Stage14-tH12",
            "task": "build a reusable receiver for generic cross-good Kummer incidence using fixed common-core/moving canonical prime, fixed canonical prime/moving common-core, and heavy-light multi-modulus decompositions; stress-test quantifiers without assuming a future t44 theorem",
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
