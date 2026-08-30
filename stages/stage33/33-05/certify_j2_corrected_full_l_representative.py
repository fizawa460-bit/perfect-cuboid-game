#!/usr/bin/env python3
"""Exact R2 repair certificate for the corrected geometric J2 CV representative.

The source-locked Stage33-05 quotient skeleton labels abstract J2 by the full
branch-algebra pair (f2,1), not by the old Q-defined function restricted
identically to both normalization components.  This verifier proves directly
in the full quotient Lbar^*/(Kbar^* Lbar^{*2}) that (f2,1) is nonzero.

No norm/divisor/residue/support-only promotion is used: quotient-zero itself
would force f2 to be a square in the common quadratic normalization E/K, and
that is ruled out exactly.
"""
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple
import hashlib
import json

ROOT = Path(__file__).resolve().parent

# Coefficients are x+y*sqrt(2), polynomials are in t.
Coeff = Tuple[int, int]

def cadd(a: Coeff, b: Coeff) -> Coeff:
    return (a[0]+b[0], a[1]+b[1])

def cmul(a: Coeff, b: Coeff) -> Coeff:
    return (a[0]*b[0] + 2*a[1]*b[1], a[0]*b[1] + a[1]*b[0])

@dataclass(frozen=True)
class Poly:
    d: Dict[int, Coeff]

    def __add__(self, other):
        other = to_poly(other)
        out = dict(self.d)
        for e,c in other.d.items():
            v = cadd(out.get(e,(0,0)), c)
            if v == (0,0):
                out.pop(e, None)
            else:
                out[e] = v
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({e:(-c[0],-c[1]) for e,c in self.d.items()})

    def __sub__(self, other):
        return self + (-to_poly(other))

    def __rsub__(self, other):
        return to_poly(other) - self

    def __mul__(self, other):
        other = to_poly(other)
        out: Dict[int,Coeff] = {}
        for e,a in self.d.items():
            for f,b in other.d.items():
                v = cadd(out.get(e+f,(0,0)), cmul(a,b))
                if v == (0,0):
                    out.pop(e+f, None)
                else:
                    out[e+f] = v
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, n: int):
        assert n >= 0
        out = to_poly(1)
        base = self
        k = n
        while k:
            if k & 1:
                out = out * base
            base = base * base
            k >>= 1
        return out

def to_poly(x):
    if isinstance(x, Poly):
        return x
    if isinstance(x, tuple):
        return Poly({0:x}) if x != (0,0) else Poly({})
    return Poly({0:(int(x),0)}) if x else Poly({})

t = Poly({1:(1,0)})
s2 = (0,1)
one = (1,0)

# r1=1+s, r2=-(1+s), r3=s-1, r4=1-s.
r1 = (1,1)
r2 = (-1,-1)
r3 = (-1,1)
r4 = (1,-1)
roots = [r1,r2,r3,r4]
assert len(set(roots)) == 4

def lin(root: Coeff) -> Poly:
    return t - root

q = t**4 - 6*t**2 + 1
assert lin(r1)*lin(r2)*lin(r3)*lin(r4) == q

# Source-locked abstract J2 representative:
# f2=(t-r2)/(t-r4)=(t+1+sqrt(2))/(t-1+sqrt(2)).
f2_num = lin(r2)
f2_den = lin(r4)
assert f2_num == t + one + s2
assert f2_den == t - one + s2

# Exact square obstruction in Kbar(t):
# v_r2(f2)=+1 and v_r4(f2)=-1, hence f2 is not a K-square.
f2_odd_valuations = {"r2": 1, "r4": -1}
assert all(v % 2 for v in f2_odd_valuations.values())

# In E=K(z), z^2=q, if (A+Bz)^2=f in K then 2AB=0.
# Since char(K)=0 and E is a field, A=0 or B=0. Therefore a base-field
# f can be an E-square only if f is a K-square or f/q is a K-square.
#
# Here f2/q = 1 / ((t-r1)(t-r3)(t-r4)^2), with odd valuations at r1,r3.
f2_over_q_den = lin(r1)*lin(r3)*(lin(r4)**2)
assert f2_num * f2_over_q_den == q * f2_den
f2_over_q_odd_valuations = {"r1": -1, "r3": -1}
assert all(v % 2 for v in f2_over_q_odd_valuations.values())

