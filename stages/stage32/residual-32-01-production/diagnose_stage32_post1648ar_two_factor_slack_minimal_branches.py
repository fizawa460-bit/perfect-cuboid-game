#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
AO = HERE / "post1648ao-special-fibre-hurwitz-budget.json"
AQ = HERE / "post1648aq-residual-g-cusp-multiplicity-grid.json"


def main() -> None:
    ao = json.loads(AO.read_text())
    aq = json.loads(AQ.read_text())

    if ao["canonical_sha256_without_this_field"] != "39e217c7223732b1834b7e9b96b4361807227f823a5624842a97eddf71390378":
        raise ValueError("AO canonical regression")
    if aq["canonical_sha256_without_this_field"] != "1831162e6f270b461d63fbdfda57b61711aacd49b85fe40e37fb5d5b3634088e":
        raise ValueError("AQ canonical regression")

    packs = {int(x["projection_degree"]): x for x in ao["boundary_six_packs"]}
    if set(packs) != {81, 105}:
        raise ValueError("factor degree regression")

    e = int(ao["v6_exact_inputs"]["exceptional_mass"])
    if e != 266 or aq["branch_count"]["exceptional_mass"] != e:
        raise ValueError("exceptional mass regression")

    factors = {}
    for n in (81, 105):
        q = int(packs[n]["q_boundary_sum"])
        R = int(packs[n]["total_ramification_genus1_to_genus0"])
        if R != 2 * n:
            raise ValueError("Riemann-Hurwitz regression")
        slack = R - q
        factors[str(n)] = {
            "degree": n,
            "q_boundary": q,
            "total_ramification": R,
            "slack": slack,
            "identity": f"{slack}=t+q{n}_node+eta{n}+rho{n}",
        }

    if factors["81"]["slack"] != 52 or factors["105"]["slack"] != 28:
        raise ValueError("two-factor slack regression")

    # Let t=e-N=sum(a-1). Each nonminimal node branch either has a>1,
    # charging >=1 to t, or has a=1 with unequal same-parity factor orders,
    # charging >=1 to exactly one node-boundary q resource.
    t_max = min(factors["81"]["slack"], factors["105"]["slack"])
    min_node_branches = e - t_max
    if min_node_branches != 238:
        raise ValueError("node branch lower bound regression")

    # q81_node <= 52-t and q105_node <= 28-t, hence
    # nonminimal <= t+(52-t)+(28-t)=80-t.
    # Since N=266-t, minimal >=186, independent of t.
    min_minimal = e - (factors["81"]["slack"] + factors["105"]["slack"])
    if min_minimal != 186:
        raise ValueError("minimal branch bound regression")

    # AQ's weaker transverse count is retained as a consistency check.
    if int(aq["branch_count"]["min_transverse_node_branches"]) != 210:
        raise ValueError("AQ transverse branch regression")

    out = {
        "mode": "SCRATCH_POST1648AR_TWO_FACTOR_SLACK_MINIMAL_BRANCHES",
        "parents": {
            "AO_canonical": ao["canonical_sha256_without_this_field"],
            "AQ_canonical": aq["canonical_sha256_without_this_field"],
        },
        "exact_inputs": {
            "exceptional_mass": e,
            "AQ_min_transverse_node_branches": int(aq["branch_count"]["min_transverse_node_branches"]),
        },
        "factor_slack": factors,
        "combined_bound": {
            "t_definition": "t=e-N=sum_node_branches(a-1)",
            "t_max": t_max,
            "minimum_node_branches": min_node_branches,
            "nonminimal_branch_charge_rule": "each nonminimal branch charges >=1 to t or q81_node or q105_node",
            "maximum_nonminimal_formula": "80-t",
            "minimum_FSM_minimal_A_B_1_1_branches": min_minimal,
            "minimal_branch_properties": {
                "exceptional_contact": 1,
                "node_boundary_contact_both_directions": 0,
                "factor_orders": [1, 1],
                "factor_ramification_both_directions": 0,
                "exceptional_landing": "lambda in C* away from the two boundary-intersection points",
            },
        },
        "decision": {
            "bounded_positive": "ANY_HYPOTHETICAL_INTEGRAL_GEOMETRIC_GENUS1_V6_CARRIER_REQUIRES_AT_LEAST_186_FSM_MINIMAL_NODE_BRANCHES",
            "v6_carrier_excluded": False,
            "next_exact_route": "RESIDUAL_G_NODE_STABILIZER_TANGENT_ACTION_ON_AT_LEAST_186_MINIMAL_LANDINGS_AND_OFF_EXCEPTIONAL_SELF_IDENTIFICATION_BUDGET",
        },
        "firewalls": {
            "scratch_only": True,
            "shared_MAIN_STATE_unchanged": True,
            "shared_authority_unchanged": True,
            "Q602_excluded": False,
            "O210_excluded": False,
            "O212_plus_advance_allowed": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
