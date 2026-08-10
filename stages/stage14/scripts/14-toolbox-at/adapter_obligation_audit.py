from pathlib import Path

root = Path(__file__).resolve().parents[4]
at = (root / "stages/stage14/14-toolbox-at/result.md").read_text()
s20 = (root / "stages/stage14/14-s7-20/result.md").read_text()
t56 = (root / "stages/stage14/14-t56/result.md").read_text()
as_ = (root / "stages/stage14/14-toolbox-as/result.md").read_text()

required_at = [
"STAGE14_TOOLBOX_AT=COMPLETE_ADAPTER_OBLIGATION_LEDGER_AND_FAILURE_MODE_TESTS",
"S_CURRENT_RECEIVER=BalancedDoubleAllocationSquareDivisibility",
"S_EIGHT_CELL_COLLAPSE_ALLOWED=false",
"S_POSITIVE_SQUARE_DIVISIBILITY_MAY_BE_DISCARDED=false",
"FIXED_U_CURRENT_RECEIVER=SharedUInvisibleCenteredProjectiveSelectorDispersion",
"FIXED_U_RECEIVER_SUFFICIENT_FOR_INVISIBLE_SUBD=true",
"FIXED_U_MIXED_BRANCH_SEPARATE=true",
"COMPLETE_TRACE_IMPLIES_SPARSE_SELECTOR_DISPERSION=false",
"ONE_PRIME_CAUCHY_REASSEMBLY_ALLOWED=false",
"POST_SQUARECLASS_CIRCULAR_ENERGY_ALLOWED=false",
"TOOLBOX_H_CONTINUATION_NEEDED=false",
"CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
"NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]
for token in required_at:
    assert token in at, token

assert "BALANCED_DOUBLE_ALLOCATION_SQUARE_DIVISIBILITY_REQUIRED=true" in s20
assert "BALANCED_DOUBLE_ALLOCATION_SQUARE_DIVISIBILITY_POWER_SAVING_PROVED=false" in s20
assert "INVISIBLE_CENTERED_SELECTOR_IMPLIES_INVISIBLE_SUBD=true" in t56
assert "SHARED_U_MIXED_BRANCH_DISPERSION_PROVED=false" in t56
assert "DIRECT_IMPORTABLE_THEOREM_COUNT=0" in as_
assert "FIXED_U_TWO_PRIME_REASSEMBLY_WITH_ZERO_FIXED_LOSS_PROVED=false" in as_

# Failure-mode truth table: every unsafe promotion remains rejected.
unsafe = {
    "stale_s_receiver": "S_STALE_PYTHAGOREAN_RECEIVER_CURRENT=false",
    "eight_cell_collapse": "S_EIGHT_CELL_COLLAPSE_ALLOWED=false",
    "complete_to_sparse": "COMPLETE_TRACE_IMPLIES_SPARSE_SELECTOR_DISPERSION=false",
    "one_prime_cauchy": "ONE_PRIME_CAUCHY_REASSEMBLY_ALLOWED=false",
    "circular_energy": "POST_SQUARECLASS_CIRCULAR_ENERGY_ALLOWED=false",
}
assert all(token in at for token in unsafe.values())
print("Stage14-toolbox-at obligation and failure-mode audit: OK")
