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
EXPECTED_CANONICAL = "f8354119d57fe7d593fa3a95a51b8b1ea5f7d5676e2ef72f471f3b65edf7c29e"
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
    got = git_blob_sha(path)
    if got != lock["blob_sha1"]:
        fail(f"blob moved: {lock['path']} got={got} expected={lock['blob_sha1']}")
    return path


def assert_json_canonical(path: Path, expected: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    got = canonical_sha(obj)
    if got != expected:
        fail(f"canonical moved: {path} got={got} expected={expected}")
    if obj.get("canonical_sha256_without_this_field") != expected:
        fail(f"recorded canonical moved: {path}")
    return obj


def assert_startup_contract_has_no_mutable_current_literals(startup: str, state: dict) -> None:
    """MAIN-START-HERE is a fixed contract; mutable current data lives only in MAIN-STATE."""
    mutable_sections = [
        state["fixed_target"],
        state["current_exact_frontier"],
        state["current"],
        state["firewalls"],
        state["cleanup_gate"],
    ]

    # Reject distinctive machine field names, but not generic one-letter keys such as
    # e/O/Q that naturally occur in prose. Their current values are checked separately.
    for section in mutable_sections:
        for key in section:
            if len(key) >= 4 and key in startup:
                fail(f"mutable MAIN-STATE field leaked into MAIN-START-HERE: {key}")

    # Exact route/frontier/cleanup identifiers are also forbidden. Generic prose such as
    # "current target" or "current firewall values" is allowed and should point to MAIN-STATE.
    for section in mutable_sections:
        for value in section.values():
            if isinstance(value, str) and len(value) >= 8 and value in startup:
                fail(f"mutable MAIN-STATE literal leaked into MAIN-START-HERE: {value}")

    target = state["fixed_target"]
    forbidden_renderings = {
        str(target["row_id"]),
        f"O={target['O']}",
        f"Q={target['Q']}",
        f"qprime={target['qprime']}",
        ",".join(str(x) for x in target["surviving_residues_decimal"]),
        ", ".join(str(x) for x in target["surviving_residues_decimal"]),
        str(target["surviving_residues_decimal"]),
    }
    for literal in forbidden_renderings:
        if literal in startup:
            fail(f"mutable target literal leaked into MAIN-START-HERE: {literal}")


def main() -> None:
    state = json.loads(STATE.read_text(encoding="utf-8"))
    if state.get("schema") != EXPECTED_SCHEMA:
        fail("MAIN-STATE schema moved")
    if state.get("role") != "ORDINARY_MAIN_STARTUP_PROJECTION_NOT_A_PROOF_CERTIFICATE":
        fail("MAIN-STATE role moved")
    if canonical_sha(state) != EXPECTED_CANONICAL:
        fail("MAIN-STATE canonical mismatch")
    if state.get("canonical_sha256_without_this_field") != EXPECTED_CANONICAL:
        fail("MAIN-STATE recorded canonical mismatch")
    if state.get("fixed_target") != EXPECTED_TARGET:
        fail("fixed target moved")

    startup = START.read_text(encoding="utf-8")
    required_startup_fragments = [
        "Ordinary `Stage32-main-batch` reads, in this order:",
        "`AGENTS.md`",
        "`stages/stage32/MAIN-STATE.json`",
        "only the paths listed in `MAIN-STATE.json.current_leaf_working_set`",
        "Read all such current values only from `MAIN-STATE.json`.",
        "Do not merge without explicit user authorization.",
    ]
    for fragment in required_startup_fragments:
        if fragment not in startup:
            fail(f"startup contract fragment missing: {fragment}")
    assert_startup_contract_has_no_mutable_current_literals(startup, state)

    working = state.get("current_leaf_working_set")
    if not isinstance(working, list) or not working:
        fail("current_leaf_working_set missing")
    if len(working) != len(set(working)):
        fail("duplicate path in current_leaf_working_set")
    for rel in working:
        if not (ROOT / rel).is_file():
            fail(f"working-set path missing: {rel}")
    forbidden = EXPECTED_EXCLUDED_STARTUP.intersection(working)
    if forbidden:
        fail(f"legacy file leaked into ordinary startup: {sorted(forbidden)}")
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
    q = latest["exceptional_quotient_preflight"]
    if q != {
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

    frontier = state["current_exact_frontier"]
    if frontier != {
        "symmetry_parity_orbit_sum_lane_closed": True,
        "direct_mod2_fiber_divisor_identity_obtained": True,
        "direct_mod2_fiber_divisor_identity_support": "EXCEPTIONAL_SPAN_ONLY",
        "image_in_mod2_quotient_by_exceptional_span": "0",
        "nonexceptional_mod2_class_obtained": False,
        "q602_residue_specific_commutator_obtained": False,
    }:
        fail("compact current frontier moved")

    fire = state["firewalls"]
    if fire != {
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
    }:
        fail("startup firewalls moved")

    cleanup = state["cleanup_gate"]
    if cleanup["stage32_root_cleanup_started"] is not False:
        fail("root cleanup started inside startup-authority PR")
    if cleanup["proof_or_source_locked_assets_may_be_deleted_without_reference_audit"] is not False:
        fail("unsafe cleanup permission detected")

    print("PASS Stage32 MAIN startup authority")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("startup_chain=AGENTS->MAIN-START-HERE->MAIN-STATE->current_leaf_working_set")
    print("main_start_here_mutable_current_literals=false")
    print("legacy_controller_state_runkey_in_ordinary_startup=false")
    print("Q602_excluded=false O210_excluded=false O212_plus_advance_allowed=false")
    print("stage32_root_cleanup_started=false")


if __name__ == "__main__":
    main()
