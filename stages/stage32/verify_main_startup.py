#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
H = Path(__file__).resolve().parent
STATE = H / "MAIN-STATE.json"
START = H / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V1_POST1588_DIRECT_MOD2_EXCEPTIONAL_ONLY"
EXPECTED_CANONICAL = "7896726df9bb9858c972460d88e94e1b73b235e2e4f892445915a7072a605719"
EXPECTED_TARGET = {
    "row_id": "g1-d186", "degree": 186, "e": 266, "genus": 1,
    "O": 210, "qprime": 4, "Q": 602,
    "surviving_residues_decimal": [73, 97, 235],
}
EXPECTED_EXCLUDED_STARTUP = {
    "stages/stage32/controller.json",
    "stages/stage32/residual-32-01-production/state.json",
    "stages/stage32/runkeys/residual32-01-full178-production.json",
    "stages/stage32/ROADMAP.md",
    "stages/stage32/GOAL_AND_STOP_CONTRACT.md",
    "stages/stage32/ROADMAP-32-01-RESIDUAL-CLOSURE.md",
    "stages/stage32/ROADMAP-32-19-21-REANCHOR.md",
    "stages/stage32/HISTORY.md",
}
EXPECTED_FRONTIER = {
    "symmetry_parity_orbit_sum_lane_closed": True,
    "direct_mod2_fiber_divisor_identity_obtained": True,
    "direct_mod2_fiber_divisor_identity_support": "EXCEPTIONAL_SPAN_ONLY",
    "image_in_mod2_quotient_by_exceptional_span": "0",
    "nonexceptional_mod2_class_obtained": False,
    "q602_residue_specific_commutator_obtained": False,
}
EXPECTED_FIREWALLS = {
    "Q602_excluded": False,
    "O210_excluded": False,
    "O212_plus_advance_allowed": False,
    "controller_promotion_granted": False,
    "heavy_compute_authorized_by_startup_state": False,
    "receiver_credit": False,
    "route_credit": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_existence_claim": False,
    "perfect_cuboid_nonexistence_claim": False,
}
EXPECTED_CLEANUP = {
    "stage32_root_cleanup_started": True,
    "root_cleanup_phase": "PHASE_B_LOOSE_LEGACY_ROOT_RELOCATION_PENDING_HOSTILE_AUDIT",
    "archive_manifest": "stages/stage32/archive/legacy-root/manifest.json",
    "proof_or_source_locked_assets_may_be_deleted_without_reference_audit": False,
    "next_cleanup_phase": "AFTER_PHASE_B_HOSTILE_AUDIT_REVIEW_REFERENCED_ROOT_AUTHORITY_FILES",
}


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


def assert_blob(lock: dict) -> Path:
    path = ROOT / lock["path"]
    if not path.is_file():
        fail(f"missing locked path: {lock['path']}")
    if git_blob_sha(path) != lock["blob_sha1"]:
        fail(f"blob moved: {lock['path']}")
    return path


