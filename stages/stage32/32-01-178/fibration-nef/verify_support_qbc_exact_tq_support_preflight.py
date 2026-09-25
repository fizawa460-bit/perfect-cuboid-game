#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from functools import lru_cache
from itertools import product
from pathlib import Path

HERE=Path(__file__).resolve().parent
RMIN=HERE/"verify_support_qbc_canonical_r_joint_min_preflight.py"
RMIN_BLOB="bb8ccb843a2e2bacaf5c25f88116e2ddddfc4439"
CANON=HERE/"verify_support_qbc_canonical_joint_min_preflight.py"
CANON_BLOB="4296a18f9fb1b59f963206ff28af73a4e9cf7ef0"
PANEL=HERE/"V48-EXACT-TSET-HIGHVALUE-PANEL-RETAINED.json"
PANEL_BLOB="19cfa17b049b94dee5f406cb8db32ca94e8cf318"
PANEL_CANON="ec9aa7f7300f7613bd05ef3dbdd56de45db0193f91c1d7a82ed7f3e4c972de60"
QCAP=4992
INF=10**30


def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)


def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()


def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p)
    req(spec is not None and spec.loader is not None,"cannot load "+str(p))
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod


@lru_cache(maxsize=None)
def pair_q_values(total:int,k:int,first_lower:int):
    vals=set()
    for x8 in range(int(total)+1):
        x10=int(total)-x8
        if x8<int(first_lower):
            continue
        if int(x8>0)+int(x10>0)!=int(k):
            continue
        vals.add(x8*x8+x10*x10)
    return frozenset(vals)


@lru_cache(maxsize=None)
def exact_q_values(b:int,c:int,t:int,support:int,r:int,qcap:int=QCAP):
    """Exact attainable qBC values at fixed canonical (b,c,t,support,r)."""
    b,c,t,support,r,qcap=map(int,(b,c,t,support,r,qcap))
    if not (0<=support<=7 and r in (0,1)) or ((t-c)&1):
        return frozenset()

    out=set()
    for x0 in range(min(c,t)+1):
        for x1 in range(x0,min(b,t-x0)+1):
            rem=t-x0-x1
            for x9 in range(max(0,rem-c),min(b-x1,rem)+1):
                x5=b-x1-x9
                x6=rem-x9
                pair_total=c-t+x1+x9
                if min(x5,x6,pair_total)<0:
                    continue
                if ((x0+pair_total)&1)!=r:
                    continue
                base_support=sum(int(v>0) for v in (x0,x1,x5,x6,x9))
                pair_support=support-base_support
                if not (0<=pair_support<=2):
                    continue
                first_lower=0 if x0<x1 else x5+int(x6>x9)
                base_q=x0*x0+x1*x1+x5*x5+x6*x6+x9*x9
                if base_q>qcap:
                    continue
                for pair_q in pair_q_values(pair_total,pair_support,first_lower):
                    q=base_q+pair_q
                    if q<=qcap:
                        out.add(q)
    return frozenset(out)


def bounded_literal_regression():
    literal={}
    # Complete for b,c<=4: every nonnegative coordinate contributing to b or c
    # is automatically <=4, so range(5)^7 covers the full finite population.
    for xs in product(range(5),repeat=7):
        x0,x1,x5,x6,x8,x9,x10=xs
        b=x1+x5+x9
        c=x0+x6+x8+x10
        if b>4 or c>4:
            continue
        if x0>x1:
            continue
        if x0==x1 and (x5,x6)>(x8,x9):
            continue
        if (x1+x8+x9+x10)&1:
            continue
        t=x0+x1+x6+x9
        support=sum(int(v>0) for v in xs)
        r=(x0+x8+x10)&1
        q=sum(v*v for v in xs)
        literal.setdefault((b,c,t,support,r),set()).add(q)

    mismatch=0
    total_q_values=0
    max_q_values_per_state=0
    for key,vals in literal.items():
        got=set(exact_q_values(*key,QCAP))
        mismatch += int(got!=vals)
        total_q_values += len(vals)
        max_q_values_per_state=max(max_q_values_per_state,len(vals))
    return {
        "literal_keys":len(literal),
        "formula_mismatches":mismatch,
        "total_exact_q_values":total_q_values,
        "max_q_values_per_state":max_q_values_per_state,
    }


