#!/usr/bin/env python3
from __future__ import annotations
import collections, hashlib, itertools, json, math, pathlib, runpy
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "d2-stageA2-triple-quotient-model-probe.json"
TRIPLES = [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]
NAMES = ["U","V","A","B"]

# Reuse the already proof-checked Stage34 branch reconstruction and the exact
# 24-of-76 rank-one sieve solely to recover the authoritative residual 52 IDs.
ns = runpy.run_path(str(ROOT / "run_d2_stageA2_rank1_mw_congruence_sieve.py"))
sel = ns["sel"]
first = ns["payload"]
residual_ids = {x["branch_id"] for x in first["unresolved"]}
assert len(residual_ids) == 52


def factor(n: int):
    n = abs(n); out = []; p = 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0: n //= p
        p = 3 if p == 2 else p + 2
    if n > 1: out.append(n)
    return out


def sf(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n); out = 1
    for p in factor(n):
        e = 0
        while n % p == 0:
            n //= p; e ^= 1
        if e: out *= p
    return sign*out


def forms(q: str):
    a,b = map(int,q.split('/'))
    # descending affine t coefficients; homogeneous degree two is implicit.
    return [[1,0,-1],[0,2,0],[a,2*b,-a],[b,2*a,-b]]


def mul_desc(p, q):
    out = [0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): out[i+j] += x*y
    return out


def square_part(n: int) -> int:
    n = abs(n)
    if n == 0: return 1
    out = 1; p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p; e += 1
        out *= p**(e//2)
        p = 3 if p == 2 else p+2
    return out


def canonical_coeffs(c):
    g = 0
    for x in c: g = math.gcd(g, abs(int(x)))
    sq = square_part(g)
    d = sq*sq
    return tuple(int(x)//d for x in c), d


def root_labels(q: str, idx: int):
    # Projective roots as reduced rational pairs (T:S), including infinity.
    a,b = map(int,q.split('/')); h = math.isqrt(a*a+b*b); assert h*h == a*a+b*b
    if idx == 0: vals = [(1,1),(-1,1)]
    elif idx == 1: vals = [(0,1),(1,0)]
    elif idx == 2: vals = [(-b+h,a),(-b-h,a)]
    elif idx == 3: vals = [(-a+h,b),(-a-h,b)]
    else: raise AssertionError(idx)
    out=[]
    for T,S in vals:
        if S == 0: out.append((1,0)); continue
        g=math.gcd(abs(T),abs(S)); T//=g; S//=g
        if S < 0: T=-T; S=-S
        out.append((T,S))
    return out


def hid(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()[:20]

models = {}
branches = []
for br in sel["branches"]:
    if br["branch_id"] not in residual_ids: continue
    q = br["q"]; delta = tuple(map(int,br["delta"])); fs = forms(q)
    ents=[]
    for tri in TRIPLES:
        s = sf(delta[tri[0]]*delta[tri[1]]*delta[tri[2]])
        poly = [1]
        roots=[]
        for i in tri:
            poly = mul_desc(poly, fs[i]); roots += root_labels(q,i)
        poly = [s*x for x in poly]
        assert len(poly) == 7
        distinct = len(set(roots))
        assert distinct == 6, (q,tri,roots)
        canon, removed_sq = canonical_coeffs(poly)
        # Canonical key is exact up to y -> sqrt(removed_sq)*y only; no Mobius
        # or abstract genus-two isomorphism compression is claimed here.
        key = (canon,)
        if key not in models:
            models[key] = {
                "model_id": None,
                "coefficients_desc_t_degree6": list(canon),
                "affine_degree": 6-next(i for i,x in enumerate(canon) if x != 0),
                "projective_branch_points": 6,
                "genus": 2,
                "associations": []
            }
        assoc={"q":q,"branch_id":br["branch_id"],"triple":"*".join(NAMES[i] for i in tri),"squareclass":s,"removed_common_square":removed_sq}
        models[key]["associations"].append(assoc)
        ents.append({"triple":assoc["triple"],"squareclass":s,"model_key":hid(list(canon))})
    branches.append({"q":q,"branch_id":br["branch_id"],"delta":list(delta),"triple_quotients":ents})

assert len(branches)==52 and sum(len(x["triple_quotients"]) for x in branches)==208
ordered=sorted(models.items(), key=lambda kv: kv[0])
key_to_id={k:i+1 for i,(k,_) in enumerate(ordered)}
for k,m in ordered:
    m["model_id"]=key_to_id[k]
    m["association_count"]=len(m["associations"])
    m["q_histogram"]=dict(sorted(collections.Counter(x["q"] for x in m["associations"]).items()))
    m["triple_histogram"]=dict(sorted(collections.Counter(x["triple"] for x in m["associations"]).items()))
for br in branches:
    for e in br["triple_quotients"]:
        # resolve by the stable short hash
        matches=[m["model_id"] for _,m in ordered if hid(m["coefficients_desc_t_degree6"])==e["model_key"]]
        assert len(matches)==1; e["model_id"]=matches[0]; del e["model_key"]

# Exact-model set-cover diagnostics: how many exact sextics suffice to give every
# residual branch at least one genus-two quotient target? Greedy only; no optimality claim.
uncovered={x["branch_id"] for x in branches}; greedy=[]
while uncovered:
    best=None
    for _,m in ordered:
        cov={a["branch_id"] for a in m["associations"]}&uncovered
        score=(len(cov), -m["model_id"])
        if cov and (best is None or score>best[0]): best=(score,m,cov)
    assert best is not None
    _,m,cov=best; greedy.append({"model_id":m["model_id"],"new_branches":len(cov)}); uncovered-=cov

payload={
 "schema":"STAGE34_02_D2_STAGEA2_TRIPLE_QUOTIENT_MODEL_PROBE_V1",
 "status":"DIAGNOSTIC_NO_CREDIT",
 "input_residual_branches":52,
 "triple_quotients_per_branch":4,
 "total_triple_quotient_conditions":208,
 "distinct_exact_sextic_models":len(models),
 "genus":2,
 "all_projective_branch_points_distinct":True,
 "model_equivalence":"Only identical affine coefficient tuples after removing a common positive rational square factor are merged. No PGL2/Mobius or abstract genus-two isomorphism identification is claimed.",
 "greedy_exact_model_cover":greedy,
 "greedy_exact_model_cover_count":len(greedy),
 "models":[m for _,m in ordered],
 "branches":branches,
 "credit":"Diagnostic target compression only. A parent rational point necessarily maps to each listed triple quotient, but neither existence nor nonexistence of quotient rational points is inferred.",
 "firewalls":{"genus2_quotient_has_Q_point":False,"low_model_count_is_closure":False,"greedy_cover_is_optimal":False,"triple_quotient_closes_parent":False,"remaining_52_closed":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("TRIPLE_QUOTIENT_MODEL_PROBE="+json.dumps({"status":payload["status"],"branches":52,"conditions":208,"distinct_exact_models":len(models),"greedy_cover_count":len(greedy),"greedy_cover":greedy},sort_keys=True))
