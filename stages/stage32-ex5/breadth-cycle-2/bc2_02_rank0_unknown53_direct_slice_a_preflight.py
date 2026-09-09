#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import bc2_02_one_indexed_full178_terminal_to_picard64_completion as v1

SCHEMA = "STAGE32EX5_BC2_02_RANK0_UNKNOWN53_DIRECT_SLICE_A_PREFLIGHT_V1"
EXPECTED_CHECKPOINT_CANONICAL = "2467b5479881c10a2e28c3d822787acefabef867540a3544d46026655ae81ed7"
EXPECTED_UNKNOWN_COUNT = 53


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    checkpoint, checkpoint_canonical = v1.load_canonical_json(args.checkpoint)
    if checkpoint_canonical != EXPECTED_CHECKPOINT_CANONICAL:
        raise ValueError("rank0 branched-exact checkpoint canonical regression")
    result = checkpoint["result"]
    if result["aggregate_result"] != "UNKNOWN" or result["unknown_branch_count"] != EXPECTED_UNKNOWN_COUNT:
        raise ValueError("rank0 unknown53 checkpoint regression")
    unknown_ids = [int(q) for q in result["unknown_branch_ids"]]
    if len(unknown_ids) != EXPECTED_UNKNOWN_COUNT or len(set(unknown_ids)) != EXPECTED_UNKNOWN_COUNT:
        raise ValueError("unknown branch-id set regression")

    bundle = v1.load_retained(args.retained, "s32ex5_bc2_02_unknown53_a_picard")
    marking = v1.load_retained(args.marking, "s32ex5_bc2_02_unknown53_a_marking")
    data = v1.reconstruct_translation_data(marking, bundle)
    bridge = data["bridge"]
    bridge_cert = bridge.certificate
    if bridge_cert.get("mass_identity_exact_on_picard64") is not True:
        raise ValueError("direct Picard slice mass identity regression")
    if bridge_cert.get("slice_coordinates") != ["degree", "exceptional_total", "first_normal_half_total"]:
        raise ValueError("direct Picard slice coordinate regression")

    degree = int(checkpoint["indexed_terminal"]["degree"])
    exceptional = int(checkpoint["indexed_terminal"]["e"])
    normal_mass = 19 * degree - 5 * exceptional
    if (degree, exceptional, normal_mass) != (8, 4, 132):
        raise ValueError("rank0 d/e/normal-mass regression")

    allowed_a = [a for a in range(normal_mass + 1) if bridge.target_in_image(degree, exceptional, a)]
    if not allowed_a:
        raise ValueError("direct Picard target image unexpectedly admits no a strata")
    if any(a < 0 or a > normal_mass for a in allowed_a):
        raise ValueError("a-stratum bound regression")
    if len(set(allowed_a)) != len(allowed_a):
        raise ValueError("duplicate a strata")

    target_image = bridge_cert["target_image"]
    payload = {
        "schema": SCHEMA,
        "stage": "32EX5",
        "leaf": "BC2-02",
        "unit": "BC2_02_RANK0_UNKNOWN53_DIRECT_SLICE_A_PREFLIGHT",
        "checkpoint_canonical_sha256": checkpoint_canonical,
        "rank0_unknown_branch_ids": unknown_ids,
        "rank0_unknown_branch_count": len(unknown_ids),
        "slice": {
            "degree": degree,
            "exceptional_total": exceptional,
            "normal_total": normal_mass,
            "a_definition": "sum of all140 normal pairings with known labels 1..46",
            "a_bounds": [0, normal_mass],
            "target_image_gate_exact": True,
            "target_image_congruence_modulus": int(target_image["congruence_modulus"]),
            "target_image_active_congruence_rows": int(target_image["active_congruence_rows"]),
            "target_image_image_index": int(target_image["image_index"]),
            "allowed_a": allowed_a,
            "allowed_a_count": len(allowed_a),
            "unknown53_times_allowed_a_strata": len(unknown_ids) * len(allowed_a),
            "partition_complete_for_each_unknown_branch": True,
            "new_mathematical_condition_added": False,
        },
        "source_locks": {
            "retained_bundle_canonical_sha256": bundle["canonical_sha256"],
            "retained_marking_canonical_sha256": marking["canonical_sha256"],
            "direct_slice_bridge_canonical_sha256": bridge_cert["canonical_sha256_without_this_field"],
        },
        "firewalls": {
            "rank0_terminal_closed": False,
            "FULL178_complete": False,
            "stage32_main_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "merge_authorized": False,
        },
        "next_exact_unit": "BC2_02_RANK0_UNKNOWN53_BY_DIRECT_SLICE_A_EXACT",
    }
    payload["canonical_sha256_without_this_field"] = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "allowed_a_count": len(allowed_a),
        "allowed_a": allowed_a,
        "strata": len(unknown_ids) * len(allowed_a),
        "modulus": target_image["congruence_modulus"],
        "image_index": target_image["image_index"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
