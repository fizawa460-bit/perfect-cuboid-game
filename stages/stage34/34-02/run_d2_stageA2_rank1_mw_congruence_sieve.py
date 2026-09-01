#!/usr/bin/env python3
from __future__ import annotations
import collections, hashlib, json, math, pathlib, re
from fractions import Fraction
from math import gcd, lcm

ROOT=pathlib.Path(__file__).resolve().parent
SEL=ROOT/"d2-stageA2-rank1-cover-selection.json"
MW=ROOT/"d2-stageA2-selected-rank1-mw-default.json"
LOCK=ROOT/"d2-stageA2-rank1-mw-congruence-sieve-lock.json"
OUT=ROOT/"d2-stageA2-rank1-mw-congruence-sieve.json"
PRIME_BOUND=211
MAX_PRIMES=12
STATE_CAP=300000


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def isprime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True
def primes(n):return [p for p in range(2,n+1) if isprime(p)]
def invmod(a,p):return pow(a%p,-1,p)
def fracmod(q,p):return (q.numerator%p)*invmod(q.denominator,p)%p
def legendre(x,p):
    x%=p
    if x==0:return 0
    return 1 if pow(x,(p-1)//2,p)==1 else -1

def parse_fraction(s):
    a=s.split('/')
    return Fraction(int(a[0]),int(a[1])) if len(a)==2 else Fraction(int(a[0]),1)
def parse_gen(line):
    z=line.replace(' ','')
    m=re.match(r'^\[\[1\],\[\[([^,\]]+),([^,\]]+)\]\]\]$',z)
    assert m,line
    return parse_fraction(m.group(1)),parse_fraction(m.group(2))

def mul(q1,q2):
    out=[0]*5
    for i,x in enumerate(q1):
        for j,y in enumerate(q2):out[i+j]+=x*y
    return out

def form_coeffs(a,b):return {"U":[1,0,-1],"V":[0,2,0],"A":[a,2*b,-a],"B":[b,2*a,-b]}
def roots_form(q,name):
    a,b=map(int,q.split('/')); h=math.isqrt(a*a+b*b); assert h*h==a*a+b*b
    if name=="U":return [Fraction(1),Fraction(-1)]
    if name=="V":return [Fraction(0),None]
    if name=="A":return [Fraction(-b+h,a),Fraction(-b-h,a)]
    if name=="B":return [Fraction(-a+h,b),Fraction(-a-h,b)]
    raise AssertionError(name)
def quartic_coeff_desc(q,pair,s):
    a,b=map(int,q.split('/')); fs=form_coeffs(a,b); f1,f2=pair.split('*')
    return [s*x for x in mul(fs[f1],fs[f2])]
def eval4(c,t):return c[0]*t**4+c[1]*t**3+c[2]*t**2+c[3]*t+c[4]
def direct_cubic(q,pair,s,r):
    c4,c3,c2,c1,c0=map(Fraction,quartic_coeff_desc(q,pair,s)); assert eval4([c4,c3,c2,c1,c0],r)==0
    A=4*c4*r**3+3*c3*r**2+2*c2*r+c1
    B=6*c4*r**2+3*c3*r+c2
    C=4*c4*r+c3
    D=c4
    assert A!=0
    pp=A*C-B*B/Fraction(3)
    qq=Fraction(2)*B**3/Fraction(27)-B*A*C/Fraction(3)+A*A*D
    return A,B,C,D,pp,qq

def point_add(P,Q,p,a4):
    if P is None:return Q
    if Q is None:return P
    x1,y1=P;x2,y2=Q
    if x1==x2 and (y1+y2)%p==0:return None
    if P==Q:
        if y1%p==0:return None
        lam=(3*x1*x1+a4)*invmod(2*y1,p)%p
    else:lam=(y2-y1)*invmod(x2-x1,p)%p
    x3=(lam*lam-x1-x2)%p; y3=(lam*(x1-x3)-y1)%p
    return x3,y3
def point_count(p,a4,a6):
    n=1
    for x in range(p):n+=1+legendre((x*x*x+a4*x+a6)%p,p)
    return n
def point_order(P,p,a4,a6):
    if P is None:return 1
    N=point_count(p,a4,a6); R=None
    for n in range(1,N+1):
        R=point_add(R,P,p,a4)
        if R is None:return n
    raise AssertionError((p,N,P))
def reduce_point(P,p):return None if P is None else (fracmod(P[0],p),fracmod(P[1],p))

def branch_data(br,gens):
    mid=int(br["selected_rank1_model"]["model_id"]); pair=br["selected_rank1_model"]["pair_occurrences"][0]
    ent=next(x for x in br["pair_ranks"] if x["pair"]==pair); s=int(ent["squareclass"]); q=br["q"]
    f1,f2=pair.split('*'); rs=roots_form(q,f1); r=next(x for x in rs if x is not None)
    A,B,C,D,pp,qq=direct_cubic(q,pair,s,r)
    a4=Fraction(int(ent["a4"])); a6=Fraction(int(ent["a6"]))
    assert a4==81*pp and a6==729*qq
    roots=roots_form(q,f1)+roots_form(q,f2); assert all(x is not None for x in roots) and len(set(roots))==4
    tors=[None]
    for rr in roots:
        if rr==r:continue
        x=9*A/(rr-r)+3*B; assert x**3+a4*x+a6==0
        tors.append((x,Fraction(0)))
    assert len(tors)==4 and len({str(x) for x in tors})==4
    G=gens[mid]; assert G[1]**2==G[0]**3+a4*G[0]+a6
    return {"mid":mid,"pair":pair,"s":s,"q":q,"r":r,"A":A,"B":B,"a4":a4,"a6":a6,"tors":tors,"G":G}

def model_good_prime(bd,p):
    if p<5:return False
    a4=int(bd["a4"]);a6=int(bd["a6"])
    return (4*a4**3+27*a6**2)%p!=0
def torsion_certificate(bd):
    g=0; used=[]
    for p in primes(PRIME_BOUND):
        if not model_good_prime(bd,p):continue
        N=point_count(p,int(bd["a4"])%p,int(bd["a6"])%p); g=gcd(g,N); used.append({"p":p,"group_order":N,"running_gcd":g})
        if g==4:break
    assert g==4
    return {"model_id":bd["mid"],"explicit_rational_2_torsion_order":4,"reduction_group_orders":used,"gcd":4,"full_rational_torsion_order":4}
def good_prime_for_branch(br,bd,p):
    if p<5 or not model_good_prime(bd,p):return False
    a,b=map(int,br["q"].split('/')); bad=6*a*b*(a*a-b*b)
    for d in br["delta"]:bad*=int(d)
    if bad%p==0:return False
    rats=[bd["r"],bd["A"],bd["B"],bd["G"][0],bd["G"][1]]+[T[0] for T in bd["tors"] if T is not None]
    if any(x.denominator%p==0 for x in rats):return False
    if bd["A"].numerator%p==0:return False
    return True
def tproj_from_E(R,bd,p):
    r=fracmod(bd["r"],p)
    if R is None:return r,1
    x,y=R; den=(x-fracmod(3*bd["B"],p))%p
    if den==0:return 1,0
    return (r+fracmod(9*bd["A"],p)*invmod(den,p))%p,1
def branch_forms_mod(q,T,S,p):
    a,b=map(int,q.split('/')); U=(T*T-S*S)%p; V=(2*T*S)%p
    return U,V,(a*U+b*V)%p,(b*U+a*V)%p
def branch_pass_mod(br,T,S,p):
    vals=branch_forms_mod(br["q"],T,S,p)
    for d,v in zip(br["delta"],vals):
        z=v*invmod(int(d),p)%p
        if legendre(z,p)==-1:return False
    return True
def allowed_at_prime(br,bd,p):
    if not good_prime_for_branch(br,bd,p):return None
    a4=int(bd["a4"])%p;a6=int(bd["a6"])%p; G=reduce_point(bd["G"],p)
    assert G is not None and (G[1]*G[1]-G[0]**3-a4*G[0]-a6)%p==0
    m=point_order(G,p,a4,a6); tors=[reduce_point(T,p) for T in bd["tors"]]
    assert len({str(T) for T in tors})==4
    arr=[]
    for Ti in tors:
        aset=set(); nG=None
        for n in range(m):
            R=point_add(nG,Ti,p,a4); T,S=tproj_from_E(R,bd,p)
            if branch_pass_mod(br,T,S,p):aset.add(n)
            nG=point_add(nG,G,p,a4)
        arr.append(aset)
    return m,arr
def crt_pair(a,M,b,m):
    if M==1:return b%m,m
    g=gcd(M,m)
    if (b-a)%g:return None
    L=M//g*m; M1=M//g; m1=m//g
    if m1==1:return a%L,L
    k=((b-a)//g*pow(M1,-1,m1))%m1
    return (a+M*k)%L,L
def combine_states(states,M,allowed,m):
    new=set()
    for a in states:
        for b in allowed:
            z=crt_pair(a,M,b,m)
            if z is not None:
                new.add(z[0])
                if len(new)>STATE_CAP:return None,None
    return new,lcm(M,m)
def sieve_branch(br,bd):
    candidates=[]
    for p in primes(PRIME_BOUND):
        ap=allowed_at_prime(br,bd,p)
        if ap is None:continue
        m,arr=ap
        if sum(len(s) for s in arr)<4*m:candidates.append((p,m,arr))
    states=[{0} for _ in range(4)]; Ms=[1]*4; used=[]; remaining=candidates[:]
    for _ in range(MAX_PRIMES):
        best=None
        for p,m,arr in remaining:
            nsall=[]; nMall=[]; overflow=False
            for j in range(4):
                ns,nM=combine_states(states[j],Ms[j],arr[j],m)
                if ns is None:overflow=True;break
                nsall.append(ns);nMall.append(nM)
            if overflow:continue
            score=(sum(len(x) for x in nsall),max(len(x) for x in nsall),p)
            if best is None or score<best[0]:best=(score,p,m,arr,nsall,nMall)
        if best is None:break
        _,p,m,arr,states,Ms=best
        used.append({"p":p,"generator_order":m,"local_allowed_counts":[len(x) for x in arr],"combined_state_counts":[len(x) for x in states],"combined_moduli":Ms[:]})
        remaining=[x for x in remaining if x[0]!=p]
        if all(not s for s in states):break
    return all(not s for s in states),used,[len(s) for s in states],Ms

lock=json.loads(LOCK.read_text()); sel=json.loads(SEL.read_text()); mw=json.loads(MW.read_text())
assert lock["status"]=="SOURCE_LOCKED_PREEXECUTION"
assert sel["status"]=="PASS_EXACT_14_MODEL_RANK1_COVER_OF_76_BRANCHES" and sel["remaining_branches"]==76
assert "branches" in sel and len(sel["branches"])==76,"regenerate run_d2_stageA2_rank1_cover_selection.py first"
assert mw["status"]=="PASS_ALL_14_UNCONDITIONAL_FULL_MW_BASES" and mw["certified_count"]==14
gens={int(x["model_id"]):parse_gen(x["mwrank_o_line"]) for x in mw["models"]}
assert sorted(gens)==sorted(map(int,mw["certified_models"]))

bdata={}; representatives={}
for br in sel["branches"]:
    bd=branch_data(br,gens); bdata[br["branch_id"]]=bd; representatives.setdefault(bd["mid"],bd)
assert len(representatives)==14
torsion_certs=[torsion_certificate(representatives[mid]) for mid in sorted(representatives)]

closed=[]; unresolved=[]
for br in sel["branches"]:
    bd=bdata[br["branch_id"]]; ok,used,counts,mods=sieve_branch(br,bd)
    rec={"q":br["q"],"branch_id":br["branch_id"],"delta":list(map(int,br["delta"])),"model_id":bd["mid"],"pair":bd["pair"],"used_primes":used,"final_state_counts":counts,"final_moduli":mods}
    if ok:
        assert counts==[0,0,0,0];closed.append(rec)
    else:unresolved.append({"q":br["q"],"branch_id":br["branch_id"],"model_id":bd["mid"],"pair":bd["pair"],"final_state_counts":counts,"final_moduli":mods})
closed_by_q=collections.Counter(x["q"] for x in closed); remaining_by_q=collections.Counter(x["q"] for x in unresolved)
exp=lock["expected"]
assert len(closed)==int(exp["closed_branches"]) and len(unresolved)==int(exp["remaining_branches"])
assert dict(sorted(closed_by_q.items()))==dict(sorted((k,int(v)) for k,v in exp["closed_by_q"].items()))
assert dict(sorted(remaining_by_q.items()))==dict(sorted((k,int(v)) for k,v in exp["remaining_by_q"].items()))

payload={
 "schema":"STAGE34_02_D2_STAGEA2_RANK1_MW_CONGRUENCE_SIEVE_V1",
 "status":"PASS_EXACT_MW_CONGRUENCE_CLOSURE_24_OF_76",
 "source_lock":"d2-stageA2-rank1-mw-congruence-sieve-lock.json",
 "source_sha256":{"rank1_cover_materialized":sha(SEL),"rank1_mw":sha(MW)},
 "parameters":{"prime_bound":PRIME_BOUND,"max_primes_per_branch":MAX_PRIMES,"state_cap_per_torsion_translate":STATE_CAP},
 "exact_map_verified_branches":76,
 "torsion_certificates":torsion_certs,
 "input_branches":76,"closed_branches":len(closed),"closed_by_q":dict(sorted(closed_by_q.items())),
 "remaining_branches":len(unresolved),"remaining_by_q":dict(sorted(remaining_by_q.items())),
 "closed":closed,"unresolved":unresolved,
 "credit":"Exactly the listed 24 branches are closed: for every rational torsion translate, generalized-CRT intersection of necessary good-prime congruence classes for the full MW integer n is empty. The 52 survivors receive no rational-point or closure credit.",
 "firewalls":{"finite_residue_survivor_is_Q_point":False,"one_translate_empty_closes_branch":False,"remaining_52_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"closed":len(closed),"closed_by_q":payload["closed_by_q"],"remaining":len(unresolved),"remaining_by_q":payload["remaining_by_q"]},sort_keys=True))
