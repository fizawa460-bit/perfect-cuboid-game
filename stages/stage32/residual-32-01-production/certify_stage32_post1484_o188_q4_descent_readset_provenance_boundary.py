#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path

CUSP_CANONICAL = "318ac76ca5baf9e5f7f7a2300628b432f3b5fbb718f2bd21bc7a4f13b9cf3328"
CUSP_BLOB = "dd5fdb8d2553d25a1479c1e5cff68a201c8396e3"
V4_CANONICAL = "2869208e7509d7b79378264ea1982299b0f1745b1a54c5856cfbba0754567ce5"
V4_BLOB = "00eaebc3c57f6b5e3696c7bcd60eac5a53121f72"
GENERATOR_BLOB = "6551e6c7b739dc25e6d47f29ebb97b10c373bab5"
GENERATOR_NAME = "diagnose_stage32_post1473_o188_q4_genus2_descent.py"
CUSP_NAME = "post1473-o188-cusp-ramification-budget.json"
V4_NAME = "post1473-x8-v4-cusp-quotient.json"
IDENTIFIER_TOKENS = (
    "node_id",
    "node_index",
    "point_id",
    "source_point_id",
    "formal_branch_id",
    "boundary_label",
    "retained_boundary_label",
    "boundary_node_id",
    "exc48_handle",
    "quotient_cusp_id",
)


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_canonical(path: Path, expected: str, expected_blob: str) -> dict:
    raw = path.read_bytes()
    actual_blob = git_blob_sha1(raw)
    if actual_blob != expected_blob:
        raise ValueError(f"blob moved for {path}: {actual_blob}")
    obj = json.loads(raw)
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    actual = csha(body)
    if claimed != expected or actual != expected:
        raise ValueError(f"canonical moved for {path}: claimed={claimed} actual={actual}")
    return obj


def const_string(node: ast.AST) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def rooted_chain(node: ast.AST) -> tuple[str, ...] | None:
    if isinstance(node, ast.Name):
        return (node.id,)
    if isinstance(node, ast.Subscript):
        parent = rooted_chain(node.value)
        key = const_string(node.slice)
        if parent is None or key is None:
            return None
        return parent + (key,)
    return None


def semantic_readset(source: str, roots: set[str]) -> list[str]:
    tree = ast.parse(source)
    found: set[tuple[str, ...]] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Subscript):
            continue
        chain = rooted_chain(node)
        if chain and chain[0] in roots:
            found.add(chain)
    return [".".join(x) for x in sorted(found)]


