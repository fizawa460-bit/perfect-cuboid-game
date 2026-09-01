#!/usr/bin/env python3
"""Fiber-tailored fixed-quotient Mordell-Weil sieve for Stage34 D2.

The first four-prime diagnostic panel projected local coefficient groups only
through the gcd of all selected generator orders.  That is exact pruning, but
it can lose essentially all free-coordinate information if even one selected
prime has an odd order.

This script uses the proof-correct MW-sieve direction instead:

  1. choose a quotient modulus m first (prefer 4, otherwise 2);
  2. select only good primes where every relevant E_q/J_q free generator
     reduction order is divisible by m;
  3. discard a prime for a case if the chosen reduced coordinate presentation
     still has a [0:0] state (fail-closed presentation policy);
  4. project the exact matching-x relation into the fixed quotient;
  5. intersect those relations across fiber-tailored primes.

An empty intersection is a rigorous global obstruction for that (q,d).  A
nonempty intersection is only a surviving MW congruence class set.
"""
from fractions import Fraction
from math import prod
import hashlib, json, pathlib

ROOT=pathlib.Path(__file__).resolve().parent
base=(ROOT/"run_d2_fiber_product_mw_panel.py").read_text(encoding="utf-8")
marker='maps=json.loads'
assert marker in base
prefix,_=base.split(marker,1)
ns={"__file__":str(ROOT/"run_d2_fiber_product_mw_panel.py"),"__name__":"stage34_d2_tailored_engine"}
exec(prefix,ns)

maps=json.loads((ROOT/"d2-quartic-map-certificate.json").read_text())
jcert=json.loads((ROOT/"d2-jacobian-mw-certificate.json").read_text())
case_map={(c["q"],int(c["d"])):c for c in maps["cases"]}
j_map={r["q"]:r for r in jcert["fibers"]}
assert len(case_map)==14 and set(j_map)==set(ns["FIBERS"])


def isprime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

PRIMES=[p for p in range(131,402) if isprime(p)]


def jq_xfunc_exact(name,d,p,case):
    a,b=ns["FIBERS"][name]["a"],ns["FIBERS"][name]["b"]
    rr,ss,tt,uu=ns["parse_iso"](case["isomorphism_data_to_common_Jq"])
    try:
        r,s,t,u=[ns["red"](z,p) for z in (rr,ss,tt,uu)]
    except Exception:
        raise ValueError("iso denominator bad at p")
    if u%p==0: raise ValueError("u=0 at p")
    invpol=case["inverse_polynomials"]
    assert invpol[0].replace(" ","")=="$.2*$.3"
    assert invpol[2].replace(" ","")=="2*$.1*$.3+$.2*$.3"
    ainv=[Fraction(x.strip()) for x in case["magma_elliptic_a_invariants"].strip()[1:-1].split(',')]
    a1,a2,a3,a4,a6=ainv
    assert a6==0 and a3!=0 and 2*a3+a4!=0
    t0=a4/(2*a3+a4)
    def f(Q):
        if Q is None:
            T,S=(1,1) if d==1 else (0,1)
        else:
            Xj,Yj=Q
            xe=(Xj-r)*ns["inv"](u*u,p)%p
            ye=(Yj-s*(Xj-r)-t)*ns["inv"](u*u*u,p)%p
            if xe==0 and ye==0:
                try:
                    T=ns["red"](t0,p); S=1
                except Exception:
                    return None
            else:
                T=ye; S=(2*xe+ye)%p
        if d==1:
            X=a*(T*T-S*S); Z=2*b*T*S
        else:
            X=a*(2*T*T-4*T*S+S*S); Z=b*(2*T*T-S*S)
        return ns["p1"](X,Z,p)
    return f


def projected_relation(name,d,p,m):
    try:
        q,e_a2,e_a4,e_basis,e_tor=ns["setup_E"](name,p)
        qj,j_a4,j_a6,j_basis,j_tor=ns["setup_J"](name,p,j_map[name])
        if q!=qj:return None
        emods=[ns["order"](P,e_a2,e_a4,p) for P in e_basis]
        jmods=[ns["order"](P,0,j_a4,p) for P in j_basis]
        if any(z%m for z in emods+jmods):return None
        emods2,eb,ew=ns["point_states"](e_basis,e_tor,e_a2,e_a4,p,ns["E_xfunc"])
        if ew:return None
        jmods2,jb,jw=ns["point_states"](j_basis,j_tor,0,j_a4,p,jq_xfunc_exact(name,d,p,case_map[(name,d)]))
        if jw:return {"skip":"presentation_degeneracy","p":p,"emods":emods,"jmods":jmods}
        assert emods2==emods and jmods2==jmods
        erank=len(emods); jrank=len(jmods)
        ep,_=ns["project_buckets"](eb,[],erank,[m]*erank)
        jp,_=ns["project_buckets"](jb,[],jrank,[m]*jrank)
        loc=set()
        for x in set(ep)&set(jp):
            for es in ep[x]:
                for js in jp[x]: loc.add(es+js)
        return {
          "p":p,"emods":emods,"jmods":jmods,"relation":loc,
          "relation_size":len(loc),"relation_sha256":ns["canon_hash"](loc),
          "E_states":sum(len(v) for v in eb.values()),
          "J_states":sum(len(v) for v in jb.values())
        }
    except (AssertionError,ValueError,ZeroDivisionError):
        return None


