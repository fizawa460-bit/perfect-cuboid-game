#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-30.

The proof is in result.md.  This audit verifies on finite physical packets:
- the two exact reciprocal equations and both common-core plus divisibilities;
- elimination to the reciprocal coefficient discriminant;
- the B^o-type bad-core mechanism through gcd(a,b);
- a valid two-way allocation of C_Delta into the two discriminant factors;
- exact reconstruction of X*Y from the dominant allocated factor/cofactor.
It also locks the exact quarter-phi exponent threshold for the next fiber.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
SCRIPTS = HERE.parents[1]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


s29 = load_module(
    "stage14_s729_s730",
    SCRIPTS / "14-s7-29" / "common_core_primitive_root_line_audit.py",
)
s28 = s29.s28
ch = s28.ch


def v2(n: int) -> int:
    assert n > 0
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def oddpart(n: int) -> int:
    return n >> v2(n)


def factor_integer(n: int):
    assert n >= 1
    out = []
    x = n
    p = 2
    while p * p <= x:
        if x % p:
            p = 3 if p == 2 else p + 2
            continue
        e = 0
        pe = 1
        while x % p == 0:
            x //= p
            e += 1
            pe *= p
        out.append((p, e, pe))
        p = 3 if p == 2 else p + 2
    if x > 1:
        out.append((x, 1, x))
    return out


def vp(n: int, p: int) -> int:
    assert n != 0
    x = abs(n)
    e = 0
    while x % p == 0:
        x //= p
        e += 1
    return e


def allocate_two_way(Cdelta: int, Eminus: int, Eplus: int):
    assert Cdelta >= 1
    assert Eminus != 0
    assert Eplus > 0
    assert (Eminus * Eplus) % Cdelta == 0

    Cminus = 1
    Cplus = 1
    for p, e, _ in factor_integer(Cdelta):
        em = vp(Eminus, p)
        ep = vp(Eplus, p)
        assert em + ep >= e
        fm = min(e, em)
        fp = e - fm
        assert fp <= ep
        Cminus *= p ** fm
        Cplus *= p ** fp

    assert Cminus * Cplus == Cdelta
    assert abs(Eminus) % Cminus == 0
    assert Eplus % Cplus == 0
    return Cminus, Cplus


def audit_packet(a_state: dict[str, int], b_state: dict[str, int]):
    data = s28.packet_data(a_state, b_state)
    s28.audit_reconstruction(data)

    C, u_res, v_res = data["triple"]
    r = int(data["r"])
    s = int(data["s"])
    X = int(data["X"])
    Y = int(data["Y"])

    U = int(data["lx_plus"])
    V = int(data["lx_minus"])
    M = int(data["lk_plus"])
    N = int(data["lk_minus"])

    a = int(data["cx_plus"])
    b = int(data["cx_minus"])
    c = int(data["ck_plus"])
    d = int(data["ck_minus"])
    epsx = int(data["epsilon_x"])
    epsk = int(data["epsilon_k"])

    kappa = 4 * r * s * epsk
    lam = 4 * X * Y * epsx

    # Exact reciprocal system.
    assert (a * U) ** 2 - (b * V) ** 2 == kappa * M * N
    assert (c * M) ** 2 - (d * N) ** 2 == lam * U * V

    # The same odd common core divides both plus hosts.
    assert ((a * U) ** 2 + (b * V) ** 2) % C == 0
    assert ((c * M) ** 2 + (d * N) ** 2) % C == 0
    assert gcd(C, U * V) == 1
    assert gcd(C, M * N) == 1

    A0 = 4 * a * b * c * d
    L0 = kappa * lam
    Delta = A0 * A0 - L0 * L0

    # Direct integral form of the elimination congruence.
    y = b * V
    assert (Delta * (y ** 4)) % C == 0

    Cbad = gcd(C, b ** 4)
    Cdelta = C // Cbad
    assert Delta % Cdelta == 0

    # The bad factor is supported on the small first quotient gcd.
    g = gcd(a, b)
    assert Cbad <= g ** 4

    singular = L0 == A0
    if singular:
        # X6 proves this is asymptotically absent; finite audit records hits only.
        return {
            "singular": True,
            "C": C,
            "Cdelta": Cdelta,
            "Cbad": Cbad,
            "h": None,
        }

    Eminus = A0 - L0
    Eplus = A0 + L0
    assert Eminus != 0 and Eplus > 0
    Cminus, Cplus = allocate_two_way(Cdelta, Eminus, Eplus)

    if Cplus >= Cminus:
        L = Cplus
        h = Eplus // L
        L0_rec = L * h - A0
        branch = "plus"
    else:
        L = Cminus
        h = abs(Eminus) // L
        eta = 1 if Eminus > 0 else -1
        L0_rec = A0 - eta * L * h
        branch = "minus"

    assert L * L >= Cdelta
    assert h > 0
    assert L0_rec == L0

    xy_denom = 16 * r * s * epsx * epsk
    assert L0_rec % xy_denom == 0
    assert L0_rec // xy_denom == X * Y

    return {
        "singular": False,
        "C": C,
        "Cdelta": Cdelta,
        "Cbad": Cbad,
        "h": h,
        "branch": branch,
        "L": L,
        "u_res": u_res,
        "v_res": v_res,
    }


