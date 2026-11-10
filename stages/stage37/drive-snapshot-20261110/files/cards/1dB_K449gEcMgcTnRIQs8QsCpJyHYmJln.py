import json, math
from fractions import Fraction as F
from pathlib import Path

def packet(u, cap=None):
    out=set()
    for a in range(1,u+1):
        if u*u%a: continue
        z=u*u//a
        if z<=a or (z+a)%2: continue
        d,v=(z+a)//2,(z-a)//2
        if math.gcd(u,v)==1 and (cap is None or d<=cap): out.add((v,d))
    return out

n=0
for u in range(1,161):
    expected=set()
    for d in range(u+1,(u*u+1)//2+1):
        v=math.isqrt(d*d-u*u)
        if v>0 and v*v+u*u==d*d and math.gcd(u,v)==1: expected.add((v,d))
    assert packet(u)==expected
    n+=len(expected)

partial_checks=0
edges=(672,153,104); R=697
# These have only TWO integral face diagonals; no endpoint is asserted.
for i,j,k in [(0,2,1),(1,2,0)]:
    b=math.gcd(R,edges[i]); u=edges[i]//b; d=R//b
    fi=math.isqrt(edges[j]**2+edges[k]**2)
    fk=math.isqrt(edges[i]**2+edges[j]**2)
    assert fi*fi==edges[j]**2+edges[k]**2
    assert fk*fk==edges[i]**2+edges[j]**2
    assert fi%b==0
    v=fi//b
    assert (v,d) in packet(u)
    t,a,c=F(edges[j],b),F(edges[k],b),F(fk,b)
    X=-t*t; Y=t*a*c
    assert Y*Y==X*(X+v*v)*(X-u*u)
    ratios=[F(e,R) for e in edges]
    assert math.lcm(*(x.denominator for x in ratios))==R
    assert F(u,d)==ratios[i] and F(t,d)==ratios[j] and F(a,d)==ratios[k]
    partial_checks+=1

ff=0
for p in (17,41,73):
    roots={}
    for x in range(p): roots.setdefault(x*x%p,x)
    for u in range(1,p):
        for v in range(1,p):
            if (u*u+v*v)%p==0: continue
            for t in range(1,p):
                aa=(v*v-t*t)%p; cc=(u*u+t*t)%p
                if aa==0 or cc==0 or aa not in roots or cc not in roots: continue
                X=-t*t%p; Y=t*roots[aa]*roots[cc]%p
                assert (Y*Y-X*(X+v*v)*(X-u*u))%p==0
                ff+=1

result={'card':'M3-T11-205','status':'PASS','primitive_leg_labels_exhaustively_checked':160,
        'primitive_space_packets':n,'two_face_partial_examples':partial_checks,
        'finite_field_elliptic_maps':ff,'physical_endpoints_checked':0,
        'scope':'algebra and reconstruction only; uniform counting is deductive using retained174 and Dujella Theorem1.1; no independent audit'}
Path('M3-T11-205-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