def build_case(name,d):
    erank=len(ns["FIBERS"][name]["E_basis"])
    jrank=int(j_map[name]["rank"])
    attempts=[]
    chosen_m=None; candidates=None; degeneracies=[]
    for m in (4,2):
        raw=[]; deg=[]
        # Order-support prefilter, then keep the 12 cheapest full-state primes.
        supports=[]
        for p in PRIMES:
            try:
                q,e_a2,e_a4,e_basis,e_tor=ns["setup_E"](name,p)
                qj,j_a4,j_a6,j_basis,j_tor=ns["setup_J"](name,p,j_map[name])
                if q!=qj:continue
                eo=[ns["order"](P,e_a2,e_a4,p) for P in e_basis]
                jo=[ns["order"](P,0,j_a4,p) for P in j_basis]
                if all(z%m==0 for z in eo+jo):
                    supports.append((prod(eo)*prod(jo),p,eo,jo))
            except Exception:
                continue
        supports.sort()
        for _,p,eo,jo in supports[:12]:
            z=projected_relation(name,d,p,m)
            if z is None:continue
            if z.get("skip"):
                deg.append({"p":p,"emods":eo,"jmods":jo})
            else: raw.append(z)
        attempts.append({"m":m,"order_supported_primes":len(supports),"usable_relation_primes":len(raw),"presentation_degenerate":deg})
        if len(raw)>=3:
            chosen_m=m; candidates=raw; degeneracies=deg; break
    if chosen_m is None:
        return {"q":name,"d":d,"status":"INSUFFICIENT_FIXED_QUOTIENT_PRIMES","attempts":attempts}

    # Greedy exact intersection: pick the prime yielding the smallest current
    # survivor set, continue only while it strictly improves the intersection.
    selected=[]; inter=None; remaining=candidates[:]
    while remaining and len(selected)<6:
        best=None
        for z in remaining:
            new=z["relation"] if inter is None else inter & z["relation"]
            key=(len(new),z["relation_size"],z["p"])
            if best is None or key<best[0]: best=(key,z,new)
        _,z,new=best
        if inter is not None and len(new)>=len(inter): break
        selected.append(z); inter=new
        remaining=[w for w in remaining if w["p"]!=z["p"]]
        if not inter: break
    total=(chosen_m**(erank+jrank))*64
    return {
      "q":name,"d":d,"status":"EMPTY_GLOBAL_OBSTRUCTION" if not inter else "NONEMPTY_FIXED_QUOTIENT_SURVIVORS",
      "m":chosen_m,"E_rank":erank,"J_rank":jrank,"quotient_total":total,
      "selected_primes":[z["p"] for z in selected],
      "intersection_survivors":len(inter),"intersection_sha256":ns["canon_hash"](inter),
      "selected_steps":[{"p":z["p"],"E_orders":z["emods"],"J_orders":z["jmods"],"local_relation_size":z["relation_size"],"local_relation_sha256":z["relation_sha256"]} for z in selected],
      "candidate_primes_tested":len(candidates),"presentation_degenerate_skips":degeneracies,
      "attempts":attempts
    }

records=[]
for name in ns["FIBERS"]:
    for d in (1,2):
        rec=build_case(name,d); records.append(rec)
        print(f"{rec['status']} {name} d={d} m={rec.get('m')} primes={rec.get('selected_primes')} survivors={rec.get('intersection_survivors')}/{rec.get('quotient_total')}")

eliminated=[[r["q"],r["d"]] for r in records if r["status"]=="EMPTY_GLOBAL_OBSTRUCTION"]
payload={
  "schema":"STAGE34_02_D2_FIBER_TAILORED_FIXED_QUOTIENT_MW_SIEVE_V1",
  "status":"PASS_EXACT_TAILORED_FIXED_QUOTIENT_SIEVE",
  "prime_search_interval":[131,401],
  "quotient_policy":"Prefer m=4 when at least three usable nondegenerate primes exist; otherwise m=2. Every relevant reduced free-generator order must be divisible by m.",
  "selection_policy":"Among at most twelve cheapest supported primes, compute exact projected matching-x relations and greedily intersect up to six primes while the survivor set strictly shrinks.",
  "cases":records,
  "globally_eliminated_cases":eliminated,
  "globally_eliminated_count":len(eliminated),
  "firewalls":{
    "empty_fixed_quotient_intersection_is_valid_global_obstruction":True,
    "nonempty_fixed_quotient_intersection_is_rational_point":False,
    "finite_sieve_closes_receiver_only_if_all_nontorsion_cases_eliminated_or_exactly_discharged":False,
    "receiver_closed":False,
    "R29_EXT_CHANG_C_closed":False
  }
}
(ROOT/"d2-fiber-product-mw-tailored.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"eliminated":len(eliminated),"cases":len(records)},sort_keys=True))
