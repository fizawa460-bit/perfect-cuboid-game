#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
RECEIPT = HERE / "GRF04-V38-TD02-FULL178-INTEGER-LATTICE-MAIN-BOUND-REPLACEMENT.json"
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stages/stage32/proof/ACTIVE-FRONTIER.json"
ADAPTERS = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"

PREDECESSOR_HEAD = "515adec9cde85e6d2285d71a590ab5c4e4d8c797"
PREDECESSOR_STATE_BLOB = "ee1947fa9fd742fbadc484624283866abdbd5a68"
PREDECESSOR_STATE_CANON = "0395d7a3f31da0cd05a6016ebd2811c0ce53b6eb4c809f4a89c998eff8c14c41"
HANDOFF_HEAD = "df3b29d20ef0f7da1e34fa92beada6418ad3a4ea"
HANDOFF_PATH = "stages/stage32/32-01-178/topdown-02/TD02-FULL178-V37-SYNC-HANDOFF.json"
HANDOFF_BLOB = "f05dc4f04f77594204298bdfd9784d9e95810eb3"
HANDOFF_CANON = "56b5c35c0343be327431977ecdde0426be923e7925052d8660ba97ae583630ab"
AUDITED_HEAD = "640195f158e2fa953ebd669820a794a56cef04fb"
AUDIT_REVIEW = 5218209619
CHECKPOINT_PATH = "stages/stage32/32-01-178/topdown-02/TD02-INTEGER-LATTICE-CAPACITY-FULL178-CHECKPOINT.json"
CHECKPOINT_BLOB = "896eefd68ce7804db28a533d61cb490f14730b1c"
V1_PATH = "stages/stage32/32-01-178/topdown-02/verify_td02_integer_lattice_capacity_full178.py"
V1_BLOB = "e4adb6fd92d88f4d9c10923627cac9424425e467"
V2_PATH = "stages/stage32/32-01-178/topdown-02/verify_td02_integer_lattice_capacity_full178_v2.py"
V2_BLOB = "331073833aee5ebe106d0bd5cd2370506284a27d"
REPLAY_HEAD = "92c68646b0844953c6f9c895a180225bcf75ed17"
REPLAY_RUN = 35054156118
OLD = 195603649074545538415
NEW = 195414091250828468192
TIGHTENING = 189557823717070223
NUMERATOR = 54911359641482799562031
DENOMINATOR = 281
REMAINDER = 79
RECEIPT_BLOB = "f959b922129354f58c2fd0e1b182d723bfa174e2"
RECEIPT_CANON = "8adf31a03c6c1fd6538e25c50deb059b843d34cfaf174bc2993f078b4657a08b"
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
    ap.add_argument("--handoff-root", type=Path)
    ap.add_argument("--audited-root", type=Path)
    args = ap.parse_args()
    req((args.handoff_root is None) == (args.audited_root is None),
        "handoff-root and audited-root must be supplied together")

    state = current_state()
    receipt = lock_json(RECEIPT, RECEIPT_BLOB, RECEIPT_CANON, "V38 replacement receipt")
    req(blob(REGISTRY) == REGISTRY_BLOB, "claim registry drift")
    req(blob(FRONTIER) == FRONTIER_BLOB, "active frontier drift")
    req(blob(ADAPTERS) == ADAPTERS_BLOB, "lane adapters drift")

    if args.handoff_root is not None:
        handoff = lock_json(args.handoff_root / HANDOFF_PATH, HANDOFF_BLOB, HANDOFF_CANON,
                            "178 V37-sync handoff")
        req(blob(args.audited_root / CHECKPOINT_PATH) == CHECKPOINT_BLOB,
            "audited FULL178 checkpoint blob drift")
        req(blob(args.audited_root / V1_PATH) == V1_BLOB, "audited FULL178 V1 verifier drift")
        req(blob(args.audited_root / V2_PATH) == V2_BLOB, "audited FULL178 V2 verifier drift")
        req(handoff["audited_boundary"]["audited_exact_head"] == AUDITED_HEAD,
            "handoff audited head")
        req(handoff["audited_boundary"]["hostile_audit_status"] == "PASS",
            "handoff hostile audit status")
        req(handoff["audited_boundary"]["audit_review_id"] == AUDIT_REVIEW,
            "handoff audit review")
        req(handoff["post_sync_replay"]["replay_exact_head"] == REPLAY_HEAD,
            "handoff replay head")
        req(handoff["post_sync_replay"]["run_id"] == REPLAY_RUN and
            handoff["post_sync_replay"]["conclusion"] == "SUCCESS",
            "handoff replay evidence")
        req(handoff["candidate"]["upper_floor"] == NEW, "handoff candidate floor")
        req(handoff["candidate"]["potential_tightening_if_consumed"] == TIGHTENING,
            "handoff tightening")
        req(handoff["consumer_contract"]["producer_ready_for_main_reentry"] is True,
            "producer not ready for MAIN re-entry")

    req(receipt["status"] ==
        "AUDITED_FULL178_HANDOFF_CONSUMED__REPLACEMENT_HEAD_PENDING_HOSTILE_REAUDIT",
        "receipt status")
    pred = receipt["predecessor_authority"]
    req(pred["version"] == "V37_FULL178_INTEGER_LATTICE_ROUTED_WAIT", "predecessor version")
    req(pred["exact_head"] == PREDECESSOR_HEAD, "predecessor head")
    req(pred["state_blob_sha1"] == PREDECESSOR_STATE_BLOB, "predecessor state blob")
    req(pred["state_canonical_sha256"] == PREDECESSOR_STATE_CANON,
        "predecessor state canonical")
    req(pred["authoritative_remaining_terminals"] == OLD, "predecessor authority")

    src = receipt["consumed_handoff"]
    req(src["producer_pr"] == 1815 and src["handoff_head"] == HANDOFF_HEAD,
        "producer handoff identity")
    req(src["handoff_blob_sha1"] == HANDOFF_BLOB and
        src["handoff_canonical_sha256"] == HANDOFF_CANON, "handoff source lock")
    req(src["audited_exact_head"] == AUDITED_HEAD and
        src["hostile_audit_review_id"] == AUDIT_REVIEW and
        src["hostile_audit_status"] == "PASS", "hostile audit identity")
    req(src["postsync_replay_exact_head"] == REPLAY_HEAD and
        src["postsync_replay_run_id"] == REPLAY_RUN and
        src["postsync_replay_conclusion"] == "SUCCESS", "post-sync replay identity")
    req(src["candidate_exact_upper_numerator"] == NUMERATOR and
        src["candidate_exact_upper_denominator"] == DENOMINATOR, "exact rational candidate")
    req(NUMERATOR // DENOMINATOR == NEW and NUMERATOR % DENOMINATOR == REMAINDER,
        "candidate floor arithmetic")
    req(src["candidate_upper_floor"] == NEW and
        src["candidate_floor_remainder"] == REMAINDER, "candidate floor/remainder")
    req(src["candidate_tightening_vs_v37"] == TIGHTENING, "candidate tightening")

    repl = receipt["replacement"]
    req(repl["authority_version"] == "V38", "replacement authority version")
    req(repl["authoritative_remaining_strata"] == 17128, "replacement strata")
    req(repl["authoritative_remaining_terminals"] == NEW, "replacement authority")
    req(repl["tightening_vs_v37"] == TIGHTENING, "replacement tightening")
    req(repl["composition_rule"] ==
        "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING",
        "replacement composition")
    req(repl["exact_incremental_rejected_identity_set_claimed"] is False,
        "identity-set overclaim")
    req(repl["additive_subtraction_performed"] is False and repl["double_charge"] is False,
        "additive/double-charge firewall")
    req(repl["full178_numerical_census_complete"] is False and
        repl["stage32_closed"] is False, "replacement closure overclaim")

    cs = receipt["claim_sync"]
    req(cs["logical_claim_statement_changed"] is False, "claim statement changed")
    req(cs["claim_registry_mutated"] is False and cs["active_frontier_mutated"] is False
        and cs["lane_adapters_mutated"] is False, "claim DAG unexpectedly mutated")
    req(cs["claim_id"] == "S32.FULL178.NUMERICAL_CENSUS.V1" and
        cs["claim_status"] == "DECLARED_GOAL_ACTIVE_INCOMPLETE", "claim status")

    req(state["schema"] ==
        "STAGE32_MAIN_COMPACT_STATE_V38_FULL178_INTEGER_LATTICE_BOUND_CONSUMED_REAUDIT_PENDING",
        "state schema")
    sync = state["authority_sync"]
    req(sync["predecessor_process_head"] == PREDECESSOR_HEAD, "state predecessor head")
    req(sync["td02_full178_integer_lattice_main_numeric_bound_replacement_consumed"] is True,
        "state consumption flag")
    req(sync["td02_full178_candidate_hostile_audit_review_id"] == AUDIT_REVIEW and
        sync["td02_full178_candidate_hostile_audit_status"] == "PASS",
        "state producer audit")
    req(sync["td02_full178_consumption_rule"] ==
        "MIN_OF_INDEPENDENT_CERTIFIED_UPPER_BOUNDS__NO_ADDITIVE_STACKING",
        "state composition")

    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == 17128, "MAIN strata authority")
    req(f["predecessor_v37_authoritative_remaining_terminals"] == OLD, "V37 bound")
    req(f["authoritative_remaining_terminals"] == NEW, "V38 bound")
    req(f["v38_td02_full178_certified_numeric_bound_tightening_vs_v37"] == TIGHTENING,
        "V38 tightening")
    req(f["live_178_td02_main_credit_consumed"] is True, "MAIN consumption not recorded")
    req(f["full178_numerical_census_complete"] is False and f["stage32_closed"] is False,
        "FULL178/closure firewall")

    req(state["current"]["mainbatch_stop_gate"] == "REPLACEMENT_HEAD_HOSTILE_REAUDIT_REQUIRED",
        "replacement hostile-reaudit gate")
    req(state["current"]["next_exact_route"] ==
        "HOSTILE_AUDIT_V38_FULL178_INTEGER_LATTICE_BOUND_REPLACEMENT",
        "next exact route")
    req(state["firewalls"]["replacement_head_hostile_reaudit_required"] is True,
        "replacement audit firewall")
    for key in ("effectivity_released", "endpoint_credit", "full178_complete",
                "merge_authorized", "perfect_cuboid_existence_claim",
                "perfect_cuboid_nonexistence_claim", "receiver_credit", "route_credit",
                "stage32_closed", "theorem_credit"):
        req(state["firewalls"][key] is False, f"firewall {key}")

    req(OLD - NEW == TIGHTENING, "authority arithmetic")
    print("PASS: Stage32 V38 consumes the hostile-audited TD02 FULL178 integer-lattice upper bound by MIN composition")
    if args.handoff_root is not None:
        print("PASS: exact producer handoff/checkpoint/verifier source locks replayed")
    else:
        print("PASS: local projection verified; external producer source replay delegated to exact-head CI/audit")
    print("PASS: replacement head is fail-closed pending hostile reaudit; FULL178 census and downstream credit remain incomplete")


if __name__ == "__main__":
    main()
