"""Card210 exact valuation-layer and moment replay; finite census only."""
import json, math, hashlib
from pathlib import Path
from fractions import Fraction

src=Path('M3-T11-208-verification.json')
rs=json.loads(src.read_text())['records']
primes=[3,5,7,11,13,17,19,23,29,31,37,41,43]
def chi(a,p):
    if a%p==0: return 0
    return 1 if pow(a%p,(p-1)//2,p)==1 else -1
def vp(a,p):
    v=0
    while a%p==0: a//=p;v+=1
    return v,a
def layered(a,p):
    total=0; power=1
    while power<=a:
        if a%power==0: total+=chi(a//power,p)
        power*=p*p
    return total
def direct(a,p):
    v,u=vp(a,p)
    return chi(u,p) if v%2==0 else 0
checks=0; hidden=[]
for r in rs:
    for side in ['minus','plus']:
        a=r['coprime_'+side];k=r[side+'_kernel']
        for p in primes:
            assert layered(a,p)==direct(a,p)==chi(k,p)
            checks+=1
            if chi(a,p)==0 and direct(a,p)==-1 and r['branch_local2_square'] and not r['branch_conductor_obstructions']:
                hidden.append({'edges':r['edges'],'R':r['R'],'c_chart':r['c_chart'],'branch':side,'prime':p,'A':a,'kernel':k,'valuation':vp(a,p)[0]})
# Dense small-integer replay tests odd/even valuation and genuine squares.
for a in range(1,10001):
    for p in [3,5,7,11,13,17,19]:
        assert layered(a,p)==direct(a,p)
        if math.isqrt(a)**2==a: assert layered(a,p)==1
        checks+=1
# B=10^6, primes>=B^alpha with alpha=0.16: 11..43 suffice for a concrete
# finite height inequality p^8>2B; no appeal to calibrated Burgess constants.
large=[11,13,17,19,23,29,31,37,41,43]; B=10**6
assert min(large)**8>2*B
triangle=[(j,k) for j in range(4) for k in range(4) if j+k<=3]
twocheck=0
for r in rs:
    for side in ['minus','plus']:
        a=r['coprime_'+side]
        for ii,p in enumerate(large):
            for q in large[ii+1:]:
                total=0
                for j,k in triangle:
                    power=p**(2*j)*q**(2*k)
                    if a%power==0: total+=chi(a//power,p)*chi(a//power,q)
                assert total==direct(a,p)*direct(a,q)
                twocheck+=1
moments=[]
for num,den in [(3,16),(5,24),(11,48)]:
    pop=[r for r in rs if r['c_chart']**den>B**num and r['branch_local2_square'] and not r['branch_conductor_obstructions']]
    Q=len(primes); N=len(pop); diagonal=0; off=0; sumsq=0
    for r in pop:
        for side in ['minus','plus']:
            signs=[direct(r['coprime_'+side],p) for p in primes]
            diagonal+=sum(s*s for s in signs)
            off+=sum(signs[i]*signs[j] for i in range(Q) for j in range(i+1,Q))
            sumsq+=sum(signs)**2
    assert sumsq==diagonal+2*off
    odd=2*N*Q-diagonal
    bound=Fraction(N,Q)-Fraction(odd,2*Q*Q)+Fraction(off,Q*Q)
    assert bound==Fraction(sumsq,2*Q*Q)>=0
    endpoints=sum(math.isqrt(r['coprime_minus'])**2==r['coprime_minus'] and math.isqrt(r['coprime_plus'])**2==r['coprime_plus'] for r in pop)
    assert endpoints<=bound
    moments.append({'B':B,'threshold':f'{num}/{den}','N':N,'prime_count':Q,'diagonal':diagonal,'odd_valuation_incidences':odd,'offdiagonal_signed_sum':off,'branch_sum_squares':sumsq,'endpoint_bound_exact':str(bound),'endpoints':endpoints})
out={'card':'M3-T11-210','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'scope':'exact receiver and finite replay, no asymptotic correlation saving','single_layer_checks':checks,'two_prime_triangle_checks':twocheck,'hidden_unit_nonresidue_examples':hidden,'triangle':triangle,'moments':moments,'independent_audit':'NOT RUN'}
Path('M3-T11-210-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
