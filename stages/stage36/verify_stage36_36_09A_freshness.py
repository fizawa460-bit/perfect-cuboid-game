#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/"stages/stage36/MAIN-STATE.json"
CURRENT_MAIN="38434ea3c4124efd1cc04a228e85b2fd207f2c14"
SYNC_MERGE="0d35b0cba86ec1bb940dabe36df672385e20f6da"
HISTORICAL_CERT_BLOB="66f31c03e5a978783a60b036322538f173a2f411"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def main() -> None:
    s=json.loads(STATE.read_text())
    req(s.get("schema")=="STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V14_36_09A_PENDING_HOSTILE_AUDIT","V14 schema moved")
    req(s.get("status")=="ACTIVE_PENDING_HOSTILE_AUDIT","36-09A lifecycle moved")
    req(s.get("base_main_sha")==CURRENT_MAIN,"current-main lock stale")
    f=s.get("freshness_sync_36_09A",{})
    req(f.get("sync_pr")==1579,"freshness source PR moved")
    req(f.get("main_sha")==CURRENT_MAIN,"freshness main SHA moved")
    req(f.get("merge_commit")==SYNC_MERGE,"freshness merge commit moved")
    req("Stage35-EX-only advance via #1579" in f.get("scope",""),"freshness scope moved")
    u=s.get("completed_units",{}).get("36-09A",{})
    req(u.get("certificate_blob_sha")==HISTORICAL_CERT_BLOB,"36-09A mathematical certificate identity moved")
    req(u.get("promotion_status")=="PROVISIONAL_NOT_AUDITED","36-09A audit state moved")
    req(u.get("legal_outcome")=="BLOCKED_UPSTREAM_BR2A_BR2B_INCOMPLETE","36-09A legal outcome moved")
    req(u.get("CAMP4_TO_CAMP2_BRAUER_COMPATIBILITY_PROVED") is False,"compatibility credit leaked")
    req(u.get("CAMP4_TO_CAMP2_BRAUER_INCOMPATIBILITY_PROVED") is False,"incompatibility credit leaked")
    cur=s.get("current",{})
    req(cur.get("unit")=="36-09A" and cur.get("36_09B_entry_allowed") is False,"36-09B boundary moved")
    req(all(v is False for v in s.get("claims",{}).values()),"higher Stage36 claim leaked")
    print("PASS STAGE36_36_09A_CURRENT_MAIN_FRESHNESS")
    print(f"current_main={CURRENT_MAIN}; sync_merge={SYNC_MERGE}")
    print("historical mathematical certificate unchanged; no higher credit")


if __name__=="__main__":
    main()
