#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage32-ex2/EX2-03/zero-intersection-restriction-adapter-gap.json"
EX202 = ROOT / "stages/stage32-ex2/EX2-02/exact-fixed-component-extraction.json"
EX201 = ROOT / "stages/stage32-ex2/EX2-01/section-source-inventory.json"
EX200 = ROOT / "stages/stage32-ex2/EX2-00/v6-source-lock-target-contract.json"
V6 = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
AG = ROOT / "stages/stage32/residual-32-01-production/post1648ag-v6-known140-basis-elimination.json"

LOCKS = {
    EX202: "b07fd12a40acbfc478cdab472157cb4a34efe39c",
    EX201: "3f9ddf435093dfd681373a1e01f455d0db04642d",
    EX200: "b72b7582339d3933ac4485a1cf92c7be07809dc9",
    V6: "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
    AG: "e0bbe443919d1ec5424bffa84c1c5a79befbdf1e",
}
ZERO = [17, 21, 24, 25, 30, 31, 98]
EXPECTED_MULT = {17: 2, 21: 3, 24: 4, 25: 4, 30: 3, 31: 5, 98: 3}


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def main() -> None:
    for path, expected in LOCKS.items():
        assert blob(path) == expected, (path, blob(path), expected)

    cert = json.loads(CERT.read_text())
    ex2 = json.loads(EX202.read_text())
    ex1 = json.loads(EX201.read_text())
    ex0 = json.loads(EX200.read_text())
    v6 = json.loads(V6.read_text())
    ag = json.loads(AG.read_text())

    assert cert["schema"] == "STAGE32EX2_EX2_03_ZERO_INTERSECTION_RESTRICTION_GAP_V1"
    assert cert["status"] == "LEAF_BLOCKED_EXACT_RESTRICTION_ADAPTER_GAP_ROUTED_TO_SYMMETRY_DIVISOR_ORBIT_PREFLIGHT"
    assert ex0["V6_target"]["row_id"] == "g1-d186"
    assert ex1["exit"]["certified_section_subspace_dimension"] == 1
    assert ex2["exact_scan"]["zero_pairing_labels_1based"] == ZERO

    pairings = [int(x) for x in v6["witness"]["all140_pairings"]]
    zero = [i + 1 for i, x in enumerate(pairings) if x == 0]
    assert zero == ZERO
    zf = cert["zero_intersection_frontier"]
    assert zf["labels_1based"] == ZERO
    assert zf["pairings_with_V6"] == [pairings[i - 1] for i in ZERO] == [0] * 7

    decomp = {int(row["known140_label_1based"]): int(row["multiplicity"]) for row in ag["known140_monoid"]["decomposition"]}
    assert {i: decomp[i] for i in ZERO} == EXPECTED_MULT
    assert {int(k): int(v) for k, v in zf["known_member_multiplicities"].items()} == EXPECTED_MULT
    assert zf["all_seven_occur_in_retained_known140_effective_divisor"] is True
    assert zf["one_member_containment_proves_fixedness"] is False
    assert zf["zero_pairing_proves_fixedness"] is False
    assert zf["zero_pairing_proves_movingness"] is False

    locks = cert["source_locks"]["known140_decomposition"]
    assert locks["all140_retained_coordinates_sha256"] == ag["source_locks"]["all140_retained_coordinates_sha256"]
    assert locks["retained_picard_gram_sha256"] == ag["source_locks"]["retained_picard_gram_sha256"]
    assert "all140_retained_coordinates" not in ag
    assert "retained_picard_gram" not in ag

    ra = cert["restriction_adapter_audit"]
    assert ra["compact_known140_source_locks_full_coordinate_payload_by_hash"] is True
    assert ra["compact_known140_source_exposes_per_curve_picard64_coordinates"] is False
    assert ra["compact_known140_source_exposes_pairwise_7x7_intersection_matrix"] is False
    assert ra["current_working_set_exposes_exact_O_V6_restriction_class_on_each_zero_curve"] is False
    assert ra["current_working_set_exposes_H0_restriction_or_evaluation_map"] is False
    assert ra["current_working_set_exposes_complete_base_ideal"] is False
    assert ra["current_working_set_exposes_second_independent_V6_divisor"] is False
    assert ra["exact_7x7_matrix_replayable_from_current_working_set"] is False
    assert ra["divisorial_base_locus_classified"] is False

    gap = cert["exact_gap"]
    assert gap["missing_object"] == "COMPACT_ZERO_CURVE_RESTRICTION_OR_DIVISOR_ORBIT_ADAPTER"
    assert gap["pairwise_intersection_matrix_alone_would_not_prove_fixedness"] is True
    assert gap["block_is_stage_exhaustion"] is False

    route = cert["distinct_lane_route"]
    assert route["next_leaf"] == "EX2-03B_SYMMETRY_DIVISOR_ORBIT_PREFLIGHT"
    assert route["lane"] == "SYMMETRY_LANE"
    assert route["requires_line_bundle_linearization_for_divisor_level_member"] is False
    assert route["requires_exact_surface_automorphism"] is True
    assert route["requires_exact_V6_class_stabilization"] is True
    assert route["requires_exact_component_action"] is True
    assert route["absence_from_transformed_divisor_must_be_exact"] is True
    assert route["symmetry_eigenspace_or_H0_representation_claimed"] is False

    assert cert["exit"]["EX2_03_restriction_preflight_complete"] is True
    assert cert["exit"]["result"] == "EXACT_SCOPED_ADAPTER_GAP_NO_BASE_LOCUS_CREDIT"
    assert cert["exit"]["claim_dag_sync_triggered"] is False
    for key, value in cert["credit_firewall"].items():
        assert value is False, (key, value)

    stored = cert["canonical_sha256_without_this_field"]
    payload = dict(cert)
    payload.pop("canonical_sha256_without_this_field")
    assert csha(payload) == stored == "22b90a9facb7c2de7d69f8cfdfc36a90bbfb02680463b8a59066d16572b392f4"

    print("Stage32EX2 EX2-03 restriction preflight: PASS scoped blocker; seven V6-zero curves remain neither fixed nor moving, the compact working set lacks the exact restriction/7x7/base-ideal adapter, and routing advances to a divisor-level symmetry-orbit preflight with no new mathematical credit.")


if __name__ == "__main__":
    main()
