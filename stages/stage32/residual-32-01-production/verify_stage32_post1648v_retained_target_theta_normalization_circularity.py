#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648v-retained-target-theta-normalization-circularity.json"
EXPECTED = "17f53e4ee5d2eb632b9c1e6c188fd9d0ab3ae36de5681df508df09c0e25de351"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()
    assert claimed == got
    return got


cert = json.loads(CERT_PATH.read_text())
assert canonical(cert) == EXPECTED

for name, lock in cert["source_locks"].items():
    path = ROOT / lock["path"]
    assert path.is_file(), name
    assert blob_sha1(path) == lock["git_blob_sha1"], name
    if "canonical_sha256" in lock:
        doc = json.loads(path.read_text())
        assert canonical(doc) == lock["canonical_sha256"], name

for name, lock in cert["policy_locks"].items():
    path = ROOT / lock["path"]
    assert path.is_file(), name
    assert blob_sha1(path) == lock["git_blob_sha1"], name

u = json.loads((ROOT / cert["source_locks"]["post1648U"]["path"]).read_text())
assert u["decision"]["explicit_delta0inf_source_vector_obtained"] is True
assert u["decision"]["absolute_delta0inf_retained_W_line_identified"] is False
assert u["decision"]["survivors_current_credit"] == [73, 97, 235]

test = cert["target_theta_normalization_test"]
assert test["source_delta0inf_half_period_explicit_from_post1648U"] == [0, 0, 1, 1]
assert test["krr_theta_divisor_embedding_explicit_before_target_identification"] is True
assert test["krr_theta_embedding_contains_origin_and_weierstrass_2torsion"] is True
assert test["bridge"] == "H48=g G48 g^-1"
assert test["explicit_g_matrix_or_A2_action_materialized_at_checked_locator"] is False
assert test["krr_composes_theta_embedding_with_g_before_identifying_H48_with_G48"] is True
assert test["theta_embedding_in_retained_G48_coordinates_materialized_independently_of_g"] is False
assert test["cecotti_specific_target_half_characteristic_in_retained_basis_selected"] is False
assert test["target_non_conjugacy_invariant_selector_materialized"] is False

audit = cert["cycle_exploration_audit"]
assert audit["triggered"] is True
assert audit["blind_rediscovery_before_arsenal"] is True
assert audit["arsenal_comparison_after_blind_pass"]["card"] == "S30-W01"
assert audit["CYCLE_ROUTE_STATUS"] == "BLOCKED_NEW_PATTERN_ISOLATED"
assert audit["CYCLE_ACTIVE_RECEIVER"] == "ABSOLUTE_DELTA0INF_RETAINED_W_LINE"
assert audit["CYCLE_UNTESTED_CANDIDATES"] == 3
assert audit["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert audit["CYCLE_BLIND_REDISCOVERY"] is True
assert audit["CYCLE_SPLIT_TRIGGERED"] is False
assert audit["CYCLE_PARKING_AUDIT_COMPLETE"] is False

ledger = {row["candidate"]: row["status"] for row in audit["candidate_ledger"]}
assert ledger["KRR theta-divisor normalization transported into retained coordinates"] == "BLOCKED"
assert ledger["actual marked ppav isomorphism / conjugating g from an external source"] == "UNTESTED"
assert ledger["explicit target half-characteristic or semicharacter in retained lattice basis"] == "UNTESTED"
assert ledger["new common branch-labelled source/target geometric anchor"] == "UNTESTED"

dec = cert["decision"]
assert dec["retained_cecotti_krr_target_theta_selector_route_closed_bounded"] is True
assert dec["global_nonexistence_of_marked_ppav_adapter_claimed"] is False
assert dec["explicit_marked_ppav_isomorphism_source_bound"] is False
assert dec["absolute_delta0inf_retained_W_line_identified"] is False
assert dec["survivors_current_credit"] == [73, 97, 235]
assert dec["Q602_excluded"] is False
assert dec["O210_excluded"] is False
assert dec["O212_plus_advance_allowed"] is False

assert not any(cert["firewalls"].values())

note = (ROOT / cert["source_locks"]["source_note"]["path"]).read_text()
for needle in (
    "H48 = g G48 g^-1",
    "composing it with this `g`",
    "circular",
    "Appell–Humbert",
    "S30-W01",
    "UNTESTED",
    "No receiver is parked",
):
    assert needle in note

print("POST1648V_RETAINED_TARGET_THETA_NORMALIZATION_CIRCULARITY_COMPLETE")
print(f"certificate_canonical={EXPECTED}")
print("krr_theta_explicit=true retained_coordinate_theta_without_g=false")
print("target_selector_materialized=false bounded_source_negative=true")
print("breadth_audit=true blind_rediscovery=true untested_candidates=3 parking=false")
print("current_survivors=73,97,235 Q602_excluded=false O210_excluded=false")
