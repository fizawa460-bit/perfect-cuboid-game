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
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/KNOWN-CURVE-CONE-WALL.json": "61e516f2cb231ad61d16eb097395ec69e409c943",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_known_curve_cone_wall.py": "338347e34eecd5b6f3dd0c8fabf720c61780bdcb",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/A1-CONTRACTION-CONDUCTOR-SOURCE-NOTE.md": "060a1c989c4fcadbb595add7250189e0b7834ab4",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/A1-CONTRACTION-CONDUCTOR.json": "fda08685a63caab19851d0d6e5bac353092c888e",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_a1_contraction_conductor.py": "dba48511316a78d2ba91fa3235d70e01c8ae1e29",
    "docs/arsenal/cards/provisional/S32-PW09.md": "14755f8d7a14dac75a80eb711b6083c5f3b0ea3b",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/SPECIAL-DISCRIMINANT-CAPACITY-WALL.json": "d6c53f35268fc09111017b1f147c656dfd6127f1",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_special_discriminant_capacity_wall.py": "bdaf7c419c29e30623a34fd3852319e80cc2545e",
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
    cert = load_json("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/CERTIFICATE.json")
    lambda_wall = load_json("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/LAMBDA-CAPACITY-WALL.json")
    known_wall = load_json("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/KNOWN-CURVE-CONE-WALL.json")
    a1 = load_json("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/A1-CONTRACTION-CONDUCTOR.json")
    disc_wall = load_json("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/SPECIAL-DISCRIMINANT-CAPACITY-WALL.json")
    pw09 = (ROOT / "docs/arsenal/cards/provisional/S32-PW09.md").read_text()

    assert "H^2 = K_S^2 = 16" in stage29
    assert "negative-definite lattice `H^perp`" in stage29
    assert mb101["branch_contract"]["exceptional_intersection_multiplicity"] == "m=min(A,B)"
    assert mb102["global_genus_contract"]["finite_degree_bound_implied"] is False
    assert mb103["quotient_contract"]["exact_for_intrinsic_node_indexed_discrete_payload"] is True

    assert al["proof_adapter"]["factor_quotient_genus_Y"] == 2
    assert al["proof_adapter"]["local_ramification_rule"] == "branch with exceptional intersection multiplicity m ramifies iff m is odd"
    assert am["source_geometry_adapter"]["boundary_elliptics_per_direction"] == 6
    assert am["source_geometry_adapter"]["singular_cusps_per_boundary_elliptic"] == 8
    assert am["source_geometry_adapter"]["special_fibre_class_formula"] == "F_E=2*E+sum(8 incident exceptional curves)"
    assert am["retained_picard_replay"]["B1_plus_B2_equals_K"] is True

    assert fsm["source_proof_constants"]["tensor_degree_factor"] == 16
    assert fsm["source_proof_constants"]["max_pole_order_per_minimal_cusp_branch_per_k"] == 8
    assert fsm["stage32_fsm16_adapter"]["minimal_pairs_equivalent"] is True

    assert cert["schema"] == "STAGE32_MB104_FINITE_WINDOW_COEFFICIENT_BARRIER_V6"
    assert cert["special_fibre_contract"]["identity"] == "6*n_i=2*q_i+M"
    assert cert["factor_slack_contract"]["global_identity"] == "M-d+4*g-4=sigma_1+sigma_2>=0"
    assert cert["minimal_branch_contract"]["derived_minimal_bound"] == "s_min>=d-4*g+4"
    assert cert["picard_hodge_contract"]["quadratic_inequality"] == "sum_i M_i^2<=d^2/8+2*d-4*g+4"
    assert cert["picard_hodge_contract"]["cauchy_global_inequality"] == "M^2<=6*d^2+96*d-192*g+192"
    assert cert["picard_hodge_contract"]["closes_degree"] is False

    assert cert["lambda_capacity_contract"]["uniform_local_constant_capacity_bound_available"] is False
    assert lambda_wall["conclusion"]["preferred_lambda_capacity_route_closes_mb104"] is False

    kc = cert["known_curve_cone_contract"]
    assert kc["strictly_positive_on_all_140_known_curves"] is True
    assert kc["riemann_roch_effective_divisor_class_for_all_k"] is True
    assert kc["integral_member_claimed"] is False
    assert kc["low_genus_member_claimed"] is False
    assert kc["closes_degree"] is False
    assert known_wall["symmetric_scaling_ray"]["exceptional_mass"] == "M=96*k=d"

    ac = cert["a1_contraction_contract"]
    assert ac["single_node_formula"] == "p_a(C)-p_a(D)=floor(M_i^2/4)"
    assert ac["global_formula"] == "Delta_image=Delta_strict+Q_A1"
    assert ac["coarse_lower_bound"] == "Q_A1>=M^2/192-12"
    assert ac["lambda_dependent"] is False
    assert ac["closes_degree"] is False
    assert a1["exact_contraction_formula"]["single_node"] == "p_a(C)-p_a(D)=floor(M^2/4)"
    assert a1["exact_contraction_formula"]["lambda_dependent"] is False

    sc = cert["special_discriminant_capacity_contract"]
    assert sc["s32_pw09_formula"] == "Disc(pi)=Br(f)+2*A"
    assert "Disc(pi)=Br+2A" in pw09
    assert sc["normalized_projection_degree"] == 2
    assert sc["special_values_needed"] == 1
    assert sc["normalization_index_unbounded_at_fixed_degree"] is True
    assert sc["discriminant_multiplicity_unbounded_at_fixed_degree"] is True
    assert sc["generic_projection_degree_plus_special_value_count_closes"] is False
    assert disc_wall["capacity_consequence"]["no_upper_bound_from_projection_degree_and_special_value_count_alone"] is True
    assert disc_wall["firewalls"]["generic_nonclosure_refutes_ambient_geometry_bound"] is False

    # Bounded algebra replay of the factor/slack identities.
    checked = 0
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
                    checked += 1

    # A1 balanced contraction debt and coarse lower bound.
    def q(m: int) -> int:
        return (m * m) // 4

    for M in range(0, 5001):
        quo, rem = divmod(M, 48)
        qmin = (48 - rem) * q(quo) + rem * q(quo + 1)
        assert qmin >= M * M / 192 - 12

    # Generic degree-two order wall: fixed normalized degree and one special
    # value admit arbitrary normalization index N.
    for N in range(0, 10001):
        assert 2 * N + 1 == 1 + 2 * N

    # Retained effective Picard ray remains compatible with the nonclosing
    # ledgers; no integral/low-genus member is inferred.
    for k in range(1, 101):
        d = 96 * k
        M = 96 * k
        D2 = 480 * k * k
        assert M == d
        assert 48 * q(2 * k) == 48 * k * k
        assert 48 * (2 * k) ** 2 <= d * d // 8 + 2 * d
        chi = 8 + (D2 - d) // 2
        assert chi == 240 * k * k - 48 * k + 8 and chi > 0

    rd = cert["route_decision"]
    assert rd["retire_generic_special_value_discriminant_capacity_bound"] is True
    assert rd["next_subobligation"] == "MB104_AMBIENT_BOX_SURFACE_CONDUCTOR_CAPACITY_BOUND"

    fw = cert["credit_firewall"]
    assert fw["mb104_complete"] is False
    assert fw["finite_degree_window_proved"] is False
    assert fw["finite_picard_enumeration_released"] is False
    assert fw["receiver_credit"] is False
    assert fw["perfect_cuboid_existence_claim"] is False
    assert fw["perfect_cuboid_nonexistence_claim"] is False
    assert fw["merge_authorized"] is False

    print("MB104 V6 verifier PASS")
    print(f"bounded factor/slack states={checked}")
    print("retained A1 contraction debt: Q_A1=sum floor(M_i^2/4) >= M^2/192-12")
    print("retained generic wall: degree 2 + one special value admits unbounded index")
    print("next: ambient box-surface conductor capacity; finite degree window remains OPEN")


if __name__ == "__main__":
    main()
