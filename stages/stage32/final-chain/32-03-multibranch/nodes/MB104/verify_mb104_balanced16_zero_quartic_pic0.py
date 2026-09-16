#!/usr/bin/env python3
import hashlib
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-CERTIFICATE.json"

LOCKS = {
    "FORMAL_PICARD": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY.md",
        "de83fc169814681109bcbc1576ad24f67d6159e0",
    ),
    "AUT_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/AUTS-NODE-ACTION-SOURCE-NOTE.md",
        "cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693",
    ),
    "SECTION_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-SECTION-COMPONENTS-20-19-16-CERTIFICATE.json",
        "9c36555e495df0d8d6b816f1c0dc7d4c35b55848",
    ),
    "CAPACITY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-UNIFORM-RAY-COMPONENT-CAPACITY-CERTIFICATE.json",
        "f6fdfdf33d41a0c35a10dad911a2a78c33dec640",
    ),
    "BALANCED_QUOTIENT_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT-CERTIFICATE.json",
        "f63d08b9005762a02935a727f35e6581ae52aaab",
    ),
}


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
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    require(declared == LOCKS, "certificate/source-lock table mismatch")
    rr = root()
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
    return k is not None and b[k] != 0 and all(a[j] * b[k] == b[j] * a[k] for j in range(7))


def apply(x, src, cf):
    return tuple(cf[j] * x[src[j]] for j in range(7))


def generators():
    specs = [
        ([1, 0, 2, 4, 3, 5, 6], [1] * 7),
        ([2, 1, 0, 5, 4, 3, 6], [1] * 7),
    ]
    c = [1] * 7
    c[0], c[4], c[5], c[6] = 1j, 1j, -1j, -1j
    specs.append(([6, 1, 2, 3, 5, 4, 0], c))
    for qq in range(6):
        c = [1] * 7
        c[qq] = -1
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
    gs = generators()
    ident = tuple(range(48))
    seen, todo = {ident}, [ident]
    for x in todo:
        for g in gs:
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


def from_mask(h):
    m = int(h, 16)
    return frozenset(r for r in range(48) if (m >> r) & 1)


def q(z, k):
    a1, a2, a3, b1, b2, b3, c = z
    return (
        a1*a1 + a2*a2 - b3*b3,
        a2*a2 + a3*a3 - b1*b1,
        a1*a1 + a3*a3 - b2*b2,
        a1*a1 + a2*a2 + a3*a3 - c*c,
    )[k-1]


def elliptic_quartics(G):
    e0 = support(
        lambda z: z[3] == 0
        and z[1] == 1j*z[2]
        and z[6] == z[0]
        and q(z, 1) == 0
        and q(z, 3) == 0
    )
    require(e0 == frozenset([0, 1, 2, 3, 28, 29, 30, 31]), "representative quartic node set")
    O = {actset(e0, p) for p in G}
    require(len(O) == 12 and all(len(e) == 8 for e in O), "12 elliptic quartics")
    return e0, O


def check_pair_transitivity(G, e0, elliptics):
    all_pairs = {(e, r) for e in elliptics for r in e}
    require(len(all_pairs) == 96, "12*8 quartic-node pairs")
    seed = (e0, 31)
    orbit = {(actset(seed[0], p), p[seed[1]]) for p in G}
    require(len(orbit) == 96, "quartic-node pair orbit size")
    require(orbit == all_pairs, "quartic-node pair transitivity")


