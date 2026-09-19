#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = HERE / "MAIN-STATE.json"
FULL = HERE / "management/btva-compressed-lift/BTVA-D8-FULL343-RETAINED-CHECKPOINT.json"
ALL140 = HERE / "management/btva-compressed-lift/BTVA-D8-ALL140-RECEIVER-SEMANTICS-RETAINED.json"
CONIC = HERE / "management/btva-compressed-lift/BTVA-D8-PLANE-CONIC-EXCEPTION-SEPARATION.json"
DIAG = HERE / "management/btva-compressed-lift/diagnose_btva_all140_receiver_nonnegativity.py"
NORMALMASS = HERE / "management/btva-compressed-lift/run_btva_static7_normalmass_bounded_panel.py"
RELAXED = HERE / "management/btva-compressed-lift/run_btva_static7_bounded_panel.py"
WAVE4_SELECTOR = HERE / "management/btva-compressed-lift/BTVA-D8-E12-RATIO-DIRECTED-WAVE4-SELECTOR-RETAINED.json"
WAVE4_SOLVER = HERE / "management/btva-compressed-lift/run_btva_e12_ratio_directed_basis_pairing_panel_wave4.py"
WAVE3_QBIN = HERE / "management/btva-compressed-lift/BTVA-D8-E12-WAVE3-PARTIAL-QBIN-RETAINED.json"

CURRENT_MAIN = "83ae3f66cfcbdfaaaebf149bea078d1b0ff11c49"
BOUND = 157570677819451133507
V41_BOUND = 179119009547804181594
TIGHTENING = 21548331728353048087
FULL_BLOB = "4ae970e17b0d7168f6d2ffd0644195f2ab57ae8d"
FULL_CANON = "5e111a460381d9df7662b7f552eadde68953ecee304cf7a47d4aa52d2a9ba776"
ALL140_BLOB = "c4c94fc8e2b45ee51660fe3665160fde98659056"
ALL140_CANON = "6561ddcf40b27ca433563635446d6d614ce36f4c26640c11d5ae61bf46abcff8"
CONIC_BLOB = "75d384c194c678ff6158ea793e943bce91741bb8"
DIAG_BLOB = "1dc8650e8bf1029828c7971411c9bcb5212e040b"
NORMALMASS_BLOB = "971cf6bab500eefd04bbef870807f1badc8b07c4"
RELAXED_BLOB = "e44bec7ad9c0b7a4d8d7d87a455f181a681035c6"
WAVE4_SELECTOR_BLOB = "2e340d1605f6b86b5e8bcc681871e1e9656e545c"
WAVE4_SOLVER_BLOB = "5160318e0d3fbe616636e115e63434226e7016f6"
WAVE3_QBIN_BLOB = "fd6cdc5386bc8b3b30a20aa6c641d7e4a7cb54e7"
WAVE3_QBIN_CANON = "edbd101483a9dc08a28203847db11c48919550eb7fe3ea25c5fe5a30d48c188c"
WAVE4_QBIN = HERE / "management/btva-compressed-lift/BTVA-D8-E12-WAVE4-27UNSAT-QBIN-RETAINED.json"
WAVE4_QBIN_BLOB = "4ccbdbe4172eee02fdebf73d2d17c1deb5492525"
WAVE4_QBIN_CANON = "8f4d67b63ed3afb4fb8907344eeb1feb8ea8b0a84d7cfd8c313408702c044920"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def load(path: Path, expected_blob: str, expected_canon: str) -> dict:
    req(blob(path) == expected_blob, path.name + " blob drift")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected_canon, path.name + " stored canonical drift")
    req(canon(obj) == expected_canon, path.name + " canonical drift")
    return obj


