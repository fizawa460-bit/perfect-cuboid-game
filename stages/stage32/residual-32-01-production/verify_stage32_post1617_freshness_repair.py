#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import verify_stage32_post1588_hperp_nonexceptional_mod2_witness as base

HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1588-hperp-nonexceptional-mod2-witness.json"
EXPECTED_BASE_MAIN = "7ce9edb2652a044fd6140e0f45b87026eefcf319"
EXPECTED_CANONICAL = "6adc55114e29720f2a89649d71381228711a58b80677d3cc6b753f54daa4b8c8"


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    if cert["base_main_sha"] != EXPECTED_BASE_MAIN:
        raise SystemExit("post1617 freshness base moved")
    if cert["canonical_sha256_without_this_field"] != EXPECTED_CANONICAL:
        raise SystemExit("post1617 repaired canonical moved")

    base.EXPECTED_CANONICAL = EXPECTED_CANONICAL
    base.main()


if __name__ == "__main__":
    main()
