#!/usr/bin/env python3
"""Validate Stage14-t57 generated audit against frozen boundary summary."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
GEN = ROOT / "stages/stage14/data/14-t57/rank1_kummer_mellin.json"
FROZEN = ROOT / "stages/stage14/data/14-t57/rank1_kummer_mellin_frozen.json"
RESULT = ROOT / "stages/stage14/14-t57/result.md"


def main() -> None:
    g = json.loads(GEN.read_text())
    f = json.loads(FROZEN.read_text())
    result = RESULT.read_text()

    assert g["stage"] == f["stage"] == "14-t57"
    assert g["split_primes"] == f["split_primes"]
    assert sum(r["ratio_product_checks"] for r in g["prime_rows"]) == f["ratio_product_checks"]
    assert sum(r["cayley_checks"] for r in g["prime_rows"]) == f["cayley_checks"]
    assert sum(r["mellin_kernel_checks"] for r in g["prime_rows"]) == f["mellin_kernel_checks"]
    assert g["crt_pair_count"] == f["crt_pair_checks"]
    assert g["ratio_product_identity"] == f["ratio_product_identity"]
    assert g["mellin_packet_l2_bound"] == f["mellin_packet_l2_energy"]

    for key, value in f.items():
        if key in g["decision"]:
            assert g["decision"][key] == value, key

    assert "STAGE14_T57=COMPLETE_RANK1_KUMMER_MELLIN_ADAPTER_AND_PHYSICAL_SELECTOR_CORRELATION_BOUNDARY" in result
    assert "FIXED_U_ONE_FIELD_RANK1_KUMMER_CERTIFICATE_PROVED=true" in result
    assert "FIXED_U_ALL_ORDER_MELLIN_PACKET_PROVED=true" in result
    assert "TWO_PRIME_KERNEL_SPECTRAL_REASSEMBLY_FIXED_POWER_LOSS=0" in result
    assert "SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED=false" in result
    assert "TH16_NEEDED=false" in result
    print("Stage14-t57 frozen validation: PASS")


if __name__ == "__main__":
    main()
