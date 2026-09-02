#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

Q4_DESCENT_CANONICAL = "3617ef2e0717a1d75de0f3a271a4b0e25f3ed7e67e76f1e58b490d3fcba9d978"
BOUNDARY_ADAPTER_CANONICAL = "b947be5a3677a9e0b46839241adc03004ee5221ee94d6371f165253281e2a81f"
OUTPUT_NAME = "post1484-o188-q4-defect-identifier-join-obstruction.json"
IDENTIFIER_FIELDS = {
    "node_id", "node_index", "point_id", "source_point_id", "formal_branch_id",
    "boundary_label", "retained_boundary_label", "exc48_handle", "boundary_node_id"
}

def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def load_canonical(path: Path, expected: str) -> dict:
    data = json.loads(path.read_text())
    claimed = data.get("canonical_sha256_without_this_field")
    body = dict(data); body.pop("canonical_sha256_without_this_field", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise ValueError(f"canonical source moved for {path}: claimed={claimed} actual={actual}")
    return data

def find_identifier_fields(value: object, prefix: str = "") -> list[str]:
    hits = []
    if isinstance(value, dict):
        for k, v in value.items():
            p = f"{prefix}.{k}" if prefix else k
            if k in IDENTIFIER_FIELDS:
                hits.append(p)
            hits.extend(find_identifier_fields(v, p))
    elif isinstance(value, list):
        for i, v in enumerate(value):
            hits.extend(find_identifier_fields(v, f"{prefix}[{i}]"))
    return hits

def build_result(descent: dict, adapter: dict) -> dict:
    B, C = descent["B"], descent["C"]
    if set(B) != {"branch_value", "descended_ramification_divisor", "local_degree", "unique_defect_contact_m"}:
        raise ValueError(f"B serialized schema moved: {sorted(B)}")
    if set(C) != {"branch_value", "descended_ramification_divisor", "local_degrees", "unique_defect_contact_m"}:
        raise ValueError(f"C serialized schema moved: {sorted(C)}")
    if B["unique_defect_contact_m"] != 3 or C["unique_defect_contact_m"] != 4:
        raise ValueError("B/C defect type moved")
    if B["branch_value"] != "a quotient cusp / Weierstrass point for each descended map":
        raise ValueError("B branch-value description moved")
    if C["branch_value"] != "P and P' map to one quotient cusp / Weierstrass point for each descended map":
        raise ValueError("C branch-value description moved")
    source_identifier_hits = find_identifier_fields({"B": B, "C": C})
    if source_identifier_hits:
        raise ValueError(f"q'=4 source unexpectedly acquired stable identifier fields: {source_identifier_hits}")

    label_map = adapter["boundary_label_to_weierstrass_id"]
    labels = sorted(int(k) for k in label_map)
    cusp_ids = sorted(set(int(v) for v in label_map.values()))
    if labels != list(range(33, 45)) or cusp_ids != list(range(1, 7)):
        raise ValueError("retained q'=2 boundary adapter inventory moved")
    expected_scope = "Adapter only. O=188 remains open; no global-correspondence existence or A/B/C exclusion follows from this certificate."
    if adapter.get("scope") != expected_scope:
        raise ValueError("boundary adapter scope firewall moved")

    result = {
        "schema": "STAGE32_POST1484_O188_Q4_DEFECT_IDENTIFIER_JOIN_OBSTRUCTION_V1",
        "stage": 32,
        "artifact_class": "exact-serialized-provenance-obstruction",
        "proof_status": "EXACT_REPLAY_PASS_NOT_CLOSURE",
        "claim_scope": "whether the pinned q'=4 B/C descent artifact and audited retained boundary adapter already contain a stable identifier-preserving join for the actual defect contact",
        "source_locks": {
            "qprime4_descent_path": "stages/stage32/residual-32-01-production/post1473-o188-q4-genus2-descent.json",
            "qprime4_descent_canonical_sha256": Q4_DESCENT_CANONICAL,
            "boundary_adapter_path": "stages/stage32/residual-32-01-production/post1473-boundary-label-weierstrass-adapter.json",
            "boundary_adapter_canonical_sha256": BOUNDARY_ADAPTER_CANONICAL,
        },
        "exact_schema_checks": {
            "B_serialized_fields": sorted(B),
            "C_serialized_fields": sorted(C),
            "stable_identifier_field_hits_in_B_C": source_identifier_hits,
            "retained_boundary_labels": labels,
            "retained_weierstrass_cusp_ids": cusp_ids,
            "boundary_adapter_scope_firewall_preserved": True,
        },
        "join_obstruction": {
            "source_side_actual_defect_identifier_available": False,
            "boundary_side_identifier_inventory_available": True,
            "explicit_shared_stable_join_key_available": False,
            "identifier_preserving_join_from_current_serialized_inputs": "UNAVAILABLE",
            "reason": "The pinned q'=4 B/C records distinguish the abstract defect type (m=3 or m=4) and generic quotient-cusp behavior but serialize no node/point/formal-branch/retained-label identifier. The audited boundary adapter serializes retained labels 33..44 and cusp ids 1..6, while its scope explicitly withholds any global B/C carrier correspondence. Therefore the two pinned artifacts have no explicit stable key on which the actual B/C defect can be joined to a retained boundary node/label.",
        },
        "information_boundary": {
            "what_is_identified": ["B versus C defect type", "abstract quotient-cusp/Weierstrass branch-value behavior", "retained q'=2 boundary label to Weierstrass-cusp map"],
            "what_is_not_identified": ["actual q'=4 source node", "actual q'=4 formal branch", "actual retained boundary label carrying the q'=4 defect"],
            "required_new_evidence": "A source-preserving correspondence carrying a stable q'=4 defect node/formal-branch identifier into the audited retained boundary label frame, or a separately proved theorem that uniquely determines that label from source-locked data.",
        },
        "non_inferences": [
            "This is not a proof that no mathematical B/C-to-boundary correspondence exists.",
            "It proves only that the currently pinned serialized source/adapter pair does not itself contain an identifier-preserving join for the actual defect contact.",
            "Do not choose an exc48 node, retained label, or Weierstrass cusp from row counts, local saturation, symmetry, or q'=2 adapter data alone.",
        ],
        "firewalls": {
            "O188_closed": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "full178_active": False,
        },
        "next_action": "Search only for new source-preserving q'=4 point/formal-branch provenance or prove a new uniqueness theorem. Do not spend another batch trying to derive a node label from the already-pinned aggregate B/C record and q'=2 adapter alone.",
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    return result

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--q4-descent", type=Path)
    ap.add_argument("--boundary-adapter", type=Path)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    here = Path(__file__).resolve().parent
    q4 = args.q4_descent or here / "post1473-o188-q4-genus2-descent.json"
    adapter = args.boundary_adapter or here / "post1473-boundary-label-weierstrass-adapter.json"
    output = args.output or here / OUTPUT_NAME
    result = build_result(load_canonical(q4, Q4_DESCENT_CANONICAL), load_canonical(adapter, BOUNDARY_ADAPTER_CANONICAL))
    if args.check:
        if json.loads(output.read_text()) != result:
            raise ValueError(f"committed certificate is not canonical: {output}")
        print(f"PASS canonical={result['canonical_sha256_without_this_field']}")
    elif args.output:
        output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    else:
        print(json.dumps(result, sort_keys=True, separators=(",", ":")))
if __name__ == "__main__":
    main()
