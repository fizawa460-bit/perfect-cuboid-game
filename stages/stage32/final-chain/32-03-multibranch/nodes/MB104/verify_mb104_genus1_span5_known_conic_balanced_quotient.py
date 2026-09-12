#!/usr/bin/env python3
import hashlib
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT-CERTIFICATE.json"

LOCKS = {
    "FORMAL_PICARD": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY.md",
        "de83fc169814681109bcbc1576ad24f67d6159e0",
    ),
    "AUT_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/AUTS-NODE-ACTION-SOURCE-NOTE.md",
        "cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693",
    ),
    "AUT_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-HYPERPLANE-AUT-ORBIT-CERTIFICATE.json",
        "3bc4453affce96e87a60864c99f745bb4c28c794",
    ),
    "SECTION_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-SECTION-COMPONENTS-20-19-16-CERTIFICATE.json",
        "9c36555e495df0d8d6b816f1c0dc7d4c35b55848",
    ),
    "CAPACITY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-UNIFORM-RAY-COMPONENT-CAPACITY-CERTIFICATE.json",
        "f6fdfdf33d41a0c35a10dad911a2a78c33dec640",
    ),
    "KNOWN_CONIC_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/KNOWN-CONIC-MULTIBRANCH-CERTIFICATE.json",
        "b425ba24932632d28752899c6ad11cd530c7de6c",
    ),
}

P = 1097
II = 341


