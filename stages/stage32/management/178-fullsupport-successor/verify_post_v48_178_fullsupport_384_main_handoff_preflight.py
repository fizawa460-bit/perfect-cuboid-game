#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

HANDOFF = HERE / "POST-V48-178-FULLSUPPORT-384-MAIN-HANDOFF-PREFLIGHT.json"
HANDOFF_BLOB = "3667b2395f50b675f6f8286074e20e0212933e2f"
HANDOFF_CANON = "f52f6e74f3ab20c9d5c8a831351da7035af9cccea50893560f4307de5dab9e76"

CANDIDATE_REL = Path("stages/stage32/32-01-178/fibration-nef/V48-FULL-SUPPORT-384-EQUIV-DERIVED-BOUND-RETAINED.json")
CANDIDATE_BLOB = "3acb9551db9fda6be8fde0194b23ddb41ca634d0"
CANDIDATE_CANON = "da7eb532daf2b775a49524fe45e5b7bf7851719f19a6926a227f5fa745258aba"
CANDIDATE_VERIFY_REL = Path("stages/stage32/32-01-178/fibration-nef/verify_v48_full_support_384_equiv_derived_bound_retained.py")
CANDIDATE_VERIFY_BLOB = "843d348351a05be083f2d0d6e16b08da45e38040"

CURRENT_MAIN_HEAD = "a834864923086e5f7c1647e462804f45ff9ac28d"
CURRENT_MAIN_STATE_BLOB = "070847c669120aef1ab3777239d45878937b41f3"
V48_SYNC_REL = Path("stages/stage32/management/178-support-qbc/V48-178-SUPPORT-QBC-AUTHORITY-SYNC.json")
V48_SYNC_BLOB = "2733e5519629e6365558bc1b4bfbc6305e0b5533"
V48_SYNC_CANON = "d106029369dd5a029cd7a56e1c7d80fdd29f8471454fd2ed6c638af2b70288b1"
V48_VERIFY_REL = Path("stages/stage32/management/178-support-qbc/verify_v48_178_support_qbc_authority_sync.py")
V48_VERIFY_BLOB = "d719482d9799f8594b4436d0882bd33945583536"

V48_TOTAL = 128470212118313474449
V48_COVERED = 37911631052805557219
REPLACEMENT_COVERED = 37884640022451662730
TIGHTENING = 26991030353894489
CANDIDATE_TOTAL = 128443221087959579960


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_locked(p: Path, expected_blob: str, expected_canon: str | None, label: str) -> dict:
    req(p.is_file(), "missing " + label)
    req(blob(p) == expected_blob, label + " blob drift")
    o = json.loads(p.read_text(encoding="utf-8"))
    if expected_canon is not None:
        req(o.get("canonical_sha256_without_this_field") == expected_canon, label + " stored canonical drift")
        req(canon(o) == expected_canon, label + " canonical drift")
    return o


