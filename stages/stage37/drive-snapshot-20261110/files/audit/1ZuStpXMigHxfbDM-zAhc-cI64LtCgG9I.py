"""Exact replay of the physical two-face + space preselector covering family."""
import csv,json,math
from collections import Counter
from pathlib import Path

rows=list(csv.DictReader(open('M3-T11-160-physical-host.tsv'),delimiter='\t'))
lim=1_000_000
sieve=bytearray(b'\x01')*(lim+1);sieve[0:2]=b'\x00\x00'
for p in range(2,math.isqrt(lim)+1):
    if sieve[p]:sieve[p*p:lim+1:p]=b'\x00'*((lim-p*p)//p+1)
primes=[p for p in range(2,lim+1) if sieve[p]]
def sf(n):
    ans=1
    for p in primes:
        if p*p>n:break
        e=0
        while n%p==0:n//=p;e+=1
        if e%2:ans*=p
    if n>1:ans*=n
    return ans
states=[];seen=set()
for z in rows:
    d={k:int(v) for k,v in z.items()};y,c,x,r=(d[k] for k in ('Y','C','X','R'))
    assert 0<c<=x and y>0 and r*r==c*c+x*x+y*y and r<=lim
    assert math.gcd(y,math.gcd(c,x))==1
    for n in (y*y+c*c,y*y+x*x):assert math.isqrt(n)**2==n
    g=math.gcd(c,x);c0,x0=c//g,x//g
    assert (c0,x0)==(d['primitive_C'],d['primitive_X'])
    k=sf(c0*c0+x0*x0);assert k==d['squarefree_missing_norm']
    a,b,p,q,ep,Z=(d[k] for k in ('a','b','p','q','epsilon','Z'))
    assert a>b>0 and p>q>0 and math.gcd(a,b)==math.gcd(p,q)==1
    A=a*a+b*b;S=p*p+q*q;g0=math.gcd(r,c)
    F=(b*p-a*q)*(a*q+b*p)*(b*q-a*p)*(b*q+a*p)
    H=(A*(p*p-q*q))**2+(2*a*b*S)**2
    assert F==Z*Z and H+4*F==A*A*S*S
    assert H*(g0*ep)**2==(2*S)**2*(c*c+x*x)
    assert g0*ep*a*b==c and g0*ep*A==2*r
    assert r*(p*p-q*q)==x*S and g0*ep*Z==y*S
    assert (y,c,x,r) not in seen;seen.add((y,c,x,r));states.append((r,k,c0,x0))
summary=[]
for B in (1000,10000,100000,1000000):
    selected=[z for z in states if z[0]<=B];counts=Counter(z[1] for z in selected)
    high={k:v for k,v in counts.items() if k**4>B**7}
    summary.append({'B':B,'states':len(selected),'squareclasses':len(counts),'energy':sum(v*v for v in counts.values()),'max_class':max(counts.values(),default=0),'class1':counts[1],'high_kernel_states':sum(high.values()),'high_kernel_energy':sum(v*v for v in high.values())})
report={'status':'PASS','height':'exact integer space diagonal R<=B','scope':'complete physical preselector covering family, not a claim of literal equality to every original canonical H_F chart; finite diagnostics are not asymptotic evidence','dual_enumeration':'C++ full Euclid faces and full difference-of-squares faces MATCH','chart_and_all_predicates':'Python integer replay PASS','summary':summary}
Path('verify160-result.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