def assert_json_canonical(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if canonical_sha(obj) != expected or obj.get("canonical_sha256_without_this_field") != expected:
        fail(f"canonical moved: {path}")
    return obj


def assert_startup_contract_has_no_mutable_current_literals(startup: str, state: dict) -> None:
    mutable_sections = [
        state["fixed_target"], state["current_exact_frontier"], state["current"],
        state["firewalls"], state["cleanup_gate"],
    ]
    for section in mutable_sections:
        for key in section:
            if len(key) >= 4 and key in startup:
                fail(f"mutable MAIN-STATE field leaked into MAIN-START-HERE: {key}")
        for value in section.values():
            if isinstance(value, str) and len(value) >= 8 and value in startup:
                fail(f"mutable MAIN-STATE literal leaked into MAIN-START-HERE: {value}")
    target = state["fixed_target"]
    forbidden = {
        str(target["row_id"]), f"O={target['O']}", f"Q={target['Q']}",
        f"qprime={target['qprime']}",
        ",".join(str(x) for x in target["surviving_residues_decimal"]),
        ", ".join(str(x) for x in target["surviving_residues_decimal"]),
        str(target["surviving_residues_decimal"]),
    }
    for literal in forbidden:
        if literal in startup:
            fail(f"mutable target literal leaked into MAIN-START-HERE: {literal}")


def main() -> None:
    state = json.loads(STATE.read_text(encoding="utf-8"))
    if state.get("schema") != EXPECTED_SCHEMA:
        fail("MAIN-STATE schema moved")
    if state.get("role") != "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE":
        fail("MAIN-STATE role moved")
    if canonical_sha(state) != EXPECTED_CANONICAL or state.get("canonical_sha256_without_this_field") != EXPECTED_CANONICAL:
        fail("MAIN-STATE canonical mismatch")
    if state.get("fixed_target") != EXPECTED_TARGET:
        fail("fixed target moved")

    startup = START.read_text(encoding="utf-8")
    for fragment in [
        "Ordinary `Stage32-main-batch` reads, in this order:",
        "`AGENTS.md`", "`stages/stage32/MAIN-STATE.json`",
        "only the paths listed in `MAIN-STATE.json.current_leaf_working_set`",
        "Read all such current values only from `MAIN-STATE.json`.",
        "Do not merge without explicit user authorization.",
    ]:
        if fragment not in startup:
            fail(f"startup contract fragment missing: {fragment}")
    assert_startup_contract_has_no_mutable_current_literals(startup, state)

    working = state.get("current_leaf_working_set")
    if not isinstance(working, list) or not working or len(working) != len(set(working)):
        fail("invalid current_leaf_working_set")
    for rel in working:
        if not (ROOT / rel).is_file():
            fail(f"working-set path missing: {rel}")
    if EXPECTED_EXCLUDED_STARTUP.intersection(working):
        fail("legacy file leaked into ordinary startup")
    if set(state.get("ordinary_startup_excludes", [])) != EXPECTED_EXCLUDED_STARTUP:
        fail("ordinary startup exclusion set moved")

    locks = state["source_locks"]
    latest_path = assert_blob(locks["post1588_direct_mod2"])
    assert_blob(locks["post1588_source_note"])
    terminal_path = assert_blob(locks["post1577_terminal_negative"])
    assert_blob(locks["post1484_fiber_divisor_source"])
    latest = assert_json_canonical(latest_path, locks["post1588_direct_mod2"]["canonical_sha256"])
    terminal = assert_json_canonical(terminal_path, locks["post1577_terminal_negative"]["canonical_sha256"])
    if latest["fixed_target"]["surviving_residues_decimal"] != [73, 97, 235]:
        fail("latest survivor set moved")
    if latest["exceptional_quotient_preflight"] != {
        "mod2_fiber_class_lies_in_exceptional_span": True,
        "image_in_mod2_quotient_by_exceptional_span": "0",
        "nonexceptional_mod2_class_obtained": False,
        "q602_residue_specific_commutator_obtained": False,
    }:
        fail("post1588 bounded conclusion moved")
    if latest["decision"]["Q602_excluded"] is not False or latest["decision"]["O210_excluded"] is not False:
        fail("post1588 exclusion firewall moved")
    if terminal["lane_closure"]["symmetry_parity_orbit_sum_lane_exhausted"] is not True:
        fail("post1577 lane closure moved")
    if "INDEPENDENT_PRIMITIVE_OR_ODD_COMMUTATOR_INVARIANT" not in terminal["lane_closure"]["reentry_requires"]:
        fail("post1577 reentry contract moved")

    if state["current_exact_frontier"] != EXPECTED_FRONTIER:
        fail("compact current frontier moved")
    if state["firewalls"] != EXPECTED_FIREWALLS:
        fail("startup firewalls moved")
    if state["cleanup_gate"] != EXPECTED_CLEANUP:
        fail("cleanup gate moved")

    print("PASS Stage32 MAIN startup authority")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("startup_chain=AGENTS->MAIN-START-HERE->MAIN-STATE->current_leaf_working_set")
    print("main_start_here_mutable_current_literals=false")
    print("legacy_controller_state_runkey_in_ordinary_startup=false")
    print("Q602_excluded=false O210_excluded=false O212_plus_advance_allowed=false")
    print("stage32_root_cleanup_phase=PHASE_B_PENDING_HOSTILE_AUDIT")


if __name__ == "__main__":
    main()
