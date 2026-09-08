#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CERT = HERE / "ex4-02-source-inventory-exact-product-binding-scratch.json"
EXPECTED_CANONICAL = "87dbeac32d29fc3a0bb15bbd3e4df875f47f287cf085abe588420d6095306293"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert claimed == got
    return got


doc = json.loads(CERT.read_text())
assert doc["schema"] == "STAGE32EX4_EX4_02_SOURCE_INVENTORY_EXACT_PRODUCT_BINDING_SCRATCH_V1"
assert canonical(doc) == EXPECTED_CANONICAL
assert doc["status"] == "SCRATCH_REPLAYABLE_BOUNDED_SOURCE_INVENTORY_NOT_RETAINED_AUTHORITY"

for name, lock in doc["repo_source_locks"].items():
    path = ROOT / lock["path"]
    assert path.is_file(), (name, lock["path"])
    assert blob_sha1(path) == lock["blob_sha1"], (name, "blob")
    if "canonical_sha256" in lock:
        src = json.loads(path.read_text())
        assert canonical(src) == lock["canonical_sha256"], (name, "canonical")

target = doc["target_contract"]
assert target["source_product"] == "phi2*phi6"
assert target["source_product_unique_fixed_pair"] == "Z3={0,infinity}"
assert target["retained_candidate_product"] == "S*T^-1"
assert target["retained_candidate_unique_fixed_W_line"] == "L2"
assert target["conditional_line_to_residue"] == {"L2": 97}
assert target["conditional_only"] is True

inventory = {x["source_id"]: x for x in doc["external_source_inventory"]}
cecotti = inventory["CECOTTI_2509_24605V1_APPENDIX_B"]
assert cecotti["classification"] == "REQUIRES_ADAPTER"
assert any("S=b4" in x and "T=-b3" in x for x in cecotti["locators"])
assert "the exact product binding phi2*phi6 -> S*T^-1" in cecotti["does_not_provide"]

krr = inventory["KRR_1904_00793V4_SECTION4"]
assert krr["classification"] == "REQUIRES_ADAPTER"
assert any("H48=gG48g^-1" in x for x in krr["locators"])
assert "an explicit mod-2 matrix for g on J[2]" in krr["does_not_provide"]

matrix = doc["source_to_required_datum_matrix"]
assert len(matrix) >= 6
assert all(row["selects_unique_W_line_now"] is False for row in matrix)

bounded = doc["bounded_inventory_conclusion"]
assert bounded["current_frozen_package_exact_product_binding_found"] is False
assert bounded["current_frozen_package_absolute_W_line_selected"] is False
assert bounded["current_frozen_package_absolute_Q602_residue_selected"] is False
assert bounded["bounded_only_not_literature_wide_absence"] is True

lanes = {x["lane"] for x in doc["legal_next_construction_lanes"]}
assert "DERAUX_KRR_EXPLICIT_G_MOD2_LANE" in lanes
assert "CECOTTI_PERIOD_HOMOLOGY_MARKING_LANE" in lanes
assert "FSM_THETA_LEVEL_TO_PRINCIPAL_G12_LANE" in lanes

decision = doc["decision"]
assert decision["result"] == "EX4_02_CURRENT_FROZEN_SOURCE_INVENTORY_DOES_NOT_YET_SUPPLY_EXACT_PRODUCT_BINDING"
assert decision["next_leaf"] == "EX4-03_DERAUX_KRR_EXPLICIT_G_MOD2_PREFLIGHT"
assert decision["recommended_first_lane"] == "DERAUX_KRR_EXPLICIT_G_MOD2_LANE"
assert decision["retained_claim_dag_sync_performed"] is False
for key in (
    "absolute_W_line_identified",
    "absolute_Q602_residue_identified",
    "Q602_excluded",
    "O210_excluded",
    "stage32_main_credit",
):
    assert decision[key] is False, key

assert not any(doc["firewalls"].values())

print("STAGE32EX4_EX4_02_SOURCE_INVENTORY_COMPLETE")
print(f"certificate_canonical={EXPECTED_CANONICAL}")
print("cecotti=requires_adapter krr=requires_adapter exact_product_binding=false")
print("absolute_W_line=false absolute_Q602_residue=false Q602_excluded=false O210_excluded=false")
print("next=EX4-03_DERAUX_KRR_EXPLICIT_G_MOD2_PREFLIGHT")
