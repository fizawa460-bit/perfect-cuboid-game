"""Two independent finite enumerations of primitive principal directions.

These are arithmetic directions, NOT physical Stage37 endpoints.
The asymptotic proof is in the accompanying research card.
"""
import json
from math import gcd, isqrt
from pathlib import Path

T = 1000
euclid = set()
for m in range(2, isqrt(T) + 1):
    for n in range(1, m):
        p = m*m + n*n
        if p > T or gcd(m,n) != 1 or (m-n)%2 != 1:
            continue
        a,b = m*m-n*n, 2*m*n
        euclid.update(((a,b,p),(b,a,p)))
circle = set()
for p in range(1,T+1):
    for a in range(1,p):
        b = isqrt(p*p-a*a)
        if b>0 and a*a+b*b==p*p and gcd(a,b)==1:
            circle.add((a,b,p))
assert euclid == circle
assert len(circle) <= 2*T
scale_checks = 0
for a,b,p in sorted(circle):
    for d in (1,2,7,19):
        c,x,f = d*a,d*b,d*p
        assert gcd(c,x)==d and c*c+x*x==f*f
        assert f//gcd(c,x)==p
        assert (c//gcd(c,x),x//gcd(c,x))==(a,b)
        scale_checks += 1
report = {
    'status':'PASS', 'direction_cutoff':T,
    'primitive_oriented_directions':len(circle),
    'independent_Euclid_and_integer_circle_enumerations':'MATCH',
    'content_invariance_checks':scale_checks,
    'physical_endpoints_enumerated':0,
    'scope':'Arithmetic direction test only. Does not test endpoint occupancy, retained010, or prove asymptotics by census.',
    'asymptotic_dependency':'Uniform physical fixed-ratio bound retained010; no new external rational-point theorem.'
}
Path('verify161-result.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
