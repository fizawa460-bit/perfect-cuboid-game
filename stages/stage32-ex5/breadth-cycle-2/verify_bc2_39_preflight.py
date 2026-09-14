#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PREFLIGHT = HERE / "bc2-39-fresh-unknown30-replay-preflight.json"
SOURCE = HERE / "bc2_39_replay_explicit_fresh_unknown30.py"
CP38 = HERE / "bc2-38-fresh-unknown34-replay-checkpoint.json"
B38 = HERE / "bc2_38_replay_explicit_fresh_unknown34.py"
SYNC = ROOT / "LIVE-MAIN-COORDINATION-SYNC-20260914.json"

PREFLIGHT_BLOB = "e3dab72865d734f2420fb71ddf3c29115f9df68e"
PREFLIGHT_CANON = "7bda94c5869c988892c979873f13a1c311debedbbe9fcc670a253e339fb5e435"
SOURCE_BLOB = "e322029cfc4476ce8cf3685ca04f35b58e2ce9f2"
CP38_BLOB = "91eca02054cd2dbf702dd4a7635398ef76ee832f"
CP38_CANON = "88b41680df6bb78f8b7f8ca00cde121d909a39e7b3c29eef765edb77b2c022ba"
B38_BLOB = "6fb0af6c77e44edfa5d2b8a13fbde73bfbd468aa"
SYNC_BLOB = "c9a3a878413df5afc634f99b94707534412b5d84"
SYNC_CANON = "fd5c7c6d025286a5677b7dcab5113f066dff83574c4647d772d89c7799b8be6c"
UNKNOWN_SHA = "d60d873c4fc66ebb6cda0530d4137e5fd195fe1b601b0a21e91f873c1df28fb7"
UNKNOWN = [1048,1050,1056,1103,1206,1216,1218,1243,1251,1703,1706,1717,1719,1733,1798,2092,2122,2187,2407,2634,2651,2819,3205,3375,3635,3885,3901,3915,3980,4200]


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def canon(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main() -> None:
    req(blob(PREFLIGHT) == PREFLIGHT_BLOB, "preflight blob")
    pf = json.loads(PREFLIGHT.read_text())
    req(pf["canonical_sha256_without_this_field"] == PREFLIGHT_CANON and canon(pf) == PREFLIGHT_CANON, "preflight canonical")
    req(blob(SOURCE) == SOURCE_BLOB, "producer blob")
    req(blob(CP38) == CP38_BLOB and blob(B38) == B38_BLOB, "BC2-38 source/checkpoint identity")
    cp = json.loads(CP38.read_text())
    req(cp["canonical_sha256_without_this_field"] == CP38_CANON and canon(cp) == CP38_CANON, "BC2-38 checkpoint canonical")
    r = cp["replay"]
    req((r["parents_checked"], r["unsat_count"], r["unknown_count"], r["sat_count"]) == (34,4,30,0), "BC2-38 partition")
    req(r["unknown_parent_indices"] == UNKNOWN and r["unknown_parent_indices_sha256"] == UNKNOWN_SHA, "BC2-38 unknown30 identity")
    req(cp["credit"]["known_parent_unsat_count_lower_bound"] == 7306, "BC2-38 audited candidate lower bound identity")

    req(blob(SYNC) == SYNC_BLOB, "live MAIN coordination sync blob")
    sync = json.loads(SYNC.read_text())
    req(sync["canonical_sha256_without_this_field"] == SYNC_CANON and canon(sync) == SYNC_CANON, "live MAIN coordination sync canonical")
    req(sync["live_exact_head"] == "9d4a24ef479d031e9c4b85001fe8f7a10198b17d", "live MAIN head")
    req(sync["live_cross_lane_registry"]["open_ex5_producer_demand_count"] == 0, "OPEN EX5 producer demand")
    req(sync["live_main_state"]["mainbatch_stop_gate"] == "NONE", "MAIN stop gate")
    req(sync["live_main_state"]["full178_complete"] is False, "FULL178 firewall")
    req(sync["live_main_state"]["remaining_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "MAIN terminal semantics")

    a = pf["audit_consumption"]
    req(a == {
        "bc2_38_hostile_audit_exact_head": "5e1d07e4c92fbecff9bfa89b0bfb65cdaf564a71",
        "bc2_38_hostile_audit_review_id": 5190676180,
        "bc2_38_hostile_audit_status": "PASS",
    }, "BC2-38 audit consumption")
    t = pf["target"]
    req(t["audited_unknown_parent_count"] == 30 and t["audited_unknown_parent_indices_sha256"] == UNKNOWN_SHA and t["parent_indices"] == UNKNOWN and t["prior_audited_unsat_count"] == 7306, "BC2-39 target")
    ex = pf["execution"]
    req(ex["per_parent_timeout_ms"] == 160000 and ex["effective_heavy_concurrency"] == 1 and ex["heavy_scaleout_authorized"] is False and ex["compact_result_only"] is True, "bounded execution")
    sp = pf["storage_preflight"]
    req(sp["planned_heavy_jobs"] == 1 and sp["planned_artifact_count"] == 1 and sp["projected_peak_new_storage_bytes"] <= sp["repository_operating_budget_bytes"] and sp["within_budget"] is True, "storage preflight")
    for key, value in pf["firewalls"].items():
        req(value is False, "firewall " + key)

    print("PASS: BC2-39 preflight is source-locked to hostile-audited BC2-38 unknown30 and live MAIN coordination")
    print("target=30 prior_audited_lower_bound=7306 timeout_ms=160000 concurrency=1 scaleout=NO main_credit=NO merge=NO")


if __name__ == "__main__":
    main()
