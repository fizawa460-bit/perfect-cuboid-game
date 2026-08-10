#!/usr/bin/env python3
"""Diagnostic audit for Stage14-s7-33.

Tests the exact Gaussian product identity

    2*T*Z_S = g1*g2*(D+iA)*(beta*r1*s2+i*gamma*s1*r2)

and checks whether the full odd common core C can be realized as a common
same-orientation Gaussian divisor of D+iA and the residual quotient W_S.
Finite enumeration is diagnostic; the proof is recorded separately.
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


def factor(n: int):
    out = []
    p = 2
    x = n
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


def relation(z, w, p):
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


def gaussian_v(z, pi):
    e = 0
    cur = z
    while True:
        q = s32.g4cf.gdiv_exact(cur, pi)
        if q is None:
            return e
        e += 1
        cur = q


def common_C_gaussian_valuation_ok(hk, WS, C):
    """For each odd p^e||C, find one orientation with >=e in both hosts."""
    profile = []
    for p, e in factor(C):
        if p == 2:
            continue
        assert p % 4 == 1, (C, p)
        a, b = s32.g4cf.prime_sum_two_squares(p)
        pi = (a, b)
        pib = (a, -b)
        vals = (
            gaussian_v(hk, pi), gaussian_v(hk, pib),
            gaussian_v(WS, pi), gaussian_v(WS, pib),
        )
        same_pi = vals[0] >= e and vals[2] >= e
        same_pib = vals[1] >= e and vals[3] >= e
        if not (same_pi or same_pib):
            return False, profile + [(p, e, vals)]
        profile.append((p, e, vals))
    return True, profile


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

    _, _, g1 = s32.state_pq(a_state)
    _, _, g2 = s32.state_pq(b_state)
    omega1 = g1 * a_state["r"] * a_state["s"]
    omega2 = g2 * b_state["r"] * b_state["s"]
    ZS = (R * b_state["x"] ** 2 * omega1, J * a_state["y"] ** 2 * omega2)
    _, WS = s32.gaussian_descent_allow_one(ZS[0], ZS[1], S)
    assert s32.gnorm(WS) == C * v_res * (S // s32.oddpart(S)) ** 2

    ES = (
        beta * a_state["r"] * b_state["s"],
        gamma * a_state["s"] * b_state["r"],
    )
    hk = (D, A)
    lhs = (2 * T * ZS[0], 2 * T * ZS[1])
    rhs = (
        g1 * g2 * (hk[0] * ES[0] - hk[1] * ES[1]),
        g1 * g2 * (hk[0] * ES[1] + hk[1] * ES[0]),
    )
    assert lhs == rhs
    assert s32.oddpart(s32.gnorm(ES)) == s32.oddpart(S * T * v_res)

    full_ok, profile = common_C_gaussian_valuation_ok(hk, WS, C)

    hx = (Q, P)
    ctr = Counter()
    for ell, _ in factor(C):
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
    return ctr, C, v_res, h, WS, S, T, s32.gnorm(ES), full_ok, profile


def main():
    groups = ch.make_groups(600)
    total = Counter()
    checked = 0
    max_C = max_v = max_h = max_wgcd = 1
    max_C_ST = max_C_v = max_C_STv = max_C_ES = 1
    nontrivial_C_ST = nontrivial_C_v = nontrivial_C_STv = 0
    full_common_ok = 0
    failed_profiles = []
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                ctr, C, v, h, WS, S, T, NES, full_ok, profile = packet_probe(a, b)
                total.update(ctr)
                checked += 1
                full_common_ok += int(full_ok)
                if not full_ok:
                    failed_profiles.append((C, v, S, T, profile))
                max_C = max(max_C, C)
                max_v = max(max_v, v)
                max_h = max(max_h, h)
                max_wgcd = max(max_wgcd, gcd(abs(WS[0]), abs(WS[1])))
                gST = gcd(C, S * T)
                gv = gcd(C, v)
                gSTv = gcd(C, S * T * v)
                gES = gcd(C, NES)
                max_C_ST = max(max_C_ST, gST)
                max_C_v = max(max_C_v, gv)
                max_C_STv = max(max_C_STv, gSTv)
                max_C_ES = max(max_C_ES, gES)
                nontrivial_C_ST += int(gST > 1)
                nontrivial_C_v += int(gv > 1)
                nontrivial_C_STv += int(gSTv > 1)
    assert checked > 0
    print("Stage14-s7-33 shared common-core orientation probe: PASS")
    print(f"finite physical pairs checked: {checked}")
    print(f"full C same-orientation Gaussian divisor packets: {full_common_ok}/{checked}")
    print(f"failed full-C profiles: {failed_profiles[:5]}")
    print(f"max C: {max_C}")
    print(f"max v_res: {max_v}")
    print(f"max quotient gcd h: {max_h}")
    print(f"max gcd(Re W_S, Im W_S): {max_wgcd}")
    print(f"max gcd(C,S*T): {max_C_ST}; nontrivial packets: {nontrivial_C_ST}")
    print(f"max gcd(C,v_res): {max_C_v}; nontrivial packets: {nontrivial_C_v}")
    print(f"max gcd(C,S*T*v_res): {max_C_STv}; nontrivial packets: {nontrivial_C_STv}")
    print(f"max gcd(C,N(E_S)): {max_C_ES}")
    for key in sorted(total, key=str):
        print(f"{key}: {total[key]}")


if __name__ == "__main__":
    main()
