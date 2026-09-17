#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHECKPOINT = HERE / "FULL178-CHECKPOINT.json"
HANDOFF = HERE / "MAIN-HANDOFF-PREFLIGHT.json"

CHECKPOINT_BLOB = "2161c2dedf94fa2124231453dd56e4047ebd8707"
CHECKPOINT_CANON = "f92ccd5296ef9f5ee041baac44cd4933662d9413ea17b4ca1f59a18bf219a961"
HANDOFF_BLOB = "b8b7dacad95d5b0cfbebbf908d7adfbb78385ef1"
HANDOFF_CANON = "ff2b20f5e654f45b367a46e893529982014b04215641d1321d57a174d037fae2"
COMPUTE_HEAD = "d4bb013da65a91545dfd9833c278dafb27618b00"
HEAVY_RUN = 35279651998
ARTIFACT_ID = 10524680156
ARTIFACT_DIGEST = "af8cca787274c1d3db53e8586fd2b287cea8e74e19ecac1f02e8388173742e25"
AGG_CANON = "82d9dcd44eca1ead942ee300d0a66f2aaf895184482b308691a5544240877769"
ROW_STREAM = "f3da144730bd68d8dec7743e282e8dffb06229e5e6443fee7ea73fa9f0b33b1d"
OLD = 179119009547804181594
NEW = 157570677819451133507
IMPROVEMENT = 21548331728353048087
STRICT_CELLS = 796

MAIN_HEAD = "37bb811b95399d73cc46fe899badcfa8eb5fca7d"
MAIN_STATE_PATH = "stages/stage32/MAIN-STATE.json"
MAIN_STATE_BLOB = "dd7dba27eb062e6a6ad4d440094ba26c290900d7"
MAIN_STATE_CANON = "b9886a12fc479acae53de4bdff84ee452a208dfb641eec3ea199ee876cb6898c"
V41_PATH = "stages/stage32/management/grf04-quadratic-capacity/GRF04-V41-HPADJ20-FULL178-AUDIT-SYNC.json"
V41_BLOB = "ee6639e2b4a4ad5dd48e964d6a6b055f551e7bd1"
V41_CANON = "ac52c7d4598eba4ef165bed05c5ff12931777052a2b8582c65286ff8067400c7"
PREFLIGHT_PATH = "stages/stage32/management/grf04-quadratic-capacity/HPADJ20-FULL-QA-HISTOGRAM-MAIN-PARALLEL-PREFLIGHT.json"
PREFLIGHT_BLOB = "0eb5672dea0712cbf5044d5376e60fe233e767c3"
PREFLIGHT_CANON = "0191c14b3fc072a762d1b702408746691cd5fe315ce9f4a0a040b75183bd13a8"


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


def lock_source(root: Path, spec: dict, label: str) -> None:
    path = root / spec["path"]
    req(path.is_file(), f"missing source {label}")
    req(blob(path) == spec["blob_sha1"], f"source blob drift: {label}")


