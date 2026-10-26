#!/usr/bin/env python3
"""AFFINE33 exact A-block composition closure for the AFFINE32 pairing[96]=1 residual.

AFFINE32 stabilizes this parent at
  pairing[92..98] = (0,1,0,0,1,0,0),
  pairing[99] = p100 = 0,
with exact A-block mass sum(pairing[92..103]) = 5.

Hence the only unfixed A-block entries are pairing[100..103], they are
nonnegative integers, and their total is exactly 3.  Enumerate all 20 weak
compositions of 3 into those four entries and classify each simultaneous
assignment using only the exact saturated HNF image, completed-square
ellipsoid emptiness, and exact real pairing separation already implemented by
AFFINE32.

This is a bounded structural closure probe.  No Fincke--Pohst scaleout and no
downstream credit are performed here.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
AFF32=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine32_singleton_forced_closure.py"
AFF32_BLOB="f41900e0e36ba36ec48e75a617261521f0d2a17c"

PAIR96_VALUE=1
FINAL_FIXED={92:0,93:1,94:0,95:0,96:1,97:0,98:0}
P100_INDEX=99
FREE_A=(100,101,102,103)
A_TOTAL=5
FREE_TOTAL=3
EXPECTED_PARENT_RADIUS="829/24"
EXPECTED_PARENT_MAX_C2="349/24"
EXPECTED_PARENT_RANK=25
EXPECTED_PARENT_KERNEL_DIM=39


def req(v,msg):
    if not v:
        raise SystemExit("FAIL: "+msg)


def blob(path):
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    req(spec is not None and spec.loader is not None,"module spec "+name)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod


def weak_compositions(total,count,prefix=()):
    if count==1:
        yield prefix+(total,)
        return
    for v in range(total+1):
        yield from weak_compositions(total-v,count-1,prefix+(v,))


def public_ctx(ctx):
    return {
        "classification":ctx["classification"],
        "rank":ctx.get("rank"),
        "kernel_dimension":ctx.get("kernel_dimension"),
        "exact_radius_squared":ctx.get("exact_radius_squared"),
        "exact_real_max_C2":ctx.get("exact_real_max_C2"),
        "separator_index":ctx.get("separator_index"),
        "separator_side":ctx.get("separator_side"),
    }


def main():
    req(AFF32.is_file() and blob(AFF32)==AFF32_BLOB,"AFFINE32 drift")
    a32=load(AFF32,"stage32ex5_eff_affine33_aff32")

    req(a32.AFF29.is_file() and a32.blob(a32.AFF29)==a32.AFF29_BLOB,"AFFINE29 drift")
    a29=a32.load(a32.AFF29,"stage32ex5_eff_affine33_aff29")
    req(a29.AFF28.is_file() and a29.blob(a29.AFF28)==a29.AFF28_BLOB,"AFFINE28 drift")
    a28=a29.load(a29.AFF28,"stage32ex5_eff_affine33_aff28")
    for path,expected,label in (
        (a28.ENGINE,a28.ENGINE_BLOB,"FP58 engine"),
        (a28.AFF15,a28.AFF15_BLOB,"AFFINE15"),
        (a28.AFF24,a28.AFF24_BLOB,"AFFINE24"),
        (a28.AFF27,a28.AFF27_BLOB,"AFFINE27"),
    ):
        req(path.is_file() and a28.blob(path)==expected,label+" drift")

    eng=a28.load(a28.ENGINE,"stage32ex5_eff_affine33_engine")
    req((eng.D,eng.E,eng.LOW,eng.NORMAL_MASS)==(18,8,-20,302),"engine constants drift")
    aff15=a28.load(a28.AFF15,"stage32ex5_eff_affine33_aff15")

    F6,_A6,_I6,_RK58,_R58,_L,_d,_c,_u,P,gram=eng.build()
    Arow=sum((P.row(i) for i in range(92,104)),Matrix.zeros(1,64))
    ABrow=sum((P.row(i) for i in range(92,116)),Matrix.zeros(1,64))
    Crow=sum((P.row(i) for i in range(116,128)),Matrix.zeros(1,64))
    P100row=P.row(aff15.P100_INDEX)
    req(aff15.P100_INDEX==P100_INDEX,"p100 index drift")

    base_rows=[F6.row(i) for i in range(6)]+[Arow,ABrow,Crow,P100row]
    base10=[eng.D,eng.E,0,1,1,1,5,6,2,0]

    req(base10[6]==A_TOTAL and base10[9]==0,"A/p100 target drift")
    req(sum(FINAL_FIXED.get(i,0) for i in range(92,99))==2,"fixed A subtotal drift")
    req(A_TOTAL-sum(FINAL_FIXED.get(i,0) for i in range(92,99))-base10[9]==FREE_TOTAL,
        "free A mass drift")

    parent=a32.direct_classification(
        a32.build_context(base_rows,base10,P,gram,aff15,FINAL_FIXED),eng)
    req(parent["classification"]=="UNRESOLVED","AFFINE32 parent classification drift")
    req(parent["rank"]==EXPECTED_PARENT_RANK and
        parent["kernel_dimension"]==EXPECTED_PARENT_KERNEL_DIM,
        "AFFINE32 parent dimension drift")
    req(parent["exact_radius_squared"]==EXPECTED_PARENT_RADIUS,
        "AFFINE32 parent radius drift")
    req(parent["exact_real_max_C2"]==EXPECTED_PARENT_MAX_C2,
        "AFFINE32 parent max-C2 drift")

    comps=list(weak_compositions(FREE_TOTAL,len(FREE_A)))
    req(len(comps)==20 and all(sum(c)==FREE_TOTAL for c in comps),
        "A composition population drift")

    rows=[]
    unresolved=[]
    counts={}
    for values in comps:
        fixed=dict(FINAL_FIXED)
        for idx,value in zip(FREE_A,values):
            fixed[idx]=value
        child=a32.direct_classification(
            a32.build_context(base_rows,base10,P,gram,aff15,fixed),eng)
        pub=public_ctx(child)
        row={"composition":list(values),**pub}
        rows.append(row)
        counts[pub["classification"]]=counts.get(pub["classification"],0)+1
        if pub["classification"]=="UNRESOLVED":
            unresolved.append(row)

    closed=len(unresolved)==0
    out={
        "schema":"STAGE32EX5_EFF_AFFINE33_A_BLOCK_COMPOSITION_CLOSURE_V1",
        "status":"PASS_BOUNDED_EXACT_A_BLOCK_COMPOSITION_CLOSURE",
        "predecessor":{
            "affine32_pairing96_value":PAIR96_VALUE,
            "affine32_final_fixed":{str(k):v for k,v in sorted(FINAL_FIXED.items())},
            "parent_rank":EXPECTED_PARENT_RANK,
            "parent_kernel_dimension":EXPECTED_PARENT_KERNEL_DIM,
            "parent_exact_radius_squared":EXPECTED_PARENT_RADIUS,
            "parent_exact_real_max_C2":EXPECTED_PARENT_MAX_C2,
        },
        "a_block":{
            "range":[92,103],
            "total_mass":A_TOTAL,
            "p100_index":P100_INDEX,
            "p100_value":0,
            "free_indices":list(FREE_A),
            "free_total":FREE_TOTAL,
            "composition_count":len(comps),
        },
        "classification_counts":counts,
        "rows":rows,
        "unresolved_compositions":unresolved,
        "pairing96_value1_closed_exactly":closed,
        "interpretation":{
            "what_is_proved":"All 20 nonnegative integer A-block compositions compatible with the AFFINE32 simultaneous fixed coordinates are exhaustively classified by exact saturated HNF membership, completed-square emptiness, or exact real pairing separation.",
            "next_exact_unit":"If closed, remove pairing[96]=1 from the selected AFFINE23 residual and continue only on the pairing[96]=0 stable residual. If not closed, continue only on the surviving A-block compositions rather than another unconstrained one-coordinate chain.",
            "what_is_not_proved":"The pairing[96]=0 parent and all other AFFINE22 residual fibers remain UNKNOWN. No effectivity, MAIN, receiver, theorem, endpoint, or merge credit is self-promoted."
        },
        "credit":{"effectivity":False,"main":False,"receiver":False,"theorem":False,"endpoint":False,"merge":False},
    }
    print("EFF_AFFINE33_A_BLOCK_COMPOSITION="+json.dumps(out,sort_keys=True,separators=(",",":")))


if __name__=="__main__":
    main()
