#!/usr/bin/env python3
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-RELATIVE-G-FOURIER-CHARACTER-CERTIFICATE.json"
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
LOCKS = {
    "HUMAN_NOTE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RELATIVE-G-FOURIER-CHARACTER.md", "42b70776bde2259efce03d500d76fba837a5cf36"),
    "FSM_COORD_SOURCE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FREITAG-SALVATI-MANNI-RESIDUAL-KUMMER-COORDINATE-SOURCE-NOTE.md", "a49f5b28b456dd88436c030e857cf771e5a1ba2f"),
    "AUT_SOURCE": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/AUTS-NODE-ACTION-SOURCE-NOTE.md", "cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693"),
    "MODULAR_CHARACTER": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-MODULAR-CONDUCTOR-DECK-CHARACTER.md", "ce9554bc047159baf7640db50aa5daf1f0c67f74"),
    "RELATIVE_H_REFINEMENT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RELATIVE-H-SUPPORT-INTERSECTION.md", "006ba1211b58c05f01aba2a14d3c2abb93f3257d"),
    "NODE_MODEL_VERIFIER": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_e2_residual_node_orbit_table.py", "ebecc69e32533c56926ccd104589a3a77cd93221"),
    "SUPPORT_CERT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-STABILIZER-UNION-CERTIFICATE.json", "31695c6908cff73d04baab2ed11dfd04608a2464"),
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


def projective_equal(x, y):
    k = next((i for i, v in enumerate(y) if v != 0), None)
    if k is None or x[k] == 0:
        return False
    lam = x[k] / y[k]
    return all(xi == lam * yi for xi, yi in zip(x, y))


def sign_flip_perm(V, bits):
    out = []
    for p in V:
        q = list(p)
        for k, bit in enumerate(bits):
            if bit:
                q[3 + k] = -q[3 + k]
        hits = [j for j, v in enumerate(V) if projective_equal(tuple(q), v)]
        req(len(hits) == 1, f"projective node match {bits}")
        out.append(hits[0])
    req(len(set(out)) == 48, f"permutation {bits}")
    return out


