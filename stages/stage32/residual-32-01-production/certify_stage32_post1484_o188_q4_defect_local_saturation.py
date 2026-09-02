#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CUSP_BUDGET_CANONICAL = "318ac76ca5baf9e5f7f7a2300628b432f3b5fbb718f2bd21bc7a4f13b9cf3328"
Q4_DESCENT_CANONICAL = "3617ef2e0717a1d75de0f3a271a4b0e25f3ed7e67e76f1e58b490d3fcba9d978"
OUTPUT_NAME = "post1484-o188-q4-defect-local-saturation.json"


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


def exact_A(m: int, parity: str, total_ramification: int, qprime: int) -> int:
    if parity == "odd":
        lower = lambda A: qprime * (A - 1)
        parity_mod = 1
    elif parity == "even":
        lower = lambda A: qprime * (A - 2)
        parity_mod = 0
    else:
        raise ValueError(parity)

    candidates = [
        A for A in range(m, total_ramification + m + 3)
        if A % 2 == parity_mod and lower(A) <= total_ramification
    ]
    if candidates != [m]:
        raise ValueError(f"local saturation not unique: m={m} candidates={candidates}")
    if lower(m) != total_ramification:
        raise ValueError(f"defect lower bound did not saturate: m={m}")
    return m


def build_result(budget: dict, descent: dict) -> dict:
    qprime = 4
    sym = budget["o188_consequences"]["qprime_4_symmetric_profile"]
    if sym["projection_degrees"] != [93, 93] or sym["ramification_totals"] != [8, 8]:
        raise ValueError("q'=4 symmetric profile moved")

    odd_formula = budget["local_adapter"]["odd_contact"]["forced_ramification_on_D_per_N_branch"]
    even_formula = budget["local_adapter"]["even_contact"]["forced_ramification_on_D_per_N_branch"]
    if odd_formula != "qprime*(A_i-1) >= qprime*(m-1)":
        raise ValueError("odd local ramification formula moved")
    if even_formula != "qprime*(A_i-2) >= qprime*(m-2)":
        raise ValueError("even local ramification formula moved")

    if descent["descent"]["two_descended_map_degrees"] != [93, 93]:
        raise ValueError("descended degrees moved")
    if descent["descent"]["two_descended_ramification_totals"] != [2, 2]:
        raise ValueError("descended ramification totals moved")
    if not descent["descent"]["cartesian_torsor_square_proved"]:
        raise ValueError("Cartesian torsor proof lock moved")

    B = descent["B"]
    C = descent["C"]
    if (
        B["unique_defect_contact_m"] != 3
        or B["descended_ramification_divisor"] != "2P"
        or B["local_degree"] != 3
    ):
        raise ValueError("B defect data moved")
    if (
        C["unique_defect_contact_m"] != 4
        or C["descended_ramification_divisor"] != "P+P'"
        or C["local_degrees"] != [2, 2]
    ):
        raise ValueError("C defect data moved")

    total = 8
    A_B = exact_A(3, "odd", total, qprime)
    A_C = exact_A(4, "even", total, qprime)

    result = {
        "schema": "STAGE32_POST1484_O188_Q4_DEFECT_LOCAL_SATURATION_V1",
        "stage": 32,
        "artifact_class": "provisional-exact-replay",
        "proof_status": "PROVISIONAL_EXACT_REPLAY_PENDING_HOSTILE_AUDIT",
        "claim_scope": "q'=4 symmetric B/C local defect saturation and abstract descended ramification concentration only",
        "source_locks": {
            "cusp_budget_path": "stages/stage32/residual-32-01-production/post1473-o188-cusp-ramification-budget.json",
            "cusp_budget_canonical_sha256": CUSP_BUDGET_CANONICAL,
            "qprime4_descent_path": "stages/stage32/residual-32-01-production/post1473-o188-q4-genus2-descent.json",
            "qprime4_descent_canonical_sha256": Q4_DESCENT_CANONICAL,
        },
        "retained_inputs": {
            "qprime": qprime,
            "source_projection_ramification_totals": [8, 8],
            "descended_projection_ramification_totals": [2, 2],
            "B": {
                "unique_defect_contact_m": 3,
                "parity": "odd",
                "descended_ramification_divisor": "2P",
                "descended_local_degrees": [3],
            },
            "C": {
                "unique_defect_contact_m": 4,
                "parity": "even",
                "descended_ramification_divisor": "P+P'",
                "descended_local_degrees": [2, 2],
            },
        },
        "exact_saturation": {
            "B": {
                "local_exponents_A1_A2": [A_B, A_B],
                "forced_source_ramification_lower_bound_formula_per_projection": "4*(A_i-1)",
                "forced_source_ramification_at_defect_contact_per_projection": [8, 8],
                "source_ramification_away_from_defect_contact_per_projection": [0, 0],
                "proof": "A_i>=3 and odd; 4*(A_i-1) is forced at the unique defect contact and cannot exceed total source ramification 8, hence A_i<=3 and A_i=3. The forced 8 exhausts each source projection.",
                "descended_ramification_divisor": "2P",
                "descended_total_ramification": 2,
                "descended_ramification_away_from_defect_support": 0,
            },
            "C": {
                "local_exponents_A1_A2": [A_C, A_C],
                "forced_source_ramification_lower_bound_formula_per_projection": "4*(A_i-2)",
                "forced_source_ramification_at_defect_contact_per_projection": [8, 8],
                "source_ramification_away_from_defect_contact_per_projection": [0, 0],
                "proof": "A_i>=4 and even; 4*(A_i-2) is forced at the unique defect contact and cannot exceed total source ramification 8, hence A_i<=4 and A_i=4. The forced 8 exhausts each source projection.",
                "descended_ramification_divisor": "P+P'",
                "descended_total_ramification": 2,
                "descended_ramification_away_from_defect_support": 0,
            },
        },
        "consequence": {
            "full_source_ramification_concentrated_over_unique_defect_contact": True,
            "full_descended_ramification_concentrated_on_abstract_defect_support": True,
            "all_other_source_ramification_support_excluded": True,
            "all_other_descended_ramification_support_excluded": True,
        },
        "unresolved_pointwise_bridge": {
            "stable_source_node_or_branch_identifier_known": False,
            "authorized_qprime4_transport_to_retained_boundary_label_known": False,
            "named_retained_boundary_support_known": False,
            "reason": "This replay is location-independent. It proves saturation at whichever source branch realizes the unique B/C defect contact, but it does not instantiate that branch on the audited 48-node boundary model.",
        },
        "firewalls": {
            "O188_closed": False,
            "full178_active": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_claim": False,
        },
        "next_action": "Construct or source-lock the actual B/C defect contact as a stable source-node/formal-branch identifier on the audited boundary model, then apply an authorized q'=4 node-to-retained-label transport. Do not infer location from counts, symmetry, or q'=2 labels.",
    }
    result["canonical_sha256_without_this_field"] = csha(result)
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cusp-budget", type=Path)
    ap.add_argument("--q4-descent", type=Path)
    ap.add_argument("--output", type=Path)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    cusp_budget = args.cusp_budget or here / "post1473-o188-cusp-ramification-budget.json"
    q4_descent = args.q4_descent or here / "post1473-o188-q4-genus2-descent.json"
    output = args.output or here / OUTPUT_NAME

    budget = load_canonical(cusp_budget, CUSP_BUDGET_CANONICAL)
    descent = load_canonical(q4_descent, Q4_DESCENT_CANONICAL)
    result = build_result(budget, descent)

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
