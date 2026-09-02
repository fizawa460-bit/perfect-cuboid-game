#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

Q4_CANONICAL = "3617ef2e0717a1d75de0f3a271a4b0e25f3ed7e67e76f1e58b490d3fcba9d978"
BOUNDARY_CANONICAL = "b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f"
JOIN_CANONICAL = "af2cc2e9d42c74657ab7c44411d878ce9bc03d74914fa65dbf916fe0e78a9c3a"
OUTPUT_NAME = "post1484-o188-q4-current-constraint-nonuniqueness.json"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_canonical(path: Path, expected: str) -> dict:
    data = json.loads(path.read_text())
    claimed = data.get("canonical_sha256_without_this_field")
    body = dict(data)
    body.pop("canonical_sha256_without_this_field", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise ValueError(
            f"canonical source moved for {path}: claimed={claimed} actual={actual}"
        )
    return data


def build_result(q4: dict, boundary: dict, join: dict) -> dict:
    b_value = "a quotient cusp / Weierstrass point for each descended map"
    c_value = "P and P' map to one quotient cusp / Weierstrass point for each descended map"
    if q4["B"]["branch_value"] != b_value:
        raise ValueError("B branch-value predicate moved")
    if q4["C"]["branch_value"] != c_value:
        raise ValueError("C branch-value predicate moved")

    forbidden_id_tokens = ("node", "point_id", "formal_branch", "retained_label", "cusp_id")
    b_keys = set(q4["B"])
    c_keys = set(q4["C"])
    if any(token in key for key in b_keys | c_keys for token in forbidden_id_tokens):
        raise ValueError("q'=4 B/C gained a stable identifier field; rerun the pointwise bridge instead")

    mapping = {int(k): int(v) for k, v in boundary["boundary_label_to_weierstrass_id"].items()}
    labels = sorted(mapping)
    cusps = sorted(set(mapping.values()))
    if labels != list(range(33, 45)):
        raise ValueError(f"retained boundary label inventory moved: {labels}")
    if cusps != list(range(1, 7)):
        raise ValueError(f"Weierstrass cusp inventory moved: {cusps}")
    if join["join_obstruction"]["explicit_shared_stable_join_key_available"] is not False:
        raise ValueError("prior identifier-join obstruction moved")
    if join["join_obstruction"]["identifier_preserving_join_from_current_serialized_inputs"] != "UNAVAILABLE":
        raise ValueError("prior join status moved")

    compatible_cusps = cusps
    compatible_labels = labels

    result = {
        "schema": "STAGE32_POST1484_O188_Q4_CURRENT_CONSTRAINT_NONUNIQUENESS_V1",
        "stage": 32,
        "artifact_class": "exact-constraint-nonuniqueness-replay",
        "proof_status": "EXACT_REPLAY_PASS_NOT_CLOSURE",
        "claim_scope": "whether the currently pinned q'=4 B/C branch-value constraints plus the audited retained boundary adapter uniquely determine a quotient cusp or retained boundary label",
        "source_locks": {
            "qprime4_descent_path": "stages/stage32/residual-32-01-production/post1473-o188-q4-genus2-descent.json",
            "qprime4_descent_canonical_sha256": Q4_CANONICAL,
            "boundary_adapter_path": "stages/stage32/residual-32-01-production/post1473-boundary-label-weierstrass-adapter.json",
            "boundary_adapter_canonical_sha256": BOUNDARY_CANONICAL,
            "prior_identifier_join_obstruction_path": "stages/stage32/residual-32-01-production/post1484-o188-q4-defect-identifier-join-obstruction.json",
            "prior_identifier_join_obstruction_canonical_sha256": JOIN_CANONICAL,
        },
        "exact_constraints": {
            "B_branch_value": b_value,
            "C_branch_value": c_value,
            "q4_record_names_no_cusp_id": True,
            "q4_record_names_no_retained_label": True,
            "audited_target_weierstrass_cusp_ids": cusps,
            "audited_target_retained_boundary_labels": labels,
        },
        "candidate_enumeration": {
            "B_current_constraint_compatible_cusp_ids": compatible_cusps,
            "C_current_constraint_compatible_cusp_ids": compatible_cusps,
            "B_current_constraint_compatible_retained_labels": compatible_labels,
            "C_current_constraint_compatible_retained_labels": compatible_labels,
            "unique_cusp_selected": len(compatible_cusps) == 1,
            "unique_retained_label_selected": len(compatible_labels) == 1,
            "cusp_candidate_count": len(compatible_cusps),
            "retained_label_candidate_count": len(compatible_labels),
        },
        "logical_consequence": {
            "current_pinned_constraints_imply_unique_cusp": len(compatible_cusps) == 1,
            "current_pinned_constraints_imply_unique_retained_label": len(compatible_labels) == 1,
            "uniqueness_from_current_pinned_constraints_alone": "IMPOSSIBLE_BY_EXACT_CANDIDATE_NONUNIQUENESS",
            "required_for_future_uniqueness": "At least one new source-locked symmetry-breaking invariant or point/formal-branch provenance datum that excludes all but one currently compatible target.",
        },
        "non_inferences": [
            "This does not prove that no external geometric uniqueness theorem exists.",
            "It proves only that the currently pinned q'=4 branch-value predicates and audited boundary adapter do not themselves reduce the target to one cusp or one retained label.",
            "Do not interpret the 6 cusp or 12 label candidates as proved geometric realizations; they are exactly the targets not excluded by the current pinned predicates.",
            "Do not choose among these candidates using counts, local saturation, V4 symmetry, nodewise reachability, or q'=2 labels.",
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
        "next_action": "Acquire a genuinely new source-locked symmetry-breaking invariant / q'=4 point-formal-branch provenance and only then attempt a unique retained-label transport. A uniqueness proof that uses no new datum beyond the pinned q'=4 branch-value predicates and audited q'=2 adapter is now ruled out.",
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--q4-descent", type=Path)
    ap.add_argument("--boundary-adapter", type=Path)
    ap.add_argument("--join-obstruction", type=Path)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    q4_path = args.q4_descent or here / "post1473-o188-q4-genus2-descent.json"
    boundary_path = args.boundary_adapter or here / "post1473-boundary-label-weierstrass-adapter.json"
    join_path = args.join_obstruction or here / "post1484-o188-q4-defect-identifier-join-obstruction.json"
    output = args.output or here / OUTPUT_NAME

    q4 = load_canonical(q4_path, Q4_CANONICAL)
    boundary = load_canonical(boundary_path, BOUNDARY_CANONICAL)
    join = load_canonical(join_path, JOIN_CANONICAL)
    result = build_result(q4, boundary, join)

    if args.check:
        committed = json.loads(output.read_text())
        if committed != result:
            raise ValueError(f"committed certificate is not canonical: {output}")
        print(f"PASS canonical={result['canonical_sha256_without_this_field']}")
        return

    if args.output:
        output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    else:
        print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
