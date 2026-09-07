#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V1_POST1648AH_CONSOLIDATION_CANDIDATE"
EXPECTED_CANONICAL = "23a414013341eb99a8aa71d5b2216f92188f70892c25dc424b52ca0f2061b81a"
EXPECTED_ROUTE = "QUANTIFY_MULTIBRANCH_LOCAL_TYPES_USING_EXCEPTIONAL_PAIRINGS_AND_FSM_CUSP_POLE_BUDGET"
EXPECTED_WORKING_SET = [
    "stages/stage32/residual-32-01-production/post1648ah-fsm-unibranch-v6-exclusion.json",
    "stages/stage32/residual-32-01-production/post1648ah-fsm-unibranch-source-note.md",
    "stages/stage32/residual-32-01-production/verify_stage32_post1648ah_fsm_unibranch_v6_exclusion.py",
    "stages/stage32/residual-32-01-production/post1648ag-v6-known140-basis-elimination.json",
    "stages/stage32/residual-32-01-production/diagnose_stage32_post1648ag_v6_known140_basis_elimination.py",
    "stages/stage32/residual-32-01-production/post1648ae-v6-carrier-member-source-gap.json",
    "stages/stage32/32-21/post1473-v6-witness-body-recovered.json",
]


def fail(msg: str) -> None:
    raise SystemExit(msg)


