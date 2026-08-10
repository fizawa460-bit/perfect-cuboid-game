#!/usr/bin/env python3
"""Deterministic audit/probe for Stage14-s7-33.

Checks the exact dual Gaussian product identities and the full common-core
same-orientation divisor. It also records, without assuming, whether the
stronger canonical S/T split selected by lambda_S,lambda_T happens on the
finite packet; failures are a guard against overclaiming.
"""
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
s32 = load_module("s32_s733", SCRIPTS / "14-s7-32" / "one_host_gaussian_boundary_audit.py")
ch = s28.ch
G = s32.g4cf


def factor(n: int):
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


def associates(z, w):
    a, b = w
    return z in ((a, b), (-a, -b), (-b, a), (b, -a))


def gaussian_v(z, pi):
    e = 0
    cur = z
    while True:
        q = G.gdiv_exact(cur, pi)
        if q is None:
            return e
        cur = q
        e += 1


def build_common_C_divisor(hk, WS, C):
    """Construct one Pi_C of norm C dividing both hk and WS."""
    out = (1, 0)
    for p, e in factor(C):
        assert p != 2 and p % 4 == 1
        a, b = G.prime_sum_two_squares(p)
        pi, pib = (a, b), (a, -b)
        cap1 = min(gaussian_v(hk, pi), gaussian_v(WS, pi))
        cap2 = min(gaussian_v(hk, pib), gaussian_v(WS, pib))
        assert cap1 + cap2 >= e, (p, e, cap1, cap2)
        take1 = min(cap1, e)
        take2 = e - take1
        assert take2 <= cap2
        out = G.gmul(out, gpow(pi, take1))
        out = G.gmul(out, gpow(pib, take2))
    assert G.gnorm(out) == C
    assert G.gdiv_exact(hk, out) is not None
    assert G.gdiv_exact(WS, out) is not None
    return out


def packet_probe(a_state, b_state):
    s32.audit_packet(a_state, b_state)
    d = s28.packet_data(a_state, b_state)
    R, S, T, J, alpha, beta, gamma, delta = d["cells"]
    C, u_res, v_res = d["triple"]
    A, D = int(d["A"]), int(d["D"])

    _, _, g1 = s32.state_pq(a_state)
    _, _, g2 = s32.state_pq(b_state)
    omega1 = g1 * a_state["r"] * a_state["s"]
    omega2 = g2 * b_state["r"] * b_state["s"]

    ZS = (R * b_state["x"] ** 2 * omega1, J * a_state["y"] ** 2 * omega2)
    ZT = (J * b_state["y"] ** 2 * omega1, R * a_state["x"] ** 2 * omega2)
    lamS, WS = s32.gaussian_descent_allow_one(ZS[0], ZS[1], S)
    lamT, WT = s32.gaussian_descent_allow_one(ZT[0], ZT[1], T)

    hk = (D, A)
    hkbar = G.gconj(hk)
    ES = (beta * a_state["r"] * b_state["s"], gamma * a_state["s"] * b_state["r"])

    rS = G.gmul(hk, ES)
    assert (2*T*ZS[0], 2*T*ZS[1]) == (g1*g2*rS[0], g1*g2*rS[1])
    rT = G.gmul(hkbar, ES)
    assert (2*S*ZT[0], 2*S*ZT[1]) == (g1*g2*rT[0], g1*g2*rT[1])

    assert s32.oddpart(G.gnorm(hk)) == C * s32.oddpart(S*T)
    assert s32.oddpart(G.gnorm(WS)) == C * s32.oddpart(v_res)
    assert s32.oddpart(G.gnorm(WT)) == C * s32.oddpart(v_res)
    assert s32.oddpart(G.gnorm(ES)) == s32.oddpart(S*T*v_res)

    Pi_any = build_common_C_divisor(hk, WS, C)
    assert G.gnorm(Pi_any) == C

    canonical_ok = quotient_associate = False
    if S % 2 and T % 2:
        K0 = G.gmul(lamS, G.gconj(lamT))
        assert G.gnorm(K0) == S*T
        Pi = G.gdiv_exact(hk, K0)
        canonical_ok = Pi is not None and G.gnorm(Pi) == C
        if canonical_ok:
            VS = G.gdiv_exact(WS, Pi)
            VT = G.gdiv_exact(WT, G.gconj(Pi))
            canonical_ok = VS is not None and VT is not None
            if canonical_ok:
                assert G.gnorm(VS) == v_res
                assert G.gnorm(VT) == v_res
                quotient_associate = associates(VS, VT)

    return {
        "C": C, "v": v_res, "S": S, "T": T,
        "canonical_ok": canonical_ok,
        "quotient_associate": quotient_associate,
        "odd_ST": bool(S % 2 and T % 2),
        "gcd_C_ST": gcd(C, S*T),
        "gcd_C_v": gcd(C, v_res),
    }


def main():
    groups = ch.make_groups(600)
    checked = odd_ST = canonical_ok = quotient_ok = 0
    max_C = max_v = max_C_ST = max_C_v = 1
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                z = packet_probe(a, b)
                checked += 1
                max_C = max(max_C, z["C"])
                max_v = max(max_v, z["v"])
                max_C_ST = max(max_C_ST, z["gcd_C_ST"])
                max_C_v = max(max_C_v, z["gcd_C_v"])
                if z["odd_ST"]:
                    odd_ST += 1
                    canonical_ok += int(z["canonical_ok"])
                    quotient_ok += int(z["quotient_associate"])
    assert checked > 0
    print("Stage14-s7-33 common-core-cancelled Gaussian probe: PASS")
    print(f"finite physical pairs checked: {checked}")
    print(f"full C shared Gaussian divisor: {checked}/{checked}")
    print(f"odd-S,T strong canonical Pi_C candidates: {canonical_ok}/{odd_ST}")
    print(f"odd-S,T strong V_S~V_T candidates: {quotient_ok}/{odd_ST}")
    print(f"strong canonical split universally valid: {canonical_ok == odd_ST and quotient_ok == odd_ST}")
    print(f"max C: {max_C}")
    print(f"max v_res: {max_v}")
    print(f"max gcd(C,S*T): {max_C_ST}")
    print(f"max gcd(C,v_res): {max_C_v}")


if __name__ == "__main__":
    main()
