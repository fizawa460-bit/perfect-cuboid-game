#!/usr/bin/env python3
import json,math,runpy,subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EY='stages/stage36/36-09EY/rho-radical-refinement-rank-compression-preflight.json'
EX='stages/stage36/36-09EX/rho-t6-controlled-radical-relaxation-preflight.json'
EXV='stages/stage36/verify_stage36_36_09EX.py'
SOURCE='stages/stage36/36-09EZ/rho-core-nullity-controlled-radical-search-source-lock.md'
CERT='stages/stage36/36-09EZ/rho-core-nullity-controlled-radical-search-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 EY:'dbad704b6e05eb0a08ff33b1794436cab7f94fc6',
 EX:'75663e2fbde9189a9c570a2075b76490151cd0b6',
 EXV:'3adbd3fe00b2e4c85261862f8e949a5c8af09c03',
 SOURCE:'ab491187ac22b336acf1c94149bc503616aa4e3d',
 CERT:'873eef8d82b89ecefe3e331b3038df9bff18fec0',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)
ey=load(EY);ex=load(EX);c=load(CERT)
assert ey['leaf_core_theorem']['sel2_identity']=='dim_F2 Sel^2(E_rho,p/Q)=nullity_F2(H)'
assert ey['replay_summary']['all_residual_nullity_two'] is True
assert c['entry_authority']['v284_exact_head']=='d3aef78cb57e15a5b371d7137dc61fda846c09ed'
assert c['entry_authority']['v284_exact_head_ci']=='34413590057/102673330087'
assert c['entry_authority']['36_09EZ_entry_allowed'] is True

# Reuse exact-green EX/ES support-matrix construction only after immutable locks.
ns=runpy.run_path(str(ROOT/EXV))
rank=ns['rank'];matrix_from_pattern=ns['matrix_from_pattern'];legbit=ns['legbit']

# Deterministic 64-bit primality/factorization for the retained fixed candidates.
def is_prime(n):
    if n<2:return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n==p:return True
        if n%p==0:return False
    d=n-1;s=0
    while d%2==0:s+=1;d//=2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a%n==0:continue
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True

def rho(n):
    if n%2==0:return 2
    if n%3==0:return 3
    for cc in range(1,100):
        x=2+cc;y=x;d=1
        for _ in range(200000):
            x=(x*x+cc)%n;y=(y*y+cc)%n;y=(y*y+cc)%n
            d=math.gcd(abs(x-y),n)
            if d==1:continue
            if d!=n:return d
            break
    raise AssertionError(('pollard-rho failed',n))

