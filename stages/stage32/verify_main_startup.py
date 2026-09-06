#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V1_POST1648J_TRACE_ORIENTATION_CANDIDATE"
EXPECTED_CANONICAL = "48c1c6cf67a7f96fe691b95d4180a4d72cdf819fd5485dd0178df8fd2c4f9c64"
EXPECTED_ROUTE = "SOURCE_BIND_THE_INNER_CONJUGATING_ELEMENT_FOR_CECOTTI_B7_B8_TO_THE_RETAINED_G12_MARKING_OR_EXPLICITLY_IDENTIFY_B7_WITH_S_AND_B8_WITH_T_INVERSE_ON_THE_MARKED_PPAV"
EXPECTED_WORKING_SET = [
    "stages/stage32/residual-32-01-production/post1648j-cecotti-trace-orientation-correction.json",
    "stages/stage32/residual-32-01-production/verify_stage32_post1648j_cecotti_trace_orientation_correction.py",
    "stages/stage32/residual-32-01-production/post1648b-cecotti-generator-pair-absolute-marking-preflight.json",
    "stages/stage32/residual-32-01-production/post1648-delta0inf-retained-w-absolute-marking-localization.json",
    "stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-principal-rosati-lock.json",
    "stages/stage32/residual-32-01-production/post1505-o210-q602-marked-w-line-gauge-orbit.json",
]


def fail(msg: str) -> None:
    raise SystemExit(msg)


