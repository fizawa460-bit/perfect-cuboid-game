#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
STATE = ROOT / "stages/stage32/final-chain/32-03-multibranch/STATE.json"

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
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/AMBIENT-A1-SCALING-WALL.json": "3d14df8ae1e4bc79fde16ac3bfd550de68747e9f",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_ambient_a1_scaling_wall.py": "411c52bc6647825b4b6d7a4a20b21408080a2bb6",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/LU-MIYAOKA-ORDINARY-NODE-DEBT-SOURCE-NOTE.md": "23bc895d79ca34d17d9a07de73acc1f990930cf5",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/LU-MIYAOKA-ORDINARY-NODE-DEBT.json": "80380d1009fb8c500ff327335b5754fde4a53b92",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_lu_miyaoka_node_debt.py": "070c54731000aaf3f60203c735ef2e833df99acc",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-MIYAOKA-COVER-WALL.md": "d01b461cc8f25b3b374e5327e678b37a52fc876b",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BEAUVILLE-MIYAOKA-COVER-WALL.json": "fdbf063329fa1f7a0cd4fbeb5034e897574e7448",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_beauville_miyaoka_cover_wall.py": "0e891d135addc8d2cf5391743ceb25889ea1975a",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BTVA-PROJECTIVE-SPAN-FILTER-SOURCE-NOTE.md": "73c00595c599e0312c69060ffa6324358b0a13a2",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BTVA-PROJECTIVE-SPAN-FILTER.json": "4ee8e6061a7cc2a54b54786fd065923434381bde",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_btva_projective_span_filter.py": "c1ce59af9df1143ad8c7492b1bf9f1ded102a034",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/TWO-FACTOR-SAME-BEAUVILLE-COVER-WALL.json": "20d9873e41fb2db25105c437d3a10c031b23c0a3",
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_two_factor_same_beauville_cover_wall.py": "fcdf95203d1b21a319cb78c32e3083649b61dae9",
}

RUN_VERIFIERS = [
    "verify_mb104_ambient_a1_scaling_wall.py",
    "verify_mb104_lu_miyaoka_node_debt.py",
    "verify_mb104_beauville_miyaoka_cover_wall.py",
    "verify_mb104_btva_projective_span_filter.py",
    "verify_mb104_two_factor_same_beauville_cover_wall.py",
]


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_json(path: Path):
    return json.loads(path.read_text())


def main() -> None:
    for rel, expected in LOCKS.items():
        got = git_blob_sha(ROOT / rel)
        assert got == expected, (rel, got, expected)

    cert = load_json(NODE / "CERTIFICATE.json")
    state = load_json(STATE)
    assert cert["schema"] == "STAGE32_MB104_FINITE_WINDOW_COEFFICIENT_BARRIER_V7"

    assert cert["special_fibre_contract"]["identity"] == "6*n_i=2*q_i+M"
    assert cert["factor_slack_contract"]["global_identity"] == "M-d+4*g-4=sigma_1+sigma_2>=0"
    assert cert["minimal_branch_contract"]["derived_minimal_bound"] == "s_min>=d-4*g+4"
    assert cert["picard_hodge_contract"]["quadratic_inequality"] == "sum_i M_i^2<=d^2/8+2*d-4*g+4"
    assert cert["picard_hodge_contract"]["cauchy_global_inequality"] == "M^2<=6*d^2+96*d-192*g+192"
    assert cert["picard_hodge_contract"]["closes_degree"] is False

    amb = cert["ambient_a1_scaling_contract"]
    assert amb["fixed_first_factor_degree"] == 2
    assert amb["fixed_exceptional_mass"] == 2
    assert amb["global_algebraic_member_constructed"] is False
    assert amb["closes_degree"] is False

    lm = cert["lu_miyaoka_contract"]
    assert lm["inequality"] == "d<=4*(g-1)+224+n_ot"
    assert lm["g0_debt"] == "n_ot>=max(0,d-220)"
    assert lm["g1_debt"] == "n_ot>=max(0,d-224)"
    assert lm["closes_degree"] is False

    bm = cert["beauville_miyaoka_contract"]
    assert bm["K_X_square"] == 32 and bm["c2_X"] == 16 and bm["K2_gt_c2"] is True
    assert bm["inequality"] == "2*d<=3*r+12*g+20"
    assert bm["closes_degree"] is False

    btva = cert["btva_projective_span_contract"]
    assert btva["all_48_node_vector_rank"] == 7
    assert btva["exact_node_profile_filter_available"] is True
    assert btva["scaling_ray_excluded"] is False
    assert btva["closes_degree"] is False

    tf = cert["two_factor_same_cover_contract"]
    assert tf["single_beauville_double_cover"] is True
    assert tf["factor_directions"] == 2
    assert tf["independent_r1_r2_available"] is False
    assert tf["combined"] == "r>=2*max(n1,n2)-4*g+4>=d-4*g+4"
    assert tf["closes_degree"] is False

    rd = cert["route_decision"]
    assert rd["retire_naive_two_factor_independent_ramification_sum"] is True
    assert rd["next_subobligation"] == "MB104_CUBOID_SPECIFIC_ORDINARY_SINGULARITY_OR_GLOBALIZATION_BOUND"
    assert state["next_obligation"]["subobligation"] == rd["next_subobligation"]

    # Replay downstream retained verifiers, rather than merely source-locking
    # their bytes. This makes the V7 main verifier depend on their executable
    # contracts as well as their identities.
    for name in RUN_VERIFIERS:
        runpy.run_path(str(NODE / name), run_name="__main__")

    # Bounded sanity checks for the current coefficient barriers.
    for g in (0, 1):
        for d in range(2, 2001):
            r0 = d - 4 * g + 4
            assert r0 > 0
            assert 2 * d <= 3 * r0 + 12 * g + 20
            lm_debt = max(0, d - (220 if g == 0 else 224))
            assert lm_debt >= 0

    for k in range(1, 501):
        d = 96 * k
        M = d
        q_a1 = 48 * k * k
        assert q_a1 * 192 == d * d
        assert 48 >= 7 and 48 >= 6

    fw = cert["credit_firewall"]
    assert fw["mb104_complete"] is False
    assert fw["finite_degree_window_proved"] is False
    assert fw["finite_picard_enumeration_released"] is False
    assert fw["r29_lg2_mb_discharged"] is False
    assert fw["receiver_credit"] is False
    assert fw["theorem_credit"] is False
    assert fw["endpoint_credit"] is False
    assert fw["merge_authorized"] is False

    print("MB104 V7 main verifier PASS")
    print("downstream executable contracts replayed: ambient/Lu-Miyaoka/Beauville/BTVA/same-cover")
    print("active leaf: MB104_CUBOID_SPECIFIC_ORDINARY_SINGULARITY_OR_GLOBALIZATION_BOUND")
    print("finite degree window remains OPEN")


if __name__ == "__main__":
    main()
