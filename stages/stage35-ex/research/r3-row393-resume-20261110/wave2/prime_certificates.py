"""Elementary recursive Lucas primality certificates; exact modular arithmetic."""
import math
from flint import fmpz
certificates={2: {'factors':[], 'witness':None}}
def certify(n):
    n=int(n)
    if n in certificates:return True
    if n<2 or n%2==0:return False
    factors=[(int(p),int(e)) for p,e in fmpz(n-1).factor()]
    if math.prod(p**e for p,e in factors)!=n-1:return False
    if not all(certify(p) for p,e in factors):return False
    for a in range(2,min(n,10000)):
        if pow(a,n-1,n)==1 and all(math.gcd(pow(a,(n-1)//p,n)-1,n)==1 for p,e in factors):
            certificates[n]={'factors':factors,'witness':a};return True
    raise RuntimeError('No certificate found for '+str(n))

def verify(data):
    data={int(k):v for k,v in data.items()};done={2}
    assert data[2]=={'factors':[], 'witness':None}
    for n in sorted(data):
        if n==2:continue
        r=data[n]; fs=r['factors'];a=r['witness']
        assert fs and all(p in done and e>=1 for p,e in fs)
        assert math.prod(p**e for p,e in fs)==n-1
        assert pow(a,n-1,n)==1
        assert all(math.gcd(pow(a,(n-1)//p,n)-1,n)==1 for p,e in fs)
        done.add(n)
    return done
