#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[4]
proof = (root / "stages/stage13/13-13fs/curved-region-self-contained-closure.md").read_text(encoding="utf-8")
result = (root / "stages/stage13/13-13fs/result.md").read_text(encoding="utf-8")

required_proof = [
    "R07_GATE_C=COMPLETE",
    "R07_VAALER_APPLIES_ONLY_TO_INNER_ANGLE_INTERVALS=true",
    "R07_PHYSICAL_CUTOFF_HANDLED_BY_MULTIPLICATIVE_SHELL=true",
    "R07_VAALER_ENDPOINT_DISCRETE_CONVENTION_EXPLICIT=true",
    "R07_PHYSICAL_EQUALITY_POINTS_RETAINED=true",
    "MESH_PER_COORD=O(log(2B)/eta)=O((log B)^9)",
    "BOX_COUNT=O((log B)^27)",
    "PER_BOX_FINITE_REMAINDER=O(B(log B)^-62)",
    "FINITE_REMAINDER_AFTER_ALL_BOXES=O(B(log B)^-35)",
    "CURVED_BOUNDARY_MAIN_MASS=O(B(log B)^-5)",
    "MESH_ERROR=O(B(log B)^-5)",
    "RETAINED_HARMONIC_POLYLOG=4*C_H+D_H+6",
]
for token in required_proof:
    assert token in proof, token

required_result = [
    "STAGE13_13FS=COMPLETE_R07_CURVED_REGION_SELF_CONTAINED_CLOSURE",
    "R07_REPAIR_BLOCKERS_OPEN=0",
    "R07_GATES_A_B_C_COMPLETE=true",
    "R07_GATE_D_HARDENING_REMAINS=true",
    "NEXT=13-13ft",
]
for token in required_result:
    assert token in result, token

# Exact ledger arithmetic.
assert 9 * 3 == 27
assert 27 - 62 == -35
assert -8 + 3 == -5
assert 4 * 0 + 0 + 6 == 6
for c_h in (0, 1, 3, 7):
    for d_h in (0, 2, 5):
        assert (4 * c_h + 4) + d_h + 2 == 4 * c_h + d_h + 6

# Wing exponents are strictly below the cubic-log main scale.
assert 9 / 4 < 3
assert 5 / 2 < 3
assert 2 < 3

# The rectangle tail exponent is exact.
from fractions import Fraction
assert Fraction(1, 4) - Fraction(1, 16) == Fraction(3, 16)

# Semantic separation guards.
assert "It is **not** used to approximate the curved physical cutoff" in proof
assert "This is an exact discrete statement, not a measure-zero argument." in proof
assert "There is no factor `N_box`" in proof

print("STAGE13_13FS_AUDIT=PASS")
print("R07_GATE_C=COMPLETE")
print("R07_REPAIR_BLOCKERS_OPEN=0")
print("DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY")
