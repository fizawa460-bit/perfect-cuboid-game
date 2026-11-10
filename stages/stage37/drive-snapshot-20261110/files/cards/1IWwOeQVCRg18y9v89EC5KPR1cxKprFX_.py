"""Card212 finite physical graph injection/cleared-character replay."""
import json,math,hashlib
from pathlib import Path
src=Path('M3-T11-208-verification.json');rs=json.loads(src.read_text())['records']
S=[11,13,17,19,23,29,31,37,41,43];Q=len(S);seen={};checks=0;cleared=0
def chi(a,p):
    if a%p==0:return 0
    return 1 if pow(a%p,(p-1)//2,p)==1 else -1
def sq(a):return math.isqrt(a)**2==a
for r in rs:
    edges=r['edges'];a=r['shared_edge'];R=r['R']
    assert len(set(edges))==3
    rest=edges.copy();rest.remove(a);b,c=sorted(rest)
    f1=math.isqrt(a*a+b*b);f2=math.isqrt(a*a+c*c)
    assert f1*f1==a*a+b*b and f2*f2==a*a+c*c
    d1=math.gcd(a,b);d2=math.gcd(a,c)
    F1=(a//d1,b//d1,f1//d1);F2=(a//d2,c//d2,f2//d2)
    g=math.gcd(F1[0],F2[0])
    rebuild=(F1[0]*F2[0]//g,F2[0]*F1[1]//g,F1[0]*F2[1]//g)
    assert rebuild==(a,b,c)
    key=tuple(sorted((F1,F2)));assert key not in seen;seen[key]=tuple(edges)
    assert math.gcd(F1[2],F2[1])*math.gcd(F2[2],F1[1])==r['c_chart']
    checks+=1
    h=math.gcd(R,a);eps=2 if a%2 else 1
    for sign,side in [(-1,'minus'),(1,'plus')]:
        A=r['coprime_'+side];K=eps*h*(R+sign*a)
        assert K==(eps*h)**2*A and sq(K)==sq(A)
        for p in S:
            assert chi(K,p)==chi(eps*h,p)*chi(R+sign*a,p)
            if h%p:assert chi(K,p)==chi(A,p)
            cleared+=1
# Abstract normalizations deliberately exercise p|h, unlike the bounded active
# M_2R survivors whose shared h happens to be1; not asserted physical cuboids.
syn=[]
for h in [1,11,13,17,121,143,187]:
    for D in range(5,102,2):
        for u in [1,2,3,4]:
            if math.gcd(D,u)>1:continue
            R=h*D;a=h*u;eps=2 if a%2 else 1
            for sign in [-1,1]:
                A=(D+sign*u)//eps;assert (D+sign*u)%eps==0 and A>0
                K=eps*h*(R+sign*a);assert K==(eps*h)**2*A
                diff=sum(abs(chi(A,p)*chi(A,q)-chi(K,p)*chi(K,q)) for i,p in enumerate(S) for q in S[i+1:])
                s=sum(h%p==0 for p in S)
                assert diff<=s*Q-s*(s+1)//2
                syn.append((R,a,eps,A,K))
tails=[]
for n,d in [(3,16),(5,24),(11,48)]:
    pop=[r for r in rs if r['c_chart']**d>10**(6*n) and r['branch_local2_square'] and not r['branch_conductor_obstructions']]
    diffs=0
    for side,sign in [('minus',-1),('plus',1)]:
        for i,p in enumerate(S):
            for q in S[i+1:]:
                G=C=0
                for r in pop:
                    a=r['shared_edge'];R=r['R'];h=math.gcd(R,a);eps=2 if a%2 else 1
                    A=r['coprime_'+side];K=eps*h*(R+sign*a)
                    G+=chi(A,p)*chi(A,q);C+=chi(K,p)*chi(K,q)
                diffs+=abs(G-C)
    tails.append({'threshold':f'{n}/{d}','N_star':len(pop),'normalization_correlation_difference':diffs})
out={'card':'M3-T11-212','scope':'exact endpoint-safe graph adapter and source-certified inherited half-power host; no new character cancellation',
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'physical_graph_injections':checks,'physical_cleared_character_checks':cleared,'abstract_normalization_cases':len(syn),
 'threshold_checks':tails,'independent_audit':'NOT RUN'}
Path('M3-T11-212-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
