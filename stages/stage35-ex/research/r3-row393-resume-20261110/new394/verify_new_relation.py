"""Independent acceptance check without full_profile or its dyadic routines.
Inherits the row393 maximal integral basis and degree-105 polynomial.
"""
import json, sys, math
from pathlib import Path
from flint import fmpz_poly, nmod_poly
if not __debug__: raise RuntimeError('Python -O is unsupported')
O=Path(__file__).resolve().parent; B=O.parent/'row393'
sys.path.insert(0,str(B/'parent392/parent391/parent390/parent389/parent388/parent381'))
from verify_row380 import G,F
r=json.loads((O/'new_relations394.json').read_text()); assert len(r)==1
r=r[0]; bs=json.loads((B/'discovery/scan_basis.json').read_text())
den=2**r['denominator_exponent']
assert den==2**34
# Explicit Z-linear combination of the inherited maximal-order basis.
H=fmpz_poly()
for j,c in r['search_terms']:
    d=bs['basis_denominators'][j]; assert den%d==0
    H+=c*(den//d)*fmpz_poly(bs['basis_numerators'][j])
h=fmpz_poly(r['coefficients'])
assert H==h or H==-h
N=int(G.resultant(h)); assert N>0
assert N==den**105*r['absolute_norm']
assert r['absolute_norm']==3931*667801*3727463395037
primes=[]
for p,j,e in r['valuations']:
    assert e==1 and p>2
    assert all(p%d for d in range(2,math.isqrt(p)+1))
    gp=nmod_poly(list(map(int,G)),p); hp=nmod_poly(list(map(int,h)),p)
    common=gp.gcd(hp); assert common.degree()==1
    root=-int(common[0])*pow(int(common[1]),-1,p)%p
    assert int(gp.derivative()(root))!=0
    fp=nmod_poly(list(map(int,F)),p)
    factors=sorted((list(map(int,f)) for f,_ in fp.factor()[1]),key=lambda f:(len(f),f))
    theta=-root*root%p
    hits=[k for k,f in enumerate(factors) if nmod_poly(f,p)(theta)==0]
    assert hits==[j] and len(factors[j])==2
    primes.append(dict(p=p,label=j,rho_root=root,valuation=1))
assert len(primes)==3
result=dict(integral_basis_identity=True,exact_resultant=True,
    norm=r['absolute_norm'],denominator=den,prime_checks='trial division through isqrt',
    primes=primes,ideal_factorization='exhaustive: these three degree-one factors account for the entire norm',
    scope='author-side second implementation; not external independent audit')
(O/'new_relation_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