def build(here: Path) -> dict:
    cusp_path = here / CUSP_NAME
    v4_path = here / V4_NAME
    gen_path = here / GENERATOR_NAME

    budget = load_canonical(cusp_path, CUSP_CANONICAL, CUSP_BLOB)
    quotient = load_canonical(v4_path, V4_CANONICAL, V4_BLOB)

    gen_raw = gen_path.read_bytes()
    actual_gen_blob = git_blob_sha1(gen_raw)
    if actual_gen_blob != GENERATOR_BLOB:
        raise ValueError(f"q4 descent generator moved: {actual_gen_blob}")
    source = gen_raw.decode()

    reads = semantic_readset(source, {"budget", "quotient"})
    expected_reads = [
        "budget.fixed_target",
        "budget.o188_consequences",
        "budget.o188_consequences.qprime_4_symmetric_profile",
        "quotient.quotient_geometry",
    ]
    if reads != expected_reads:
        raise ValueError(f"q4 semantic input readset moved: {reads}")

    totals = budget["coarse_nodewise_nonexclusion"]["fixed_exceptional_totals"]
    orbits = quotient["quotient_cusp_orbits_mod8_pm"]
    if len(totals) != 48 or len(orbits) != 6 or any(len(o) != 4 for o in orbits):
        raise ValueError("available node/cusp inventory moved")

    token_hits = sorted(t for t in IDENTIFIER_TOKENS if t in source)
    if token_hits:
        raise ValueError(f"identifier token entered q4 descent generator: {token_hits}")

    if "coarse_nodewise_nonexclusion" in source or "quotient_cusp_orbits_mod8_pm" in source:
        raise ValueError("previously-unconsumed pointwise inventory entered q4 descent generator")
    if "one of the six quotient cusps / Weierstrass points for each projection" not in source:
        raise ValueError("B generic branch-value predicate moved")
    if "the two support points map to one quotient cusp / Weierstrass point for each projection" not in source:
        raise ValueError("C generic branch-value predicate moved")

    result = {
        "schema": "STAGE32_POST1484_O188_Q4_DESCENT_READSET_PROVENANCE_BOUNDARY_V1",
        "stage": 32,
        "artifact_class": "exact-static-semantic-readset-provenance-boundary",
        "proof_status": "EXACT_STATIC_REPLAY_PASS_NOT_CLOSURE",
        "source_locks": {
            "q4_descent_generator": {"path": f"stages/stage32/residual-32-01-production/{GENERATOR_NAME}", "blob_sha1": GENERATOR_BLOB},
            "cusp_budget": {"path": f"stages/stage32/residual-32-01-production/{CUSP_NAME}", "blob_sha1": CUSP_BLOB, "canonical_sha256": CUSP_CANONICAL},
            "v4_cusp_quotient": {"path": f"stages/stage32/residual-32-01-production/{V4_NAME}", "blob_sha1": V4_BLOB, "canonical_sha256": V4_CANONICAL},
        },
        "semantic_readset": {
            "generator_direct_budget_and_quotient_paths": reads,
            "available_but_not_semantically_read": {
                "cusp_budget.coarse_nodewise_nonexclusion.fixed_exceptional_totals_count": len(totals),
                "v4_cusp_quotient.quotient_cusp_orbits_mod8_pm_count": len(orbits),
            },
            "carrier_specific_identifier_token_hits": token_hits,
            "nodewise_inventory_used_to_select_B_or_C_defect": False,
            "abstract_cusp_orbit_inventory_used_to_select_B_or_C_branch_value": False,
        },
        "logical_consequence": {
            "current_q4_descent_edge_has_carrier_specific_point_or_formal_branch_selector": False,
            "current_q4_descent_edge_has_retained_boundary_label_selector": False,
            "current_q4_descent_edge_has_abstract_cusp_orbit_selector": False,
            "generic_B_C_branch_value_predicates_are_constructed_without_pointwise_selector": True,
            "required_new_evidence": "A new carrier-specific q'=4 point/formal-branch datum or symmetry-breaking invariant must enter through a new source-locked comparison/transport edge; replaying this retained descent edge cannot create the missing selector.",
        },
        "non_inferences": [
            "This is a static semantic-readset statement about the pinned q'=4 descent generator, not a theorem that no geometric correspondence exists.",
            "Canonical hashing reads the complete input files for integrity; 'not semantically read' means the generator does not access those fields to derive B/C or select a cusp/node.",
            "The 48 node totals and six abstract cusp orbits are inventories, not proved realizations of the B/C defect support.",
            "Do not choose a node, cusp, or retained label from counts, symmetry, local saturation, or q'=2 labels.",
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
        "next_action": "Search outside the retained q'=4 descent semantic readset for a genuinely carrier-specific source datum or new symmetry-breaking invariant with an authorized comparison to the audited boundary frame.",
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    ap.add_argument("--check", type=Path)
    args = ap.parse_args()
    here = Path(__file__).resolve().parent
    result = build(here)
    if args.check:
        committed = json.loads(args.check.read_text())
        if committed != result:
            raise ValueError("committed provenance-boundary certificate differs from replay")
    if args.output:
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print("STAGE32_POST1484_O188_Q4_DESCENT_READSET_PROVENANCE_BOUNDARY=PASS")
    print(f"CANONICAL={result['canonical_sha256_without_this_field']}")


if __name__ == "__main__":
    main()
