#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGES = HERE.parent
ART = HERE / "ex1-05g-h4-common-cover-correspondence-coupling.json"
UP05F = HERE / "ex1-05f-h4-local-cusp-projection-ramification-adapter.json"
V4_NOTE = STAGES / "stage32/residual-32-01-production/post1503-o210-q4-relative-v4-torsor-mod2-coupling-source-note.md"
V4_ART = STAGES / "stage32/residual-32-01-production/post1503-o210-q4-relative-v4-torsor-mod2-coupling.json"
ROS_NOTE = STAGES / "stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair-source-note.md"
ROS_ART = STAGES / "stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair.json"


def git_blob_sha1(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def load_canonical(path: Path):
    d = json.loads(path.read_text(encoding="utf-8"))
    claimed = d.pop("canonical_sha256_without_this_field")
    canon = json.dumps(d, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    actual = hashlib.sha256(canon.encode()).hexdigest()
    assert actual == claimed, (path, actual, claimed)
    return d, claimed


d, claimed = load_canonical(ART)
up05f = json.loads(UP05F.read_text(encoding="utf-8"))
v4, v4canon = load_canonical(V4_ART)
ros, roscanon = load_canonical(ROS_ART)

assert d["audited_predecessor"] == {
    "pr": 1688,
    "review_id": 5135375926,
    "exact_head": "93c455e1e69ed65fbfb553462fdcfbc8e2becbae",
    "result": "PASS",
    "merge_commit": "6431ec2a90ed9260d4362d7146a9788cbc21c8d1",
    "credit_ceiling": "INTERMEDIATE_BRANCH_EXCLUSION_AND_EXACT_BLOCKER_ONLY",
}

locks = d["source_locks"]
assert up05f["canonical_sha256_without_this_field"] == locks["ex1_05f"]["canonical_sha256"]
assert git_blob_sha1(V4_NOTE) == locks["stage32_relative_v4_source_note"]["blob_sha1"]
assert git_blob_sha1(V4_ART) == locks["stage32_relative_v4_artifact"]["blob_sha1"]
assert v4canon == locks["stage32_relative_v4_artifact"]["canonical_sha256"]
assert git_blob_sha1(ROS_NOTE) == locks["stage32_rosati_repair_source_note"]["blob_sha1"]
assert git_blob_sha1(ROS_ART) == locks["stage32_rosati_repair_artifact"]["blob_sha1"]
assert roscanon == locks["stage32_rosati_repair_artifact"]["canonical_sha256"]

v4txt = V4_NOTE.read_text(encoding="utf-8")
for anchor in [
    "`f1^* Z ~= f2^* Z`",
    "81 alpha = alpha  (mod 2)",
    "105 alpha = alpha (mod 2)",
    "leaves exactly `28` residue classes",
]:
    assert anchor in v4txt, anchor

rostxt = ROS_NOTE.read_text(encoding="utf-8")
for anchor in [
    "## Retained exact class/deck arithmetic",
    "`Gamma^2 = D^2 + D.uD + D.vD + D.uvD`",
    "`Gamma^2 = 3874+11932 = 15806`",
    "`sigma(Gamma)=2*105*81-15806=1204`",
    "`Q(T)=602`",
    "## O=210 normalization arithmetic",
]:
    assert anchor in rostxt, anchor

A = d["notation_adapter"]
assert A["C0_equals_EX1_C2"] is True
assert A["projection_degrees"] == [105, 81]
assert A["EX1_Q"].startswith("deg Ram(D->N)")

C = d["common_cover_consequence"]
assert C["D_maps_to_relative_H_isomorphism_torsor"] is True
assert C["W_dimension"] == 2
assert C["odd_projection_degrees"] == [105, 81]
assert C["push_pull_consequence"] == ["T_12|W=id mod 2", "T_21|W=id mod 2"]

F = d["fixed_correspondence_arithmetic"]
assert F["pair_map_birational"] is True
assert F["Gamma_bidegree"] == [105, 81]
assert F["Gamma_square"] == ros["corrected_rosati_arithmetic"]["Gamma_square"] == 15806
assert F["sigma"] == ros["corrected_rosati_arithmetic"]["sigma"] == 1204
assert F["Q_Rosati"] == ros["corrected_rosati_arithmetic"]["Q"] == 602

d1, d2 = 105, 81
sigma = 1204
pa = (2*d1*d2 + 2*(d1+d2) + 2 - sigma) // 2
assert pa == F["Gamma_arithmetic_genus"] == 8090

L = d["Q_defect_ladder"]
Qvals = list(range(210, 267, 2))
assert L["EX1_Q_values"] == Qvals
assert L["r_values"] == list(range(29))
for r, Q in enumerate(Qvals):
    gD = 1 + Q//2
    delta = pa - gD
    R105 = Q - 210
    R81 = Q - 162
    assert gD == 106 + r == L["genus_D_values"][r]
    assert delta == 7984 - r == L["delta_Gamma_values"][r]
    assert R105 == 2*r == L["R105_values"][r]
    assert R81 == 48 + 2*r == L["R81_values"][r]
    assert 2*delta + R105 == 15968
    assert 2*delta + R81 == 16016
    assert delta >= 0

M = d["mod2_shell_replay_adapter"]
source_preflight = v4["q602_mod2_preflight"]
assert M["Q_Rosati"] == source_preflight["Q"] == 602
assert M["realized_residue_class_count"] == source_preflight["realized_residue_class_count"] == 96
assert M["fixed_plane_survivor_count"] == source_preflight["surviving_residue_class_count"] == 28
assert M["fixed_plane_survivors_decimal"] == source_preflight["surviving_residue_classes_decimal"]
assert M["fixed_plane_survivors_hex"] == source_preflight["surviving_residue_classes_hex"]

J = d["coarse_joint_compatibility"]
assert J["EX1_Q_state_count"] == 29
assert J["mod2_residue_state_count"] == 28
assert J["cartesian_cell_count"] == 29 * 28 == 812
assert J["states_excluded_by_05G"] == 0

D = d["decision"]
assert D["Q_states_entering_05G"] == 29
assert D["Q_states_excluded_by_common_cover_correspondence_coupling"] == 0
assert D["Q_states_leaving_05G"] == 29
assert D["next_route"] == "EX1-05H_CORRESPONDENCE_DEFECT_TO_OFF_CUSP_RAMIFICATION_COUPLING"

E = d["exit"]
assert E["finite_Q_slack_ledger_complete"] is True
assert E["finite_joint_product_compatibility_ledger_complete"] is True
assert E["finite_residual_configuration_ledger_complete"] is False
assert E["all_residual_configurations_disposed"] is False
assert E["positive_witness_established"] is False
assert E["full_target_closure"] is False

FW = d["firewalls"]
for key in [
    "stage32_O210_specific_transvection_16_to_3_imported_without_adapter",
    "Q602_residue_survival_promoted_to_geometric_correspondence",
    "cartesian_812_cells_promoted_to_geometric_realizability",
    "Gamma_defect_identified_with_original_curve_delta_472",
    "projection_ramification_identified_with_intrinsic_delta",
    "off_cusp_ramification_numerical_assignment_promoted_to_map_existence",
    "full_v6_exclusion_claimed",
    "stage32_main_credit",
    "Q602_excluded",
    "O210_excluded",
    "receiver_credit",
    "theorem_credit",
    "endpoint_credit",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
]:
    assert FW[key] is False, key

print("EX1-05G replay PASS: common-cover/Rosati coupling gives Q_Rosati=602 and delta_Gamma=7984-r for all 29 states; 0/29 Q states excluded")
print("canonical_sha256", claimed)
print("coarse_joint_cells", 812)
