from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]

s150 = (ROOT / "stages/stage14/14-s7-150/result.md").read_text()
s151 = (ROOT / "stages/stage14/14-s7-151/result.md").read_text()
s152 = (ROOT / "stages/stage14/14-s7-152/result.md").read_text()
report = (ROOT / "stages/stage14/14-s-batch/s7-150-152-report.md").read_text()

assert "Q23_W1_WITNESS_DEPENDENCE_SEPARABILITY_TEST=FAIL_WITNESS_DEPENDENCE_ESSENTIAL" in s150
assert "W1(lambda)=4*r_ep*s_ep*epsilon_k*p(lambda)*q(lambda)" in s150
assert "Q23_FIXED_SHIFT_OR_AP_OR_BINARY_FORM_JOINT_NORMAL_FORM_TEST=FAIL_NO_EXACT_STANDARD_REDUCTION" in s151
assert "SUPPORT_ENLARGEMENT_USED=false" in s151
assert "UniformScalarFilteredTau3WitnessCoupledReciprocalFactorPairCRTJointIncidenceFirstMomentLowerBound" in s152
assert "UniformPolynomialOuterPairFilteredTau3WitnessCoupledReciprocalFactorPairCRTJointIncidenceFirstMomentLowerBound" in s152
assert "Q24_NEEDED=false" in s152
assert "BATCH_STOP_REASON=receiver_change" in report
assert "NEXT=Stage14-s7-153" in report

# Tiny logical sanity: a moving p*q cannot be outer-only if two retained witnesses
# on the same outer host carry different reconstructed p*q values.
outer = "z0"
witnesses = [(outer, 2, 3), (outer, 2, 5)]
products = {p*q for _, p, q in witnesses}
assert len(products) == 2

print("STAGE14_S_BATCH_S7_150_152_AUDIT=PASS")