def main() -> None:
    state = json.loads(STATE.read_text(encoding="utf-8"))
    req(canon(state) == state.get("canonical_sha256_without_this_field"), "MAIN state canonical drift")
    req(state["authority_sync"]["current_repository_main"] == CURRENT_MAIN, "repository main drift")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "strata authority drift")
    req(f["authoritative_remaining_terminals"] == BOUND, "authority bound drift")
    req(f["predecessor_v41_authoritative_remaining_terminals"] == V41_BOUND, "V41 bound drift")
    req(f["v42_hpadj21_certified_numeric_bound_tightening_vs_v41"] == TIGHTENING, "V42 tightening drift")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False, "authority overclaim")
    req(f["v44_wave4_exact_27_unsat_qbin_reoptimization_complete"] is True, "wave4 qbin completion state")
    req(f["v44_wave4_exact_27_unsat_qbin_row_floor"] == 418504, "wave4 qbin state floor")
    req(f["v44_wave4_candidate_total_tightening_vs_hpadj21"] == 29927, "wave4 qbin state tightening")
    req(f["v44_wave4_candidate_global_upper_bound_if_promoted"] == "157570677819451103580", "wave4 qbin state candidate bound")
    req(f["v44_wave4_candidate_main_credit"] is False, "wave4 qbin state credit firewall")

    full = load(FULL, FULL_BLOB, FULL_CANON)
    all140 = load(ALL140, ALL140_BLOB, ALL140_CANON)
    req(blob(CONIC) == CONIC_BLOB, "conic separation blob drift")
    conic = json.loads(CONIC.read_text(encoding="utf-8"))
    req(conic["status"] == "STRUCTURAL_SEPARATION_PASS_ZERO_CREDIT", "conic separation status")
    req(conic["separation"]["target_hyperplane_degree"] == 8 and conic["separation"]["plane_conic_hyperplane_degree"] == 2, "conic degree separation")
    req(blob(DIAG) == DIAG_BLOB, "all140 diagnostic blob drift")
    req(blob(NORMALMASS) == NORMALMASS_BLOB, "normalmass solver drift")
    req(blob(RELAXED) == RELAXED_BLOB, "relaxed solver drift")
    req(blob(WAVE4_SELECTOR) == WAVE4_SELECTOR_BLOB, "wave4 selector drift")
    req(blob(WAVE4_SOLVER) == WAVE4_SOLVER_BLOB, "wave4 solver drift")
    wave3_qbin = load(WAVE3_QBIN, WAVE3_QBIN_BLOB, WAVE3_QBIN_CANON)
    req(wave3_qbin["result"]["wave3_partial_exact_qbin_row_floor"] == 425610, "wave3 qbin floor drift")
    req(wave3_qbin["result"]["total_tightening_vs_hpadj21_baseline"] == 22821, "wave3 qbin tightening drift")
    wave4_qbin = load(WAVE4_QBIN, WAVE4_QBIN_BLOB, WAVE4_QBIN_CANON)
    req(wave4_qbin["result"]["wave4_27unsat_exact_qbin_row_floor"] == 418504, "wave4 qbin floor drift")
    req(wave4_qbin["result"]["additional_tightening_beyond_wave3_partial"] == 7106, "wave4 incremental tightening drift")
    req(wave4_qbin["result"]["total_tightening_vs_hpadj21_baseline"] == 29927, "wave4 total tightening drift")
    req(wave4_qbin["authority_candidate"]["candidate_global_upper_bound_if_promoted"] == "157570677819451103580", "wave4 candidate bound drift")
    req(wave4_qbin["composition"]["five_wave4_unknown_keys_left_adversarially_present"] is True, "wave4 UNKNOWN firewall drift")

    r = full["result"]
    req(full["target"]["base4_key_count"] == 343 and full["target"]["terminal_mass"] == 1278934, "full343 population drift")
    req((r["unsat_base4_fibers"], r["unknown_base4_fibers"], r["compatible_sat_base4_fibers"]) == (255, 88, 0), "full343 outcome drift")
    req(r["terminal_mass_covered_by_unsat_fibers"] == 1030560 and r["survivor_terminal_mass"] == 248374, "full343 mass drift")
    pairs = r["survivor_index_mass_pairs"]
    req(len(pairs) == 88 and len({int(x[0]) for x in pairs}) == 88, "survivor identity drift")
    req(sum(int(x[1]) for x in pairs) == 248374, "survivor mass sum drift")
    req(1278934 - 1030560 == 248374, "population conservation")
    req(full["execution"]["aggregate_canonical_sha256"] == "8e3d8b51955d89b1bb83b7c79ad0cc9e82d90510edfa6d023a24b4fe585455db", "aggregate identity drift")
    req(full["semantics"]["unknown_is_not_unsat"] is True and full["semantics"]["main_authority_changed"] is False, "full343 firewall drift")

    ar = all140["result"]
    req(ar["all140_count"] == 140 and ar["normal_known_nonexceptional_count"] == 92 and ar["exceptional_count"] == 48, "all140 count drift")
    req(ar["degree_histogram"] == {"0": 48, "2": 32, "4": 60}, "all140 degree histogram drift")
    req(ar["target_degree_equal_row_count"] == 0 and ar["target_degree_equal_rows_0based"] == [], "unexpected degree-8 known row")
    sem = all140["semantics"]
    req(sem["all140_rows_are_known_curve_or_exceptional_pairing_rows"] is True, "all140 row semantics")
    req(sem["d8_candidate_distinct_from_every_all140_known_curve_by_hyperplane_degree"] is True, "d8 distinctness")
    req(sem["all140_nonnegativity_is_necessary_for_d8_integral_curve_receiver"] is True, "all140 receiver necessity")
    req(all140["execution"]["diagnostic_canonical_sha256"] == "4dfea2684f3ec750643b7aabd404a73ff97a4fedda9327117624cd603e3f2ffc", "diagnostic identity drift")

    cur = state["current"]
    locks = state["source_locks"]
    req(locks["btva_d8_full343_retained"]["blob_sha1"] == FULL_BLOB, "full343 state lock")
    req(locks["btva_d8_all140_receiver_semantics"]["blob_sha1"] == ALL140_BLOB, "all140 state lock")
    req(locks["btva_d8_conic_exception"]["blob_sha1"] == CONIC_BLOB, "conic state lock")
    qlock = locks["btva_d8_e12_wave4_27unsat_qbin"]
    req(qlock["retained_blob_sha1"] == WAVE4_QBIN_BLOB, "wave4 qbin state blob lock")
    req(qlock["artifact_canonical_sha256"] == WAVE4_QBIN_CANON, "wave4 qbin state canonical lock")
    req(qlock["workflow_run_id"] == 35408417941 and qlock["artifact_id"] == 10572768864, "wave4 qbin artifact identity")
    req(qlock["wave4_27unsat_exact_qbin_row_floor"] == 418504 and qlock["candidate_total_tightening_vs_hpadj21"] == 29927, "wave4 qbin state result")
    req(qlock["main_pruning_credit"] is False and qlock["five_unknown_left_adversarial"] is True, "wave4 qbin state firewall")
    sw = locks["live_specialist_sweep"]
    req(cur["mainbatch_stop_gate"] == "NONE", "historical MAIN stop gate drift")
    req(cur["research_os_checkpoint_gate"] == "NONE", "Research OS checkpoint gate drift")
    req(cur["research_os_checkpoint_audit_status"] == "PASS", "Research OS checkpoint audit status drift")
    req(cur["research_os_checkpoint_audit_review_id"] == 5253605587, "Research OS checkpoint review drift")
    req(cur["research_os_checkpoint_audited_exact_head"] == "e1795ad7ad47f45ca46e435dfd204e3bba8d6064", "Research OS checkpoint audited head drift")
    req(cur["latest_main_native_research"] == "V44_BTVA_D8_E12_WAVE4_27UNSAT_EXACT_QBIN__ZERO_MAIN_CREDIT", "V44 wave4 routing drift")
    w4 = locks["btva_d8_e12_wave4_panel"]
    req(w4["exact_head"] == "01a4ba3ab34df2ece9cf9c3236c7ebe2b3eb54a7", "wave4 exact-head drift")
    req(w4["workflow_run_id"] == 35405380332 and w4["artifact_id"] == 10571698422, "wave4 artifact identity drift")
    req(w4["artifact_canonical_sha256"] == "0b5528b4ab2eebb99bcdc5a83ce26ccc2aecb9669a2f7b074a6c223fd1a90a76", "wave4 canonical drift")
    req((w4["unsat_base4_count"], w4["unknown_base4_count"], w4["compatible_sat_base4_count"]) == (27, 5, 0), "wave4 outcome drift")
    req(w4["all_selected_unsat"] is False and w4["main_pruning_credit"] is False, "wave4 firewall drift")
    req(sw["lane_178_pr"] == 1821 and sw["lane_178_head"] == "fd8ffe03ff4b90f811e317a43e76a95f31c30464" and sw["lane_178_pending_main_handoff"] == "NONE", "178 live observation")
    req(sw["lane_178_latest_audited_exact_head"] == "8a8efc48866f8008d253c21ebd272e698d18dc44" and sw["lane_178_latest_audit_review_id"] == 5245717271, "178 audited-boundary observation")
    req(sw["ex5_pr"] == 1823 and sw["ex5_head"] == "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2" and sw["ex5_pending_main_handoff"] == "NONE", "EX5 live observation")
    req(sw["mb_pr"] == 1819 and sw["mb_head"] == "dfcfc56f0f652e2a2a072102ec2d469870ccdcba" and sw["mb_pending_main_handoff"] == "NONE", "MB live observation")
    req(sw["bridge_pr"] == 1813 and sw["bridge_head"] == "ee755bbfd46f405ca83e4930b354ee63459ad362" and sw["bridge_runkey_generation"] == 1 and sw["bridge_runkey_armed"] is True and sw["bridge_pending_main_handoff"] == "NONE", "BRIDGE live observation")
    req(sw["bridge_latest_audited_doorstep_head"] == "4a84fc8c09bb2ccb35aab965797aeaefd3b6efe8" and sw["bridge_latest_audit_review_id"] == 5247726057, "BRIDGE audited-doorstep observation")
    req(sw["cut_open_successor"] is False and sw["cut_handoff"] == "NONE", "CUT observation")

    for obj in (full["firewalls"], all140["firewalls"], state["firewalls"]):
        for key in ("main_pruning_credit", "receiver_credit", "effectivity_credit", "theorem_credit", "endpoint_credit", "full178_complete", "stage32_closed", "merge_authorized"):
            if key in obj:
                req(obj[key] is False, "firewall " + key)
    print("PASS: V44 d=8 full343 result retained exactly with 255 UNSAT / 88 timeout / 0 SAT")
    print("PASS: d=8 all140 nonnegativity receiver necessity and plane-conic separation are structurally closed")
    print("PASS: V43 numerical authority remains unchanged; V44 carries zero MAIN/theorem/effectivity/endpoint credit")


if __name__ == "__main__":
    main()
