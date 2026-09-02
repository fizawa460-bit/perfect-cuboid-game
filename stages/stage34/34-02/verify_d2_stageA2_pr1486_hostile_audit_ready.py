#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name: str):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require_blob(name: str, expected: str) -> None:
    got = git_blob_sha(ROOT / name)
    assert got == expected, (name, got, expected)


packet = load("d2-stageA2-pr1486-hostile-audit-ready.json")
assert packet["status"] == "READY_FOR_HOSTILE_AUDIT_NO_PROMOTION_APPLIED"
assert packet["authoritative_before_audit"]["remaining_branches"] == 8
assert packet["authoritative_before_audit"]["remaining_sign_orbits"] == 4
assert packet["promotion_ceiling_if_hostile_audit_passes_both_q80_39_representatives_and_sign_transfer"]["authoritative_after"]["remaining_branches"] == 4
assert packet["promotion_ceiling_if_hostile_audit_passes_both_q80_39_representatives_and_sign_transfer"]["authoritative_after"]["remaining_sign_orbits"] == 2

for item in packet["audit_candidates"]["q80_39_branch_closure_preaudit"]:
    require_blob(item["certificate"], item["certificate_blob_sha"])
    require_blob(item["lock"], item["lock_blob_sha"])
    require_blob(item["proof_script"], item["proof_script_blob_sha"])
    cert = load(item["certificate"])
    assert cert["branch_id"] == item["representative"]
    assert cert["sign_partner"] == item["sign_partner"]
    assert cert["status"] == item["preaudit_status"]
    assert cert["nondegenerate_full_parent_lift_count"] == 0
    assert cert["firewalls"]["branch_closed"] is False
    assert cert["firewalls"]["sign_partner_closed"] is False
    assert cert["firewalls"]["hostile_audit_passed"] is False
    assert cert["firewalls"]["authoritative_remaining_branches"] == 8
    assert cert["firewalls"]["authoritative_remaining_sign_orbits"] == 4

pair_meta = packet["audit_candidates"]["sign_transfer"]
require_blob(pair_meta["file"], pair_meta["blob_sha"])
pairs = load(pair_meta["file"])["pairs"]
pair_set = {(p["left"]["branch_id"], p["right"]["branch_id"]) for p in pairs}
for pair in map(tuple, pair_meta["required_pairs"]):
    assert pair in pair_set, pair

q84 = packet["audit_candidates"]["q84_13_rankzero_only"]
require_blob(q84["certificate"], q84["certificate_blob_sha"])
q84c = load(q84["certificate"])
assert q84c["status"] == q84["status"]
assert q84c["model38"]["mordell_weil_rank"] == 0
assert q84c["model165"]["mordell_weil_rank"] == 0
assert q84c["firewalls"]["rational_X_classified"] is False
assert q84c["firewalls"]["parent_pullback_classified"] is False
assert q84c["firewalls"]["branch_40dc_closed"] is False
assert q84c["firewalls"]["branch_7a7_closed"] is False
assert q84c["firewalls"]["authoritative_remaining_branches"] == 8
assert q84c["firewalls"]["authoritative_remaining_sign_orbits"] == 4

assert packet["forbidden_promotions"]["q84_13_branch_closure_from_rankzero_alone"] is True
assert packet["forbidden_promotions"]["remaining_8_to_0"] is True
assert packet["firewalls"]["hostile_audit_passed"] is False
assert packet["firewalls"]["promotion_applied"] is False
print("PASS PR1486 hostile-audit readiness packet: authority remains 8 branches / 4 sign orbits; promotion ceiling is 4 / 2.")
