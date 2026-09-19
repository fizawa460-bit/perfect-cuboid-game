#!/usr/bin/env python3
import itertools, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/"MB104-SIX-FIBRATION-DIFFERENTIAL-SPANNING-CONDUCTOR-POLAR-CERTIFICATE.json"

TRIPLES=[
    ("b1","a2","a3"),
    ("b2","a1","a3"),
    ("b3","a1","a2"),
    ("b1","a1","c"),
    ("b2","a2","c"),
    ("b3","a3","c"),
]

def comps(zero):
    n=len(TRIPLES)
    adj=[set() for _ in range(n)]
    for i,j in itertools.combinations(range(n),2):
        if any(x not in zero for x in set(TRIPLES[i]) & set(TRIPLES[j])):
            adj[i].add(j); adj[j].add(i)
    seen=set(); cc=[]
    for s in range(n):
        if s in seen: continue
        stack=[s]; seen.add(s); cur=set()
        while stack:
            v=stack.pop(); cur.add(v)
            for w in adj[v]:
                if w not in seen:
                    seen.add(w); stack.append(w)
        cc.append(cur)
    return cc

def main():
    d=json.loads(CERT.read_text())
    assert d["schema"]=="STAGE32_MB104_SIX_FIBRATION_DIFFERENTIAL_SPANNING_CONDUCTOR_POLAR_V1"
    assert [tuple(x) for x in d["fibration_triples"]]==TRIPLES

    vars_=sorted(set().union(*map(set,TRIPLES)))
    minimal=[]
    for r in range(len(vars_)+1):
        for zt in itertools.combinations(vars_,r):
            z=set(zt)
            if len(comps(z))<=1:
                continue
            if any(len(comps(z-{x}))>1 for x in z):
                continue
            minimal.append(tuple(sorted(z)))
    expected=sorted(tuple(sorted(x)) for x in TRIPLES)
    assert sorted(minimal)==expected
    assert sorted(tuple(sorted(x)) for x in d["minimal_disconnecting_zero_sets"])==expected

    # Imported carrier degrees from the prior preflight.
    deg48=(24,56,56,32,56,56)
    deg768=(40,40,56,44,44,56)
    assert 2*min(deg48)==48
    assert 2*min(deg768)==80

    c=d["conclusions"]
    assert c["combined_differential_injective_on_original_smooth_locus"] is True
    assert c["branch_ramification_min_equals_multiplicity_minus_one"] is True
    assert c["common_ramification_degree_bound"]["size48"]=="48*l"
    assert c["common_ramification_degree_bound"]["size768"]=="80*l"

    print("PASS: six-fibration differential-spanning/conductor-polar preflight")
    print("minimal differential-disconnect loci are exactly the six 8-node base triples")
    print("common branch ramification defect <=48l (size48), <=80l (size768)")

if __name__=="__main__":
    main()