def factor(n,out=None):
    n=abs(n)
    if out is None:out=[]
    if n==1:return out
    if is_prime(n):out.append(n);return out
    d=rho(n);factor(d,out);factor(n//d,out);return out

def raw_pattern(SD,SP,SQ):
    verts=[(q,'D',q%8) for q in SD]+[(q,'P',q%8) for q in SP]+[(q,'Q',q%8) for q in SQ]
    odd=[q for q,_,_ in verts]
    return {
      'eps':'shallow',
      'vertices':[[lab,m8] for _,lab,m8 in verts],
      'legendre_bits':[[0 if i==j else legbit(odd[j],odd[i]) for j in range(len(odd))] for i in range(len(odd))]
    }

def peel(M):
    A=[list(r) for r in M];k=0
    while A and A[0]:
        nr=len(A);nc=len(A[0]);chosen=None
        for i in range(nr):
            js=[j for j in range(nc) if A[i][j]]
            if len(js)==1:chosen=(i,js[0]);break
        if chosen is None:
            for j in range(nc):
                ii=[i for i in range(nr) if A[i][j]]
                if len(ii)==1:chosen=(ii[0],j);break
        if chosen is None:break
        i,j=chosen
        B=[[A[r][q] for q in range(nc) if q!=j] for r in range(nr) if r!=i]
        assert rank(A)==1+rank(B)
        A=B;k+=1
    return k,A

def psi3_coeffs(a,b):
    N=a*a-b*b;M=a*a+b*b;d=a*b
    return [-64*N*N*d*d*(M**4+4*N*N*d*d),-192*N*N*d*d*M*M,-96*N*N*d*d,4*M*M,3]
def has_root_mod(coeffs,q):
    for x in range(q):
        y=0
        for z in reversed(coeffs):y=(y*x+z)%q
        if y==0:return True
    return False

# Exact previously promoted fixed-parameter registry: 44 pre-EX + 32 EX = 76.
prev={Fraction(x) for o in ns['previous_orbits'] for x in o}
for t in ex['templates']:
    prev.update(Fraction(x) for x in t['literal_orbit'])
assert len(prev)==76

rows=c['candidate_replay'];assert len(rows)==29
seen=set();spectrum={}
for row in rows:
    u=row['u'];K=729
    assert u==17627+34440*((u-17627)//34440) and (u-17627)%34440==0
    a=2*u;b=2*u+K;q=4*u+K
    assert math.gcd(a,b)==1
    A=8*u*u-K*K;B=8*u*u+8*K*u+K*K
    assert A%7==0 and B%41==0
    s=A//7;t=B//41
    vals={'u':u,'b':b,'q':q,'s':s,'t':t}
    fs={name:factor(v,[]) for name,v in vals.items()}
    for name,v in vals.items():
        z=1
        for p in fs[name]:assert is_prime(p);z*=p
        assert z==abs(v),(name,u,z,v)
    SD=sorted({3}|{p for name in ('u','b','q') for p in fs[name]})
    SP=sorted({7}|set(fs['s']))
    SQ=sorted({41}|set(fs['t']))
    assert not (set(SD)&set(SP) or set(SD)&set(SQ) or set(SP)&set(SQ))
    M,n=matrix_from_pattern(raw_pattern(SD,SP,SQ));r=rank(M)
    k,H=peel(M);rh=rank(H);m=len(H)
    assert (n,r,k,m,rh,m-rh)==(row['n'],row['rank'],row['leaf_pivots'],row['residual_size'],row['residual_rank'],row['residual_nullity'])
    assert r==2*n-2 and m-rh==2
    spectrum[f'{m}/{rh}']=spectrum.get(f'{m}/{rh}',0)+1
    D=-(2**4)*(3**6)*u*b*q
    rr=math.isqrt(abs(D));assert rr*rr!=abs(D)
    coeff=[z%5 for z in psi3_coeffs(a,b)]
    assert coeff==[4,0,4,0,3] and not has_root_mod(coeff,5)
    orbit={Fraction(a,b),Fraction(b,a),Fraction(K,q),Fraction(q,K)}
    assert len(orbit)==4 and not (orbit&prev) and not (orbit&seen)
    seen.update(orbit)

summary=c['replay_summary'];impact=c['registry_impact']
assert len(seen)==summary['new_fixed_parameter_count']==116
assert summary['new_u_count']==summary['new_literal_orbit_count']==29
assert summary['all_rank_2n_minus_2'] is True and summary['all_residual_nullity_two'] is True
assert summary['all_EH_no4_no3_screens_pass'] is True
assert spectrum==summary['residual_core_spectrum']
assert impact=={'previous_count':76,'new_orbits':29,'new_parameters':116,'disjoint':True,'provisional_count':192,'exact_sufficient_template_count_unchanged':17}
assert len(prev|seen)==192
assert c['search_family']['window_exhaustiveness_claimed'] is False
assert c['route_result']['next_leaf']=='36-09FA_RHO_RESIDUAL_CORE_TYPE_PARAMETRIC_REALIZATION_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for key,val in c['scope_firewalls'].items():assert val is False,(key,val)
print('36-09EZ verified: 29 explicit new controlled-radical u values have exact residual-core nullity two, pass EH no4/no3 screens, and give 29 disjoint four-point literal orbits. Provisional fixed-p registry 76->192; template count stays 17. No discovery-window exhaustivity, infinitude, parent receiver, or endpoint credit.')
