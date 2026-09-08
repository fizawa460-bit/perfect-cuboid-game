#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ART = HERE / "post1728-breadth-reentry-audit.json"


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


d = json.loads(ART.read_text(encoding="utf-8"))
stored = d.pop("canonical_sha256_without_this_field")
assert csha(d) == stored == "0123671e5e029c1411916d20ba45fec66e5b2cfe2b35a27fedc57bae362607fb"
assert d["schema"] == "STAGE32EX5_POST1728_BREADTH_REENTRY_AUDIT_V1"
assert d["authority"] == "SCRATCH_NONAUTHORITATIVE"
assert d["base_main_sha"] == "56ce8213ffe90635aaa499c46639971c952724f1"

for lock in d["source_locks"]:
    p = ROOT / lock["path"]
    assert p.is_file(), lock["path"]
    assert blob_sha1(p) == lock["blob_sha1"], lock["path"]

assert d["receiver_delta"]["g1_d186_numerical_row_status"] == "OPEN"
assert d["receiver_delta"]["v6_subpopulation_status"] == "CLOSED_AUDITED_NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER"
assert d["xstage_reentry_test"]["pr1728_satisfies_blocker"] is False
assert d["xstage_reentry_test"]["xstage_route_status"] == "BLOCKED_UNCHANGED"
assert d["independence_test"]["can_direct_import_qualify_as_independent_ex5_route"] is False

p = d["new_pattern"]
assert p["status"] == "LIVE"
assert p["receiver_effect_obtained"] is False
assert "RES3=73,97,235" in p["scope_specific_constants"]
assert "bidegree endpoints 81,105" in p["scope_specific_constants"]

ledger = {x["candidate_id"]: x for x in d["candidate_ledger"]}
assert ledger["EX5R-CSC-002"]["status"] == "LIVE"
assert ledger["EX5R-ENUM-BTVA-002"]["status"] == "UNTESTED"
assert d["cycle"]["route_status"] == "BLOCKED_NEW_PATTERN_ISOLATED"
assert d["cycle"]["exhaustive_view_audit"] is True
assert d["cycle"]["blind_rediscovery"] is True
assert d["cycle"]["breadth_cycle_2_authority_opened"] is False
assert d["cycle"]["breadth_cycle_2_scratch_candidate_opened"] is True
assert d["next_route"] == "EX5R-CSC-002_NON_V6_CLASS_TO_CELLULAR_ASSEMBLY_ADAPTER_PREFLIGHT"

for key, value in d["firewalls"].items():
    assert value is False, key

print("PASS_STAGE32EX5_POST1728_BREADTH_REENTRY_AUDIT")
print("next", d["next_route"])
