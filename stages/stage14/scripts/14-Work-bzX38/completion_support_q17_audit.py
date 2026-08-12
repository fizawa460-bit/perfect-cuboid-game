from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

RESULT = ROOT / "stages/stage14/14-Work-bzX38/result.md"
MATRIX = ROOT / "docs/stage14-toolbox/work-bzX38-receiver-matrix.md"
Q17 = ROOT / "docs/stage14-q17-summary.md"
Q17_RADAR = ROOT / "docs/stage14-q17-reciprocal-crt-literature-radar.md"
WORK37 = ROOT / "stages/stage14/14-Work-byX37/result.md"
MAIN = ROOT / "stages/stage14/14-4ge/result.md"
S = ROOT / "stages/stage14/14-s7-113/result.md"
T = ROOT / "stages/stage14/14-t149/result.md"
Q16 = ROOT / "docs/stage14-q16-summary.md"
CONTRACT = ROOT / "docs/stage14-toolbox/work-toolbox-x-task-contract.md"


def text(path: Path) -> str:
    assert path.exists(), path
    return path.read_text(encoding="utf-8")


r = text(RESULT)
m = text(MATRIX)
q17 = text(Q17)
radar = text(Q17_RADAR)
w37 = text(WORK37)
main = text(MAIN)
s = text(S)
t = text(T)
q16 = text(Q16)
contract = text(CONTRACT)

# Canonical XQ contract is merged and this run obeys the new decision record.
assert "Stage14-Work-toolbox-XQ" in contract
for needle in [
    "TOOLBOX_COMPONENT_COMPLETE=true",
    "X_COMPONENT_COMPLETE=true",
    "Q_COMPONENT=COMPLETE",
    "Q_TRIGGER_STAGE=Stage14-4gd+Stage14-4ge",
    "EXACT_Q_OBSTRUCTION=FixedAgreementPairRadialLinearTwoLevelDivisorCRTReciprocalSolvabilitySupport",
    "Q_LEDGER_BASELINE=Stage14-q16",
    "Q_RESULT_IMPORTED_BACK_TO_X=true",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]:
    assert needle in r, needle

# Merged predecessor locks.
assert "GLOBAL_S_HEAVY_RECEIVERS_ALL_REDUCED_TO_CONDITIONAL_PHYSICAL_COMPLETION_OR_LIFT=true" in w37
assert "COMPLETION_DEFICIT_EXACTLY_SPLITS_AS_DELTA_REC_PLUS_DELTA_POST=true" in main
assert "FIXED_PAIR_RECIPROCAL_CANDIDATE_MULTIPLICITY=Bo1" in main
assert "TWO_LEVEL_COMPLETION_DEFICIT_LEDGER_EXACT=true" in s
assert "S7_113_NEW_AUXILIARY_H_NEEDED=false" in s
assert "RESIDUE_HOST_NORMALIZED_MANY_WIDTH_FLOOR_PROVED=true" in t
assert "SPARSE_SINGLE_INTERVAL_RESIDUE_NORMALIZED_NEAR_FULL_PROVED=true" in t
assert "FIXED_E_CONDITIONAL_PHYSICAL_LIFT_REMAINS=true" in q16
assert "Q16_CONDITIONAL_LIFT_EXTERNAL_SEARCH_TRIGGERED=false" in q16

# X38 must preserve route separation.
for needle in [
    "BOUNDED_WITNESS_MULTIPLICITY_DOES_NOT_IMPLY_EXISTENCE_DENSITY=true",
    "SUBPOLYNOMIAL_EXTENSION_FIBER_CANNOT_CLOSE_EXISTENTIAL_SUPPORT_DEFICIT=true",
    "GLOBAL_S_TWO_LEVEL_COMPLETION_QUANTIFIER_LANGUAGE_PROVED=true",
    "MAIN_FIXED_E_RECIPROCAL_CRT_REFINEMENT_CROSS_PROMOTED_TO_ALL_S=false",
    "FIXED_U_PRIME_OCCUPANCY_REMAINS_DISTINCT_FROM_GLOBAL_S_COMPLETION=true",
    "COMMON_COMPLETION_TO_GAUSSIAN_PRIME_OCCUPANCY_ADAPTER_PROVED=false",
]:
    assert needle in r, needle

# Finite sanity example: bounded witness multiplicity can coexist with tiny support.
# Each nonempty fiber has size <= 1, but only one ambient point has a witness.
for n in [10, 100, 1000]:
    fibers = [1] + [0] * (n - 1)
    assert max(fibers) <= 1
    support = sum(1 for x in fibers if x)
    assert support == 1
    assert support / n <= 0.1

# Nested-support exponent bookkeeping: total deficit is additive, not multiplicative.
def nested_deficits(kappa, sigma, tau):
    assert kappa >= sigma >= tau
    d1 = kappa - sigma
    d2 = sigma - tau
    return d1, d2, kappa - tau

for triple in [(0.40, 0.36, 0.31), (0.25, 0.25, 0.24), (0.5, 0.42, 0.42)]:
    d1, d2, total = nested_deficits(*triple)
    assert abs((d1 + d2) - total) < 1e-12

# q17 classification and handoff locks.
for needle in [
    "STAGE14_Q17=COMPLETE_RECIPROCAL_CRT_SUPPORT_LITERATURE_RADAR",
    "DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0",
    "RECIPROCAL_CRT_SUPPORT_DIRECT_THEOREM_FOUND=false",
    "DIVISOR_AP_MOMENT_TO_EXISTENTIAL_SUPPORT_ADAPTER_PROVED=false",
    "Q17_EXPLICIT_RECIPROCAL_SELECTOR_CONSTRUCTION_TEST",
    "Q17_DIVISOR_AP_FIRST_SECOND_MOMENT_SUPPORT_TRANSFER_TEST",
    "Q17_BINARY_FORM_DIVISOR_SUM_ENCODING_TEST",
]:
    assert needle in radar, needle

for needle in [
    "STAGE14_Q17=COMPLETE_RECIPROCAL_CRT_SUPPORT_LITERATURE_RADAR",
    "DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0",
    "RECIPROCAL_CRT_SUPPORT_DIRECT_THEOREM_FOUND=false",
    "Q17_POST_MASK_SEARCHED=false",
    "Q17_FIXED_U_SEARCHED=false",
]:
    assert needle in q17, needle

# Matrix mirrors integrated locks.
for needle in [
    "COMMON_SUPPORT_EXISTENCE_AFTER_MULTIPLICITY_EXHAUSTION_LANGUAGE_PROVED=true",
    "Q_COMPONENT=COMPLETE",
    "Q17_DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0",
    "COMMON_COMPLETION_TO_GAUSSIAN_PRIME_OCCUPANCY_ADAPTER_PROVED=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]:
    assert needle in m, needle

print("Stage14-Work-bzX38 + q17 completion-support audit: PASS")