def active_cell_stats(rmin,c:int):
    b=36
    t_domain=tuple(range(c&1,b+c+1,2))
    exact_hist_qbc_bins=0
    strict_qbc_bins=0
    removed_t_total=0
    max_removed_t=0
    best=None

    for support in range(8):
        for r in (0,1):
            floors={t:rmin.canonical_r_joint_q_lower(
                load(CANON,"exact_tq_canon_"+str(c)+"_"+str(support)+"_"+str(r)),
                b,c,t,support,r
            ) for t in t_domain}
            qsets={t:exact_q_values(b,c,t,support,r,QCAP) for t in t_domain}
            union=set()
            for vals in qsets.values():
                union.update(vals)
            exact_hist_qbc_bins += len(union)
            for qbc in union:
                floor_t=tuple(t for t in t_domain if floors[t]<=qbc)
                exact_t=tuple(t for t in t_domain if qbc in qsets[t])
                req(set(exact_t).issubset(floor_t),
                    f"exact t-set escaped floor t-set {(c,support,r,qbc)}")
                removed=len(floor_t)-len(exact_t)
                if removed:
                    strict_qbc_bins += 1
                    removed_t_total += removed
                    max_removed_t=max(max_removed_t,removed)
                    if best is None or removed>best["removed_t"]:
                        best={
                            "c":c,"support":support,"r":r,"qbc":qbc,
                            "floor_tset":list(floor_t),
                            "exact_tset":list(exact_t),
                            "removed_t":removed,
                        }

    return {
        "c":c,
        "exact_hist_qbc_bins":exact_hist_qbc_bins,
        "strict_qbc_bins":strict_qbc_bins,
        "removed_t_total":removed_t_total,
        "max_removed_t":max_removed_t,
        "max_removed_witness":best,
    }


def main():
    req(RMIN.is_file() and blob(RMIN)==RMIN_BLOB,"r-min verifier blob drift")
    req(CANON.is_file() and blob(CANON)==CANON_BLOB,"canonical verifier blob drift")
    req(PANEL.is_file() and blob(PANEL)==PANEL_BLOB,"retained panel blob drift")
    panel=json.loads(PANEL.read_text())
    req(canon(panel)==PANEL_CANON==panel["canonical_sha256_without_this_field"],
        "retained panel canonical drift")

    rmin=load(RMIN,"exact_tq_rmin")

    literal=bounded_literal_regression()
    req(literal=={
        "literal_keys":197,
        "formula_mismatches":0,
        "total_exact_q_values":256,
        "max_q_values_per_state":3,
    },f"bounded literal exact-q regression drift {literal}")

    expected={
        83:{"exact_hist_qbc_bins":8274,"strict_qbc_bins":5912,
            "removed_t_total":97503,"max_removed_t":59},
        85:{"exact_hist_qbc_bins":7909,"strict_qbc_bins":5478,
            "removed_t_total":85294,"max_removed_t":60},
        89:{"exact_hist_qbc_bins":7152,"strict_qbc_bins":4586,
            "removed_t_total":60952,"max_removed_t":57},
    }
    stats=[]
    retained={int(x["c"]):int(x["active_tset_states"]) for x in panel["cells"]}
    for c in (83,85,89):
        row=active_cell_stats(rmin,c)
        for k,v in expected[c].items():
            req(int(row[k])==v,f"active exact-q summary drift {(c,k,row[k],v)}")
        req(row["exact_hist_qbc_bins"]==retained[c],
            f"reconstructed exact qBC support disagrees with retained histogram support c={c}")
        stats.append(row)

    req(sum(x["exact_hist_qbc_bins"] for x in stats)==23335,"three-cell qBC support total drift")
    req(sum(x["strict_qbc_bins"] for x in stats)==15976,"three-cell strict qBC total drift")
    req(sum(x["removed_t_total"] for x in stats)==243749,"three-cell removed-t total drift")

    out={
        "schema":"STAGE32_32_01_178_SUPPORT_QBC_EXACT_TQ_SUPPORT_PREFLIGHT_V1",
        "status":"EXACT_CANONICAL_T_QBC_SUPPORT_STRICTLY_REFINES_R_MIN_TSETS__ZERO_MAIN_CREDIT",
        "source_locks":{
            "canonical_r_joint_min_verifier_blob_sha1":RMIN_BLOB,
            "canonical_joint_min_verifier_blob_sha1":CANON_BLOB,
            "retained_exact_tset_panel_blob_sha1":PANEL_BLOB,
            "retained_exact_tset_panel_canonical_sha256":PANEL_CANON,
        },
        "claim":{
            "fixed_data":"(b,c,H-support,r)",
            "exact_support":"for every t, enumerate the exact attainable qBC values of retained canonical H tuples; at an exact histogram qBC bin retain t iff qBC is in that exact value set",
            "dominance":"T_exact_qBC subset T_canonical_r_floor subset T_canonical subset T_relaxed_joint subset current hull",
            "same_population_check":"the reconstructed qBC support-bin counts equal the independent retained exact histogram-bin counts for c=83,85,89",
            "actual_weighted_v48_gain_claimed":False,
        },
        "bounded_literal_enumeration":literal,
        "active_three_cell_structural_scan":stats,
        "active_three_cell_totals":{
            "exact_hist_qbc_bins":23335,
            "strict_qbc_bins":15976,
            "removed_t_total":243749,
            "max_removed_t_in_one_qbc_bin":60,
        },
        "next_gate":"replace floor-based tsets by exact attainable-qBC tsets in the same full-support+Picard weighted replay",
        "firewalls":{
            "main_credit":False,"full178_numerical_census_changed":False,
            "effectivity_credit":False,"receiver_credit":False,"route_credit":False,
            "theorem_credit":False,"endpoint_credit":False,"stage32_closed":False,
            "merge_authorized":False,
        },
    }
    print("SUPPORT_QBC_EXACT_TQ_SUPPORT_PREFLIGHT="+json.dumps(out,sort_keys=True))

if __name__=="__main__": main()
