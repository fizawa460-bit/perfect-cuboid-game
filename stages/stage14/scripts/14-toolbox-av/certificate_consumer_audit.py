from pathlib import Path

root = Path(__file__).resolve().parents[4]
av = (root / "stages/stage14/14-toolbox-av/result.md").read_text()
matrix = (root / "docs/stage14-toolbox/certificate-consumer-matrix.md").read_text()
cg = (root / "stages/stage14/14-4cg/result.md").read_text()
s21 = (root / "stages/stage14/14-s7-21/result.md").read_text()
t58 = (root / "stages/stage14/14-t58/result.md").read_text()

for token in [
    "STAGE14_TOOLBOX_AV=COMPLETE_CERTIFICATE_CONSUMER_AUDIT_AGAINST_4CG_S7_21_T58",
    "S_4CG_CERTIFICATE_PROMOTION_READY=false",
    "S_S7_21_CERTIFICATE_PROMOTION_READY=false",
    "S_REFINEMENT_SAVINGS_INDEPENDENT=false",
    "FIXED_U_T58_SUPPORT_ENERGY_GATE_CLOSED=true",
    "FIXED_U_CURRENT_RECEIVER=SharedUCanonicalPrimeDeltaToroidalSecondMoment",
    "FIXED_U_SECOND_MOMENT_PROMOTION_READY=false",
    "TH16_NEEDED=true",
    "TOOLBOX_H_CONTINUATION_NEEDED=false",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8",
]:
    assert token in av, token

for token in [
    "PHYSICAL_LIFT_FROM_COMMON_CORE_RESIDUAL_DATA_BO1_PROVED=false",
    "COUPLED_COMMON_CORE_GAUSSIAN_RESIDUAL_INCIDENCE_PROVED=false",
]:
    assert token in cg, token
for token in [
    "BALANCED_DUAL_CRT_SHORT_VECTOR_ENERGY_PROVED=false",
    "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]:
    assert token in s21, token
for token in [
    "FIXED_U_PHYSICAL_SELECTOR_SUPPORT_ENERGY_TRANSFER_PROVED=true",
    "SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false",
    "TH16_NEEDED=true",
]:
    assert token in t58, token

assert "never multiply" in matrix
assert "support-energy transfer is not toroidal correlation" in matrix
print("Stage14-toolbox-av certificate-consumer audit: OK")
