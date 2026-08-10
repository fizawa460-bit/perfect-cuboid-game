#!/usr/bin/env python3
"""Deterministic boundary audit for Stage14-toolbox-ap."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

FILES = {
    "ao": ROOT / "stages/stage14/14-toolbox-ao/result.md",
    "4cd": ROOT / "stages/stage14/14-4cd/result.md",
    "s717": ROOT / "stages/stage14/14-s7-17/result.md",
    "t53": ROOT / "stages/stage14/14-t53/result.md",
    "t54": ROOT / "stages/stage14/14-t54/result.md",
    "matrix": ROOT / "docs/stage14-toolbox/theorem-compatibility-matrix.md",
    "result": ROOT / "stages/stage14/14-toolbox-ap/result.md",
}

for label, path in FILES.items():
    if not path.is_file():
        raise SystemExit(f"missing {label}: {path}")

text = {label: path.read_text(encoding="utf-8") for label, path in FILES.items()}

required_upstream = {
    "ao": [
        "CENTERED_XI_K_DISPERSION_PROVED=false",
        "GLOBAL_PRINCIPAL_KUMMER_INCIDENCE_PROVED=false",
        "NONPRINCIPAL_SELECTOR_DISPERSION_PROVED=false",
    ],
    "4cd": [
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
    ],
    "s717": [
        "PRIME_PAIR_PROJECTIVE_SLOPE_DISPERSION_PROVED=false",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8",
    ],
    "t53": [
        "FROZEN_SHARED_U_GENERIC_BLOCKS=6",
        "GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_PROVED=false",
    ],
    "t54": [
        "FIXED_U_REDUCES_TO_ONE_DIMENSIONAL_CANONICAL_PRIME_SUM=false",
        "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false",
    ],
}
for label, needles in required_upstream.items():
    for needle in needles:
        if needle not in text[label]:
            raise SystemExit(f"{label} contract missing: {needle}")

matrix_tokens = [
    "**DIRECT**",
    "**ADAPTER_ONLY**",
    "**CONDITIONAL**",
    "**REJECT**",
    "PrimePairProjectiveSlopeDispersion",
    "SharedUBipartiteSquareclassEnergy",
    "per-modulus absolute completion",
    "U/V tensorization",
    "precompletion pair-to-cross-kernel collapse",
    "The unconditional physical whole-family exponent remains `7/8`",
]
for token in matrix_tokens:
    if token not in text["matrix"]:
        raise SystemExit(f"matrix token missing: {token}")

boundary_tokens = [
    "STAGE14_TOOLBOX_AP=COMPLETE_THEOREM_COMPATIBILITY_MATRIX_AND_IMPORT_REJECTION_AUDIT",
    "MERGED_S7_17_IMPORTED_AS_ADAPTER_ONLY=true",
    "FIXED_U_DIVISOR_FAN_IMPLIES_BIPARTITE_ENERGY=false",
    "ROW_COLUMN_ENERGY_GLOBALIZATION_ALLOWED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
    "TOOLBOX_H_REQUIRED_FOR_TOOLBOX_MAIN=false",
    "TH15_REPLACED_BY_TOOLBOX_H=false",
    "NEXT=Stage14-toolbox-aq",
]
for token in boundary_tokens:
    if token not in text["result"]:
        raise SystemExit(f"result boundary missing: {token}")

for forbidden in [
    "PRIME_PAIR_PROJECTIVE_SLOPE_DISPERSION_PROVED=true",
    "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=true",
    "GLOBAL_PRINCIPAL_KUMMER_INCIDENCE_PROVED=true",
]:
    if forbidden in text["result"]:
        raise SystemExit(f"forbidden promotion: {forbidden}")

print("Stage14-toolbox-ap compatibility audit: PASS")
