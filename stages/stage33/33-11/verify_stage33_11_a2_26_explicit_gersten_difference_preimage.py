#!/usr/bin/env python3
"""Independent structural verifier for the A2_26 Gersten-difference preimage."""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
MATERIALIZER = HERE / "materialize_stage33_11_a2_26_explicit_gersten_difference_preimage.py"
OUT = HERE / "stage33-11-a2-26-explicit-gersten-difference-preimage.json"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


# Recompute from the locked upstream artifacts, rather than trusting a stored JSON.
ns = runpy.run_path(str(MATERIALIZER))
cert = ns["cert"]
stored = json.loads(OUT.read_text(encoding="utf-8"))
if stored != cert:
    raise SystemExit("stored Gersten-difference preimage differs from fresh recomputation")
body = dict(stored)
claimed = body.pop("canonical_sha256")
if csha(body) != claimed:
    raise SystemExit("Gersten-difference preimage canonical hash mismatch")
if stored["repair_frontier"]["ambient_function_package_difference_before_purity_correction_is_zero"] is not True:
    raise SystemExit("ambient function package difference regression")
if stored["repair_frontier"]["height_one_prime_valuation_attachment_materialized"] is not False:
    raise SystemExit("verifier refuses an unverified valuation attachment")
if stored["repair_frontier"]["cc_ct_five_bit_vector_materialized"] is not False:
    raise SystemExit("five bits must remain withheld until valuation attachment is exact")
if stored["repair_frontier"]["exact_progress"] != "0/26":
    raise SystemExit("hostile-audit exact progress firewall moved")
for key in (
    "merge_allowed",
    "advance_allowed",
    "stage33_12_released",
    "stage33_08_released",
    "theorem_credit",
    "endpoint_credit",
):
    if stored["firewalls"][key] is not False:
        raise SystemExit(f"firewall moved: {key}")
print(
    json.dumps(
        {
            "success": True,
            "certificate_sha256": claimed,
            "ambient_pre_correction_difference": "ZERO_EXACT",
            "five_bits": "WITHHELD_EXACTLY",
            "blocker": stored["repair_frontier"]["blocker_code"],
            "exact_progress": "0/26",
        },
        indent=2,
        sort_keys=True,
    )
)
