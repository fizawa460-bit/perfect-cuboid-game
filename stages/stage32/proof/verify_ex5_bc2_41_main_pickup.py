#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PICKUP = HERE / "EX5-BC2-41-MAIN-PICKUP.json"
CAND = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-41-first-e8-block-main-subtraction-adapter-candidate.json"
MAIN = ROOT / "stages/stage32/MAIN-STATE.json"

EXPECTED_PICKUP_CANON = "236ba2a19ba627404b52bf7d21c1ba5b5745bb8c8eb67e7f6b41ff0c48bf4fd9"
EXPECTED_CAND_BLOB = "12791a4300afac6ce8b5324982d2ac63208dd4e7"
EXPECTED_CAND_CANON = "cd40eb0e9b380eb219d94fd75d44b457bcdb3d1edee83f1c9a56cac38415628a"
EXPECTED_MAIN_BLOB = "b8df16056625db5fbb1947f1e927593de258f1ff"
EXPECTED_MAIN_CANON = "bdaab3df8871e656652e5c1f78f972405081a45b8d5e421cc4a9bacddef3bf5d"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT, text=True).strip()


def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    req(PICKUP.is_file(), "missing MAIN pickup artifact")
    req(CAND.is_file(), "missing BC2-41 candidate")
    req(MAIN.is_file(), "missing MAIN state")
    req(blob(CAND) == EXPECTED_CAND_BLOB, "BC2-41 candidate blob drift")
    req(blob(MAIN) == EXPECTED_MAIN_BLOB, "MAIN state blob drift")

    p = json.loads(PICKUP.read_text())
    c = json.loads(CAND.read_text())
    m = json.loads(MAIN.read_text())

    req(p["schema"] == "STAGE32_MAIN_EX5_BC2_41_PICKUP_V1", "pickup schema")
    req(p["canonical_sha256_without_this_field"] == EXPECTED_PICKUP_CANON and canon(p) == EXPECTED_PICKUP_CANON, "pickup canonical")
    req(p["status"] == "PICKUP_READY_AUDIT_PENDING_NO_MAIN_CREDIT", "pickup status")
    req(p["producer_lane"] == "EX5" and p["consumer_lane"] == "MAIN", "lane routing")

    sl = p["source_locks"]
    req(sl["candidate_blob_sha1"] == EXPECTED_CAND_BLOB, "pickup candidate blob lock")
    req(sl["candidate_canonical_sha256"] == EXPECTED_CAND_CANON, "pickup candidate canonical lock")
    req(sl["main_state_blob_sha1"] == EXPECTED_MAIN_BLOB, "pickup MAIN blob lock")
    req(sl["main_state_canonical_sha256"] == EXPECTED_MAIN_CANON, "pickup MAIN canonical lock")
    req(sl["bc2_40_hostile_audit_exact_head"] == "b3b16f3db20074e3dbdb1851ad123d5c2004b843", "BC2-40 audited head")
    req(sl["bc2_40_hostile_audit_review_id"] == 5204245683, "BC2-40 audit review")

    req(c["canonical_sha256_without_this_field"] == EXPECTED_CAND_CANON and canon(c) == EXPECTED_CAND_CANON, "BC2-41 candidate canonical")
    req(c["status"] == "AUDIT_REQUIRED_NO_MAIN_CREDIT", "BC2-41 candidate status")
    req(c["target"] == {"block_index": 0, "current_main_audited_prefix_survivor": True, "d": 8, "e": 8, "g": 1, "row_id": "g1-d008", "terminal_count": 113, "terminal_rank_range": [0, 112]}, "BC2-41 target identity")
    req(c["coverage"]["bc2_40_audited_unsat_parent_count"] == 7336, "audited parent count")
    req(c["coverage"]["remaining_unknown_count"] == 0 and c["coverage"]["sat_count"] == 0, "candidate residual statuses")
    req(c["candidate_consequence"]["main_terminal_subtraction_candidate"] == 113, "113-terminal candidate")
    req(c["candidate_consequence"]["main_terminal_subtraction_authorized"] is False, "no subtraction authorization")

    # MAIN is intentionally source-locked but not mutated by this pickup surface.
    req(m["canonical_sha256_without_this_field"] == EXPECTED_MAIN_CANON, "MAIN canonical lock")
    req(p["main_pickup_contract"]["mainbatch_should_detect"] is True, "MAIN pickup flag")
    req(p["main_pickup_contract"]["bc2_41_hostile_audit_required_before_main_acceptance"] is True, "BC2-41 audit gate")
    req(p["main_pickup_contract"]["explicit_main_acceptance_required_before_subtraction"] is True, "MAIN acceptance gate")
    req(all(v is False for v in p["firewalls"].values()), "pickup credit firewalls")

    print("PASS: MAIN can detect the EX5 BC2-41 113-terminal subtraction candidate; audit/acceptance still required and MAIN credit remains zero")


if __name__ == "__main__":
    main()
