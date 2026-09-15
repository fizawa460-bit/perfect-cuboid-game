#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ADAPTER = HERE / "CURRENT-MAIN-NO-DOUBLE-CHARGE-ADAPTER.json"
EXPECTED_ADAPTER_CANON = "14de9512d0ad1449b80b89f660ccbfd6d9e0864702e9b711234e8697596ff7c1"

LOCKS = {
    "current_main_state": (
        "stages/stage32/MAIN-STATE.json",
        "b8df16056625db5fbb1947f1e927593de258f1ff",
        None,
    ),
    "hpadj08_full178_result": (
        "stages/stage32-ex5/hpadj-08_ex5/FULL178-RESULT.json",
        "f9a01c3e673dc630a3446ac4560c72c4f76db812",
        "625e289a1a9f086b5e02f247665a7f9ac4b7fe72eaacd3011fe73a0e96041953",
    ),
    "hpadj08_preflight": (
        "stages/stage32-ex5/hpadj-08_ex5/HPADJ08-EX5-EXACT-SQUARE-PREFLIGHT.json",
        "8ecc5ecd97838d4225de1d1163fd8843451b68e5",
        "9867898a32d34f470ec421fef560527dcbcc5579453a0dab8454553a142cf953",
    ),
    "hpadj08_worker": (
        "stages/stage32-ex5/hpadj-08_ex5/hpadj08_ex5_full178_b_shard.py",
        "c5fc340ea734dfc54436f124bb302c1ec6c5677c",
        None,
    ),
    "hpadj07_main_consumption": (
        "stages/stage32/management/hpadj-07/HPADJ07-V23-MAIN-CONSUMPTION.json",
        "e942711b67ebc43b39a73ab55bc10862654059f8",
        "6fc1800b84de587e2218c372966e1424186405e57477586e8a284961f575f417",
    ),
    "hpadj07_current_v23_rebase": (
        "stages/stage32/management/hpadj-07/proof-chain/CURRENT-V23-CONSERVATIVE-REBASE.json",
        "8883cfc59a6d48e34d7e256fad15e69714dc02d1",
        "9ae15dd70a3ba84fe83d2d11dfa8e1081c44a8b06e68b78dda4f871aa0f00e01",
    ),
    "corrected_general_type_adjunction": (
        "stages/stage32/management/hpadj-07/proof-chain/GENERAL-TYPE-ADJUNCTION-CORRECTION.json",
        "c90b41dcfbd5bd081629a6fa62d9447d43cb3d5e",
        "87e9ee4ea791d894f5f1ba093d5ad295ad2ebb3d569f2f50fa9a1b1d4c1858aa",
    ),
}

A = 20713268924714183714810
B = 40886299509963924857401
C = 154697
CURRENT = 26876434389242951089388
SAFE = 20173030585249740987894
POST = 6703403803993210101494


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_json(path: Path, blob: str, expected_canon: str | None) -> dict:
    req(path.is_file(), f"missing {path}")
    req(git_blob(path) == blob, f"blob drift {path}")
    if path.suffix != ".json":
        req(expected_canon is None, f"non-JSON source unexpectedly has canonical lock {path}")
        return {}
    obj = json.loads(path.read_text(encoding="utf-8"))
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon,
            f"stored canonical drift {path}")
        req(canon(obj) == expected_canon, f"canonical drift {path}")
    return obj


