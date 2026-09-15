#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-A1-LIFT-ENERGY-IDENTITY-CERTIFICATE.json"
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
LOCKS = {
    "HUMAN_NOTE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-A1-LIFT-ENERGY-IDENTITY.md", "3fb4152c35b88160f36730fac941f542566664a8"),
    "EQUALITY_RIGIDITY": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY.md", "a20547082b1ea2f786b1272d1b76af3527508e9b"),
    "INTERMEDIATE_H": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-INTERMEDIATE-H-QUOTIENT-MODEL.md", "d2e3056137360a9e15ae7c820088d2977a5eb137"),
    "NODE_ORBIT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE.md", "dbfea5a4f62b1388c9810c37ad867076ed4dca6e"),
    "SPLIT_HODGE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SPLIT-HODGE-CONDUCTOR.md", "b8f876f78fa23a64911baa4b9057f7920bfea014"),
    "A1_DELTA": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/A1-CONDUCTOR-BRANCH-DELTA-WALL.md", "a4de57f430aea249300c589aeeeaa3dbe67d5006"),
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


def energy(l, xs):
    return sum(x * (8*l - x) for x in xs)


def main():
    rr = root()
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_000707_E2_A1_LIFT_ENERGY_IDENTITY_V1", "schema")
    req(cert["active_leaf"] == ACTIVE, "active leaf")

    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    for key, (rel, want) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"missing {key}")
        req(blob(p) == want, f"SOURCE_LOCK_FAIL {key}")
    req(cert["evidence"]["verifier_blob_sha1"] == blob(Path(__file__)), "verifier identity")

    exact = cert["exact_identity"]
    n_coeff = 28
    product_intersection = 2 * n_coeff * n_coeff
    req(product_intersection == 1568, "Z.TZ coefficient")
    req(product_intersection // 4 == 392, "X_H pre-resolution coefficient")
    req(exact["projection_degree_coefficient"] == n_coeff, "projection degree")
    req(exact["product_intersection_coefficient_l2"] == 1568, "product intersection")
    req(exact["intermediate_intersection_coefficient_l2"] == 392, "intermediate intersection")

    support = exact["support_nodes"]
    req(support == [0,1,2,3,8,9,10,11,24,25,26,32,33,34], "support")
    req(len(support) == 14, "support size")
    req(exact["branches_per_supported_node_coefficient"] == 8, "8l branches")
    req(exact["a1_exceptional_self_intersection"] == -2, "A1 exceptional square")
    req(exact["node_resolution_correction"] == "x_j*(8*l-x_j)", "node correction")
    req(exact["y_formula"] == "392*l^2-sum_j x_j*(8*l-x_j)", "y formula")
    req(exact["centered_y_formula"] == "168*l^2+(1/4)*sum_j d_j^2", "centered y")
    req(exact["weighted_cut_formula"] == "84*l^2+(1/8)*sum_j d_j^2", "weighted cut")
    req(exact["same_sheet_formula"] == "84*l^2+56*l-(1/8)*sum_j d_j^2", "same-sheet formula")

    # Replay the centered algebra for several l and allocation patterns, including
    # both retained formal saturation witnesses from the node-orbit note.
    for l in range(1, 9):
        patterns = [
            [4*l] * 14,
            [0] * 14,
            [8*l] * 14,
            [5*l,4*l,3*l,4*l,4*l,4*l,4*l,5*l,3*l,4*l,4*l,4*l,4*l,4*l],
        ]
        for xs in patterns:
            req(all(0 <= x <= 8*l for x in xs), "allocation bounds")
            ds = [2*x - 8*l for x in xs]
            s = energy(l, xs)
            req(392*l*l - s == 168*l*l + sum(d*d for d in ds)//4, "energy-y algebra")
            lhs8 = 4 * (392*l*l - s)
            rhs8 = 8 * 84*l*l + sum(d*d for d in ds)
            req(lhs8 == rhs8, "weighted-cut algebra")
            same8 = 8*(168*l*l + 56*l) - lhs8
            req(same8 == 8*(84*l*l + 56*l) - sum(d*d for d in ds), "same-sheet algebra")

    # Per-node convexity makes the Hodge threshold automatic.
    for l in range(1, 9):
        for x in range(0, 8*l + 1):
            req(x*(8*l-x) <= 16*l*l, "node energy maximum")
        req(392*l*l - 14*16*l*l == 168*l*l, "Hodge minimum")

    route = cert["routing_consequence"]
    req(route["hodge_threshold_automatic_from_identity"] is True, "Hodge route diagnosis")
    req(route["individual_conductor_pair_map_materialized"] is False, "no pair map")
    req(route["e2_closed"] is False, "e2 open")
    req(route["active_leaf_unchanged"] is True, "active leaf unchanged")

    fw = cert["credit_firewall"]
    req(all(v is False for v in fw.values()), "credit firewall")

    print("PASS STAGE32_MB104_000707_E2_A1_LIFT_ENERGY_IDENTITY_V1")
    print("y=168*l^2+(1/4)sum d_j^2; y/2=84*l^2+(1/8)sum d_j^2")
    print("Hodge threshold automatic; e=2 remains open; credit 0")


if __name__ == "__main__":
    main()
