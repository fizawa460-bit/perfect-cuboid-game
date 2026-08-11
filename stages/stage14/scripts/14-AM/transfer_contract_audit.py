#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
contract = json.loads((ROOT / "data/14-AM/transfer_contract.json").read_text())

assert contract["stage"] == "Stage14-AM"
assert contract["classification"] == "BLOCKED"
assert contract["current_exponent"] == "1/2"
assert contract["strict_subsqrt_proved"] is False
assert "multiplicative_Folner_k_average_equals_primitive_k_1" in contract["failed"]
assert "uniform_fixed_power_aperiodic_decay" in contract["unverified"]
assert contract["ordinary_root_projector_terms"].startswith("phi(q)")
assert contract["gaussian_orientation_terms"].startswith("2^omega(q)")
assert contract["gaussian_orientation_l1_cost"] == "1"
assert contract["next_lemma"] == "Primitive Physical Hecke Adapter Lemma"

result = (ROOT / "14-AM/result.md").read_text()
for token in (
    "FINAL_CLASSIFICATION=BLOCKED",
    "APERIODIC_BRANCH_FIXED_POWER_SAVING=false",
    "PRETENTIOUS_SQRT_SATURATION_EXCLUDED=false",
    "Primitive Physical Hecke Adapter Lemma",
):
    assert token in result

print("STAGE14_AM_TRANSFER_CONTRACT_AUDIT=PASS")

