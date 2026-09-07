#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGES = HERE.parent
ART = HERE / "ex1-05h-upstairs-conductor-discriminant-off-cusp-coupling.json"
NOTE = HERE / "ex1-05h-upstairs-conductor-discriminant-source-note.md"
UP05G = HERE / "ex1-05g-h4-common-cover-correspondence-coupling.json"
ROS_ART = STAGES / "stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair.json"
ROS_NOTE = STAGES / "stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair-source-note.md"


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
up05g, up05g_canon = load_canonical(UP05G)
ros, ros_canon = load_canonical(ROS_ART)

assert d["schema"] == "STAGE32EX1_EX1_05H_UPSTAIRS_CONDUCTOR_DISCRIMINANT_OFF_CUSP_COUPLING_V1"
assert d["status"] == "PASS_EXACT_UPSTAIRS_DEFECT_AND_DISCRIMINANT_DIVISOR_COUPLING_NONPRUNING_CANDIDATE"

locks = d["source_locks"]
assert up05g_canon == locks["ex1_05g"]["canonical_sha256"] == "5a1c30a64857b900f7523153f326c0742ad5cb4ef88e77b0748dd6c4e532be08"
assert git_blob_sha1(NOTE) == locks["ex1_05h_source_note"]["blob_sha1"] == "47837ed1bc55c120883039c32a1a0b25f26e7aa3"
assert ros_canon == locks["stage32_rosati_repair"]["artifact_canonical_sha256"] == "e28c7539e05b9c4836b9bc51c8f69316723eb8c368700a26706627045525fe07"
assert git_blob_sha1(ROS_NOTE) == locks["stage32_rosati_repair"]["source_note_blob_sha1"] == "b0ea281eae453929c292059a919bc1f68b3080b3"

note = NOTE.read_text(encoding="utf-8")
for anchor in [
    "`D0^2 = 3874`",
    "`delta_D0 = p_a(D0)-g(D) = 2018-r`",
    "`C_nu + R105 ~ nu0^*D0 + f2^*K_C2`",
    "`C_nu + R81  ~ nu0^*D0 + f1^*K_C2`",
    "`Disc(pi_i) = Br_i + 2*A_i`",
    "`mult_y Disc(pi_i) = mult_y Br_i + 2*mult_y A_i`",
    "Tag `0C1B`",
    "Tag `0C17`",
    "Tag `0BWA`",
    "Tag `0C1R`",
    "Tag `0AA4`",
]:
    assert anchor in note, anchor

# Re-establish the retained upstairs fixed arithmetic from the audited Rosati repair.
ret = ros["retained_exact_inputs"]
F = d["upstairs_fixed_arithmetic"]
assert F["D0_square"] == ret["D_square"] == 3874
source_cross = ret["deck_cross"]
assert F["deck_intersections"] == {k: source_cross[k] for k in ["u", "v", "uv"]} == {"u": 3892, "v": 4020, "uv": 4020}
assert source_cross["sum"] == F["deck_cross_sum"] == sum(F["deck_intersections"].values()) == 11932
assert F["deck_half_cross_sum"] * 2 == F["deck_cross_sum"]
assert F["deck_half_cross_sum"] == 5966

# q is etale over C2 x C2 and the two degrees are 105,81; deg K_C2 = 2.
degrees = d["notation_adapter"]["projection_degrees"]
assert degrees == [105, 81]
Kdot = 2 * sum(degrees)
assert Kdot == F["K_S0_dot_D0"] == 372
pa_D0 = (F["D0_square"] + Kdot) // 2 + 1
assert pa_D0 == F["D0_arithmetic_genus"] == 2124

