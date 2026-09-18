#!/usr/bin/env python3
import hashlib
import json

H = 96
EXPECTED_TOTAL_MASS = 174_683_387_305
EXPECTED_TOTAL_BCT_CELLS = 453_937
PER_B_CAP = 16 * 1024
SHARD_CAP = 32 * 1024
PARENT_CAP = 64 * 1024
SHA = "f" * 64
I128 = "9" * 39

SHARDS = [
    (0, 11), (12, 23), (24, 35), (36, 47),
    (48, 59), (60, 71), (72, 83), (84, 96),
]
SHARD_STATE_COUNTS = [249095, 345921, 409990, 473976, 537010, 600154, 663730, 790834]
SHARD_CELL_COUNTS = [31590, 38598, 45510, 52422, 59334, 66246, 73158, 87079]


def canonical_b_mass_and_cells(b: int):
    mass = 0
    cells = 0
    for c in range(H + 1):
        for t in range(b + c + 1):
            if (c + t) & 1:
                continue
            ulo = max(0, t - c)
            uhi = min(b, t)
            if ulo > uhi:
                continue
            cellmass = 0
            for u in range(ulo, uhi + 1):
                v = t - u
                w = c - t + u
                x5 = b - u

                # x0 < x1 branch.  For fixed u,v, x0 ranges through the
                # canonical triangle and (x8,x10) contributes w+1 splits.
                m = min(v, u - 1)
                count_neq = (
                    (w + 1) * ((m + 1) * u - m * (m + 1) // 2)
                    if m >= 0 else 0
                )

                # x0 = x1 branch with the retained lexicographic canonical rule.
                L = x5 + (1 if v > u else 0)
                count_eq = (min(u, v) + 1) * max(0, w - L + 1)
                cellmass += count_neq + count_eq

            if cellmass:
                cells += 1
                mass += cellmass
    return mass, cells


def encoded(obj):
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()


per_b = [canonical_b_mass_and_cells(b) for b in range(H + 1)]
assert sum(m for m, _ in per_b) == EXPECTED_TOTAL_MASS
assert sum(c for _, c in per_b) == EXPECTED_TOTAL_BCT_CELLS
assert per_b[0] == (76097, 2305)
assert per_b[96] == (6150481225, 7009)

# This is a storage-width sentinel, not a FULL178 mathematical result.  It uses
# actual retained b=96 routing topology where already known and deliberately
# maximal-width i128/hash fields for values that only the eventual heavy run
# may fill.  The future workflow must reject any persisted compact certificate
# that exceeds the hard class cap below.
per_b_sentinel = {
    "schema": "STAGE32_BR204_PER_B_CERTIFICATE_V1",
    "status": "WIDTH_SENTINEL_NOT_MATHEMATICAL_RESULT",
    "b": 96,
    "compact_state_count": 63094,
    "bct_cell_count": per_b[96][1],
    "population_multiplicity": per_b[96][0],
    "k8": {
        "retained_q_levels": 439932,
        "retained_parity_buckets": 1011820,
        "summary_sha256": SHA,
    },
    "picard_mu": {
        "mu_table_sha256": "f8570c9b045c204d55231cd855832648dbac1f26244c9581855f21cf4f8b6dbb",
        "terminal_syndrome_sha256": "2456dba5d197737eaa6be0e0a83bbe8087dcea638d4a50c2f2ef737bfdbd6a31",
        "mu_histogram": {"0": I128, "1": I128, "2": I128},
        "summary_sha256": SHA,
    },
    "capacity_bin_map": {
        "bin_count": 99999999,
        "commitment_sha256": SHA,
    },
    "br202_baseline_objective_contribution": {
        "numerator": I128,
        "denominator": I128,
    },
    "br203_mu_objective_contribution": {
        "numerator": I128,
        "denominator": I128,
    },
    "deterministic_stream_sha256": SHA,
    "source_locks": {
        "compressed_terminal_family_blob": "90ff82ed312dcc0cb32cf207935945f550e29170",
        "full178_production_state_blob": "931e80ba892ec0d98f3e7b909ac2dd46660c116c",
        "compact_producer_blob": "336285a0c204276e40da57a63ab634e88dae2b88",
        "compact_mu_equivalence_blob": "b7fc7e0c6c889c92cb152d4e8b54d05d2b71a5d1",
        "compact_equivalence_result_blob": "a0d193e44f59c50a69586124e65903db4b4ed9ce",
    },
    "completion_status": True,
}
per_b_bytes = len(encoded(per_b_sentinel))
assert per_b_bytes < PER_B_CAP

# The largest scheduling group has 13 b-units.  Its persisted summary records
# unit commitments, not raw state maps.
lo, hi = SHARDS[-1]
shard_sentinel = {
    "schema": "STAGE32_BR204_SHARD_SUMMARY_V1",
    "status": "WIDTH_SENTINEL_NOT_MATHEMATICAL_RESULT",
    "shard": 7,
    "b_lo": lo,
    "b_hi": hi,
    "unit_count": hi - lo + 1,
    "compact_state_count": SHARD_STATE_COUNTS[-1],
    "bct_cell_count": SHARD_CELL_COUNTS[-1],
    "population_multiplicity": sum(per_b[b][0] for b in range(lo, hi + 1)),
    "unit_certificate_sha256": [SHA for _ in range(lo, hi + 1)],
    "capacity_bin_union_commitment_sha256": SHA,
    "br202_baseline_objective_contribution": {"numerator": I128, "denominator": I128},
    "br203_mu_objective_contribution": {"numerator": I128, "denominator": I128},
    "stream_union_sha256": SHA,
    "source_lock_manifest_sha256": SHA,
    "completion_status": True,
}
shard_bytes = len(encoded(shard_sentinel))
assert shard_bytes < SHARD_CAP

parent_sentinel = {
    "schema": "STAGE32_BR204_PARENT_MANIFEST_V1",
    "status": "WIDTH_SENTINEL_NOT_MATHEMATICAL_RESULT",
    "complete_b_values": list(range(97)),
    "shard_ranges": [{"b_lo": lo, "b_hi": hi} for lo, hi in SHARDS],
    "shard_certificate_sha256": [SHA for _ in SHARDS],
    "routing_state_count": 4070710,
    "routing_bct_cells": EXPECTED_TOTAL_BCT_CELLS,
    "routing_assignment_mass": EXPECTED_TOTAL_MASS,
    "coverage_sha256": SHA,
    "population_conservation": True,
    "br203_never_exceeds_br202": True,
    "final_bin_union_commitment_sha256": SHA,
    "br202_final_objective": {"numerator": I128, "denominator": I128},
    "br203_final_objective": {"numerator": I128, "denominator": I128},
    "source_lock_manifest_sha256": SHA,
    "completion_status": True,
}
parent_bytes = len(encoded(parent_sentinel))
assert parent_bytes < PARENT_CAP

projected_peak = 97 * PER_B_CAP + 8 * SHARD_CAP + PARENT_CAP
assert projected_peak < 500 * 1024 * 1024

result = {
    "schema": "STAGE32_BR204_CERTIFICATE_STORAGE_PREFLIGHT_V1",
    "status": "PASS_LIGHT_PREFLIGHT_ZERO_CREDIT",
    "canonical_population_regression": {
        "H": 96,
        "total_assignment_mass": EXPECTED_TOTAL_MASS,
        "total_bct_cells": EXPECTED_TOTAL_BCT_CELLS,
        "b0": {"assignment_mass": per_b[0][0], "bct_cells": per_b[0][1]},
        "b96": {"assignment_mass": per_b[96][0], "bct_cells": per_b[96][1]},
    },
    "representative_serialization": {
        "per_b_width_sentinel_b": 96,
        "per_b_measured_bytes": per_b_bytes,
        "largest_shard_width_sentinel": "b=84..96",
        "shard_summary_measured_bytes": shard_bytes,
        "parent_manifest_measured_bytes": parent_bytes,
        "note": (
            "Width sentinels are storage-schema measurements, not FULL178 objective results. "
            "They use actual retained routing counts where available and conservative "
            "maximal-width numeric/hash fields."
        ),
    },
    "hard_upload_caps_bytes": {
        "per_b_certificate": PER_B_CAP,
        "per_shard_summary": SHARD_CAP,
        "parent_manifest": PARENT_CAP,
    },
    "projected_new_peak_persistent_storage_bytes": projected_peak,
    "projected_new_peak_persistent_storage_mib": projected_peak / (1024 * 1024),
    "repository_operating_budget_bytes": 500 * 1024 * 1024,
    "budget_fraction": projected_peak / (500 * 1024 * 1024),
    "evidence_topology": {
        "per_b_certificates": 97,
        "shard_summaries": 8,
        "parent_manifests": 1,
        "raw_state_artifacts_uploaded": False,
        "intermediate_retention_days": 1,
        "upload_rule": "Fail closed before upload if any compact JSON exceeds its class hard cap.",
    },
    "storage_gate": "PASS_WITH_HARD_CAPS",
    "heavy_authorized": False,
    "remaining_heavy_gates": [
        "MAIN freshness identity synchronized by owner",
        "dedicated fresh BR204 run-key explicitly armed",
    ],
    "credit": {
        "stage32_main": False,
        "full178_complete": False,
        "theorem": False,
        "effectivity": False,
        "receiver": False,
        "endpoint": False,
        "perfect_cuboid": False,
        "merge": False,
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
print("RESULT_SHA256", hashlib.sha256(encoded(result)).hexdigest())
