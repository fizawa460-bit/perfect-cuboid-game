#!/usr/bin/env python3
"""Replay the V7 K_c test with the historical c-sign lock interpreted correctly.

The retained endpoint field `picard_sign_rows_sha256.c` is the canonical SHA256
of the historical `picard-action-sign-c.json` certificate, not a SHA256 of the
bare 64x64 matrix payload.  V7 incorrectly compared that certificate SHA to a
canonical hash of the fresh matrix rows.  This wrapper keeps the endpoint
certificate lock, independently locks the nonexpiring retained seven-sign
bundle, and requires the freshly materialized Magma c-sign matrix to equal the
retained c-sign matrix literally before the V7 exact pushforward calculation
continues.
"""
from __future__ import annotations

import json
from pathlib import Path

import diagnose_stage32_post1473_kc_pinned_replay_v7 as v7

RETAINED_SIGN_BUNDLE_EXPECTED = "5cd64ca89ee9f3ec76d275bc4082349764ac8a5cb4647a9bb9a4eaf267b76ab9"
RETAINED_C_CERTIFICATE_EXPECTED = "65f90a3356941bd4bdaeb77cfc3a8c5370d5726e2f66e2eb348bf5f9633af43a"


def install_retained_sigma_c_lock() -> None:
    repo = Path(__file__).resolve().parents[3]
    retained = v7.v6.base.load_module(
        repo / "stages/stage33/33-07/picard_coordinate_sign_rows_retained.py",
        "stage32_kc_retained_coordinate_signs_v8",
    ).load()
    if retained.get("canonical_sha256") != RETAINED_SIGN_BUNDLE_EXPECTED:
        raise ValueError("retained seven-sign Picard bundle canonical lock moved")
    if retained.get("coordinate_order") != ["a1", "a2", "a3", "b1", "b2", "b3", "c"]:
        raise ValueError("retained seven-sign coordinate order moved")
    if retained.get("action_certificate_sha256", {}).get("c") != RETAINED_C_CERTIFICATE_EXPECTED:
        raise ValueError("retained c-sign certificate canonical lock moved")
    if v7.SIGMA_C_PICARD_ROWS_EXPECTED != RETAINED_C_CERTIFICATE_EXPECTED:
        raise ValueError("V7 endpoint c-sign certificate lock moved")

    endpoint = json.loads(
        (repo / "stages/stage33/33-07/retained-q256-geometric-sign-endpoint.json").read_text()
    )
    if endpoint.get("canonical_sha256") != v7.ENDPOINT_EXPECTED:
        raise ValueError("retained geometric-sign endpoint canonical lock moved")
    if endpoint.get("source_locks", {}).get("picard_sign_rows_sha256", {}).get("c") != RETAINED_C_CERTIFICATE_EXPECTED:
        raise ValueError("endpoint c-sign certificate lock moved")

    retained_rows = [
        [int(a) for a in row]
        for row in retained.get("picard_actions_64x64", {}).get("c", [])
    ]
    if len(retained_rows) != 64 or any(len(row) != 64 for row in retained_rows):
        raise ValueError("retained c-sign Picard64 matrix shape moved")
    retained_rows_sha = v7.v6.base.csha(retained_rows)

    original = v7.compact_materialize

    def locked_materialize(repo_arg: Path, epi0: list[int]) -> dict:
        # V7's internal bare-row check is retained, but supplied the actual
        # bare-row SHA derived from the canonical retained matrix bundle.
        certificate_lock = v7.SIGMA_C_PICARD_ROWS_EXPECTED
        v7.SIGMA_C_PICARD_ROWS_EXPECTED = retained_rows_sha
        try:
            materialized = original(repo_arg, epi0)
        finally:
            v7.SIGMA_C_PICARD_ROWS_EXPECTED = certificate_lock
        if materialized["sigma_rows"] != retained_rows:
            raise ValueError("fresh Magma c-sign Picard64 matrix differs from retained matrix literally")
        materialized["retained_sigma_c_bundle_canonical_sha256"] = RETAINED_SIGN_BUNDLE_EXPECTED
        materialized["retained_sigma_c_certificate_canonical_sha256"] = RETAINED_C_CERTIFICATE_EXPECTED
        materialized["retained_sigma_c_bare_rows_sha256"] = retained_rows_sha
        return materialized

    v7.compact_materialize = locked_materialize


if __name__ == "__main__":
    install_retained_sigma_c_lock()
    v7.main()
