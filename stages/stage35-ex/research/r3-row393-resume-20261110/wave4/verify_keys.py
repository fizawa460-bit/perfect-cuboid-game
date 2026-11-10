"""Check the two key generators without full_profile or dyadic routines."""
import json,sys,math
from pathlib import Path
from flint import fmpz_poly,nmod_poly
if not __debug__:raise RuntimeError('Python -O is unsupported')
O=Path(__file__).resolve().parent;B=O.parent/'row393'
sys.path.insert(0,str(B/'parent392/parent391/parent390/parent389/parent388/parent381'))
from verify_row380 import G,F
rows=json.loads((O/'new_relations_wave4.json').read_text());bs=json.loads((B/'discovery/scan_basis.json').read_text())
checks=[]
for index in [710,977]:
    r=rows[index];k=r['denominator_exponent'];h=fmpz_poly(r['coefficients'])
    den=max(bs['basis_denominators'][j] for j,c in r['search_terms']);H=fmpz_poly()
    for j,c in r['search_terms']:
        d=bs['basis_denominators'][j];assert den%d==0
        H+=c*(den//d)*fmpz_poly(bs['basis_numerators'][j])
    assert den%2**k==0
    assert H==(den//2**k)*h or H==-(den//2**k)*h
    N=abs(int(G.resultant(h)));assert N==2**(105*k)*r['absolute_norm']
    assert r['absolute_norm']==math.prod(p for p,j,e in r['valuations'])
    roots=[]
    for p,j,e in r['valuations']:
        assert e==1 and p>2 and all(p%d for d in range(2,math.isqrt(p)+1))
        gp=nmod_poly(list(map(int,G)),p);hp=nmod_poly(list(map(int,h)),p)
        common=gp.gcd(hp);assert common.degree()==1
        root=-int(common[0])*pow(int(common[1]),-1,p)%p
        assert gp.derivative()(root)!=0
        fs=sorted((list(map(int,f)) for f,_ in nmod_poly(list(map(int,F)),p).factor()[1]),key=lambda f:(len(f),f))
        assert [i for i,f in enumerate(fs) if nmod_poly(f,p)(-root*root%p)==0]==[j]
        assert len(fs[j])==2
        roots.append([p,j,root])
    checks.append(dict(index=index,integral_basis_identity=True,resultant_verified=True,absolute_norm=r['absolute_norm'],denominator_exponent=k,degree_one_prime_roots=roots))
(O/'key_verification.json').write_text(json.dumps(checks,indent=2)+'\n');print('PASS key generators 710 and 977, integral basis / resultants / prime roots')
