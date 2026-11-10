"""Exact finite check of card209; does not estimate Burgess constants or counts."""
import json, hashlib, math
from collections import Counter
from pathlib import Path

source=Path('M3-T11-208-verification.json')
data=json.loads(source.read_text())
def primes(n):
    s=bytearray(b'\1')*(n+1); s[:2]=b'\0\0'
    for p in range(2,math.isqrt(n)+1):
        if s[p]: s[p*p:n+1:p]=b'\0'*((n-p*p)//p+1)
    return [p for p in range(2,n+1) if s[p]]
ps=primes(10000)
def kernel(n):
    k=1
    for p in ps:
        if p*p>n: break
        v=0
        while n%p==0: n//=p; v+=1
        if v%2: k*=p
    return k*n
def local(n,p):
    v=0
    while n%p==0: n//=p; v+=1
    if v%2: return False,'odd_valuation'
    ok=n%8==1 if p==2 else pow(n%p,(p-1)//2,p)==1
    return ok, 'square' if ok else 'unit_nonresidue'
out=[]; checks=0; mask_count=0
for r in data['records']:
    am,ap=r['coprime_minus'],r['coprime_plus']
    km,kp=kernel(am),kernel(ap)
    assert (km,kp)==(r['minus_kernel'],r['plus_kernel'])
    assert math.gcd(am,ap)==1
    mask=all(local(a,p)[0] for a in (am,ap) for p in [2]+r['conductor_primes'])
    expected=r['branch_local2_square'] and not r['branch_conductor_obstructions']
    assert mask==expected
    checks+=2*(1+len(r['conductor_primes']))
    if not mask: continue
    mask_count+=1
    assert km%8==kp%8==1 and math.gcd(km*kp,2*r['R'])==1
    assert km*kp>1
    first=None; first_unit=None
    for p in ps:
        if 2*r['R']%p==0: continue
        for side,a,k in [('minus',am,km),('plus',ap,kp)]:
            ok,why=local(a,p); checks+=1
            if not ok and first is None: first={'prime':p,'branch':side,'type':why}
            # An odd-prime nonresidue of the fundamental-discriminant character.
            if k%p and pow(k%p,(p-1)//2,p)==p-1 and first_unit is None:
                assert not ok and why=='unit_nonresidue'
                first_unit={'prime':p,'branch':side,'kernel':k}
        if first and first_unit: break
    assert first and first_unit
    out.append({'edges':r['edges'],'R':r['R'],'c_chart':r['c_chart'],
                'A_minus':am,'A_plus':ap,'kappa_minus':km,'kappa_plus':kp,
                'least_transverse_obstruction':first,'least_transverse_unit_witness':first_unit})
assert mask_count==38
tails=[]
for B in [1000,10000,100000,1000000]:
    for numerator,denominator in [(3,16),(5,24),(11,48)]:
        selected=[r for r in out if r['R']<=B and r['c_chart']**denominator>B**numerator]
        tails.append({'B':B,'exponent':f'{numerator}/{denominator}',
            'mask_2R':len(selected),'survivors_by_prime_cutoff':
            {str(L):sum(r['least_transverse_obstruction']['prime']>L for r in selected)
             for L in [3,5,7,11,13,17,19,23,29,31]}})
summary={'card':'M3-T11-209','input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'raw_records':len(data['records']),'mask_2R_survivors':mask_count,
 'checks':checks,'least_obstruction_histogram':dict(sorted(Counter(r['least_transverse_obstruction']['prime'] for r in out).items())),
 'max_least_unit_witness':max(r['least_transverse_unit_witness']['prime'] for r in out),
 'max_least_local_obstruction':max(r['least_transverse_obstruction']['prime'] for r in out),
 'finite_only':True,'Burgess_constant_calibrated':False,'physical_endpoints':0,
 'threshold_spectrum':tails}
Path('M3-T11-209-verification.json').write_text(json.dumps({'summary':summary,'records':out},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
