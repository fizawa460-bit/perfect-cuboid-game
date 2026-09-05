#!/usr/bin/env python3
"""Verify V91C1C user-authorized merged-route Stage33 MAIN startup."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

H = Path(__file__).resolve().parents[1]
D = H / "33-12"
STATE = H / "MAIN-STATE.json"
V91C1C = D / "e3-v91c1c-a2-02-strict-transform-prime-refinement.json"
STATE_SHA = "17497a9498ab43ef0d15f0c9a80f099605add68ec98ab4b2fe57c2e712c1862b"
V91C1C_SHA = "ac46916c7e46d3f5b6ac67125b4622d4e4aaa028509879d45811f0e4ec8f28f6"
NEXT = "V91C1D_MATERIALIZE_A2_02_PURITY_OFFBOUNDARY_CORRECTION_AND_PRIME_LEVEL_CECH_CARTIER_TRANSITION_DATA"


def csha(o): return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def load(path, expected):
    o=json.loads(path.read_text(encoding="utf-8")); b=dict(o); h=b.pop("canonical_sha256")
    assert h==expected==csha(b); return o

s=load(STATE, STATE_SHA); c=load(V91C1C, V91C1C_SHA)
p=s["continuation_provenance"]
assert s["schema"]=="STAGE33_MAIN_COMPACT_STATE_V33_V91C1C_USER_AUTHORIZED_MERGED_ROUTE"
assert s["authority_sync"]["frontier_authority"]=="V91C1C_A2_02_STRICT_TRANSFORM_PRIME_REFINEMENT"
assert p["v91c1c_pr"]==1620 and p["merged_head"]=="75585168c54241591fb29c9271b64e1e95d1f1f6"
assert p["merge_commit"]=="e2103a2de367a0a6d0826b044b6bb83d24ad6f6f"
assert p["user_authorized_merge"] is True and p["user_judged_mathematics_pass"] is True
assert p["hostile_audit_pass_claimed"] is False and p["theorem_credit_from_user_authorized_merge"] is False
assert c["exact_consequence"]["resolved_full_surface_height_one_attachment_for_a2_02_complete"] is True
assert c["exact_consequence"]["prime_level_cc_ct_transport_complete"] is True
assert c["exact_consequence"]["purity_offboundary_correction_materialized"] is False
assert s["current"]["next_exact_leaf"]==NEXT and s["execution_gate"]["advance_allowed"] is True
assert s["stage33_progress"]=="6/11" and s["firewalls"]["merge_allowed"] is False
print(json.dumps({"success":True,"marker":"V96_V91C1C_USER_AUTHORIZED_MERGED_ROUTE_STARTUP","state_sha256":STATE_SHA,"v91c1c_sha256":V91C1C_SHA,"next_exact_leaf":NEXT,"hostile_audit_pass_claimed":False},sort_keys=True))