def canonical_sha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


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
    required_authority = {
        "startup_authority": "stages/stage32/MAIN-STATE.json",
        "latest_audited_stage32_leaf": "POST1623_HPERP_V6_HDECK_CHARACTER_PREFLIGHT",
        "latest_audited_stage32_pr": 1643,
        "latest_hostile_audit_review_id": 5123545511,
        "latest_audited_exact_head": "8550ab88e12cbbfd42b2d1e07c8f42be124de1a6",
        "latest_exact_head_ci": {"run_id": 34000915113, "job_id": 101399505061, "result": "SUCCESS"},
        "latest_stage32_merge_commit": "dc244645097809948f118d915534a92e56ab60ec",
        "legacy_detailed_files_are_not_ordinary_startup_authority": True,
        "consolidation_candidate_pr": 1648,
        "consolidation_base_main_sha": "652cbd51cd6b546f2a178597f7f2d3474c92b1c6",
        "consolidation_hostile_audit_status": "PENDING",
    }
    if authority != required_authority:
        fail("authority/consolidation synchronization moved")

    if state["fixed_target"] != {
        "row_id": "g1-d186", "degree": 186, "e": 266, "genus": 1,
        "O": 210, "qprime": 4, "Q": 602, "surviving_residues_decimal": [73, 97, 235],
    }:
        fail("fixed target moved")

    frontier = state["current_exact_frontier"]
    required_frontier = {
        "nonexceptional_mod2_witness_source_bound": True,
        "source_bound_nonexceptional_H_character_probe_obtained": True,
        "source_bound_H_character_probe_normal_curve_label_1based": 9,
        "source_bound_H_character_probe_character": "chi_u",
        "abstract_delta_0inf_direction_recovered": True,
        "delta0inf_source_bound_to_Z3_b3_retained_boundary_block": True,
        "principal_b3_stoll_candidates_after_boundary_weierstrass_filter": 32,
        "cecotti_B7_B8_trace_orientation_exact": True,
        "absolute_delta0inf_retained_W_line_identified": False,
        "q602_residue_specific_commutator_obtained": False,
        "v6_self_intersection": 758,
        "v6_canonical_intersection": 186,
        "v6_effective_divisor_exists_by_rr": True,
        "v6_h0_lower_bound": 294,
        "v6_known140_effective_decomposition_obtained": True,
        "v6_known140_decomposition_nonzero_term_count": 61,
        "v6_known140_decomposition_total_multiplicity": 155,
        "v6_integral_irreducible_genus1_member_materialized": False,
        "v6_positive_exceptional_support": 47,
        "v6_exceptional_total_mass": 266,
        "v6_unibranch_bijective_normalization_genus1_carrier_excluded": True,
        "v6_remaining_genus1_carrier_requires_multibranch_node": True,
    }
    for key, value in required_frontier.items():
        if frontier.get(key) != value:
            fail(f"frontier moved: {key}")

    current = state["current"]
    if current != {
        "active_missing_interface": "MULTIBRANCH_LOCAL_TYPE_FOR_ANY_V6_GENUS1_CARRIER",
        "next_exact_route": EXPECTED_ROUTE,
        "stop_semantics": "LEAF_GATE_ONLY_NOT_STAGE_EXHAUSTION",
        "stacked_candidate_audit_status": "PENDING_BATCH_HOSTILE_AUDIT",
    }:
        fail("current route block moved")

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
    # Audited historical layers are immutable source locks at ordinary startup;
    # their heavyweight verifiers are not rerun here. Consolidation/hostile gates
    # may replay expensive layers explicitly when needed.
    j = load_locked_json(locks["post1648j_trace_orientation"])
    char = load_locked_json(locks["post1643_hdeck_character_preflight"])
    load_locked_json(locks["post1621_hperp_witness"])
    load_locked_json(locks["post1588_direct_mod2"])
    load_locked_json(locks["post1577_terminal_negative"])
    ag = load_locked_json(locks["post1648ag_known140_decomposition"])
    ah = load_locked_json(locks["post1648ah_unibranch_exclusion"])
    ae = load_locked_json(locks["post1648ae_member_source_gap"])
    v6 = load_locked_json(locks["v6_witness_body"])

    for verifier_key in ["post1648j_trace_orientation_verifier", "post1643_hdeck_character_verifier"]:
        path = ROOT / locks[verifier_key]["path"]
        if not path.is_file() or git_blob_sha(path) != locks[verifier_key]["blob_sha1"]:
            fail(f"audited verifier blob moved: {verifier_key}")

    if j["decision"]["survivors_current_credit"] != [73, 97, 235] or j["decision"]["absolute_delta0inf_retained_W_line_identified"]:
        fail("post1648J boundary moved")
    if char["fixed_target"]["surviving_residues_decimal"] != [73, 97, 235]:
        fail("audited post1643 survivor set moved")
    if ae["exact_effective_divisor_replay"]["h0_lower_bound"] != 294 or not ae["exact_effective_divisor_replay"]["effective_divisor_exists_in_V6_class"]:
        fail("AE effectivity moved")
    if ae["retained_member_level_boundary"]["actual_integral_irreducible_genus1_carrier_materialized"]:
        fail("AE member firewall moved")
    if ag["status"] != "EXACT_SAT_KNOWN140_MONOID_DECOMPOSITION" or not ag["known140_monoid"]["membership"]:
        fail("AG monoid result moved")
    if (ag["known140_monoid"]["nonzero_term_count"], ag["known140_monoid"]["total_multiplicity"]) != (61, 155):
        fail("AG decomposition counts moved")
    if ah["decision"]["remaining_open_case"] != "ANY_V6_GENUS1_CARRIER_MUST_BE_MULTIBRANCH_OVER_AT_LEAST_ONE_OF_THE_47_MET_SURFACE_NODES":
        fail("AH remaining case moved")
    if not ah["local_A1_resolution"]["contradiction"] or ah["v6_exact_data"]["exceptional_mass_e"] != 266:
        fail("AH bounded exclusion moved")
    if v6["witness"]["positive_exceptional_support"] != 47 or v6["target"]["d"] != 186:
        fail("V6 witness moved")

    for key, value in state["firewalls"].items():
        if value:
            fail(f"startup firewall moved: {key}")

    print("PASS Stage32 MAIN startup authority")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("latest_audited_stage32_pr=1643 hostile_review=5123545511")
    print("consolidation_candidate_pr=1648 hostile_audit=PENDING base_main=652cbd51cd6b546f2a178597f7f2d3474c92b1c6")
    print("v6_effective=true h0_lower_bound=294 known140_explicit=true terms=61 multiplicity=155")
    print("v6_unibranch_genus1_excluded=true remaining_case=multibranch_at_one_or_more_of_47_nodes")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false O212_plus_advance_allowed=false")


if __name__ == "__main__":
    main()
