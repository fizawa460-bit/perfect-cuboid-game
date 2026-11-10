import math,json
from pathlib import Path

B=50000; Z=200
euclid=set(); alltri=set()
for m in range(2,math.isqrt(B)+1):
    for n in range(1,m):
        d=m*m+n*n
        if d>B or math.gcd(m,n)>1 or (m-n)%2==0: continue
        u,v=sorted((m*m-n*n,2*m*n))
        alltri.add((u,v,d))
        if v-u<=Z: euclid.add((u,v,d))

pell=set(); seeds=0; orbit_envelopes=0
for delta in range(1,Z+1,2):
    roots=[]
    for d in range(1,6*delta+1):
        xx=2*d*d-delta*delta
        if xx<=0: continue
        x=math.isqrt(xx)
        if x*x!=xx or x<=delta or (x-delta)%2: continue
        u,v=(x-delta)//2,(x+delta)//2
        if math.gcd(u,v)>1: continue
        xp,dp=3*x-4*d,3*d-2*x
        if xp>delta and dp>0: continue
        roots.append((x,d))
    omega=sum(1 for p in range(2,delta+1) if delta%p==0 and all(p%q for q in range(2,math.isqrt(p)+1)))
    assert len(roots)<=2**omega
    orbit_envelopes+=1
    seeds+=len(roots)
    for x,d in roots:
        while d<=B:
            u,v=(x-delta)//2,(x+delta)//2
            assert u*u+v*v==d*d and math.gcd(u,v)==1
            pell.add((u,v,d))
            x,d=3*x+4*d,2*x+3*d
assert pell==euclid

circle_checks=0; trace_checks=0
for u,v,d in alltri:
    delta=v-u; x=u+v
    assert x*x-2*d*d==-delta*delta and x*x+delta*delta==2*d*d
    for h in (1,3,5,17):
        R=h*d;e=h*u;f=h*v
        assert math.gcd(R,e-f)==h and math.gcd(R,e+f)==h
        assert 2*e*f==R*R-(h*delta)**2
        circle_checks+=1

# Circle triples test signed trace only. They are not sphere/endpoint data.
for u,v,d in sorted(alltri)[:300]:
    for signs in ((1,1,1),(1,-1,1),(-1,-1,1),(-1,-1,-1)):
        pairs=((u,v),(v,u),(u,v))
        nt=sum(s*a*b for s,(a,b) in zip(signs,pairs))
        G=sum(s*(a-b)**2 for s,(a,b) in zip(signs,pairs))
        assert 2*nt==d*d*sum(signs)-G
        assert math.gcd(d*d,G)==math.gcd(d*d,nt)
        trace_checks+=1

out={'card':'M3-T11-206','status':'PASS','primitive_triangles':len(alltri),
 'complete_pell_euclid_match_B':B,'gap_cutoff':Z,'matched_unordered_directions':len(pell),
 'primitive_pell_seeds':seeds,'odd_gap_orbit_envelopes':orbit_envelopes,
 'scaled_circle_gap_gcd_checks':circle_checks,'signed_trace_circle_triples':trace_checks,
 'physical_endpoints_checked':0,'independent_audit':'NOT_RUN',
 'scope':'arithmetic adapters only; endpoint count uses retained174 and162'}
Path('M3-T11-206-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
