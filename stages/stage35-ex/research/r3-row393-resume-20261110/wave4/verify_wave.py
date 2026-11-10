"""Exact acceptance replay of every retained new generator, no floating tests."""
import json,sys,math
from pathlib import Path
from flint import fmpz_poly
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'wave2'))
from prime_certificates import verify
if not __debug__:raise RuntimeError('Python -O is unsupported')
O=Path(__file__).resolve().parent;B=O.parent/'row393'
sys.path.insert(0,str(B/'parent392/parent391/parent390/parent389/parent388/parent381'))
import verify_units381 as v
import verify_row380 as v380
proved=verify(json.loads((O/'prime_certificates.json').read_text()))
sys.path.insert(0,str(O.parent/'wave3'))
from arbitrary_precision import activate
activate(v,v380,lambda p:p in proved)
rows=json.loads((O/'new_relations_wave4.json').read_text())
for r in rows:
    h=fmpz_poly(r['coefficients']);N=int(v.G.resultant(h));k=r['denominator_exponent']
    assert abs(N)==r['absolute_norm']*2**(105*k)
    assert math.prod(p**e for p,e in r['odd_factorization'])==abs(N)//(abs(N)&-abs(N))
    assert all(p in proved for p,e in r['odd_factorization'])
    for i,a in enumerate(h(v.X+1)):assert int(a)%2**max(0,k-i//3)==0
    vs,code,positive_h=v.full_profile(r)
    for j in [0,1]:
        value=vs.get((2,j),0)-3*k
        if value:vs[2,j]=value
        else:vs.pop((2,j),None)
    assert [[p,j,e] for (p,j),e in sorted(vs.items()) if e]==r['valuations']
    assert hex(code)==r['local_unit_code']
    assert (1 if N>0 else -1)==r['norm_sign']
result=dict(exact_generators_verified=len(rows),prime_certificates_verified=len(proved),
    floating_point_used=False,scope='author exact replay, inheriting parent maximal order and local routines; not external independent audit')
(O/'verification_wave4.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
