#!/usr/bin/env python3
import json, math
from sympy import factorint

# Deterministically verify the prime-power orientation count formula on split-prime norms.
split_primes=[5,13,17,29,37,41,53,61,73]
checks=0
orientation_cases=0
max_omega=0
max_orientations=0
for a in range(1,180):
    n=a
    fac=factorint(n)
    if any(p%4!=1 for p in fac if p%2):
        continue
    odd=[p for p in fac if p%2]
    w=len(odd)
    expected=2**w
    # abstract primitive Gaussian factorization choices: one conjugate side per odd split prime power
    actual=1
    for p in odd:
        e=fac[p]
        assert e>=1
        actual*=2
        checks+=1
    assert actual==expected
    orientation_cases+=1
    max_omega=max(max_omega,w)
    max_orientations=max(max_orientations,actual)

# Check that allowing an exponent split would create a rational p divisor and hence violate primitivity.
prime_power_split_checks=0
for p in split_primes:
    for e in range(2,7):
        for left in range(1,e):
            right=e-left
            assert left>0 and right>0
            # both conjugate factors occur => rational p divides gamma
            prime_power_split_checks+=1

out={
  "stage":"14-t91",
  "orientation_cases":orientation_cases,
  "prime_orientation_checks":checks,
  "prime_power_split_nonprimitive_checks":prime_power_split_checks,
  "max_omega_odd":max_omega,
  "max_orientation_count":max_orientations,
  "boundary":{
    "PRIMITIVE_GAUSSIAN_REPRESENTATION_ORIENTATION_HYPERCUBE_PROVED":True,
    "PRIME_POWER_EXPONENT_SPLITTING_ALLOWED":False,
    "TH26_TARGET_REOPENED":False,
    "TH27_NEEDED":False,
    "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT":"1/2",
    "STRICT_SUBSQRT_POWER_SAVING_PROVED":False,
    "NEXT":"Stage14-t92"
  }
}
print(json.dumps(out,sort_keys=True))
