#!/usr/bin/env python3
"""Stage14-t58: physical-mask toroidal separation and radial-cell L2 transfer audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T57_RESULT = ROOT / "stages/stage14/14-t57/result.md"
TH2_RESULT = ROOT / "stages/stage14/14-tH2/result.md"
TH4_RESULT = ROOT / "stages/stage14/14-tH4/result.md"
TH5_RESULT = ROOT / "stages/stage14/14-tH5/result.md"
OUT = ROOT / "stages/stage14/data/14-t58/physical_mask_radial_transfer.json"

B_FROZEN = 10_000


def gaussian_unit_key(z):
    x, y = z
    return min(((x, y), (-y, x), (-x, -y), (y, -x)))


def norm(z):
    return z[0] * z[0] + z[1] * z[1]


def radial_key(s):
    k = s["n"] // s["delta"]
    return (gaussian_unit_key(s["U"]), s["eps"], k, s["ell"], s["delta"])


def frac_str(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> None:
    t57 = T57_RESULT.read_text()
    th2 = TH2_RESULT.read_text()
    th4 = TH4_RESULT.read_text()
    th5 = TH5_RESULT.read_text()

    assert "STAGE14_T57=COMPLETE_RANK1_KUMMER_MELLIN_ADAPTER_AND_PHYSICAL_SELECTOR_CORRELATION_BOUNDARY" in t57
    assert "SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED=false" in t57
    assert "EXACT_PRODUCT_CUTOFF_RETAINED=true" in th2
    assert "GOOD_PRIME_MASK_L2_COST=1" in th4
    assert "FULL_EXACT_GAUSSIAN_PAIR_COEFFICIENT_COLLISION_ENERGY_PROVED=true" in th5
    assert "EXACT_PAIR_COLLAPSE_FIXED_POWER_LOSS=false" in th5

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    assert len(reps) == 560

    chamber_checks = 0
    inverse_checks = 0
    direction_mask_checks = 0
    invisible_branch_norm_checks = 0
    hyperbola_checks = 0

    # The physical reconstruction chamber is exactly separated in the
    # t57 ratio/product coordinates u=x/t, v=t*x.
    for s in reps:
        t = Fraction(s["a"], s["b"])
        x = Fraction(s["p"], s["q"])
        u = x / t
        v = t * x

        original = (s["a"] * s["q"] < s["b"] * s["p"] and
                    s["a"] * s["p"] < s["b"] * s["q"])
        toroidal = (u > 1 and 0 < v < 1)
        assert original and toroidal and original == toroidal
        chamber_checks += 1

        assert t * t == v / u
        assert x * x == u * v
        inverse_checks += 1

        # Hyperbola identity from the frozen physical reconstruction.
        assert s["eps"] * s["ell"] * s["m"] * s["delta"] // 2 <= B_FROZEN
        hyperbola_checks += 1

        if s["branch"] == "invisible":
            k = s["n"] // s["delta"]
            assert norm(s["V"]) == s["n"] == k * s["delta"]
            assert s["ell"] % 2 == 1
            assert s["n"] % s["ell"] != 0
            invisible_branch_norm_checks += 1

    # Canonical-prime / U / epsilon data depend only on the direction side,
    # not on the cover coordinate.  This is an exact one-side mask check.
    by_direction = defaultdict(list)
    for s in reps:
        by_direction[(s["a"], s["b"])].append(s)
    for fiber in by_direction.values():
        assert len({s["ell"] for s in fiber}) == 1
        assert len({gaussian_unit_key(s["U"]) for s in fiber}) == 1
        assert len({s["eps"] for s in fiber}) == 1
        assert len({s["m"] for s in fiber}) == 1
        direction_mask_checks += len(fiber)

    invisible = [s for s in reps if s["branch"] == "invisible"]
    assert len(invisible) == 419

    # Radial cells retain fixed U, epsilon and divisor-fan k, plus moving
    # canonical prime norm ell and delta.  Angular reconstruction inside one
    # cell is divisor-bounded asymptotically; the finite audit records its size.
    cells = defaultdict(list)
    for s in invisible:
        cells[radial_key(s)].append(s)

    hist = Counter(len(v) for v in cells.values())
    assert len(cells) == 408
    assert hist == Counter({1: 397, 2: 11})
    assert max(map(len, cells.values())) == 2
    radial_energy = sum(len(v) ** 2 for v in cells.values())
    assert radial_energy == 441

    # Per fixed-U frozen ledger.
    by_u = defaultdict(list)
    for s in invisible:
        by_u[gaussian_unit_key(s["U"])].append(s)
    per_u = []
    for U, states in sorted(by_u.items()):
        local = Counter((s["eps"], s["n"] // s["delta"], s["ell"], s["delta"]) for s in states)
        per_u.append({
            "U": list(U),
            "states": len(states),
            "radial_cells": len(local),
            "max_cell": max(local.values()),
            "radial_cell_energy": sum(v * v for v in local.values()),
        })
    assert per_u == [
        {"U": [-2, -1], "states": 27, "radial_cells": 19, "max_cell": 2, "radial_cell_energy": 43},
        {"U": [-2, 1], "states": 15, "radial_cells": 12, "max_cell": 2, "radial_cell_energy": 21},
        {"U": [-1, -1], "states": 160, "radial_cells": 160, "max_cell": 1, "radial_cell_energy": 160},
        {"U": [-1, 0], "states": 217, "radial_cells": 217, "max_cell": 1, "radial_cell_energy": 217},
    ]

    # The chamber separates, but the actual physical toroidal support is not
    # itself one Cartesian product.  Freeze a 3-of-4 rectangle witness.
    witness_u = (-1, 0)
    support = set()
    for s in by_u[witness_u]:
        t = Fraction(s["a"], s["b"])
        x = Fraction(s["p"], s["q"])
        support.add((x / t, t * x))
    u1, u2 = Fraction(15, 8), Fraction(40, 3)
    v1, v2 = Fraction(1, 30), Fraction(2, 15)
    rectangle = {
        "u1_v1": (u1, v1) in support,
        "u2_v1": (u2, v1) in support,
        "u1_v2": (u1, v2) in support,
        "u2_v2": (u2, v2) in support,
    }
    assert rectangle == {"u1_v1": True, "u2_v1": True, "u1_v2": True, "u2_v2": False}

    report = {
        "stage": "14-t58",
        "input": {
            "reciprocal_states": len(reps),
            "invisible_states": len(invisible),
            "fixed_U_fibers": len(by_u),
        },
        "toroidal_reconstruction": {
            "identity": "u=x/t, v=t*x; t^2=v/u, x^2=u*v",
            "physical_chamber": "t<x<1/t iff u>1 and 0<v<1",
            "chamber_checks": chamber_checks,
            "inverse_checks": inverse_checks,
            "proved": True,
        },
        "mask_classification": {
            "canonical_prime_and_fixed_U": "direction/pi-side only",
            "primitive_V": "V-side only",
            "invisible_branch": "radial: ell does not divide N(V)=k*delta",
            "hyperbola": "radial sharp product: eps*ell*N(U)*delta/2<=B",
            "interval_reconstruction": "toroidally separated: 1_{u>1}1_{0<v<1}",
            "bounded_masks_L2_safe_via_tH4": True,
            "sharp_product_cutoff_retained_via_tH2_policy": True,
            "direction_mask_checks": direction_mask_checks,
            "invisible_branch_norm_checks": invisible_branch_norm_checks,
            "hyperbola_checks": hyperbola_checks,
        },
        "radial_cell_energy": {
            "cell_key": "(U_unit,eps,k,ell,delta) on invisible branch",
            "cells": len(cells),
            "multiplicity_histogram": {str(k): v for k, v in sorted(hist.items())},
            "max_frozen_cell": max(map(len, cells.values())),
            "frozen_energy": radial_energy,
            "theoretical_cell_bound": "O(r2(ell)*r2(k*delta))=B^o(1); for split prime ell, r2(ell)=8",
            "weighted_cell_cauchy": "sum_cell |sum_{s in cell} w_s phase_s|^2 <= B^o(1)*sum_s |w_s|^2",
            "per_U": per_u,
            "support_energy_transfer_proved": True,
        },
        "non_cartesian_guard": {
            "U": list(witness_u),
            "u1": frac_str(u1),
            "u2": frac_str(u2),
            "v1": frac_str(v1),
            "v2": frac_str(v2),
            "rectangle_membership": rectangle,
            "single_cartesian_product_selector_valid": False,
        },
        "decision": {
            "STAGE14_T58": "COMPLETE_TOROIDAL_RECONSTRUCTION_MASK_SEPARATION_AND_RADIAL_CELL_ENERGY_TRANSFER",
            "PHYSICAL_INTERVAL_TOROIDAL_SEPARATION_PROVED": True,
            "TOROIDAL_INVERSE_SQUARE_COMPATIBILITY_PROVED": True,
            "CANONICAL_MASK_PI_SIDE_ONLY": True,
            "INVISIBLE_BRANCH_MASK_RADIAL_ONLY": True,
            "SHARP_HYPERBOLA_MASK_RADIAL_ONLY": True,
            "PHYSICAL_RADIAL_CELL_MULTIPLICITY_B_O1": True,
            "FIXED_U_PHYSICAL_SELECTOR_SUPPORT_ENERGY_TRANSFER_PROVED": True,
            "FULL_PHYSICAL_SELECTOR_SINGLE_CARTESIAN_PRODUCT": False,
            "SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED": False,
            "SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED": False,
            "SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED": False,
            "SHARED_U_MIXED_BRANCH_DISPERSION_PROVED": False,
            "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED": False,
            "TH16_NEEDED": True,
            "T_ROUTE_BLOCKED_WAITING_FOR_TH16": False,
            "NEXT": "Stage14-t59 attack SharedUCanonicalPrimeDeltaToroidalSecondMoment on the sharp ell*delta hyperbola; run tH16 in parallel on the same-modulus two-coordinate analytic theorem",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
