#!/usr/bin/env python3
from __future__ import annotations

import base64, bz2, csv, io, json, math
from collections import Counter, defaultdict, deque
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SOURCE = ROOT / 'stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64'


def load_rows():
    encoded=''.join(SOURCE.read_text(encoding='ascii').split())
    raw=bz2.decompress(base64.b64decode(encoded)).decode('utf-8')
    rows=[tuple(int(r[k]) for k in ('a','b','c','d','mask')) for r in csv.DictReader(io.StringIO(raw))]
    assert len(rows)==3495 and len(set(rows))==3495
    return rows


def label(mask):
    return {0b011:'a',0b101:'b',0b110:'c'}[mask]


def face_mask(a,b,c):
    mask=0; ds=[]
    for i,v in enumerate((a*a+b*b,a*a+c*c,b*b+c*c)):
        r=isqrt(v)
        if r*r==v: mask |= 1<<i; ds.append(r)
        else: ds.append(0)
    return mask,tuple(ds)


def primitive_face(shared,other,hyp):
    g=gcd(shared,other)
    return shared//g, other//g, hyp//g


def object_edge(rec):
    a,b,c,d,mask=rec
    _,(dab,dac,dbc)=face_mask(a,b,c)
    if mask==0b011:
        u=primitive_face(a,b,dab); v=primitive_face(a,c,dac)
    elif mask==0b101:
        u=primitive_face(b,a,dab); v=primitive_face(b,c,dbc)
    elif mask==0b110:
        u=primitive_face(c,a,dac); v=primitive_face(c,b,dbc)
    else: raise ArithmeticError(mask)
    return tuple(sorted((u,v)))


def ratios(counts):
    n=sum(counts.values())
    return {q:counts[q]/n for q in 'abc'} if n else {q:0.0 for q in 'abc'}


def l2shift(lo,hi):
    return math.sqrt(sum((hi[q]-lo[q])**2 for q in 'abc'))


def shell_ratio(rows,lo,hi,weights=None):
    c={q:0.0 for q in 'abc'}
    for i,r in enumerate(rows):
        if lo < r[3] <= hi:
            c[label(r[4])] += 1.0 if weights is None else weights[i]
    return ratios(c)


