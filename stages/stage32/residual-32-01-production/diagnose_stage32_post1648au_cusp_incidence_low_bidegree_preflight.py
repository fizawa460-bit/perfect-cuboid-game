#!/usr/bin/env python3
from __future__ import annotations

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
    unseen=set(adj); out=[]
    while unseen:
        start=min(unseen); q=deque([start]); seen={start}; es=set()
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
            "vertex_count":len(seen),"edge_count":len(rows),
            "vertices":[f"{k}{i}" for k,i in sorted(seen)],
            "edges":rows,"weight_sum":sum(r[2] for r in rows),
        })
    return sorted(out,key=lambda x:(x["vertex_count"],x["vertices"]))


def max_weight_matching(edges: list[tuple[int,int,int]]) -> dict:
    # Only for the (1,1) simple-capacity witness; exhaustive 2^12 check.
    best_weight=-1; best_edges=[]; n=len(edges)
    for mask in range(1<<n):
        A=set(); B=set(); w=0; chosen=[]; ok=True
        for i,(a,b,m) in enumerate(edges):
            if (mask>>i)&1:
                if a in A or b in B:
                    ok=False; break
                A.add(a); B.add(b); w+=m; chosen.append([a,b,m])
        if ok and w>best_weight:
            best_weight=w; best_edges=chosen
    return {"max_weight":best_weight,"edges":best_edges,"edge_count":len(best_edges)}


def main() -> None:
    at=json.loads(AT.read_text())
    assert at["canonical_sha256_without_this_field"]=="bc11998f941f4791ac0a394c85725368659262a55ec8206288aefa5ee2241b86"

    proc=subprocess.run([sys.executable,"-B",str(AQ_DIAG)],cwd=ROOT,check=True,capture_output=True,text=True)
    aq=json.loads(proc.stdout)
    assert aq["mode"]=="SCRATCH_POST1648AQ_RESIDUAL_G_CUSP_MULTIPLICITY_GRID"
    edges=sorted((int(r["dir81_boundary_label"]),int(r["dir105_boundary_label"]),int(r["image_multiplicity"])) for r in aq["target_cusp_grid"]["rows"])
    assert len(edges)==12 and sum(m for _,_,m in edges)==266

    A=sorted({a for a,_,_ in edges}); B=sorted({b for _,b,_ in edges})
    assert len(A)==len(B)==6
    degA=Counter(a for a,_,_ in edges); degB=Counter(b for _,b,_ in edges)
    assert set(degA.values())=={2} and set(degB.values())=={2}
    comps=components(edges)
    assert len(comps)==3 and all(c["vertex_count"]==4 and c["edge_count"]==4 for c in comps)

    row_sums={str(a):sum(m for aa,_,m in edges if aa==a) for a in A}
    col_sums={str(b):sum(m for _,bb,m in edges if bb==b) for b in B}
    assert max(row_sums.values())<=81 and max(col_sums.values())<=105

    # For any curve L = a F81 + b F105 with no special-fibre component, let
    # k_e = mult_{p_e}(L) at the 12 cusp points. Intersecting L with each
    # special fibre gives the universal capacity constraints
    #   sum_{e incident to A_i} k_e <= b,
    #   sum_{e incident to B_j} k_e <= a.
    # Therefore the weighted forced intersection with D is bounded in two ways:
    #   sum m_e k_e <= b * sum_A max_edge_weight(A) = 168 b,
    #   sum m_e k_e <= a * sum_B max_edge_weight(B) = 173 a.
    # If both exceeded D.L=81a+105b, we would simultaneously need
    #   b/a > 81/63 = 9/7
    # and
    #   b/a < 92/105,
    # impossible. Hence cusp multiplicities alone can never force D as a
    # component of L for any positive bidegree, regardless of actual cusp
    # coordinates or higher multiplicity of L at those cusps.
    row_max={str(a):max(m for aa,_,m in edges if aa==a) for a in A}
    col_max={str(b):max(m for _,bb,m in edges if bb==b) for b in B}
    row_max_sum=sum(row_max.values()); col_max_sum=sum(col_max.values())
    assert (row_max_sum,col_max_sum)==(168,173)
    assert 9/7 > 92/105

    matching=max_weight_matching(edges)
    assert matching["max_weight"]==168
    assert matching["max_weight"]<186

    out={
        "mode":"SCRATCH_POST1648AU_CUSP_INCIDENCE_LOW_BIDEGREE_PREFLIGHT_V2",
        "parent":{"AT_canonical":at["canonical_sha256_without_this_field"]},
        "cusp_incidence":{
            "dir81_labels":A,"dir105_labels":B,
            "edges":[{"dir81":a,"dir105":b,"m":m} for a,b,m in edges],
            "all_vertex_degrees":True,"common_vertex_degree":2,
            "components":comps,"component_type":"3_disjoint_K2_2",
            "total_weight":266,"dir81_weight_sums":row_sums,"dir105_weight_sums":col_sums,
        },
        "universal_bezout_capacity":{
            "row_max_weights":row_max,"row_max_sum":row_max_sum,
            "column_max_weights":col_max,"column_max_sum":col_max_sum,
            "for_L_class":"a*F81+b*F105",
            "forced_cusp_intersection_upper_bounds":["168*b","173*a"],
            "D_dot_L":"81*a+105*b",
            "contradictory_ratio_requirements_if_obstruction":["b/a>9/7","b/a<92/105"],
            "all_positive_bidegrees_excluded_from_cusp_weight_bezout_obstruction":True,
            "special_fibre_components_also_safe":True,
            "special_fibre_reason":"each exact fibre cusp-weight sum is <= its D intersection degree; remove such components additively",
        },
        "one_one_check":{
            "D_dot_1_1":186,
            "max_weight_matching":matching["max_weight"],
            "margin":matching["max_weight"]-186,
            "maximizing_edges":matching["edges"],
        },
        "decision":{
            "v6_carrier_excluded":False,
            "bounded_wall":"THE_EXACT_12_CUSP_MULTIPLICITY_DATA_CANNOT_FORCE_ANY_BEZOUT_COMPONENT_FOR_ANY_BIDEGREE_CURVE_USING_ONLY_CUSP_MULTIPLICITY_LOWER_BOUNDS",
            "next_missing_input":"MEMBER_LEVEL_TANGENT_OR_HIGHER_JET_RELATIONS, OR A DIFFERENT GLOBAL INEQUALITY NOT REDUCIBLE_TO CUSP MULTIPLICITY BEZOUT",
        },
        "firewalls":{
            "scratch_only":True,"shared_MAIN_STATE_unchanged":True,"shared_authority_unchanged":True,
            "Q602_excluded":False,"O210_excluded":False,"O212_plus_advance_allowed":False,
        },
    }
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
