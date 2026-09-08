#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage32-ex2/EX2-02/exact-fixed-component-extraction.json"
EX200 = ROOT / "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json"
EX201 = ROOT / "stages/stage32-ex2/EX2-01/section-source-inventory.json"
V6 = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
AG = ROOT / "stages/stage32/residual-32-01-production/post1648ag-v6-known140-basis-elimination.json"

LOCKS = {
    EX200: "b72b7582339d3933ac4485a1cf92c7be07809dc9",
    EX201: "3f9ddf435093dfd681373a1e01f455d0db04642d",
    V6: "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
    AG: "e0bbe443919d1ec5424bffa84c1c5a79befbdf1e",
}


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    for path, expected in LOCKS.items():
        actual = blob(path)
        assert actual == expected, (path, actual, expected)

    cert = json.loads(CERT.read_text())
    ex0 = json.loads(EX200.read_text())
    ex1 = json.loads(EX201.read_text())
    v6 = json.loads(V6.read_text())
    ag = json.loads(AG.read_text())

    assert cert["schema"] == "STAGE32EX2_EX2_02_EXACT_FIXED_COMPONENT_EXTRACTION_V1"
    assert cert["status"] == "PASS_BOUNDED_NEGATIVE_INTERSECTION_SCAN_EMPTY_NO_FIXED_PART_CLASSIFICATION"
    assert cert["target"]["divisor_class"] == "V6"
    assert ex0["V6_target"]["row_id"] == "g1-d186"
    assert ex1["exit"]["next_leaf"] == "EX2-02_EXACT_FIXED_COMPONENT_EXTRACTION"

    assert v6["canonical_sha256_without_this_field"] == "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    assert len(pairings) == 140
    assert csha(pairings) == v6["witness"]["all140_pairings_sha256"]
    assert v6["witness"]["all140_pairings_sha256"] == cert["exact_scan"]["all140_pairings_sha256"]

    assert ag["exact_reduction"]["v6_all140_pairing_replay_exact"] is True
    assert ag["known140_monoid"]["all140_pairing_reconstruction_exact"] is True
    assert ag["source_locks"]["v6_witness_blob_sha1_expected"] == LOCKS[V6]
    assert ag["source_locks"]["v6_witness_canonical_sha256"] == v6["canonical_sha256_without_this_field"]

    negative = [i + 1 for i, x in enumerate(pairings) if x < 0]
    zero = [i + 1 for i, x in enumerate(pairings) if x == 0]
    positive = [i + 1 for i, x in enumerate(pairings) if x > 0]

    scan = cert["exact_scan"]
    assert scan["pairing_count"] == len(pairings) == 140
    assert scan["minimum_pairing"] == min(pairings) == 0
    assert scan["maximum_pairing"] == max(pairings) == 56
    assert scan["negative_labels_1based"] == negative == []
    assert scan["negative_pairing_count"] == len(negative) == 0
    assert scan["zero_pairing_labels_1based"] == zero == [17, 21, 24, 25, 30, 31, 98]
    assert scan["zero_pairing_count"] == len(zero) == 7
    assert scan["positive_pairing_count"] == len(positive) == 133
    assert scan["scan_exact"] is True

    fx = cert["fixed_component_extraction"]
    assert fx["negative_seed_set_empty"] is True
    assert fx["iterative_subtraction_entered"] is False
    assert fx["new_forced_fixed_components_certified_by_this_gate"] == 0
    assert fx["new_forced_fixed_multiplicities"] == []
    assert fx["residual_after_certified_subtractions"] == "D=V6"
    assert fx["residual_is_proved_moving_part"] is False
    assert fx["known140_fixed_part_proved_zero"] is False
    assert fx["full_fixed_part_proved_zero"] is False

    unresolved = cert["unresolved"]
    assert unresolved["fixed_part_fully_classified"] is False
    assert unresolved["zero_pairing_labels_are_not_proved_fixed_or_moving"] == zero
    assert unresolved["positive_pairing_does_not_by_itself_rule_out_fixedness"] is True
    assert unresolved["retained_known140_is_not_asserted_exhaustive_for_all_possible_fixed_curves"] is True
    assert unresolved["curves_outside_retained_known140_remain_uncontrolled"] is True
    assert unresolved["one_known140_reducible_member_is_not_promoted_to_fixed_part"] is True

    exit_ = cert["exit"]
    assert exit_["EX2_02_complete"] is True
    assert exit_["bounded_negative_intersection_gate_closed"] is True
    assert exit_["next_leaf"] == "EX2-03_BASE_LOCUS_AND_MOVING_SYSTEM_STRUCTURE"

    assert cert["claim_sync"]["trigger"] == "RETAINED_CONSOLIDATION"
    assert cert["claim_sync"]["status"] == "PENDING_CURRENT_MAIN_RECONCILIATION"
    assert cert["claim_sync"]["required_before_checkpoint_is_claim_dag_complete"] is True

    for key, value in cert["credit_firewall"].items():
        assert value is False, (key, value)

    stored = cert["canonical_sha256_without_this_field"]
    payload = dict(cert)
    payload.pop("canonical_sha256_without_this_field")
    assert csha(payload) == stored

    print(
        "Stage32EX2 EX2-02 fixed-component extraction: PASS; all 140 exact V6 intersections are nonnegative, so the D.E<0 gate certifies no fixed component, does not prove the fixed part empty, and leaves claim-DAG consolidation pending current-main reconciliation."
    )


if __name__ == "__main__":
    main()
