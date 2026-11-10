import json
from pathlib import Path

def primes(n):
    return [p for p in range(5,n+1) if p%4==1 and all(p%d for d in range(2,int(p**.5)+1))]

out={'card':'M3-T11-137','status':'PASS','global_counting_credit':0,
     'physical_endpoints_enumerated':0,'external_audit':False,'field_counts':[],
     'truncated_cover_x_checks':0,'parameter_witnesses':0,'finite_checks_are_proof':False}
for p in primes(113):
    sq={z*z%p for z in range(p)}
    image=set()
    for t in range(1,p):
        n=(t*t+1)%p
        if n and n in sq:image.add(n*n*pow(4*t*t,-1,p)%p)
    non=image-{1}
    expect=(p-9)//8 if p%8==1 else (p-5)//8
    assert len(non)==expect
    assert (1 in image)==(p%8==1)
    assert all(x in sq and (x-1)%p in sq for x in image)
    if p==5:assert not image
    out['field_counts'].append({'p':p,'noncollision':len(non),'collision_allowed':1 in image})
    if p==13:
        strong={x for x in range(2,p) if x in sq and (x-1)%p in sq}
        out['p13_strictness']={'136_classes':sorted(strong),'137_classes':sorted(non)}

# Exhaust the existential leading-square cover over several prime-power rings.
# These are NOT actual cuboid endpoints or full higher-order cubic lifts.
for p,lam in [(5,1),(13,1),(17,1),(5,2)]:
    q=p**(2*lam); sq={z*z%q for z in range(q)}
    usq={z for z in sq if z%p}
    u=next(z for z in range(q) if (z*z+1)%q==0)
    assert (1+u)**2%q==2*u%q
    image=set()
    for t in range(1,q):
        if t%p==0:continue
        n=(t*t+1)%q
        if n in usq:
            x=n*n*pow(4*t*t,-1,q)%q
            image.add(x)
            out['parameter_witnesses']+=1
    for a0 in [1,4]:
        for x in range(1,q):
            if x%p==0:continue
            s0=16*u*x*pow(a0,-1,q)%q
            dt=s0*pow(2,-1,q)%q
            prod=u*s0*pow(a0,-1,q)%q
            exists=False
            if dt in usq:
                for dj in usq:
                    dk=(dt-dj)%q
                    if dk in usq and dj*dk%q==prod:
                        exists=True;break
            assert exists==(x in image),(p,lam,a0,x)
            if p%8==5 and exists:assert x%p!=1
            out['truncated_cover_x_checks']+=1
out['fresh_five_empty']=True
Path('M3-T11-137-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
