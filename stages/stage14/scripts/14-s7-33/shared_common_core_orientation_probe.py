#!/usr/bin/env python3
"""Exploratory/diagnostic audit for Stage14-s7-33.

Classify how odd common-core primes occur in the k-plus Gaussian host,
xi-plus Gaussian host, and the residual xi switched Gaussian quotient W_S.
This is finite diagnostic evidence; asymptotic claims belong in result.md.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
SCRIPTS = HERE.parents[1]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


s28 = load_module("s28_s733", SCRIPTS / "14-s7-28" / "primitive_ratio_reconstruction_audit.py")
s31 = load_module("s31_s733", SCRIPTS / "14-s7-31" / "fixed_outer_common_gcd_audit.py")
s32 = load_module("s32_s733", SCRIPTS / "14-s7-32" / "one_host_gaussian_boundary_audit.py")
ch = s28.ch


def prime_factors(n: int):
    out = []
    p = 2
    x = n
    while p * p <= x:
        if x % p:
            p = 3 if p == 2 else p + 2
            continue
        out.append(p)
        while x % p == 0:
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        out.append(x)
    return out


def relation(z, w, p):
    """same/opposite Gaussian slope mod p, or degenerate."""
    a, b = z
    c, d = w
    if (a * b * c * d) % p == 0:
        return "degenerate"
    same = (a * d - b * c) % p == 0
    opp = (a * d + b * c) % p == 0
    if same and not opp:
        return "same"
    if opp and not same:
        return "opposite"
    if same and opp:
        return "both"
    return "neither"


def packet_probe(a_state, b_state):
    s32.audit_packet(a_state, b_state)
    d = s28.packet_data(a_state, b_state)
    R, S, T, J, alpha, beta, gamma, delta = d["cells"]
    C, u_res, v_res = d["triple"]
    A = int(d["A"])
    D = int(d["D"])
    P = int(d["P"])
    Q = int(d["Q"])
    c = int(d["ck_plus"])
    dd = int(d["ck_minus"])
    h = gcd(c, dd)

    P1, Q1, g1 = s32.state_pq(a_state)
    P2, Q2, g2 = s32.state_pq(b_state)
    omega1 = g1 * a_state["r"] * a_state["s"]
    omega2 = g2 * b_state["r"] * b_state["s"]
    ZS = (R * b_state["x"] ** 2 * omega1, J * a_state["y"] ** 2 * omega2)
    lamS, WS = s32.gaussian_descent_allow_one(ZS[0], ZS[1], S)
    assert s32.gnorm(WS) == C * v_res * (S // s32.oddpart(S)) ** 2

    hk = (D, A)
    hx = (Q, P)
    ctr = Counter()
    for ell in prime_factors(C):
        if ell == 2:
            continue
        ctr[("Cprime",)] += 1
        if WS[0] % ell == 0 and WS[1] % ell == 0:
            ctr[("WS_common",)] += 1
            if h % ell == 0:
                ctr[("WS_common_h",)] += 1
            if (d["r"] * d["s"]) % ell == 0:
                ctr[("WS_common_rs",)] += 1
            continue
        ctr[("hk_hx", relation(hk, hx, ell))] += 1
        ctr[("hk_ws", relation(hk, WS, ell))] += 1
        ctr[("hx_ws", relation(hx, WS, ell))] += 1
    return ctr, C, v_res, h, WS


def main():
    groups = ch.make_groups(600)
    total = Counter()
    checked = 0
    max_C = max_v = max_h = max_wgcd = 1
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                ctr, C, v, h, WS = packet_probe(a, b)
                total.update(ctr)
                checked += 1
                max_C = max(max_C, C)
                max_v = max(max_v, v)
                max_h = max(max_h, h)
                max_wgcd = max(max_wgcd, gcd(abs(WS[0]), abs(WS[1])))
    assert checked > 0
    print("Stage14-s7-33 shared common-core orientation probe: PASS")
    print(f"finite physical pairs checked: {checked}")
    print(f"max C: {max_C}")
    print(f"max v_res: {max_v}")
    print(f"max quotient gcd h: {max_h}")
    print(f"max gcd(Re W_S, Im W_S): {max_wgcd}")
    for key in sorted(total, key=str):
        print(f"{key}: {total[key]}")


if __name__ == "__main__":
    main()
