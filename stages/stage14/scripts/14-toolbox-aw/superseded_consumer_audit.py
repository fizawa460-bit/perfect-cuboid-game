from pathlib import Path

root = Path(__file__).resolve().parents[4]
aw = (root / "stages/stage14/14-toolbox-aw/result.md").read_text()
matrix = (root / "docs/stage14-toolbox/superseded-consumer-current-receiver-matrix.md").read_text()

sources = {
    "4ch": (root / "stages/stage14/14-4ch/result.md").read_text(),
    "s22": (root / "stages/stage14/14-s7-22/result.md").read_text(),
    "t59": (root / "stages/stage14/14-t59/result.md").read_text(),
    "x1": (root / "stages/stage14/14-X1/result.md").read_text(),
    "s23": (root / "stages/stage14/14-s7-23/result.md").read_text(),
    "s29": (root / "stages/stage14/14-s7-29/result.md").read_text(),
    "4cp": (root / "stages/stage14/14-4cp/result.md").read_text(),
    "th18": (root / "stages/stage14/14-tH18/result.md").read_text(),
    "t68": (root / "stages/stage14/14-t68/result.md").read_text(),
}

required_aw = [
    "STAGE14_TOOLBOX_AW=COMPLETE_SUPERSEDED_CONSUMER_AUDIT_AND_THREE_QUARTER_RECEIVER_REFRESH",
    "CURRENT_MAIN_S_RECEIVER=QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy",
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=3/4",
    "IMPROVEMENT_OVER_7_8=1/8",
    "TH16_REQUEST_CURRENT=false",
    "TH18_PREVIOUS_REQUEST_SUPERSEDED=true",
    "TH18_NEEDED=false",
    "CURRENT_FIXED_U_RECEIVER=SharedUMutuallyCayleyPrivateSquareScaleEnergy",
    "MAIN_S_AND_FIXED_U_RECEIVERS_EQUIVALENT=false",
    "NEW_AW_WHOLE_FAMILY_POWER_SAVING_PROVED=false",
]
for token in required_aw:
    assert token in aw, token

checks = {
    "4ch": ["FIXED_EIGHT_CELLS_COMMON_CORE_RESIDUAL_PHYSICAL_LIFT_BO1=true"],
    "s22": ["PACKET_TO_DUAL_NORMAL_AVERAGE_FIBER_PROVED=false"],
    "t59": ["SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED=false"],
    "x1": ["JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA_PROVED=true"],
    "s23": ["STAGE14_S7_23=COMPLETE_CELLWISE_DUAL_SUPPORT_AND_RANK_THREE_ENDPOINT_ELIMINATION"],
    "s29": ["STAGE14_S7_29=COMPLETE_COMMON_CORE_GAUSSIAN_ROOT_LINE_PRIMITIVE_LATTICE_COUNT_AND_3_4_BOUND"],
    "4cp": ["REMAINING_RECEIVER=QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy"],
    "th18": ["FOUVRY_IWANIEC_DIRECT_IMPORT_VALID=false"],
    "t68": ["SHARED_U_MUTUALLY_CAYLEY_PRIVATE_SQUARE_SCALE_ENERGY_PROVED=false", "TH18_NEEDED=false"],
}
for name, tokens in checks.items():
    for token in tokens:
        assert token in sources[name], (name, token)

for phrase in [
    "Do not report `7/8` as the current global exponent",
    "Do not multiply common-core and dual-CRT savings",
    "Do not keep tH16 or the old tH18 request active",
]:
    assert phrase in matrix, phrase

print("Stage14-toolbox-aw superseded-consumer audit: OK")
