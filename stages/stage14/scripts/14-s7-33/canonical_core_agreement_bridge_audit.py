#!/usr/bin/env python3
"""Deterministic audit for the Stage14-s7-33 canonical bridge.

Imports the 4ct residual-host gcd peel, constructs its canonical good-core
Gaussian divisor Pi_C from W_S/g, and verifies on finite physical packets that
Pi_C also divides the k-plus host Z_k=D+iA.  After the endpoint-small signed-
quotient gcd peel, the induced primitive agreement root is the Cayley transform
of the same Gaussian orientation: t=(D+A)/(D-A)=-D/A mod the live core.
"""
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
SCRIPTS = HERE.parents[1]


def load_module(name, path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    m = module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


s28 = load_module("s28_s733_bridge", SCRIPTS / "14-s7-28" / "primitive_ratio_reconstruction_audit.py")
s32 = load_module("s32_s733_bridge", SCRIPTS / "14-s7-32" / "one_host_gaussian_boundary_audit.py")
G = s32.g4cf
ch = s28.ch


def factor(n):
    out = []
    x = n
    p = 2
    while p * p <= x:
        if x % p:
            p = 3 if p == 2 else p + 2
            continue
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        out.append((p, e))
        p = 3 if p == 2 else p + 2
    if x > 1:
        out.append((x, 1))
    return out


def gpow(z, e):
    out = (1, 0)
    for _ in range(e):
        out = G.gmul(out, z)
    return out


def canonical_pi(W0, C_good):
    out = (1, 0)
    for p, e in factor(C_good):
        assert p != 2 and p % 4 == 1
        a, b = G.prime_sum_two_squares(p)
        pe = gpow((a, b), e)
        pbe = gpow((a, -b), e)
        q1 = G.gdiv_exact(W0, pe)
        q2 = G.gdiv_exact(W0, pbe)
        assert (q1 is None) != (q2 is None), (W0, C_good, p, e, q1, q2)
        out = G.gmul(out, pe if q1 is not None else pbe)
    assert G.gnorm(out) == C_good
    assert G.gdiv_exact(W0, out) is not None
    return out


def audit_packet(a_state, b_state):
    s32.audit_packet(a_state, b_state)
    d = s28.packet_data(a_state, b_state)
    R, S, T, J, alpha, beta, gamma, delta = d["cells"]
    C, u_res, v_res = d["triple"]
    A, D = int(d["A"]), int(d["D"])
    hk = (D, A)

    _, _, g1 = s32.state_pq(a_state)
    _, _, g2 = s32.state_pq(b_state)
    omega1 = g1 * a_state["r"] * a_state["s"]
    omega2 = g2 * b_state["r"] * b_state["s"]
    ZS = (R * b_state["x"] ** 2 * omega1, J * a_state["y"] ** 2 * omega2)
    _, WS = s32.gaussian_descent_allow_one(ZS[0], ZS[1], S)

    # Imported 4ct gcd peel.
    gw = s32.oddpart(gcd(abs(WS[0]), abs(WS[1])))
    assert WS[0] % gw == 0 and WS[1] % gw == 0
    W0 = (WS[0] // gw, WS[1] // gw)
    C_bad = gcd(C, gw * gw)
    C_good = C // C_bad
    d_excess = gw * gw // C_bad
    v = s32.oddpart(v_res)
    assert v % d_excess == 0
    Pi = canonical_pi(W0, C_good)

    # New s7-33 bridge: the canonical residual orientation also divides Z_k.
    K = G.gdiv_exact(hk, Pi)
    assert K is not None, (hk, WS, C, gw, C_good, Pi)
    assert s32.oddpart(G.gnorm(K)) == C_bad * s32.oddpart(S * T)

    # Remove the endpoint-small common quotient coefficient gcd before using
    # projective primitive coordinates.
    aq = int(d["cx_plus"])
    bq = int(d["cx_minus"])
    U = int(d["lx_plus"])
    V = int(d["lx_minus"])
    gab = gcd(aq, bq)
    a0, b0 = aq // gab, bq // gab
    C_ab_bad = gcd(C_good, gab * gab)
    C_live = C_good // C_ab_bad

    root_checks = 0
    for p, e in factor(C_live):
        mod = p ** e
        assert gcd(A * (b0 * V), mod) == 1
        r = (D * pow(A, -1, mod)) % mod
        t = ((a0 * U) * pow((b0 * V) % mod, -1, mod)) % mod
        assert (r * r + 1) % mod == 0
        assert (t * t + 1) % mod == 0
        assert t == (-r) % mod
        root_checks += 1

    return C, C_good, C_live, gw, root_checks


def main():
    groups = ch.make_groups(600)
    checked = root_checks = 0
    max_C = max_C_good = max_gw = 1
    live_packets = 0
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                C, Cg, Cl, gw, rc = audit_packet(a, b)
                checked += 1
                root_checks += rc
                live_packets += int(Cl > 1)
                max_C = max(max_C, C)
                max_C_good = max(max_C_good, Cg)
                max_gw = max(max_gw, gw)
    assert checked > 0
    print("Stage14-s7-33 canonical core agreement bridge audit: PASS")
    print(f"finite physical pairs checked: {checked}")
    print(f"canonical 4ct Pi_C divides Z_k: {checked}/{checked}")
    print(f"packets with nontrivial live core: {live_packets}")
    print(f"prime-power primitive Cayley root checks: {root_checks}")
    print(f"max C: {max_C}")
    print(f"max C_good: {max_C_good}")
    print(f"max residual-host odd coordinate gcd: {max_gw}")
    print("primitive root orientation t=-D/A mod live common core: exact")


if __name__ == "__main__":
    main()
