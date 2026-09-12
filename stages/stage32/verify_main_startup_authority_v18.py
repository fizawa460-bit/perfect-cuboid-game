#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
PREDECESSOR = ROOT / "stages/stage32/management/MAIN-STATE-V17-CUT196-PRE-REAUDIT.json"
RECEIPT = ROOT / "stages/stage32/management/post-cut196-v17-hostile-reaudit-pass-consumption-20260912.json"
V17_VERIFIER = ROOT / "stages/stage32/verify_main_startup_authority_v17.py"

STATE_BLOB = "48a3b18671ddd85a8b0916a8be1d9f611c38b534"
STATE_CANONICAL = "8590ba2d6a8d9e5250f5849a5052a3abeef43884eee2e237d5372dd61f841bef"
PREDECESSOR_BLOB = "157acdb438bfbde40a71a5974effbd097bff05df"
PREDECESSOR_CANONICAL = "a21faa5b3c3f5be259d8c5bc7ffa6f7aac827b911256e7a916e0bf9ea8e85de9"
RECEIPT_BLOB = "e9948350c09dfd769e6cf05297731fb499c2d677"
RECEIPT_CANONICAL = "e93fdfdd9405de44c6db459aa59a073f097da8fd3ffb2c34479ed63f543f1cb3"
V17_VERIFIER_BLOB = "80ced46d6a716f6e3ba13775cd8fb17f07afd72c"

AUDITED_V17_HEAD = "43685b50e285151364a0934b349f6dcc911484f4"
AUDITED_V17_REVIEW = 5186409565
AUDITED_V17_MAIN_CI = 34692061716
CUT197_PR = 1798
CUT197_HEAD = "c23df92827f7be9dbe9ca28cd240a576581b1763"
CUT197_HEAVY_RUN = 34691947196
POST = 47598978285064933730081
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
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def load_locked(path: Path, blob: str, can: str) -> dict:
    req(path.is_file(), f"missing {path.relative_to(ROOT)}")
    req(git_blob(path) == blob, f"blob drift {path.relative_to(ROOT)}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == can,
        f"stored canonical drift {path.relative_to(ROOT)}")
    req(canonical(obj) == can, f"canonical drift {path.relative_to(ROOT)}")
    return obj

