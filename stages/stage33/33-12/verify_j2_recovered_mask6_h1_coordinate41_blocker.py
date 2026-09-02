#!/usr/bin/env python3
"""Replay the recovered mask-6 candidate H1-coordinate-41 blocker exactly.

This does not source-lock the named J2 order-4 lift and therefore does not
promote mask 6 as the named source.  It only converts the recovered H1/raw-ct
diagnostic into a deterministic certificate against the current locked inputs.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-recovered-mask6-h1-coordinate41-blocker.json"
AUDIT = HERE / "audit_v4_kummer_extension_space_after_j2_anchor.py"


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


cert = json.loads(CERT.read_text(encoding="utf-8"))
body = dict(cert)
claimed = body.pop("canonical_sha256")
assert claimed == "b32efc97dcb2c19ec8fca4017e2d21712a3635031665f89cc7ac62a77edb4095"
assert csha(body) == claimed

# Reuse the exact all-extension audit.  Its stdout is intentionally suppressed;
# this verifier exposes only the compact separating witness.
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(AUDIT))

result = ns["result"]
j2_reachable = ns["j2_reachable"]
j2_h1 = ns["j2_h1"]
j2_retained_mask = ns["j2_retained_mask"]
projection_basis = ns["projection_basis"]
NP = ns["NP"]

coord0 = cert["exact_h1_blocker"]["separating_coordinate_1based"] - 1
assert coord0 == 40
assert j2_retained_mask == cert["candidate_scope"]["retained10_mask_decimal"] == 6
assert len(j2_reachable) == cert["exact_h1_blocker"]["reachable_H1_subspace_dimension_f2"] == 13
assert ns["j2_target_reachable"] is False
assert ((j2_h1 >> coord0) & 1) == cert["exact_h1_blocker"]["locked_target_coordinate_value"] == 1
assert all(((row >> coord0) & 1) == 0 for row in j2_reachable.values())
assert cert["exact_h1_blocker"]["reachable_subspace_coordinate_value"] == 0
assert result["locked_named_j2"]["locked_target_reachable_from_locked_source"] is False
assert result["source_locks"] == cert["source_locks"]

# Coordinate 41's locked H1 representative is exactly the recovered raw-ct
# support [9,11,19], with zero raw-cc half.
_, _, h1_representatives = projection_basis()
rep41 = h1_representatives[coord0]
assert len(rep41) == 2 * NP
cc_support = [i + 1 for i, bit in enumerate(rep41[:NP]) if bit]
ct_support = [i + 1 for i, bit in enumerate(rep41[NP:]) if bit]
assert cc_support == cert["raw_ct_support_recovery"]["raw_cc_support_indices_1based"] == []
assert ct_support == cert["raw_ct_support_recovery"]["raw_ct_support_indices_1based"] == [9, 11, 19]
assert cert["raw_ct_support_recovery"]["replayed_by_this_certificate"] is True

# Semantic firewall: exact diagnostic replay is not source-label authority.
assert cert["candidate_scope"]["named_J2_source_selected"] is False
assert cert["firewall"]["named_J2_mask6_promoted"] is False
assert cert["firewall"]["named_order4_two_bit_value_source_locked"] is False
assert cert["firewall"]["named_order4_actual_s3_behavior_source_locked"] is False
assert cert["firewall"]["stage33_12_closed_exact"] is False

print(json.dumps({
    "success": True,
    "status": cert["status"],
    "candidate_retained10_mask_decimal": j2_retained_mask,
    "reachable_H1_dimension_f2": len(j2_reachable),
    "separating_coordinate_1based": coord0 + 1,
    "target_bit": (j2_h1 >> coord0) & 1,
    "reachable_subspace_bit": 0,
    "coordinate41_raw_cc_support_1based": cc_support,
    "coordinate41_raw_ct_support_1based": ct_support,
    "named_J2_mask6_promoted": False,
    "canonical_sha256": claimed,
}, sort_keys=True))
