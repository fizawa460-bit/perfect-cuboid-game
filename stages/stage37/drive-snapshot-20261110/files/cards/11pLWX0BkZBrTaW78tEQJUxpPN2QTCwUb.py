"""80-digit geometric replay; not a perfect-endpoint census."""
from decimal import Decimal, getcontext
from itertools import combinations_with_replacement, product
import json
getcontext().prec=80
D=Decimal; eps=D('1e-65'); triples=0; signed=0
for a,b,c in combinations_with_replacement(range(1,19),3):
    es=list(map(D,(a,b,c))); R2=sum(e*e for e in es); R=R2.sqrt()
    fs=[(R2-e*e).sqrt() for e in es]
    xs=[e*f for e,f in zip(es,fs)]; P=sum(xs)
    ls=[P-2*x for x in xs]; ell=min(ls)
    assert ell>0 and ell+eps>=D(a)*R/D(6).sqrt() and ell<=D(a)*R+eps
    assert ls[1]+eps>=xs[0] and ls[2]+eps>=xs[0]/2
    assert ls[0]/P+eps>=D(1)/3
    for signs in product((-1,1),repeat=3):
        ff=[s*f for s,f in zip(signs,fs)]
        N=sum(e*f for e,f in zip(es,ff)); As=[N-2*e*f for e,f in zip(es,ff)]
        vals=sorted([abs(N)]+list(map(abs,As)))
        targets=sorted([P]+ls)
        assert max(abs(x-y) for x,y in zip(vals,targets))<eps
        Y=es[0]*es[1]*ff[2]+es[0]*es[2]*ff[1]+es[1]*es[2]*ff[0]-ff[0]*ff[1]*ff[2]
        prodA=As[0]*As[1]*As[2]
        assert abs(R2*prodA-N*Y*Y)<eps
        assert abs(Y)+eps>=D(a)*R2/3
        assert abs(Y)<=R**3+eps
        assert min(vals)+eps>=D(a)*R/D(6).sqrt()
        signed+=1
    triples+=1
out={'status':'PASS','positive_real_sphere_edge_triples':triples,
     'signed_trace_states':signed,'precision_digits':80,
     'checked':['trace magnitude permutation','strict triangle and slack bounds','original Y product identity','imaginary phase lower bound'],
     'physical_endpoints':0,'independent_audit':'NOT RUN',
     'scope':'Positive real spheres with generally irrational faces; numerical replay only. Universal claims use the card proofs and retained204 counting theorem.'}
with open('M3-T11-220-verification.json','w') as f: json.dump(out,f,indent=2)
print(json.dumps(out))
