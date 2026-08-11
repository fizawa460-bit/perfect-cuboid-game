#!/usr/bin/env python3
from pathlib import Path
from math import isqrt

ROOT = Path(__file__).resolve().parents[4]
locks = {
    'stages/stage14/14-4ds/result.md': 'SQRT_ZERO_MODE_REQUIRES_EXPONENT_ZERO_GAUSSIAN_MOVER_DENSITY=true',
    'stages/stage14/14-s7-61/result.md': 'FRESH_THIN_RESIDUE_SUPPORT_PROVED=false',
    'stages/stage14/14-Work-bhX20/result.md': 'NEXT_INTERNAL_TARGET=PrimeMoverDensityOrEnergyLemma',
}
for rel, needle in locks.items():
    assert needle in (ROOT / rel).read_text(), (rel, needle)

# Verify plus-state factorization reconstruction on examples.
for D, A in ((5, 2), (7, 4), (11, 6), (13, 8)):
    y = D*D - A*A
    r, s = D-A, D+A
    assert r*s == y
    assert (r+s)//2 == D
    assert (s-r)//2 == A

# Count candidate D,A pairs from factorizations of y: divisor-many.
def factor_pairs(n):
    out=[]
    for r in range(1, isqrt(n)+1):
        if n % r == 0:
            s=n//r
            if (r+s)%2==0:
                out.append((r,s))
    return out
for y in (21,33,45,65,105,165):
    assert len(factor_pairs(y)) <= sum(1 for d in range(1,y+1) if y%d==0)

res=(ROOT/'stages/stage14/14-4dt/result.md').read_text()
for needle in [
    'STAGE14_4DT=COMPLETE_FINITE_DIVISOR_CANDIDATE_SUPPORT_NO_WHOLE_FAMILY_SAVING',
    'FIXED_FROZEN_STATE_MOVER_PRIME_CANDIDATE_COUNT=Bo1',
    'FINITE_CANDIDATE_SUPPORT_GIVES_FIXED_POWER_SAVING=false',
    'SQRT_OBSTRUCTION_REDUCED_TO_WEIGHTED_MOVER_CANDIDATE_CONCENTRATION=true',
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2',
    'NEXT_H_NEEDED=false',
]:
    assert needle in res, needle
print({'stage':'14-4dt','current_exponent':'1/2','next':'Stage14-4du'})
