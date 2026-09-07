#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import subprocess
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
AQ_DIAG = HERE / "diagnose_stage32_post1648aq_residual_g_action_preflight.py"
AT = HERE / "post1648at-intermediate-quotient-blowup-conductor.json"


def components(edges: list[tuple[int,int,int]]) -> list[dict]:
    adj: dict[tuple[str,int], list[tuple[str,int]]] = defaultdict(list)
    weight = {}
    for a,b,m in edges:
        u=("A",a); v=("B",b)
        adj[u].append(v); adj[v].append(u); weight[(u,v)]=weight[(v,u)]=m
    unseen=set(adj)
    out=[]
    while unseen:
        start=min(unseen)
        q=deque([start]); seen={start}; es=set()
        while q:
            u=q.popleft()
            for v in adj[u]:
                es.add(tuple(sorted([u,v])))
                if v not in seen:
                    seen.add(v); q.append(v)
        unseen-=seen
        rows=[]
        for uv in sorted(es):
            u,v=uv
            if u[0]=="B": u,v=v,u
            rows.append([u[1],v[1],weight[(u,v)]])
        out.append({
            "vertex_count":len(seen),
            "edge_count":len(rows),
            "vertices":[f"{k}{i}" for k,i in sorted(seen)],
            "edges":rows,
            "weight_sum":sum(r[2] for r in rows),
        })
    return sorted(out,key=lambda x:(x["vertex_count"],x["vertices"]))


def max_weight_bmatching(edges: list[tuple[int,int,int]], capA: int, capB: int) -> dict:
    best_weight=-1; best_edges=[]
    n=len(edges)
    for mask in range(1<<n):
        degA=Counter(); degB=Counter(); w=0; chosen=[]; ok=True
        for i,(a,b,m) in enumerate(edges):
            if (mask>>i)&1:
                degA[a]+=1; degB[b]+=1
                if degA[a]>capA or degB[b]>capB:
                    ok=False; break
                w+=m; chosen.append([a,b,m])
        if ok and w>best_weight:
            best_weight=w; best_edges=chosen
    return {"max_weight":best_weight,"edges":best_edges,"edge_count":len(best_edges)}


def main() -> None:
    at=json.loads(AT.read_text())
    assert at["canonical_sha256_without_this_field"]=="bc11998f941f4791ac0a394c85725368659262a55ec8206288aefa5ee2241b86"

    proc=subprocess.run([sys.executable,"-B",str(AQ_DIAG)],cwd=ROOT,check=True,capture_output=True,text=True)
    aq=json.loads(proc.stdout)
    assert aq["mode"]=="SCRATCH_POST1648AQ_RESIDUAL_G_CUSP_MULTIPLICITY_GRID"
    rows=aq["target_cusp_grid"]["rows"]
    edges=[]
    for r in rows:
        edges.append((int(r["dir81_boundary_label"]),int(r["dir105_boundary_label"]),int(r["image_multiplicity"])))
    edges=sorted(edges)
    assert len(edges)==12
    assert sum(m for _,_,m in edges)==266

    A=sorted({a for a,_,_ in edges}); B=sorted({b for _,b,_ in edges})
    assert len(A)==len(B)==6
    degA=Counter(a for a,_,_ in edges); degB=Counter(b for _,b,_ in edges)
    assert set(degA.values())=={2} and set(degB.values())=={2}

    comps=components(edges)
    assert len(comps)==3 and all(c["vertex_count"]==4 and c["edge_count"]==4 for c in comps)

    # Any irreducible divisor L=a*F81+b*F105 not containing a special fibre
    # can pass simply through a cusp subset whose incidence degrees are <=b on
    # each F81 vertex and <=a on each F105 vertex. Its intersection with D is
    # 81*a+105*b. For pure cusp-multiplicity Bezout, only (1,1) can possibly
    # beat the budget because total cusp weight is 266, while (2,1) costs 267
    # and (1,2) costs 291; larger positive bidegrees cost more.
    tests=[]
    for a,b in [(1,1),(2,1),(1,2),(2,2)]:
        bm=max_weight_bmatching(edges,capA=b,capB=a)
        budget=81*a+105*b
        tests.append({
            "class":f"{a}*F81+{b}*F105",
            "capacity_on_each_F81":b,
            "capacity_on_each_F105":a,
            "D_intersection_budget":budget,
            "max_cusp_weight_lower_bound":bm["max_weight"],
            "margin_weight_minus_budget":bm["max_weight"]-budget,
            "maximizing_edges":bm["edges"],
        })

    t11=tests[0]
    pure_f81={str(a):sum(m for aa,_,m in edges if aa==a) for a in A}
    pure_f105={str(b):sum(m for _,bb,m in edges if bb==b) for b in B}
    assert max(pure_f81.values())<=81
    assert max(pure_f105.values())<=105

    no_positive_low_bidegree_cusp_bezout=(
        t11["max_cusp_weight_lower_bound"]<=t11["D_intersection_budget"]
        and 266<267 and 266<291
    )

    out={
        "mode":"SCRATCH_POST1648AU_CUSP_INCIDENCE_LOW_BIDEGREE_PREFLIGHT",
        "parent":{"AT_canonical":at["canonical_sha256_without_this_field"]},
        "cusp_incidence":{
            "dir81_labels":A,
            "dir105_labels":B,
            "edges":[{"dir81":a,"dir105":b,"m":m} for a,b,m in edges],
            "all_vertex_degrees":True,
            "common_vertex_degree":2,
            "components":comps,
            "component_type":"3_disjoint_K2_2",
            "total_weight":266,
            "dir81_weight_sums":pure_f81,
            "dir105_weight_sums":pure_f105,
        },
        "low_bidegree_bezout":{
            "tests":tests,
            "only_positive_bidegree_case_with_budget_below_total_weight":"(1,1)",
            "max_1_1_weight":t11["max_cusp_weight_lower_bound"],
            "D_intersection_1_1":t11["D_intersection_budget"],
            "max_1_1_margin":t11["margin_weight_minus_budget"],
            "no_obstruction_from_cusp_multiplicity_lower_bounds_alone":no_positive_low_bidegree_cusp_bezout,
            "scope":"bounded to divisors not containing special fibres and using only forced local intersection >= multiplicity at the 12 cusps",
        },
        "decision":{
            "v6_carrier_excluded":False,
            "bounded_wall":"EXACT_12_CUSP_INCIDENCE_AND_MULTIPLICITIES_DO_NOT_FORCE_A_LOW_BIDEGREE_BEZOUT_COMPONENT_USING_CUSP_MULTIPLICITY_LOWER_BOUNDS_ALONE",
            "next_missing_input":"ACTUAL_CUSP_COORDINATES_AND_SPECIAL_LOW_BIDEGREE_RELATIONS_OR_MEMBER_LEVEL_JETS; COMBINATORIAL_INCIDENCE_ALONE_IS_INSUFFICIENT",
        },
        "firewalls":{
            "scratch_only":True,
            "shared_MAIN_STATE_unchanged":True,
            "shared_authority_unchanged":True,
            "Q602_excluded":False,
            "O210_excluded":False,
            "O212_plus_advance_allowed":False,
        },
    }
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
