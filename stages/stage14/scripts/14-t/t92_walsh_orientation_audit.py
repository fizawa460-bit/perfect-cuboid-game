#!/usr/bin/env python3
import json
from itertools import product, combinations


def walsh_coeff(values, subset, r):
    total = 0.0
    for eps, val in values.items():
        chi = 1
        for j in subset:
            chi *= eps[j]
        total += val * chi
    return total / (2 ** r)


def audit_function(r, fn):
    vals = {eps: float(fn(eps)) for eps in product((-1, 1), repeat=r)}
    coeffs = {}
    for k in range(r + 1):
        for S in combinations(range(r), k):
            coeffs[S] = walsh_coeff(vals, S, r)
    # inversion
    for eps, val in vals.items():
        rec = sum(c * __import__('math').prod(eps[j] for j in S) for S, c in coeffs.items())
        assert abs(rec - val) < 1e-9
    mean = coeffs[()]
    centered_mean = sum(v - mean for v in vals.values()) / (2 ** r)
    assert abs(centered_mean) < 1e-9
    lhs = sum(c*c for c in coeffs.values())
    rhs = sum(v*v for v in vals.values()) / (2 ** r)
    assert abs(lhs-rhs) < 1e-9
    nonconst = sum(c*c for S,c in coeffs.items() if S)
    centered_rhs = sum((v-mean)**2 for v in vals.values())/(2**r)
    assert abs(nonconst-centered_rhs) < 1e-9
    max_degree = max((len(S) for S,c in coeffs.items() if abs(c)>1e-12), default=0)
    return max_degree, len(coeffs)

checks=0
full_degree_examples=0
max_degree=0
for r in range(1,9):
    funcs = [
        lambda e: 1,
        lambda e: 1 if sum(e) >= 0 else 0,
        lambda e: __import__('math').prod(e),
        lambda e: 1 if __import__('math').prod(e) == 1 else 0,
    ]
    for fn in funcs:
        deg,nc = audit_function(r,fn)
        checks += nc
        max_degree=max(max_degree,deg)
        if deg==r:
            full_degree_examples += 1

out={
    "stage":"14-t92",
    "walsh_coefficient_checks":checks,
    "full_degree_stress_examples":full_degree_examples,
    "max_verified_degree":max_degree,
    "boundary":{
        "GENERIC_ORIENTATION_WALSH_EXPANSION_EXACT":True,
        "PRINCIPAL_CUBE_MEAN_ISOLATED":True,
        "CENTERED_ORIENTATION_COEFFICIENT_MEAN_ZERO":True,
        "WALSH_PARSEVAL_IDENTITY_RETAINED":True,
        "BOUNDED_WALSH_DEGREE_PROVED":False,
        "FIXED_DEGREE_TAIL_POWER_SAVING_PROVED":False,
        "WALSH_MONOMIALS_IDENTIFIED_WITH_ORIENTATION_CHARACTERS":True,
        "FINITE_CHARACTER_DECOMPOSITION_READY":False,
        "PRINCIPAL_REPRESENTATION_DENSITY_OBSTRUCTION_RETAINED":True,
        "TH26_COMPLETE_CONSUMED":True,
        "TH26_TARGET_REOPENED":False,
        "TH27_NEEDED":False,
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT":"1/2",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED":False,
        "NEXT":"Stage14-t93"
    }
}
print(json.dumps(out,sort_keys=True))
