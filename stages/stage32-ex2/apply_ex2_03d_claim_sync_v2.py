#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
REGISTRY = ROOT / "stages/stage32/proof/CLAIM-REGISTRY.json"
LANES = ROOT / "stages/stage32/proof/LANE-ADAPTERS.json"
STATE = HERE / "MAIN-STATE.json"
VERIFY_MAIN = HERE / "verify_main_state.py"
ORIGINAL_HELPER = HERE / "apply_ex2_03d_claim_sync.py"

V1 = "S32.EX2.SECTION_SOURCE_INVENTORY.V1"
V2 = "S32.EX2.SECTION_SOURCE_INVENTORY.V2"
V1_CORE = "8f9c9f588b68c997340c954777b1f14cb255470e9035f900cbd3e6204df5ba0e"
V2_CORE = "8e712dc5941068dbf2db7d3163991dc2163c4b449d3f6f83713df727d48b955b"
V2_VERIFIER = "stages/stage32-ex2/verify_ex2_01_section_sources_v2.py"
V2_VERIFIER_BLOB = "0d5a4025002d2bb30765023ae96d164fb77e5ecb"
INVENTORY = "stages/stage32-ex2/EX2-01/section-source-inventory.json"
INVENTORY_BLOB = "3f9ddf435093dfd681373a1e01f455d0db04642d"
CORE_KEYS = [
    "claim_id", "kind", "statement", "scope_key", "scope", "proves",
    "does_not_prove", "requires", "bridges", "source_locks", "replay_verifier",
]


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def dump(path: Path, obj: object) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")


def v2_claim_from_v1(v1: dict) -> dict:
    c = {
        "claim_id": V2,
        "kind": v1["kind"],
        "statement": v1["statement"],
        "scope_key": v1["scope_key"],
        "scope": v1["scope"],
        "proves": v1["proves"],
        "does_not_prove": v1["does_not_prove"],
        "requires": v1["requires"],
        "source_locks": [
            {"blob_sha1": INVENTORY_BLOB, "path": INVENTORY},
            {"blob_sha1": V2_VERIFIER_BLOB, "path": V2_VERIFIER},
        ],
        "replay_verifier": V2_VERIFIER,
        "authority_status": "PROVISIONAL",
        "audit_receipt": None,
    }
    c["claim_core_sha256"] = csha({k: c[k] for k in CORE_KEYS if k in c})
    assert c["claim_core_sha256"] == V2_CORE
    return c


# Preserve the immutable V1 evidence exactly and version only the repaired replay interface.
r = json.loads(REGISTRY.read_text())
claims = {c["claim_id"]: c for c in r["claims"]}
assert V1 in claims
v1 = claims[V1]
assert v1["claim_core_sha256"] == V1_CORE
assert v1["source_locks"] == [
    {"blob_sha1": INVENTORY_BLOB, "path": INVENTORY},
    {
        "blob_sha1": "369a0946bf2ffb70e8d29b8e990c4073cdc804a3",
        "path": "stages/stage32-ex2/verify_ex2_01_section_sources.py",
    },
]
v1["authority_status"] = "SUPERSEDED"
v2 = v2_claim_from_v1(v1)
if V2 in claims:
    assert claims[V2] == v2
else:
    idx = r["claims"].index(v1)
    r["claims"].insert(idx + 1, v2)
dump(REGISTRY, r)

l = json.loads(LANES.read_text())
ex2 = next(x for x in l["lanes"] if x["lane"] == "EX2")
refs = ex2["claim_refs"]
if V1 in refs:
    refs[refs.index(V1)] = V2
assert V2 in refs and V1 not in refs
dump(LANES, l)

# Apply the already-source-locked EX2-03D registration/state transition.
runpy.run_path(str(ORIGINAL_HELPER), run_name="__main__")

# The generated MAIN verifier must replay the versioned repair, while immutable V1 stays on disk.
text = VERIFY_MAIN.read_text()
old = ' "verify_ex2_01_section_sources.py",'
new = ' "verify_ex2_01_section_sources_v2.py",'
assert old in text and V2_VERIFIER.split("/")[-1] not in text
text = text.replace(old, new, 1)
VERIFY_MAIN.write_text(text)

# Keep the active working set explicit about the versioned replay repair.
s = json.loads(STATE.read_text())
if V2_VERIFIER not in s["current_leaf_working_set"]:
    insert_at = s["current_leaf_working_set"].index(INVENTORY) + 1
    s["current_leaf_working_set"].insert(insert_at, V2_VERIFIER)
s["authority"]["EX2_01_replay_claim_id"] = V2
s["authority"]["EX2_01_replay_verifier_blob_sha1"] = V2_VERIFIER_BLOB
s["claim_sync"]["section_source_inventory_replay_version_migration"] = {
    "from_claim_id": V1,
    "to_claim_id": V2,
    "reason": "Preserve immutable V1 evidence while replacing a brittle wording-only replay assertion with an exact-status plus linearization/H0 semantic check.",
    "mathematical_statement_changed": False,
    "mathematical_credit_changed": False,
}
dump(STATE, s)

print("migrated EX2-01 replay V1->V2 without changing mathematical credit")
print("applied EX2-03D claim/state; current leaf EX2-03E")