def verify_local() -> tuple[dict, dict]:
    checkpoint = lock_json(CHECKPOINT, CHECKPOINT_BLOB, CHECKPOINT_CANON, "HPADJ21 FULL178 checkpoint")
    handoff = lock_json(HANDOFF, HANDOFF_BLOB, HANDOFF_CANON, "HPADJ21 MAIN handoff preflight")

    req(checkpoint["schema"] == "STAGE32EX5_HPADJ21_FULL178_CHECKPOINT_V1", "checkpoint schema")
    req(checkpoint["status"] == "EXACT_FULL178_FULL_QA_HISTOGRAM_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
        "checkpoint status")
    req(checkpoint["route_id"] == "HPADJ-21_ex5", "checkpoint route")

    for label, spec in checkpoint["source_locks"].items():
        lock_source(ROOT, spec, label)

    comp = checkpoint["computation_boundary"]
    req(comp["pr"] == 1818 and comp["exact_head"] == COMPUTE_HEAD, "computation boundary")
    req(comp["run_id"] == HEAVY_RUN and comp["run_conclusion"] == "success", "heavy run")
    req(comp["artifact_id"] == ARTIFACT_ID and comp["artifact_digest_sha256"] == ARTIFACT_DIGEST,
        "artifact identity")
    req(comp["aggregate_canonical_sha256"] == AGG_CANON, "aggregate canonical")

    cov = checkpoint["coverage"]
    req(cov["expected_rows"] == cov["received_rows"] == 178, "FULL178 row coverage")
    req(cov["row_gaps"] == 0 and cov["row_overlaps"] == 0, "row partition gap/overlap")
    req(cov["row_certificate_stream_sha256"] == ROW_STREAM, "row certificate stream")
    req(cov["carried_complete_rows"] == 173 and cov["computed_rows"] == 5 and cov["computed_b_chunks"] == 57,
        "resume composition")

    totals = checkpoint["totals"]
    req(totals["hpadj20_cellwise_floor_sum"] == OLD, "HPADJ20 replay total")
    req(totals["hpadj21_cellwise_floor_sum"] == NEW, "HPADJ21 total")
    req(totals["improvement_vs_hpadj20"] == IMPROVEMENT, "improvement total")
    req(OLD - NEW == IMPROVEMENT, "replacement arithmetic")
    req(totals["strict_cell_count"] == STRICT_CELLS, "strict-cell count")

    sem = checkpoint["semantics"]
    req(sem["same_population_as_hpadj20"] is True and
        sem["same_post_mass_constraints_as_hpadj20"] is True and
        sem["full_qA_histogram_exact_multiplicity"] is True,
        "same-population refinement semantics")
    req(sem["composition_rule"] == "DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION",
        "composition rule")
    req(sem["exact_incremental_rejected_identity_set_available"] is False and
        sem["statistical_independence_assumed"] is False and
        sem["additive_subtraction_used"] is False,
        "composition firewalls")

    req(handoff["schema"] == "STAGE32EX5_HPADJ21_FULL178_MAIN_HANDOFF_PREFLIGHT_V1", "handoff schema")
    req(handoff["status"] == "HOSTILE_AUDIT_REQUIRED_BEFORE_MAIN_CONSUMPTION__ZERO_MAIN_CREDIT",
        "handoff status")
    prod = handoff["producer"]
    req(prod["pr"] == 1818 and prod["computation_exact_head"] == COMPUTE_HEAD, "handoff producer")
    req(prod["hostile_audit_status"] == "PENDING_REQUIRED" and prod["hostile_audit_review_id"] is None,
        "handoff must remain pre-audit")
    req(prod["checkpoint"]["blob_sha1"] == CHECKPOINT_BLOB and
        prod["checkpoint"]["canonical_sha256"] == CHECKPOINT_CANON,
        "handoff checkpoint identity")

    tr = handoff["candidate_transition"]
    req(tr["current_main_v41_upper_bound"] == OLD and tr["hpadj21_candidate_upper_bound"] == NEW,
        "candidate bounds")
    req(tr["strict_improvement_vs_current_main_v41"] == IMPROVEMENT and
        tr["strict_cell_count"] == STRICT_CELLS, "candidate improvement")
    req(tr["producer_full178_row_coverage_complete"] is True and
        tr["stage32_full178_numerical_census_complete"] is False,
        "row coverage vs Stage32 FULL178 claim")
    req(tr["remaining_strata_if_consumed_as_valid_replacement"] == 17128, "strata")
    req(tr["composition_rule"] == "DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION",
        "handoff composition")
    req(tr["additive_subtraction_authorized"] is False and
        tr["ex5_main_authority_mutation_performed"] is False,
        "handoff authority firewall")

    cp = handoff["consumer_preconditions"]
    req(cp["independent_hpadj21_hostile_audit_pass_required"] is True, "producer audit requirement")
    req(cp["main_replacement_transition_requires_its_own_hostile_audit"] is True,
        "MAIN replacement audit requirement")
    req(cp["consumer_must_not_additively_subtract_hpadj21_improvement"] is True,
        "no additive subtraction precondition")

    for key, value in handoff["firewalls"].items():
        if key == "hostile_audit_pass_claimed":
            req(value is False, "hostile audit overclaim")
        elif key in {"stage32_main_pruning_credit", "current_main_incremental_credit", "main_consumption_performed",
                     "exact_incremental_rejected_identity_set_claimed", "full178_complete", "effectivity_credit",
                     "receiver_credit", "route_credit", "theorem_credit", "endpoint_credit", "stage32_closed",
                     "perfect_cuboid_credit", "merge_authorized"}:
            req(value is False, f"firewall {key}")

    return checkpoint, handoff


