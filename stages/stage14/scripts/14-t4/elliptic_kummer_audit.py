#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

OUT = Path("stages/stage14/data/14-t4/elliptic_kummer_audit.json")
s = sp.symbols("s")
x = sp.symbols("x")
INF = sp.oo

branches = {
    "U0": INF,
    "U1": sp.Integer(0),
    "U2": sp.Integer(1),
    "W": -1/s,
    "R": 1/(1-s),
}


def cross_ratio(a, b, c, d):
    vals = [a, b, c, d]
    if INF in vals:
        A, B, C, D = [x if v is INF else v for v in vals]
        z = ((A-C)*(B-D))/((A-D)*(B-C))
        return sp.factor(sp.limit(z, x, sp.oo))
    return sp.factor(((a-c)*(b-d))/((a-d)*(b-c)))


def j_of(lam):
    return sp.factor(256*(1-lam+lam**2)**3/(lam**2*(1-lam)**2))

factors = {}
for omit in branches:
    pts = [v for k, v in branches.items() if k != omit]
    lam = cross_ratio(*pts)
    j = j_of(lam)
    factors[omit] = {
        "omitted_branch": str(branches[omit]),
        "lambda": str(lam),
        "j": str(j),
    }

j_plus = sp.factor(256*(s**2+s+1)**3/(s**2*(s+1)**2))
j_zero = sp.factor(256*(s**4-s**2+1)**3/(s**4*(s-1)**2*(s+1)**2))
j_minus = sp.factor(256*(s**2-s+1)**3/(s**2*(s-1)**2))

assert sp.simplify(j_of(cross_ratio(0,1,-1/s,1/(1-s))) - j_plus) == 0  # omit infinity / U0
assert sp.simplify(j_of(cross_ratio(INF,1,-1/s,1/(1-s))) - j_zero) == 0  # omit 0 / U1
assert sp.simplify(j_of(cross_ratio(INF,0,-1/s,1/(1-s))) - j_minus) == 0  # omit 1 / U2
assert sp.simplify(factors["W"]["j"] == str(j_minus))
assert sp.simplify(factors["R"]["j"] == str(j_plus))

# Original raw-pair family y^2=x(x-1)(x+s) has Legendre parameter -s.
raw_pair_j = j_of(-s)
assert sp.simplify(raw_pair_j - j_plus) == 0

branch_restriction = []
for odd_support in (8, 6, 4, 2, 0):
    genus = None if odd_support == 0 else (odd_support - 2)//2
    branch_restriction.append({"odd_support": odd_support, "normalized_genus": genus})

report = {
    "metadata": {
        "stage": "14-t4",
        "title": "Elliptic-factor compression and Kummer branch restriction audit",
    },
    "branch_assignment": {k: str(v) for k, v in branches.items()},
    "factors": factors,
    "geometric_j_types": {
        "plus": str(j_plus),
        "zero": str(j_zero),
        "minus": str(j_minus),
        "pairing": [["U0", "R"], ["U2", "W"], ["U1"]],
        "count": 3,
    },
    "raw_pair_factor": {
        "factor": "R",
        "raw_pair_j": str(raw_pair_j),
        "matches_plus_type": True,
    },
    "kummer_restriction": {
        "triple_branch_class": "2M",
        "M_degree_of_extremal_bisection": 4,
        "restricted_total_branch_degree": 8,
        "odd_support_genus_table": branch_restriction,
        "generic_transverse_odd_support": 8,
        "generic_normalized_genus": 3,
        "low_genus_requires_odd_support_at_most": 4,
    },
    "status": {
        "STAGE14_T4": "COMPLETE_ELLIPTIC_COMPRESSION_AND_KUMMER_RESTRICTION",
        "ELLIPTIC_FACTOR_COUNT": 5,
        "GEOMETRIC_ELLIPTIC_J_TYPES": 3,
        "RAW_PAIR_FACTOR": "E_R",
        "THIRD_FACE_FACTOR": "E_W",
        "GENERIC_M_DEGREE4_TRIPLE_LIFT_GENUS": 3,
        "T_O_SQRT_B_PROVED": False,
    },
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report["status"], indent=2))
