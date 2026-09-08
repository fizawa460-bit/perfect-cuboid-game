#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "e3-v91c1x-r5b2d1-source-bound-swap23-action-adapter.json"
R1 = HERE / "e3-v91c1x-r1-chain-level-action-difference-preflight.json"
C3 = HERE / "e3-v91c1x-r5b2c3-all-double-overlaps-317-cover.json"
DIAG = HERE / "diagnose_e3_v91c1r_swap23_boundary_function_package_transport.py"

R1_SHA = "b8e02dd9bf9971cb022d490dd5e6e7fcd9085e5a5e26be3a2bf1f75d6d384fcb"
C3_SHA = "a49f7a77ad9aad10714e556503dbd5a84585c8f1c92241b9213d3e439819ca50"
DIAG_BLOB = "5119c130cf9316efd666fd99410e7e58345d08a6"
PERM = [0, 2, 1, 3, 5, 4, 6]
NEXT_BLOCKER = "EXPLICIT_SWAP23_PULLBACK_OF_317_COVER_CHART_DOMAINS_AND_COMMON_REFINEMENT_INDEX_WITH_TRANSITION_COMPATIBILITY"


def csha(obj: object) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def embedded_lock(path: Path, expected: str, label: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    claimed = obj.get("canonical_sha256")
    body = dict(obj)
    body.pop("canonical_sha256", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise SystemExit(f"{label} canonical lock moved: {claimed} {actual}")
    return obj


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def replay() -> dict:
    if git_blob_sha(DIAG.read_bytes()) != DIAG_BLOB:
        raise SystemExit("literal transport diagnostic blob moved")
    run = subprocess.run([sys.executable, str(DIAG)], check=True, capture_output=True, text=True)
    rows = [json.loads(line) for line in run.stdout.splitlines() if line.startswith("{")]
    if len(rows) != 1:
        raise SystemExit("literal transport replay output moved")
    return rows[0]


def main() -> None:
    r1 = embedded_lock(R1, R1_SHA, "R1")
    c3 = embedded_lock(C3, C3_SHA, "C3")
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    claimed = cert.get("canonical_sha256")
    body = dict(cert)
    body.pop("canonical_sha256", None)
    if csha(body) != claimed:
        raise SystemExit("B2D1 canonical sha invalid")

    if cert["schema"] != "stage33.e3.v91c1x_r5b2d1.source_bound_swap23_action_adapter.v1":
        raise SystemExit("B2D1 schema moved")
    if cert["entry"]["authority"] != "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT":
        raise SystemExit("authority moved")
    if cert["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("Stage33 progress moved")
    if cert["source_locks"]["r1_chain_preflight_canonical_sha256"] != R1_SHA:
        raise SystemExit("R1 lock moved")
    if cert["source_locks"]["r5b2c3_canonical_sha256"] != C3_SHA:
        raise SystemExit("C3 lock moved")

    row = replay()
    if row["marker"] != "V91C1R_SWAP23_LITERAL_BOUNDARY_FUNCTION_PACKAGE_TRANSPORT_DIAGNOSTIC":
        raise SystemExit("literal transport marker moved")
    if row["q_word"] != ["swap12", "swap13", "swap12"]:
        raise SystemExit("source action word moved")
    if row["composed_coordinate_permutation"] != PERM:
        raise SystemExit("source-bound coordinate permutation moved")
    if row["composed_coordinate_action"] != "a2<->a3,b2<->b3,a1/b1/c fixed":
        raise SystemExit("source-bound coordinate action moved")

    action = cert["source_bound_action"]
    if action["word"] != row["q_word"]:
        raise SystemExit("certificate action word moved")
    if action["composed_coordinate_permutation_zero_based"] != PERM:
        raise SystemExit("certificate permutation moved")
    if action["literal_boundary_package_transport_replayed"] is not True:
        raise SystemExit("literal transport replay credit lost")
    if action["source_bound_coordinate_action_locator_materialized"] is not True:
        raise SystemExit("source-bound action adapter lost")
    if action["package_level_literal_closure"] is not False:
        raise SystemExit("R1 same-eight package closure firewall violated")
    if action["package_level_closure_required_for_action_adapter"] is not False:
        raise SystemExit("action adapter wrongly requires package closure")

    status = cert["construction_status"]
    if status["source_bound_swap23_coordinate_action_materialized"] is not True:
        raise SystemExit("source action status moved")
    if status["r5b2c3_317_chart_cover_available"] is not True:
        raise SystemExit("C3 cover status moved")
    for key in [
        "swap23_pullback_of_each_317_chart_domain_materialized",
        "cover_action_or_common_refinement_materialized",
        "same_representative_transport_materialized",
        "literal_mu2_2_cocycle_materialized",
        "equivalent_unimodular_cech_glue_materialized",
        "triple_overlap_action_difference_identity_verified",
    ]:
        if status[key] is not False:
            raise SystemExit(f"construction firewall violated: {key}")

    if cert["exact_consequence"]["previous_missing_source_action_locator_resolved"] is not True:
        raise SystemExit("resolved locator consequence moved")
    if cert["exact_consequence"]["next_blocker"] != NEXT_BLOCKER:
        raise SystemExit("next blocker moved")
    for key, value in cert["credit_firewall"].items():
        if value is not False:
            raise SystemExit(f"credit firewall violated: {key}")

    if r1["source_locks"]["swap23_literal_package_transport"] != "stages/stage33/33-12/diagnose_e3_v91c1r_swap23_boundary_function_package_transport.py":
        raise SystemExit("R1 transport locator moved")
    if c3["construction_status"]["swap23_cover_action_or_common_refinement_materialized"] is not False:
        raise SystemExit("C3 common-refinement firewall moved")

    print(json.dumps({
        "success": True,
        "marker": "V91C1X_R5B2D1_SOURCE_BOUND_SWAP23_ACTION_ADAPTER_VERIFIED",
        "certificate_sha256": claimed,
        "source_bound_coordinate_permutation": PERM,
        "next_blocker": NEXT_BLOCKER,
        "stage33_progress": "6/11",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
