"""Card213: exact fixed-face curve/phase, complete local sums and L1 sparsity."""
import json, math, hashlib
from pathlib import Path
from fractions import Fraction
from collections import Counter, defaultdict
src=Path('M3-T11-208-verification.json'); records=json.loads(src.read_text())['records']
primes=[29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
def chi(a,p):
    return 0 if a%p==0 else (1 if pow(a%p,(p-1)//2,p)==1 else -1)
def face(r):
    a=r['shared_edge'];others=sorted(x for x in r['edges'] if x!=a)
    faces=[]
    for b in others:
        d=math.gcd(a,b);faces.append((a//d,b//d,math.isqrt(a*a+b*b)//d,d,b))
    S,X,H,d,b=min(faces);c=next(x for x in others if x!=b)
    return (S,X,H),d,c
curves={};local=[]
for r in records:
    (S,X,H),d,c=face(r);a=r['shared_edge'];R=r['R'];h=math.gcd(R,a);eps=2 if a%2 else 1
    t=Fraction(c,d);v=Fraction(math.isqrt(a*a+c*c),d);w=Fraction(R,d)
    assert v*v==t*t+S*S and w*w==t*t+H*H
    assert eps*h*d*(w-S)==eps*h*(R-a)
    assert eps*h*d*(w+S)==eps*h*(R+a)
    curves[(S,X,H)]=True
# Enumerate complete affine curve exactly, with four rational points at infinity.
complete={};cases=0;phase_checks=0
for S,X,H in sorted(curves):
    for p in primes:
        if (2*S*X*H*(S*S-X*X))%p==0:continue
        roots=defaultdict(list)
        for u in range(p):roots[u*u%p].append(u)
        pts=[]
        for t in range(p):
            for v in roots[(t*t+S*S)%p]:
                for w in roots[(t*t+H*H)%p]:pts.append((t,v,w))
        N=len(pts);sminus=sum(chi(w-S,p) for t,v,w in pts);splus=sum(chi(w+S,p) for t,v,w in pts)
        assert abs(N+4-p-1)<=2*math.sqrt(p)+1e-10
        assert abs(sminus)<=12*math.sqrt(p) and abs(splus)<=12*math.sqrt(p)
        assert N>=p/2
        complete[((S,X,H),p)]=(N,sminus,splus)
        cases+=1
        if cases<=12:local.append({'face':[S,X,H],'p':p,'affine_points':N,'sum_minus':sminus,'sum_plus':splus})
for r in records:
    F,d,c=face(r);S,X,H=F;a=r['shared_edge'];R=r['R'];h=math.gcd(R,a);eps=2 if a%2 else 1
    L=2*d*h*S*X*H*abs(S*S-X*X)
    for p in primes:
        if L%p==0:continue
        t=c*pow(d,-1,p)%p;v=math.isqrt(a*a+c*c)*pow(d,-1,p)%p;w=R*pow(d,-1,p)%p
        assert v*v%p==(t*t+S*S)%p and w*w%p==(t*t+H*H)%p
        for sigma in [-1,1]:
            K=eps*h*(R+sigma*a)
            assert chi(K,p)==chi(eps*h*d,p)*chi(w+sigma*S,p)
            phase_checks+=1
# Exact CRT receiver and sparse-measure L1 bound on actual masked support.
pop=[r for r in records if r['branch_local2_square'] and not r['branch_conductor_obstructions'] and r['c_chart']**16>10**18]
pair_tests=[]
for p,q in [(29,31),(37,41),(43,47),(53,59),(61,67)]:
    blocks=defaultdict(Counter);direct=[0,0];bad=0
    for r in pop:
        F,d,c=face(r);S,X,H=F;a=r['shared_edge'];R=r['R'];h=math.gcd(R,a);eps=2 if a%2 else 1;m=p*q
        L=2*d*h*S*X*H*abs(S*S-X*X)
        if math.gcd(L,m)>1:bad+=1;continue
        vp=math.isqrt(a*a+c*c);coord=tuple((u*pow(d,-1,ell)%ell) for ell in (p,q) for u in (c,vp,R))
        blocks[(F,eps*h*d%m)][coord]+=1
        for j,s in enumerate([-1,1]):direct[j]+=chi(eps*h*(R+s*a),p)*chi(eps*h*(R+s*a),q)
    main=[Fraction(0),Fraction(0)];signed=[Fraction(0),Fraction(0)];l1=Fraction(0);lower=Fraction(0)
    for (F,z),counts in blocks.items():
        n=sum(counts.values());r0=len(counts);Np,Sm,Sp=complete[(F,p)];Nq,Tm,Tp=complete[(F,q)];M=Np*Nq
        mean=Fraction(n,M);co=chi(z,p)*chi(z,q)
        l1+=sum(abs(Fraction(v)-mean) for v in counts.values())+(M-r0)*mean
        lower+=2*n*(1-Fraction(r0,M))
        for j,s in enumerate([-1,1]):
            base=co*mean*([Sm,Sp][j])*([Tm,Tp][j]);main[j]+=base
            val=sum(v*co*chi(k[2]+s*F[0],p)*chi(k[5]+s*F[0],q) for k,v in counts.items())
            signed[j]+=val-base
    assert l1>=lower and l1<=2*(len(pop)-bad)
    assert [main[j]+signed[j] for j in range(2)]==direct
    pair_tests.append({'p':p,'q':q,'N_good':len(pop)-bad,'bad':bad,'blocks':len(blocks),'direct':direct,'complete_term':[str(x) for x in main],'signed_discrepancy':[str(x) for x in signed],'L1':str(l1),'L1_lower':str(lower)})
out={'card':'M3-T11-213','input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'rational_curve_adapters':len(records),'distinct_faces':len(curves),'complete_good_curve_prime_cases':cases,'physical_good_phase_checks':phase_checks,'local_examples':local,'masked_tail':len(pop),'actual_CRT_receiver_checks':pair_tests,'scope':'exact adapter, local complete bounds replay and sparse L1 firewall; no physical cancellation or global saving','independent_audit':'NOT RUN'}
Path('M3-T11-213-verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='local_examples'},indent=2))