def main() -> None:
    prev = load_locked(PREDECESSOR, PREDECESSOR_BLOB, PREDECESSOR_CANONICAL)
    req(prev["schema"] == "STAGE32_MAIN_COMPACT_STATE_V17_CUT196_AUDITED_CONSUMED",
        "unexpected V17 predecessor schema")
    pf = prev["current_exact_frontier"]
    req(pf["authoritative_remaining_strata"] == STRATA, "V17 predecessor strata drift")
    req(pf["authoritative_remaining_terminals"] == POST, "V17 predecessor terminals drift")
    req(pf["cut196_main_pruning_credit"] is True, "V17 CUT196 credit missing")
    req(pf["cut196_synchronized_head_hostile_audited"] is False,
        "V17 predecessor self-awarded replacement-head audit")
    req(git_blob(V17_VERIFIER) == V17_VERIFIER_BLOB, "V17 authority verifier blob drift")

    receipt = load_locked(RECEIPT, RECEIPT_BLOB, RECEIPT_CANONICAL)
    req(receipt["schema"] ==
        "STAGE32_MAIN_POST_CUT196_V17_HOSTILE_REAUDIT_PASS_CONSUMPTION_V1",
        "audit-consumption receipt schema drift")
    prior = receipt["prior_main_boundary"]
    req(prior["pr"] == 1799, "V17 predecessor PR drift")
    req(prior["exact_head"] == AUDITED_V17_HEAD, "V17 audited exact head drift")
    req(prior["hostile_reaudit_status"] == "PASS", "V17 hostile re-audit status drift")
    req(prior["hostile_reaudit_review_id"] == AUDITED_V17_REVIEW,
        "V17 hostile re-audit review drift")
    req(prior["exact_head_main_startup_ci_run"] == AUDITED_V17_MAIN_CI,
        "V17 exact-head MAIN CI drift")
    ra = receipt["authority"]
    req(ra["authority_before_and_after_same"] is True,
        "audit synchronization changed numerical authority")
    req(ra["before_remaining_strata"] == STRATA and
        ra["after_remaining_strata"] == STRATA, "audit-sync strata drift")
    req(ra["before_remaining_terminals"] == POST and
        ra["after_remaining_terminals"] == POST, "audit-sync terminal drift")

    cut197 = receipt["cut197_frontier"]
    req(cut197["pr"] == CUT197_PR, "CUT197 PR drift")
    req(cut197["observed_exact_head"] == CUT197_HEAD, "CUT197 selected head drift")
    req(cut197["survivor_offset_range"] == [1021, 1275], "CUT197 offset range drift")
    req(cut197["target_block_count"] == 255 and
        cut197["target_terminal_count"] == 28815, "CUT197 target population drift")
    req(cut197["heavy_workflow_run"] == CUT197_HEAVY_RUN and
        cut197["heavy_workflow_status"] == "SUCCESS", "CUT197 heavy evidence drift")
    req(cut197["heavy_all_8_shards_success"] is True, "CUT197 shard completion drift")
    req(cut197["retained_result_frozen"] is False,
        "CUT197 frontier incorrectly claims retained freeze")
    req(cut197["hostile_audit_status"] == "NOT_AUDITED",
        "CUT197 frontier incorrectly claims hostile audit")
    req(cut197["stage32_main_pruning_credit"] is False,
        "CUT197 frontier self-awarded MAIN credit")

    state = load_locked(STATE, STATE_BLOB, STATE_CANONICAL)
    req(state["schema"] ==
        "STAGE32_MAIN_COMPACT_STATE_V18_CUT196_REAUDIT_CONSUMED_CUT197_SELECTED",
        "unexpected V18 schema")
    auth = state["authority_sync"]
    req(auth["current_repository_main"] ==
        "e4d3b8b83626526ffeccdbd9c956081735fe1a6e", "repository main identity drift")
    req(auth["cut196_post_sync_reaudit_required"] is False,
        "CUT196 replacement re-audit still marked required")
    req(auth["cut196_post_sync_reaudit_status"] == "PASS",
        "CUT196 replacement re-audit PASS not consumed")
    req(auth["cut196_post_sync_reaudit_exact_head"] == AUDITED_V17_HEAD,
        "CUT196 replacement audited head drift")
    req(auth["cut196_post_sync_reaudit_review_id"] == AUDITED_V17_REVIEW,
        "CUT196 replacement audit review drift")
    req(auth["cut196_synchronized_head_hostile_audited"] is True,
        "CUT196 synchronized-head audit not consumed")
    req(auth["cut197_candidate_pr"] == CUT197_PR and
        auth["cut197_candidate_exact_head"] == CUT197_HEAD, "CUT197 selection drift")
    req(auth["cut197_heavy_workflow_run"] == CUT197_HEAVY_RUN and
        auth["cut197_heavy_workflow_status"] == "SUCCESS", "CUT197 heavy status drift")
    req(auth["cut197_candidate_hostile_audit_status"] == "NOT_AUDITED",
        "CUT197 self-awarded hostile audit")
    req(auth["cut197_main_pruning_credit_consumed"] is False,
        "CUT197 self-awarded MAIN consumption")

    f = state["current_exact_frontier"]
    req(f["authoritative_remaining_strata"] == STRATA, "V18 strata drift")
    req(f["authoritative_remaining_terminals"] == POST, "V18 terminal authority drift")
    req(f["cut196_main_pruning_credit"] is True, "V18 lost CUT196 MAIN credit")
    req(f["cut196_synchronized_head_hostile_audited"] is True,
        "V18 lost CUT196 synchronized audit")
    req(f["cut197_candidate_pr"] == CUT197_PR and
        f["cut197_candidate_exact_head"] == CUT197_HEAD, "V18 CUT197 frontier drift")
    req(f["cut197_heavy_workflow_status"] == "SUCCESS", "V18 CUT197 heavy status drift")
    req(f["cut197_retained_result_frozen"] is False,
        "V18 CUT197 retained freeze self-awarded")
    req(f["cut197_candidate_hostile_audited"] is False,
        "V18 CUT197 audit self-awarded")
    req(f["cut197_main_pruning_credit"] is False,
        "V18 CUT197 MAIN credit self-awarded")
    req(f["full178_numerical_census_complete"] is False, "FULL178 falsely closed")
    req(f["stage32_closed"] is False, "Stage32 falsely closed")

    fw = state["firewalls"]
    for key in ("receiver_credit", "theorem_credit", "endpoint_credit",
                "perfect_cuboid_existence_claim", "perfect_cuboid_nonexistence_claim",
                "merge_authorized", "stage32_closed"):
        req(fw[key] is False, f"firewall opened: {key}")
    req(fw["cut197_main_credit_without_retained_audit_and_current_authority_composition"]
        is False, "CUT197 promotion firewall drift")

    print(json.dumps({
        "verdict":"PASS_STAGE32_MAIN_V18_CUT196_REAUDIT_CONSUMED_CUT197_SELECTED",
        "authoritative_remaining_strata":STRATA,
        "authoritative_remaining_terminals":POST,
        "cut196_replacement_head_hostile_reaudited":True,
        "cut197_heavy_run":CUT197_HEAVY_RUN,
        "cut197_heavy_success":True,
        "cut197_retained_result_frozen":False,
        "cut197_hostile_audited":False,
        "cut197_main_pruning_credit":False,
        "full178_complete":False,
        "merge_authorized":False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
