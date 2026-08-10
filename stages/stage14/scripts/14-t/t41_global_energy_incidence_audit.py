#!/usr/bin/env python3
"""Stage14-t41: global squareclass energy / two-sided incidence audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T40_DATA = ROOT / "stages/stage14/data/14-t40/cross_kernel_hecke_dispersion.json"
OUT = ROOT / "stages/stage14/data/14-t41/global_energy_incidence.json"


def common_packet_key(s):
    k = s["n"] // s["delta"]
    assert k * s["delta"] == s["n"]
    h = s["eps"] * s["m"] // k
    assert h * k == s["eps"] * s["m"]
    return (s["eps"], s["delta"], h, s["branch"])


def descended_packet_key(s):
    return (
        s["branch"],
        tuple(s["U"]),
        tuple(s["V"]),
        s["eps"],
        s["m"],
        s["n"],
        s["delta"],
    )


def direction_key(s):
    return (s["a"], s["b"])


def ordered_cover_key(s):
    return (s["p"], s["q"])


def unordered_cover_key(s):
    return tuple(sorted((s["p"], s["q"])))


def energy_by_partition(states, keyfn):
    cells = defaultdict(Counter)
    for s in states:
        cells[keyfn(s)][int(s["kernel"])] += 1
    return sum(v * v for cell in cells.values() for v in cell.values()), len(cells)


def principal_collision_breakdown(states):
    by_kernel = defaultdict(list)
    for idx, s in enumerate(states):
        by_kernel[int(s["kernel"])].append((idx, s))

    counts = Counter()
    off_examples = []
    cross_kernel_hist = Counter()

    for kernel, members in by_kernel.items():
        for ia, a in members:
            for ib, b in members:
                counts["global"] += 1
                same_dir = direction_key(a) == direction_key(b)
                same_cov = ordered_cover_key(a) == ordered_cover_key(b)
                same_ucov = unordered_cover_key(a) == unordered_cover_key(b)
                same_ell = a["ell"] == b["ell"]
                same_f = a["F"] == b["F"]
                same_u = tuple(a["U"]) == tuple(b["U"])
                same_v = tuple(a["V"]) == tuple(b["V"])
                same_common = common_packet_key(a) == common_packet_key(b)
                same_desc = descended_packet_key(a) == descended_packet_key(b)

                if same_dir:
                    counts["same_direction"] += 1
                else:
                    counts["cross_direction"] += 1
                if same_cov:
                    counts["same_ordered_cover"] += 1
                if same_ucov:
                    counts["same_unordered_cover"] += 1
                if same_ell:
                    counts["same_ell"] += 1
                if same_f:
                    counts["same_exact_F"] += 1
                if same_u:
                    counts["same_U"] += 1
                if same_v:
                    counts["same_V"] += 1
                if same_common:
                    counts["same_common_packet"] += 1
                if same_desc:
                    counts["same_descended_packet"] += 1
                if (not same_dir) and (not same_ucov):
                    counts["cross_direction_and_cover"] += 1
                if (not same_dir) and same_f:
                    counts["cross_direction_same_exact_F"] += 1
                if (not same_dir) and same_ell:
                    counts["cross_direction_same_ell"] += 1
                if (not same_dir) and same_common:
                    counts["cross_direction_same_common_packet"] += 1
                if (not same_dir) and same_desc:
                    counts["cross_direction_same_descended_packet"] += 1

                if ia < ib and not same_dir and len(off_examples) < 40:
                    off_examples.append(
                        {
                            "kernel": kernel,
                            "same_exact_F": same_f,
                            "same_ell": same_ell,
                            "same_unordered_cover": same_ucov,
                            "same_common_packet": same_common,
                            "same_descended_packet": same_desc,
                            "left": {
                                "a": a["a"], "b": a["b"], "p": a["p"], "q": a["q"],
                                "ell": a["ell"], "branch": a["branch"], "F": a["F"],
                                "m": a["m"], "n": a["n"], "delta": a["delta"],
                                "U": list(a["U"]), "V": list(a["V"]),
                            },
                            "right": {
                                "a": b["a"], "b": b["b"], "p": b["p"], "q": b["q"],
                                "ell": b["ell"], "branch": b["branch"], "F": b["F"],
                                "m": b["m"], "n": b["n"], "delta": b["delta"],
                                "U": list(b["U"]), "V": list(b["V"]),
                            },
                        }
                    )

    row_energy, direction_cells = energy_by_partition(states, direction_key)
    ordered_cover_energy, ordered_cover_cells = energy_by_partition(states, ordered_cover_key)
    unordered_cover_energy, unordered_cover_cells = energy_by_partition(states, unordered_cover_key)
    ell_energy, ell_cells = energy_by_partition(states, lambda s: s["ell"])
    common_packet_energy, common_packet_cells = energy_by_partition(states, common_packet_key)
    descended_packet_energy, descended_packet_cells = energy_by_partition(states, descended_packet_key)

    assert counts["global"] == 2368
    assert row_energy == 2240
    assert counts["same_direction"] == row_energy
    assert counts["cross_direction"] == 128

    return {
        "ordered_collision_categories": dict(sorted(counts.items())),
        "partition_energies": {
            "direction": {"cells": direction_cells, "energy": row_energy},
            "ordered_cover": {"cells": ordered_cover_cells, "energy": ordered_cover_energy},
            "unordered_cover": {"cells": unordered_cover_cells, "energy": unordered_cover_energy},
            "ell": {"cells": ell_cells, "energy": ell_energy},
            "common_packet": {"cells": common_packet_cells, "energy": common_packet_energy},
            "descended_packet": {"cells": descended_packet_cells, "energy": descended_packet_energy},
        },
        "cross_direction_unordered_examples": off_examples,
    }


def fourth_energy_decomposition(states):
    single = Counter(int(s["kernel"]) for s in states)
    H = len(states)
    A1 = sum(v * v for v in single.values())

    def cross_kernel(s, t):
        from math import gcd
        g = gcd(s, t)
        return (s // g) * (t // g)

    conv = Counter()
    items = list(single.items())
    for s, rs in items:
        for t, rt in items:
            conv[cross_kernel(s, t)] += rs * rt

    E4 = sum(v * v for v in conv.values())
    principal_fourth = A1 * A1
    nonprincipal_fourth = E4 - principal_fourth
    assert conv[1] == A1
    assert E4 == 21_193_216
    assert principal_fourth > 0 and nonprincipal_fourth > 0

    top = sorted(conv.items(), key=lambda kv: (-kv[1], kv[0]))[:20]
    assert top[0][0] == 1 and top[0][1] == A1

    return {
        "H": H,
        "A1": A1,
        "E4": E4,
        "principal_fourth_contribution": principal_fourth,
        "nonprincipal_fourth_contribution": nonprincipal_fourth,
        "principal_fraction": principal_fourth / E4,
        "E4_over_H2": E4 / (H * H),
        "A1_over_H": A1 / H,
        "top_cross_kernel_multiplicities": [[k, v] for k, v in top],
        "universal_inequalities": {
            "lower": "E4>=A1^2 (principal cross kernel alone)",
            "upper": "E4<=A1*H^2 by Cauchy: c(t)<=A1 and sum_t c(t)=H^2",
        },
    }


def main():
    frozen40 = json.loads(T40_DATA.read_text())
    assert frozen40["decision"]["STAGE14_T40"] == (
        "COMPLETE_ONE_CAUCHY_QUADRATIC_HECKE_CROSS_KERNEL_AND_ENERGY_BOUNDARY"
    )
    assert frozen40["decision"]["PRINCIPAL_CROSS_KERNEL_EQUALS_GLOBAL_SQUARECLASS_COLLISION"] is True
    assert frozen40["decision"]["FOURTH_ORDER_CROSS_KERNEL_ENERGY_REQUIRED"] is True

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    states = t36["build_frozen_states"]()
    assert len(states) == 1120

    principal = principal_collision_breakdown(states)
    fourth = fourth_energy_decomposition(states)

    report = {
        "stage": "14-t41",
        "frozen_audit": {
            "principal_collision_breakdown": principal,
            "fourth_energy": fourth,
        },
        "two_sided_incidence": {
            "row_theorem": "t36: for each fixed direction d, sum_k r_{d,k}^2 <= J_d*B^o(1)",
            "column_theorem": "t37 reverse: for each fixed cover state v, sum_k r_{v,k}^2 <= K_v*B^o(1)",
            "logical_gap": (
                "row and column energies being near-linear do not imply global A1 near-linear: "
                "a perfect matching with one common color has O(H) row/column energy but H^2 global energy"
            ),
        },
        "off_fiber_geometry": {
            "fixed_packet_pair_surface": "Y^2=f_gamma(x)*f_gamma_prime(y)",
            "elliptic_curves": "E_gamma:u^2=f_gamma(x), E_gamma_prime:v^2=f_gamma_prime(y)",
            "quotient_identity": (
                "the map (x,u;y,v)->(x,y,Y=u*v) identifies the collision surface birationally "
                "with (E_gamma x E_gamma_prime)/{(u,v)~(-u,-v)}; after resolution this is Kummer-type"
            ),
            "consequence": (
                "t36/t38 genus-one bounds control either elliptic fibration after freezing one variable, "
                "but they do not by themselves give B^o(1) points on the two-dimensional off-fiber surface"
            ),
        },
        "energy_boundary": {
            "principal": (
                "A1 splits into already-controlled same-direction energy plus genuine off-direction Kummer-surface incidences"
            ),
            "fourth": (
                "E4 is the multiplicative energy of the squareclass multiset; A1 alone only gives "
                "A1^2 <= E4 <= A1*H^2, so near-linear A1 would still not prove near-quadratic E4"
            ),
            "needed_new_input": (
                "a mixed transversality / squareclass-expansion theorem controlling off-fiber Kummer incidences "
                "and nonprincipal cross-kernel convolution, while retaining canonical-prime and physical packet constraints"
            ),
        },
        "decision": {
            "STAGE14_T41": "COMPLETE_TWO_SIDED_INCIDENCE_AUDIT_AND_KUMMER_ENERGY_BARRIER",
            "T36_ROW_ENERGY_REUSED": True,
            "T37_REVERSE_COLUMN_ENERGY_REUSED": True,
            "TWO_SIDED_LOCAL_ENERGY_IMPLIES_GLOBAL_NEAR_LINEAR": False,
            "OFF_FIBER_COLLISION_SURFACE_KUMMER_TYPE": True,
            "GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED": False,
            "A1_DECOMPOSED_INTO_LOCAL_PLUS_OFF_FIBER": True,
            "E4_LOWER_BOUND_A1_SQUARED": True,
            "E4_UPPER_BOUND_A1_H_SQUARED": True,
            "GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED": False,
            "CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED": False,
            "CANONICAL_PRIME_SUM_POWER_SAVING_PROVED": False,
            "A_11_POWER_SAVING_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": (
                "Stage14-t42 isolate the 128-type off-direction collision mechanism as a mixed Kummer incidence. "
                "Use canonical-prime/common-core constraints to seek a transversality or isogeny-exception split; "
                "simultaneously control nonprincipal squareclass convolution needed for E4"
            ),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["frozen_audit"], indent=2, sort_keys=True))
    print(json.dumps(report["decision"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