# Replay the full 29-state upstairs defect ladder.
L = d["upstairs_defect_ladder"]
Qvals = list(range(210, 267, 2))
rvals = list(range(29))
assert L["EX1_Q_values"] == Qvals
assert L["r_values"] == rvals
assert L["delta_D0_range"] == [1990, 2018]
for r, Q in zip(rvals, Qvals):
    gD = 1 + Q // 2
    delta_D0 = pa_D0 - gD
    delta_Gamma = delta_D0 + F["deck_half_cross_sum"]
    R105 = Q - 210
    R81 = Q - 162

    assert gD == L["normalization_genus_values"][r] == 106 + r
    assert delta_D0 == L["delta_D0_values"][r] == 2018 - r
    assert delta_Gamma == L["delta_Gamma_values"][r] == 7984 - r
    assert R105 == L["R105_values"][r] == 2 * r
    assert R81 == L["R81_values"][r] == 48 + 2 * r
    assert delta_Gamma == up05g["Q_defect_ladder"]["delta_Gamma_values"][r]
    assert 2 * delta_D0 + R105 == 4036
    assert 2 * delta_D0 + R81 == 4084

C = d["conductor_adjunction_coupling"]
assert C["D0_cartier_gorenstein"] is True
assert C["conductor_degree_formula"] == "deg(C_nu)=2*delta_D0"
assert C["projection_105_degree_identity"] == "2*delta_D0+R105=4036"
assert C["projection_81_degree_identity"] == "2*delta_D0+R81=4084"
assert C["ramification_difference_class"] == "R81-R105 ~ f1^*K_C2-f2^*K_C2"
assert C["ramification_difference_line_bundle_2_divisible"] is True

P = d["projection_discriminant_coupling"]
assert P["index_divisor_degree"] == "deg A_i=delta_D0"
assert P["local_trace_lattice_formula"] == "disc(B)=det(M)^2*disc(B')"
assert P["global_divisor_formula"] == "Disc(pi_i)=Br(f_i)+2*A_i"
assert P["disc_105_degree"] == 4036
assert P["disc_81_degree"] == 4084
assert P["same_base_point_even_tradeoff"] is True

assert up05g["Q_defect_ladder"]["conservation_1"] == "2*delta_Gamma+R105=15968"
assert up05g["Q_defect_ladder"]["conservation_2"] == "2*delta_Gamma+R81=16016"
assert 4036 + 2 * F["deck_half_cross_sum"] == 15968
assert 4084 + 2 * F["deck_half_cross_sum"] == 16016

pr = d["pruning_result"]
assert pr["Q_states_entering"] == 29
assert pr["Q_states_excluded_by_05H"] == 0
assert pr["Q_states_leaving"] == 29

D = d["decision"]
assert D["member_level_coupling_obtained"] is True
assert D["projection_discriminant_support_extracted"] is False
assert D["actual_D0_singularity_cycle_extracted"] is False
assert D["next_route"] == "EX1-05I_UPSTAIRS_SINGULARITY_CYCLE_OR_PROJECTION_DISCRIMINANT_SUPPORT_EXTRACTION"

E = d["exit"]
assert E["finite_Q_slack_ledger_complete"] is True
assert E["finite_residual_configuration_ledger_complete"] is False
assert E["all_residual_configurations_disposed"] is False
assert E["positive_witness_established"] is False
assert E["full_target_closure"] is False

FW = d["firewalls"]
for key in [
    "D0_identified_with_smooth_EX1_D",
    "delta_D0_identified_with_original_V6_delta_472",
    "delta_Gamma_identified_with_original_V6_delta_472",
    "deck_half_cross_5966_localized_to_D0_singularities_without_proof",
    "discriminant_degree_promoted_to_discriminant_support",
    "two_divisibility_promoted_to_existence_or_exclusion",
    "superseded_zero_rosati_O210_exclusion_reused",
    "historical_O210_16_to_3_imported_without_adapter",
    "Q_states_pruned_by_05H",
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

print("EX1-05H replay PASS: upstairs defect delta_D0=2018-r and divisor-level Disc=Br+2*Index coupling; 0/29 Q states excluded")
print("canonical_sha256", claimed)
print("disc_degrees", 4036, 4084)
