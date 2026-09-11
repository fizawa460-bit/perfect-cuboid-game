#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
N342 = ROOT / "stages/stage32/32-01-178/nodes/N342/RESULT.json"
N348 = ROOT / "stages/stage32/32-01-178/nodes/N348/RESULT.json"
CONTRACT = HERE / "FSM_BOUNDARY_EQUALITY_CONTRACT.md"
OLD_REFINEMENT = ROOT / "stages/stage32/32-21/post-21bl-freitag-node-support-refinement.md"

EXPECTED_N342 = "0a556575c4ad365d5f0816a60c380de16ca609310961e58f6e63834082a61c88"
EXPECTED_N348 = "9a1f1cd3ec4060239d74e552d63126fe4b948d3accb3fe0fbe3e8e0213b51672"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load(path: Path, expected: str) -> dict:
    d = json.loads(path.read_text())
    claimed = d.pop("canonical_sha256_without_this_field")
    if claimed != expected or csha(d) != expected:
        raise ValueError(f"canonical regression: {path}")
    d["canonical_sha256_without_this_field"] = claimed
    return d


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    n342 = load(N342, EXPECTED_N342)
    n348 = load(N348, EXPECTED_N348)
    contract = CONTRACT.read_text()
    old = OLD_REFINEMENT.read_text()

    for s in [
        "a1+a2 >= 8",
        "`(a1,a2)=(4,4)` at every node",
        "LOCAL_CUSP_PAIR_DATA_PRESENT=false",
        "PICARD_PAIRING_ONE_IMPLIES_LOCAL_PAIR_4_4=false",
    ]:
        if s not in contract:
            raise ValueError(f"N349 contract regression: {s}")
    for s in ["d <= 16g - 16 + 4n", "Putting `n=48` recovers"]:
        if s not in old:
            raise ValueError(f"audited N1472 refinement regression: {s}")

    if n342["aggregate"]["sat_terminal_count"] != 21:
        raise ValueError("N342 terminal count regression")
    if not n342["aggregate"]["all_have_exact_labelled_support48"]:
        raise ValueError("N342 all48 support regression")
    if n342["aggregate"]["support_count_each"] != 48:
        raise ValueError("N342 support count regression")
    if n348["aggregate"]["geometric_effective_divisor_representative_count"] != 21:
        raise ValueError("N348 effectivity count regression")

    rows = [
        {"row_id": "g0-d176", "genus": 0, "degree": 176, "terminal_count": 10},
        {"row_id": "g1-d192", "genus": 1, "degree": 192, "terminal_count": 11},
    ]
    for row in rows:
        g, d = row["genus"], row["degree"]
        boundary = 176 + 16 * g
        if d != boundary:
            raise ValueError(f"not on FSM boundary: {row}")
        # Existing audited support refinement d <= 16g-16+4n.
        required_n = (d - 16 * g + 16 + 3) // 4
        if required_n != 48:
            raise ValueError(f"boundary support requirement drift: {row}")
        row["fsm_boundary_degree"] = boundary
        row["minimum_node_support"] = required_n
        row["retained_exact_node_support"] = 48
        row["support_condition_saturated"] = True
        row["necessary_local_pair_at_each_node"] = [4, 4]
        row["local_pair_evidence_present"] = False

    result = {
        "schema": "STAGE32_32_01_178_N349_FSM_BOUNDARY_EQUALITY_PREFLIGHT_V1",
        "node_id": "N349",
        "source_locks": {
            "n342_checkpoint_canonical": EXPECTED_N342,
            "n348_checkpoint_canonical": EXPECTED_N348,
            "fsm_node_support_refinement_merge_commit": "8cb707ffdc4ea72094d397df1896b374a4bbb1a7",
            "fsm_primary_source_doi": "10.1307/mmj/1480734014",
            "fsm_primary_source_locator": "Theorem 3.1 proof, printed pp. 10-11",
        },
        "rows": rows,
        "aggregate": {
            "boundary_terminal_count": 21,
            "all_boundary_degrees_exact": True,
            "all_have_required_48_node_support": True,
            "local_pair_4_4_evidence_count": 0,
            "local_pair_evidence_unknown_count": 21,
        },
        "exact_boundary_consequence": {
            "if_integral_irreducible_bijective_normalization_low_genus_member_exists":
                "every one of its 48 node branches must saturate the FSM local pole bound",
            "required_translation_pair_at_every_node": [4, 4],
            "reason": "global boundary equality forces total pole order 384k; 48 local bounds <=8k must all be equalities; positive translation-lattice multiples of 4 with sum 8 give (4,4)",
        },
        "next_required_adapter": {
            "name": "ACTUAL_MEMBER_TO_48_LOCAL_FSM_CUSP_PAIRS",
            "present": False,
            "acceptable_closure": [
                "construct integral irreducible genus-0/1 member and replay all 48 local pairs as (4,4)",
                "prove no integral irreducible member in the locked class can realize (4,4) at all 48 nodes",
            ],
        },
        "semantics": {
            "new_numerical_pruning_credit": False,
            "picard_pairing_one_is_not_local_pair_certificate": True,
            "integral_irreducible_member_credit": False,
            "bijective_normalization_low_genus_credit": False,
            "multibranch_credit": False,
            "q_defined_effective_member_credit": False,
            "production_leaf_credit": False,
            "n350_producer_registry_unchanged": True,
            "full178_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "hostile_audit_required_before_main_credit": True,
            "merge_authorized": False,
        },
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_N349_FSM_BOUNDARY_EQUALITY_PREFLIGHT_GAP_EXPOSED",
        "boundary_terminals": 21,
        "all48_support": True,
        "required_local_pair": "4,4",
        "local_pair_certified": 0,
        "local_pair_unknown": 21,
        "canonical": result["canonical_sha256_without_this_field"],
        "pruning_credit": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
