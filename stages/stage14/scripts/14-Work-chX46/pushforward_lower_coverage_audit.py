from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def text(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


result = text("stages/stage14/14-Work-chX46/result.md")
matrix = text("docs/stage14-toolbox/work-chX46-receiver-matrix.md")
s140 = text("stages/stage14/14-s7-140/result.md")
cgx45 = text("stages/stage14/14-Work-cgX45/result.md")
q17 = text("docs/stage14-q17-summary.md")
q20 = text("docs/stage14-q20-summary.md")

required_result = [
    "TOOLBOX_COMPONENT_COMPLETE=true",
    "X_COMPONENT_COMPLETE=true",
    "Q_COMPONENT=NOT_TRIGGERED",
    "PUSHFORWARD_UPPER_ENVELOPE_DOES_NOT_IMPLY_LOWER_COVERAGE=true",
    "PUSHFORWARD_LOWER_COVERAGE_IS_INDEPENDENT_DIRECTION=true",
    "S_Q17_GOOD_PACKET_COVERAGE_PROVED=false",
    "S_PUSHFORWARD_LOWER_COVERAGE_THEOREM_SPECIES_COUNT=2",
    "Q17_INNER_KERNEL_DEFICIT_RECHARGED=false",
    "POST_MASK_REMAINS_SEPARATELY_CHARGED=true",
    "Q21_NEEDED=false",
    "TH34_NEEDED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    "COMMON_ADAPTER_PROVED=false",
    "NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]
for token in required_result:
    assert token in result, token

for token in [
    "S_PUSHFORWARD_POINTWISE_UPPER_ENVELOPE=Bo1",
    "S_Q17_GOOD_PACKET_COVERAGE_PROVED=false",
    "Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false",
    "Q21_NEEDED=false",
]:
    assert token in s140, token

for token in [
    "CONDITIONED_KERNEL_MEASURE_FIREWALL_LEMMA_PROVED=true",
    "Q17_TO_S_CONDITIONED_MEASURE_ADAPTER_PROVED=false",
    "Q21_NEEDED=false",
]:
    assert token in cgx45, token

assert "STAGE14_Q17=COMPLETE_RECIPROCAL_CRT_SUPPORT_LITERATURE_RADAR" in q17
assert "STAGE14_Q20=COMPLETE_CONDITIONED_DIVISOR_CORRELATION_LITERATURE_RADAR" in q20

for token in [
    "PUSHFORWARD_POINTWISE_UPPER_ENVELOPE_DOES_NOT_PROVE_GOOD_PACKET_COVERAGE=true",
    "PAIR_TO_SCALAR_HOST_ADAPTER_PROVED=false",
    "Q21_NEEDED=false",
    "TH34_NEEDED=false",
]:
    assert token in matrix, token

# Deterministic finite-set witness: an upper fiber bound does not imply coverage.
theta = tuple(range(8))
good = {0, 1, 2, 3}
pushforward_mult = {4: 1, 5: 1}
assert max(pushforward_mult.values()) <= 1
assert sum(pushforward_mult.get(t, 0) for t in good) == 0
assert len(good) == 4

print("Stage14-Work-chX46 audit: PASS")
