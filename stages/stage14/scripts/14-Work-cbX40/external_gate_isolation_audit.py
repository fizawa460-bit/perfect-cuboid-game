from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def text(rel: str) -> str:
    p = ROOT / rel
    assert p.exists(), p
    return p.read_text(encoding="utf-8")


result = text("stages/stage14/14-Work-cbX40/result.md")
matrix = text("docs/stage14-toolbox/work-cbX40-receiver-matrix.md")
work39 = text("stages/stage14/14-Work-caX39/result.md")
main_h = text("stages/stage14/14-4ghH/result.md")
s119 = text("stages/stage14/14-s7-119/result.md")
t155 = text("stages/stage14/14-t155/result.md")
q17 = text("docs/stage14-q17-summary.md")
contract = text("docs/stage14-toolbox/work-toolbox-x-task-contract.md")

# Canonical XQ contract and predecessor boundary.
assert "Stage14-Work-toolbox-XQ" in contract
assert "Q_COMPONENT=NOT_TRIGGERED" in work39
assert "RESTRICTED_MAIN_S_FIXED_E_TWO_SIDED_ADAPTER_PROVED=true" in work39

# Main external gate is complete as an audit but unresolved mathematically.
for needle in [
    "MINIMAL_UNRESOLVED_EXTERNAL_GATE=UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment",
    "MAINLINE_H_COMPLETED=true",
    "MAINLINE_BLOCKED_BY_H=true",
    "DIRECT_TRANSFER_PROVED=false",
    "EXACT_QUADRATIC_DIVISOR_ROOT_NORMAL_FORM_DERIVED=true",
]:
    assert needle in main_h, needle

# s nonaligned reverse kernel is explicit, but support and measure remain distinct.
for needle in [
    "S_SQUARECLASS_REVERSE_WITNESS_SET_DEFINED=true",
    "S_SQUARECLASS_REVERSE_WITNESS_MULTIPLICITY=Bo1",
    "S_SQUARECLASS_REVERSE_EXISTENCE_AUTOMATIC=false",
    "S_SQUARECLASS_OUTER_MEASURE_COMMON=false",
    "S_ROUTE_H_NEEDED=false",
]:
    assert needle in s119, needle

# fixed-U only reuses the native tH31 theorem envelope.
for needle in [
    "ACTUAL_SCALE_KAI_ENVELOPE_DEFINED=true",
    "TH31_RECONSUMED_WITHOUT_RECHARGE=true",
    "ACTUAL_SCALE_KAI_ADMISSIBLE_LONG_FIXED_POWER_DEPLETION_RULED_OUT=true",
    "TH33_NEEDED=false",
]:
    assert needle in t155, needle

# q17 already owns the main reciprocal-support literature target.
for needle in [
    "STAGE14_Q17=COMPLETE_RECIPROCAL_CRT_SUPPORT_LITERATURE_RADAR",
    "RECIPROCAL_CRT_SUPPORT_DIRECT_THEOREM_FOUND=false",
    "Q17_NEXT_SEARCH_TRIGGER=exact_divisor_AP_or_binary_form_encoding_or_new_stable_obstruction_after_4gf",
]:
    assert needle in q17, needle

# X40 required locks.
for needle in [
    "TOOLBOX_COMPONENT_COMPLETE=true",
    "X_COMPONENT_COMPLETE=true",
    "Q_COMPONENT=NOT_TRIGGERED",
    "Q_TRIGGER_STAGE=NONE",
    "EXACT_Q_OBSTRUCTION=NONE",
    "Q_LEDGER_BASELINE=Stage14-q17",
    "Q_RESULT_IMPORTED_BACK_TO_X=not-applicable",
    "LOCALIZED_EXTERNAL_GATE_NONPROPAGATION_LEMMA_PROVED=true",
    "WHOLE_STAGE14_BLOCKED_BY_MAIN_EXTERNAL_GATE=false",
    "S_NONALIGNED_COMMON_SQUARECLASS_REVERSE_WITNESS_KERNEL_PROVED=true",
    "S_NONALIGNED_COMMON_OUTER_MEASURE_PROVED=false",
    "COMMON_ADAPTER_PROVED=false",
    "SAVING_CROSS_PROMOTABLE=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "MAINLINE_H_NEEDED=true",
    "MAINLINE_H_COMPLETED=true",
    "MAINLINE_BLOCKED_BY_H=true",
    "NEW_HEAVY_MAIN_H_NEEDED=false",
    "S_ROUTE_H_NEEDED=false",
    "FIXED_U_H_NEEDED=false",
    "TH33_NEEDED=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]:
    assert needle in result, needle

# Logical sanity: an unresolved predicate on one labelled alternative says nothing
# about a second alternative unless an adapter is supplied.
A = {("aligned", i) for i in range(5)}
B = {("nonaligned", i) for i in range(7)}
family = A | B
assert A.isdisjoint(B)
assert len(family) == len(A) + len(B)
# Mark A as unresolved; B's cardinality and membership are unchanged.
unresolved = set(A)
assert len(B - unresolved) == len(B)

# Bounded witness multiplicity again does not imply existence density.
fibers = [0] * 99 + [1]
assert max(fibers) <= 1
assert sum(bool(x) for x in fibers) == 1

# Matrix mirrors the same boundary.
for needle in [
    "LOCALIZED_EXTERNAL_GATE_NONPROPAGATION_LEMMA_PROVED=true",
    "Q_COMPONENT=NOT_TRIGGERED",
    "MAINLINE_H_TARGET=UniformPrimitiveRectangleNestedKFreeQuadraticDivisorRootFirstMoment",
    "S_NONALIGNED_SUPPORT_ADAPTER_PROVED=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]:
    assert needle in matrix, needle

print("Stage14-Work-cbX40 external-gate isolation audit: PASS")
