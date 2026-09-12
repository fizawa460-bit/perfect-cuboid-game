#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

FILES = {
    "n374_state": (HERE / "STATE.json", "a0122c46ec8c72a87f5a510b8faf83205cce44fa"),
    "n374_result": (HERE / "RESULT.json", "4e6fde243d1ea4695f7472ce3444df2b0e3b002c"),
    "n373_state": (HERE.parent / "N373/STATE.json", "9a40813a25507a8f3e322fb79b17d321ea406274"),
    "n373_result": (HERE.parent / "N373/RESULT.json", "2520e180f3637ab393584d95933c4d56ac15c5a8"),
    "n101_state": (HERE.parent / "N101/STATE.json", "18338cf234cdbece7698c625cc83467ce0896081"),
    "n101_result": (HERE.parent / "N101/RESULT.md", "ee95344c2d8cd5e604746663d3cabad3953dac17"),
    "n105_state": (HERE.parent / "N105/STATE.json", "afb86271584a4545bf1cea91f75551252e2ab0f5"),
    "main_state": (ROOT / "stages/stage32/MAIN-STATE.json", "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"),
    "production_state": (ROOT / "stages/stage32/residual-32-01-production/state.json", "931e80ba892ec0d98f3e7b909ac2dd46660c116c"),
    "n362_generator": (HERE.parent / "N362/generate_n362_current_v15_witness_probe.py", "f2b97ffb52dcf48e8e549cf71eb70a6ffcdebb30"),
    "prefix_engine": (ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py", "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b"),
    "reynolds_map": (ROOT / "stages/stage32/residual-32-01-production/direct_picard_reynolds_rank2_quotient_class_map.py", "64bb7bd1b78ac5a800113f2a9249c3037bab6519"),
    "ex5_handoff": (ROOT / "stages/stage32/proof/CUT192-EX5-E8-HANDOFF-SATISFIED.json", "b8ff5a4b962c24a6e4f4bca5621cbdb79f6d4781"),
}

STATE_CANON = "172a472b799435b6486f68ef5e1131b38ee28ce6e872559c9195caef370d798c"
RESULT_CANON = "db888ed985b46de6506f1dd9b3e383dcbeb7ab9fcd6f1cf05b94fe2bc88d7602"
N373_STATE_CANON = "100b1be5c34481464d8bc2f98454b2e47ae3a78600c25675c140bdcab1c003a1"
N373_RESULT_CANON = "f480eec4f07f12e5f93341f307071b4ca0d44d6065bc65aa83ad01545576151d"
MAIN_CANON = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return csha(q)


def load_json(name: str, canon: str | None = None) -> dict:
    path, expected = FILES[name]
    req(blob(path) == expected, f"blob drift: {name}")
    obj = json.loads(path.read_text())
    if canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == canon, f"stored canonical drift: {name}")
        req(canonical(obj) == canon, f"canonical drift: {name}")
    return obj


