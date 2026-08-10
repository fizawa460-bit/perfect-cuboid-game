#!/usr/bin/env python3
"""Validate the frozen Stage14-t72 theorem boundary."""

from __future__ import annotations

from math import gcd
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "stages/stage14/data/14-t72/kappa_rootline_pell_smooth_frozen.json"
RESULT = ROOT / "stages/stage14/14-t72/result.md"


def main() -> None:
    data = json.loads(DATA.read_text())
    text = RESULT.read_text()

    assert data["stage"] == "14-t72"
    assert data["reciprocal_states"] == 560
    assert data["invisible_states"] == 419
    assert data["denominator_kappa_tag_checks"] == 419
    assert data["pell_norm_identity_checks"] == 419
    assert data["canonical_largest_prime_smooth_checks"] == 419
    assert data["angular_cofactor_checks"] == 419
    assert data["mutually_cayley_private_pairs"] == 5
    assert data["denominator_switch_formula_checks"] == 5
    assert data["odd_kappa_resultant_partition_checks"] == 5
    assert data["odd_kappa_crt_cayley_rootline_checks"] == 5
    assert data["J_kappa_coprime_checks"] == 5
    assert data["primitive_cayley_rootline_exhaustive_checks"] == 360
    assert data["synthetic_generic_pell_orbit_guard"]["checked_orbit_length"] == 8
    assert data["synthetic_generic_pell_orbit_guard"]["largest_prime_tag_hits"] == 1

    profiles = data["private_pair_profiles"]
    assert len(profiles) == 5
    for row in profiles:
        K = row["Kodd"]
        assert row["K_agree"] * row["K_switch"] == K
        assert gcd(row["K_agree"], row["K_switch"]) == 1
        assert gcd(row["J"], row["kappa"]) == 1
        if K > 1:
            assert (row["lambda"] * row["lambda"] - 1) % K == 0

    boundary = data["boundary"]
    assert boundary["CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT"] == "5/8"
    assert boundary["TH19_NEEDED"] is True
    assert boundary["TH19_REQUESTED_OBJECT"] == "SmallOddKappaCanonicalLargestPrimePellSmoothEnergy"
    assert boundary["NEXT"] == "Stage14-t73"

    required = [
        "STAGE14_T72=COMPLETE_KAPPA_DENOMINATOR_TAG_FULL_CAYLEY_ROOTLINE_AND_PELL_SMOOTH_REDUCTION",
        "SIGNED_SPLIT_BETA_EQUALS_GCD_KAPPA_V=true",
        "ODD_KAPPA_CROSS_RESULTANT_PARTITION_PROVED=true",
        "ODD_KAPPA_CRT_COMPRESSES_TO_ONE_CAYLEY_ROOT_LINE=true",
        "FIXED_ANCHOR_KAPPA_ROOTLINE_PARTNER_BOUND=(1+Z/Kodd)*Bo1",
        "SMALL_KAPPA_REAL_QUADRATIC_NORM_REDUCTION_PROVED=true",
        "CANONICAL_LARGEST_PRIME_PELL_SMOOTH_FILTER_PROVED=true",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8",
        "TH19_NEEDED=true",
        "TH19_REQUESTED_OBJECT=SmallOddKappaCanonicalLargestPrimePellSmoothEnergy",
        "T_ROUTE_BLOCKED_WAITING_FOR_TH19=false",
        "NEXT=Stage14-t73",
    ]
    for token in required:
        assert token in text, token

    print("Stage14-t72 frozen boundary: OK")


if __name__ == "__main__":
    main()
