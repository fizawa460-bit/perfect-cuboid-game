#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"

LOCKS = {
    "stages/stage29/29-02c-LG2/result.md": "820ed4e1b1a53db14085678de6f186b59ae0ea48",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB101/CERTIFICATE.json": "282fc94d8d5feb0221cf6bf096ed4b0030883563",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB102/CERTIFICATE.json": "f852f66c67343b6a553b5c20e15dc0a0f55d5226",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB103/CERTIFICATE.json": "6d2b7acb667e7757a4f859b7eb0680ce4fd3aae0",
    "stages/stage32/residual-32-01-production/post1648al-beauville-cover-projection-genus-bound.json": "dbe2bea1b2cae1e69ad6c27e5828f81494532fa4",
    "stages/stage32/residual-32-01-production/post1648am-beauville-fibration-picard-source-lock.json": "aa14d340e8b68f863d4013d34fb0eee7b306c0ee",
    "stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md": "512fcc70afb1acf16956fd4b7a2b9b935a052150",
    "stages/stage32/residual-32-01-production/post1648ar-two-factor-slack-minimal-branches-source-note.md": "da9b6ba755b8bd43d5b342d5540053caeb218f57",
    "stages/stage32-ex6/post1697-fsm16-modular-tensor-multibranch-contract.json": "ef000f3607f7d85bde02d41f7323492edf80799f",
    "stages/stage32-ex6/post1697-fsm16-weighted-node-divisor-wall.md": "f035251b6e2e79e8a2162d4cb62bbe3c52639ae8",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/LAMBDA-CAPACITY-WALL.json": "2b5f64ff7ab6da7eccd889b0f99f887c19a3c88d",
}


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text())


