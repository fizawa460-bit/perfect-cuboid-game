#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-RELATIVE-H-SUPPORT-INTERSECTION-CERTIFICATE.json"
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RELATIVE-H-SUPPORT-INTERSECTION.md",
        "006ba1211b58c05f01aba2a14d3c2abb93f3257d",
    ),
    "FSM_COORD_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FREITAG-SALVATI-MANNI-RESIDUAL-KUMMER-COORDINATE-SOURCE-NOTE.md",
        "a49f5b28b456dd88436c030e857cf771e5a1ba2f",
    ),
    "MODULAR_CHARACTER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-MODULAR-CONDUCTOR-DECK-CHARACTER.md",
        "ce9554bc047159baf7640db50aa5daf1f0c67f74",
    ),
    "AUT_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/AUTS-NODE-ACTION-SOURCE-NOTE.md",
        "cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693",
    ),
    "SUPPORT_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION-CERTIFICATE.json",
        "31695c6908cff73d04baab2ed11dfd04608a2464",
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

def nodes():
    out = []
    for j in range(3):
        for sa in (1, -1):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    z = [0j] * 7
                    z[j] = sa
                    o = [t for t in range(3) if t != j]
                    z[3 + o[0]], z[3 + o[1]], z[6] = s1, s2, 1
                    out.append(tuple(z))
    for j in range(3):
        o = [t for t in range(3) if t != j]
        a, b = o
        for sr in (1, -1):
            for ep in (1, -1):
                for eq in (1, -1):
                    z = [0j] * 7
                    z[a], z[b], z[3 + a], z[3 + b] = 1, 1j * sr, 1j * ep, -eq * sr
                    out.append(tuple(z))
    req(len(out) == 48 and len(set(out)) == 48, "48-node model")
    return out

def projectively_equal(p, q):
    k = next((i for i, x in enumerate(p) if x != 0), None)
    req(k is not None, "zero projective point")
    if q[k] == 0:
        return False
    return all(p[i] * q[k] == q[i] * p[k] for i in range(7))

def transform(p, flips):
    q = list(p)
    for i in flips:
        q[i] = -q[i]
    return tuple(q)

def permutation(v, flips):
    out = {}
    for i, p in enumerate(v):
        q = transform(p, flips)
        hits = [j for j, r in enumerate(v) if projectively_equal(q, r)]
        req(len(hits) == 1, f"unique node image P{i}")
        out[i] = hits[0]
    req(len(set(out.values())) == 48, "node permutation")
    return out

def class_intersection(overlap):
    # D = 7l H - 4l sum E_p, H^2=16, E_p^2=-2.
    return 49 * 16 - 32 * overlap

def main():
    rr = root()
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_000707_E2_RELATIVE_H_SUPPORT_INTERSECTION_V1", "schema")
    req(cert["active_leaf"] == ACTIVE, "active leaf")

    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    for key, (rel, want) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"missing source {key}")
        req(blob(p) == want, f"SOURCE_LOCK_FAIL {key}")

    req(cert["evidence"]["verifier_blob_sha1"] == blob(Path(__file__)), "verifier identity")

    support_cert = json.loads((rr / LOCKS["SUPPORT_CERT"][0]).read_text())
    sc = support_cert["support_stabilizers"]["000707000f0f"]
    req(sc["support_orbit_size"] == 768, "support orbit size")
    req(sc["omitted_node_set"] == [27, 35], "support omitted nodes")
    req(support_cert["scope"]["divisor_ray"] == "D_l=7lH-4l sum_{i in Sigma}E_i", "divisor ray")

    mask = int("000707000f0f", 16)
    support = [i for i in range(48) if (mask >> i) & 1]
    expected_support = [0,1,2,3,8,9,10,11,24,25,26,32,33,34]
    req(support == expected_support, "support decode")

    v = nodes()
    actions = {
        "beta_b1": ([3], {
            0:0,1:1,2:2,3:3,8:10,9:11,10:8,11:9,
            24:24,25:25,26:26,32:34,33:35,34:32,
        }),
        "beta_b2": ([4], {
            0:2,1:3,2:0,3:1,8:8,9:9,10:10,11:11,
            24:26,25:27,26:24,32:32,33:33,34:34,
        }),
        "beta_b1b2": ([3,4], {
            0:2,1:3,2:0,3:1,8:10,9:11,10:8,11:9,
            24:26,25:27,26:24,32:34,33:35,34:32,
        }),
    }
    expected_images = {
        "beta_b1": [0,1,2,3,8,9,10,11,24,25,26,32,34,35],
        "beta_b2": [0,1,2,3,8,9,10,11,24,26,27,32,33,34],
        "beta_b1b2": [0,1,2,3,8,9,10,11,24,26,27,32,34,35],
    }
    expected_overlaps = {"beta_b1":13, "beta_b2":13, "beta_b1b2":12}
    expected_intersections = {"beta_b1":368, "beta_b2":368, "beta_b1b2":400}
    expected_diff_squares = {"beta_b1":-64, "beta_b2":-64, "beta_b1b2":-128}

    for name, (flips, expected_map) in actions.items():
        p = permutation(v, flips)
        got_map = {i:p[i] for i in support}
        req(got_map == expected_map, f"{name} support permutation")
        image = sorted(p[i] for i in support)
        req(image == expected_images[name], f"{name} image support")
        overlap = len(set(support) & set(image))
        req(overlap == expected_overlaps[name], f"{name} overlap")
        inter = class_intersection(overlap)
        req(inter == expected_intersections[name], f"{name} class intersection")
        diff_sq = 2 * 336 - 2 * inter
        req(diff_sq == expected_diff_squares[name], f"{name} difference square")

    exact = cert["exact_relative_h_geometry"]
    req(exact["support_nodes"] == expected_support, "certificate support")
    req(exact["overlap_counts"] == expected_overlaps, "certificate overlap counts")
    req(exact["intersection_coefficients_l2"] == expected_intersections, "certificate intersections")
    req(exact["difference_square_coefficients_l2"] == expected_diff_squares, "certificate difference squares")
    req(exact["D_self_intersection_coefficient_l2"] == 336, "self intersection")

    route = cert["routing_consequence"]
    req(route["relative_H_is_residual_G_mod_H_deck"] is False, "semantic firewall")
    req(route["conductor_pair_adapter_proved"] is False, "no conductor adapter")
    req(route["weighted_cut_bound_proved"] is False, "no cut bound")
    req(route["active_leaf_unchanged"] is True, "leaf unchanged")

    fw = cert["credit_firewall"]
    req(all(v is False for v in fw.values()), "all closure/credit/heavy/merge flags false")

    print("PASS STAGE32_MB104_000707_E2_RELATIVE_H_SUPPORT_INTERSECTION_V1")
    print("overlaps: beta_b1=13 beta_b2=13 beta_b1b2=12")
    print("intersections/l^2: 368 368 400; conductor transition remains open; credit 0")

if __name__ == "__main__":
    main()
