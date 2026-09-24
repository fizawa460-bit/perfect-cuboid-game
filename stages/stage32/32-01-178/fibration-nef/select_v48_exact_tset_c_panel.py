#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import math
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SUPPORT = HERE / "run_hpadj22_support_qbc_local_row_b.py"
SUPPORT_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
V47_HELPER = ROOT / "stages/stage32/management/grf04-hpadj22-joint/benchmark_grf04_hpadj22_highd_bchunk.py"
V47_HELPER_BLOB = "99eef03657b07eb5cf86be8d880050fd8aa2d13b"


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(p: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, p)
    req(spec is not None and spec.loader is not None, "cannot load " + str(p))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def tset(support, b: int, c: int, s: int, qbc: int) -> tuple[int, ...]:
    parity = c & 1
    return tuple(
        t for t in range(parity, b + c + 1, 2)
        if support.aggregate_q_lower(b, c, t, s) <= qbc
    )


def dist(y: int, vals: tuple[int, ...]) -> int:
    p = bisect.bisect_left(vals, y)
    best = 10**30
    if p < len(vals):
        best = min(best, abs(vals[p] - y))
    if p:
        best = min(best, abs(vals[p - 1] - y))
    return best


def exact_count(xs: list[int], *, d: int, g: int, vals: tuple[int, ...], q: int) -> int:
    if not xs or not vals:
        return 0
    rem = 3*d*d + 48*d + 96 - 96*g - 24*q
    if rem < 0:
        return 0
    rad = math.isqrt(rem // 4)
    return sum(dist(d//2 - 2*x4, vals) <= rad for x4 in xs)


def main() -> None:
    started=time.perf_counter()
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--top",type=int,default=3)
    a=ap.parse_args()

    req(blob(SUPPORT)==SUPPORT_BLOB,"support worker drift")
    req(blob(V47_HELPER)==V47_HELPER_BLOB,"V47 helper drift")
    support=load(SUPPORT,"exact_tset_selector_support")
    hd=load(V47_HELPER,"exact_tset_selector_v47")
    direct=hd.load(hd.DIRECT,hd.DIRECT_BLOB,"exact_tset_selector_direct")
    old=direct.load_old(a.source_root)
    ctx=old.source_context()
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second=ctx

    row_index=22
    row_id,g0,d0=rows[row_index]
    g,d=int(g0),int(d0)
    req((row_id,g,d)==("g1-d192",1,192),"row22 identity drift")
    h=d//2
    b=36
    tq=(d*d+16*d+(32 if g==0 else 0))//8
    joint=bc.build_joint_bc_shard(old.HMAX,b,b)

    qa_values=set()
    for aa in range(h+1):
        if counter.component_a(d,aa)<0:
            continue
        for sa in range(4):
            tiers=profiles[aa][sa]
            if tiers:
                qa_values.update(int(q) for q,_ in tiers if 0<=int(q)<=tq)
    qa_values=sorted(qa_values)[-8:]  # selector heuristic only; exact cell replay below uses every qA tier

    rows_out=[]
    for c in range(h+1):
        c3=counter.component3(d,b,c)
        if c3<0:
            continue
        jbc=joint[b][c]
        active=[]
        for sbc in range(8):
            for r in (0,1):
                hist={int(q):int(w) for q,w in jbc[sbc][r].items() if int(w) and int(q)<=tq}
                if hist:
                    active.append((sbc,r,hist))
        if not active:
            continue

        points=hd.x4_points(h16,h,g,b,c)
        score=0
        strict_states=0
        hole_states=0
        max_delta=0
        qbc_states=0
        for sbc,r,hist in active:
            cache={}
            for qbc,mult in hist.items():
                vals=tset(support,b,c,sbc,qbc)
                req(bool(vals),f"empty tset {(c,sbc,r,qbc)}")
                hull=support.support_t_interval(b=b,c=c,support=sbc,qbc=qbc)
                req((vals[0],vals[-1])==hull,f"hull endpoint drift {(c,sbc,r,qbc)}")
                cache[qbc]=(vals,hull)
                qbc_states+=1
                parity_hull=((hull[1]-hull[0])//2)+1
                hole_states += int(len(vals)<parity_hull)

            for qa in qa_values:
                xs=[x4 for x4,cap in points[r] if cap>=qa]
                if not xs:
                    continue
                for qbc,mult in hist.items():
                    if qa+qbc>tq:
                        continue
                    vals,hull=cache[qbc]
                    hc=hd.count_intersection(counter,xs,d=d,g=g,tint=hull,q=qa+qbc)
                    ec=exact_count(xs,d=d,g=g,vals=vals,q=qa+qbc)
                    req(ec<=hc,f"selector weakening {(c,sbc,r,qbc,qa,ec,hc)}")
                    delta=hc-ec
                    if delta:
                        strict_states+=1
                        max_delta=max(max_delta,delta)
                        score += int(mult)*delta

        rows_out.append({
            "c":c,
            "heuristic_hist_x4_saving_score":str(score),
            "strict_count_states":strict_states,
            "hole_states":hole_states,
            "qbc_states":qbc_states,
            "max_hull_minus_exact_x4_count":max_delta,
        })

    ranked=sorted(
        rows_out,
        key=lambda x:(int(x["heuristic_hist_x4_saving_score"]),x["strict_count_states"],x["hole_states"]),
        reverse=True,
    )
    selected=[x["c"] for x in ranked if int(x["heuristic_hist_x4_saving_score"])>0][:a.top]
    req(bool(selected),"selector found no c with any exact-set count tightening")
    out={
        "schema":"STAGE32_32_01_178_V48_EXACT_TSET_C_PANEL_SELECTOR_V1",
        "status":"HEURISTIC_BOUNDED_SELECTOR_ONLY__ZERO_MAIN_CREDIT",
        "target":{"row_index":22,"row_id":row_id,"g":g,"d":d,"b":b},
        "selected_c":selected,
        "top_rows":ranked[:10],
        "coverage":{"eligible_c_rows":len(rows_out),"selector_qa_values":len(qa_values),"selector_uses_highest_qA_tiers":True},
        "semantics":{
            "selector_score_is_not_terminal_credit":True,
            "selector_omits_a_e_profile_weights":True,
            "exact_weighted_cell_replay_required":True,
        },
        "timing":{"wall_seconds":time.perf_counter()-started},
        "firewalls":{"main_credit":False,"theorem_credit":False,"endpoint_credit":False,"merge":False},
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
    print("V48_EXACT_TSET_C_PANEL_SELECTOR="+json.dumps(out,sort_keys=True))


if __name__=="__main__":
    main()