def canonical_sha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_locked_json(lock: dict) -> dict:
    path = ROOT / lock["path"]
    if not path.is_file():
        fail(f"missing locked path: {lock['path']}")
    if git_blob_sha(path) != lock["blob_sha1"]:
        fail(f"blob moved: {lock['path']}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    expected = lock["canonical_sha256"]
    if canonical_sha(obj) != expected or obj.get("canonical_sha256_without_this_field") != expected:
        fail(f"canonical moved: {lock['path']}")
    return obj


def run_marker(path: Path, marker: str) -> None:
    proc = subprocess.run([sys.executable, str(path)], check=True, text=True, capture_output=True)
    if marker not in proc.stdout:
        fail(f"verifier completion marker missing: {marker}")


def main() -> None:
    state = json.loads(STATE.read_text(encoding="utf-8"))
    if state.get("schema") != EXPECTED_SCHEMA:
        fail("MAIN-STATE schema moved")
    if canonical_sha(state) != EXPECTED_CANONICAL or state.get("canonical_sha256_without_this_field") != EXPECTED_CANONICAL:
        fail("MAIN-STATE canonical mismatch")

    authority = state["authority_sync"]
    if authority != {
        "startup_authority": "stages/stage32/MAIN-STATE.json",
        "latest_audited_stage32_leaf": "POST1623_HPERP_V6_HDECK_CHARACTER_PREFLIGHT",
        "latest_audited_stage32_pr": 1643,
        "latest_hostile_audit_review_id": 5123545511,
        "latest_audited_exact_head": "8550ab88e12cbbfd42b2d1e07c8f42be124de1a6",
        "latest_exact_head_ci": {"run_id": 34000915113, "job_id": 101399505061, "result": "SUCCESS"},
        "latest_stage32_merge_commit": "dc244645097809948f118d915534a92e56ab60ec",
        "legacy_detailed_files_are_not_ordinary_startup_authority": True,
    }:
        fail("audited authority synchronization moved")

    if state["fixed_target"] != {
        "row_id": "g1-d186", "degree": 186, "e": 266, "genus": 1,
        "O": 210, "qprime": 4, "Q": 602,
        "surviving_residues_decimal": [73, 97, 235],
    }:
        fail("fixed target moved")

    frontier = state["current_exact_frontier"]
    required = {
        "nonexceptional_mod2_witness_source_bound": True,
        "source_bound_nonexceptional_H_character_probe_obtained": True,
        "source_bound_H_character_probe_normal_curve_label_1based": 9,
        "source_bound_H_character_probe_character": "chi_u",
        "source_bound_H_character_probe_profile_id_u_v_uv": [0, 1, 0, 1],
        "abstract_delta_0inf_direction_recovered": True,
        "delta0inf_source_bound_to_Z3_b3_retained_boundary_block": True,
        "delta0inf_retained_boundary_labels_1based": [41, 42, 43, 44],
        "principal_b3_stoll_candidates_after_boundary_weierstrass_filter": 32,
        "unmarked_full_J2_group_matching_closed_nonpruning": True,
        "deraux_affine_sixpoint_matching_closed_nonpruning": True,
        "central_r_operator_matching_closed_nonpruning": True,
        "full_G_deck_as_nontrivial_Stoll_B_route_closed_type_mismatch": True,
        "cecotti_B7_B8_trace_orientation_exact": True,
        "cecotti_B7_B8_trace_phi2_phi6": "+r",
        "cecotti_named_S_T_trace": "-r",
        "cecotti_named_S_T_orientation_ruled_out_for_specific_B7_B8": True,
        "cecotti_compatible_ordered_pair_orbit": "INNER_CONJUGATES_OF_S_T_INVERSE",
        "literal_S_T_inverse_representative_conditional_residue_decimal": 97,
        "literal_S_T_inverse_representative_promoted": False,
        "plus_r_inner_conjugates_W_line_bijections": 6,
        "absolute_delta0inf_retained_W_line_identified": False,
        "q602_residue_specific_commutator_obtained": False,
    }
    for key, value in required.items():
        if frontier.get(key) != value:
            fail(f"frontier moved: {key}")

    current = state["current"]
    if current["active_missing_interface"] != "DISTINGUISHED_INNER_CONJUGATING_ELEMENT_FOR_CECOTTI_B7_B8_TO_RETAINED_G12_MARKING":
        fail("active missing interface moved")
    if current["next_exact_route"] != EXPECTED_ROUTE:
        fail("next exact route moved")
    if current["stop_semantics"] != "LEAF_GATE_ONLY_NOT_STAGE_EXHAUSTION":
        fail("stop semantics moved")
    if current["stacked_candidate_audit_status"] != "PENDING_BATCH_HOSTILE_AUDIT":
        fail("batch audit status moved")

    if state["current_leaf_working_set"] != EXPECTED_WORKING_SET:
        fail("current leaf working set moved")
    for rel in EXPECTED_WORKING_SET:
        if not (ROOT / rel).is_file():
            fail(f"working-set path missing: {rel}")

    startup = START.read_text(encoding="utf-8")
    for fragment in [
        "Ordinary `Stage32-main-batch` reads, in this order:",
        "only the paths listed in `MAIN-STATE.json.current_leaf_working_set`",
        "Do not merge without explicit user authorization.",
    ]:
        if fragment not in startup:
            fail(f"startup contract fragment missing: {fragment}")

    locks = state["source_locks"]
    j = load_locked_json(locks["post1648j_trace_orientation"])
    j_verifier = ROOT / locks["post1648j_trace_orientation_verifier"]["path"]
    if git_blob_sha(j_verifier) != locks["post1648j_trace_orientation_verifier"]["blob_sha1"]:
        fail("post1648J verifier blob moved")
    run_marker(j_verifier, "POST1648J_CECOTTI_TRACE_ORIENTATION_CORRECTION_COMPLETE")

    char = load_locked_json(locks["post1643_hdeck_character_preflight"])
    char_verifier = ROOT / locks["post1643_hdeck_character_verifier"]["path"]
    if git_blob_sha(char_verifier) != locks["post1643_hdeck_character_verifier"]["blob_sha1"]:
        fail("post1643 verifier blob moved")
    run_marker(char_verifier, "POST1623_HPERP_V6_HDECK_CHARACTER_PREFLIGHT_COMPLETE")

    load_locked_json(locks["post1621_hperp_witness"])
    load_locked_json(locks["post1588_direct_mod2"])
    load_locked_json(locks["post1577_terminal_negative"])

    if j["decision"]["survivors_current_credit"] != [73, 97, 235]:
        fail("post1648J survivor set moved")
    if j["decision"]["absolute_delta0inf_retained_W_line_identified"]:
        fail("post1648J absolute line firewall moved")
    if j["correction_to_post1648b"]["new_exact_status"] != "RULED_OUT_FOR_THE_SPECIFIC_CECOTTI_B7_B8_PAIR_BY_HOLOMORPHIC_DIFFERENTIAL_TRACE":
        fail("post1648J correction moved")
    if j["W_line_consequence"]["literal_plus_r_conditional_delta0inf_residue_decimal"] != 97:
        fail("post1648J literal plus-r diagnostic moved")
    if j["W_line_consequence"]["all_plus_r_inner_conjugates"]["distinct_W_line_bijections"] != 6:
        fail("post1648J inner-conjugacy ambiguity moved")

    if char["fixed_target"]["surviving_residues_decimal"] != [73, 97, 235]:
        fail("audited post1643 survivor set moved")

    fw = state["firewalls"]
    for key in [
        "Q602_excluded", "O210_excluded", "O212_plus_advance_allowed",
        "controller_promotion_granted", "heavy_compute_authorized_by_startup_state",
        "receiver_credit", "route_credit", "theorem_credit", "endpoint_credit",
        "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
    ]:
        if fw[key]:
            fail(f"startup firewall moved: {key}")

    print("PASS Stage32 MAIN startup authority")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("latest_audited_stage32_pr=1643 hostile_review=5123545511")
    print("stacked_candidate=post1648J pending_batch_hostile_audit")
    print("cecotti_B7_B8_trace=+r named_ST_trace=-r compatible_orbit=conjugates_of_S_Tinv")
    print("literal_plus_r_conditional_residue=97 not_promoted=true")
    print("inner_conjugates_W_line_bijections=6 absolute_delta0inf_retained_W_line_identified=false")
    print("audited_survivors=73,97,235")
    print("Q602_excluded=false O210_excluded=false O212_plus_advance_allowed=false")


if __name__ == "__main__":
    main()
