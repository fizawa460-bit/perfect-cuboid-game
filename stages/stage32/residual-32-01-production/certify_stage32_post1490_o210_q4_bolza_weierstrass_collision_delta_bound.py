#!/usr/bin/env python3
import argparse, hashlib, json
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
DEFAULT=Path("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-weierstrass-collision-delta-bound.json")

def req(c,m):
    if not c: raise AssertionError(m)
def load(p):
    with (ROOT/p).open("r",encoding="utf-8") as f: return json.load(f)
def blob(p):
    b=(ROOT/p).read_bytes(); return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def lock(x):
    p=Path(x["path"]); req(blob(p)==x["blob_sha1"],f"blob {p}")
    o=load(p); req(o["canonical_sha256_without_this_field"]==x["canonical_sha256"],f"stored canonical {p}"); req(canon(o)==x["canonical_sha256"],f"canonical {p}"); return o
def choose2(n): return n*(n-1)//2
def d4_coeff(N):
    s=[0]*(N+1)
    for d in range(1,N+1,2):
        for k in range(d,N+1,d): s[k]+=d
    return [1]+[24*s[i] for i in range(1,N+1)]
def d4d4_prefix(N):
    c=d4_coeff(N); pref=[]; z=0
    for x in c: z+=x; pref.append(z)
    return sum(c[i]*pref[N-i] for i in range(N+1))
def dp_min(pair_mc,total_y):
    dp={0:(0,[])}
    for key,M,cap in pair_mc:
        nd={}
        for used,(cost,path) in dp.items():
            for y in range(cap+1):
                n=M-2*y; u=used+y; v=cost+choose2(n)
                if u not in nd or v<nd[u][0]: nd[u]=(v,path+[(key,y,n,choose2(n))])
        dp=nd
    return dp[total_y]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--check",type=Path,default=DEFAULT); ns=ap.parse_args(); o=load(ns.check)
    req(o["schema"]=="STAGE32_POST1490_O210_Q4_BOLZA_WEIERSTRASS_COLLISION_DELTA_BOUND_V1","schema")
    req(o["fixed_target"]=={"row_id":"g1-d186","d":186,"e":266,"genus":1,"z":[-15,62,-44,26,32],"O":210,"qprime":4},"target")
    d4=lock(o["source_locks"]["d4d4_trace_reduction"]); bid=lock(o["source_locks"]["bidegree_boundary"]); inc=lock(o["source_locks"]["marked_exceptional_incidence"]); wit=lock(o["source_locks"]["v6_witness"]); v4=lock(o["source_locks"]["v4_cusp_quotient"])
    note=o["source_locks"]["source_note"]; req(blob(Path(note["path"]))==note["blob_sha1"],"source note")
    req(d4["pair_map_birationality"]["pair_map_birational"] is True,"birational source"); req(d4["correspondence_trace"]["exact_identity"]=="Q(T)=8586-delta","trace source")
    prof=bid["O210_extremal_profile"]["forced_contact_histogram"]; req(prof["m1_odd"]==210 and prof["m2_even"]==28 and prof["all_other_contacts"]==0,"histogram")
    req(v4["quotient_geometry"]["six_quotient_cusps_are_Weierstrass_points"] is True,"Weierstrass source")
    req(inc["checks"]["distinct_realized_boundary_pair_count"]==12 and inc["checks"]["each_realized_boundary_pair_node_count"]==4,"pair incidence")
    pairings=wit["witness"]["all140_pairings"]; ph=hashlib.sha256(json.dumps(pairings,separators=(",",":")).encode()).hexdigest()
    req(ph==wit["witness"]["all140_pairings_sha256"]==o["source_locks"]["v6_witness"]["all140_pairings_sha256"],"pairing hash"); req(len(pairings)==140,"140 pairings")
    exc={93+i:m for i,m in enumerate(pairings[-48:])}; req(sum(exc.values())==266,"exceptional mass")
    by=defaultdict(list)
    for row in inc["rows"]:
        lab=row["exceptional_label"]; key=(row["first_factor_boundary_label"],row["second_factor_boundary_label"]); by[key].append((lab,exc[lab]))
    req(len(by)==12 and all(len(v)==4 for v in by.values()),"12x4 grouping")
    order=[tuple(map(int,s.split(":"))) for s in o["weierstrass_support"]["pair_order"]]; pair_mc=[]; rebuilt=[]
    for key in order:
        vals=by[key]; M=sum(m for _,m in vals); cap=sum(m//2 for _,m in vals); pair_mc.append((key,M,cap)); rebuilt.append({"first_factor_boundary_label":key[0],"second_factor_boundary_label":key[1],"exceptional_mass":M,"m2_capacity":cap})
    req(rebuilt==o["weierstrass_support"]["pair_mass_capacity"],"pair mass/cap reconstruction"); req(sum(x[1] for x in pair_mc)==266,"pair mass total")
    best,path=dp_min(pair_mc,28); opt=o["collision_optimization"]; req(best==opt["exact_minimum_delta"]==1924,"delta DP")
    req(sum(y for _,y,_,_ in path)==28 and sum(n for _,_,n,_ in path)==210,"DP totals")
    stored=[(x["pair"],x["y_m2"],x["n_m1"],x["delta_pair_lower_bound"]) for x in opt["one_minimizer"]]; got=[(f"{k[0]}:{k[1]}",y,n,c) for k,y,n,c in path]
    req(got==stored,"stored minimizer"); req(sum(c for *_,c in path)==1924,"minimizer cost"); req(opt["nodewise_pair_interval_complete"] is True,"interval completeness")
    tc=o["trace_consequence"]; req(8586-best==tc["new_trace_upper_bound"]==6662,"trace bound"); req(tc["half_trace_upper_bound"]==3331,"half trace")
    req(d4d4_prefix(3331)==tc["d4d4_integral_count_Q_le_6662"]==1999360132285041,"D4+D4 residual count"); req(tc["residual_materialization_safe"] is False and tc["O210_excluded"] is False,"nonexclusion/materialization")
    dec=o["decision"]; req(dec["delta_lower_bound"]==1924 and dec["trace_upper_bound"]==6662,"decision numbers"); req(dec["O210_excluded"] is False and dec["next_exact_leaf"]=="O210_Q4_BOLZA_DECK_TRANSLATE_INTERSECTION_GEOMETRY","decision")
    req(canon(o)==o["canonical_sha256_without_this_field"],"canonical")
    print(json.dumps({"ok":True,"canonical_sha256":canon(o),"delta_lower_bound":1924,"Q_upper_bound":6662,"D4D4_count":tc["d4d4_integral_count_Q_le_6662"],"O210_excluded":False,"next_exact_leaf":dec["next_exact_leaf"]},sort_keys=True))
if __name__=="__main__": main()
