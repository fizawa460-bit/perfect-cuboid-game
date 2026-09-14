#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STAGE = ROOT / "stages/stage32"
STATE = STAGE / "MAIN-STATE.json"
PREDECESSOR = STAGE / "management/MAIN-STATE-V18-N358-PRECONSUMPTION.json"
N358_RESULT = STAGE / "management/N358-AUDITED-RESULT.json"
RECEIPT = STAGE / "management/post-n358-current-v18-composition-consumption-20260912.json"
COMPOSITION = STAGE / "management/verify_n358_v18_current_authority_composition.py"

STATE_BLOB = "acad022fe90b4d72edeac5f9d7ba08930decdff2"
STATE_CANONICAL = "2f0ed49bd3640f4f7158176bc435344d46785928e20c4ce67173305eb3974771"
PREDECESSOR_BLOB = "48a3b18671ddd85a8b0916a8be1d9f611c38b534"
PREDECESSOR_CANONICAL = "8590ba2d6a8d9e5250f5849a5052a3abeef43884eee2e237d5372dd61f841bef"
N358_RESULT_BLOB = "e42c2b6cc6128c4666372b0c3f3c172afc006d7f"
N358_RESULT_CANONICAL = "383921ed9387693a8cfa300a9629f629f3a20ed4272979508441c7b13af5a287"
RECEIPT_BLOB = "efa87a1b62cc698745f87814cd8f9eb9fe95dbd2"
RECEIPT_CANONICAL = "27c50848e19c242389298b6a23d7c5b6a8ea86afd97c36ced16905adc66a5bdc"
COMPOSITION_BLOB = "e441287905c35284fd33e7ede7956d3db1c4aa80"

AUDITED_V18_HEAD = "152e8f92346c038aed5628d7d70063cc5c8cd9d4"
AUDITED_V18_REVIEW = 5186446561
AUDITED_V18_MAIN_CI = 34694166001
AUDITED_N358_HEAD = "462174f74d6470ec7c64f5b6d078757c7b3372fc"
AUDITED_N358_REVIEW = 5184322011
AUDITED_N358_CI = 34659319718