def main() -> None:
    for name, (path, expected) in FILES.items():
        req(blob(path) == expected, f"blob drift: {name}: {path}")

    state = load_json("n374_state", STATE_CANON)
    result = load_json("n374_result", RESULT_CANON)
    n373_state = load_json("n373_state", N373_STATE_CANON)
    n373_result = load_json("n373_result", N373_RESULT_CANON)
    n101 = load_json("n101_state")
    n105 = load_json("n105_state")
    main_state = load_json("main_state", MAIN_CANON)
    handoff = load_json("ex5_handoff")

    req(state["status"] == "RETAINED_GLOBAL_COMPRESSION_REOPEN_AUDIT_NO_CREDIT", "N374 state status drift")
    req(result["status"] == state["status"], "N374 result/state status mismatch")
    req(state["next_gate"] == "SOURCE_LOCKED_NUMERICAL_LEAF_INVARIANCE_SIGNATURE_PROTOTYPE_NO_CREDIT", "N374 next gate drift")
    req(state["method"]["heavy_compute_authorized"] is False, "N374 unexpectedly authorizes heavy compute")
    req(state["method"]["rerun_n373_solver"] is False, "N374 unexpectedly reruns N373")
    req(state["method"]["timeout_ceiling_escalated"] is False, "N374 timeout ceiling escalated")

    req(n373_state["status"] == "RETAINED_PARTIAL_X4_PROJECTION_UNKNOWN_TIMEOUT_NO_CREDIT", "N373 retained boundary drift")
    req(n373_result["status"] == "PARTIAL_X4_PROJECTION_UNKNOWN_TIMEOUT", "N373 result status drift")
    req(n373_result["projection"]["complete"] is False, "N373 unexpectedly complete")
    req(n373_result["projection"]["feasible_x4"] == [0], "N373 seed set drift")
    req(n373_result["method"]["per_check_timeout_ms"] == 5000, "N373 timeout ceiling drift")
    req(n373_result["method"]["reason_unknown"] == "timeout", "N373 timeout reason drift")

    req(n101["semantic_key"] == "s32-01-178:indexed-terminal-compression", "N101 semantic key drift")
    rr101 = n101["retained_result"]
    req(rr101["status"] == "BLOCKED_WITH_EXACT_REDESIGN", "N101 blocker status drift")
    req(rr101["safe_reduced_terminal_family_count"] is None, "N101 unexpectedly has safe reduced count")
    req(rr101["known_downstream_projection_class_count"] == 16384, "N101 projection count drift")
    req(len(rr101["reopen_condition"]) == 4, "N101 reopen contract drift")

    req(n105["semantic_key"] == "s32-01-178:independent-global-cut-discovery", "N105 semantic key drift")
    req(n105["retained_result"]["classification"] == "NO_NEW_GLOBAL_CUT_IN_SEARCHED_ASSETS", "N105 classification drift")
    req("MISSING_TERMINAL_TO_COMPLETE_PICARD64_SOURCE_LOCK" in n105["retained_result"]["obstruction_signatures"], "N105 historical completion blocker drift")

    frontier = main_state["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == 17128, "MAIN V15 strata drift")
    req(frontier["authoritative_remaining_terminals"] == 47598978285064933757427, "MAIN V15 terminal drift")
    req(frontier["full178_numerical_census_complete"] is False, "FULL178 unexpectedly complete")

    req(handoff["status"] == "SATISFIED", "EX5/CUT handoff status drift")
    req(handoff["consumer_lane"] == "CUT", "EX5 handoff consumer ownership drift")
    sem = handoff["interface_semantics"]
    req(sem["artifact_type"] == "SOURCE_LOCKED_EXACT_TERMINAL_TO_PICARD64_COMPLETION_INTERFACE", "EX5 handoff interface drift")
    req(sem["handoff_universe_blocks"] == 7596 and sem["handoff_universe_terminals"] == 858348 and sem["terminal_block_width"] == 113, "EX5 e8 scope drift")
    req(handoff["audit_and_credit_firewall"]["full178_complete"] is False, "EX5 handoff unexpectedly completes FULL178")

    n362_text = FILES["n362_generator"][0].read_text()
    for needle in (
        'parent["selected_exceptional_pairings"]',
        's.add(y[label - 1] == value)',
        's.add(Or(*[(y[48] % 8) == r for r in allowed]))',
        'ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]',
    ):
        req(needle in n362_text, f"N362 exact leaf interface marker missing: {needle}")

    prefix_text = FILES["prefix_engine"][0].read_text()
    for needle in (
        "class PrefixMembershipOracle:",
        "def close_permutation_group(permutations_1based:",
        "def canonical_pairing_key(pairings:",
        "return min(permute_pairings(base, g) for g in group)",
    ):
        req(needle in prefix_text, f"prefix engine marker missing: {needle}")
    req("def canonical_pairing_key(pairings: Sequence[int], group:" in prefix_text, "canonical key is not explicitly caller-supplied-group based")

    reynolds_text = FILES["reynolds_map"][0].read_text()
    req("EXPECTED_PROJECTION_CLASS_COUNT = 16384" in reynolds_text, "Reynolds class count marker drift")
    req('"map_is_representation_only": True' in reynolds_text, "Reynolds representation-only firewall drift")
    req('"terminal_family_materialization_run": False' in reynolds_text, "Reynolds materialization firewall drift")

    findings = result["source_locked_findings"]
    req(findings["n101_reopen_status"] == "NOT_YET_REOPENED_GLOBALLY", "N374 overclaims N101 reopening")
    req(findings["n101_s1_exact_semantic_sufficiency"] == "UNPROVED", "N374 overclaims S1")
    req(findings["prefix_picard_membership"]["numerical_leaf_preserving_group_source_locked"] is False, "N374 overclaims preserved group")
    req(findings["prefix_picard_membership"]["multiplicity_conservation_under_group_source_locked"] is False, "N374 overclaims group multiplicity")
    req(findings["reynolds_rank2_quotient"]["map_is_representation_only"] is True, "N374 Reynolds semantics drift")

    decision = result["decision"]
    req(decision["declare_n101_reopened_now"] is False, "N374 declares N101 reopened")
    req(decision["declare_symmetry_quotient_valid_now"] is False, "N374 declares symmetry quotient")
    req(decision["rerun_n373_timeout_route"] is False, "N374 reruns timeout route")
    req(decision["duplicate_cut_finite_ring_route"] is False, "N374 duplicates CUT")
    req(decision["next_exact_unit"] == "SOURCE_LOCKED_NUMERICAL_LEAF_INVARIANCE_SIGNATURE_PROTOTYPE", "N374 next unit drift")

    for owner in (state, result):
        for key, value in owner["credit"].items():
            req(value is False, f"credit firewall drift: {key}")

    print(json.dumps({
        "verdict": "PASS_N374_GLOBAL_COMPRESSION_REOPEN_AUDIT_NO_CREDIT",
        "n101_reopened": False,
        "s1_semantic_sufficiency_proved": False,
        "s2_prefix_infrastructure_available": True,
        "generic_canonical_pairing_key_available": True,
        "numerical_leaf_preserving_group_source_locked": False,
        "reynolds_representation_only": True,
        "rerun_n373": False,
        "timeout_ceiling_escalated": False,
        "full178_complete": False,
        "main_pruning_credit": False,
        "merge_authorized": False,
        "next_gate": state["next_gate"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
