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

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V1_POST1643_HPERP_V6_HDECK_CHARACTER_PREFLIGHT"
EXPECTED_CANONICAL = "e44eed469d36f8d98151372a36da99ca65e0918a127606d25721a03612b71ca3"
EXPECTED_ROUTE = "SOURCE_BIND_DELTA_0INF_TO_ONE_RETAINED_W_LINE_BY_EQUIVARIANT_PRINCIPAL_BOLZA_ACTION_OR_AN_EQUIVALENT_ABSOLUTE_TORSOR_TO_J2_ADAPTER"
EXPECTED_WORKING_SET = [
    "stages/stage32/residual-32-01-production/post1623-hperp-v6-hdeck-character-preflight.json",
    "stages/stage32/residual-32-01-production/verify_stage32_post1623_hperp_v6_hdeck_character_preflight.py",
    "stages/stage32/residual-32-01-production/post1505-o210-q602-marked-w-line-gauge-orbit.json",
    "stages/stage32/residual-32-01-production/post1505-o210-q4-x8-v4-torsor-plane-weierstrass-lock.json",
    "stages/stage32/residual-32-01-production/post1588-hperp-nonexceptional-mod2-witness.json",
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
        "nonexceptional_mod2_witness_normal_curve_label_1based": 1,
        "source_bound_nonexceptional_H_character_probe_obtained": True,
        "source_bound_H_character_probe_normal_curve_label_1based": 9,
        "source_bound_H_character_probe_character": "chi_u",
        "source_bound_H_character_probe_profile_id_u_v_uv": [0, 1, 0, 1],
        "abstract_delta_0inf_direction_recovered": True,
        "absolute_delta0inf_retained_W_line_identified": False,
        "q602_residue_specific_commutator_obtained": False,
    }
    for key, value in required.items():
        if frontier.get(key) != value:
            fail(f"frontier moved: {key}")

    current = state["current"]
    if current["active_missing_interface"] != "ABSOLUTE_ADAPTER_DELTA_0INF_TO_ONE_RETAINED_W_LINE":
        fail("active missing interface moved")
    if current["next_exact_route"] != EXPECTED_ROUTE:
        fail("next exact route moved")
    if current["stop_semantics"] != "LEAF_GATE_ONLY_NOT_STAGE_EXHAUSTION":
        fail("stop semantics moved")

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
    char = load_locked_json(locks["post1643_hdeck_character_preflight"])
    leaf_verifier_path = ROOT / locks["post1643_hdeck_character_verifier"]["path"]
    if git_blob_sha(leaf_verifier_path) != locks["post1643_hdeck_character_verifier"]["blob_sha1"]:
        fail("post1643 verifier blob moved")
    load_locked_json(locks["post1621_hperp_witness"])
    load_locked_json(locks["post1588_direct_mod2"])
    load_locked_json(locks["post1577_terminal_negative"])

    proc = subprocess.run([sys.executable, str(leaf_verifier_path)], check=True, text=True, capture_output=True)
    if "POST1623_HPERP_V6_HDECK_CHARACTER_PREFLIGHT_COMPLETE" not in proc.stdout:
        fail("post1643 leaf verifier completion marker missing")

    if char["fixed_target"]["surviving_residues_decimal"] != [73, 97, 235]:
        fail("post1643 survivor set moved")
    probe = char["exact_hdeck_probe"]["source_bound_nontrivial_character"]
    if probe != {
        "character_name": "chi_u",
        "chi_u_labels_1based": [9, 14, 85, 88, 89, 92],
        "chi_uv_single_normal_labels_1based": [],
        "chi_v_single_normal_labels_1based": [],
        "normal_curve_label_1based": 9,
        "one_plus_chi_u_labels_1based": [12, 15, 86, 87, 90, 91],
        "profile": [0, 1, 0, 1],
    }:
        fail("post1643 chi_u probe moved")
    bounded = char["bounded_conclusion"]
    if bounded["next_exact_route"] != EXPECTED_ROUTE:
        fail("post1643 route moved")
    if not bounded["abstract_delta_0inf_direction_recovered"]:
        fail("abstract delta_0inf credit missing")
    if not bounded["absolute_delta0inf_retained_W_line_still_unidentified"]:
        fail("absolute W-line gap moved")
    if not bounded["audited_three_residues_still_not_arithmetically_contracted"]:
        fail("survivor firewall moved")
    if bounded["q602_residue_specific_commutator_obtained"]:
        fail("commutator firewall moved")

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
    print("audited_survivors=73,97,235")
    print("source_bound_H_character_probe=normal_label_9 profile_0101=chi_u")
    print("abstract_delta_0inf_direction_recovered=true")
    print("absolute_delta0inf_retained_W_line_identified=false")
    print("Q602_excluded=false O210_excluded=false O212_plus_advance_allowed=false")


if __name__ == "__main__":
    main()
