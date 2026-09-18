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

    full = load(FULL, FULL_BLOB, FULL_CANON)
    all140 = load(ALL140, ALL140_BLOB, ALL140_CANON)
    req(blob(CONIC) == CONIC_BLOB, "conic separation blob drift")
    conic = json.loads(CONIC.read_text(encoding="utf-8"))
    req(conic["status"] == "STRUCTURAL_SEPARATION_PASS_ZERO_CREDIT", "conic separation status")
    req(conic["separation"]["target_hyperplane_degree"] == 8 and conic["separation"]["plane_conic_hyperplane_degree"] == 2, "conic degree separation")
    req(blob(DIAG) == DIAG_BLOB, "all140 diagnostic blob drift")
    req(blob(NORMALMASS) == NORMALMASS_BLOB, "normalmass solver drift")
    req(blob(RELAXED) == RELAXED_BLOB, "relaxed solver drift")

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
    req(cur["latest_main_native_research"] == "V44_BTVA_D8_FULL343_RECEIVER_STRUCTURAL_CLOSURE__ZERO_MAIN_CREDIT", "V44 routing drift")
    req(cur["mainbatch_stop_gate"] == "NONE", "unexpected MAIN stop gate")
    locks = state["source_locks"]
    req(locks["btva_d8_full343_retained"]["blob_sha1"] == FULL_BLOB, "full343 state lock")
    req(locks["btva_d8_all140_receiver_semantics"]["blob_sha1"] == ALL140_BLOB, "all140 state lock")
    req(locks["btva_d8_conic_exception"]["blob_sha1"] == CONIC_BLOB, "conic state lock")
    sw = locks["live_specialist_sweep"]
    req(sw["lane_178_pr"] == 1821 and sw["lane_178_head"] == "f263548c2968e8e14cfc14a80e5c779053e81724" and sw["lane_178_pending_main_handoff"] == "NONE", "178 live observation")
    req(sw["ex5_pr"] == 1818 and sw["ex5_head"] == "33f63a4c0bb3dde9d56efd895f4e8eb19d9217e2" and sw["ex5_pending_main_handoff"] == "NONE__CONSUMED_BY_V42", "EX5 observation")
    req(sw["mb_pr"] == 1819 and sw["mb_head"] == "5d113826cc36d2c0600ccad4795e7684f35879e5" and sw["mb_pending_main_handoff"] == "NONE", "MB observation")
    req(sw["bridge_pr"] == 1813 and sw["bridge_head"] == "aba66e35ad0c76205acbb99e9c3af5ce0bb00b42" and sw["bridge_runkey_generation"] == 0 and sw["bridge_runkey_armed"] is False and sw["bridge_pending_main_handoff"] == "NONE", "BRIDGE observation")
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
