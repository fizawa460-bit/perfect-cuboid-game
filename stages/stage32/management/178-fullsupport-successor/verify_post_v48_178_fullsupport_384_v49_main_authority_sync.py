#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

RECEIPT = HERE / "POST-V48-178-FULLSUPPORT-384-V49-MAIN-AUTHORITY-SYNC.json"
RECEIPT_BLOB = "5fa510fb9878211e04f534ffc9dcdfed765dd4bc"
RECEIPT_CANON = "f4c713421a5ea3e085392e9df93fd89ccde3974f7accb2f418c73dcbfdf789c1"

STATE = ROOT / "stages/stage32/MAIN-STATE.json"
V48 = ROOT / "stages/stage32/management/178-support-qbc/V48-178-SUPPORT-QBC-AUTHORITY-SYNC.json"
V48_BLOB = "2733e5519629e6365558bc1b4bfbc6305e0b5533"
V48_CANON = "d106029369dd5a029cd7a56e1c7d80fdd29f8471454fd2ed6c638af2b70288b1"

ACTIVE = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ACTIVE_BLOB = "2515c3591f9ccf88474b7cfdf6f9c7bf54ec8798"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
REGISTRY_BLOB = "862e12ddf95e02c5d4907adba76e73e99400cd92"
ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"
ADAPTERS_BLOB = "2ca34942569532d5ba448e978aa280e85420025f"
AUDITED_STATE_VERIFIER_SNAPSHOT = ROOT / "stages/stage32/proof/historical-routing-blobs/VERIFY-V49-MAIN-AUTHORITY-SYNC-PRE-ROUTING-CLEANUP.py"
AUDITED_STATE_VERIFIER_BLOB = "729cbb13410a4efcbeab2b08007208bcfb92e040"

HANDOFF_HEAD = "44d274770de1d092022ebbefff80f3cefb914982"
HANDOFF_PACKET_REL = Path("stages/stage32/management/178-fullsupport-successor/POST-V48-178-FULLSUPPORT-384-CURRENT-MAIN-TRANSPLANT.json")
HANDOFF_PACKET_BLOB = "e643a8a4e3c233817469f3e1c7dc9e60c41bea05"
HANDOFF_PACKET_CANON = "b80dd49ce146f37a91974e4081c29cd6754d3e68b2dc0c4912650cf4afee2392"
HANDOFF_VERIFIER_REL = Path("stages/stage32/management/178-fullsupport-successor/verify_post_v48_178_fullsupport_384_current_main_transplant.py")
HANDOFF_VERIFIER_BLOB = "de43524403d2616980f06af7d30fefb9323e7467"

PRODUCER_HEAD = "adcb7eb2eef153a1207294e956bf6115794e564d"
SOURCE_HANDOFF_REL = Path("stages/stage32/management/178-fullsupport-successor/POST-V48-178-FULLSUPPORT-384-MAIN-HANDOFF-PREFLIGHT.json")
SOURCE_HANDOFF_BLOB = "3667b2395f50b675f6f8286074e20e0212933e2f"
SOURCE_HANDOFF_CANON = "f52f6e74f3ab20c9d5c8a831351da7035af9cccea50893560f4307de5dab9e76"
SOURCE_HANDOFF_VERIFIER_REL = Path("stages/stage32/management/178-fullsupport-successor/verify_post_v48_178_fullsupport_384_main_handoff_preflight.py")
SOURCE_HANDOFF_VERIFIER_BLOB = "484dac8d43fc90357e08d033d2e93835fcad4c2e"
CANDIDATE_REL = Path("stages/stage32/32-01-178/fibration-nef/V48-FULL-SUPPORT-384-EQUIV-DERIVED-BOUND-RETAINED.json")
CANDIDATE_BLOB = "3acb9551db9fda6be8fde0194b23ddb41ca634d0"
CANDIDATE_CANON = "da7eb532daf2b775a49524fe45e5b7bf7851719f19a6926a227f5fa745258aba"
CANDIDATE_VERIFIER_REL = Path("stages/stage32/32-01-178/fibration-nef/verify_v48_full_support_384_equiv_derived_bound_retained.py")
CANDIDATE_VERIFIER_BLOB = "843d348351a05be083f2d0d6e16b08da45e38040"

