#!/usr/bin/env python3
"""Local-only check of Stage32 MB104 route-E operational index (no theorem credit)."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STATE = HERE.parent / "STATE.json"
PREFIX = "stages/stage32/32-03-multibranch/MB104/route-E/"
EXPECTED = {f"E{i:02d}" for i in range(1, 13)} | {"F83"}

def require(ok: bool, label: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + label)

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> None:
    data = json.loads(STATE.read_text(encoding="utf-8"))
    route = data["route_register"]["routes"]["E"]
    items = route["github_unaudited_notes"]
    ids = [item["id"] for item in items]
    require(len(ids) == len(set(ids)) == 13 and set(ids) == EXPECTED, "route-E inventory E01-E12 + F83")
    for item in items:
        rel = item["note_path"]
        require(rel.startswith(PREFIX) and ".." not in Path(rel).parts, "safe source path " + item["id"])
        path = ROOT / rel
        require(path.is_file(), "source exists " + item["id"])
        require(digest(path) == item["note_sha256"], "source SHA256 " + item["id"])
    e11 = next(z for z in items if z["id"] == "E11")
    require(e11["status"] == "EXACT_SLACK0_SMALL_BIDEGREES_AUDIT_PASS_SCOPED_ZERO_CREDIT", "E11 scoped audit status")
    audit_rel = e11["audit_record_path"]
    require(audit_rel.startswith(PREFIX), "E11 audit path")
    require(digest(ROOT / audit_rel) == e11["audit_record_sha256"], "E11 audit source SHA256")
    e12 = next(z for z in items if z["id"] == "E12")
    require(e12["status"] == "UNAUDITED_RESEARCH_NOTE_PARKED_ZERO_CREDIT" and e12["audit_required"] is True, "E12 parked noncredit")
    require(all(v is False for v in e12["credit"].values()), "E12 credit firewall")
    require(route["status"] == "OPEN_PARKED", "global MB route-E still open")
    require(data["next_obligation"]["active_leaf"] == data["resume_obligation"]["active_leaf"] == "MB104-000707-E2-UNIQUE-PAIR-M1-POSTULATION-OR-BULK", "legacy audit leaf unchanged")
    nxt = data["next_obligation"]["operational_next"]
    require(nxt["stage32_32_03_complete"] is False and nxt["new_main_credit"] is False and nxt["audit_or_merge_authorization"] is False, "operational firewalls")
    require(all(v is False for v in data["credit_firewall"].values()), "MB credit firewall")
    d16 = json.loads((ROOT / "stages/stage32/management/d16-all-classes/RESULT.json").read_text(encoding="utf-8"))
    require("round 3 PASS" in d16["status"] and d16["main_authority_change"] is False and d16["credit_flags_changed"] is False, "fixed-degree D16 noncredit")
    main = (ROOT / "stages/stage32/MAIN-START-HERE.md").read_text(encoding="utf-8")
    require("next_obligation.operational_next" in main and "d = 16 multibranch classes (32-03)" not in main, "MAIN startup current routing")
    print("PASS: route-E E01-E12 + F83 exact SHA256; E11 scoped PASS; E12 parked; D16 fixed-degree; legacy verifier leaf preserved; MB credit unchanged")

if __name__ == "__main__":
    main()
