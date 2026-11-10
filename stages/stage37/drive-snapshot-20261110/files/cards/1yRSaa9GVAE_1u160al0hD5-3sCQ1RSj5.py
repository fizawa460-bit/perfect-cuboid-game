import json
from math import gcd
from pathlib import Path

def primes(n):
    return [p for p in range(5,n+1) if all(p%d for d in range(2,int(p**.5)+1)) and p%4==1]

out={'card':'M3-T11-136','status':'PASS','global_counting_credit':0,
     'physical_endpoints_enumerated':0,'external_audit':False,'local_cover_cases':0,
     'field_counts':[], 'finite_checks_are_theorem':False}
for p in primes(113):
    squares={z*z%p for z in range(p)}
    strong=[x for x in range(2,p) if x in squares and (x-1)%p in squares]
    old=[x for x in range(2,p) if x*(1-x)%p in squares]
    assert len(strong)==(p-5)//4 and len(old)==(p-3)//2
    assert set(strong)<=set(old)
    out['field_counts'].append({'p':p,'strong':len(strong),'old':len(old)})
for p,lam in [(5,1),(13,1),(17,1),(5,2)]:
    q=p**(2*lam); squares={z*z%q for z in range(q)}
    uu=next(z for z in range(q) if (z*z+1)%q==0)
    lim=min(q,180)
    for alpha in range(1,lim):
        if alpha%p==0:continue
        for beta in range(1,lim):
            if beta%p==0:continue
            dj,dk=alpha*alpha%q,beta*beta%q
            dt=(dj+dk)%q
            if dt%p==0 or dt not in squares:continue
            s0=2*dt%q
            a0=uu*s0*pow(dj*dk,-1,q)%q
            if a0 not in squares:continue
            xx=a0*s0*pow(16*uu,-1,q)%q
            rootx=s0*pow(4*alpha*beta,-1,q)%q
            rootxm=(dj-dk)*pow(2*alpha*beta,-1,q)%q
            assert xx==rootx*rootx%q
            assert (xx-1)%q==rootxm*rootxm%q
            assert xx in squares and (xx-1)%q in squares
            # Consumed scaled pole quadratic: pole roots 2dj,2dk.
            assert (2*dj+2*dk-s0)%q==0
            assert (4*dj*dk-4*uu*s0*pow(a0,-1,q))%q==0
            out['local_cover_cases']+=1
assert (6*(1-6))%13==9 and 6 not in {z*z%13 for z in range(13)}
out['old_legendre_counterexample']={'p':13,'x':6,'old_square':9,'new_x_square':False}
Path('M3-T11-136-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
