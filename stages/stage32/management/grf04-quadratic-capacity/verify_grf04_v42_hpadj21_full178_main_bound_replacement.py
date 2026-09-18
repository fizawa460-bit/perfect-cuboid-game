#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
RECEIPT = HERE / "GRF04-V42-HPADJ21-FULL178-MAIN-BOUND-REPLACEMENT.json"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

PREDECESSOR_HEAD = "cbe4a7c2f45710ccd2b0c6da70fc89b9dc11c80e"
PREDECESSOR_STATE_BLOB = "c21ac0bfa1d91b6998499e67848dfaf28de85b49"
PREDECESSOR_STATE_CANON = "87a2d4657239648c0363a054e9d8066548b20870683b3e48d835e1032321a2d4"
REPOSITORY_MAIN = "37bb811b95399d73cc46fe899badcfa8eb5fca7d"
HANDOFF_HEAD = "33f63a4c0bb3dde9d56efd895f4e8eb19d9217e2"
HANDOFF_PATH = "stages/stage32-ex5/hpadj-21_ex5/MAIN-HANDOFF.json"
HANDOFF_BLOB = "c0a27ff6fdc78fba8e530d340bf4774be1f5341f"
HANDOFF_CANON = "b574fe4c48ac7f525063dfbcc7f9b43aeb0a40877a559e696159d16851ce6416"
HANDOFF_VERIFIER_PATH = "stages/stage32-ex5/hpadj-21_ex5/verify_main_handoff.py"
HANDOFF_VERIFIER_BLOB = "81023950899a7576f2b9313c738a1697219f764c"
AUDITED_HEAD = "265fbef0a67014494fcf773af6c3a9f1b095ef95"
AUDIT_REVIEW = 5242670540

BCHUNK_WORKER_PATH = "stages/stage32-ex5/hpadj-21_ex5/run_full_hist_bchunk.py"
BCHUNK_WORKER_BLOB = "76087962f8fc464a74ad60121f9522c6bf9b19cb"
ROW_WORKER_PATH = "stages/stage32-ex5/hpadj-21_ex5/run_full_hist_row.py"
ROW_WORKER_BLOB = "68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
EXECUTION_CONTRACT_PATH = "stages/stage32-ex5/hpadj-21_ex5/HEAVY-EXECUTION-CONTRACT.json"
EXECUTION_CONTRACT_BLOB = "871aaade9aaa85d24db362e094a8c1b5fc71ac6c"
ROW_ASSEMBLER_PATH = "stages/stage32-ex5/hpadj-21_ex5/assemble_full_hist_row_from_bchunks.py"
ROW_ASSEMBLER_BLOB = "82510e4e478e9145317e07c237ce08b8d189c306"
UNION_AGGREGATOR_PATH = "stages/stage32-ex5/hpadj-21_ex5/aggregate_full_hist_rows.py"
UNION_AGGREGATOR_BLOB = "a8b175e8a03356937957149088e0c003fa82eb4a"

HEAVY_RUN = 35279651998
HEAVY_ARTIFACT_ID = 10524680156
HEAVY_ARTIFACT_DIGEST = "af8cca787274c1d3db53e8586fd2b287cea8e74e19ecac1f02e8388173742e25"
HEAVY_AGGREGATE_CANON = "82d9dcd44eca1ead942ee300d0a66f2aaf895184482b308691a5544240877769"
ROW_STREAM = "f3da144730bd68d8dec7743e282e8dffb06229e5e6443fee7ea73fa9f0b33b1d"

