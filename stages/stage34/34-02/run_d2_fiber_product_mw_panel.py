#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, prod
import hashlib, json, pathlib, re

ROOT=pathlib.Path(__file__).resolve().parent
PANEL=[107,109,113,127]
FIBERS={
 "20/21":{"a":20,"b":21,"E_basis":[("-45/49","10/343")]},
 "80/39":{"a":80,"b":39,"E_basis":[("-160/39","1760/1521")]},
 "24/7":{"a":24,"b":7,"E_basis":[("-75/7","510/49")]},
 "84/13":{"a":84,"b":13,"E_basis":[("17787/169","216678/169")]},
 "48/55":{"a":48,"b":55,"E_basis":[("-24/25","24/275")]},
 "20/99":{"a":20,"b":99,"E_basis":[("-20/27","980/2673")]},
 "60/11":{"a":60,"b":11,"E_basis":[("-180/11","7020/121"),("-300/11","5100/121")]},
}

def inv(a,p): return pow(a%p,-1,p)
def red(v,p):
    f=Fraction(v); return f.numerator%p*inv(f.denominator,p)%p

def add(P,Q,a2,a4,p):
    if P is None: return Q
    if Q is None: return P
    x1,y1=P; x2,y2=Q
    if x1==x2 and (y1+y2)%p==0: return None
    if P==Q:
        if y1%p==0: return None
        m=(3*x1*x1+2*a2*x1+a4)*inv(2*y1,p)%p
    else: m=(y2-y1)*inv(x2-x1,p)%p
    x3=(m*m-a2-x1-x2)%p
    y3=(-y1+m*(x1-x3))%p
    return (x3,y3)
def mul(P,n,a2,a4,p):
    if n<0: return mul(None if P is None else (P[0],-P[1]%p),-n,a2,a4,p)
    R=None; Q=P
    while n:
        if n&1: R=add(R,Q,a2,a4,p)
        Q=add(Q,Q,a2,a4,p); n//=2
    return R
def order(P,a2,a4,p):
    if P is None:return 1
    R=None
    for n in range(1,p+2+2*isqrt(p)+33):
        R=add(R,P,a2,a4,p)
        if R is None:return n
    raise RuntimeError("order not found")

def parse_points(line):
    pts=[]
    for x,y in re.findall(r"\[(-?\d+(?:/\d+)?),(-?\d+(?:/\d+)?)\]",line): pts.append((x,y))
    return pts
def parse_iso(s):
    vals=[Fraction(x.strip()) for x in s.strip()[1:-1].split(',')]
    assert len(vals)==4
    return vals

def canon_hash(rows):
    data=json.dumps(sorted([list(r) for r in rows]),separators=(",",":"))
    return hashlib.sha256(data.encode()).hexdigest()
def bucket_hash(buckets,wild):
    rows=[]
    for k in sorted(buckets,key=lambda z:(str(type(z)),str(z))):
        st=buckets[k]
        rows.append([str(k),len(st),canon_hash(st)])
    rows.append(["WILDCARD",len(wild),canon_hash(wild)])
    return hashlib.sha256(json.dumps(rows,separators=(",",":"),sort_keys=True).encode()).hexdigest()

def p1(X,Z,p):
    X%=p; Z%=p
    if X==0 and Z==0:return None
    if Z==0:return "inf"
    return X*inv(Z,p)%p

def point_states(basis,torsion,a2,a4,p,xfunc):
    mods=[order(P,a2,a4,p) for P in basis]
    mults=[[mul(P,n,a2,a4,p) for n in range(m)] for P,m in zip(basis,mods)]
    buckets={}; wild=[]
    for coeffs in product(*[range(m) for m in mods]):
        Q=None
        for arr,n in zip(mults,coeffs): Q=add(Q,arr[n],a2,a4,p)
        for lab,T in torsion:
            R=add(Q,T,a2,a4,p)
            key=xfunc(R)
            state=tuple(coeffs)+tuple(lab)
            if key is None:wild.append(state)
            else:buckets.setdefault(key,[]).append(state)
    return mods,buckets,wild

def project_state(st,rank,mods):
    return tuple(st[i]%mods[i] if mods[i]>1 else 0 for i in range(rank))+tuple(st[rank:])
def project_buckets(buckets,wild,rank,mods):
    out={k:{project_state(s,rank,mods) for s in v} for k,v in buckets.items()}
    return out,{project_state(s,rank,mods) for s in wild}

def setup_E(name,p):
    f=FIBERS[name]; a,b=f["a"],f["b"]
    assert (2*a*b*(a*a-b*b)*(a*a+b*b))%p
    q=a%p*inv(b,p)%p; a2=(1+q*q)%p; a4=q*q%p
    basis=[(red(x,p),red(y,p)) for x,y in f["E_basis"]]
    R4=(q,q*(q+1)%p); S2=(-1%p,0)
    assert order(R4,a2,a4,p)==4 and order(S2,a2,a4,p)==2
    tors=[]
    for r in range(4):
      for s in range(2): tors.append(((r,s),add(mul(R4,r,a2,a4,p),mul(S2,s,a2,a4,p),a2,a4,p)))
    assert len({x[1] for x in tors})==8
    return q,a2,a4,basis,tors

def setup_J(name,p,jrec):
    a,b=FIBERS[name]["a"],FIBERS[name]["b"]; q=a%p*inv(b,p)%p
    a4=red(jrec["jacobian_a4"],p); a6=red(jrec["jacobian_a6"],p)
    basis=[(red(x,p),red(y,p)) for x,y in parse_points(jrec["mwrank_o_line"])]
    assert len(basis)==jrec["rank"]
    R4=((5-q*q)*inv(3,p)%p,2*(q*q-1)%p)
    S2=((-q*q+6*q-1)*inv(3,p)%p,0)
    assert order(R4,0,a4,p)==4 and order(S2,0,a4,p)==2
    tors=[]
    for r in range(4):
      for s in range(2): tors.append(((r,s),add(mul(R4,r,0,a4,p),mul(S2,s,0,a4,p),0,a4,p)))
    assert len({x[1] for x in tors})==8
    return q,a4,a6,basis,tors

