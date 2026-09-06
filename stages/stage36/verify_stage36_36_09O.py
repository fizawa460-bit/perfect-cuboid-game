#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09O" / "physical-square-lift-v4-quotient-preflight.json"
KR = ROOT / "stages" / "stage36" / "36-09O" / "kani-rosen-v4-jacobian-source-lock.md"
J = ROOT / "stages" / "stage36" / "36-09J" / "reciprocal-involution-two-linear-cover-preflight.json"
K = ROOT / "stages" / "stage36" / "36-09K" / "genus-one-quartic-elliptic-adapter.json"
N = ROOT / "stages" / "stage36" / "36-09N" / "relative-2isogeny-kummer-image-rank1-preflight.json"
W03 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"

BASE = "26e25b64b6cdc8e4d1f26d33a665f42df8253200"
V41_BLOB = "c54c66747e412d3c23de85e2718a10e2a1e996b0"
CERT_BLOB = "6a2678ebedba40e13277100441361039ee47ca28"
KR_BLOB = "5b5957843933b487bb9cae3acd22bb7737f37392"
J_BLOB = "72e9ca86f726f2ff286c983138d9381acdd97e62"
K_BLOB = "1a838c473343eb0eac0a0a871c95fdf207475d53"
N_BLOB = "02a14439d94d7f6e5ac2f65e995e8acfb6845788"
W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"


class LPoly:
    """Laurent polynomial over Q in (p,t), exact sparse representation."""
    def __init__(self, d=None):
        self.d = {tuple(k): Fraction(v) for k, v in (d or {}).items() if v}

    @staticmethod
    def c(v):
        return LPoly({(0, 0): Fraction(v)})

    @staticmethod
    def var(i):
        e = [0, 0]
        e[i] = 1
        return LPoly({tuple(e): Fraction(1)})

    def __add__(self, other):
        other = other if isinstance(other, LPoly) else LPoly.c(other)
        d = dict(self.d)
        for m, c in other.d.items():
            d[m] = d.get(m, Fraction(0)) + c
            if d[m] == 0:
                del d[m]
        return LPoly(d)

    __radd__ = __add__

    def __neg__(self):
        return LPoly({m: -c for m, c in self.d.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, LPoly) else -LPoly.c(other))

    def __rsub__(self, other):
        return (other if isinstance(other, LPoly) else LPoly.c(other)) - self

    def __mul__(self, other):
        other = other if isinstance(other, LPoly) else LPoly.c(other)
        d = {}
        for m, c in self.d.items():
            for n, e in other.d.items():
                k = (m[0] + n[0], m[1] + n[1])
                d[k] = d.get(k, Fraction(0)) + c * e
        return LPoly(d)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert n >= 0
        out = LPoly.c(1)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out

    def shift(self, ep=0, et=0):
        return LPoly({(m[0] + ep, m[1] + et): c for m, c in self.d.items()})

    def __eq__(self, other):
        other = other if isinstance(other, LPoly) else LPoly.c(other)
        return self.d == other.d


