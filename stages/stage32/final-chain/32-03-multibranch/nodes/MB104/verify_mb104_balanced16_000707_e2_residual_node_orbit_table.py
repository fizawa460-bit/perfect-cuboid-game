#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE-CERTIFICATE.json"
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
LOCKS = {
    "HUMAN_NOTE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE.md", "dbfea5a4f62b1388c9810c37ad867076ed4dca6e"),
    "FSM_COORD_SOURCE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FREITAG-SALVATI-MANNI-RESIDUAL-KUMMER-COORDINATE-SOURCE-NOTE.md", "a49f5b28b456dd88436c030e857cf771e5a1ba2f"),
    "EXPLICIT_KUMMER": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EXPLICIT-RESIDUAL-KUMMER-COORDINATE.md", "5017d7c137f6d4994a34cb1edac28aadcd832a2a"),
    "MODULAR_CHARACTER": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-MODULAR-CONDUCTOR-DECK-CHARACTER.md", "ce9554bc047159baf7640db50aa5daf1f0c67f74"),
    "NODE_MODEL_VERIFIER": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_two_quartic_gluing.py", "20b49289677b5f7b6f5370107b286ac977fe6a11"),
    "SUPPORT_CERT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION-CERTIFICATE.json", "31695c6908cff73d04baab2ed11dfd04608a2464"),
    "SATURATION_CERT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION-CERTIFICATE.json", "1f51cf157b3de6db393049af41fda0843e0f2068")
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

def inv_triple(P):
    W1, W2, W3, Z1, Z2, Z3, C = P
    dz = W1 - 1j * W2
    dw = W1 + 1j * W2
    dp = C - W3
    req(dz != 0 and dw != 0 and dp != 0, "finite residual chart")
    rz2 = 2 * (C + W3) / dz
    rw2 = 2 * (C + W3) / dw
    prod = 2 * Z3 / dp
    return (rz2, rw2, prod)

def normz(z):
    def n(x):
        if abs(x) < 1e-12:
            return 0
        y = round(x)
        req(abs(x-y) < 1e-12, "Gaussian-integer invariant")
        return int(y)
    return [n(z.real), n(z.imag)]

def encoded(t):
    return [normz(z) for z in t]

def q0_value(x):
    return x[0]-x[1]+x[2]-x[3]-x[24]+x[25]-x[26]

def q1_value(x):
    return sum(x[i] for i in (8,9,10,11,32,33,34))

def main():
    rr = root()
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_000707_E2_RESIDUAL_NODE_ORBIT_TABLE_V1", "schema")
    declared = {x["id"]:(x["path"],x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    for key, (rel, want) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"missing {key}")
        req(blob(p) == want, f"source lock {key}")
    req(cert["evidence"]["verifier_blob_sha1"] == blob(Path(__file__)), "verifier identity")

    support_cert = json.loads((rr / LOCKS["SUPPORT_CERT"][0]).read_text())
    sat = json.loads((rr / LOCKS["SATURATION_CERT"][0]).read_text())
    req(support_cert["support_stabilizers"]["000707000f0f"]["omitted_node_set"] == [27,35], "omitted nodes")
    req(sat["support"]["mask"] == "000707000f0f", "saturation support")
    req(sat["support"]["branches_per_supported_node"] == "8*l", "branch packet")
    req(sat["fiber_saturation"]["e2"]["each_fiber_reduced_cardinality"] == "28*l", "e2 saturation")

    V = nodes()
    mask = int("000707000f0f", 16)
    support = [i for i in range(48) if (mask >> i) & 1]
    expected_support = [0,1,2,3,8,9,10,11,24,25,26,32,33,34]
    req(support == expected_support, "support decode")

    expected = {
        0:[[2,0],[2,0],[2,0]], 2:[[2,0],[2,0],[2,0]],
        1:[[2,0],[2,0],[-2,0]], 3:[[2,0],[2,0],[-2,0]],
        24:[[-2,0],[2,0],[0,-2]], 26:[[-2,0],[2,0],[0,-2]],
        25:[[-2,0],[2,0],[0,2]],
        8:[[0,2],[0,-2],[2,0]], 10:[[0,2],[0,-2],[2,0]],
        9:[[0,2],[0,-2],[-2,0]], 11:[[0,2],[0,-2],[-2,0]],
        32:[[0,2],[0,2],[0,-2]], 34:[[0,2],[0,2],[0,-2]],
        33:[[0,2],[0,2],[0,2]],
    }
    for i in support:
        req(encoded(inv_triple(V[i])) == expected[i], f"residual orbit P{i}")
    req(encoded(inv_triple(V[27])) == expected[25], "P27 residual orbit equals P25")
    req(encoded(inv_triple(V[35])) == expected[33], "P35 residual orbit equals P33")

    tab = cert["exact_residual_orbits"]
    req(tab["support_nodes"] == expected_support, "certificate support")
    req(tab["simultaneous_deck_action"] == "(r_z,r_w)->(-r_z,-r_w)", "deck action")
    req(tab["per_normalization_branch_member_selected"] is False, "no branch selection")

    half = {i:4 for i in support}
    alt = dict(half)
    alt[0], alt[2], alt[8], alt[9] = 5,3,5,3
    for alloc in (half, alt):
        req(all(0 <= alloc[i] <= 8 for i in support), "formal allocation bounds")
        req(q0_value(alloc) == -4, "Q0 saturation in units l")
        req(q1_value(alloc) == 28, "Q1 saturation in units l")
    req(half != alt, "nonunique formal allocations")

    sc = cert["saturation_constraints"]
    req(sc["q0"] == "x0-x1+x2-x3-x24+x25-x26=-4*l", "Q0 equation")
    req(sc["q1"] == "x8+x9+x10+x11+x32+x33+x34=28*l", "Q1 equation")
    req(sc["branch_allocation_unique_from_current_data"] is False, "allocation remains open")
    req(sc["formal_nonuniqueness_witnesses_geometrically_realized"] is False, "formal-only witness firewall")

    route = cert["routing_consequence"]
    req(route["active_leaf"] == ACTIVE, "active leaf")
    req(route["node_to_residual_orbit_materialized"] is True, "orbit materialized")
    req(route["per_branch_orbit_member_missing"] is True, "per-branch selection missing")
    req(route["conductor_transition_missing"] is True, "transition missing")
    req(route["weighted_cut_bound_proved"] is False, "no cut bound")

    fw = cert["credit_firewall"]
    req(all(v is False for v in fw.values()), "all closure/credit/heavy/merge flags false")

    print("PASS STAGE32_MB104_000707_E2_RESIDUAL_NODE_ORBIT_TABLE_V1")
    print("materialized: 14 supported node -> exact residual R x R simultaneous-sign orbit")
    print("derived: exact Q0/Q1 28l/28l saturation equations")
    print("open: per-branch orbit member, conductor transition, chi_res weighted cut; credit 0")

if __name__ == "__main__":
    main()
