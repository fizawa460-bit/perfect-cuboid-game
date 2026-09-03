#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-proper14-boundary-bridge-absence-lock-v46.json"


def main() -> None:
    d = json.loads(CERT.read_text(encoding="utf-8"))
    assert d["schema"] == "stage33.e3.proper14_boundary_bridge_absence_lock.v46"
    assert d["micro_goal"] == "A1_1_LOCK_BRIDGE_ABSENCE_IN_FROZEN_INPUTS"
    assert d["scope"] == "CURRENT_STAGE33_FROZEN_REVIEWED_INPUT_SET_ONLY"
    assert d["bridge"]["name"] == "P_W"
    assert d["bridge"]["materialized_in_frozen_inputs"] is False
    assert d["bridge"]["global_nonexistence_claimed"] is False
    assert d["search_policy"]["broad_search_allowed"] is False
    assert d["search_policy"]["repeat_search_of_reviewed_assets_allowed"] is False
    assert d["search_policy"]["reopen_conditions"] == [
        "NEW_NAMED_INPUT_ARTIFACT",
        "EXPLICIT_AUTHORITY_CONTRADICTION",
        "VERIFIER_OR_HOSTILE_AUDIT_INPUT_CHANGE",
    ]
    anti = set(d["anti_inference"])
    assert "DO_NOT_REOPEN_STAGE33_11D_11E_11F_OR_BROAD_HISTORY_SEARCH_WITHOUT_A_REOPEN_CONDITION" in anti
    locks = d["source_locks"]
    assert locks["a1_0_basis_lock_commit"] == "1c5157a7e5fc556da7e7bb7f66b19366b7dd6c5c"
    assert locks["v44_bridge_gap_canonical_sha256"] == "81368384bfa77ebe37a27e7eb2f16b7244810fe998e1c47db00f31751f2f5445"
    assert locks["v41_e3_source_canonical_sha256"] == "04c6ead2226c87defff085fc641ee80867e1fdf4b07baa28c5e97d2c5e534ac6"
    assert d["stage33_credit"] == {
        "progress_big_tasks": "6/11",
        "stage33_12_exact_closed": False,
        "stage33_13_released": False,
        "endpoint_credit": False,
        "merge_allowed": False,
    }
    assert d["status"] == "PASS_EXACT_A1_1_FROZEN_INPUT_ABSENCE_LOCK_NO_RESEARCH"
    assert d["next_exact_leaf"] == "DEFINE_FINITE_NEW_CONSTRUCTION_CONTRACT_FOR_P_W_WITHOUT_SEARCHING_FOR_AN_EXISTING_BRIDGE"
    print("PASS: V46 frozen-input bridge absence lock")


if __name__ == "__main__":
    main()
