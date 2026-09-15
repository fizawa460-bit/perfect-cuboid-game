#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-ANTIINVARIANT-CLASS-DECOMPOSITION-CERTIFICATE.json"
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ANTIINVARIANT-CLASS-DECOMPOSITION.md",
        "8217f81e6ee176f4b760a5609a6048bf823b3721",
    ),
    "ENERGY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-A1-LIFT-ENERGY-IDENTITY-CERTIFICATE.json",
        "0cec993c9d22e31fcf982985b37f0ae82c8cbce7",
    ),
    "NODE_ORBIT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE.md",
        "dbfea5a4f62b1388c9810c37ad867076ed4dca6e",
    ),
    "SPLIT_HODGE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SPLIT-HODGE-CONDUCTOR.md",
        "b8f876f78fa23a64911baa4b9057f7920bfea014",
    ),
    "HALF_BRANCH": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS.md",
        "e22de5a6f4be163268e699cde03d37e1e564d43b",
    ),
    "INTERMEDIATE_H": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL.md",
        "d2e3056137360a9e15ae7c820088d2977a5eb137",
    ),
}


def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main():
    rr = root()
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_000707_E2_ANTIINVARIANT_CLASS_DECOMPOSITION_V1", "schema")
    req(cert["active_leaf"] == ACTIVE, "active leaf")

    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    for key, (rel, want) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"missing source {key}")
        req(blob(p) == want, f"SOURCE_LOCK_FAIL {key}")

    req(cert["evidence"]["verifier_blob_sha1"] == blob(Path(__file__)), "verifier identity")

    exact = cert["exact_numerical_decomposition"]
    support = [0,1,2,3,8,9,10,11,24,25,26,32,33,34]
    req(exact["support_nodes"] == support, "support nodes")
    req(exact["supported_exceptional_preimage"] == "E_j^+ disjoint_union E_j^-", "split exceptional")
    req(exact["F_j_square"] == -4, "F_j square")
    req(exact["F_i_F_j_for_i_ne_j"] == 0, "F orthogonality")
    req(exact["v_F_j"] == "2*d_j", "v.F_j")
    req(exact["v_square"] == "-sum_j d_j^2", "v square")
    req(exact["exceptional_projection"] == "-sum_j (d_j/2)*F_j", "projection")
    req(exact["numerical_remainder_square"] == 0, "remainder square")
    req(exact["numerical_class"] == "C_1-C_2 == -sum_j (d_j/2)*(E_j^+-E_j^-)", "class formula")

    # Local algebra: d=2x-8l is even; F^2=-4 and v.F=2d force
    # projection coefficient -d/2 and projection norm -d^2.
    for l in range(1, 5):
        for x in range(0, 8*l + 1):
            d = 2*x - 8*l
            req(d % 2 == 0, "d parity")
            a = -d // 2
            req(a * (-4) == 2*d, "projection pairing")
            req(a*a*(-4) == -(d*d), "projection norm")

    # Global coefficient identity imported from the retained energy certificate:
    # v^2 = 2*C^2 - 4*y, C^2=336l^2,
    # y=168l^2 + (1/4)S, hence v^2=-S.
    for l in range(1, 5):
        for S4 in (0, 4, 16, 64, 256):
            # S4 stands for an admissible sample sum of even squares, divisible by 4.
            four_v2 = 4*(2*336*l*l) - 16*(168*l*l) - 4*S4
            req(four_v2 == -4*S4, "energy-to-v-square")

    route = cert["routing_consequence"]
    req(route["hidden_numerical_antiinvariant_direction_remaining"] is False, "no hidden numerical direction")
    req(route["linear_equivalence_claimed"] is False, "no linear-equivalence overclaim")
    req(route["individual_conductor_pair_map_materialized"] is False, "no conductor map")
    req(route["e2_closed"] is False, "e2 remains open")
    req(route["active_leaf_unchanged"] is True, "active leaf unchanged")

    fw = cert["credit_firewall"]
    req(all(v is False for v in fw.values()), "all credit/heavy/merge flags false")

    print("PASS STAGE32_MB104_000707_E2_ANTIINVARIANT_CLASS_DECOMPOSITION_V1")
    print("v == -sum_j (d_j/2)F_j numerically; hidden numerical anti-invariant remainder = 0; credit 0")


if __name__ == "__main__":
    main()