OLD = 179119009547804181594
NEW = 157570677819451133507
TIGHTENING = 21548331728353048087
RECEIPT_BLOB = "3072d84981eaec239ba55a5e5e25a3481d37406b"
RECEIPT_CANON = "06be0bdf846364622af9c555e6f7e64be50b58c1d369d6db66c2f0b21d644831"
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
    receipt = lock_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON, "V42 replacement receipt")
    req(blob(REGISTRY) == REGISTRY_BLOB, "claim registry drift")
    req(blob(FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters drift")

    if args.ex5_handoff_root is not None:
        handoff = lock_json(args.ex5_handoff_root / HANDOFF_PATH, HANDOFF_BLOB, HANDOFF_CANON,
                            "EX5 HPADJ21 MAIN handoff")
        req(blob(args.ex5_handoff_root / HANDOFF_VERIFIER_PATH) == HANDOFF_VERIFIER_BLOB,
            "HPADJ21 handoff verifier blob drift")
        for path, expected, label in (
            (BCHUNK_WORKER_PATH, BCHUNK_WORKER_BLOB, "HPADJ21 b-chunk worker"),
            (ROW_WORKER_PATH, ROW_WORKER_BLOB, "HPADJ21 row worker"),
            (EXECUTION_CONTRACT_PATH, EXECUTION_CONTRACT_BLOB, "HPADJ21 execution contract"),
            (ROW_ASSEMBLER_PATH, ROW_ASSEMBLER_BLOB, "HPADJ21 row assembler"),
            (UNION_AGGREGATOR_PATH, UNION_AGGREGATOR_BLOB, "HPADJ21 union aggregator"),
        ):
            req(blob(args.ex5_audited_root / path) == expected, label + " drift")

        p = handoff["producer"]
        req(p["audited_exact_head"] == AUDITED_HEAD, "handoff audited head")
        req(p["hostile_audit_review_id"] == AUDIT_REVIEW and
            p["hostile_audit_verdict"] == "PASS", "handoff hostile audit")
        heavy = p["heavy_run"]
        req(heavy["run_id"] == HEAVY_RUN and heavy["conclusion"] == "success",
            "handoff heavy run")
        req(heavy["artifact_id"] == HEAVY_ARTIFACT_ID and
            heavy["artifact_digest_sha256"] == HEAVY_ARTIFACT_DIGEST,
            "handoff artifact identity")
        req(heavy["aggregate_canonical_sha256"] == HEAVY_AGGREGATE_CANON,
            "handoff aggregate canonical")
        req(heavy["row_certificate_stream_sha256"] == ROW_STREAM,
            "handoff row stream")
        req(heavy["full178_rows"] == 178 and
            heavy["row_gap_count"] == 0 and heavy["row_overlap_count"] == 0,
            "handoff FULL178 coverage")
        t = handoff["candidate_transition"]
        req(t["current_main_v41_upper_bound"] == OLD and
            t["hpadj21_candidate_upper_bound"] == NEW, "handoff candidate bounds")
        req(t["strict_improvement_vs_current_main_v41"] == TIGHTENING,
            "handoff tightening")
        req(t["same_hpadj20_pre_domain_population"] is True and
            t["same_hpadj20_post_mass_constraints"] is True and
            t["ordered_triple_population_preserved_exactly"] is True,
            "handoff population semantics")
        req(t["additive_subtraction_authorized"] is False,
            "handoff additive subtraction unexpectedly authorized")

    req(receipt["status"] ==
        "AUDITED_EX5_HPADJ21_HANDOFF_CONSUMED__REPLACEMENT_HEAD_PENDING_HOSTILE_REAUDIT",
        "receipt status")
    pred = receipt["predecessor_authority"]
    req(pred["exact_head"] == PREDECESSOR_HEAD, "predecessor head")
    req(pred["repository_main"] == REPOSITORY_MAIN, "predecessor repository main")
    req(pred["state_blob_sha1"] == PREDECESSOR_STATE_BLOB, "predecessor state blob")
    req(pred["state_canonical_sha256"] == PREDECESSOR_STATE_CANON,
        "predecessor state canonical")
    req(pred["authoritative_remaining_terminals"] == OLD, "predecessor authority")
    req(pred["v40_replacement_hostile_audit_status"] == "PASS",
        "V40 audit not synchronized")

    compat = receipt["target_compatibility"]
    req(compat["numeric_authority_unchanged_between_target_and_predecessor"] is True,
        "target/predecessor authority compatibility")
    req(compat["current_predecessor_only_adds_zero_credit_preflights_and_live_observation_sync"] is True,
        "predecessor semantic drift not bounded")

    src = receipt["consumed_handoff"]
    req(src["producer_pr"] == 1818 and src["post_audit_handoff_head"] == HANDOFF_HEAD,
        "producer handoff identity")
    req(src["handoff_blob_sha1"] == HANDOFF_BLOB and
        src["handoff_canonical_sha256"] == HANDOFF_CANON,
        "handoff source lock")
    req(src["audited_exact_head"] == AUDITED_HEAD and
        src["hostile_audit_review_id"] == AUDIT_REVIEW and
        src["hostile_audit_status"] == "PASS", "producer audit identity")
    req(src["candidate_upper_bound"] == NEW and
        src["candidate_tightening_vs_v41"] == TIGHTENING, "candidate arithmetic")
    req(src["full178_rows"] == 178 and src["row_gap_count"] == 0 and
        src["row_overlap_count"] == 0 and src["strict_cell_count"] == 796,
        "producer coverage/strict-cell identity")
    req(src["same_hpadj20_pre_domain_population"] is True and
        src["same_hpadj20_post_mass_constraints"] is True and
        src["ordered_triple_population_preserved_exactly"] is True,
        "same-population semantics")
    req(src["additive_subtraction_authorized"] is False,
        "source additive-subtraction firewall")

    repl = receipt["replacement"]
    req(repl["authority_version"] == "V42", "replacement version")
    req(repl["authoritative_remaining_strata"] == 17128, "replacement strata")
    req(repl["authoritative_remaining_terminals"] == NEW, "replacement authority")
    req(repl["tightening_vs_v41"] == TIGHTENING, "replacement tightening")
    req(repl["composition_rule"] ==
        "MIN_OF_CERTIFIED_UPPER_BOUNDS__HPADJ21_SAME_POPULATION_REFINEMENT__NO_ADDITIVE_STACKING",
        "replacement composition")
    req(repl["exact_incremental_rejected_identity_set_claimed"] is False,
        "identity-set overclaim")
    req(repl["additive_subtraction_performed"] is False and repl["double_charge"] is False,
        "additive/double-charge firewall")
    req(repl["full178_numerical_census_complete"] is False and repl["stage32_closed"] is False,
        "closure overclaim")

    cs = receipt["claim_sync"]
    req(cs["logical_claim_statement_changed"] is False, "claim statement changed")
    req(cs["claim_registry_mutated"] is False and
        cs["active_frontier_mutated"] is False and
        cs["lane_adapters_mutated"] is False, "claim DAG unexpectedly mutated")
    req(cs["claim_id"] == "S32.FULL178.NUMERICAL_CENSUS.V1" and
        cs["claim_status"] == "DECLARED_GOAL_ACTIVE_INCOMPLETE", "claim status")

    req(state["schema"] ==
        "STAGE32_MAIN_COMPACT_STATE_V42_HPADJ21_FULL178_BOUND_CONSUMED_REAUDIT_PENDING",
        "state schema")
    sync = state["authority_sync"]
    req(sync["predecessor_process_head"] == PREDECESSOR_HEAD, "state predecessor head")
    req(sync["hpadj21_full178_main_numeric_bound_replacement_consumed"] is True,
        "state consumption flag")
    req(sync["hpadj21_candidate_audited_exact_head"] == AUDITED_HEAD and
        sync["hpadj21_candidate_hostile_audit_review_id"] == AUDIT_REVIEW and
        sync["hpadj21_candidate_hostile_audit_status"] == "PASS",
        "state producer audit")
    req(sync["hpadj21_consumption_rule"] ==
        "MIN_OF_CERTIFIED_UPPER_BOUNDS__HPADJ21_SAME_POPULATION_REFINEMENT__NO_ADDITIVE_STACKING",
        "state composition")

    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN strata authority")
    req(f["predecessor_v41_authoritative_remaining_terminals"] == OLD,
        "V41 predecessor bound")
    req(f["authoritative_remaining_terminals"] == NEW, "V42 bound")
    req(f["v42_hpadj21_certified_numeric_bound_tightening_vs_v41"] == TIGHTENING,
        "V42 tightening")
    req(f["live_ex5_hpadj21_main_credit_consumed"] is True,
        "EX5 handoff not consumed")
    req(f["full178_numerical_census_complete"] is False and
        f["stage32_closed"] is False, "FULL178/closure firewall")

    req(state["current"]["mainbatch_stop_gate"] ==
        "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED", "replacement hostile-reaudit gate")
    req(state["current"]["next_exact_route"] ==
        "HOSTILE_AUDIT_V42_HPADJ21_FULL178_BOUND_REPLACEMENT", "next exact route")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True,
        "replacement audit firewall")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete",
                "merge_authorized", "perfect_cuboid_existence_claim",
                "perfect_cuboid_nonexistence_claim", "receiver_credit", "route_credit",
                "stage32_closed", "theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall {key}")

    req(OLD - NEW == TIGHTENING, "authority arithmetic")
    print("PASS: Stage32 V42 consumes hostile-audited EX5 HPADJ21 by non-additive same-population bound replacement")
    if args.ex5_handoff_root is not None:
        print("PASS: exact HPADJ21 handoff and audited producer source locks replayed")
    else:
        print("PASS: local projection verified; external EX5 source replay delegated to exact-head CI/audit")
    print("PASS: numerical authority is 157570677819451133507; replacement head awaits independent hostile reaudit")
    print("PASS: FULL178 census and downstream theorem/effectivity/receiver/endpoint credit remain incomplete")


if __name__ == "__main__":
    main()
