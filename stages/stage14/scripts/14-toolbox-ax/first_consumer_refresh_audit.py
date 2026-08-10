#!/usr/bin/env python3
"""Stage14-toolbox-ax: deterministic first-consumer / current-receiver audit."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

FILES = {
    "aw": ROOT / "stages/stage14/14-toolbox-aw/result.md",
    "four_cq": ROOT / "stages/stage14/14-4cq/result.md",
    "x8": ROOT / "stages/stage14/14-X8/result.md",
    "four_cr": ROOT / "stages/stage14/14-4cr/result.md",
    "s7_30": ROOT / "stages/stage14/14-s7-30/result.md",
    "s7_31": ROOT / "stages/stage14/14-s7-31/result.md",
    "t69": ROOT / "stages/stage14/14-t69/result.md",
    "t70": ROOT / "stages/stage14/14-t70/result.md",
    "ax": ROOT / "stages/stage14/14-toolbox-ax/result.md",
    "matrix": ROOT / "docs/stage14-toolbox/first-consumer-five-eighths-receiver-matrix.md",
}


def need(text: str, token: str, source: str) -> None:
    assert token in text, f"missing {token!r} in {source}"


def main() -> None:
    docs = {name: path.read_text() for name, path in FILES.items()}

    # toolbox-aw predecessor and its explicit next task.
    need(
        docs["aw"],
        "STAGE14_TOOLBOX_AW=COMPLETE_SUPERSEDED_CONSUMER_AUDIT_AND_THREE_QUARTER_RECEIVER_REFRESH",
        "aw",
    )
    need(
        docs["aw"],
        "NEXT=Stage14-toolbox-ax audit the first 4cq/s7-30/t69 consumers against the refreshed three-quarter certificates",
        "aw",
    )

    # 4cq -> X8 / 4cr chain.
    need(
        docs["four_cq"],
        "STAGE14_4CQ=COMPLETE_DUAL_COMMON_CORE_CAYLEY_DIVISOR_COLLAPSE_AND_SYMMETRIC_QUARTER_QUARTER_REDUCTION",
        "4cq",
    )
    need(docs["x8"], "STAGE14_X8=COMPLETE_TWO_THIRDS_MINIMAX", "X8")
    need(docs["x8"], "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=2/3", "X8")
    need(
        docs["four_cr"],
        "STAGE14_4CR=COMPLETE_TWO_THIRDS_PROMOTION_AND_CAYLEY_GAUSSIAN_ORIENTATION_FACTORIZATION",
        "4cr",
    )
    need(docs["four_cr"], "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=2/3", "4cr")
    need(
        docs["four_cr"],
        "REMAINING_RECEIVER=TwoThirdsCayleyGaussianCommonGcdRootProductIncidence",
        "4cr",
    )

    # Canonical merged s7-30 must be the 11/16 theorem, not the closed-unmerged
    # alternate short-cofactor PR that reused the same stage label.
    need(docs["s7_30"], "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/16", "s7-30")
    need(
        docs["s7_30"],
        "TopCornerOppositeSignedQuotientCommonGcdRootProductIncidence",
        "s7-30",
    )
    assert "QuarterPhiFixedXYCommonCoreReciprocalFiber" not in docs["s7_30"], (
        "main s7-30 unexpectedly matches the closed-unmerged alternate PR"
    )

    # s7-31 is the strongest currently merged whole-family certificate.
    need(docs["s7_31"], "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8", "s7-31")
    need(docs["s7_31"], "oddpart(h)^2 | C*u_res", "s7-31")
    need(
        docs["s7_31"],
        "FiveEighthsTwoBoundaryCommonCoreReciprocalIncidence",
        "s7-31",
    )

    # t69 -> t70 chain remains fixed-U and separate.
    need(
        docs["t69"],
        "STAGE14_T69=COMPLETE_NONCANONICAL_CAYLEY_FACTOR_AND_COMMON_SUPPORT_REDUCTION",
        "t69",
    )
    need(
        docs["t70"],
        "STAGE14_T70=COMPLETE_FULL_COMMON_SUPPORT_CRT_ROOTLINE_AND_SMALL_OVERLAP_REDUCTION",
        "t70",
    )
    need(docs["t70"], "T69_EXTRA_ONLY_DICHOTOMY_SUPERSEDED=true", "t70")
    need(docs["t70"], "LARGE_FULL_COMMON_SUPPORT_ROOTLINE_BRANCH_NEAR_LINEAR=true", "t70")
    need(
        docs["t70"],
        "SHARED_U_PRIVATE_LARGEST_PRIME_SMALL_COMMON_SUPPORT_PHYSICAL_SQUARE_SCALE_ENERGY_PROVED=false",
        "t70",
    )
    need(docs["t70"], "TH19_NEEDED=false", "t70")

    # Exact exponent ordering: each historical global barrier is weaker than 5/8.
    e_34 = Fraction(3, 4)
    e_1116 = Fraction(11, 16)
    e_23 = Fraction(2, 3)
    e_58 = Fraction(5, 8)
    assert e_58 < e_23 < e_1116 < e_34
    assert e_34 - e_58 == Fraction(1, 8)

    # Lock the ax output boundary and matrix.
    boundary = [
        "STAGE14_TOOLBOX_AX=COMPLETE_FIRST_CONSUMER_AUDIT_AND_FIVE_EIGHTHS_RECEIVER_REFRESH",
        "CANONICAL_MERGED_S7_30_PR=517",
        "CLOSED_UNMERGED_ALTERNATE_S7_30_PR_521_CANONICAL=false",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8",
        "CURRENT_GLOBAL_S_RECEIVER=FiveEighthsTwoBoundaryCommonCoreReciprocalIncidence",
        "CURRENT_FIXED_U_RECEIVER=SharedUPrivateLargestPrimeSmallCommonSupportPhysicalSquareScaleEnergy",
        "GLOBAL_S_AND_FIXED_U_RECEIVERS_EQUIVALENT=false",
        "TH19_NEEDED=false",
        "TOOLBOX_H_CONTINUATION_NEEDED=false",
        "NEW_AX_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
    ]
    for token in boundary:
        need(docs["ax"], token, "ax")

    need(docs["matrix"], "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8", "matrix")
    need(
        docs["matrix"],
        "CURRENT_FIXED_U_RECEIVER=SharedUPrivateLargestPrimeSmallCommonSupportPhysicalSquareScaleEnergy",
        "matrix",
    )

    report = {
        "stage": "14-toolbox-ax",
        "audited_sources": ["4cq", "s7-30", "t69"],
        "audited_first_consumers": ["X8", "4cr", "s7-31", "t70"],
        "canonical_s7_30_pr": 517,
        "closed_unmerged_duplicate_s7_30_pr": 521,
        "historical_global_exponents": ["3/4", "11/16", "2/3"],
        "current_global_exponent": "5/8",
        "improvement_over_aw_3_4": "1/8",
        "current_global_receiver": "FiveEighthsTwoBoundaryCommonCoreReciprocalIncidence",
        "current_fixed_u_receiver": "SharedUPrivateLargestPrimeSmallCommonSupportPhysicalSquareScaleEnergy",
        "toolbox_h_continuation_needed": False,
        "boundary_locked": True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