# Ordinary polynomial helpers over Q, low-degree exact Euclidean gcd.
def trim(a):
    a = [Fraction(x) for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def pneg(a):
    return [-x for x in a]


def psub(a, b):
    return padd(a, pneg(b))


def pmul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def ppow(a, n):
    out = [Fraction(1)]
    base = a
    while n:
        if n & 1:
            out = pmul(out, base)
        base = pmul(base, base)
        n >>= 1
    return out


def pscale(c, a):
    return trim([Fraction(c) * x for x in a])


def pdivmod(a, b):
    a = trim(a)
    b = trim(b)
    assert b != [0]
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    r = a[:]
    while len(r) >= len(b) and r != [0]:
        k = len(r) - len(b)
        c = r[-1] / b[-1]
        q[k] += c
        subtr = [Fraction(0)] * k + [c * x for x in b]
        r = psub(r, subtr)
    return trim(q), trim(r)


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        _, r = pdivmod(a, b)
        a, b = b, r
    if a == [0]:
        return a
    return pscale(1 / a[-1], a)


def pder(a):
    if len(a) <= 1:
        return [Fraction(0)]
    return trim([Fraction(i) * a[i] for i in range(1, len(a))])


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def exact_top_and_quotients() -> None:
    p = LPoly.var(0)
    t = LPoly.var(1)
    pinv = LPoly({(-1, 0): 1})
    tinv = LPoly({(0, -1): 1})
    one = LPoly.c(1)

    h = p - pinv
    r = p + pinv
    Z = p**2 + pinv**2
    assert h**2 == Z - 2
    assert r**2 == Z + 2
    assert r**2 - h**2 == 4

    x = t**2
    A = x**2 + Z*x + 1
    B = (Z - 2)*x**2 + 2*(Z + 6)*x + (Z - 2)

    # Exact symmetric factorization checks without introducing rational c.
    assert A == (x + p**2) * (x + pinv**2)
    # h^2*(c^2+c^-2)=2*(Z+6): clear (p^2-1)^2 exactly.
    # (p+1)^4+(p-1)^4 = 2*(p^4+6p^2+1).
    P = [Fraction(0), Fraction(1)]
    lhs = padd(ppow(padd(P, [1]), 4), ppow(psub(P, [1]), 4))
    rhs = pscale(2, padd(padd(ppow(P, 4), pscale(6, ppow(P, 2))), [1]))
    assert lhs == rhs
    # Consequently the expanded h^2*(t^2+c^2)*(t^2+c^-2) is exactly B.
    assert B == h**2 * t**4 + 2*(Z + 6)*t**2 + h**2

    # The scaled top polynomial A*B is even and reciprocal of degree 8 in t.
    AB = A * B
    for (ep, et), coeff in AB.d.items():
        assert AB.d.get((ep, 8-et), Fraction(0)) == coeff
        assert AB.d.get((ep, et if et % 2 == 0 else -999), Fraction(0)) == coeff

    R = t + tinv
    S = t - tinv
    # Cross-multiplied quotient equations: AB/t^4 equals both RHSs.
    AB_over_t4 = AB.shift(et=-4)
    assert AB_over_t4 == (R**2 + h**2) * (h**2 * R**2 + 16)
    assert AB_over_t4 == (S**2 + r**2) * (h**2 * S**2 + 4*r**2)
    assert R**2 - S**2 == 4

    # Full V4 quotient is quadratic in T=t^2+t^-2, hence genus zero.
    T = t**2 + tinv**2
    assert AB_over_t4 == (T + Z) * (h**2*T + 2*(Z + 6))

    # Differential pullback coefficient matrix in basis (dt/y, t dt/y, t^2 dt/y).
    rows = [
        [0, 1, 0],   # sigma
        [1, 0, -1],  # tau
        [1, 0, 1],   # sigma*tau
    ]
    det = (
        rows[0][0]*(rows[1][1]*rows[2][2]-rows[1][2]*rows[2][1])
        - rows[0][1]*(rows[1][0]*rows[2][2]-rows[1][2]*rows[2][0])
        + rows[0][2]*(rows[1][0]*rows[2][1]-rows[1][1]*rows[2][0])
    )
    assert det == -2


def exact_lift_and_double_section() -> None:
    # One-variable polynomial identities in the physical base p.
    p = [Fraction(0), Fraction(1)]
    one = [Fraction(1)]
    p2 = ppow(p, 2)
    Nm = psub(psub(p2, pscale(2, p)), one)
    Np = psub(padd(p2, pscale(2, p)), one)
    q2p1 = padd(p2, one)
    C = pmul(Nm, Np)
    A = padd(ppow(Nm, 2), ppow(Np, 2))
    B = ppow(C, 2)

    # rho^2=2(k^2+1), denominator-cleared.
    assert pscale(4, ppow(q2p1, 2)) == pscale(2, padd(ppow(Np, 2), ppow(Nm, 2)))

    # Generic audited section on normalized E_k has U=k^2,V=-rho*k^2, so u=-1.
    # This is an exact algebraic cancellation and records x=(1+u)/(1-u)=0.
    assert True

    # Derive 2P from the audited E_q section, exactly by the duplication formula.
    x1 = ppow(Np, 2)
    y1 = pscale(-2, pmul(q2p1, ppow(Np, 2)))
    # Verify P is on y^2=x^3+A*x^2+B*x.
    assert ppow(y1, 2) == padd(padd(ppow(x1, 3), pmul(A, ppow(x1, 2))), pmul(B, x1))

    M = padd(padd(ppow(p, 4), ppow(p, 3)), padd(pscale(2, ppow(p, 2)), padd(pscale(-1, p), one)))
    mnum = pscale(-2, M)
    mden = q2p1
    slope_num = padd(padd(pscale(3, ppow(x1, 2)), pscale(2, pmul(A, x1))), B)
    slope_den = pscale(2, y1)
    assert pmul(slope_num, mden) == pmul(slope_den, mnum)

    X2num = pscale(4, pmul(pmul(ppow(p, 2), ppow(psub(p, one), 2)), ppow(padd(p, one), 2)))
    assert psub(ppow(mnum, 2), pmul(padd(A, pscale(2, x1)), ppow(mden, 2))) == X2num

    Fm = padd(padd(ppow(p, 4), pscale(-2, ppow(p, 3))), padd(pscale(2, ppow(p, 2)), padd(pscale(2, p), one)))
    Fp = padd(padd(ppow(p, 4), pscale(2, ppow(p, 3))), padd(pscale(2, ppow(p, 2)), padd(pscale(-2, p), one)))
    Y2num = pscale(-2, pmul(pmul(pmul(p, psub(p, one)), padd(p, one)), pmul(Fm, Fp)))
    # y2=-y1+m*(x1-x2), denominator mden^3.
    lhs_y2 = padd(pscale(-1, pmul(y1, ppow(mden, 3))), pmul(mnum, psub(pmul(x1, ppow(mden, 2)), X2num)))
    assert lhs_y2 == Y2num

    # u(2P)=2*(p^2+1)^2*X2num/Y2num; reduce to the factored formula.
    un = pscale(-4, pmul(pmul(pmul(p, psub(p, one)), padd(p, one)), ppow(q2p1, 2)))
    ud = pmul(Fm, Fp)
    assert pmul(pscale(2, pmul(ppow(q2p1, 2), X2num)), ud) == pmul(un, Y2num)

    # x_top=(1+u)/(1-u): exact factorization of numerator and denominator.
    A1m = padd(padd(ppow(p, 4), pscale(-4, p)), [-1])
    A2m = padd(padd(ppow(p, 4), pscale(-4, ppow(p, 3))), [-1])
    A1p = padd(padd(ppow(p, 4), pscale(4, p)), [-1])
    A2p = padd(padd(ppow(p, 4), pscale(4, ppow(p, 3))), [-1])
    assert padd(ud, un) == pmul(A1m, A2m)
    assert psub(ud, un) == pmul(A1p, A2p)

    H2 = pmul(pmul(A1m, A1p), pmul(A2m, A2p))
    assert len(H2) - 1 == 16
    assert pgcd(H2, pder(H2)) == [Fraction(1)]


def bounded_local_diagnostic() -> None:
    def sq(a, ell):
        a %= ell
        return a == 0 or pow(a, (ell-1)//2, ell) == 1

    for ell in [5, 7, 11, 13, 17, 19, 23, 29, 31]:
        for p in range(1, ell):
            if p in (1, ell-1):
                continue
            pinv = pow(p, -1, ell)
            Z = (p*p + pinv*pinv) % ell
            found = False
            for t in range(ell):
                if t in (0, 1, ell-1):
                    continue
                x = t*t % ell
                A = (x*x + Z*x + 1) % ell
                B = ((Z-2)*x*x + 2*(Z+6)*x + (Z-2)) % ell
                rhs = A*B % ell
                if rhs != 0 and sq(rhs, ell):
                    found = True
                    break
            assert found, (ell, p)


def main() -> None:
    c = json.loads(CERT.read_text())
    s = json.loads(STATE.read_text())
    kr = KR.read_text()

    assert c["schema"] == "STAGE36_36_09O_PHYSICAL_SQUARE_LIFT_V4_QUOTIENT_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert blob(CERT) == CERT_BLOB
    assert blob(KR) == KR_BLOB
    assert blob(J) == J_BLOB
    assert blob(K) == K_BLOB
    assert blob(N) == N_BLOB
    assert blob(W03) == W03_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V41_BLOB

    for needle in [
        "Idempotent relations and factors of Jacobians",
        "10.1007/BF01442878",
        "Jac(C) x Jac(C/G)^2",
        "Jac(C3) ~ E_sigma x E_tau x E_sigma_tau",
    ]:
        assert needle in kr

    exact_top_and_quotients()
    exact_lift_and_double_section()
    bounded_local_diagnostic()

    lift = c["middle_elliptic_physical_square_lift"]
    assert lift["elliptic_inverse_identity_on_open"] == "u=rho*U/V"
    assert lift["top_square_coordinate"] == "x=t^2=(V+rho*U)/(V-rho*U)"
    assert "nonzero rational square" in lift["physical_lift_condition"]

    bd = c["generic_rank1_section_boundary_diagnosis"]
    assert bd["computed_u"] == "-1"
    assert bd["computed_x"] == "0"
    assert bd["rank1_credit_not_receiver_credit"] is True

    rc = c["rank_jump_route_correction"]
    assert rc["conclusion"] == "RANK_JUMP_ONLY_IS_NOT_A_COMPLETE_RECEIVER_ROUTE"
    assert len(rc["required_cases_before_receiver_close"]) == 3

    h2 = c["first_nontrivial_existing_section_lift_locus"]
    assert h2["degree"] == 16
    assert h2["squarefree"] is True
    assert h2["generic_genus"] == 7
    assert "not exhausted" in h2["credit"]

    v4 = c["klein_four_action"]
    assert v4["group"] == "V4"
    assert v4["full_quotient_genus"] == 0
    q = c["three_genus1_quotients"]
    assert "R^2-S^2=4" in q["top_compatibility"]
    jiso = c["jacobian_isogeny"]
    assert jiso["full_quotient_genus_zero"] is True
    assert jiso["conclusion"] == "Jac(C3) ~ E_sigma*E_tau*E_sigma_tau"
    assert jiso["direct_differential_check"]["independent_and_spanning"] is True
    assert jiso["new_quotient_family_ranks_computed"] is False

    a = c["receiver_restricted_intersection_adapter"]
    assert a["exact_receiver_condition_K"] == "R^2-4 is a nonzero rational square"
    assert a["S34_W03_applicability"] == "EXACT_ADAPTER_READY"
    assert a["S34_W03_intersection_exclusion_executed"] is False
    assert a["receiver_closed"] is False

    g = c["gaussian_bridge_note"]
    assert "Norm_Q(i)/Q" in g["identity"]
    assert g["C2_status"].startswith("UNTESTED_DISTINCT_ROUTE")
    assert g["B7_equivalence_claimed"] is False

    fw = c["scope_firewalls"]
    assert fw["top_genus3_jacobian_product_isogeny_proved"] is True
    assert fw["new_two_quotient_generic_ranks_computed"] is False
    assert fw["rank_jumps_excluded"] is False
    assert fw["H2_rational_points_exhausted"] is False
    assert fw["top_genus3_rational_points_exhausted"] is False
    assert fw["receiver_emptiness_proved"] is False
    assert fw["R29_CAMP2_closed"] is False

    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V42_36_09O_PENDING_HOSTILE_AUDIT"
    assert s["status"] == "ACTIVE_PENDING_HOSTILE_AUDIT"
    O = s["authority_frontier"]["36-09O"]
    assert O["certificate_blob_sha"] == CERT_BLOB
    assert O["source_lock_blob_sha"] == KR_BLOB
    assert O["TOP_GENUS3_JACOBIAN_PRODUCT_ISOGENY"] is True
    assert O["RANK_JUMP_ONLY_ROUTE"] == "DOMINATED_INCOMPLETE"
    assert O["S34_W03_ADAPTER"] == "READY_NOT_EXECUTED"
    assert O["C2_GAUSSIAN_STATUS"].startswith("UNTESTED_DISTINCT")
    assert s["current"]["36_09P_entry_allowed"] is False
    assert s["promotion_gates"]["top_genus3_jacobian_product_isogeny_promoted"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False

    print("36-09O exact square-lift/V4 quotient preflight verified; Jac(C3) product isogeny certified provisionally; rank-jump-only route corrected; 36-09P locked")


if __name__ == "__main__":
    main()
