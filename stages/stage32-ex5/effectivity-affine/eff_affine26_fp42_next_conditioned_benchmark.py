#!/usr/bin/env python3
"""Second bounded exact FP42 benchmark for AFFINE24 pairing[96]=4.

AFFINE25 closed pairing[96]=5 exactly in 146 nodes. This successor tests only
the next-smallest unresolved AFFINE24 branch under the same conditioner.
"""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path
from sympy import Matrix

ROOT=Path(__file__).resolve().parents[3]
AFF25=ROOT/"stages/stage32-ex5/effectivity-affine/eff_affine25_fp42_conditioned_benchmark.py"
AFF25_BLOB="9ae0c149236be3ad7777004d0a1c0a187fba4bbd"
TARGET_VALUE=4
TARGET_RADIUS="457/24"
TARGET_MAX_C2="-23/24"

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)
def blob(path):
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    req(spec is not None and spec.loader is not None,"module spec")
    mod=importlib.util.module_from_spec(spec); sys.modules[name]=mod; spec.loader.exec_module(mod)
    return mod

def main():
    req(AFF25.is_file() and blob(AFF25)==AFF25_BLOB,"AFFINE25 drift")
    a25=load(AFF25,"stage32ex5_eff_affine26_aff25")
    for path,expected,label in (
        (a25.ENGINE,a25.ENGINE_BLOB,"FP58 engine"),
        (a25.AFF15,a25.AFF15_BLOB,"AFFINE15"),
        (a25.AFF17,a25.AFF17_BLOB,"AFFINE17"),
        (a25.AFF19,a25.AFF19_BLOB,"AFFINE19"),
        (a25.AFF24,a25.AFF24_BLOB,"AFFINE24"),
    ):
        req(path.is_file() and a25.blob(path)==expected,label+" drift")

    eng=a25.load(a25.ENGINE,"stage32ex5_eff_affine26_engine")
    aff15=a25.load(a25.AFF15,"stage32ex5_eff_affine26_aff15")
    aff24=a25.load(a25.AFF24,"stage32ex5_eff_affine26_aff24")
    F6,_A6,_I6,_RK58,_R58,_L,_d,_c,_u,P,gram=eng.build()
    Arow=sum((P.row(i) for i in range(92,104)),Matrix.zeros(1,64))
    ABrow=sum((P.row(i) for i in range(92,116)),Matrix.zeros(1,64))
    Crow=sum((P.row(i) for i in range(116,128)),Matrix.zeros(1,64))
    P100row=P.row(aff15.P100_INDEX)
    base_rows=[F6.row(i) for i in range(6)]+[Arow,ABrow,Crow,P100row]
    base10=[eng.D,eng.E,*a25.TARGET_BASE4,a25.TARGET_A,a25.TARGET_AB,a25.TARGET_C,a25.TARGET_P100]
    ctx=aff24.build_conditioned_context(a25.TARGET_PAIRING_INDEX,base_rows,P,gram,aff15)
    req(ctx is not None and ctx["kernel_dimension"]==42,"conditioned context drift")
    cheap=aff24.branch_classification(ctx,base10,TARGET_VALUE,P,gram,eng)
    req(cheap["classification"]=="UNRESOLVED_AFTER_ONE_PAIRING_CONDITIONING","AFFINE24 value4 classification drift")
    req(cheap["exact_radius_squared"]==TARGET_RADIUS,"AFFINE24 value4 radius drift")
    req(cheap["exact_real_max_C2"]==TARGET_MAX_C2,"AFFINE24 value4 max-C2 drift")

    a25.TARGET_PAIRING_VALUE=TARGET_VALUE
    a25.TARGET_RADIUS=TARGET_RADIUS
    result=a25.solve42(ctx,a25.build_lll42(ctx,P,gram),base10,P,gram,eng,aff24)
    out={
        "schema":"STAGE32EX5_EFF_AFFINE26_FP42_NEXT_CONDITIONED_BENCHMARK_V1",
        "status":"PASS_BOUNDED_EXACT_FP42_NEXT_CONDITIONED_BENCHMARK",
        "predecessor":{
            "affine25_pairing_value":5,
            "affine25_classification":"BAD_SHELL_UNSAT_EXACT_FP42",
            "affine25_node_count":146,
            "pairing_index":a25.TARGET_PAIRING_INDEX,
            "next_pairing_value":TARGET_VALUE,
            "kernel_dimension":42,
            "exact_radius_squared":TARGET_RADIUS,
            "exact_real_max_C2":TARGET_MAX_C2,
        },
        "selection":{"rule":"next-smallest exact-radius unresolved branch under AFFINE24 pairing[96] conditioner","horizontal_scaleout":False},
        "result":result,
        "interpretation":{
            "what_is_proved":"If complete=true, this one saturated pairing[96]=4 branch is resolved exactly by FP42. If complete=false, it remains UNKNOWN.",
            "next_exact_unit":"If this branch also closes cheaply, compare exact search growth against value5 before deciding whether one more branch or a structural separator is the smaller next leaf.",
            "what_is_not_proved":"pairing[96] values 0..3 and all other AFFINE22 residual fibers remain untouched. No effectivity, MAIN, receiver, theorem, endpoint, or merge credit is self-promoted.",
        },
        "credit":{"effectivity":False,"main":False,"receiver":False,"theorem":False,"endpoint":False,"merge":False},
    }
    print("EFF_AFFINE26_FP42_NEXT="+json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__":
    main()
