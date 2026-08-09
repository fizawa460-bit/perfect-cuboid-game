#!/usr/bin/env python3
"""Stage14-num5 finite moving-window scaling and anomaly diagnostics.

This stage consumes the frozen Stage14-num4 B=100m object source and manifest.
All statistics are descriptive finite diagnostics.  Power-law fits, drift flags,
and anomaly thresholds are deliberately non-theorem heuristics.
"""
from __future__ import annotations

import argparse
import base64
import bz2
import csv
import hashlib
import io
import json
import math
from collections import Counter, defaultdict
from math import gcd, isqrt
from pathlib import Path

BOUND = 100_000_000
GRID_STEP = 5_000_000
PRIMES = (2, 3, 5, 7, 11, 13)
EXPECTED = {
    "object_count": 1875,
    "counts": {"a": 729, "b": 758, "c": 388, "total": 1875, "triple": 0},
    "object_key_sha256": "b8151aedbf46f33700b213c79a5227fa62653d2279eed954103a2b9e768fff42",
    "object_key_mask_sha256": "2ac9a994f735d2d4f8f3c519145de17d920bdcf9841f32a73793cae3ec94e14f",
    "vertex_ledger_sha256": "99f9cf72d473df19a2fc27e04032095607995ea43d874afd08a15e7fc7e240f0",
    "edge_ledger_sha256": "c54aa6fea7971a44e317a041986ca1197671af2cab97825943ebb9d51cadd97e",
    "num4_full_sha256": "fade5a039ae63490ff3422ec0b25b1474063ec5f47906826b838f656959a580c",
    "num4_face_sha256": "52a214b0bbb782525f7b15afd275fc49662c19699b098054f01332d18264e8a5",
    "num4_edge_sha256": "9d49ad5643d2aa3753ebd142609c51e546aab281ee4fcbe4c844030e0ae06db8",
    "num4_provenance_sha256": "8aa69b3788b8e359314775c43f349a03fbb60f44a87c8ae2685d687d4a7c5192",
}


def digest_rows(rows) -> str:
    payload = "".join(",".join(map(str, row)) + "\n" for row in sorted(rows))
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def read_objects(path: Path):
    if path.is_dir():
        parts = sorted(path.glob("part-*.b64"))
        if not parts:
            raise ArithmeticError("empty num4 object-source directory")
        encoded = "".join(p.read_text(encoding="ascii").strip() for p in parts)
        raw = bz2.decompress(base64.b64decode(encoded))
        stream = io.StringIO(raw.decode("utf-8"), newline="")
    else:
        stream = path.open(newline="", encoding="utf-8")
    try:
        rows = [tuple(int(r[k]) for k in ("a", "b", "c", "d", "mask")) for r in csv.DictReader(stream)]
    finally:
        stream.close()
    if len(rows) != len(set(rows)):
        raise ArithmeticError("duplicate num4 object rows")
    return sorted(rows)


def is_square(n: int):
    r = isqrt(n)
    return r*r == n, r


def face_mask(a: int, b: int, c: int):
    mask = 0
    ds = []
    for i, value in enumerate((a*a+b*b, a*a+c*c, b*b+c*c)):
        ok, r = is_square(value)
        if ok:
            mask |= 1 << i
            ds.append(r)
        else:
            ds.append(0)
    return mask, tuple(ds)


