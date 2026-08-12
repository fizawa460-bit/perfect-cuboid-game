from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

s120 = read("stages/stage14/14-s7-120/result.md")
s121 = read("stages/stage14/14-s7-121/result.md")
s122 = read("stages/stage14/14-s7-122/result.md")
report = read("stages/stage14/14-s-batch/s7-120-122-report.md")
prev = read("stages/stage14/14-s7-119/result.md")
work = read("stages/stage14/14-Work-cbX40/result.md")

for token in [
    "S_SQUARECLASS_REVERSE_WITNESS_SET_DEFINED=true",
    "S_SQUARECLASS_OUTER_MEASURE_COMMON=false",
    "NEXT=Stage14-s7-120",
]:
    assert token in prev

for token in [
    "Q18_PREMATURE_PENDING_S7_120_THEOREM_CONTRACT=true",
    "S_NONALIGNED_COMMON_SQUARECLASS_REVERSE_WITNESS_KERNEL_PROVED=true",
]:
    assert token in work

for token in [
    "S_SQUARECLASS_BARE_SUPPORT_DEFINED=true",
    "S_SQUARECLASS_POSTMASK_SUPPORT_DEFINED=true",
    "S_SQUARECLASS_DEFICIT_LEDGER_EXACT=true",
]:
    assert token in s120

for token in [
    "S_ONE_DIMENSIONAL_BRANCHES_COMMON_THEOREM_SPECIES=true",
    "UniformOneDimensionalFixedSquareClassTwoLevelReverseReciprocalFactorPairSupport",
    "S_ONE_DIMENSIONAL_BARE_FULL_EXPONENT_PROVED=false",
]:
    assert token in s121

for token in [
    "UniformPolynomialOuterPairFiberedFixedSquareClassTwoLevelReverseReciprocalFactorPairSupport",
    "S_POLYNOMIAL_PAIR_TO_SCALAR_N_SUPPORT_ADAPTER_PROVED=false",
    "S_THEOREM_CONTRACT_SEPARATION_COMPLETE=true",
    "Q18_THEOREM_TARGETS_NOW_STABLE=true",
]:
    assert token in s122

# Fixed n has divisor-many ordered positive factorizations n=E*m.
def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]
for n in range(1, 200):
    pairs = [(d, n // d) for d in divisors(n)]
    assert len(pairs) == len(divisors(n))
    assert all(e * m == n for e, m in pairs)

for token in [
    "BATCH_FIRST_STAGE=Stage14-s7-120",
    "BATCH_LAST_STAGE=Stage14-s7-122",
    "BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3",
    "BATCH_STOP_REASON=receiver_change",
    "S_ROUTE_H_NEEDED=false",
    "NEXT=Stage14-s7-123",
    "STAGE14_AUTOMATION_SAFE=true",
    "STAGE14_ROUTE=s",
]:
    assert token in report

print("STAGE14_S_BATCH_S7_120_122_AUDIT=PASS")
