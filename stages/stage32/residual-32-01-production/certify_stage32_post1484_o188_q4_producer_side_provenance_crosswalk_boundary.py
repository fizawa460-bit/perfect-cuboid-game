#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

Q4_NAME = "diagnose_stage32_post1473_o188_q4_genus2_descent.py"
Q4_BLOB = "6551e6c7b739dc25e6d47f29ebb97b10c373bab5"
BOUNDARY_NAME = "diagnose_stage32_post1473_x8_satake_boundary_marking.py"
BOUNDARY_BLOB = "1f08f3b5f228b498867e917374e0ba2cdada7ea6"
ADAPTER_NAME = "post1473-boundary-label-weierstrass-adapter.json"
ADAPTER_BLOB = "d3f9c82ab087ea4a2721737867159900a3f304c4"
ADAPTER_CANONICAL = "b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def locked_text(path: Path, expected_blob: str) -> str:
    raw = path.read_bytes()
    actual = git_blob_sha1(raw)
    if actual != expected_blob:
        raise ValueError(f"blob moved for {path}: {actual}")
    return raw.decode()


def build(here: Path) -> dict:
    q4 = locked_text(here / Q4_NAME, Q4_BLOB)
    boundary = locked_text(here / BOUNDARY_NAME, BOUNDARY_BLOB)
    adapter_raw = (here / ADAPTER_NAME).read_bytes()
    if git_blob_sha1(adapter_raw) != ADAPTER_BLOB:
        raise ValueError("boundary adapter blob moved")
    adapter = json.loads(adapter_raw)
    adapter_body = dict(adapter)
    claimed = adapter_body.pop("canonical_sha256_without_this_field", None)
    if claimed != ADAPTER_CANONICAL or csha(adapter_body) != ADAPTER_CANONICAL:
        raise ValueError("boundary adapter canonical moved")

    required_boundary = (
        'matching_signs(block, "z", s)',
        'matching_signs(block, "w", s)',
        'z_labels == [34, 35, 38, 39, 42, 43]',
        'w_labels == [33, 36, 37, 40, 41, 44]',
        'sorted(z_labels + w_labels) == list(range(33, 45))',
    )
    missing = [x for x in required_boundary if x not in boundary]
    if missing:
        raise ValueError(f"boundary marking producer moved: {missing}")

    label_map = {int(k): v for k, v in adapter["boundary_label_to_weierstrass_id"].items()}
    if sorted(label_map) != list(range(33, 45)) or sorted(set(label_map.values())) != list(range(1, 7)):
        raise ValueError("boundary label/Weierstrass frame moved")

    b_pred = "one of the six quotient cusps / Weierstrass points for each projection"
    c_pred = "the two support points map to one quotient cusp / Weierstrass point for each projection"
    if b_pred not in q4 or c_pred not in q4:
        raise ValueError("q4 generic branch-value predicates moved")
    forbidden_q4_selector_strings = (
        "matching_signs(",
        "z_labels",
        "w_labels",
        "boundary_label_to_weierstrass_id",
        "retained_boundary_label",
        "boundary_node_id",
        "formal_branch_id",
        "source_point_id",
        "quotient_cusp_id",
    )
    hits = [x for x in forbidden_q4_selector_strings if x in q4]
    if hits:
        raise ValueError(f"compatible selector entered q4 producer: {hits}")

    result = {
        "schema": "STAGE32_POST1484_O188_Q4_PRODUCER_SIDE_PROVENANCE_CROSSWALK_BOUNDARY_V1",
        "stage": 32,
        "artifact_class": "exact-static-producer-side-provenance-crosswalk-boundary",
        "proof_status": "EXACT_STATIC_REPLAY_PASS_NOT_CLOSURE",
        "source_locks": {
            "q4_descent_generator": {"path": f"stages/stage32/residual-32-01-production/{Q4_NAME}", "blob_sha1": Q4_BLOB},
            "satake_boundary_marking_generator": {"path": f"stages/stage32/residual-32-01-production/{BOUNDARY_NAME}", "blob_sha1": BOUNDARY_BLOB},
            "boundary_label_weierstrass_adapter": {"path": f"stages/stage32/residual-32-01-production/{ADAPTER_NAME}", "blob_sha1": ADAPTER_BLOB, "canonical_sha256": ADAPTER_CANONICAL},
        },
        "producer_frames": {
            "boundary_marking": {
                "has_block_selector": True,
                "has_factor_selector": True,
                "has_branch_sign_selector": True,
                "z_fixed_labels": [34, 35, 38, 39, 42, 43],
                "w_fixed_labels": [33, 36, 37, 40, 41, 44],
                "labels_33_44_partitioned_exactly_once": True,
                "labels_map_to_weierstrass_ids_1_6": True,
            },
            "q4_B_C": {
                "B_branch_value_predicate": b_pred,
                "C_branch_value_predicate": c_pred,
                "emits_boundary_marking_block_selector": False,
                "emits_boundary_marking_factor_selector": False,
                "emits_boundary_marking_branch_sign_selector": False,
                "emits_retained_boundary_label": False,
                "emits_weierstrass_id": False,
            },
        },
        "crosswalk": {
            "common_explicit_carrier_key_in_pinned_producer_triplet": False,
            "boundary_side_selector_frame_exists": True,
            "q4_side_compatible_selector_frame_exists": False,
            "authorized_transport_from_q4_defect_support_to_boundary_selector_frame": False,
            "consequence": "The pinned boundary producer can distinguish retained labels, but the pinned q'=4 B/C producer does not carry a compatible block/factor/branch-sign, retained-label, or Weierstrass-id key. Therefore these pinned producer-side artifacts do not instantiate the missing q'=4 defect-to-retained-boundary transport.",
        },
        "non_inferences": [
            "This certificate does not prove that no external carrier-specific correspondence or symmetry-breaking invariant exists.",
            "The existence of retained boundary labels does not authorize assigning one to the hypothetical q'=4 B/C defect support.",
            "Do not infer a join from shared words such as branch, cusp, quotient, or Weierstrass; the required stable carrier key must be explicitly transported.",
            "This certificate does not close B, C, O=188, the receiver, route, theorem, endpoint, or perfect-cuboid problem.",
        ],
        "firewalls": {
            "O188_closed": False,
            "full178_active": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_claim": False,
        },
        "next_action": "Search upstream of the pinned q'=4 B/C producer for a source-preserving carrier identifier that can be compared to the boundary block/factor/branch-sign frame, or derive a new source-locked invariant with an explicit transport proof. Do not replay the retained q'=4 descent edge for label selection.",
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ap.add_argument("--check", type=Path)
    args = ap.parse_args()
    result = build(Path(__file__).resolve().parent)
    if args.check:
        committed = json.loads(args.check.read_text())
        if committed != result:
            raise ValueError("committed producer-side crosswalk certificate differs from replay")
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("STAGE32_POST1484_O188_Q4_PRODUCER_SIDE_PROVENANCE_CROSSWALK_BOUNDARY=PASS")
    print(f"CANONICAL={result['canonical_sha256_without_this_field']}")


if __name__ == "__main__":
    main()
