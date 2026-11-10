"""Card211 physical aggregate-depth replay, no distribution assumption."""
import json,math,hashlib
from pathlib import Path
from fractions import Fraction
src=Path('M3-T11-208-verification.json');rs=json.loads(src.read_text())['records']
S=[11,13,17,19,23,29,31,37,41,43];Q=len(S);B=10**6;P=min(S)
def chi(a,p):
    if a%p==0:return 0
    return 1 if pow(a%p,(p-1)//2,p)==1 else -1
def lam(a,p):
    v=0
    while a%p==0:a//=p;v+=1
    return chi(a,p) if v%2==0 else 0
def dmax(limit,P):
    d=0
    while P**(2*(d+1))<limit:d+=1
    return d
d=dmax(2*B,P);assert d==3 and P**8>2*B
pairs=[(p,q) for i,p in enumerate(S) for q in S[i+1:]]
layers=[(j,k) for j in range(4) for k in range(4) if j+k<=3]
check=0;dense=0
for A in range(1,100001):
    roots=sum(A%(p*p)==0 for p in S)
    assert roots<=d
    diff=sum(abs(lam(A,p)*lam(A,q)-chi(A,p)*chi(A,q)) for p,q in pairs)
    assert diff<=roots*Q-roots*(roots+1)//2<=d*(Q-1)
    if math.isqrt(A)**2==A:
        assert sum(chi(A,p) for p in S)>=Q-d
    dense+=1
out=[]
synthetic=0
for A in [11**6]+[(11*13)**2*v for v in range(1,31)]:
    assert A<2*B
    interior=0;nonzero=0
    for p,q in pairs:
        total=0
        for j,k in layers:
            t=p**(2*j)*q**(2*k)
            term=chi(A//t,p)*chi(A//t,q) if A%t==0 else 0
            total+=term
            if j+k>0:nonzero+=abs(term)
            if j>0 and k>0:interior+=abs(term)
        assert total==lam(A,p)*lam(A,q)
    s=sum(A%(p*p)==0 for p in S)
    assert nonzero<=s*Q-s*(s+1)//2 and interior<=s*(s-1)//2
    synthetic+=1
for num,den in [(3,16),(5,24),(11,48)]:
    pop=[r for r in rs if r['c_chart']**den>B**num and r['branch_local2_square'] and not r['branch_conductor_obstructions']]
    N=len(pop);branches=[]
    for side in ['minus','plus']:
        layer_sums={(p,q,j,k):0 for p,q in pairs for j,k in layers}
        moments=0;diag=0;rootinc=0;maxroots=0
        for r in pop:
            A=r['coprime_'+side];s=sum(A%(p*p)==0 for p in S);rootinc+=s;maxroots=max(maxroots,s)
            assert s<=d
            ordinary=[chi(A,p) for p in S];moments+=sum(ordinary)**2;diag+=sum(v*v for v in ordinary)
            for p,q in pairs:
                val=0
                for j,k in layers:
                    t=p**(2*j)*q**(2*k)
                    if A%t==0:
                        term=chi(A//t,p)*chi(A//t,q);val+=term
                        layer_sums[p,q,j,k]+=term
                assert val==lam(A,p)*lam(A,q);check+=1
        zero=sum(v for (p,q,j,k),v in layer_sums.items() if j+k==0)
        deep_abs=sum(abs(v) for (p,q,j,k),v in layer_sums.items() if j+k>0)
        interior_abs=sum(abs(v) for (p,q,j,k),v in layer_sums.items() if j>0 and k>0)
        assert deep_abs<=N*d*(Q-1)
        assert interior_abs<=N*d*(d-1)//2
        assert moments==diag+2*zero
        branches.append({'branch':side,'square_prime_incidences':rootinc,'max_square_prime_count':maxroots,
          'deep_layer_absolute_sum':deep_abs,'deep_layer_upper':N*d*(Q-1),'interior_absolute_sum':interior_abs,'interior_upper':N*d*(d-1)//2,
          'zero_layer_signed_sum':zero,'ordinary_diagonal':diag,'ordinary_moment':moments})
    bound=Fraction(sum(b['ordinary_moment'] for b in branches),2*(Q-d)**2)
    E=sum(math.isqrt(r['coprime_minus'])**2==r['coprime_minus'] and math.isqrt(r['coprime_plus'])**2==r['coprime_plus'] for r in pop)
    assert E<=bound
    out.append({'threshold':f'{num}/{den}','N':N,'Q':Q,'d':d,'branches':branches,'direct_ordinary_moment_bound':str(bound),'physical_endpoints':E})
result={'card':'M3-T11-211','scope':'summed depth-layer bound on actual physical population; zero-layer cancellation and total tail still OPEN',
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'prime_pool':S,'B':B,'dense_pointwise_checks':dense,'synthetic_integer_layer_cases':synthetic,'physical_pair_layer_checks':check,'threshold_results':out,'independent_audit':'NOT RUN'}
Path('M3-T11-211-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
