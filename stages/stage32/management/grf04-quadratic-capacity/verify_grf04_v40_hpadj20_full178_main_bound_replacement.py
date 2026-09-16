#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
RECEIPT = HERE / "GRF04-V40-HPADJ20-FULL178-MAIN-BOUND-REPLACEMENT.json"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

PREDECESSOR_HEAD = "2543fe4732c1409e013bf02d8c5802f85057ccbd"
PREDECESSOR_STATE_BLOB = "187e34e2be989c7de674d2f5448e9dcebf0820c9"
PREDECESSOR_STATE_CANON = "660c8e07093af9885372a53da35dbdfb7396a306afc09e2ffafaa9b8257fb179"
HANDOFF_PATH = "stages/stage32-ex5/hpadj-20_ex5/MAIN-HANDOFF.json"
HANDOFF_BLOB = "52ca73eeb52b7d930f905c42a85b62f044bda269"
HANDOFF_CANON = "826966a95f22c2235258c6499c9bc9c03b2521687d71dbf99d9728eaaaa6d3f5"
AUDITED_HEAD = "4140e5eb2ebee0c32b22ec78fd531ab35fb7c3ff"
AUDIT_REVIEW = 5228477451
PRODUCER_PATH = "stages/stage32-ex5/hpadj-20_ex5/derive_two_tier_qa_predomain_picard_lp_bound.py"
PRODUCER_BLOB = "837d647cfcbc96bbe384e564f449cd7042a46d48"
ROW_WORKER_PATH = "stages/stage32-ex5/hpadj-20_ex5/run_row_shard.py"
ROW_WORKER_BLOB = "380c191b7dd3bcc6c1e290495c776203d4a92b63"
AGGREGATOR_PATH = "stages/stage32-ex5/hpadj-20_ex5/aggregate_row_shards.py"
AGGREGATOR_BLOB = "cfa58039f9cce06767a18b7594782dc620865e51"
HEAVY_RUN = 35077283028
HEAVY_ARTIFACT_ID = 10456339298
HEAVY_ARTIFACT_DIGEST = "4083552fbe016f25bbb6b53a06e9abd6bef9f8fea63693032107919f3f03c8dd"
HEAVY_UNION_CANON = "801999649a71700c369f0c2a32da9f7603b86e077212d3a4865ffbf1773822e7"
OLD = 195414091250828468192
NEW = 179119009547804181594
TIGHTENING = 16295081703024286598
RECEIPT_BLOB = "f9d984f64d2c428481e082be622848e33407baf1"
RECEIPT_CANON = "f330348d1d6aee5417df20e119479c3c2b6b045a2ce96f7d6e4e54ac9a88d53d"
REGISTRY_BLOB = "f3a884adc1c82aace81cb73d049ff14720ace862"
FRONTIER_BLOB = "4c251be4aa5c355481fe3bcfc71c292fb6389ba4"
ADAPTERS_BLOB = "c0ef34e5838e27046a20fed77063593009c56f40"

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def lock_json(path: Path, expected_blob: str, expected_canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(blob(path) == expected_blob, f"{label} blob drift")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == expected_canon,
        f"{label} stored canonical drift")
    req(canon(obj) == expected_canon, f"{label} canonical drift")
    return obj