PRE = 47598978285064933730081
INC = 9274971107798843958
POST = 47589703313957134886123
STRATA = 17128

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def load_locked(path: Path, blob: str, can: str) -> dict:
    req(path.is_file(), f"missing {path.relative_to(ROOT)}")
    req(git_blob(path) == blob, f"blob drift {path.relative_to(ROOT)}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == can, f"stored canonical drift {path.relative_to(ROOT)}")
    req(canonical(obj) == can, f"canonical drift {path.relative_to(ROOT)}")
    return obj

def main() -> None:
    prev = load_locked(PREDECESSOR, PREDECESSOR_BLOB, PREDECESSOR_CANONICAL)
    req(prev["schema"] == "STAGE32_MAIN_COMPACT_STATE_V18_CUT196_REAUDIT_CONSUMED_CUT197_SELECTED", "unexpected V18 predecessor schema")
    pf = prev["current_exact_frontier"]
    req(pf["authoritative_remaining_strata"] == STRATA, "V18 predecessor strata drift")
    req(pf["authoritative_remaining_terminals"] == PRE, "V18 predecessor terminals drift")
    req(pf["n357_main_pruning_credit"] is True, "V18 lost N357 credit")
    req(pf["cut195_main_pruning_credit"] is True and pf["cut196_main_pruning_credit"] is True, "V18 consumed CUT credit drift")
    req(pf["cut197_main_pruning_credit"] is False, "V18 self-awarded CUT197 credit")

    n358 = load_locked(N358_RESULT, N358_RESULT_BLOB, N358_RESULT_CANONICAL)
    req(n358["node_id"] == "N358", "N358 result node drift")
    agg = n358["aggregate"]
    req(agg["incremental_rejected_terminals"] == INC, "N358 audited increment drift")
    req(agg["source_terminals"] == 47598978285064933810198, "N358 audited source drift")
    req(agg["candidate_remaining_terminals"] == 47589703313957134966240, "N358 historical candidate remainder drift")
    req(n358["semantics"]["main_pruning_credit"] is False, "audited N358 artifact self-awarded MAIN credit")

    req(git_blob(COMPOSITION) == COMPOSITION_BLOB, "N358 current-V18 composition verifier drift")
    receipt = load_locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANONICAL)
    req(receipt["schema"] == "STAGE32_MAIN_POST_N358_CURRENT_V18_COMPOSITION_CONSUMPTION_V1", "N358 consumption receipt schema drift")
    prior = receipt["prior_main_boundary"]
    req(prior["exact_head"] == AUDITED_V18_HEAD, "V18 audited exact head drift")
    req(prior["hostile_reaudit_review_id"] == AUDITED_V18_REVIEW, "V18 hostile audit review drift")
    req(prior["exact_head_main_startup_ci_run"] == AUDITED_V18_MAIN_CI, "V18 exact-head MAIN CI drift")
    cand = receipt["n358_candidate"]
    req(cand["audited_exact_head"] == AUDITED_N358_HEAD, "N358 audited head drift")
    req(cand["hostile_audit_review_id"] == AUDITED_N358_REVIEW and cand["hostile_audit_status"] == "PASS", "N358 audit identity/status drift")
    req(cand["exact_head_claim_frontier_ci_run"] == AUDITED_N358_CI, "N358 exact-head CI drift")
    rr = receipt["current_v18_composition_replay"]
    req(rr["n358_is_incremental_on_hostile_audited_n357_frontier"] is True, "N358/N357 incremental semantics lost")
    req(rr["n357_overlap_terminals"] == 0, "N358/N357 overlap drift")
    req(all(x["n358_overlap_terminals"] == 0 for x in rr["consumed_cut_targets"]), "N358/consumed-cut overlap drift")
    req(rr["already_consumed_cut_total_terminals"] == 80117, "consumed-cut total drift")
    req(rr["double_charge"] is False, "N358 double-charge flag set")
    ra = receipt["authority"]
    req(ra["before_remaining_terminals"] == PRE, "receipt pre-authority drift")
    req(ra["incremental_rejected_terminals"] == INC, "receipt increment drift")
    req(ra["after_remaining_terminals"] == POST, "receipt post-authority drift")
    req(PRE - INC == POST, "N358 current-authority arithmetic drift")

    state = load_locked(STATE, STATE_BLOB, STATE_CANONICAL)
    req(state["schema"] == "STAGE32_MAIN_COMPACT_STATE_V19_N358_AUDITED_CURRENT_V18_CONSUMED", "unexpected V19 schema")
    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == STRATA, "V19 strata drift")
    req(f["authoritative_remaining_terminals"] == POST, "V19 terminal authority drift")
    req(f["n358_main_pruning_credit"] is True, "V19 N358 MAIN credit missing")
    req(f["n358_incremental_rejected_terminals"] == INC, "V19 N358 increment drift")
    req(f["n358_current_v18_overlap_consumed_main_terminals"] == 0, "V19 overlap drift")
    req(f["n358_synchronized_head_hostile_audited"] is False, "V19 replacement head self-awarded hostile audit")
    req(f["cut193_main_pruning_credit"] is False, "CUT193 gained unauthorized credit")
    req(f["cut197_main_pruning_credit"] is False, "CUT197 gained unauthorized credit")
    req(f["full178_numerical_census_complete"] is False, "FULL178 falsely closed")
    req(f["stage32_closed"] is False, "Stage32 falsely closed")

    auth = state["authority_sync"]
    req(auth["n358_candidate_hostile_audit_status"] == "PASS", "N358 hostile audit PASS missing")
    req(auth["n358_candidate_hostile_audit_review_id"] == AUDITED_N358_REVIEW, "N358 review drift")
    req(auth["n358_current_v18_composition_replayed"] is True, "N358 current-V18 composition replay missing")
    req(auth["n358_current_v18_overlap_consumed_main_terminals"] == 0, "N358 overlap not zero")
    req(auth["n358_main_pruning_credit_consumed"] is True, "N358 consumption flag false")
    req(auth["n358_post_sync_reaudit_required"] is True and auth["n358_post_sync_reaudit_status"] == "PENDING", "replacement-head re-audit gate lost")

    fw = state["firewalls"]
    for key in ("receiver_credit", "theorem_credit", "endpoint_credit", "perfect_cuboid_existence_claim",
                "perfect_cuboid_nonexistence_claim", "merge_authorized", "stage32_closed"):
        req(fw[key] is False, f"firewall opened: {key}")

    print(json.dumps({
        "verdict":"PASS_STAGE32_MAIN_V19_N358_AUDITED_CURRENT_V18_CONSUMED",
        "n358_incremental_rejected_terminals":INC,
        "n358_overlap_consumed_main_terminals":0,
        "authoritative_remaining_strata":STRATA,
        "authoritative_remaining_terminals":POST,
        "full178_complete":False,
        "replacement_head_hostile_reaudit_required":True,
        "merge_authorized":False
    }, sort_keys=True))

if __name__ == "__main__":
    main()
