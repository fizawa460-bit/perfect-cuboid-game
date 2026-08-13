from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def text(rel: str) -> str:
    path = ROOT / rel
    assert path.exists(), path
    return path.read_text(encoding="utf-8")


result = text("stages/stage14/14-Work-ccX41/result.md")
matrix = text("docs/stage14-toolbox/work-ccX41-receiver-matrix.md")
q18 = text("stages/stage14/archive/docs/q-research/stage14-q18-summary.md")
radar = text("stages/stage14/archive/docs/q-research/stage14-q18-squareclass-reverse-literature-radar.md")
cbx40 = text("stages/stage14/14-Work-cbX40/result.md")
s125 = text("stages/stage14/14-s7-125/result.md")
t157 = text("stages/stage14/14-t157/result.md")
th33 = text("stages/stage14/14-t157/th33-target.md")
main_h = text("stages/stage14/14-4ghH/result.md")
q17 = text("stages/stage14/archive/docs/q-research/stage14-q17-summary.md")
contract = text("docs/stage14-toolbox/work-toolbox-x-task-contract.md")

# Canonical XQ invocation contract and predecessor boundary.
assert "Stage14-Work-toolbox-XQ" in contract
assert "LOCALIZED_EXTERNAL_GATE_NONPROPAGATION_LEMMA_PROVED=true" in cbx40
assert "Q18_PREMATURE_PENDING_S7_120_THEOREM_CONTRACT=true" in cbx40

# Current merged route locks.
for needle in [
    "S_MULTIPLICATIVE_REVERSE_POSTMASK_THREE_DEFICIT_LEDGER_PROVED=true",
    "S_ONE_DIMENSIONAL_MULTIPLICATIVE_REVERSE_THEOREM_CONTRACT_FROZEN=true",
    "S_POLYNOMIAL_PAIR_MULTIPLICATIVE_REVERSE_THEOREM_CONTRACT_FROZEN=true",
    "Q18_THEOREM_TARGETS_REFINED=true",
]:
    assert needle in s125, needle

for needle in [
    "SPARSE_AREA_LONG_SHARE_SAME_POINTWISE_PRIME_THEOREM=true",
    "T_ROUTE_H_NEEDED=true",
    "T_ROUTE_H_REQUEST=SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio",
    "TH33_NEEDED=true",
    "TH33_EXECUTED=false",
]:
    assert needle in t157, needle

for needle in [
    "TARGET_FROZEN=true",
    "REQUESTED_OBJECT=SuperKaiIndividualGaussianResidueLongIntervalPrimeOccupancyLowerRatio",
    "T(X;d,beta_*) >= B^(-o(1)) M(X;d)",
]:
    assert needle in th33, needle

assert "MINIMAL_UNRESOLVED_EXTERNAL_GATE=UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment" in main_h
assert "MAINLINE_BLOCKED_BY_H=true" in main_h
assert "STAGE14_Q17=COMPLETE_RECIPROCAL_CRT_SUPPORT_LITERATURE_RADAR" in q17

# X41 theorem-species partition and required XQ locks.
for needle in [
    "COMMON_HOST_ALGEBRA_DOES_NOT_IDENTIFY_CHARGED_SUPPORT_MEASURE=true",
    "SUBPOLYNOMIAL_HOST_FIBER_CANNOT_SCALARIZE_PAIR_SUPPORT=true",
    "S_NONALIGNED_COMMON_TRIPLE_PRODUCT_REVERSE_KERNEL_PROVED=true",
    "S_NONALIGNED_THEOREM_SPECIES_COUNT=2",
    "S_SCALAR_BRANCHES_SHARE_THEOREM_SPECIES=true",
    "S_POLYNOMIAL_PAIR_REQUIRES_DISTINCT_THEOREM_SPECIES=true",
    "Q_COMPONENT=COMPLETE",
    "Q_TRIGGER_STAGE=Stage14-s7-122+Stage14-s7-125",
    "Q_LEDGER_BASELINE=Stage14-q17",
    "Q_RESULT_IMPORTED_BACK_TO_X=true",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
    "MAINLINE_H_NEEDED=true",
    "S_ROUTE_H_NEEDED=false",
    "FIXED_U_H_NEEDED=true",
    "TH33_NEEDED=true",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]:
    assert needle in result, needle

# q18 classification locks.
for needle in [
    "STAGE14_Q18=COMPLETE_FILTERED_TRIPLE_PRODUCT_REVERSE_SUPPORT_LITERATURE_RADAR",
    "DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0",
    "SCALAR_TRIPLE_PRODUCT_REVERSE_DIRECT_THEOREM_FOUND=false",
    "POLYNOMIAL_PAIR_FIBERED_REVERSE_DIRECT_THEOREM_FOUND=false",
    "FILTERED_TAU3_TO_SUPPORT_ADAPTER_PROVED=false",
    "PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false",
    "Q18_SCALAR_FILTERED_TAU3_ENCODING_TEST",
    "Q18_POLYNOMIAL_PAIR_FIBERED_SUPPORT_MOMENT_TEST",
]:
    assert needle in radar, needle

for needle in [
    "STAGE14_Q18=COMPLETE_FILTERED_TRIPLE_PRODUCT_REVERSE_SUPPORT_LITERATURE_RADAR",
    "DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0",
    "Q18_POST_MASK_SEARCHED=false",
    "Q18_FIXED_U_SEARCHED=false",
    "Q18_TH33_DUPLICATED=false",
]:
    assert needle in q18, needle

# Matrix mirrors the charged-measure separation and H routing.
for needle in [
    "S_NONALIGNED_THEOREM_SPECIES_COUNT=2",
    "S_POLYNOMIAL_PAIR_SCALAR_HOST_REPLACEMENT_PROVED=false",
    "Q18_DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0",
    "FIXED_U_H_NEEDED=true",
    "TH33_NEEDED=true",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]:
    assert needle in matrix, needle

# Finite sanity model: one scalar host can carry several charged pairs with
# different pair-dependent predicates, so scalar support does not determine
# pair support even when the host fiber is finite/subpolynomial.
pairs = [(1, 6), (2, 3)]
assert all(E * m == 6 for E, m in pairs)
pair_filter = {(1, 6): 0, (2, 3): 1}
scalar_host_nonempty = any(pair_filter[p] for p in pairs)
assert scalar_host_nonempty
assert sum(pair_filter.values()) == 1
assert len(pairs) == 2

# Deficit bookkeeping remains additive across nested supports.
def total_deficit(sig_pre, sig_mult, sig_rev2, tau):
    assert sig_pre >= sig_mult >= sig_rev2 >= tau
    return (sig_pre - sig_mult) + (sig_mult - sig_rev2) + (sig_rev2 - tau)

for vals in [(0.40, 0.37, 0.34, 0.31), (0.25, 0.25, 0.24, 0.24)]:
    d = total_deficit(*vals)
    assert abs(d - (vals[0] - vals[3])) < 1e-12

print("Stage14-Work-ccX41 + q18 squareclass-reverse audit: PASS")