def main() -> None:
    for rel, expected in LOCKS.items():
        got = git_blob_sha(ROOT / rel)
        assert got == expected, (rel, got, expected)

    stage29 = (ROOT / "stages/stage29/29-02c-LG2/result.md").read_text()
    mb101 = load_json("stages/stage32/final-chain/32-03-multibranch/nodes/MB101/CERTIFICATE.json")
    mb102 = load_json("stages/stage32/final-chain/32-03-multibranch/nodes/MB102/CERTIFICATE.json")
    mb103 = load_json("stages/stage32/final-chain/32-03-multibranch/nodes/MB103/CERTIFICATE.json")
    al = load_json("stages/stage32/residual-32-01-production/post1648al-beauville-cover-projection-genus-bound.json")
    am = load_json("stages/stage32/residual-32-01-production/post1648am-beauville-fibration-picard-source-lock.json")
    fsm = load_json("stages/stage32-ex6/post1697-fsm16-modular-tensor-multibranch-contract.json")
    cert = json.loads((NODE / "CERTIFICATE.json").read_text())
    lambda_wall = json.loads((NODE / "LAMBDA-CAPACITY-WALL.json").read_text())

    assert "H^2 = K_S^2 = 16" in stage29
    assert "negative-definite lattice `H^perp`" in stage29
    assert mb101["branch_contract"]["exceptional_intersection_multiplicity"] == "m=min(A,B)"
    assert mb101["branch_contract"]["A_plus_B_even"] is True
    assert mb102["global_genus_contract"]["finite_degree_bound_implied"] is False
    assert mb103["quotient_contract"]["exact_for_intrinsic_node_indexed_discrete_payload"] is True

    assert al["proof_adapter"]["factor_quotient_genus_Y"] == 2
    assert al["proof_adapter"]["local_ramification_rule"] == "branch with exceptional intersection multiplicity m ramifies iff m is odd"
    assert am["source_geometry_adapter"]["boundary_elliptics_per_direction"] == 6
    assert am["source_geometry_adapter"]["singular_cusps_per_boundary_elliptic"] == 8
    assert am["source_geometry_adapter"]["special_fibre_class_formula"] == "F_E=2*E+sum(8 incident exceptional curves)"
    assert am["retained_picard_replay"]["B1_plus_B2_equals_K"] is True

    assert fsm["source_proof_constants"]["tensor_degree_factor"] == 16
    assert fsm["source_proof_constants"]["zero_lower_bound_per_degree_per_k"] == 2
    assert fsm["source_proof_constants"]["max_pole_order_per_minimal_cusp_branch_per_k"] == 8
    assert fsm["stage32_fsm16_adapter"]["A_B_positive"] is True
    assert fsm["stage32_fsm16_adapter"]["A_plus_B_even"] is True
    assert fsm["stage32_fsm16_adapter"]["minimal_pairs_equivalent"] is True

    assert cert["schema"] == "STAGE32_MB104_FINITE_WINDOW_COEFFICIENT_BARRIER_V4"
    assert cert["special_fibre_contract"]["identity"] == "6*n_i=2*q_i+M"
    assert cert["factor_slack_contract"]["global_identity"] == "M-d+4*g-4=sigma_1+sigma_2>=0"
    assert cert["minimal_branch_contract"]["derived_minimal_bound"] == "s_min>=d-4*g+4"
    assert cert["picard_hodge_contract"]["quadratic_inequality"] == "sum_i M_i^2<=d^2/8+2*d-4*g+4"
    assert cert["picard_hodge_contract"]["cauchy_global_inequality"] == "M^2<=6*d^2+96*d-192*g+192"
    assert cert["picard_hodge_contract"]["closes_degree"] is False
    assert cert["fsm_tensor_contract"]["branchwise_necessary_bound"] == "d<=16*g-16+4*s_min"
    assert "alpha<1" in cert["closing_thresholds"]["minimal_branch_direct_threshold"]
    assert "alpha<1" in cert["closing_thresholds"]["exceptional_mass_upper_coefficient"]

    # Exact local nonclosure wall: lambda is a free C* landing parameter in the
    # retained A1 model, while the retained FSM weighted order is lambda-blind.
    assert cert["lambda_capacity_contract"]["arbitrarily_many_pairwise_distinct_local_landings_allowed"] is True
    assert cert["lambda_capacity_contract"]["uniform_local_constant_capacity_bound_available"] is False
    assert cert["lambda_capacity_contract"]["fsm_weighted_order_depends_on_lambda"] is False
    assert cert["lambda_capacity_contract"]["local_lambda_route_closes_degree"] is False
    assert lambda_wall["local_minimal_branch"]["fsm_type"] == "(A,B)=(1,1)"
    assert lambda_wall["local_minimal_branch"]["exceptional_multiplicity"] == 1
    assert lambda_wall["local_minimal_branch"]["fsm_exponents_determine_lambda"] is False
    assert lambda_wall["arbitrary_local_capacity_witness"]["uniform_local_constant_cap_on_minimal_branches_derivable"] is False
    assert lambda_wall["arbitrary_local_capacity_witness"]["global_algebraic_curve_existence_claimed"] is False
    assert lambda_wall["fsm_tensor_visibility"]["depends_on_lambda"] is False
    assert lambda_wall["conclusion"]["preferred_lambda_capacity_route_closes_mb104"] is False

    checked = 0
    hodge_compatible = 0
    for g in (0, 1):
        for d in range(2, 81):
            for n1 in range(1, d):
                n2 = d - n1
                for M in range(0, 3 * d + 1, 2):
                    q1_num = 6 * n1 - M
                    q2_num = 6 * n2 - M
                    if q1_num < 0 or q2_num < 0 or q1_num % 2 or q2_num % 2:
                        continue
                    q1, q2 = q1_num // 2, q2_num // 2
                    sigma1 = 2 * g - 2 + 2 * n1 - q1
                    sigma2 = 2 * g - 2 + 2 * n2 - q2
                    if sigma1 < 0 or sigma2 < 0:
                        continue
                    assert sigma1 + sigma2 == M - d + 4 * g - 4
                    assert d <= M + 4 * g - 4
                    checked += 1
                    if M * M <= 6 * d * d + 96 * d - 192 * g + 192:
                        hodge_compatible += 1

    for A in range(1, 10):
        for B in range(1, 10):
            if (A + B) % 2:
                continue
            pole = max(0, 16 - 4 * (A + B))
            assert (pole > 0) == (A == 1 and B == 1)
            if pole > 0:
                assert pole == 8

    for d in range(2, 2002, 2):
        assert d * d <= 6 * d * d + 96 * d
        M0 = d + 4
        assert M0 * M0 <= 6 * d * d + 96 * d + 192

    fw = cert["credit_firewall"]
    assert fw["mb104_complete"] is False
    assert fw["finite_degree_window_proved"] is False
    assert fw["finite_picard_enumeration_released"] is False
    assert fw["receiver_credit"] is False
    assert fw["perfect_cuboid_existence_claim"] is False
    assert fw["perfect_cuboid_nonexistence_claim"] is False
    assert fw["merge_authorized"] is False

    print("MB104 V4 coefficient/Hodge/lambda-wall verifier PASS")
    print(f"bounded algebra sanity states={checked}; Hodge-compatible={hodge_compatible}")
    print("retained: M-d+4g-4=sigma1+sigma2>=0; s_min>=d-4g+4")
    print("retained Hodge: M^2<=6d^2+96d-192g+192")
    print("retained local wall: lambda-cardinality route is nonclosing")
    print("finite degree window remains OPEN")


if __name__ == "__main__":
    main()