def require(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root not found")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def source_lock_preflight(cert):
    rr = root()
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    require(declared == LOCKS, "certificate/source-lock table mismatch")
    for key, (rel, sha) in LOCKS.items():
        p = rr / rel
        if not p.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL: missing {key}: {rel}")
        got = blob_sha1(p)
        if got != sha:
            raise SystemExit(f"SOURCE_LOCK_FAIL: {key}: expected {sha}, got {got}")


def nodes():
    out = []
    for j in range(3):
        for sa in (1, -1):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    z = [0j] * 7
                    z[j] = sa
                    o = [t for t in range(3) if t != j]
                    z[3 + o[0]] = s1
                    z[3 + o[1]] = s2
                    z[6] = 1
                    out.append(tuple(z))
    for j in range(3):
        o = [t for t in range(3) if t != j]
        a, b = o
        for sr in (1, -1):
            for ep in (1, -1):
                for eq in (1, -1):
                    z = [0j] * 7
                    z[a] = 1
                    z[b] = 1j * sr
                    z[3 + a] = 1j * ep
                    z[3 + b] = -eq * sr
                    out.append(tuple(z))
    require(len(out) == 48 and len(set(out)) == 48, "48-node model")
    return out


V = nodes()


def peq(a, b):
    k = next((j for j, x in enumerate(a) if x != 0), None)
    if k is None or b[k] == 0:
        return False
    return all(a[j] * b[k] == b[j] * a[k] for j in range(7))


def apply(x, src, cf):
    return tuple(cf[j] * x[src[j]] for j in range(7))


def generators():
    specs = []
    specs.append(([1, 0, 2, 4, 3, 5, 6], [1] * 7))
    specs.append(([2, 1, 0, 5, 4, 3, 6], [1] * 7))
    c = [1] * 7
    c[0], c[4], c[5], c[6] = 1j, 1j, -1j, -1j
    specs.append(([6, 1, 2, 3, 5, 4, 0], c))
    for q in range(6):
        c = [1] * 7
        c[q] = -1
        specs.append((list(range(7)), c))
    out = []
    for src, cf in specs:
        p = []
        for x in V:
            y = apply(x, src, cf)
            hits = [r for r, z in enumerate(V) if peq(y, z)]
            require(len(hits) == 1, "automorphism node image")
            p.append(hits[0])
        out.append(tuple(p))
    require(len(out) == 9, "nine generators")
    return out


def compose(a, b):
    return tuple(a[b[i]] for i in range(48))


def aut_group():
    ident = tuple(range(48))
    seen = {ident}
    todo = [ident]
    for x in todo:
        for g in generators():
            h = compose(g, x)
            if h not in seen:
                seen.add(h)
                todo.append(h)
    require(len(todo) == 1536, "Aut(S) node action order")
    return todo


def actset(s, p):
    return frozenset(p[i] for i in s)


def support(pred):
    return frozenset(r for r, z in enumerate(V) if pred(z))


def mask(s):
    return sum(1 << r for r in s)


def from_mask(h):
    m = int(h, 16)
    return frozenset(r for r in range(48) if (m >> r) & 1)


def q(z, k):
    a1, a2, a3, b1, b2, b3, c = z
    return (
        a1 * a1 + a2 * a2 - b3 * b3,
        a2 * a2 + a3 * a3 - b1 * b1,
        a1 * a1 + a3 * a3 - b2 * b2,
        a1 * a1 + a2 * a2 + a3 * a3 - c * c,
    )[k - 1]


def rank_mod(ids):
    M = []
    for r in ids:
        row = []
        for x in V[r]:
            a, b = int(x.real), int(x.imag)
            row.append((a + b * II) % P)
        M.append(row)
    rk = 0
    for c in range(7):
        pv = next((r for r in range(rk, len(M)) if M[r][c]), None)
        if pv is None:
            continue
        M[rk], M[pv] = M[pv], M[rk]
        inv = pow(M[rk][c], P - 2, P)
        M[rk] = [(x * inv) % P for x in M[rk]]
        for r in range(len(M)):
            if r != rk and M[r][c]:
                f = M[r][c]
                M[r] = [(M[r][j] - f * M[rk][j]) % P for j in range(7)]
        rk += 1
        if rk == len(M):
            break
    return rk


def known_conics(G):
    # Retained representative family with e1=e2=e3=+1:
    # a1=0, a2=-b3, a3=-b2, b1=-c.
    c0 = support(lambda z: z[0] == 0 and z[1] == -z[5] and z[2] == -z[4] and z[3] == -z[6])
    require(len(c0) == 6, "known-conic representative node count")
    O = {actset(c0, p) for p in G}
    require(len(O) == 32, "known-conic Aut orbit size")
    require(all(len(c) == 6 for c in O), "known-conic six-node supports")
    return O


def elliptic_quartics(G):
    # One retained incidence-16 smooth elliptic quartic; Aut orbit is the low-degree test library.
    e0 = support(lambda z: z[3] == 0 and z[1] == 1j * z[2] and z[6] == z[0] and q(z, 1) == 0 and q(z, 3) == 0)
    require(len(e0) == 8, "elliptic-quartic representative node count")
    O = {actset(e0, p) for p in G}
    require(len(O) == 12, "elliptic-quartic Aut orbit size")
    require(all(len(e) == 8 for e in O), "elliptic-quartic eight-node supports")
    return O


def low_incidence_closure(conics):
    reps14 = {
        "14_96": "0000185aa566",
        "14_192a": "00033c123303",
        "14_192b": "00033c123330",
        "14_384a": "0005185aa524",
        "14_384b": "0005185aa581",
    }
    for key, h in reps14.items():
        S = from_mask(h)
        require(len(S) == 14 and rank_mod(sorted(S)) == 6, f"{key} rank-six N14 support")
        hits = sorted((len(S & c) for c in conics), reverse=True)
        require(hits[:2] == [6, 6], f"{key} two six-node known conics")
        require(sum(n >= 4 for n in hits) == 2, f"{key} exactly two negative known conics")

    S15 = from_mask("111919162121")
    require(len(S15) == 15 and rank_mod(sorted(S15)) == 6, "inc15 representative support")
    hits15 = sorted((len(S15 & c) for c in conics), reverse=True)
    require(hits15[:3] == [6, 6, 6], "inc15 N15 three six-node known conics")
    require(sum(n >= 4 for n in hits15) == 3, "inc15 N15 exactly three negative known conics")
    for omit in S15:
        S = frozenset(set(S15) - {omit})
        require(rank_mod(sorted(S)) == 6, "inc15 N14 subset spans P5")
        hits = sorted((len(S & c) for c in conics), reverse=True)
        require(hits[:3] == [6, 6, 5], "inc15 N14 negative-conic incidence 6,6,5")
        require(sum(n >= 4 for n in hits) == 3, "inc15 N14 exactly three negative known conics")


def balanced_supports():
    S16a = support(lambda z: z[3] == 0)
    C16a = []
    for s in (1, -1):
        for t in (1, -1):
            C16a.append(set(support(lambda z, s=s, t=t: z[3] == 0 and z[1] == s * 1j * z[2] and z[6] == t * z[0] and q(z, 1) == 0 and q(z, 3) == 0)))
    require(len(S16a) == 16 and [len(c) for c in C16a] == [8, 8, 8, 8], "inc16 size3 components")
    A = set()
    for omit in combinations(S16a, 2):
        S = frozenset(set(S16a) - set(omit))
        counts = tuple(len(S & c) for c in C16a)
        if all(n <= 7 for n in counts):
            require(counts == (7, 7, 7, 7), "inc16 size3 balanced pattern")
            require(rank_mod(sorted(S)) == 6, "inc16 size3 balanced rank")
            A.add(S)
    require(len(A) == 32, "inc16 size3 balanced count")

    H16b = lambda z: z[6] == z[0] + z[1] + 1j * z[2]
    S16b = support(H16b)
    C1 = set(support(lambda z: H16b(z) and z[0] + 1j * z[2] == 0 and z[4] == 0 and q(z, 1) == 0 and q(z, 2) == 0))
    C2 = set(support(lambda z: H16b(z) and z[1] + 1j * z[2] == 0 and z[3] == 0 and q(z, 1) == 0 and q(z, 3) == 0))
    require(len(S16b) == 16 and len(C1) == len(C2) == 8 and not (C1 & C2), "inc16 size24 components")
    B = set()
    for omit in combinations(S16b, 2):
        S = frozenset(set(S16b) - set(omit))
        counts = (len(S & C1), len(S & C2))
        if all(n <= 7 for n in counts):
            require(counts == (7, 7), "inc16 size24 balanced pattern")
            require(rank_mod(sorted(S)) == 6, "inc16 size24 balanced rank")
            B.add(S)
    require(len(B) == 64, "inc16 size24 balanced count")
    return A, B


def quotient_balanced(G, A, B, conics, elliptics):
    base = A | B
    seen = set()
    rows = []
    global_union = set()
    for S in sorted(base, key=mask):
        if S in seen:
            continue
        O = {actset(S, p) for p in G}
        seen |= O
        global_union |= O
        canon = min(O, key=mask)
        rows.append((f"{mask(canon):012x}", len(O), len(O & A), len(O & B)))
    rows.sort()
    require(rows == [
        ("0000770000ff", 48, 16, 0),
        ("00007b0000ff", 48, 16, 0),
        ("000707000f0f", 768, 0, 32),
        ("00070b000f0f", 768, 0, 32),
    ], "four balanced support Aut orbits")
    require(len(global_union) == 1632, "global balanced support population")
    require(3 * len(A) + 24 * len(B) == 1632, "ambient-orbit global population accounting")

    for S in base:
        require(max(len(S & c) for c in conics) == 2, "balanced support known-conic max incidence")
        require(max(len(S & e) for e in elliptics) == 7, "balanced support elliptic-quartic max incidence")

    # Zero-pairing quartics: n=7 gives D_l.Q=l*(28-28)=0.
    orbit_zero_profiles = {}
    for h, osz, _, _ in rows:
        S = from_mask(h)
        zeros = [e for e in elliptics if len(S & e) == 7]
        landing_mult = Counter(sum(r in e for e in zeros) for r in S)
        orbit_zero_profiles[h] = (len(zeros), dict(landing_mult))
    require(orbit_zero_profiles["0000770000ff"] == (4, {2: 14}), "orbit48a zero-quartic profile")
    require(orbit_zero_profiles["00007b0000ff"] == (4, {2: 14}), "orbit48b zero-quartic profile")
    require(orbit_zero_profiles["000707000f0f"] == (2, {1: 14}), "orbit768a zero-quartic profile")
    require(orbit_zero_profiles["00070b000f0f"] == (2, {1: 14}), "orbit768b zero-quartic profile")
    return rows


def main():
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_GENUS1_SPAN5_KNOWN_CONIC_BALANCED_QUOTIENT_V1", "certificate schema")
    source_lock_preflight(cert)

    G = aut_group()
    conics = known_conics(G)
    elliptics = elliptic_quartics(G)
    low_incidence_closure(conics)
    A, B = balanced_supports()
    rows = quotient_balanced(G, A, B, conics, elliptics)

    require(cert["retained_consequence"]["incidence15_uniform_ray_closed"] is True, "certificate inc15 closure")
    require(cert["retained_consequence"]["all_five_incidence14_orbits_uniform_ray_closed"] is True, "certificate inc14 closure")
    require(cert["retained_consequence"]["balanced16_global_support_count"] == 1632, "certificate balanced global count")
    require(cert["retained_consequence"]["balanced16_aut_orbit_sizes"] == [48, 48, 768, 768], "certificate balanced quotient")
    require(cert["credit_firewall"]["whole_span5_closed"] is False, "whole-span5 firewall")
    require(cert["credit_firewall"]["MB104_complete"] is False, "MB104 firewall")

    print("PASS STAGE32_MB104_GENUS1_SPAN5_KNOWN_CONIC_BALANCED_QUOTIENT_V1")
    print("known_conics=32 nodes_each=6 elliptic_quartics=12 nodes_each=8")
    print("inc15=N15_has_6,6,6;every_N14_has_6,6,5 => fixed_known_conic")
    print("inc14=all_5_ambient_orbits_have_two_6_node_known_conics => fixed_known_conic")
    print("balanced16=1632_global_supports aut_orbits=48,48,768,768")
    print("balanced16_known_conic_max=2 elliptic_quartic_max=7 no_negative_low_degree_test_curve")
    print("balanced16_zero_quartics=orbit48:4_each_node_on2;orbit768:2_each_node_on1")
    print("scope=displayed_uniform_P5_ray_only whole_span5_open unequal_coefficients_open")


if __name__ == "__main__":
    main()