def verify_main_root(root: Path, handoff: dict) -> None:
    req((root / ".git").exists(), "main-root is not a checkout")
    state_path = root / "stages/stage32/MAIN-STATE.json"
    req(state_path.is_file(), "main-root missing MAIN-STATE")
    req(blob(state_path) == CURRENT_MAIN_STATE_BLOB, "current MAIN state blob drift")

    sync = load_locked(root / V48_SYNC_REL, V48_SYNC_BLOB, V48_SYNC_CANON, "V48 authority sync")
    req((root / V48_VERIFY_REL).is_file() and blob(root / V48_VERIFY_REL) == V48_VERIFY_BLOB,
        "V48 authority-sync verifier blob drift")
    req(sync["authority"]["v48_same_population_replacement_upper_bound"] == str(V48_TOTAL),
        "V48 sync authority bound drift")
    req(sync["authority"]["additive_subtraction"] is False, "V48 sync additive accounting drift")
    req(sync["authority"]["no_double_charge"] is True, "V48 sync no-double-charge drift")
    req(sync["firewalls"]["main_credit_consumed"] is True, "V48 sync not consumed by MAIN")

    main_ref = handoff["current_main_authority"]
    req(main_ref["repository_main"] == CURRENT_MAIN_HEAD, "handoff current-main head drift")
    req(main_ref["main_state_blob_sha1"] == CURRENT_MAIN_STATE_BLOB, "handoff MAIN-state lock drift")
    req(main_ref["v48_authority_sync_blob_sha1"] == V48_SYNC_BLOB, "handoff V48-sync blob lock drift")
    req(main_ref["v48_authority_sync_canonical_sha256"] == V48_SYNC_CANON, "handoff V48-sync canonical lock drift")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane178-root", type=Path, default=ROOT)
    ap.add_argument("--main-root", type=Path)
    args = ap.parse_args()

    lane_root = args.lane178_root.resolve()
    candidate = lane_root / CANDIDATE_REL
    candidate_verify = lane_root / CANDIDATE_VERIFY_REL

    h = load_locked(HANDOFF, HANDOFF_BLOB, HANDOFF_CANON, "MAIN handoff")
    c = load_locked(candidate, CANDIDATE_BLOB, CANDIDATE_CANON, "384/384 candidate")
    req(candidate_verify.is_file() and blob(candidate_verify) == CANDIDATE_VERIFY_BLOB,
        "candidate verifier blob drift")

    subprocess.run([sys.executable, str(candidate_verify)], check=True)

    req(h["schema"] == "STAGE32_MAIN_POST_V48_178_FULLSUPPORT_384_HANDOFF_PREFLIGHT_V1",
        "handoff schema drift")
    req(h["status"] == "READY_FOR_HOSTILE_AUDIT__NOT_AUTHORIZED_FOR_MAIN_CONSUMPTION__ZERO_MAIN_CREDIT",
        "handoff status drift")

    auth = h["current_main_authority"]
    req(int(auth["authoritative_remaining_terminals"]) == V48_TOTAL, "handoff V48 total drift")
    req(auth["semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET",
        "handoff authority semantics drift")
    req(auth["full178_numerical_census_complete"] is True, "handoff FULL178 census flag drift")

    p = h["producer"]
    req(p["specialist_pr"] == 1821, "producer PR drift")
    req(p["candidate_blob_sha1"] == CANDIDATE_BLOB, "candidate blob lock drift")
    req(p["candidate_canonical_sha256"] == CANDIDATE_CANON, "candidate canonical lock drift")
    req(p["candidate_verifier_blob_sha1"] == CANDIDATE_VERIFY_BLOB, "candidate verifier lock drift")
    req(int(p["candidate_upper_bound"]) == CANDIDATE_TOTAL, "producer candidate drift")
    req(int(p["tightening_vs_v48"]) == TIGHTENING, "producer tightening drift")
    req(p["main_consumption_performed"] is False, "producer self-consumption overclaim")
    req(p["coverage"] == {
        "expected_coordinates": 384,
        "eligible_replacement_coordinates": 384,
        "strict_replacement_coordinates": 384,
        "gaps": 0,
        "overlaps": 0,
        "source_ineligible_coordinates": 0,
    }, "producer coverage drift")

    cc = c["coverage"]
    req(cc["expected_coordinates"] == 384 and cc["eligible_replacement_coordinates"] == 384,
        "candidate 384 coverage drift")
    req(cc["strict_replacement_coordinates"] == 384 and cc["gaps"] == 0 and cc["overlaps"] == 0,
        "candidate strict coverage drift")
    req(int(c["derivation"]["candidate_global_upper_bound_if_promoted"]) == CANDIDATE_TOTAL,
        "candidate certificate total drift")
    req(int(c["derivation"]["certified_tightening_vs_v48"]) == TIGHTENING,
        "candidate certificate tightening drift")
    req(c["firewalls"]["hostile_audit_required_before_promotion"] is True,
        "candidate hostile-audit firewall drift")
    req(c["semantics"]["main_consumption_performed"] is False,
        "candidate already consumed")

    a = h["same_population_accounting"]
    req(int(a["v48_covered_384_upper_bound_sum"]) == V48_COVERED, "covered V48 sum drift")
    req(int(a["replacement_384_upper_bound_sum"]) == REPLACEMENT_COVERED, "covered replacement sum drift")
    req(int(a["tightening_on_covered_population"]) == TIGHTENING, "covered tightening drift")
    req(V48_COVERED - REPLACEMENT_COVERED == TIGHTENING, "covered arithmetic drift")
    req(V48_TOTAL - V48_COVERED + REPLACEMENT_COVERED == CANDIDATE_TOTAL,
        "global replacement arithmetic drift")
    req(int(a["global_formula_value"]) == CANDIDATE_TOTAL, "stored global formula drift")
    req(a["composition_rule"] == "SAME_POPULATION_PER_COORDINATE_MIN_UPPER_BOUND_REPLACEMENT__NO_ADDITIVE_SUBTRACTION",
        "composition rule drift")
    req(a["candidate_is_not_an_identity_set"] is True, "identity-set semantics overclaim")
    req(a["exact_intersection_identity_set_required"] is False, "identity-set requirement drift")
    req(a["additive_subtraction"] is False, "additive subtraction forbidden")
    req(a["statistical_independence"] is False, "independence assumption forbidden")
    req(a["no_double_charge"] is True, "no-double-charge firewall drift")
    req(a["uncovered_v48_population_unchanged"] is True, "uncovered population drift")

    audit = h["hostile_audit_gate"]
    req(audit["required"] is True and audit["status"] == "PENDING", "hostile-audit gate drift")
    req(audit["audited_exact_head"] is None and audit["review_or_comment_id"] is None,
        "premature audit identity")
    req(audit["exact_head_ci_required"] is True, "exact-head CI gate drift")
    req(audit["promotion_before_pass_forbidden"] is True, "promotion firewall drift")

    g = h["future_main_consumer_requirements"]
    for k in (
        "producer_candidate_verifier_pass_required",
        "producer_hostile_audit_pass_required",
        "producer_exact_head_ci_required",
        "v48_authority_identity_recheck_required",
        "current_main_refresh_required",
        "strict_improvement_against_then_current_main_required",
        "if_main_has_advanced_reclassify_instead_of_subtracting_from_stale_v48",
        "same_population_replacement_only",
        "additive_stacking_with_v48_or_overlapping_178_routes_forbidden",
        "explicit_main_authority_sync_receipt_required",
        "main_state_update_must_be_separate_from_producer",
    ):
        req(g[k] is True, "future MAIN consumer requirement drift " + k)

    d = h["disposition"]
    req(d["handoff_ready_for_hostile_audit"] is True, "handoff audit readiness drift")
    req(d["handoff_ready_for_main_consumption"] is False, "premature MAIN consumption readiness")
    req(int(d["candidate_upper_bound_if_current_v48_remains_authority"]) == CANDIDATE_TOTAL,
        "disposition candidate drift")
    req(int(d["candidate_tightening_if_current_v48_remains_authority"]) == TIGHTENING,
        "disposition tightening drift")
    req(d["main_pruning_credit"] is False and d["main_authority_changed"] is False,
        "premature MAIN credit")
    req(d["merge_authorized"] is False, "merge authorization drift")

    for k, v in h["firewalls"].items():
        req(v is False, "handoff firewall drift " + k)

    if args.main_root is not None:
        verify_main_root(args.main_root.resolve(), h)

    print("POST_V48_178_FULLSUPPORT_MAIN_HANDOFF_PREFLIGHT=PASS")
    print("CURRENT_V48_UPPER_BOUND=128470212118313474449")
    print("CANDIDATE_REPLACEMENT_UPPER_BOUND=128443221087959579960")
    print("TIGHTENING_IF_V48_REMAINS_CURRENT=26991030353894489")
    print("COMPOSITION=SAME_POPULATION_BOUND_REPLACEMENT_NOT_ADDITIVE_SUBTRACTION")
    print("HOSTILE_AUDIT_STATUS=PENDING")
    print("MAIN_CONSUMPTION_AUTHORIZED=false")
    print("MAIN_CREDIT_CHANGED=false")


if __name__ == "__main__":
    main()