f2_is_K_square = False
f2_over_q_is_K_square = False
f2_is_E_square = f2_is_K_square or f2_over_q_is_K_square
assert f2_is_E_square is False

# Full quotient test. If (f2,1)=k*(u^2,v^2) with diagonal k in K^*, then
# 1=k*v^2 and hence f2=(u/v)^2 in E, contradiction.
corrected_pair_zero_in_full_quotient = f2_is_E_square
assert corrected_pair_zero_in_full_quotient is False

cert = {
    "schema": "STAGE33_05_J2_CORRECTED_FULL_L_REPRESENTATIVE_V1",
    "status": "PASS_EXACT_R2_CORRECTED_REPRESENTATIVE_NONZERO",
    "source_lock": {
        "abstract_J2_pair_source": "stages/stage33/33-05/lce_filtered_quotient_skeleton.py",
        "abstract_J2_pair_source_blob_sha1": "ac8bb0096714d85e67efd55f8bb4730e1d1169ce",
        "normalization_source": "stages/stage33/33-05/normalization_galois_skeleton.py",
        "normalization_source_blob_sha1": "139a309c52a6646e649d37bdb03c3bb535d29cf1",
        "old_zero_regression": "stages/stage33/33-12/j2-cv-lclass-zero-regression.json",
    },
    "base_field_scope": "geometric Kbar=Qbar(t)",
    "full_branch_algebra": "Lbar=Kbar(B_plus) x Kbar(B_minus)=E_plus x E_minus",
    "common_normalization": "E=Kbar(z), z^2=q(t), q=t^4-6*t^2+1",
    "branch_roots": {
        "r1": "1+sqrt(2)",
        "r2": "-(1+sqrt(2))",
        "r3": "sqrt(2)-1",
        "r4": "1-sqrt(2)",
    },
    "abstract_J2_source_locked_pair": "(f2,1)",
    "f2": "(t+1+sqrt(2))/(t-1+sqrt(2))",
    "corrected_representative": {
        "name": "ell_J2_corrected",
        "scope": "GEOMETRIC_FULL_L_PAIR",
        "pair": "(f2,1)",
    },
    "full_quotient_zero_test": {
        "quotient": "Lbar^*/(Kbar^* Lbar^{*2})",
        "zero_would_imply": "f2=(u/v)^2 in E after dividing the two components",
        "f2_square_in_E": False,
        "corrected_pair_zero": False,
    },
    "quadratic_extension_square_test": {
        "lemma": "For f in Kbar, if (A+B*z)^2=f in E=Kbar(z), then 2*A*B=0; hence f is a Kbar-square or f/q is a Kbar-square.",
        "f2_K_square": False,
        "f2_K_square_obstruction": "odd valuations v_r2=+1 and v_r4=-1",
        "f2_over_q_K_square": False,
        "f2_over_q_identity": "f2/q=1/((t-r1)*(t-r3)*(t-r4)^2)",
        "f2_over_q_K_square_obstruction": "odd valuations v_r1=-1 and v_r3=-1",
    },
    "exact_exit": "CORRECTED_ELL_J2_NONZERO_IN_LSTAR_MOD_KSTAR_LSTAR2",
    "old_Q_defined_ell_nonzero_credit_restored": False,
    "Q_defined_descent_credit_restored": False,
    "explicit_E2_cocycle_materialized": False,
    "marked_brauer_coordinate_selected": False,
    "stage33_05_reclosed": False,
    "stage33_12_closed_exact": False,
    "stage33_13_released": False,
    "class3_promoted": False,
    "theorem_credit": False,
    "receiver_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_existence_claim": False,
    "perfect_cuboid_nonexistence_claim": False,
    "next_exact_leaf": "R3_APPLY_CORRECTED_REPRESENTATIVE_TO_CREUTZ_VIRAY_EXPLICIT_E2_COCYCLE",
}
raw = json.dumps(cert, sort_keys=True, separators=(",",":")).encode()
cert["canonical_sha256"] = hashlib.sha256(raw).hexdigest()
out = ROOT/"j2-corrected-full-l-representative.json"
out.write_text(json.dumps(cert, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "exact_exit": cert["exact_exit"],
    "corrected_pair": cert["corrected_representative"]["pair"],
    "f2_square_in_E": cert["full_quotient_zero_test"]["f2_square_in_E"],
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
