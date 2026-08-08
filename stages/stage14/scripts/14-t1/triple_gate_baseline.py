#!/usr/bin/env python3
"""Stage14-t1 deterministic triple-gate baseline audit.

This audit does not search beyond the frozen Stage14 ceiling.  It repackages the
two-route Stage14-2 census into a triple-specific ledger, verifies the smooth
fixed-base genus-5 model on representative physical parameters, records the
exceptional base values, and freezes the physical one-fiber height comparison.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CENSUS = ROOT / "stages/stage14/data/14-2/final_census_audit.json"
OUTPUT = ROOT / "stages/stage14/data/14-t1/triple_gate_baseline.json"


def A(t: Fraction) -> Fraction:
    return (1 - t * t) / (1 + t * t)


def C(t: Fraction) -> Fraction:
    return Fraction(2, 1) / (t * t) - 1


def quartic_simple(coef: Fraction) -> bool:
    # q^4 + 2*coef*q^2 + 1 has repeated roots iff coef^2=1.
    return coef * coef != 1


def family_checks() -> dict:
    samples = [Fraction(3, 4), Fraction(4, 3), Fraction(5, 12)]
    checked = []
    for t in samples:
        a = A(t)
        c = C(t)
        difference = a - c
        expected = -Fraction(2, 1) / (t * t * (1 + t * t))
        assert difference == expected
        assert quartic_simple(a)
        assert quartic_simple(c)
        assert a != c
        checked.append(
            {
                "t": str(t),
                "A": str(a),
                "C": str(c),
                "A_minus_C": str(difference),
                "space_quartic_simple": True,
                "third_face_quartic_simple": True,
                "branch_sets_disjoint": True,
            }
        )

    # A connected (Z/2)^2 cover of P1 with 8 simple branch values has
    # degree 4.  Every branch value contributes two ramification points of
    # index 2, hence total ramification 16:
    #   2g-2 = 4*(-2)+16 = 8, so g=5.
    total_ramification = 16
    genus = (4 * (-2) + total_ramification + 2) // 2
    assert genus == 5

    return {
        "space_quartic": "W^2=q^4+2Aq^2+1, A=(1-t^2)/(1+t^2)",
        "third_face_quartic": "R^2=q^4+2Cq^2+1, C=2/t^2-1",
        "difference_identity": "A-C=-2/(t^2(1+t^2))",
        "sample_checks": checked,
        "generic_cover_degree": 4,
        "generic_simple_branch_values": 8,
        "riemann_hurwitz_total_ramification": total_ramification,
        "generic_genus": genus,
        "complex_exceptional_base_values": ["0", "infinity", "+1", "-1", "+i", "-i"],
        "physical_positive_pythagorean_base_hits_exceptional_set": False,
        "note": "For a genuine primitive Pythagorean face t=X/S>0; t=0 is degenerate and t=1 would require equal legs. The remaining listed exceptional values are non-real or projective boundary values.",
    }


def height_checks() -> dict:
    tests = []
    for u, v, delta in [(2, 5, 1), (3, 7, 2), (5, 13, 1)]:
        h2 = Fraction(u * u + v * v, delta)
        assert Fraction(v * v, 2) < h2 < 2 * v * v
        tests.append({"u": u, "v": v, "delta": delta, "H2": str(h2)})
    return {
        "second_face_parameter": "q=u/v in lowest terms, 0<u<v",
        "H2_formula": "H2=(u^2+v^2)/delta, delta in {1,2}",
        "H2_bounds": "v^2/2 < H2 < 2v^2",
        "physical_height_sandwich": "S1*H2/(sqrt(2)g) < d < sqrt(3)*S1*H2/g",
        "fiber_denominator_scale": "v asymp sqrt(Bg/S1)",
        "sample_checks": tests,
    }


def finite_baseline() -> dict:
    census = json.loads(CENSUS.read_text(encoding="utf-8"))
    assert census["metadata"]["all_11_rows_crosschecked_by_both_generation_routes"] is True
    assert census["metadata"]["max_verified_B"] == 2_000_000
    assert census["audit"]["all_rows_match_between_routes"] is True
    assert census["audit"]["all_triple_counts_zero_in_verified_range"] is True
    rows = [{"B": r["B"], "T": r["T"], "N2": r["N_2"]} for r in census["rows"]]
    assert len(rows) == 11
    assert all(r["T"] == 0 for r in rows)
    return {
        "source": "stages/stage14/data/14-2/final_census_audit.json",
        "generation_routes": 2,
        "rows": rows,
        "max_verified_B": 2_000_000,
        "T_at_max_verified_B": 0,
        "perfect_cuboid_nonexistence_inferred": False,
    }


def main() -> None:
    report = {
        "metadata": {
            "stage": "14-t1",
            "title": "Triple-gate definition, genus-5 family, finite baseline, and height audit",
            "counting_convention": "primitive canonical 0<a<b<c, gcd(a,b,c)=1, integer space diagonal d<=B",
        },
        "ledger": {
            "identity": "E(B)=N2(B)+3T(B)",
            "T_definition": "primitive canonical Stage14 objects with all three face diagonals integral",
            "triple_multiplicity_in_raw_pair_ledger": 3,
        },
        "fixed_base_family": family_checks(),
        "physical_height": height_checks(),
        "finite_baseline": finite_baseline(),
        "theorem_gap": {
            "fiberwise_finiteness_available": True,
            "uniform_moving_base_point_bound_available_for_this_physical_family": False,
            "T_o_sqrtB_proved": False,
            "power_saving_from_finite_zero_count_claimed": False,
            "next_attack": "quantitative moving-family bound with explicit dependence on base height and fiber point height",
        },
        "decision": {
            "STAGE14_T1": "COMPLETE_BASELINE_AND_THEOREM_GAP",
            "TRIPLE_GATE_INTERFACE_LOCKED": True,
            "TRIPLE_FIXED_BASE_GENUS": 5,
            "PHYSICAL_FIBERS_AVOID_GENERIC_DEGENERACY": True,
            "FINITE_TRIPLE_CENSUS_MAX_B": 2_000_000,
            "FINITE_TRIPLE_COUNT_AT_MAX_B": 0,
            "FINITE_ZERO_IMPLIES_NONEXISTENCE": False,
            "T_O_SQRT_B_PROVED": False,
            "NEXT": "Stage14-t2 quantitative moving-family attack",
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
