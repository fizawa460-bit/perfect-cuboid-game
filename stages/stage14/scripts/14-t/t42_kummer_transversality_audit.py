#!/usr/bin/env python3
"""Stage14-t42: reciprocal quotient and twisted-Kummer energy reduction audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T41_DATA = ROOT / "stages/stage14/data/14-t41/global_energy_incidence.json"
OUT = ROOT / "stages/stage14/data/14-t42/kummer_transversality.json"


def common_packet_key(s):
    k = s["n"] // s["delta"]
    h = s["eps"] * s["m"] // k
    assert k * s["delta"] == s["n"]
    assert h * k == s["eps"] * s["m"]
    return (s["eps"], s["delta"], h, s["branch"])


def gaussian_unit_key(z):
    x, y = z
    return min(((x, y), (-y, x), (-x, -y), (y, -x)))


def square_ratio(F1, F2):
    g = gcd(F1, F2)
    a, b = F1 // g, F2 // g
    ra, rb = isqrt(a), isqrt(b)
    assert ra * ra == a and rb * rb == b
    return [ra, rb]


def cross_kernel(a, b):
    g = gcd(a, b)
    return (a // g) * (b // g)


def direction_lambda(a, b):
    return Fraction((b * b - a * a) ** 2, (a * a + b * b) ** 2)


def direction_branch_moduli_key(a, b):
    lam = direction_lambda(a, b)
    assert 0 < lam < 1
    # For lambda,lambda' in (0,1), an S3 cross-ratio orbit meets (0,1)
    # exactly in {lambda,1-lambda}.  Thus this is the exact PGL2
    # branch-divisor-equivalence key for {+-a/b,+-b/a}.
    return min(lam, 1 - lam)


def reciprocal_quotient(states):
    groups = defaultdict(list)
    for s in states:
        key = (s["a"], s["b"], min(s["p"], s["q"]), max(s["p"], s["q"]))
        groups[key].append(s)
    assert len(groups) == 560
    reps = []
    for (a, b, p0, q0), members in groups.items():
        assert len(members) == 2
        assert {(s["p"], s["q"]) for s in members} == {(p0, q0), (q0, p0)}
        assert len({s["F"] for s in members}) == 1
        assert len({s["kernel"] for s in members}) == 1
        reps.append(min(members, key=lambda s: (s["p"], s["q"])))
    return reps


def principal_blocks(reps):
    by_kernel = defaultdict(list)
    for s in reps:
        by_kernel[s["kernel"]].append(s)
    hist = Counter(len(v) for v in by_kernel.values())
    assert hist == Counter({1: 528, 2: 16})

    names = (
        "same_U_unit",
        "same_V_unit",
        "same_branch",
        "same_common_packet",
        "same_cover",
        "same_ell",
        "same_exact_F",
        "direction_branch_divisors_PGL2_equivalent",
    )
    summary = {name: 0 for name in names}
    direction_degree = Counter()
    cover_degree = Counter()
    blocks = []

    for kernel, members in sorted(by_kernel.items()):
        if len(members) != 2:
            continue
        x, y = members
        dx, dy = (x["a"], x["b"]), (y["a"], y["b"])
        cx = (min(x["p"], x["q"]), max(x["p"], x["q"]))
        cy = (min(y["p"], y["q"]), max(y["p"], y["q"]))
        assert dx != dy
        flags = {
            "same_U_unit": gaussian_unit_key(x["U"]) == gaussian_unit_key(y["U"]),
            "same_V_unit": gaussian_unit_key(x["V"]) == gaussian_unit_key(y["V"]),
            "same_branch": x["branch"] == y["branch"],
            "same_common_packet": common_packet_key(x) == common_packet_key(y),
            "same_cover": cx == cy,
            "same_ell": x["ell"] == y["ell"],
            "same_exact_F": x["F"] == y["F"],
            "direction_branch_divisors_PGL2_equivalent": (
                direction_branch_moduli_key(*dx) == direction_branch_moduli_key(*dy)
            ),
        }
        for name, value in flags.items():
            summary[name] += int(value)
        direction_degree[dx] += 1
        direction_degree[dy] += 1
        cover_degree[cx] += 1
        cover_degree[cy] += 1
        blocks.append(
            {
                "kernel": kernel,
                "directions": [list(dx), list(dy)],
                "covers": [list(cx), list(cy)],
                "ells": [x["ell"], y["ell"]],
                "branches": [x["branch"], y["branch"]],
                "square_ratio_root_reduced": square_ratio(x["F"], y["F"]),
            }
        )

    assert len(blocks) == 16
    assert summary == {
        "same_U_unit": 8,
        "same_V_unit": 3,
        "same_branch": 14,
        "same_common_packet": 2,
        "same_cover": 3,
        "same_ell": 2,
        "same_exact_F": 1,
        "direction_branch_divisors_PGL2_equivalent": 0,
    }
    assert max(direction_degree.values()) == 2
    assert Counter(direction_degree.values()) == Counter({1: 18, 2: 7})
    assert max(cover_degree.values()) == 7
    assert Counter(cover_degree.values()) == Counter({1: 7, 2: 2, 4: 2, 6: 1, 7: 1})

    return {
        "blocks": blocks,
        "summary": {"blocks": 16, **summary},
        "direction_collision_graph": {
            "vertices": len(direction_degree),
            "max_degree": max(direction_degree.values()),
            "degree_histogram": dict(sorted(Counter(direction_degree.values()).items())),
        },
        "cover_collision_graph": {
            "vertices": len(cover_degree),
            "max_degree": max(cover_degree.values()),
            "degree_histogram": dict(sorted(Counter(cover_degree.values()).items())),
        },
    }


def convolution_audit(reps):
    r = Counter(s["kernel"] for s in reps)
    H = len(reps)
    A1 = sum(v * v for v in r.values())
    assert H == 560 and A1 == 592
    assert Counter(r.values()) == Counter({1: 528, 2: 16})

    conv = Counter()
    for a, ra in r.items():
        for b, rb in r.items():
            conv[cross_kernel(a, b)] += ra * rb
    E4 = sum(v * v for v in conv.values())
    assert E4 == 1_324_576
    assert conv[1] == A1

    top = sorted(((k, v) for k, v in conv.items() if k != 1), key=lambda kv: (-kv[1], kv[0]))[:8]
    assert top == [(91, 40), (209, 38), (286, 34), (34034, 34), (41, 32), (329, 32), (4641, 32), (11, 30)]
    C_non = top[0][1]
    refined_upper = A1 * A1 + C_non * (H * H - A1)
    assert E4 <= refined_upper

    return {
        "H_reciprocal_orbits": H,
        "A1_quotient": A1,
        "A1_excess_over_diagonal": A1 - H,
        "distinct_squareclasses": len(r),
        "squareclass_multiplicity_histogram": dict(sorted(Counter(r.values()).items())),
        "E4_quotient": E4,
        "E4_over_H2": E4 / (H * H),
        "principal_E4": A1 * A1,
        "nonprincipal_E4": E4 - A1 * A1,
        "distinct_cross_kernels": len(conv),
        "max_nonprincipal_cross_kernel_multiplicity": C_non,
        "top_nonprincipal_cross_kernels": [[k, v] for k, v in top],
        "trivial_upper_A1_H2": A1 * H * H,
        "refined_upper_using_C_non": refined_upper,
        "observed_to_trivial_upper_ratio": E4 / (A1 * H * H),
    }


def main():
    frozen41 = json.loads(T41_DATA.read_text())
    assert frozen41["decision"]["STAGE14_T41"] == (
        "COMPLETE_TWO_SIDED_INCIDENCE_AUDIT_AND_KUMMER_ENERGY_BARRIER"
    )
    assert frozen41["decision"]["OFF_FIBER_COLLISION_SURFACE_KUMMER_TYPE"] is True

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    states = t36["build_frozen_states"]()
    reps = reciprocal_quotient(states)
    blocks = principal_blocks(reps)
    conv = convolution_audit(reps)

    report = {
        "stage": "14-t42",
        "reciprocal_quotient": {
            "ordered_states": len(states),
            "orbits": len(reps),
            "exact_frozen_scaling": "H=2H*, A1=4A1*, E4=16E4*",
            "reason": "F(a,b,p,q)=F(a,b,q,p) exactly",
        },
        "off_direction_principal": blocks,
        "cross_kernel_convolution": conv,
        "twisted_kummer_interface": {
            "surface": "K^(tau)_{gamma,gamma'}: Y^2=tau*f_gamma(x)*f_gamma_prime(y)",
            "principal": "tau=1; after the reciprocal quotient, off-direction incidences are the non-diagonal principal points",
            "nonprincipal": "tau!=1; c(tau)=#{(s,t): [F_s F_t]=tau}",
            "exact_energy_identity": "E4=A1^2+sum_{tau!=1} c(tau)^2",
            "refined_energy_bound": "E4<=A1^2+C_non*(H^2-A1), C_non=max_{tau!=1}c(tau)",
            "sufficient_interface": "A1<=H*B^o(1) and C_non<=B^o(1) imply E4<=H^2*B^o(1)",
        },
        "decision": {
            "STAGE14_T42": "COMPLETE_RECIPROCAL_QUOTIENT_AND_TWISTED_KUMMER_ENERGY_REDUCTION",
            "RECIPROCAL_DOUBLE_COVER_QUOTIENTED": True,
            "FROZEN_RECIPROCAL_ORBITS": 560,
            "FROZEN_OFF_DIRECTION_PRINCIPAL_BLOCKS": 16,
            "FROZEN_DIRECTION_COLLISION_GRAPH_MAX_DEGREE": 2,
            "FROZEN_DIRECTION_BRANCH_PGL2_EQUIVALENT_BLOCKS": 0,
            "PRINCIPAL_AND_NONPRINCIPAL_UNIFIED_BY_TWISTED_KUMMER": True,
            "REFINED_E4_BOUND": "A1^2+C_non*(H^2-A1)",
            "A1_NEAR_LINEAR_PLUS_CNON_SUBPOLY_IMPLIES_E4_NEAR_QUADRATIC": True,
            "OFF_DIRECTION_PRINCIPAL_AGGREGATE_BOUND_PROVED": False,
            "NONPRINCIPAL_TWIST_MULTIPLICITY_SUBPOLY_PROVED": False,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "CANONICAL_PRIME_SUM_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": (
                "Stage14-t43 prove canonical-prime/common-core transversality for K^(tau): "
                "near-linear aggregate off-direction incidence for tau=1 after reciprocal quotient, "
                "and B^o(1) multiplicity for every tau!=1; isolate exceptional low-degree correspondences separately"
            ),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["reciprocal_quotient"], indent=2, sort_keys=True))
    print(json.dumps(report["off_direction_principal"]["summary"], indent=2, sort_keys=True))
    print(json.dumps(report["cross_kernel_convolution"], indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