def main():
    rows=load_rows()
    global_counts=Counter(label(r[4]) for r in rows)

    # Same-space-diagonal multiplicity.
    by_d=defaultdict(list)
    for i,r in enumerate(rows): by_d[r[3]].append(i)
    mult_hist=Counter(len(v) for v in by_d.values())
    object_mult_hist=Counter()
    for ids in by_d.values(): object_mult_hist[len(ids)] += len(ids)
    max_mult=max(mult_hist)
    repeated_d=sum(1 for ids in by_d.values() if len(ids)>1)
    repeated_objects=sum(len(ids) for ids in by_d.values() if len(ids)>1)

    equal_d_weights=[0.0]*len(rows)
    for ids in by_d.values():
        w=1.0/len(ids)
        for i in ids: equal_d_weights[i]=w
    equal_d_counts={q:0.0 for q in 'abc'}
    for i,r in enumerate(rows): equal_d_counts[label(r[4])] += equal_d_weights[i]

    # Primitive-face graph connected components: each exactly-two object is one graph edge.
    edges=[]; adj=defaultdict(set); edge_to_rows=defaultdict(list)
    for i,r in enumerate(rows):
        e=object_edge(r); edges.append(e); edge_to_rows[e].append(i)
        u,v=e; adj[u].add(v); adj[v].add(u)
    # exact alpha population has one row per graph edge, but keep audit explicit
    duplicate_graph_edges=sum(1 for ids in edge_to_rows.values() if len(ids)>1)
    vertices=set(adj)
    comp_of={}; comps=[]
    for s in vertices:
        if s in comp_of: continue
        cid=len(comps); q=deque([s]); comp_of[s]=cid; vs=[]
        while q:
            u=q.popleft(); vs.append(u)
            for v in adj[u]:
                if v not in comp_of: comp_of[v]=cid; q.append(v)
        comps.append(vs)
    comp_rows=defaultdict(list)
    for i,(u,v) in enumerate(edges):
        cid=comp_of[u]; assert comp_of[v]==cid; comp_rows[cid].append(i)
    comp_sizes=sorted((len(ids),cid) for cid,ids in comp_rows.items())
    comp_edge_hist=Counter(len(ids) for ids in comp_rows.values())
    largest=sorted(comp_rows.items(), key=lambda kv:len(kv[1]), reverse=True)[:10]

    equal_comp_weights=[0.0]*len(rows)
    for ids in comp_rows.values():
        w=1.0/len(ids)
        for i in ids: equal_comp_weights[i]=w
    equal_comp_counts={q:0.0 for q in 'abc'}
    for i,r in enumerate(rows): equal_comp_counts[label(r[4])] += equal_comp_weights[i]

    def comp_summary(cid,ids):
        cc=Counter(label(rows[i][4]) for i in ids)
        ds=[rows[i][3] for i in ids]
        return {'component_id':cid,'edges':len(ids),'vertices':len(comps[cid]),'counts':{q:cc[q] for q in 'abc'},'ratios':ratios(cc),'d_min':min(ds),'d_max':max(ds)}

    # Late-shell shift under de-clustering.
    lo=(300_000_000,400_000_000); hi=(400_000_000,500_000_000)
    raw_lo=shell_ratio(rows,*lo); raw_hi=shell_ratio(rows,*hi)
    d_lo=shell_ratio(rows,*lo,weights=equal_d_weights); d_hi=shell_ratio(rows,*hi,weights=equal_d_weights)
    c_lo=shell_ratio(rows,*lo,weights=equal_comp_weights); c_hi=shell_ratio(rows,*hi,weights=equal_comp_weights)

    # Remove largest connected components progressively, to see whether a few families drive the shell shift.
    removal=[]
    banned=set()
    for rank,(cid,ids) in enumerate(largest[:5],1):
        banned.update(ids)
        kept=[r for i,r in enumerate(rows) if i not in banned]
        rlo=shell_ratio(kept,*lo); rhi=shell_ratio(kept,*hi)
        removal.append({'removed_top_components':rank,'removed_objects':len(banned),'late_shift_l2':l2shift(rlo,rhi),'lo':rlo,'hi':rhi})

    # Direction distribution by d multiplicity class.
    mult_classes={'1':Counter(),'2':Counter(),'3+':Counter()}
    for d,ids in by_d.items():
        k='1' if len(ids)==1 else ('2' if len(ids)==2 else '3+')
        for i in ids: mult_classes[k][label(rows[i][4])] += 1

    report={
        'stage':'14-num-alpha11-diag5',
        'classification':'SAME_DIAGONAL_AND_PRIMITIVE_FACE_GRAPH_CLUSTER_DEPENDENCE_DIAGNOSTIC',
        'source_rows':len(rows),
        'global_direction_counts':{q:global_counts[q] for q in 'abc'},
        'same_diagonal':{
            'distinct_d':len(by_d),'repeated_d':repeated_d,'objects_on_repeated_d':repeated_objects,
            'max_objects_per_d':max_mult,
            'd_multiplicity_histogram':dict(sorted(mult_hist.items())),
            'object_weighted_multiplicity_histogram':dict(sorted(object_mult_hist.items())),
            'direction_by_multiplicity':{k:{'counts':{q:v[q] for q in 'abc'},'ratios':ratios(v)} for k,v in mult_classes.items()},
            'raw_global_ratios':ratios(global_counts),
            'equal_weight_per_d_ratios':ratios(equal_d_counts),
        },
        'primitive_face_graph_clusters':{
            'vertices':len(vertices),'unique_edges':len(edge_to_rows),'duplicate_graph_edges':duplicate_graph_edges,
            'connected_components':len(comps),'max_component_edges':max(comp_edge_hist),
            'component_edge_size_histogram':dict(sorted(comp_edge_hist.items())),
            'largest_components':[comp_summary(cid,ids) for cid,ids in largest],
            'equal_weight_per_component_ratios':ratios(equal_comp_counts),
        },
        'late_shell_300_400_vs_400_500':{
            'raw':{'lo':raw_lo,'hi':raw_hi,'shift_l2':l2shift(raw_lo,raw_hi)},
            'equal_weight_per_d':{'lo':d_lo,'hi':d_hi,'shift_l2':l2shift(d_lo,d_hi)},
            'equal_weight_per_component':{'lo':c_lo,'hi':c_hi,'shift_l2':l2shift(c_lo,c_hi)},
            'largest_component_removal':removal,
        },
        'interpretation_boundary':{
            'finite_exact_diagnostic_only':True,
            'iid_object_claim':False,
            'graph_component_equals_true_parametric_family_claim':False,
            'component_is_operational_dependency_proxy':True,
            'asymptotic_claim':False,
        },
    }
    raw=report['late_shell_300_400_vs_400_500']['raw']['shift_l2']
    de_d=report['late_shell_300_400_vs_400_500']['equal_weight_per_d']['shift_l2']
    de_c=report['late_shell_300_400_vs_400_500']['equal_weight_per_component']['shift_l2']
    report['decision']={
        'SAME_DIAGONAL_MULTIPLICITY_MATERIALLY_REDUCES_LATE_SHIFT': de_d <= 0.75*raw,
        'GRAPH_COMPONENT_EQUAL_WEIGHT_MATERIALLY_REDUCES_LATE_SHIFT': de_c <= 0.75*raw,
        'FEW_LARGEST_COMPONENTS_DRIVE_LATE_SHIFT': bool(removal and min(x['late_shift_l2'] for x in removal) <= 0.5*raw),
        'RAW_LATE_SHIFT_L2':raw,'EQUAL_D_LATE_SHIFT_L2':de_d,'EQUAL_COMPONENT_LATE_SHIFT_L2':de_c,
        'NEXT':'Stage14-num-alpha11-diag6 compare Stage13 exactly-one and Stage14 exactly-two under matched cutoff/shell/direction conventions if cluster dependence does not explain the late shift; otherwise isolate the driving family proxy',
    }
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__': main()
