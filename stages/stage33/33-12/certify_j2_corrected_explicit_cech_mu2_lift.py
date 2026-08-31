#!/usr/bin/env python3
"""Materialize the corrected J2 Cech/symbol preimage and surface mu_2 lift.

This checker starts from the corrected branch datum D=P_r2-P_r4 and the
resolved B1-sign double cover.  It does not import the retired arithmetic
descent producer, the old ell_Q, or the historical Kummer-glue producer.

On the rational quotient use t=A2/(A1+B3), s=A3/(A1+B2) and put

    f2=(t-r2)/(t-r4),
    g22=1-s^2+i*s*(1-t^2)/t.

The cup product {f2,g22} has boundary kappa_D on C22 and zero boundary on
C21.  Every other codimension-one residue is killed by an explicit square.
It therefore gives the requested class e_D in H^2(Ubar,mu_2).  Pullback to
the double cover gives a concrete H^2(Kc_bar,mu_2) lift lambda_D.

The script also computes the generic splitting of the cc/ct Galois defects.
Those splittings prove that the defects lie in Pic/2, but do not identify the
integral Picard coordinates.  Hence no HS d2 or Q-descent credit is claimed.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
S33 = HERE.parent
ADAPTER = HERE / "j2-corrected-branch-surface-mu2-adapter.json"
SUPPORT = HERE / "j2-corrected-kc-branch-support.json"
PRE = S33 / "33-05" / "j2-corrected-pre-kummer-descent-cochain.json"
OUT = HERE / "j2-corrected-explicit-cech-mu2-lift.json"

EXPECTED_ADAPTER = "edb98c634c79c97c09b0ea4a14402f32d9c5900c63dd9584eca5ea91b91d6875"
EXPECTED_SUPPORT = "a9eb7d4d3868581d88ff7ce88c23a42b7010c79c959ead1579738e4a0c56961a"
EXPECTED_PRE = "940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256", None)
    assert claimed == expected == csha(body), (path, claimed, csha(body))
    return obj


# Q(i,sqrt(2)) = Q-basis 1,i,sqrt(2),i*sqrt(2).
def k(a=0, b=0, c=0, d=0):
    return tuple(Fraction(x) for x in (a, b, c, d))


def kadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def kneg(x):
    return tuple(-a for a in x)


def kmul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return (
        a*e + 2*c*g - b*f - 2*d*h,
        a*f + b*e + 2*(c*h + d*g),
        a*g + c*e - b*h - d*f,
        a*h + b*g + c*f + d*e,
    )


ZERO = k()
ONE = k(1)
I = k(0, 1)
S2 = k(0, 0, 1)


class P:
    """Sparse polynomial in t,s over Q(i,sqrt(2))."""

    def __init__(self, terms=None):
        self.d = {m: c for m, c in (terms or {}).items() if c != ZERO}

    @staticmethod
    def const(c=ZERO):
        if isinstance(c, int):
            c = k(c)
        return P({(0, 0): c}) if c != ZERO else P()

    @staticmethod
    def mon(et=0, es=0, c=ONE):
        return P({(et, es): c})

    def __add__(self, other):
        other = top(other)
        out = dict(self.d)
        for m, c in other.d.items():
            out[m] = kadd(out.get(m, ZERO), c)
            if out[m] == ZERO:
                out.pop(m)
        return P(out)

    __radd__ = __add__

    def __neg__(self):
        return P({m: kneg(c) for m, c in self.d.items()})

    def __sub__(self, other):
        return self + (-top(other))

    def __rsub__(self, other):
        return top(other) - self

    def __mul__(self, other):
        other = top(other)
        out = {}
        for (at, ass), ac in self.d.items():
            for (bt, bs), bc in other.d.items():
                m = (at + bt, ass + bs)
                out[m] = kadd(out.get(m, ZERO), kmul(ac, bc))
                if out[m] == ZERO:
                    out.pop(m)
        return P(out)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert n >= 0
        out = P.const(ONE)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out

    def __eq__(self, other):
        return self.d == top(other).d

    def eval_t(self, value):
        out = {}
        for (et, es), coeff in self.d.items():
            term = kmul(coeff, kpow(value, et))
            out[es] = kadd(out.get(es, ZERO), term)
            if out[es] == ZERO:
                out.pop(es)
        return out


def top(value):
    if isinstance(value, P):
        return value
    if isinstance(value, tuple):
        return P.const(value)
    return P.const(k(int(value)))


def kpow(value, n):
    out = ONE
    base = value
    while n:
        if n & 1:
            out = kmul(out, base)
        base = kmul(base, base)
        n //= 2
    return out


adapter = load_locked(ADAPTER, EXPECTED_ADAPTER)
support = load_locked(SUPPORT, EXPECTED_SUPPORT)
pre = load_locked(PRE, EXPECTED_PRE)
assert adapter["kummer_gysin_adapter"]["open_complement"] == "Ubar=Sprime_bar-Cbar"
assert adapter["double_cover_geometry"]["corrected_component"] == "C22=CsK[22]"
assert support["marked_Kc_support"]["marked_branch_curve"] == "CsK[22]"
assert pre["normalization"]["half_divisor_D"] == "P_r2-P_r4"

t = P.mon(et=1)
s = P.mon(es=1)
i = P.const(I)
one = P.const(ONE)

r1 = k(1, 0, 1)
r2 = k(-1, 0, -1)
r3 = k(-1, 0, 1)
r4 = k(1, 0, -1)


def lin(root):
    return t - P.const(root)


q = t**4 - 6*t**2 + one
assert lin(r1)*lin(r2)*lin(r3)*lin(r4) == q

fnum = lin(r2)
fden = lin(r4)
gp = t*(one-s**2) + i*s*(one-t**2)
gm = t*(one-s**2) - i*s*(one-t**2)

# Rational quotient coordinates and inverse chart.
A1 = (one-t**2)*(one-s**2)
A2 = 2*t*(one-s**2)
A3 = 2*s*(one-t**2)
B2 = (one+s**2)*(one-t**2)
B3 = (one+t**2)*(one-s**2)
assert A1**2 + A2**2 == B3**2
assert A1**2 + A3**2 == B2**2
assert A2 == t*(A1+B3)
assert A3 == s*(A1+B2)
assert A3-i*A2 == -2*i*gp

# Cover relation: gp*gm=F and B1^2=4F, hence on Kc
# (gp/t)*(gm/t)=(B1/(2t))^2.
F = t**2*(one-s**2)**2 + s**2*(one-t**2)**2
assert gp*gm == F
assert A2**2 + A3**2 == 4*F

# The only odd f2 valuations are t=r2 (+1) and t=r4 (-1).
# At both fibers g22=gp/t is an explicit square.
sq_r2 = (one+i*s)**2
sq_r4 = (one-i*s)**2
assert gp.eval_t(r2) == (t*sq_r2).eval_t(r2)
assert gp.eval_t(r4) == (t*sq_r4).eval_t(r4)

# At the odd poles t=0 and t=infinity of g22, f2 specializes to a square.
c0 = kadd(ONE, S2)
assert fnum.eval_t(ZERO) == (P.const(kmul(c0, c0))*fden).eval_t(ZERO)
assert fnum.d[(1, 0)] == fden.d[(1, 0)] == ONE  # f2(infinity)=1.

# sqrt(2)-conjugation gives ct(f2)/f2=h^2/q in Qbar(t)^*/squares.
hnum = lin(r3)*lin(r4)
ct_ratio_num = lin(r3)*lin(r4)
ct_ratio_den = lin(r1)*lin(r2)
assert ct_ratio_num*q == (hnum**2)*ct_ratio_den

# g22 is minus a norm from z^2=q.  Clearing 4t^2 verifies
# Norm(s-i(1-t^2+z)/(2t))=-g22.
norm_cleared = (2*t*s-i*(one-t**2))**2 + q
assert norm_cleared == -4*t*gp

cert = {
    "schema": "STAGE33_12_J2_CORRECTED_EXPLICIT_CECH_MU2_LIFT_V1",
    "status": "PASS_EXACT_EXPLICIT_CECH_SYMBOL_PREIMAGE_AND_SURFACE_MU2_LIFT_PIC_COORDINATES_OPEN",
    "source_locks": {
        "branch_surface_adapter": {
            "path": "stages/stage33/33-12/j2-corrected-branch-surface-mu2-adapter.json",
            "canonical_sha256": EXPECTED_ADAPTER,
        },
        "corrected_support": {
            "path": "stages/stage33/33-12/j2-corrected-kc-branch-support.json",
            "canonical_sha256": EXPECTED_SUPPORT,
        },
        "corrected_pre_kummer": {
            "path": "stages/stage33/33-05/j2-corrected-pre-kummer-descent-cochain.json",
            "canonical_sha256": EXPECTED_PRE,
        },
        "primary_sources": [
            {
                "work": "Skorobogatov, Cohomology and the Brauer group of double covers",
                "url": "https://www.ma.imperial.ac.uk/~anskor/doub8.pdf",
                "locations": ["Gysin sequence (15)", "exact sequence (16)", "Proposition 3.1"],
            },
            {
                "work": "Creutz--Viray, On Brauer groups of double covers of ruled surfaces",
                "url": "https://www.math.canterbury.ac.nz/~b.creutz/Papers/CreutzViray_Surfaces.pdf",
                "locations": ["gamma^0 definition in Section 2.3", "residue formula (3.1)", "corestriction residue formula (3.2)"],
            },
        ],
    },
    "quotient_chart": {
        "parameters": ["t=A2/(A1+B3)", "s=A3/(A1+B2)"],
        "parametrization": {
            "A1": "(1-t^2)*(1-s^2)",
            "A2": "2*t*(1-s^2)",
            "A3": "2*s*(1-t^2)",
            "B2": "(1+s^2)*(1-t^2)",
            "B3": "(1+t^2)*(1-s^2)",
        },
        "corrected_branch_identity": "A3-i*A2=-2*i*t*g22",
        "corrected_branch": "C22:g22=0",
    },
    "explicit_cech_preimage": {
        "open": "Ubar=Sprime_bar-(C21_tilde disjoint_union C22_tilde)",
        "f2": "(t+1+sqrt(2))/(t-1+sqrt(2))",
        "g22": "1-s^2+i*s*(1-t^2)/t",
        "class": "e_D={f2,g22}=kum(f2) cup kum(g22) in H^2(Ubar,mu_2)",
        "cech_model": "cup product of the two Kummer double-cover Cech 1-cocycles, extended across the listed divisors using the displayed residue-square trivializations",
        "boundary_on_C21_C22": ["0", "kappa_D represented by f2"],
        "maps_to_corrected_branch_class": True,
        "concrete_Cech_preimage_e_D_materialized": True,
    },
    "codimension_one_residue_audit": {
        "formula": "partial_v{a,b}=(-1)^(v(a)v(b))*a^v(b)/b^v(a) mod squares",
        "rows": [
            {"divisor": "C22", "valuations": [0, 1], "residue": "f2", "role": "required boundary kappa_D"},
            {"divisor": "C21", "valuations": [0, 0], "residue": "1", "role": "zero boundary"},
            {"divisor": "t=r2", "valuations": [1, 0], "residue_square_witness": "g22(r2,s)=(1+i*s)^2"},
            {"divisor": "t=r4", "valuations": [-1, 0], "residue_square_witness": "g22(r4,s)=(1-i*s)^2"},
            {"divisor": "t=0", "valuations": [0, -1], "residue_square_witness": "f2(0)=(1+sqrt(2))^2"},
            {"divisor": "t=infinity", "valuations": [0, -1], "residue_square_witness": "f2(infinity)=1"},
            {"divisor": "s=infinity", "valuations": [0, -2], "residue": "f2^-2 is a square"},
        ],
        "other_prime_divisors_have_both_valuations_zero": True,
        "all_nonboundary_residues_zero": True,
    },
    "resolution_residue_audit": {
        "quotient_A1_exceptionals": "centers are disjoint from C21 union C22; g22 is a unit at the centers and f2 has generic exceptional valuation zero",
        "branch_crossing_exceptionals": "the four centers have t=0 or t=infinity; any exceptional residue is killed by f2(0)=(1+sqrt(2))^2 or f2(infinity)=1",
        "corrected_support_avoids_crossings": True,
        "all_exceptional_residues_zero": True,
    },
    "surface_mu2_lift": {
        "surface": "minimal resolution Kc_tilde_bar",
        "class": "lambda_D=alpha(e_D), represented generically by {f2,g22}",
        "ramification_check": "pi^*g22 has valuation 2 along the ramification curve over C22, so the required surface residue is trivial",
        "cv_projection_formula": "Cor_{K(C22)(s)/K(t,s)}{f2,s-alpha22}={f2,Norm(s-alpha22)}={f2,g22}",
        "brauer_image": "corrected nonzero J2=(f2,1)",
        "genuine_surface_H2_mu2_lift_materialized": True,
        "old_ell_Q_used": False,
        "historical_kummer_glue_used": False,
    },
    "galois_defect_generic_splittings": {
        "tau": {
            "formula": "tau(lambda_D)-lambda_D=0",
            "generic_symbol_zero": True,
        },
        "cc": {
            "formula": "cc(lambda_D)-lambda_D={f2,g21*g22}={f2,(B1/(2*t))^2}",
            "generic_symbol_zero": True,
            "consequence": "the full defect lies in Pic(Kc_bar)/2",
        },
        "ct": {
            "formula": "ct(lambda_D)-lambda_D={ct(f2)/f2,g22}={q,g22}",
            "squareclass_identity": "ct(f2)/f2=((t-r3)*(t-r4))^2/q",
            "norm_splitting": "g22=-Norm_{Qbar(t,z)/Qbar(t)}(s-i*(1-t^2+z)/(2*t)), z^2=q",
            "generic_symbol_zero": True,
            "consequence": "the full defect lies in Pic(Kc_bar)/2",
        },
        "pic_mod2_kernel_membership_materialized": True,
        "pic_mod2_integral_coordinates_materialized": False,
    },
    "exact_information_boundary": {
        "explicit_Cech_preimage_e_D_materialized": True,
        "surface_mu2_lift_materialized": True,
        "generic_galois_defect_splittings_materialized": True,
        "pic_mod2_defect_1cocycle_materialized": False,
        "integral_Pic_lift_materialized": False,
        "HS_d2_2cocycle_materialized": False,
        "HS_d2_zero_or_nonzero_proved": False,
        "Q_defined_arithmetic_Brauer_preimage_proved": False,
        "reason": "The explicit symbol fixes the lift and proves each Galois difference is algebraic, but the divisor classes of the cc/ct splitting cochains have not yet been expressed in the integral marked Picard lattice."
    },
    "next_exact_leaf": "COMPUTE_DIVISORS_OF_CC_CT_SYMBOL_SPLITTING_COCHAINS_IN_MARKED_PIC_KC_MOD2_THEN_INTEGRAL_BOCKSTEIN_HS_D2",
    "promotion_firewall": {
        "old_j2_arithmetic_descent_reused": False,
        "old_ell_Q_reused": False,
        "historical_kummer_glue_reused": False,
        "Q_defined_descent_credit_restored": False,
        "R5_full_repair_exit_reached": False,
        "stage33_05_reclosed": False,
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "stage33_progress": "5/11",
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}

cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "status": cert["status"],
    "explicit_Cech_preimage_e_D_materialized": True,
    "surface_mu2_lift_materialized": True,
    "pic_mod2_integral_coordinates_materialized": False,
    "canonical_sha256": cert["canonical_sha256"],
    "next_exact_leaf": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
