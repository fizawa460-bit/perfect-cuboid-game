#!/usr/bin/env python3
"""Run the stage-five audit with a bounded, larger-stack saturation step."""

from __future__ import annotations

from fractions import Fraction
from typing import Any

import audit_two_face_rank_height_stage5 as base


def audit_generator_7_32_fixed(
    by_index: dict[int, dict[str, Any]],
    saturation_bound: int,
    timeout: int,
) -> dict[str, Any]:
    item = by_index.get(base.GENERATOR_SOURCE_INDEX)
    if item is None:
        raise ValueError(f"source index {base.GENERATOR_SOURCE_INDEX} is missing")
    if str(item["lambda"]) != base.GENERATOR_LAMBDA:
        raise ValueError(
            f"source index {base.GENERATOR_SOURCE_INDEX} has lambda={item['lambda']}"
        )
    lam = Fraction(base.GENERATOR_LAMBDA)
    a2, a4 = base.curve_coefficients(lam)
    observed = base.point_from_record(item["weierstrass_point"])
    script = f"""
default(parisizemax,500000000);
default(parisize,100000000);
default(realprecision,100);
E=ellinit([0,{base.gp_fraction(a2)},0,{base.gp_fraction(a4)},0]);
P={base.gp_point(observed)};
W=ellsaturation(E,[P],{saturation_bound});
print("SATURATED_GENERATOR_COUNT=",#W);
print("SATURATED_GENERATOR=",W[1]);
regP=matdet(ellheightmatrix(E,[P]));
regW=matdet(ellheightmatrix(E,W));
print("OBSERVED_REGULATOR=",regP);
print("SATURATED_REGULATOR=",regW);
print("INDEX_SQUARED=",round(regP/regW));
quit;
"""
    raw = base.run_gp(script, timeout)
    generator = base.parse_gp_point(base.text_field(raw, "SATURATED_GENERATOR"))
    if not base.point_on_curve(generator, lam):
        raise ArithmeticError("PARI saturated generator is not on the curve")
    relation = base.identify_generator_relation(observed, generator, lam)
    return {
        "valid": relation is not None,
        "lambda": base.GENERATOR_LAMBDA,
        "source_index": base.GENERATOR_SOURCE_INDEX,
        "source_tuple": item["source_tuple"],
        "saturation_bound": saturation_bound,
        "observed_point": base.point_record(observed),
        "saturated_generator": base.point_record(generator),
        "saturated_generator_count": base.integer_field(
            raw, "SATURATED_GENERATOR_COUNT"
        ),
        "observed_regulator_raw": base.text_field(raw, "OBSERVED_REGULATOR"),
        "saturated_regulator_raw": base.text_field(raw, "SATURATED_REGULATOR"),
        "index_squared": base.integer_field(raw, "INDEX_SQUARED"),
        "exact_relation": relation,
        "raw_pari_output": raw,
        "scope": {
            "certified": (
                "the displayed group-law relation is an exact rational identity; "
                f"the PARI saturation result excludes index primes below {saturation_bound}"
            ),
            "not_certified": (
                "full saturation at primes at or above the chosen bound"
            ),
        },
    }


base.audit_generator_7_32 = audit_generator_7_32_fixed

if __name__ == "__main__":
    raise SystemExit(base.main())
