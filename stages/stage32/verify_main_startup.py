#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
START = HERE / "MAIN-START-HERE.md"

EXPECTED_SCHEMA = "STAGE32_MAIN_COMPACT_STATE_V1_POST1648AH_SCOPE_REPAIR_CANDIDATE"
EXPECTED_CANONICAL = "4f984ff1a7d885e6a83a606025b92a114c774707099833a8e7839d24354fb8f0"
EXPECTED_ROUTE = "SPLIT_GLOBAL_NONBIJECTIVITY_BY_AMBIENT_LOCATION_THEN_ANALYZE_SURFACE_NODE_MULTIBRANCH_AND_SMOOTH_LOCUS_CURVE_SINGULARITY_BRANCHES"
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


def require_blob(lock: dict) -> Path:
    path = ROOT / lock["path"]
    if not path.is_file() or git_blob_sha(path) != lock["blob_sha1"]:
        fail(f"blob moved: {lock['path']}")
    return path


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
        "consolidation_base_main_sha": "4e6708cb807cc37bea6509245447a5817965256f",
        "consolidation_hostile_audit_status": "PENDING_REAUDIT_AFTER_SCOPE_REPAIR",
        "last_failed_consolidation_hostile_audit": {
            "review_id": 5127399479,
            "exact_head": "d635edc9d0a13ef5b82732a5bd42debe078a0545",
            "result": "FAIL",
            "reason": "AH contrapositive prematurely localized global normalization nonbijectivity to one of the 47 met surface nodes",
        },
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
        "v6_globally_bijective_normalization_genus1_carrier_excluded": True,
        "v6_remaining_genus1_carrier_requires_nonbijective_normalization_somewhere": True,
        "v6_nonbijectivity_location_identified": False,
        "v6_surface_node_multibranch_branch_open": True,
        "v6_smooth_ambient_locus_curve_singularity_branch_open": True,
    }
    for key, value in required_frontier.items():
        if frontier.get(key) != value:
            fail(f"frontier moved: {key}")
    if "v6_remaining_genus1_carrier_requires_multibranch_node" in frontier:
        fail("revoked premature multibranch-node localization returned")

    if state["current"] != {
        "active_missing_interface": "GLOBAL_NORMALIZATION_NONBIJECTIVITY_LOCATION_AND_TYPE_FOR_ANY_V6_GENUS1_CARRIER",
        "next_exact_route": EXPECTED_ROUTE,
        "stop_semantics": "LEAF_GATE_ONLY_NOT_STAGE_EXHAUSTION",
        "stacked_candidate_audit_status": "PENDING_BATCH_HOSTILE_REAUDIT",
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
    j = load_locked_json(locks["post1648j_trace_orientation"])
    char = load_locked_json(locks["post1643_hdeck_character_preflight"])
    load_locked_json(locks["post1621_hperp_witness"])
    load_locked_json(locks["post1588_direct_mod2"])
    load_locked_json(locks["post1577_terminal_negative"])
    ag = load_locked_json(locks["post1648ag_known140_decomposition"])
    ah = load_locked_json(locks["post1648ah_bijective_normalization_exclusion"])
    ae = load_locked_json(locks["post1648ae_member_source_gap"])
    v6 = load_locked_json(locks["v6_witness_body"])
    note = require_blob(locks["post1648ah_scope_source_note"])
    require_blob(locks["post1648ah_scope_verifier"])
    require_blob(locks["post1648j_trace_orientation_verifier"])
    require_blob(locks["post1643_hdeck_character_verifier"])

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

    if ah["fsm_refinement"]["hypothesis"] != "normalization_map_is_globally_bijective":
        fail("AH global bijectivity hypothesis moved")
    if ah["decision"]["remaining_open_case"] != "ANY_V6_GENUS1_CARRIER_MUST_HAVE_NONBIJECTIVE_NORMALIZATION_SOMEWHERE":
        fail("AH corrected contrapositive moved")
    if ah["decision"]["nonbijectivity_location_identified"]:
        fail("AH nonbijectivity was incorrectly localized")
    split = ah["decision"]["remaining_case_split"]
    if len(split) != 2 or not split[0].startswith("AMBIENT_SURFACE_NODE_MULTIBRANCH") or not split[1].startswith("SMOOTH_AMBIENT_LOCUS_CURVE_SINGULARITY"):
        fail("AH required two-branch split moved")
    if not ah["firewalls"]["does_not_localize_nonbijectivity_to_surface_nodes"]:
        fail("AH localization firewall moved")
    if not ah["firewalls"]["smooth_ambient_locus_curve_singularity_branch_open"]:
        fail("AH smooth-locus branch firewall moved")
    if not ah["local_A1_resolution"]["contradiction"] or ah["v6_exact_data"]["exceptional_mass_e"] != 266:
        fail("AH bounded exclusion arithmetic moved")
    if hashlib.sha256(note.read_bytes()).hexdigest() != ah["source_locks"]["fsm_source_note_sha256"]:
        fail("AH source-note sha256 moved")
    if v6["witness"]["positive_exceptional_support"] != 47 or v6["target"]["d"] != 186:
        fail("V6 witness moved")

    for key, value in state["firewalls"].items():
        if value:
            fail(f"startup firewall moved: {key}")

    print("PASS Stage32 MAIN startup authority")
    print(f"main_state_canonical={EXPECTED_CANONICAL}")
    print("latest_audited_stage32_pr=1643 hostile_review=5123545511")
    print("pr1648_previous_hostile_review=5127399479 result=FAIL scope_repair=PENDING_REAUDIT")
    print("consolidation_base_main=4e6708cb807cc37bea6509245447a5817965256f")
    print("v6_bijective_normalization_excluded=true")
    print("remaining_implication=normalization_nonbijective_somewhere location_identified=false")
    print("open_branches=surface_node_multibranch,smooth_ambient_locus_curve_singularity")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false O212_plus_advance_allowed=false")


if __name__ == "__main__":
    main()