def verify_main(main_root: Path, handoff: dict) -> None:
    state = lock_json(main_root / MAIN_STATE_PATH, MAIN_STATE_BLOB, MAIN_STATE_CANON, "Stage32 MAIN V41 state")
    receipt = lock_json(main_root / V41_PATH, V41_BLOB, V41_CANON, "Stage32 MAIN V41 audit sync")
    preflight = lock_json(main_root / PREFLIGHT_PATH, PREFLIGHT_BLOB, PREFLIGHT_CANON,
                          "MAIN full-qA structural preflight")

    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V41_HPADJ20_FULL178_BOUND_AUDIT_SYNCED",
        "MAIN V41 schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN strata")
    req(f["authoritative_remaining_terminals"] == OLD, "MAIN current bound")
    req(f["v40_hpadj20_bound_consumed"] is True and f["v40_replacement_head_hostile_audited"] is True,
        "MAIN HPADJ20 audit-synced authority")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,
        "MAIN closure firewall")

    req(receipt["status"] == "V40_REPLACEMENT_HOSTILE_AUDIT_PASS_SYNCED__ZERO_NEW_PRUNING",
        "V41 receipt status")
    req(receipt["hostile_audit"]["status"] == "PASS", "V40 hostile audit not synced")
    req(receipt["sync"]["authoritative_remaining_terminals"] == OLD and
        receipt["sync"]["numeric_authority_changed"] is False,
        "V41 numeric authority")

    req(preflight["status"] == "STRUCTURAL_DOMINANCE_PREFLIGHT__NUMERICAL_REPLAY_NOT_RUN__ZERO_MAIN_CREDIT",
        "MAIN full-qA preflight status")
    req(preflight["structural_dominance"]["full_histogram_cell_objective_no_larger_than_hpadj20"] is True,
        "MAIN full-qA dominance preflight")

    target = handoff["target_main"]
    req(target["observed_repository_main"] == MAIN_HEAD, "target MAIN exact head")
    req(target["main_state_blob_sha1"] == MAIN_STATE_BLOB and
        target["main_state_canonical_sha256"] == MAIN_STATE_CANON,
        "target MAIN state identity")
    req(target["v41_audit_sync_receipt_blob_sha1"] == V41_BLOB and
        target["v41_audit_sync_receipt_canonical_sha256"] == V41_CANON,
        "target V41 receipt identity")
    req(target["existing_full_qA_preflight_blob_sha1"] == PREFLIGHT_BLOB and
        target["existing_full_qA_preflight_canonical_sha256"] == PREFLIGHT_CANON,
        "target full-qA preflight identity")
    req(target["authoritative_remaining_terminal_upper_bound"] == OLD and
        target["authoritative_remaining_strata"] == 17128,
        "target MAIN authority")
    req(target["recommended_consumption_rule_after_producer_audit"] ==
        "MIN_OF_CERTIFIED_UPPER_BOUNDS__HPADJ21_SAME_POPULATION_REFINEMENT__NO_ADDITIVE_STACKING",
        "target consumption rule")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--main-root", type=Path)
    args = ap.parse_args()
    _, handoff = verify_local()
    print("PASS: HPADJ21 compact FULL178 checkpoint source-locks exact heavy evidence")
    print("PASS: HPADJ21 157570677819451133507 strictly refines audited MAIN V41 HPADJ20 bound by 21548331728353048087")
    print("PASS: pre-audit handoff remains zero-credit and non-additive")
    if args.main_root is not None:
        verify_main(args.main_root, handoff)
        print("PASS: handoff preflight targets exact Stage32 MAIN V41 audited HPADJ20 authority")
    else:
        print("PASS: MAIN target replay not requested; exact V41 replay is required in CI/audit before promotion")


if __name__ == "__main__":
    main()
