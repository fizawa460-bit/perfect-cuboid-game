"""Independent full primitive-pair enumeration of the TWO closed certificates."""
import json
from math import gcd

rows=json.load(open('ti003_certificates.json'))
closed=[r for r in rows if r['rank_zero_certified']]
assert [(r['m'],r['n']) for r in closed]==[(4,1),(9,4)]
count=0
for r in closed:
    u,v,w=r['U'],r['V'],r['W']
    m,n=r['m'],r['n']
    assert (u,v,w)==(m*m-n*n,2*m*n,m*m+n*n)
    expected_E = {1,3,5,15} if (m,n)==(4,1) else {1,5,13,65}
    expected_Ep_positive = {1,2,17,34} if (m,n)==(4,1) else {1,2,3,6,97,194,291,582}
    assert set(r['E_survivors']) | {int(d) for d in r['E_obstructions']} == expected_E
    assert set(r['E_survivors']) == {1}
    expected_Tp = {1,-1,34,-34} if (m,n)==(4,1) else {1,-1,194,-194}
    assert set(r['Eprime_survivors']) == expected_Tp
    assert (set(r['Eprime_survivors']) | {int(d) for d in r['Eprime_obstructions']}) == (expected_Ep_positive | {-d for d in expected_Ep_positive})
    for name,a,b in [('E',-2*(v*v+w*w),u**4),
                     ('Eprime',4*(v*v+w*w),16*v*v*w*w)]:
        for ds,(q,k) in r[name+'_obstructions'].items():
            d=int(ds); M=q**k
            sq={j*j%M for j in range(M)}
            for z in range(M):
                for t in range(M):
                    if z%q==0 and t%q==0:continue
                    rhs=(d*z**4+a*z*z*t*t+(b//d)*t**4)%M
                    assert rhs not in sq,(r['m'],r['n'],name,d,q,k,z,t)
            count+=1
    # Verify the explicit rational points producing all four dual classes.
    for X,Y in [(-4*v*v,0),(4*v*w,8*v*w*(v+w)),
                (-4*v*w,8*v*w*(w-v))]:
        assert Y*Y==X*(X+4*v*v)*(X+4*w*w)
    assert any(u*v*w%q for q in (7,11,13,17))
print('Independent full-pair modular obstruction proofs:',count)
print('Dual class point identities and TI-002 torsion screen: PASS')
print('Closed sources:',[(r['m'],r['n']) for r in closed])