def primitive_face(S: int, X: int, H: int):
    q = gcd(S, X)
    return (S//q, X//q, H//q)


def direction(mask: int):
    return {0b011: "a", 0b101: "b", 0b110: "c", 0b111: "triple"}[mask]


def object_edge_detail(rec):
    a,b,c,d,mask = rec
    _, (dab,dac,dbc) = face_mask(a,b,c)
    out=[]
    if mask & 1 and mask & 2:
        out.append((a,b,c,primitive_face(a,b,dab),primitive_face(a,c,dac)))
    if mask & 1 and mask & 4:
        out.append((b,a,c,primitive_face(b,a,dab),primitive_face(b,c,dbc)))
    if mask & 2 and mask & 4:
        out.append((c,a,b,primitive_face(c,a,dac),primitive_face(c,b,dbc)))
    return out


def object_edge(rec):
    details = object_edge_detail(rec)
    if len(details) != 1:
        raise ArithmeticError("num5 expects exact-two objects at frozen B=100m")
    *_, f1, f2 = details[0]
    return tuple(sorted((f1,f2)))


def local_state(g: int, u: int, v: int, p: int):
    G = g % p == 0
    U = u % p == 0
    V = v % p == 0
    if U and V:
        raise ArithmeticError("coprime u,v local-state violation")
    return (("G" if G else "") + ("U" if U else "") + ("V" if V else "")) or "none"


def edge_states(rec):
    e,x,y,_,_ = object_edge_detail(rec)[0]
    u = gcd(e,x)
    v = gcd(e,y)
    if gcd(u,v) != 1 or e % (u*v):
        raise ArithmeticError("gcd/lcm inverse regression")
    g = e // (u*v)
    return {str(p): local_state(g,u,v,p) for p in PRIMES}


def validate_num4(objects, manifest):
    counts = Counter(direction(r[4]) for r in objects)
    got_counts = {
        "a": counts["a"], "b": counts["b"], "c": counts["c"],
        "total": counts["a"]+counts["b"]+counts["c"], "triple": counts["triple"]
    }
    edges=set()
    vertices=set()
    for rec in objects:
        a,b,c,d,mask=rec
        if not (0<a<b<c and gcd(a,gcd(b,c)) == 1 and d <= BOUND and a*a+b*b+c*c == d*d):
            raise ArithmeticError("population contract regression")
        m,_=face_mask(a,b,c)
        if m != mask:
            raise ArithmeticError("face-mask regression")
        edge=object_edge(rec)
        edges.add(edge)
        vertices.update(edge)
    got = {
        "object_count": len(objects),
        "counts": got_counts,
        "object_key_sha256": digest_rows(r[:4] for r in objects),
        "object_key_mask_sha256": digest_rows(objects),
        "vertex_ledger_sha256": digest_rows(vertices),
        "edge_ledger_sha256": digest_rows(u+v for u,v in edges),
    }
    for key in ("object_count","counts","object_key_sha256","object_key_mask_sha256","vertex_ledger_sha256","edge_ledger_sha256"):
        if got[key] != EXPECTED[key]:
            raise ArithmeticError(f"num4 source regression {key}: {got[key]}")
    if manifest["decision"]["STAGE14_NUM4"] != "COMPLETE_UNIFIED_FINITE_FINGERPRINT_LEDGER":
        raise ArithmeticError("num4 decision lock missing")
    hashes=manifest["hashes"]
    expected_hashes={
        "unified_full_ledger_sha256": EXPECTED["num4_full_sha256"],
        "unified_face_core_sha256": EXPECTED["num4_face_sha256"],
        "unified_edge_fingerprint_sha256": EXPECTED["num4_edge_sha256"],
        "provenance_catalog_sha256": EXPECTED["num4_provenance_sha256"],
    }
    if hashes != expected_hashes:
        raise ArithmeticError("num4 unified hash regression")
    return got


def ols_power_fit(rows):
    xs=[math.log(float(B)) for B,N in rows]
    ys=[math.log(float(N)) for B,N in rows]
    xm=sum(xs)/len(xs); ym=sum(ys)/len(ys)
    den=sum((x-xm)**2 for x in xs)
    alpha=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/den
    intercept=ym-alpha*xm
    pred=[alpha*x+intercept for x in xs]
    ssr=sum((y-p)**2 for y,p in zip(ys,pred))
    sst=sum((y-ym)**2 for y in ys)
    r2=1-ssr/sst if sst else 1.0
    return {"alpha":alpha,"log_C":intercept,"r2":r2}


def tvd(c1, c2):
    n1=sum(c1.values()); n2=sum(c2.values())
    keys=set(c1)|set(c2)
    return 0.5*sum(abs(c1[k]/n1-c2[k]/n2) for k in keys)


def graph_at(rows):
    degree=defaultdict(int)
    vertices=set()
    for rec in rows:
        u,v=object_edge(rec)
        vertices.add(u); vertices.add(v)
        degree[u]+=1; degree[v]+=1
    hist=Counter(degree.values())
    return {
        "active_faces": len(vertices),
        "max_degree": max(degree.values(), default=0),
        "degree_ge_8": sum(n for deg,n in hist.items() if deg >= 8),
        "degree_histogram": {str(k):v for k,v in sorted(hist.items())},
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--objects", type=Path, required=True)
    ap.add_argument("--num4-manifest", type=Path, required=True)
    ap.add_argument("--manifest-out", type=Path, required=True)
    args=ap.parse_args()

    objects=read_objects(args.objects)
    num4=json.loads(args.num4_manifest.read_text(encoding="utf-8"))
    base=validate_num4(objects,num4)
    states={r[:4]:edge_states(r) for r in objects}

    cumulative=[]
    graph=[]
    for B in range(GRID_STEP, BOUND+1, GRID_STEP):
        rows=[r for r in objects if r[3] <= B]
        c=Counter(direction(r[4]) for r in rows)
        N=c["a"]+c["b"]+c["c"]
        cumulative.append({
            "B": B,
            "N2": N,
            "counts": {"a":c["a"],"b":c["b"],"c":c["c"],"triple":c["triple"]},
            "direction_share": {q:(c[q]/N if N else 0.0) for q in "abc"},
            "N2_over_sqrt_B": N/math.sqrt(B) if N else 0.0,
        })
        g=graph_at(rows)
        g["B"]=B
        graph.append(g)

    rolling=[]
    for i in range(4,len(cumulative)):
        window=cumulative[i-4:i+1]
        fit=ols_power_fit([(r["B"],r["N2"]) for r in window])
        rolling.append({
            "end_B":window[-1]["B"],
            "start_B":window[0]["B"],
            "points":5,
            **fit,
        })

    shells=[]
    prev_local=None
    for B in range(30_000_000, BOUND+1, GRID_STEP):
        lo=B//2
        rows=[r for r in objects if lo < r[3] <= B]
        c=Counter(direction(r[4]) for r in rows)
        n=len(rows)
        local={str(p):Counter() for p in PRIMES}
        for r in rows:
            for p,s in states[r[:4]].items():
                local[p][s]+=1
        shell={
            "B":B,"lower_exclusive":lo,"objects":n,
            "counts":{q:c[q] for q in "abc"},
            "direction_share":{q:c[q]/n for q in "abc"},
            "local_state_counts":{p:dict(sorted(v.items())) for p,v in local.items()},
            "adjacent_shell_tvd": {p:(None if prev_local is None else tvd(prev_local[p],local[p])) for p in map(str,PRIMES)},
        }
        shells.append(shell)
        prev_local=local

    final_share=cumulative[-1]["direction_share"]
    direction_extrema={}
    for q in "abc":
        candidates=[(abs(r["direction_share"][q]-final_share[q]),r) for r in shells]
        dev,row=max(candidates,key=lambda t:t[0])
        direction_extrema[q]={
            "max_abs_deviation_from_B100m_cumulative_share":dev,
            "at_B":row["B"],
            "shell_share":row["direction_share"][q],
            "B100m_cumulative_share":final_share[q],
        }

    local_tvd_max={}
    for p in map(str,PRIMES):
        candidates=[(r["adjacent_shell_tvd"][p],r["B"]) for r in shells if r["adjacent_shell_tvd"][p] is not None]
        val,B=max(candidates)
        local_tvd_max[p]={"max_adjacent_shell_tvd":val,"at_B":B}

    degree_jumps=[]
    for a,b in zip(graph,graph[1:]):
        if b["max_degree"] > a["max_degree"]:
            degree_jumps.append({"B":b["B"],"from":a["max_degree"],"to":b["max_degree"]})

    earliest=rolling[0]; latest=rolling[-1]
    sqrt_first=cumulative[0]["N2_over_sqrt_B"]
    sqrt_last=cumulative[-1]["N2_over_sqrt_B"]
    thresholds={
        "rolling_alpha_total_drift":0.05,
        "direction_shell_abs_share_deviation":0.04,
        "local_adjacent_shell_tvd":0.05,
        "graph_max_degree_jump":1,
    }
    flags={
        "scaling_alpha_drift": abs(latest["alpha"]-earliest["alpha"]) >= thresholds["rolling_alpha_total_drift"],
        "direction_shell_drift": any(v["max_abs_deviation_from_B100m_cumulative_share"] >= thresholds["direction_shell_abs_share_deviation"] for v in direction_extrema.values()),
        "local_fingerprint_instability": any(v["max_adjacent_shell_tvd"] >= thresholds["local_adjacent_shell_tvd"] for v in local_tvd_max.values()),
        "graph_degree_jump": any(j["to"]-j["from"] >= thresholds["graph_max_degree_jump"] for j in degree_jumps),
        "perfect_cuboid_emergency": cumulative[-1]["counts"]["triple"] != 0,
    }

    compact_cumulative=[
        [r["B"],r["N2"],r["counts"]["a"],r["counts"]["b"],r["counts"]["c"],r["counts"]["triple"],r["N2_over_sqrt_B"],graph[i]["max_degree"]]
        for i,r in enumerate(cumulative)
    ]
    compact_rolling=[[r["start_B"],r["end_B"],r["alpha"],r["r2"]] for r in rolling]
    compact_shells=[
        [r["lower_exclusive"],r["B"],r["objects"],r["direction_share"]["a"],r["direction_share"]["b"],r["direction_share"]["c"],
         *[r["adjacent_shell_tvd"][str(p)] for p in PRIMES]]
        for r in shells
    ]
    manifest={
        "metadata":{
            "stage":"14-num5",
            "classification":"FINITE_MOVING_WINDOW_SCALING_AND_ANOMALY_DIAGNOSTICS",
            "bound":BOUND,
            "grid_step":GRID_STEP,
            "half_range_shell_count":len(shells),
            "finite_diagnostic_only":True,
            "fit_is_theorem":False,
            "anomaly_thresholds_are_theorem":False,
        },
        "num4_regression":base,
        "thresholds":thresholds,
        "cumulative_grid_columns":["B","N2","a","b","c","triple","N2_over_sqrt_B","max_degree"],
        "cumulative_grid":compact_cumulative,
        "rolling_power_fit_columns":["start_B","end_B","alpha","r2"],
        "rolling_power_fits_5point":compact_rolling,
        "half_range_shell_columns":["lower_exclusive","B","objects","share_a","share_b","share_c","tvd_p2","tvd_p3","tvd_p5","tvd_p7","tvd_p11","tvd_p13"],
        "half_range_shells":compact_shells,
        "summary":{
            "rolling_alpha_first":earliest,
            "rolling_alpha_last":latest,
            "rolling_alpha_change":latest["alpha"]-earliest["alpha"],
            "N2_over_sqrt_B_first_B5m":sqrt_first,
            "N2_over_sqrt_B_last_B100m":sqrt_last,
            "N2_over_sqrt_B_fractional_change":sqrt_last/sqrt_first-1.0,
            "direction_shell_extrema":direction_extrema,
            "local_tvd_max":local_tvd_max,
            "graph_max_degree_jumps":degree_jumps,
            "flags":flags,
        },
        "decision":{
            "STAGE14_NUM5":"COMPLETE_FINITE_SCALING_ANOMALY_DIAGNOSTICS",
            "MOVING_WINDOWS_FROZEN":True,
            "ROLLING_FITS_NON_THEOREM":True,
            "SCALING_STABILIZED":False,
            "LOCAL_FINGERPRINT_MATERIAL_INSTABILITY_DETECTED":flags["local_fingerprint_instability"],
            "MATERIAL_FINITE_CHANGE_HANDOFF": flags["scaling_alpha_drift"] or flags["direction_shell_drift"] or flags["graph_degree_jump"],
            "FINITE_DIAGNOSTIC_ONLY":True,
            "ASYMPTOTIC_CLAIM":False,
            "PERFECT_CUBOID_EXISTENCE_CLAIM":False,
            "PERFECT_CUBOID_NONEXISTENCE_CLAIM":False,
            "NEXT":"Stage14-num6 rolling observatory / larger exact cutoff append",
        },
    }
    args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
    args.manifest_out.write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"summary":manifest["summary"],"decision":manifest["decision"]},indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