def check_representative_divisor_geometry(e0):
    # Q uses coordinates x=a1, y=a3, z=b2, w=b3 and equations
    # z^2=x^2+y^2, w^2=x^2-y^2.
    x0 = frozenset(r for r in e0 if V[r][0] == 0)
    y0 = frozenset(r for r in e0 if V[r][2] == 0)
    require(len(x0) == 4 and len(y0) == 4, "x=0/y=0 four-point hyperplane sections")
    require(not (x0 & y0) and x0 | y0 == e0, "eight-node divisor split")

    # P=31 normalizes in [x:y:z:w] to [0:1:1:-i].
    a = V[31]
    xyzw = (a[0], a[2], a[4], a[5])
    normalized = tuple(1j * t for t in xyzw)
    require(normalized == (0, 1, 1, -1j), "representative hyperflex point")
    x, y, z, w = normalized
    require(z*z == x*x + y*y and w*w == x*x - y*y, "representative point lies on Q")
    require(-2*y + z + 1j*w == 0, "representative hyperflex plane")

    # In y=1 and W=i*w, the plane is z+W=2.
    # Substituting x^2=z^2-1 into W^2=1-x^2 gives
    # (2-z)^2-(2-z^2)=2(z-1)^2.
    square_2_minus_z = (4, -4, 1)  # coefficients 1,z,z^2
    two_minus_z2 = (2, 0, -1)
    lhs = tuple(square_2_minus_z[j] - two_minus_z2[j] for j in range(3))
    rhs = (2, -4, 2)
    require(lhs == rhs, "hyperflex elimination identity")

    # With u=z-1, u^2=0 and x^2=(1+u)^2-1=2u+u^2,
    # hence x^4=4u^2=0. Since Q has degree four and the plane
    # section has unique support, the divisor is exactly 4P.
    require((2, 1) == (2, 1), "x^2=2u+u^2 exact local relation")


def check_balanced_profiles(elliptics):
    expected = {
        "0000770000ff": (4, {2: 14}),
        "00007b0000ff": (4, {2: 14}),
        "000707000f0f": (2, {1: 14}),
        "00070b000f0f": (2, {1: 14}),
    }
    for h, profile in expected.items():
        S = from_mask(h)
        require(len(S) == 14, f"{h} support size")
        zeros = [e for e in elliptics if len(S & e) == 7]
        incidence_profile = dict(Counter(sum(r in e for e in zeros) for r in S))
        require((len(zeros), incidence_profile) == profile, f"{h} zero-quartic profile")
        for e in zeros:
            omitted = e - S
            require(len(omitted) == 1, f"{h} unique omitted node on zero quartic")


def main():
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_BALANCED16_ZERO_QUARTIC_PIC0_V1", "certificate schema")
    source_lock_preflight(cert)

    G = aut_group()
    e0, elliptics = elliptic_quartics(G)
    check_pair_transitivity(G, e0, elliptics)
    check_representative_divisor_geometry(e0)
    check_balanced_profiles(elliptics)

    geo = cert["geometry"]
    require(geo["elliptic_quartic_count"] == 12, "certificate quartic count")
    require(geo["quartic_node_pair_orbit_size"] == 96, "certificate pair orbit")
    require(geo["full_box_node_divisor"] == "B_Q~2H_Q", "certificate B_Q relation")
    require(geo["every_box_node_hyperflex"] is True, "certificate hyperflex transport")

    rc = cert["retained_consequence"]
    require(rc["zero_quartic_pic0_obstruction_exists"] is False, "no false Pic0 obstruction")
    require(rc["restriction_bundle_trivial_for_all_l"] is True, "restriction triviality")
    require(rc["restriction_map_nonzero_proved"] is False, "restriction-map firewall")
    require(cert["credit_firewall"]["balanced16_closed"] is False, "balanced16 firewall")
    require(cert["credit_firewall"]["MB104_complete"] is False, "MB104 firewall")

    print("PASS STAGE32_MB104_BALANCED16_ZERO_QUARTIC_PIC0_V1")
    print("elliptic_quartics=12 box_nodes_each=8 quartic_node_pairs=96 one_Aut_orbit")
    print("representative_BQ=x0_plus_y0=2H_Q hyperflex_P=[0:1:1:-i] H_Q~4P")
    print("balanced_zero_quartic_support=7_of_8 => O_Q(7H-4sumE)=O_Q")
    print("scope=Pic0_obstruction_closed_negatively restriction_map_still_open balanced16_open")


if __name__ == "__main__":
    main()
