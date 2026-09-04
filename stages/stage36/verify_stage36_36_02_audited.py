#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage36/MAIN-STATE.json"
INV_PATH = ROOT / "stages/stage36/36-02/representative-inventory.json"

AUDITED_INVENTORY_BLOB = "88130b9380a677a191f91c24df87618e65be0a2f"
AUDITED_HEAD = "3a78f9ff156b53f509625d353df48d1b3e02b836"
AUDIT_REVIEW = 5113379283
AUDIT_CI_RUN = 33876389406
AUDIT_CI_JOB = 101034265419
AUDITED_PR_MERGE = "4c93ccb79e95cbcd9e2416ad3b6a3f4788d6f586"
PROMOTION_MERGE = "26fb608cb2551ab2102ae36ad3b57c063959df58"
HISTORICAL_BASE = "a873c8fca0074aa966a22e36475a3551a378560d"


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def main() -> None:
    # S30-WF02: freeze the hostile-audited mathematical inventory byte-for-byte.
    require(blob_sha(INV_PATH) == AUDITED_INVENTORY_BLOB, "36-02 audited inventory blob drift")

    inv = json.loads(INV_PATH.read_text())
    require(inv.get("schema") == "STAGE36_36_02_THREE_Q_REPRESENTATIVE_INVENTORY_V1", "36-02 inventory schema moved")
    require(inv.get("status") == "EXACT_THREE_Q_REPRESENTATIVES_PENDING_HOSTILE_AUDIT", "36-02 audited inventory historical status moved")
    require(inv.get("base_main_sha") == HISTORICAL_BASE, "36-02 audited inventory historical base moved")
    require(inv.get("pass_condition") == {
        "THREE_CERTIFIED_Q_REPRESENTATIVES_EXACT": True,
        "EXACT_Q_ISOMORPHISM_CLASS_COUNT_CLAIM": False,
    }, "36-02 audited pass condition moved")
    require(inv.get("finite_reconstruction", {}).get("q_orbit_sizes") == [6, 2, 2], "36-02 Q orbit split moved")
    require(inv.get("finite_reconstruction", {}).get("geometric_qi_orbit_sizes") == [8, 2], "36-02 Q(i) orbit split moved")
    require(inv.get("finite_reconstruction", {}).get("exact_Q_isomorphism_class_count_proved") is False, "36-02 Q-isomorphism firewall moved")
    require(set(inv.get("representatives", {})) == {"Q6_GEOM8", "Q2_GEOM8", "Q2_GEOM2"}, "36-02 representative set moved")
    require(inv.get("degree_check", {}).get("generic_squareclass_rank") == 3, "36-02 squareclass rank moved")
    require(inv.get("degree_check", {}).get("canonical_quotient_degree") == 8, "36-02 degree moved")
    require(all(v is False for v in inv.get("claims", {}).values()), "36-02 audited inventory leaked higher credit")

    state = json.loads(STATE_PATH.read_text())
    schema = state.get("schema")
    require(schema in {
        "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V5_36_02_AUDITED",
        "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V6_36_03_PENDING_AUDIT",
    }, "36-02 audited successor schema moved")

    auth = state.get("stage36_36_02_authority", {})
    require(auth == {
        "pr": 1541,
        "hostile_audit_review": AUDIT_REVIEW,
        "audited_head": AUDITED_HEAD,
        "merged_main_sha": AUDITED_PR_MERGE,
        "exact_head_ci_run": AUDIT_CI_RUN,
        "exact_head_ci_job": AUDIT_CI_JOB,
        "inventory_blob_sha": AUDITED_INVENTORY_BLOB,
        "verdict": "PASS",
    }, "36-02 authority block moved")

    unit = state.get("completed_units", {}).get("36-02", {})
    require(unit.get("status") == "AUDITED_PASS", "36-02 unit not audited PASS")
    require(unit.get("promotion_status") == "AUDITED", "36-02 unit promotion moved")
    require(unit.get("hostile_audit_review") == AUDIT_REVIEW, "36-02 review moved")
    require(unit.get("audited_head") == AUDITED_HEAD, "36-02 audited head moved")
    require(unit.get("exact_head_ci_run") == AUDIT_CI_RUN, "36-02 CI run moved")
    require(unit.get("exact_head_ci_job") == AUDIT_CI_JOB, "36-02 CI job moved")
    require(unit.get("merged_main_sha") == AUDITED_PR_MERGE, "36-02 merged authority moved")
    require(unit.get("inventory_blob_sha") == AUDITED_INVENTORY_BLOB, "36-02 inventory authority moved")
    require(unit.get("THREE_CERTIFIED_Q_REPRESENTATIVES_EXACT") is True, "36-02 exact representative credit lost")
    require(unit.get("EXACT_Q_ISOMORPHISM_CLASS_COUNT_CLAIM") is False, "36-02 Q-isomorphism overclaim")
    require(unit.get("NEW_THEOREM_CREDIT") is False, "36-02 theorem credit leaked")

    gates = state.get("promotion_gates", {})
    require(gates.get("source_authority_lock_complete") is True, "36-01 authority gate lost")
    require(gates.get("three_Q_representatives_exact") is True, "36-02 audited gate not promoted")
    require(gates.get("physical_open_push_and_boundary_complete") is False, "36-03 gate promoted during 36-02 replay")
    for key, value in gates.items():
        if key not in {"source_authority_lock_complete", "three_Q_representatives_exact"}:
            require(value is False, f"later gate prematurely promoted: {key}")

    current = state.get("current", {})
    require(current.get("unit") == "36-03", "current unit is not 36-03")
    require(current.get("next_exact_leaf") == "36-03_PHYSICAL_OPEN_PUSH_AND_BOUNDARY", "36-03 leaf moved")
    require(all(v is False for v in state.get("claims", {}).values()), "Stage36 higher claim leaked")

    if schema == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V5_36_02_AUDITED":
        require(state.get("status") == "ACTIVE", "36-02 promotion state status moved")
        require(state.get("base_main_sha") == AUDITED_PR_MERGE, "36-02 promotion state base moved")
        require("36-03" not in state.get("completed_units", {}), "36-03 started inside 36-02 promotion state")
    else:
        require(state.get("status") == "ACTIVE_PENDING_HOSTILE_AUDIT", "36-03 successor audit status moved")
        require(state.get("base_main_sha") == PROMOTION_MERGE, "36-03 successor base moved")
        promo = state.get("stage36_36_02_promotion", {})
        require(promo.get("pr") == 1548, "36-02 promotion PR moved")
        require(promo.get("merged_main_sha") == PROMOTION_MERGE, "36-02 promotion merge moved")
        require(promo.get("NEW_THEOREM_CREDIT") is False, "36-02 promotion leaked theorem credit")
        next_unit = state.get("completed_units", {}).get("36-03", {})
        require(next_unit.get("promotion_status") == "PROVISIONAL_NOT_AUDITED", "36-03 successor prematurely audited")

    print("PASS STAGE36_36_02_AUDITED_SUCCESSOR_REPLAY")
    print(f"hostile_audit_review={AUDIT_REVIEW}; audited_head={AUDITED_HEAD}")
    print(f"audited_inventory_blob={AUDITED_INVENTORY_BLOB}")
    print(f"successor_schema={schema}; three_Q_representatives_exact=true")
    print("no theorem/receiver/endpoint/perfect-cuboid credit")


if __name__ == "__main__":
    main()