def finite_physical_audit(limit: int = 600):
    groups = ch.make_groups(limit)
    checked = 0
    singular_hits = 0
    max_bad = 1
    max_h = 1
    branch_hist = {"plus": 0, "minus": 0}

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a_state, b_state = states[i], states[j]
                if (a_state["a"], a_state["b"]) == (b_state["a"], b_state["b"]):
                    continue
                if (a_state["km"], a_state["kp"]) == (b_state["km"], b_state["kp"]):
                    continue
                out = audit_packet(a_state, b_state)
                checked += 1
                singular_hits += int(out["singular"])
                max_bad = max(max_bad, int(out["Cbad"]))
                if not out["singular"]:
                    max_h = max(max_h, int(out["h"]))
                    branch_hist[str(out["branch"])] += 1

    assert checked > 0
    return checked, singular_hits, max_bad, max_h, branch_hist


def exponent_ledger_audit() -> None:
    # Quarter-phi only.  c ranges over the legal common-core dyadic exponent.
    for j in range(0, 25):
        c = Fraction(j, 64)
        if c > Fraction(3, 8):
            continue
        outer = c + Fraction(1, 4)
        old_root_line_fiber = Fraction(1, 2) - c
        short_h = Fraction(1, 4) - c / 2

        assert outer + old_root_line_fiber == Fraction(3, 4)
        # A fixed-XY fiber strictly smaller than short_h gives a whole-family saving.
        assert outer + short_h + short_h == Fraction(3, 4)
        assert short_h >= Fraction(1, 16)

    assert Fraction(1, 4) - Fraction(3, 8) / 2 == Fraction(1, 16)


def boundary_audit() -> None:
    root = HERE.parents[4]
    s29_text = (root / "stages/stage14/14-s7-29/result.md").read_text()
    cp = (root / "stages/stage14/14-4cp/result.md").read_text()
    s28_text = (root / "stages/stage14/14-s7-28/result.md").read_text()
    aw = (root / "stages/stage14/14-toolbox-aw/result.md").read_text()

    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=3/4" in s29_text
    assert "THREE_QUARTER_SATURATION_REQUIRES_THETA=5/16" in cp
    assert "THREE_QUARTER_SATURATION_REQUIRES_PHI=1/4" in cp
    assert "TOP_THETA_LAMBDA4_SINGULAR_BRANCH_EMPTY=true" in cp
    assert "SELF_GENERATED_FOUR_ROOT_MODULI_CHARGED_AS_INDEPENDENT_SPACING=false" in cp
    assert "ABSOLUTE_MODULUS_SCALE_DEFECT=1" in s28_text
    assert "CURRENT_MAIN_S_RECEIVER=QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy" in aw
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=3/4" in aw


def main() -> None:
    boundary_audit()
    exponent_ledger_audit()
    checked, singular_hits, max_bad, max_h, hist = finite_physical_audit()

    print("Stage14-s7-30 reciprocal discriminant short-cofactor audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"finite singular hits: {singular_hits}")
    print(f"max finite discriminant bad-core factor: {max_bad}")
    print(f"max finite dominant discriminant cofactor h: {max_h}")
    print(f"dominant discriminant branch histogram: {hist}")
    print("common core divides reciprocal coefficient discriminant after B^o bad peel: exact")
    print("two-way common-core discriminant allocation: exact")
    print("dominant allocated core >= sqrt(C_Delta): exact")
    print("short cofactor reconstructs moving X*Y: exact")
    print("quarter-phi fixed-XY fiber threshold exponent: 1/4-c/2")
    print("whole-family exponent remains 3/4")
    print("s7-30 auxiliary H needed: false")


if __name__ == "__main__":
    main()