def jq_xfunc(name,d,p,case):
    a,b=FIBERS[name]["a"],FIBERS[name]["b"]
    rr,ss,tt,uu=parse_iso(case["isomorphism_data_to_common_Jq"])
    r,s,t,u=[red(z,p) for z in (rr,ss,tt,uu)]
    assert u%p
    invpol=case["inverse_polynomials"]
    assert invpol[0].replace(" ","")=="$.2*$.3"
    assert invpol[2].replace(" ","")=="2*$.1*$.3+$.2*$.3"
    def f(Q):
        if Q is None:
            T,S=(1,1) if d==1 else (0,1)
        else:
            Xj,Yj=Q
            xe=(Xj-r)*inv(u*u,p)%p
            ye=(Yj-s*(Xj-r)-t)*inv(u*u*u,p)%p
            T=ye; S=(2*xe+ye)%p
        if d==1:
            X=a*(T*T-S*S); Z=2*b*T*S
        else:
            X=a*(2*T*T-4*T*S+S*S); Z=b*(2*T*T-S*S)
        return p1(X,Z,p)
    return f

def E_xfunc(Q): return "inf" if Q is None else Q[0]

maps=json.loads((ROOT/"d2-quartic-map-certificate.json").read_text())
jcert=json.loads((ROOT/"d2-jacobian-mw-certificate.json").read_text())
case_map={(c["q"],c["d"]):c for c in maps["cases"]}
j_map={r["q"]:r for r in jcert["fibers"]}
assert len(case_map)==14 and set(j_map)==set(FIBERS)

# Per case / prime full finite relation, retained in compressed x-bucket form.
structures={}; summaries=[]
for name in FIBERS:
  for d in (1,2):
    prime_data=[]
    for p in PANEL:
        q,e_a2,e_a4,e_basis,e_tor=setup_E(name,p)
        qj,j_a4,j_a6,j_basis,j_tor=setup_J(name,p,j_map[name]); assert q==qj
        emods,eb,ew=point_states(e_basis,e_tor,e_a2,e_a4,p,E_xfunc); assert not ew
        jmods,jb,jw=point_states(j_basis,j_tor,0,j_a4,p,jq_xfunc(name,d,p,case_map[(name,d)]))
        common=set(eb)&set(jb)
        allowed=sum(len(eb[x])*len(jb[x]) for x in common)+sum(len(v) for v in eb.values())*len(jw)
        total=sum(len(v) for v in eb.values())*(sum(len(v) for v in jb.values())+len(jw))
        prime_data.append({"p":p,"emods":emods,"jmods":jmods,"eb":eb,"jb":jb,"jw":jw,"allowed":allowed,"total":total,
                           "relation_hash":hashlib.sha256((bucket_hash(eb,[])+bucket_hash(jb,jw)).encode()).hexdigest()})
    erank=len(prime_data[0]["emods"]); jrank=len(prime_data[0]["jmods"])
    em=[prime_data[0]["emods"][i] for i in range(erank)]
    jm=[prime_data[0]["jmods"][i] for i in range(jrank)]
    for z in prime_data[1:]:
        em=[gcd(x,y) for x,y in zip(em,z["emods"])]
        jm=[gcd(x,y) for x,y in zip(jm,z["jmods"])]
    projected=[]
    for z in prime_data:
        ep,_=project_buckets(z["eb"],[],erank,em)
        jp,jw=project_buckets(z["jb"],z["jw"],jrank,jm)
        loc=set()
        for x in set(ep)&set(jp):
            for es in ep[x]:
                for js in jp[x]: loc.add(es+js)
        if jw:
            all_e=set().union(*ep.values()) if ep else set()
            for es in all_e:
                for js in jw: loc.add(es+js)
        projected.append(loc)
    inter=set.intersection(*projected)
    possible=prod(em)*8*prod(jm)*8
    rec={"q":name,"d":d,"E_rank":erank,"J_rank":jrank,"common_E_moduli":em,"common_J_moduli":jm,
         "common_projection_total":possible,"common_projection_survivors":len(inter),"common_projection_sha256":canon_hash(inter),
         "local":[{"p":z["p"],"E_basis_orders":z["emods"],"J_basis_orders":z["jmods"],"allowed_pairs":z["allowed"],"total_pairs":z["total"],"relation_hash":z["relation_hash"],"J_indeterminate_states":len(z["jw"])} for z in prime_data]}
    summaries.append(rec)
    print(f"PASS {name} d={d}: common mods E={em} J={jm}; projection {len(inter)}/{possible}")

payload={"schema":"STAGE34_02_D2_FIBER_PRODUCT_MW_PANEL_V1","status":"PASS_EXACT_FOUR_PRIME_MATCHING_X_PANEL",
 "primes":PANEL,"source_maps":"d2-quartic-map-certificate.json","source_jacobian_mw":"d2-jacobian-mw-certificate.json",
 "source_jacobian_torsion":"d2-jacobian-torsion-lock.json","cases":summaries,
 "globally_eliminated_cases":[[r["q"],r["d"]] for r in summaries if r["common_projection_survivors"]==0],
 "firewalls":{"finite_panel_is_proof_complete_global_MW_sieve":False,"nonempty_common_projection_is_rational_point":False,"receiver_closed":False}}
(ROOT/"d2-fiber-product-mw-panel.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("PASS exact D2 fiber-product MW panel; finite survivors grant no closure unless projection is empty")