OLD = 128470212118313474449
COVERED = 37911631052805557219
REPLACEMENT = 37884640022451662730
TIGHT = 26991030353894489
NEW = 128443221087959579960
AUDIT_REVIEW = 5313265646

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def load_locked(path: Path, expected_blob: str, expected_canon: str | None, label: str) -> dict:
    req(path.is_file(), "missing " + label)
    req(blob(path) == expected_blob, label + " blob drift")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon, label + " stored canonical drift")
        req(canon(obj) == expected_canon, label + " canonical drift")
    return obj

def git_head(root: Path) -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, check=True, text=True, stdout=subprocess.PIPE
    ).stdout.strip()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--handoff-root", type=Path)
    ap.add_argument("--producer-root", type=Path)
    args = ap.parse_args()

    rec = load_locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON, "V49 authority-sync receipt")
    req(rec["status"] == "HOSTILE_AUDITED_178_POST_V48_FULLSUPPORT_384_CONSUMED_AS_SAME_POPULATION_PER_COORDINATE_BOUND_REPLACEMENT", "receipt status")
    src = rec["source"]
    req(src["compact_handoff_audited_exact_head"] == HANDOFF_HEAD, "audited handoff head")
    req(src["specialist_producer_exact_head"] == PRODUCER_HEAD, "producer head")
    req(src["hostile_audit_status"] == "PASS" and src["hostile_audit_review_id"] == AUDIT_REVIEW, "audit binding")
    req(src["compact_handoff_blob_sha1"] == HANDOFF_PACKET_BLOB, "handoff packet lock")
    req(src["compact_handoff_verifier_blob_sha1"] == HANDOFF_VERIFIER_BLOB, "handoff verifier lock")
    req(src["source_candidate_blob_sha1"] == CANDIDATE_BLOB, "candidate lock")

    ci = rec["exact_head_ci"]
    req(ci["all_required_stage32_checks_success"] is True, "exact-head CI status")
    req(ci["compact_handoff_run_id"] == 36093376905, "compact handoff run id")
    req(ci["main_startup_run_id"] == 36093376891, "MAIN startup run id")
    req(ci["claim_frontier_run_id"] == 36093376879, "claim frontier run id")
    req(ci["stale_run_sweeper_run_id"] == 36093376910, "stale sweeper run id")

    a = rec["authority"]
    req(int(a["predecessor_v48_upper_bound"]) == OLD, "old bound")
    req(int(a["covered_v48_384_upper_bound_sum"]) == COVERED, "covered bound")
    req(int(a["replacement_384_upper_bound_sum"]) == REPLACEMENT, "replacement bound")
    req(int(a["exact_tightening_vs_v48"]) == TIGHT, "tightening")
    req(int(a["v49_same_population_replacement_upper_bound"]) == NEW, "new bound")
    req(OLD - COVERED + REPLACEMENT == NEW and OLD - NEW == TIGHT, "replacement arithmetic")
    req(a["replacement_formula"] == "V48_total - covered_V48_384 + replacement_384", "replacement formula")
    req(a["composition_rule"] == "SAME_POPULATION_PER_COORDINATE_MIN_UPPER_BOUND_REPLACEMENT__NO_ADDITIVE_SUBTRACTION", "composition")
    req(a["additive_subtraction"] is False and a["statistical_independence"] is False, "nonadditive/nonindependent")
    req(a["exact_rejected_identity_set_claimed"] is False and a["no_double_charge"] is True, "identity/no-double-charge")

    v48 = load_locked(V48, V48_BLOB, V48_CANON, "V48 authority receipt")
    req(int(v48["authority"]["v48_same_population_replacement_upper_bound"]) == OLD, "V48 predecessor authority")

    for path, expected, label in (
        (ACTIVE, ACTIVE_BLOB, "active frontier"),
        (REGISTRY, REGISTRY_BLOB, "claim registry"),
        (ADAPTERS, ADAPTERS_BLOB, "lane adapters"),
    ):
        req(path.is_file() and blob(path) == expected, label + " drift")

    active = json.loads(ACTIVE.read_text(encoding="utf-8"))
    by = {x["claim_id"]: x for x in active["claims"]}
    req(by["S32.FULL178.NUMERICAL_CENSUS.V2"]["authority_status"] == "AUDITED", "numerical claim authority")
    req(by["S32.GOAL.STAGE32_CLOSURE.V2"]["frontier_status"] == "BLOCKED_OPEN_GOAL", "closure remains open")

    cs = rec["claim_sync"]
    req(cs["transition_class"] == "AUTHORITY_METADATA_ONLY__EXISTING_NUMERICAL_CENSUS_CLAIM_CORE_UNCHANGED", "claim-sync class")
    req(cs["claim_registry_mutation_required"] is False, "claim registry mutation firewall")
    req(cs["active_frontier_mutation_required"] is False, "active frontier mutation firewall")
    req(cs["lane_adapter_mutation_required"] is False, "lane adapter mutation firewall")

    st = json.loads(STATE.read_text(encoding="utf-8"))
    expected_state_canon = canon(st)
    req(st.get("canonical_sha256_without_this_field") == expected_state_canon,
        "MAIN state canonical; expected=" + expected_state_canon)
    req(st["schema"] == "STAGE32_MAIN_COMPACT_STATE_V49_POST_V48_178_FULLSUPPORT_384_AUDIT_SYNCED", "MAIN schema")
    f = st["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "remaining strata")
    req(f["authoritative_remaining_terminals"] == NEW, "MAIN V49 authority")
    req(f["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "authority semantics")
    req(f["v49_predecessor_upper_bound"] == OLD, "V49 predecessor")
    req(f["v49_covered_v48_384_upper_bound_sum"] == COVERED, "V49 covered sum")
    req(f["v49_replacement_384_upper_bound_sum"] == REPLACEMENT, "V49 replacement sum")
    req(f["v49_exact_tightening_vs_v48"] == TIGHT, "V49 tightening")
    req(f["v49_178_fullsupport_384_main_numeric_bound_replacement_consumed"] is True, "V49 consumption")
    req(f["v49_additive_subtraction_performed"] is False, "V49 additive firewall")
    req(f["v49_exact_incremental_rejected_identity_set_claimed"] is False, "V49 identity firewall")

    cur = st["current"]
    req(cur["latest_main_native_research"] == "V49_POST_V48_178_FULLSUPPORT_384_AUTHORITY_SYNC", "latest MAIN research")
    req(cur["next_exact_route"] == "ROADMAP_32_02_AND_32_03_THEN_32_04_SYNTHESIS", "next route")
    req(cur["operator_entrypoint"] == "stage32mainbatch", "operator entrypoint")
    req(cur["routing_mode"] == "ROADMAP_FIRST_ON_DEMAND_SPECIALIST_DISPATCH", "routing mode")
    req(st["authority_sync"]["current_repository_main"] == "a834864923086e5f7c1647e462804f45ff9ac28d", "current repository-main identity")

    locks = st["source_locks"]["v49_post_v48_178_fullsupport_384_authority_sync"]
    req(locks["receipt_blob_sha1"] == RECEIPT_BLOB, "state receipt lock")
    req(locks["receipt_canonical_sha256"] == RECEIPT_CANON, "state receipt canonical lock")
    req(blob(AUDITED_STATE_VERIFIER_SNAPSHOT) == AUDITED_STATE_VERIFIER_BLOB, "audited state verifier snapshot drift")
    req(locks["verifier_blob_sha1"] == AUDITED_STATE_VERIFIER_BLOB, "state retained verifier lock")
    req(locks["compact_handoff_audited_exact_head"] == HANDOFF_HEAD, "state handoff head lock")
    req(locks["compact_handoff_blob_sha1"] == HANDOFF_PACKET_BLOB, "state handoff packet lock")
    req(locks["producer_exact_head"] == PRODUCER_HEAD, "state producer head lock")
    req(locks["hostile_audit_review_id"] == AUDIT_REVIEW, "state audit review lock")

    sweep = st["source_locks"]["live_specialist_sweep"]
    req(sweep["mode"] == "ROADMAP_SELECTED_ON_DEMAND_COORDINATION_SNAPSHOT", "coordination snapshot mode")
    req(sweep["global_sweep_required"] is False, "global sweep unexpectedly required")
    req(sweep["observed_repository_main"] == "a834864923086e5f7c1647e462804f45ff9ac28d", "coordination main")
    req(sweep["sweep_date"] == "2026-09-25", "coordination date")
    req(sweep["lane_178_status"] == "PARKED_RETAINED_AFTER_AUDITED_32_01_COMPLETION", "178 parked status")
    req(sweep["lane_178_retained_source_head"] == PRODUCER_HEAD, "178 retained source head")
    req(sweep["lane_178_latest_audited_exact_head"] == HANDOFF_HEAD, "178 audit head")
    req(sweep["lane_178_latest_audit_review_id"] == AUDIT_REVIEW, "178 audit receipt")
    req(sweep["lane_178_pending_main_handoff"] == "NONE", "178 pending handoff")
    req(sweep["ex5_pr"] == 1831 and sweep["ex5_head"] == "ffc3cf84ff9995b91bacd406193a05708f8cc84e", "32-02 EX5 helper")
    req(sweep["mb_pr"] == 1827 and sweep["mb_head"] == "50205efc2d57af4553cff75dd3667b204e4b089d", "32-03 MB")
    req(sweep["mb_fib_pr"] == 1829 and sweep["mb_fib_head"] == "090cf1ce97819736f9be09a9a96fb6421349acad", "32-03 MB-FIB")
    req(sweep["bridge_status"] == "PARKED_OPTIONAL_POST_32_01_REFINEMENT" and sweep["bridge_pending_main_handoff"] == "NONE", "BRIDGE parked")
    req(sweep["cut_status"] == "RETAINED_HISTORY_NO_OPEN_SUCCESSOR" and sweep["cut_pending_main_handoff"] == "NONE", "CUT retained")

    for k in ("effectivity_released","receiver_credit","route_credit","theorem_credit","endpoint_credit","stage32_closed","perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized"):
        req(st["firewalls"][k] is False, "firewall " + k)

    if args.handoff_root is not None:
        hr = args.handoff_root.resolve()
        req(git_head(hr) == HANDOFF_HEAD, "handoff checkout head")
        hp = load_locked(hr / HANDOFF_PACKET_REL, HANDOFF_PACKET_BLOB, HANDOFF_PACKET_CANON, "compact handoff packet")
        req((hr / HANDOFF_VERIFIER_REL).is_file() and blob(hr / HANDOFF_VERIFIER_REL) == HANDOFF_VERIFIER_BLOB, "compact handoff verifier drift")
        req(hp["accounting"]["candidate_global_upper_bound"] == str(NEW), "compact handoff bound")
        req(hp["accounting"]["tightening"] == str(TIGHT), "compact handoff tightening")
        req(hp["accounting"]["no_double_charge"] is True and hp["accounting"]["additive_subtraction"] is False, "compact handoff accounting")

    if args.producer_root is not None:
        pr = args.producer_root.resolve()
        req(git_head(pr) == PRODUCER_HEAD, "producer checkout head")
        sh = load_locked(pr / SOURCE_HANDOFF_REL, SOURCE_HANDOFF_BLOB, SOURCE_HANDOFF_CANON, "source handoff")
        cand = load_locked(pr / CANDIDATE_REL, CANDIDATE_BLOB, CANDIDATE_CANON, "source candidate")
        req((pr / SOURCE_HANDOFF_VERIFIER_REL).is_file() and blob(pr / SOURCE_HANDOFF_VERIFIER_REL) == SOURCE_HANDOFF_VERIFIER_BLOB, "source handoff verifier drift")
        req((pr / CANDIDATE_VERIFIER_REL).is_file() and blob(pr / CANDIDATE_VERIFIER_REL) == CANDIDATE_VERIFIER_BLOB, "candidate verifier drift")
        req(sh["disposition"]["candidate_upper_bound_if_current_v48_remains_authority"] == str(NEW), "source handoff candidate")
        req(cand["coverage"]["expected_coordinates"] == cand["coverage"]["eligible_replacement_coordinates"] == 384, "candidate coverage")
        req(cand["coverage"]["gaps"] == 0 and cand["coverage"]["overlaps"] == 0, "candidate gaps/overlaps")
        req(cand["semantics"]["main_consumption_performed"] is False, "producer self-consumption firewall")

    print("PASS: Stage32 MAIN V49 consumes hostile-audited POST-V48 178 384-coordinate bound as same-population replacement")
    print("V48_UPPER_BOUND=" + str(OLD))
    print("V49_UPPER_BOUND=" + str(NEW))
    print("TIGHTENING=" + str(TIGHT))
    print("ACCOUNTING=SAME_POPULATION_PER_COORDINATE_MIN_UPPER_BOUND_REPLACEMENT__NO_ADDITIVE_SUBTRACTION")

if __name__ == "__main__":
    main()
