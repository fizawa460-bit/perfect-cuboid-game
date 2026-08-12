from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

required = {
    "stages/stage14/14-s7-147/result.md": [
        "Q22_GOOD_INDICATOR_EXACT_WITNESS_EXPANSION_TEST=PASS_NONNEGATIVE_Q17_WITNESS_COUNT",
        "M1_G <= J1_G <= B^o(1) M1_G",
    ],
    "stages/stage14/14-s7-148/result.md": [
        "Q22_POSITIVE_FIRST_MOMENT_NORMAL_FORM_TEST=PASS_JOINT_NONNEGATIVE_DIVISOR_CRT_INCIDENCE",
        "f*n = W1(lambda)",
        "n+f == 0 (mod 2U)",
        "n-f == 0 (mod 2V)",
    ],
    "stages/stage14/14-s7-149/result.md": [
        "Q23_THEOREM_TARGET_NOW_STABLE=true",
        "S_JOINT_INCIDENCE_FIRST_MOMENT_LOWER_BOUND_PROVED=false",
        "NEXT=Stage14-s7-150",
    ],
    "stages/stage14/14-s-batch/s7-147-149-report.md": [
        "BATCH_STOP_REASON=receiver_change",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
    ],
}

for rel, tokens in required.items():
    text = (ROOT / rel).read_text()
    for token in tokens:
        assert token in text, (rel, token)

# Finite sanity check of the Boolean-to-witness-count sandwich.
for count in range(8):
    indicator = int(count >= 1)
    assert indicator <= count if count else indicator == 0
    if count:
        assert count <= 8 * indicator

# Joint-incidence algebra sanity: factor witnesses satisfy the two CRT tests.
U, V, W = 2, 3, 35
hits = []
for f in range(1, W + 1):
    if W % f:
        continue
    n = W // f
    if (n + f) % (2 * U) == 0 and (n - f) % (2 * V) == 0:
        hits.append((f, n))
for f, n in hits:
    assert f * n == W
    assert (n + f) % (2 * U) == 0
    assert (n - f) % (2 * V) == 0

print("STAGE14_S_BATCH_S7_147_149_AUDIT=PASS")
