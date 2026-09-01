#!/usr/bin/env python3
from __future__ import annotations

from sympy import Matrix

import diagnose_stage32_post1473_integral_picard_support_selfsq_preflight as v8

EXPECTED_REDUCED_TRANSLATION_SHA256 = "e9e9570e4cf17fa8e1d4ce6663c56e502cd05fecce51d723518f8fe81a19898a"
EXPECTED_ORIGINAL_TRANSLATION_SHA256 = "45493b2f889c4cb288341c18e7a34e34617efe639428471665860eb315258779"
EXPECTED_PICARD_COORDINATES_SHA256 = "2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726"
EXPECTED_ALL140_PAIRINGS_SHA256 = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
EXPECTED_SELF_INTERSECTION = 758
EXPECTED_SUPPORT = 47
EXPECTED_ZERO_EXCEPTIONAL_INDICES = [5]

_ORIGINAL_WRAPPER = v8.reconstruct_witness_with_self_intersection


def reconstruct_witness_with_retained_body(**kwargs) -> dict:
    """Recover the prior V6/V7/V8 body only when every retained digest matches.

    This does not promote a newly found support-47 witness.  It reuses the
    unchanged V6 candidate/exact replay path and persists the reconstructed
    integer vectors only if they reproduce the already retained SHA256 locks.
    """
    witness = _ORIGINAL_WRAPPER(**kwargs)

    data = kwargs["data"]
    z = tuple(int(value) for value in kwargs["z"])
    Mred = kwargs["Mred"]
    U = kwargs["U"]
    y0 = kwargs["y0"]
    rvars = kwargs["rvars"]
    model = kwargs["model"]

    rv = Matrix([int(model.eval(var, model_completion=True).as_long()) for var in rvars])
    original_t = U * rv
    picard = data["x0_map"] * Matrix(z) + data["K"] * original_t
    pairings = y0 + Mred * rv

    reduced_translation = [int(value) for value in rv]
    original_translation = [int(value) for value in original_t]
    picard_coordinates = [int(value) for value in picard]
    all140_pairings = [int(pairings[i, 0]) for i in range(pairings.rows)]

    locks = {
        "reduced_translation_sha256": (v8.v5.csha(reduced_translation), EXPECTED_REDUCED_TRANSLATION_SHA256),
        "original_translation_sha256": (v8.v5.csha(original_translation), EXPECTED_ORIGINAL_TRANSLATION_SHA256),
        "picard_coordinates_sha256": (v8.v5.csha(picard_coordinates), EXPECTED_PICARD_COORDINATES_SHA256),
        "all140_pairings_sha256": (v8.v5.csha(all140_pairings), EXPECTED_ALL140_PAIRINGS_SHA256),
    }
    for key, (actual, expected) in locks.items():
        if actual != expected or witness.get(key) != expected:
            raise ValueError(f"V6 retained witness-body recovery hash mismatch at {key}: {actual} != {expected}")

    if int(witness.get("self_intersection")) != EXPECTED_SELF_INTERSECTION:
        raise ValueError("V7 retained self-intersection regression during witness-body recovery")
    if int(witness.get("positive_exceptional_support")) != EXPECTED_SUPPORT:
        raise ValueError("V6 retained support regression during witness-body recovery")
    if witness.get("zero_exceptional_indices") != EXPECTED_ZERO_EXCEPTIONAL_INDICES:
        raise ValueError("V6 retained zero-exceptional regression during witness-body recovery")

    witness["retained_witness_body_recovery"] = {
        "status": "EXACT_HASH_MATCH_TO_PRIOR_V6_V7_V8_WITNESS",
        "not_a_new_witness": True,
        "reduced_translation": reduced_translation,
        "original_translation": original_translation,
        "picard_coordinates": picard_coordinates,
        "all140_pairings": all140_pairings,
        "source_hash_locks": {
            key: expected for key, (_, expected) in locks.items()
        },
    }
    return witness


def main() -> None:
    # v8.main installs this wrapper into the unchanged V6 exact replay path.
    v8.reconstruct_witness_with_self_intersection = reconstruct_witness_with_retained_body
    v8.main()


if __name__ == "__main__":
    main()