def current_state() -> dict:
    req(STATE.is_file(), "missing current MAIN state")
    obj = json.loads(STATE.read_text(encoding="utf-8"))
    stored = obj.get("canonical_sha256_without_this_field")
    req(isinstance(stored, str) and canon(obj) == stored, "current MAIN state canonical drift")
    return obj

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ex5-handoff-root", type=Path)
    ap.add_argument("--ex5-audited-root", type=Path)
    args = ap.parse_args()
    req((args.ex5_handoff_root is None) == (args.ex5_audited_root is None),
        "ex5-handoff-root and ex5-audited-root must be supplied together")

    state = current_state()
    receipt = lock_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON, "V40 replacement receipt")
    req(blob(REGISTRY) == REGISTRY_BLOB, "claim registry drift")
    req(blob(FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters drift")

    if args.ex5_handoff_root is not None:
        handoff = lock_json(args.ex5_handoff_root / HANDOFF_PATH, HANDOFF_BLOB, HANDOFF_CANON,
                            "EX5 HPADJ20 MAIN handoff")
        req(blob(args.ex5_audited_root / PRODUCER_PATH) == PRODUCER_BLOB,
            "HPADJ20 producer blob drift")
        req(blob(args.ex5_audited_root / ROW_WORKER_PATH) == ROW_WORKER_BLOB,
            "HPADJ20 row-worker blob drift")
        req(blob(args.ex5_audited_root / AGGREGATOR_PATH) == AGGREGATOR_BLOB,
            "HPADJ20 aggregator blob drift")
        prod = handoff["producer"]
        req(prod["audited_exact_head"] == AUDITED_HEAD, "handoff audited head")
        req(prod["hostile_audit_review_id"] == AUDIT_REVIEW and
            prod["hostile_audit_verdict"] == "PASS", "handoff hostile audit")
        heavy = prod["heavy_run"]
        req(heavy["run_id"] == HEAVY_RUN and heavy["conclusion"] == "success",
            "handoff heavy run")
        req(heavy["artifact_id"] == HEAVY_ARTIFACT_ID and
            heavy["artifact_digest_sha256"] == HEAVY_ARTIFACT_DIGEST,
            "handoff artifact identity")
        req(heavy["union_canonical_sha256"] == HEAVY_UNION_CANON, "handoff union canonical")
        req(handoff["candidate_transition"]["hpadj20_candidate_upper_bound"] == NEW,
            "handoff candidate upper")
        req(handoff["candidate_transition"]["strict_improvement_vs_observed_current_main"] == TIGHTENING,
            "handoff tightening")
        req(handoff["candidate_transition"]["same_hpadj08_td01_x4_complete_population"] is True,
            "handoff population identity")
        req(handoff["candidate_transition"]["ordered_triple_population_preserved_exactly"] is True,
            "handoff ordered-triple population")
        req(handoff["candidate_transition"]["additive_subtraction_authorized"] is False,
            "handoff additive subtraction unexpectedly authorized")

    req(receipt["status"] ==
        "AUDITED_EX5_HPADJ20_HANDOFF_CONSUMED__REPLACEMENT_HEAD_PENDING_HOSTILE_REAUDIT",
        "receipt status")
    pred = receipt["predecessor_authority"]
    req(pred["version"] == "V39_FULL178_INTEGER_LATTICE_BOUND_AUDIT_SYNCED",
        "predecessor version")
    req(pred["exact_head"] == PREDECESSOR_HEAD, "predecessor head")
    req(pred["state_blob_sha1"] == PREDECESSOR_STATE_BLOB, "predecessor state blob")
    req(pred["state_canonical_sha256"] == PREDECESSOR_STATE_CANON,
        "predecessor state canonical")
    req(pred["authoritative_remaining_terminals"] == OLD, "predecessor authority")

    src = receipt["consumed_handoff"]
    req(src["producer_pr"] == 1814 and src["handoff_blob_sha1"] == HANDOFF_BLOB,
        "producer handoff identity")
    req(src["handoff_canonical_sha256"] == HANDOFF_CANON, "handoff canonical")
    req(src["audited_exact_head"] == AUDITED_HEAD and
        src["hostile_audit_review_id"] == AUDIT_REVIEW and
        src["hostile_audit_status"] == "PASS", "producer audit identity")
    req(src["heavy_run_id"] == HEAVY_RUN and src["heavy_run_conclusion"] == "SUCCESS",
        "heavy run identity")
    req(src["heavy_artifact_id"] == HEAVY_ARTIFACT_ID and
        src["heavy_artifact_digest_sha256"] == HEAVY_ARTIFACT_DIGEST and
        src["heavy_union_canonical_sha256"] == HEAVY_UNION_CANON,
        "heavy artifact source lock")
    req(src["candidate_upper_bound"] == NEW and
        src["candidate_tightening_vs_v39"] == TIGHTENING, "candidate arithmetic")
    req(src["same_hpadj08_td01_x4_complete_population"] is True and
        src["ordered_triple_population_preserved_exactly"] is True,
        "same-population semantics")
    req(src["additive_subtraction_authorized"] is False, "additive subtraction source firewall")

    repl = receipt["replacement"]
    req(repl["authority_version"] == "V40", "replacement version")
    req(repl["authoritative_remaining_strata"] == 17128, "replacement strata")
    req(repl["authoritative_remaining_terminals"] == NEW, "replacement authority")
    req(repl["tightening_vs_v39"] == TIGHTENING, "replacement tightening")
    req(repl["composition_rule"] ==
        "MIN_OF_CERTIFIED_UPPER_BOUNDS__HPADJ20_SAME_POPULATION_REFINEMENT__NO_ADDITIVE_STACKING",
        "replacement composition")
    req(repl["exact_incremental_rejected_identity_set_claimed"] is False,
        "identity-set overclaim")
    req(repl["additive_subtraction_performed"] is False and repl["double_charge"] is False,
        "additive/double-charge firewall")
    req(repl["full178_numerical_census_complete"] is False and repl["stage32_closed"] is False,
        "closure overclaim")

    cs = receipt["claim_sync"]
    req(cs["logical_claim_statement_changed"] is False, "claim statement changed")
    req(cs["claim_registry_mutated"] is False and cs["active_frontier_mutated"] is False and
        cs["lane_adapters_mutated"] is False, "claim DAG unexpectedly mutated")
    req(cs["claim_id"] == "S32.FULL178.NUMERICAL_CENSUS.V1" and
        cs["claim_status"] == "DECLARED_GOAL_ACTIVE_INCOMPLETE", "claim status")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V40_HPADJ20_FULL178_BOUND_CONSUMED_REAUDIT_PENDING",
        "state schema")
    sync = state["authority_sync"]
    req(sync["predecessor_process_head"] == PREDECESSOR_HEAD, "state predecessor head")
    req(sync["hpadj20_full178_main_numeric_bound_replacement_consumed"] is True,
        "state consumption flag")
    req(sync["hpadj20_candidate_audited_exact_head"] == AUDITED_HEAD and
        sync["hpadj20_candidate_hostile_audit_review_id"] == AUDIT_REVIEW and
        sync["hpadj20_candidate_hostile_audit_status"] == "PASS", "state producer audit")

    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN strata authority")
    req(f["predecessor_v39_authoritative_remaining_terminals"] == OLD, "V39 bound")
    req(f["authoritative_remaining_terminals"] == NEW, "V40 bound")
    req(f["v40_hpadj20_certified_numeric_bound_tightening_vs_v39"] == TIGHTENING,
        "V40 tightening")
    req(f["live_ex5_hpadj20_main_credit_consumed"] is True, "EX5 handoff not consumed")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,
        "FULL178/closure firewall")

    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED",
        "replacement hostile-reaudit gate")
    req(state["current"]["next_exact_route"] == "HOSTILE_AUDIT_V40_HPADJ20_FULL178_BOUND_REPLACEMENT",
        "next exact route")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True,
        "replacement audit firewall")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete",
                "merge_authorized", "perfect_cuboid_existence_claim",
                "perfect_cuboid_nonexistence_claim", "receiver_credit", "route_credit",
                "stage32_closed", "theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall {key}")

    req(OLD - NEW == TIGHTENING, "authority arithmetic")
    print("PASS: Stage32 V40 consumes hostile-audited EX5 HPADJ20 by non-additive certified-bound replacement")
    if args.ex5_handoff_root is not None:
        print("PASS: exact EX5 handoff and audited producer source locks replayed")
    else:
        print("PASS: local projection verified; external EX5 source replay delegated to exact-head CI/audit")
    print("PASS: replacement head is fail-closed pending hostile reaudit; FULL178 and downstream credit remain incomplete")

if __name__ == "__main__":
    main()
