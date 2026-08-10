#!/usr/bin/env python3
"""Stage14-toolbox-ay: audit first 4cr/s7-31/t70 consumers and current receivers."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

FILES = {
    "ax": ROOT / "stages/stage14/14-toolbox-ax/result.md",
    "four_cr": ROOT / "stages/stage14/14-4cr/result.md",
    "x9": ROOT / "stages/stage14/14-X9/result.md",
    "four_cs": ROOT / "stages/stage14/14-4cs/result.md",
    "s7_31": ROOT / "stages/stage14/14-s7-31/result.md",
    "s7_32": ROOT / "stages/stage14/14-s7-32/result.md",
    "t70": ROOT / "stages/stage14/14-t70/result.md",
    "t71": ROOT / "stages/stage14/14-t71/result.md",
    "t72": ROOT / "stages/stage14/14-t72/result.md",
    "four_ct": ROOT / "stages/stage14/14-4ct/result.md",
    "x10": ROOT / "stages/stage14/14-X10/result.md",
    "ay": ROOT / "stages/stage14/14-toolbox-ay/result.md",
    "matrix": ROOT / "docs/stage14-toolbox/unique-top-corner-pell-receiver-matrix.md",
}


def need(text: str, token: str, source: str) -> None:
    assert token in text, f"missing {token!r} in {source}"


def main() -> None:
    docs = {name: path.read_text() for name, path in FILES.items()}

    # Predecessor and explicit ay scope.
    need(
        docs["ax"],
        "STAGE14_TOOLBOX_AX=COMPLETE_FIRST_CONSUMER_AUDIT_AND_FIVE_EIGHTHS_RECEIVER_REFRESH",
        "ax",
    )
    need(
        docs["ax"],
        "NEXT=Stage14-toolbox-ay audit first 4cr/s7-31/t70 consumers against the five-eighths certificate",
        "ax",
    )
    need(docs["ax"], "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8", "ax")

    # First 4cr consumers: X9 and 4cs.
    need(
        docs["four_cr"],
        "STAGE14_4CR=COMPLETE_TWO_THIRDS_PROMOTION_AND_CAYLEY_GAUSSIAN_ORIENTATION_FACTORIZATION",
        "4cr",
    )
    need(
        docs["x9"],
        "STAGE14_X9=COMPLETE_FIVE_EIGHTHS_PROMOTION_AND_UPPER_CORE_LOWER_CORELESS_BOUNDARY_SPLIT",
        "X9",
    )
    need(docs["x9"], "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8", "X9")
    need(
        docs["four_cs"],
        "STAGE14_4CS=COMPLETE_FIVE_EIGHTHS_PROMOTION_COMMON_GCD_ROOT_GCD_IDENTIFICATION_AND_TWO_BOUNDARY_SPLIT",
        "4cs",
    )
    need(docs["four_cs"], "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8", "4cs")
    need(docs["four_cs"], "FIVE_EIGHTHS_SATURATION_COMPONENT_COUNT=2", "4cs")
    need(docs["four_cs"], "ODDPART_H_EQUALS_ODDPART_GCD_XY=true", "4cs")

    # First s7-31 decisive consumer: s7-32 unique top corner.
    need(docs["s7_31"], "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8", "s7-31")
    need(
        docs["s7_32"],
        "STAGE14_S7_32=COMPLETE_ONE_HOST_GAUSSIAN_RECONSTRUCTION_AND_UNIQUE_TOP_CORNER_5_8_LOCALIZATION",
        "s7-32",
    )
    need(docs["s7_32"], "OLD_FIVE_EIGHTHS_LOWER_CORNER_SURVIVES=false", "s7-32")
    need(docs["s7_32"], "OLD_FIVE_EIGHTHS_TOP_EDGE_PHI_LT_1_4_SURVIVES=false", "s7-32")
    need(docs["s7_32"], "UNIQUE_FIVE_EIGHTHS_SATURATION=(theta,phi)=(5/16,1/4)", "s7-32")
    need(
        docs["s7_32"],
        "REMAINING_RECEIVER=TopCornerCommonCoreXiGaussianSquareHostPrimitiveAgreementIncidence",
        "s7-32",
    )

    # Current merged global refinements of that same unique corner.
    need(
        docs["four_ct"],
        "STAGE14_4CT=COMPLETE_TOP_CORNER_RESIDUAL_HOST_GCD_PEEL_AND_PRIMITIVE_GAUSSIAN_COMMON_CORE_LIFT",
        "4ct",
    )
    need(docs["four_ct"], "LOWER_FIVE_EIGHTHS_RECEIVER_SURVIVES=false", "4ct")
    need(docs["four_ct"], "FIVE_EIGHTHS_SATURATION_REQUIRES_RESIDUAL_HOST_GCD=Bo1", "4ct")
    need(docs["four_ct"], "FIVE_EIGHTHS_SATURATION_GOOD_COMMON_CORE_EXPONENT=3/8", "4ct")
    need(
        docs["four_ct"],
        "REMAINING_RECEIVER=TopCornerPrimitiveXiResidualGaussianCoreAgreementIncidence",
        "4ct",
    )

    need(
        docs["x10"],
        "STAGE14_X10=COMPLETE_TOP_CORNER_ROOT_GCD_DICHOTOMY_AND_DOMINANT_CAYLEY_SHORT_COFACTOR_REDUCTION",
        "X10",
    )
    need(docs["x10"], "FIVE_EIGHTHS_SATURATION_COMPONENT_COUNT=1", "X10")
    need(docs["x10"], "POTENTIAL_SATURATION_H_EXPONENT_MAX=1/16", "X10")
    need(docs["x10"], "POTENTIAL_SATURATION_DOMINANT_CAYLEY_FACTOR_EXPONENT_MIN=1/8", "X10")
    need(docs["x10"], "POTENTIAL_SATURATION_DOMINANT_CAYLEY_SHORT_COFACTOR_EXPONENT_MAX=1/8", "X10")
    need(
        docs["x10"],
        "REMAINING_RECEIVER=TopCornerSmallRootGcdDominantCayleyGaussianShortCofactorIncidence",
        "X10",
    )

    # First t70 consumer and its current t72 successor.
    need(
        docs["t70"],
        "STAGE14_T70=COMPLETE_FULL_COMMON_SUPPORT_CRT_ROOTLINE_AND_SMALL_OVERLAP_REDUCTION",
        "t70",
    )
    need(
        docs["t71"],
        "STAGE14_T71=COMPLETE_PHYSICAL_GAUSSIAN_ANGULAR_AND_SQUARECLASS_FOUR_CELL_TRANSFER_REDUCTION",
        "t71",
    )
    need(docs["t71"], "CAYLEY_COMMON_SUPPORT_AND_KAPPA_TRANSFER_COPRIME=true", "t71")
    need(
        docs["t72"],
        "STAGE14_T72=COMPLETE_KAPPA_DENOMINATOR_TAG_FULL_CAYLEY_ROOTLINE_AND_PELL_SMOOTH_REDUCTION",
        "t72",
    )
    need(docs["t72"], "LARGE_ODD_KAPPA_CAYLEY_ROOTLINE_BRANCH_NEAR_LINEAR=true", "t72")
    need(
        docs["t72"],
        "SHARED_U_SMALL_ODD_KAPPA_CANONICAL_LARGEST_PRIME_PELL_SMOOTH_PHYSICAL_ENERGY_PROVED=false",
        "t72",
    )
    need(docs["t72"], "TH19_NEEDED=true", "t72")
    need(docs["t72"], "TH19_REQUESTED_OBJECT=SmallOddKappaCanonicalLargestPrimePellSmoothEnergy", "t72")

    # Exponent ledger: ay localizes equality but owns no improvement below 5/8.
    e_58 = Fraction(5, 8)
    e_sqrt = Fraction(1, 2)
    assert e_58 - e_sqrt == Fraction(1, 8)
    assert Fraction(1, 16) < Fraction(1, 8) < Fraction(3, 8)

    # Open draft s7-33 must not already be a merged canonical result on this branch base.
    assert not (ROOT / "stages/stage14/14-s7-33/result.md").exists(), (
        "s7-33 result is present on branch base; re-audit its merge status before using this ay guard"
    )

    boundary = [
        "STAGE14_TOOLBOX_AY=COMPLETE_FIRST_CONSUMER_AUDIT_AND_UNIQUE_TOP_CORNER_PELL_REFRESH",
        "FIRST_4CR_CONSUMERS_AUDITED=true",
        "FIRST_S7_31_CONSUMERS_AUDITED=true",
        "FIRST_T70_CONSUMER_AUDITED=true",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8",
        "FIVE_EIGHTHS_SATURATION_COMPONENT_COUNT=1",
        "OLD_AX_TWO_BOUNDARY_RECEIVER_CURRENT=false",
        "FOUR_CS_TWO_BOUNDARY_SATURATION_METADATA_CURRENT=false",
        "FOUR_CT_AND_X10_FILTERS_SIMULTANEOUSLY_APPLICABLE_TO_SATURATING_PHYSICAL_PACKET=true",
        "CURRENT_GLOBAL_TOOLBOX_RECEIVER=TopCornerPrimitiveResidualGaussianCoreSmallRootGcdDominantCayleyShortCofactorIncidence",
        "CURRENT_GLOBAL_TOOLBOX_RECEIVER_PROVED=false",
        "CURRENT_FIXED_U_RECEIVER=SharedUSmallOddKappaCanonicalLargestPrimePellSmoothPhysicalEnergy",
        "TH19_NEEDED=true",
        "TH19_REQUESTED_OBJECT=SmallOddKappaCanonicalLargestPrimePellSmoothEnergy",
        "T72_CROSS_PROMOTED_TO_GLOBAL_TOP_CORNER=false",
        "OPEN_S7_33_DRAFT_USED_AS_CANONICAL_SOURCE=false",
        "TOOLBOX_H_CONTINUATION_NEEDED=false",
        "NEW_AY_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
    ]
    for token in boundary:
        need(docs["ay"], token, "ay")

    need(docs["matrix"], "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8", "matrix")
    need(
        docs["matrix"],
        "TopCornerPrimitiveResidualGaussianCoreSmallRootGcdDominantCayleyShortCofactorIncidence",
        "matrix",
    )
    need(
        docs["matrix"],
        "SharedUSmallOddKappaCanonicalLargestPrimePellSmoothPhysicalEnergy",
        "matrix",
    )
    need(docs["matrix"], "TH19_NEEDED=true", "matrix")

    report = {
        "stage": "14-toolbox-ay",
        "audited_sources": ["4cr", "s7-31", "t70"],
        "first_consumers": ["X9", "4cs", "s7-32", "t71"],
        "current_global_refinements": ["4ct", "X10"],
        "current_fixed_u_refinement": "t72",
        "current_global_exponent": "5/8",
        "current_gap_to_sqrt": "1/8",
        "unique_saturation": ["5/16", "1/4"],
        "global_receiver": "TopCornerPrimitiveResidualGaussianCoreSmallRootGcdDominantCayleyShortCofactorIncidence",
        "fixed_u_receiver": "SharedUSmallOddKappaCanonicalLargestPrimePellSmoothPhysicalEnergy",
        "th19_needed": True,
        "open_s7_33_used": False,
        "toolbox_h_continuation_needed": False,
        "boundary_locked": True,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