def rank_q(rows):
    if not rows:
        return 0
    A = [[Fraction(x) for x in row] for row in rows]
    m, n = len(A), len(A[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if A[i][c] != 0), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        z = A[r][c]
        A[r] = [x / z for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                z = A[i][c]
                A[i] = [a - z * b for a, b in zip(A[i], A[r])]
        r += 1
        if r == m:
            break
    return r


def dot_bits(a, b):
    return sum(x * y for x, y in zip(a, b)) % 2


def xor(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def main():
    rr = root()
    cert = json.loads(CERT.read_text())
    req(cert["schema"] == "STAGE32_MB104_000707_E2_RELATIVE_G_FOURIER_CHARACTER_V1", "schema")
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "source-lock table")
    for key, (rel, want) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"missing {key}")
        req(blob(p) == want, f"source lock {key}")
    req(cert["evidence"]["verifier_blob_sha1"] == blob(Path(__file__)), "verifier identity")

    support_cert = json.loads((rr / LOCKS["SUPPORT_CERT"][0]).read_text())
    req(support_cert["support_stabilizers"]["000707000f0f"]["omitted_node_set"] == [27, 35], "support certificate")

    V = nodes()
    G = list(itertools.product((0, 1), repeat=3))
    perms = {g: sign_flip_perm(V, g) for g in G}
    support = [0,1,2,3,8,9,10,11,24,25,26,32,33,34]
    expected = {
        (0,0,0): [0,1,2,3,8,9,10,11,24,25,26,32,33,34],
        (0,0,1): [0,1,2,3,8,9,10,11,24,25,27,32,33,35],
        (0,1,0): [0,1,2,3,8,9,10,11,24,26,27,32,33,34],
        (0,1,1): [0,1,2,3,8,9,10,11,25,26,27,32,33,35],
        (1,0,0): [0,1,2,3,8,9,10,11,24,25,26,32,34,35],
        (1,0,1): [0,1,2,3,8,9,10,11,24,25,27,33,34,35],
        (1,1,0): [0,1,2,3,8,9,10,11,24,26,27,32,34,35],
        (1,1,1): [0,1,2,3,8,9,10,11,25,26,27,33,34,35],
    }
    orbit = {g: sorted(perms[g][i] for i in support) for g in G}
    req(orbit == expected, "eight-support orbit")

    overlaps = {g: len(set(support) & set(orbit[g])) for g in G}
    req(overlaps[(0,0,0)] == 14, "self overlap")
    req(overlaps[(1,0,0)] == 13 and overlaps[(0,1,0)] == 13, "H single overlaps")
    req(overlaps[(1,1,0)] == 12, "H product overlap")
    req(all(overlaps[g] == 12 for g in G if g[2] == 1), "residual-coset overlaps")

    kernel = {g: 784 - 32 * overlaps[g] for g in G}
    req(kernel[(0,0,0)] == 336, "self intersection")
    req(kernel[(1,0,0)] == kernel[(0,1,0)] == 368, "single H intersections")
    req(kernel[(1,1,0)] == 400, "double H intersection")
    req(all(kernel[g] == 400 for g in G if g[2] == 1), "residual-coset intersections")

    # Unit-l divisor vectors: [H, E0,...,E47].
    dvec = {}
    for g in G:
        S = set(orbit[g])
        dvec[g] = [7] + [-4 if i in S else 0 for i in range(48)]
    req(rank_q(list(dvec.values())) == 6, "orbit Picard rank")

    def lincomb(coeff):
        return [sum(coeff[g] * dvec[g][j] for g in G) for j in range(49)]

    r0 = {g: 0 for g in G}
    r0[(0,0,0)], r0[(0,1,0)], r0[(1,0,0)], r0[(1,1,0)] = 1,-1,-1,1
    r1 = {g: 0 for g in G}
    r1[(0,0,1)], r1[(0,1,1)], r1[(1,0,1)], r1[(1,1,1)] = 1,-1,-1,1
    req(all(x == 0 for x in lincomb(r0)), "relation R0")
    req(all(x == 0 for x in lincomb(r1)), "relation R1")

    # Residual character is c, i.e. sign (-1)^c.
    cres = {g: (1 if g[2] == 0 else -1) for g in G}
    F = lincomb(cres)
    expected_F = [0] * 49
    kres = {24:-1,25:1,26:-1,27:1,32:-1,33:1,34:-1,35:1}
    for i, a in kres.items():
        expected_F[1+i] = 8 * a
    req(F == expected_F, "residual Fourier class")

    # Intersection form on H,E_i basis.
    kres_sq = -2 * sum(a*a for a in kres.values())
    req(kres_sq == -16, "K_res square")
    d_dot_k = sum((-4 if i in support else 0) * a * (-2) for i, a in kres.items())
    req(d_dot_k == -16, "D.K_res unit-l coefficient")
    req(64 * kres_sq == -1024, "F_res square unit-l2 coefficient")
    req(8 * d_dot_k == -128, "D.F_res unit-l2 coefficient")

    spectrum = {}
    for chi in G:
        spectrum[chi] = sum(kernel[g] * (1 if dot_bits(chi, g) == 0 else -1) for g in G)
    expected_spectrum = {
        (0,0,0):3072,
        (0,0,1):-128,
        (0,1,0):-64,
        (0,1,1):-64,
        (1,0,0):-64,
        (1,0,1):-64,
        (1,1,0):0,
        (1,1,1):0,
    }
    req(spectrum == expected_spectrum, "Fourier spectrum")

    c = cert["exact_character_refinement"]
    req(c["orbit_picard_rank"] == 6, "certificate rank")
    req(c["residual_character_kernel"] == "c=0=<beta1,beta2>", "certificate character kernel")
    req(c["residual_coset_overlap"] == 12, "certificate coset overlap")
    req(c["residual_coset_intersection_l2"] == 400, "certificate coset intersection")
    req(c["K_res"] == "-E24+E25-E26+E27-E32+E33-E34+E35", "certificate K_res")
    req(c["K_res_square"] == -16, "certificate K_res square")
    req(c["D_dot_K_res"] == "-16*l", "certificate D.K_res")
    req(c["F_res_square"] == "-1024*l^2", "certificate F square")
    req(c["D_dot_F_res"] == "-128*l^2", "certificate D.F")
    req(c["conductor_transition_computed"] is False, "no conductor transition")
    req(c["weighted_cut_bound_proved"] is False, "no cut bound")

    route = cert["routing"]
    req(route["active_leaf"] == ACTIVE, "active leaf")
    req(route["residual_character_picard_channel_materialized"] is True, "character channel")
    req(route["branch_to_relative_translate_adapter_missing"] is True, "adapter remains missing")

    fw = cert["credit_firewall"]
    req(all(v is False for v in fw.values()), "all credit/closure/heavy/merge flags false")

    print("PASS STAGE32_MB104_000707_E2_RELATIVE_G_FOURIER_CHARACTER_V1")
    print("orbit: rank 6; two exact parallelogram relations")
    print("residual coset: four translates, each overlap 12 and intersection 400*l^2")
    print("chi_res Fourier: F_res=8*l*K_res, K_res^2=-16, D.K_res=-16*l")
    print("open: branch/conductor -> relative transition adapter; credit 0")


if __name__ == "__main__":
    main()