def main() -> None:
    adapter = json.loads(ADAPTER.read_text(encoding="utf-8"))
    req(adapter.get("canonical_sha256_without_this_field") == EXPECTED_ADAPTER_CANON,
        "adapter stored canonical drift")
    req(canon(adapter) == EXPECTED_ADAPTER_CANON, "adapter canonical drift")

    loaded = {}
    for name, (rel, blob, expected_canon) in LOCKS.items():
        loaded[name] = load_json(ROOT / rel, blob, expected_canon)

    state = loaded["current_main_state"]
    frontier = state["current_exact_frontier"]
    req(state.get("schema") == "STAGE32_MAIN_COMPACT_STATE_V24_HPADJ07_AUDIT_SYNCED",
        "current MAIN schema drift")
    req(frontier["authoritative_remaining_strata"] == 17128, "MAIN strata drift")
    req(frontier["authoritative_remaining_terminals"] == CURRENT, "MAIN terminal authority drift")
    req(frontier["authoritative_remaining_terminals_semantics"] ==
        "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET",
        "MAIN remaining semantics drift")
    req(frontier["hpadj07_main_pruning_credit"] is True, "HPADJ07 not consumed in MAIN")
    req(frontier["hpadj07_certified_rejected_terminals_lower_bound"] ==
        20713268924714183560113, "consumed HPADJ07 lower bound drift")

    result = loaded["hpadj08_full178_result"]
    req(result["old_group_cauchy_candidate_rejected_terminals"] == A, "HPADJ08 A count drift")
    req(result["stored_exact_square_candidate_rejected_terminals"] == B, "HPADJ08 B count drift")
    req(result["incremental_candidate_over_group_cauchy"] == B - A, "HPADJ08 increment drift")

    preflight = loaded["hpadj08_preflight"]
    req(preflight["mathematical_contract"]["group_cauchy_is_subset"] is True,
        "group-Cauchy subset contract missing")
    req(preflight["scaleout"]["main_overlap_resolution_deferred_to_main"] is True,
        "HPADJ08 overlap handoff contract drift")

    consumption = loaded["hpadj07_main_consumption"]
    req(consumption["accounting"]["later_v23_certlift03_removed_terminals"] == C,
        "CERTLIFT03 count drift in HPADJ07 consumption")
    req(consumption["accounting"]["double_charge"] is False,
        "prior HPADJ07 double-charge firewall drift")

    rebase = loaded["hpadj07_current_v23_rebase"]
    req(rebase["set_theoretic_rebase"]["v22_to_v23_total_removed"] == C,
        "V22->V23 removed count drift")
    req(rebase["composition_notes"]["earlier_cut_overlap"].startswith(
        "The corrected V22 replay inherits HPADJ-01's conservative composition firewall"),
        "earlier CUT overlap firewall drift")

    correction = loaded["corrected_general_type_adjunction"]
    req(correction["corrected_v22_conservative_replay"]
        ["candidate_rejected_terminals_lower_bound"] == A,
        "corrected HPADJ07 candidate count drift")

    acct = adapter["set_theoretic_accounting"]
    req(acct["A_count"] == A and acct["B_count"] == B and acct["C_count"] == C,
        "adapter source counts drift")
    req(acct["B_minus_A_count"] == B - A, "adapter B-minus-A arithmetic drift")
    req(SAFE == (B - A) - C, "verifier safe increment constant drift")
    req(acct["safe_current_main_incremental_rejected_terminals_lower_bound"] == SAFE,
        "adapter safe increment drift")
    req(POST == CURRENT - SAFE, "verifier post-bound constant drift")
    req(acct["current_main_pre_adapter_remaining_terminals_upper_bound"] == CURRENT,
        "adapter current MAIN bound drift")
    req(acct["candidate_post_adapter_remaining_terminals_upper_bound"] == POST,
        "adapter post-bound drift")
    req(acct["exact_C_intersection_with_B_minus_A_computed"] is False,
        "adapter unexpectedly claims exact overlap")
    req(acct["exact_overlap_required_for_safe_lower_bound"] is False,
        "adapter exact-overlap requirement drift")
    req(acct["no_double_charge_proved_for_stated_lower_bound"] is True,
        "adapter no-double-charge proof flag missing")

    credit = adapter["credit"]
    for key in (
        "stage32_main_pruning_credit", "main_promotion_authorized", "full178_complete",
        "effectivity_credit", "receiver_credit", "theorem_credit", "endpoint_credit",
        "stage32_closed", "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim", "merge_authorized",
    ):
        req(credit[key] is False, f"credit firewall opened: {key}")
    req(credit["adapter_candidate_only"] is True, "adapter candidate firewall missing")
    req(credit["current_main_subtraction_prepared"] is True,
        "adapter subtraction-prepared flag missing")

    print(json.dumps({
        "status": "PASS",
        "safe_current_main_incremental_rejected_terminals_lower_bound": SAFE,
        "candidate_post_adapter_remaining_terminals_upper_bound": POST,
        "exact_overlap_computed": False,
        "worst_case_overlap_bound": C,
        "stage32_main_pruning_credit": False,
        "main_promotion_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
