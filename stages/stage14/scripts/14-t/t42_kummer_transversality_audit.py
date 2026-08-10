#!/usr/bin/env python3
"""Stage14-t42: reciprocal quotient, off-direction blocks, twisted Kummer energy audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
OUT = ROOT / "stages/stage14/data/14-t42/kummer_transversality.json"


def common_packet_key(s):
    k = s["n"] // s["delta"]
    h = s["eps"] * s["m"] // k
    assert k * s["delta"] == s["n"]
    assert h * k == s["eps"] * s["m"]
    return (s["eps"], s["delta"], h, s["branch"])


def gaussian_unit_key(z):
    x, y = z
    orbit = ((x, y), (-y, x), (-x, -y), (y, -x))
    return min(orbit)


def square_ratio(F1, F2):
    g = gcd(F1, F2)
    a, b = F1 // g, F2 // g
    ra, rb = isqrt(a), isqrt(b)
    assert ra * ra == a and rb * rb == b
    return ra, rb


def cross_kernel(a, b):
    g = gcd(a, b)
    return (a // g) * (b // g)


def direction_lambda(a, b):
    # Cross-ratio representative for branch set {+-a/b,+-b/a}.
    # With r=a/b: lambda=((1-r^2)/(1+r^2))^2 in (0,1).
    return Fraction((b * b - a * a) ** 2, (a * a + b * b) ** 2)


def direction_branch_moduli_key(a, b):
    # For lambda in (0,1), the S3 cross-ratio orbit meets (0,1)
    # only in lambda and 1-lambda.  This is an exact branch-divisor
    # PGL2-equivalence test for this symmetric quartic family.
    lam = direction_lambda(a, b)
    return min(lam, 1 - lam)


def reciprocal_quotient(states):
    groups = defaultdict(list)
    for s in states:
        key = (s["a"], s["b"], min(s["p"], s["q"]), max(s["p"], s["q"]))
        groups[key].append(s)
    assert len(groups) == 560
    reps = []
    for key, members in groups.items():
        assert len(members) == 2
        a, b, p0, q0 = key
        assert {(s["p"], s["q"]) for s in members} == {(p0, q0), (q0, p0)}
        assert len({s["F"] for s in members}) == 1
        assert len({s["kernel"] for s in members}) == 1
        rep = min(members, key=lambda s: (s["p"], s["q"]))
        reps.append(rep)
    return reps


def block_audit(reps):
    by_kernel = defaultdict(list)
    for s in reps:
        by_kernel[s["kernel"]].append(s)
    hist = Counter(len(v) for v in by_kernel.values())
    assert hist == Counter({1: 528, 2: 16})

    blocks = []
    summary = Counter()
    direction_graph = Counter()
    cover_graph = Counter()
    for kernel, members in sorted(by_kernel.items()):
        if len(members) != 2:
            continue
        x, y = members
        dx = (x["a"], x["b"])
        dy = (y["a"], y["b"])
        assert dx != dy
        cx = (min(x["p"], x["q"]), max(x["p"], x["q"]))
        cy = (min(y["p"], y["q"]), max(y["p"], y["q"]))
        r1, r2 = square_ratio(x["F"], y["F"])
        same_ell = x["ell"] == y["ell"]
        same_branch = x["branch"] == y["branch"]
        same_common = common_packet_key(x) == common_packet_key(y)
        same_u = gaussian_unit_key(x["U"]) == gaussian_unit_key(y["U"])
        same_v = gaussian_unit_key(x["V"]) == gaussian_unit_key(y["V"])
        same_cover = cx == cy
        exact_f = x["F"] == y["F"]
        branch_equiv = direction_branch_moduli_key(*dx) == direction_branch_moduli_key(*dy)

        summary["blocks"] += 1
        for name, val in (
            ("same_ell", same_ell),
            ("same_branch", same_branch),
            ("same_common_packet", same_common),
            ("same_U_unit", same_u),
            ("same_V_unit", same_v),
            ("same_cover", same_cover),
            ("same_exact_F", exact_f),
            ("direction_branch_divisors_PGL2_equivalent", branch_equiv),
        ):
            if val:
                summary[name] += 1

        direction_graph[dx] += 1
        direction_graph[dy] += 1
        cover_graph[cx] += 1
        cover_graph[cy] += 1
        blocks.append(
            {
                "kernel": kernel,
                "directions": [list(dx), list(dy)],
                "covers": [list(cx), list(cy)],
                "ells": [x["ell"], y["ell"]],
                "branches": [x["branch"], y["branch"]],
                "m_n_delta": [[x["m"], x["n"], x["delta"]], [y["m"], y["n"], y["delta"]]],
                "square_ratio_root_reduced": [r1, r2],
                "same_ell": same_ell,
                "same_branch": same_branch,
                "same_common_packet": same_common,
                "same_U_unit": same_u,
                "same_V_unit": same_v,
                "same_cover": same_cover,
                "same_exact_F": exact_f,
                "direction_branch_divisors_PGL2_equivalent": branch_equiv,
                "direction_det": x["a"] * y["b"] - y["a"] * x["b"],
                "cover_det": x["p"] * y["q"] - y["p"] * x["q"],
            }
        )

    assert summary["blocks"] == 16
    return {
        "summary": dict(summary),
        "direction_collision_graph": {
            "vertices": len(direction_graph),
            "max_degree": max(direction_graph.values()),
            "degree_histogram": dict(sorted(Counter(direction_graph.values()).items())),
        },
        "cover_collision_graph": {
            "vertices": len(cover_graph),
            "max_degree": max(cover_graph.values()),
            "degree_histogram": dict(sorted(Counter(cover_graph.values()).items())),
        },
        "blocks": blocks,
    }


def convolution_audit(reps):
    r = Counter(s["kernel"] for s in reps)
    H = len(reps)
    A1 = sum(v * v for v in r.values())
    assert H == 560 and A1 == 592
    conv = Counter()
    items = list(r.items())
    for a, ra in items:
        for b, rb in items:
            conv[cross_kernel(a, b)] += ra * rb
    E4 = sum(v * v for v in conv.values())
    assert E4 == 21_193_216 // 16
    assert conv[1] == A1
    non = [(k, v) for k, v in conv.items() if k != 1]
    top = sorted(non, key=lambda kv: (-kv[1], kv[0]))[:20]
    C_non = top[0][1]
    exact_refined_upper = A1 * A1 + C_non * (H * H - A1)
    assert E4 <= exact_refined_upper
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
        "observed_to_trivial_upper_ratio": E4 / (A1 * H * H),
        "refined_upper_using_C_non": exact_refined_upper,
        "refined_energy_identity": (
            "E4=A1^2+sum_{tau!=1} c(tau)^2 <= A1^2+C_non*(H^2-A1), "
            "where c(tau)=#{(s,t): [F_s F_t]=tau}"
        ),
        "sufficient_asymptotic_interface": (
            "A1<=H*B^o(1) and max_{tau!=1} c(tau)<=B^o(1) imply E4<=H^2*B^o(1)"
        ),
    }


def main():
    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    states = t36["build_frozen_states"]()
    reps = reciprocal_quotient(states)
    blocks = block_audit(reps)
    conv = convolution_audit(reps)
    report = {
        "stage": "14-t42",
        "reciprocal_quotient": {
            "ordered_states": len(states),
            "orbits": len(reps),
            "exact_scaling": "H=2H*, A1=4A1*, E4=16E4* for the frozen p<->q double cover",
            "structural_note": "p<->q leaves F exactly invariant and can be quotiented at bounded cost",
        },
        "off_direction_blocks": blocks,
        "cross_kernel_convolution": conv,
        "twisted_kummer_interface": {
            "fixed_twist_surface": "K^(tau)_{gamma,gamma'}: Y^2=tau*f_gamma(x)*f_gamma'(y)",
            "principal_twist": "tau=1; its off-fiber points are the principal same-squareclass collisions",
            "nonprincipal_twists": "tau!=1; c(tau) is the global multiplicity of the corresponding cross-squareclass",
            "uniform_goal": (
                "control principal off-direction incidences in aggregate and prove subpolynomial multiplicity "
                "for every nonprincipal twist after canonical-prime/common-core restrictions"
            ),
            "why_this_closes_E4": (
                "the refined identity isolates the unavoidable principal diagonal A1^2; all remaining fourth energy "
                "is bounded by C_non times the total nonprincipal pair mass"
            ),
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
