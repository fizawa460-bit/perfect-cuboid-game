#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENERAL = HERE / "verify_fibration_nef_zero_center_general_caps.py"
GENERAL_BLOB = "cc6e6aabace3bbe0d92a9cb32e659b3a7df76650"
FAST = HERE / "verify_fibration_nef_lowmass_parity_separable_picard_min.py"
FAST_BLOB = "a4f7b35e52d01d36614c7f46a592fdb7cb54518b"
HPADJ16_BLOB = "61805f8b6d661c29805b6966e2453ed411d73189"
HPADJ10_BLOB = "eebeb47f91df22461c33e9974d63aceca4da3b52"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def first_even_not_excluded(lower: int, upper: int, excluded: set[int]) -> int | None:
    e = lower if lower % 2 == 0 else lower + 1
    while e <= upper and e in excluded:
        e += 2
    return None if e > upper else e


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hpadj16", type=Path, required=True)
    ap.add_argument("--hpadj10", type=Path, required=True)
    args = ap.parse_args()

    req(GENERAL.is_file() and blob(GENERAL) == GENERAL_BLOB, "general-cap theorem drift")
    req(FAST.is_file() and blob(FAST) == FAST_BLOB, "zero-center Picard source drift")
    req(args.hpadj16.is_file() and blob(args.hpadj16) == HPADJ16_BLOB, "HPADJ16 source drift")
    req(args.hpadj10.is_file() and blob(args.hpadj10) == HPADJ10_BLOB, "HPADJ10 source drift")

    general = load_module(GENERAL, "stage32_178_e208_general")
    fast = load_module(FAST, "stage32_178_e208_fast")
    h16 = load_module(args.hpadj16, "stage32_178_e208_hpadj16")
    h10 = load_module(args.hpadj10, "stage32_178_e208_hpadj10")

    req(general.BNB.is_file() and general.git_blob(general.BNB) == general.BNB_BLOB, "BNB source drift")
    req(general.SIG.is_file() and general.git_blob(general.SIG) == general.SIG_BLOB, "signature source drift")
    bnb = general.load_module(general.BNB, "stage32_178_e208_bnb")
    bnb.lock_extra_sources()
    vf = bnb.load_module(bnb.RECOVERABILITY, "stage32_178_e208_recoverability")
    vf.lock_sources()
    kernel = bnb.build_kernel(vf)
    sigmod = general.load_module(general.SIG, "stage32_178_e208_signature")
    cert = fast.load_certificate()

    g, d, h = 1, 192, 96
    legacy = 4
    K = h10.ceil_div(d - 16 * g + 16, 4)
    req(K == 48, "K drift")
    BC = h10.build_bc_exact_parity(h)

    # Exact replay of the current HPADJ pre-domain source predicate, projected
    # only to the minimum even e at which any (a,b,c,support,r) source key exists.
    active_floor = None
    floor_examples = []
    aggregate_states = 0
    for b in range(h + 1):
        for c in range(h + 1):
            bcv = BC[b][c]
            if not any(any(pair) for pair in bcv):
                continue
            c3 = h10.component3(d, b, c)
            if c3 < 0:
                continue
            for a in range(h + 1):
                if 8*a*a + 8*b*b + 6*c*c <= 3*d*d + 96:
                    continue
                ca = h10.component_a(d, a)
                if ca < 0:
                    continue
                M = a + b + c
                srem = min(16, d) + ca + c3
                for sa in range(4):
                    acount = h10.triple_free_count(a, sa)
                    if not acount:
                        continue
                    for sbc, pair in enumerate(bcv):
                        for r in (0, 1):
                            left = int(pair[r])
                            if not left:
                                continue
                            support = sbc + sa
                            qneed = K - support
                            if qneed > 0 and srem < qneed:
                                continue
                            lower = max(legacy, K, d - 4*g + 4, M, M + max(0, qneed))
                            upper = min((19*d)//5, 3*d, 3*d - (b-c))
                            if lower > upper:
                                continue
                            excluded = set()
                            e_n358 = 3*d - (b-c)
                            if b <= h-5 and support+srem == K and e_n358-M >= srem:
                                excluded.add(e_n358)
                            e0 = first_even_not_excluded(lower, upper, excluded)
                            if e0 is None:
                                continue
                            aggregate_states += 1
                            rec = {
                                "a":a,"b":b,"c":c,"support":support,"r":r,
                                "sa":sa,"sbc":sbc,"minimum_even_e":e0,
                            }
                            if active_floor is None or e0 < active_floor:
                                active_floor = e0
                                floor_examples = [rec]
                            elif e0 == active_floor and len(floor_examples) < 32:
                                floor_examples.append(rec)

    req(active_floor == 208, f"current g1-d192 active e floor drift: {active_floor}")
    req(aggregate_states > 0, "source scan empty")
    req(any(x["a"] == 91 and x["b"] == 75 and x["c"] == 4 and x["support"] == 10
            for x in floor_examples), "chosen e208 aggregate not present at active floor")

    # Concrete canonical source terminal at that exact active floor.
    e = 208
    x0,x1,x2,x3,x5,x6,x7,x8,x9,x10 = (1,25,30,30,25,1,31,1,25,1)
    req(x0 < x1 and all(v > 0 for v in (x0,x1,x2,x3,x5,x6,x7,x8,x9,x10)),
        "canonical positive-support witness drift")
    a=x2+x3+x7
    b=x1+x5+x9
    c=x0+x6+x8+x10
    t=x0+x1+x6+x9
    qA=x2*x2+x3*x3+x7*x7
    qH=x0*x0+x1*x1+x5*x5+x6*x6+x8*x8+x9*x9+x10*x10
    qexc=qA+qH
    r=(x0+x8+x10)&1
    supportA=3
    supportH=7
    support=supportA+supportH
    req((a,b,c,t,qA,qH,qexc,r,support) == (91,75,4,52,2761,1879,4640,1,10),
        "concrete witness aggregate drift")
    req(((x1+x8+x9+x10)&1) == 0, "terminal-family parity drift")
    req(int(BC[b][c][supportH][r]) > 0, "exact BC source bucket empty")
    req(h10.triple_free_count(a,supportA) > 0, "exact A source bucket empty")
    req(8*a*a+8*b*b+6*c*c > 3*d*d+96, "quadratic pre-domain source predicate failed")

    ca=h10.component_a(d,a)
    c3=h10.component3(d,b,c)
    srem=min(16,d)+ca+c3
    qneed=K-support
    M=a+b+c
    lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed))
    upper=min((19*d)//5,3*d,3*d-(b-c))
    excluded=set()
    e_n358=3*d-(b-c)
    if b<=h-5 and support+srem==K and e_n358-M>=srem:
        excluded.add(e_n358)
    req((ca,c3,srem,qneed,M,lower,upper) == (13,9,38,38,170,208,505),
        "current-source arithmetic drift")
    req(e == first_even_not_excluded(lower,upper,excluded), "witness not at exact active e floor")
    B=19*d-5*e+1
    req(B == 2609, "normal block size drift")

    xr=h16.a0_interval(h,g,b,c)
    req(xr == (0,99), f"HPADJ x4 interval drift: {xr}")
    current=[]
    for x4 in range(xr[0],xr[1]+1):
        if (x4 & 1) != r:
            continue
        room=-int(h16.f0(h,g,b,c,x4))
        if room >= 0 and qA <= room//138:
            current.append(x4)
    req(current == list(range(1,49,2)), f"current HPADJ survivor set drift: {current}")
    req(len(current)==24, "current survivor count")

    refined=[]
    rejected=[]
    for x4 in current:
        problem=sigmod.signature_problem(
            bnb,kernel,g=g,d=d,e=e,sig=(a,b,c,t,x4,qexc)
        )
        if problem.get("structurally_infeasible"):
            rejected.append({"x4":x4,"reason":problem["reason"]})
            continue
        minimum,residual,meta=general.general_zero_center_minimum(
            problem,cert,(a,b,c,t,x4,e,d),fast
        )
        req(minimum is not None and residual is not None, f"residual minimum unexpectedly absent x4={x4}")
        if minimum <= problem["penalty_budget"]:
            refined.append(x4)
        else:
            rejected.append({"x4":x4,"reason":"residual_penalty_exceeds_budget"})

    req(refined == list(range(1,45,2)), f"refined survivor set drift: {refined}")
    req([x["x4"] for x in rejected] == [45,47], f"strict rejection set drift: {rejected}")
    req(len(refined)==22 and len(current)-len(refined)==2, "strict survivor decrement drift")

    out={
      "schema":"STAGE32_32_01_178_ACTIVE_E208_ZERO_CENTER_STRICT_WITNESS_V1",
      "status":"CURRENT_HPADJ21_SOURCE_POPULATION_STRICT_WITNESS_PASS__ZERO_MAIN_CREDIT",
      "source":{
        "hpadj21_audited_exact_head":"265fbef0a67014494fcf773af6c3a9f1b095ef95",
        "hpadj16_blob_sha1":HPADJ16_BLOB,
        "hpadj10_blob_sha1":HPADJ10_BLOB,
        "general_zero_center_blob_sha1":GENERAL_BLOB,
      },
      "active_source_floor":{
        "row_id":"g1-d192","g":g,"d":d,
        "minimum_even_e":active_floor,
        "e192_source_population_empty":True,
        "e208_source_population_nonempty":True,
        "scanned_aggregate_source_states":aggregate_states,
        "retained_floor_examples":floor_examples,
      },
      "strict_witness":{
        "e":e,"normal_block_size":B,
        "coordinates":{"x0":x0,"x1":x1,"x2":x2,"x3":x3,"x5":x5,"x6":x6,"x7":x7,"x8":x8,"x9":x9,"x10":x10},
        "aggregate":{"a":a,"b":b,"c":c,"t":t,"qA":qA,"qH":qH,"qexc":qexc,"support":support,"required_x4_parity":r},
        "current_hpadj21_surviving_x4":current,
        "zero_center_refined_surviving_x4":refined,
        "strictly_removed_x4":[x["x4"] for x in rejected],
        "current_survivor_count":len(current),
        "refined_survivor_count":len(refined),
      },
      "meaning":"The previous e192 witness was outside the current HPADJ source population. At the exact active floor e=208, this concrete canonical terminal family is genuinely in the current source population and the zero-center qexc/residual condition strictly refines the current HPADJ21 qA/parity survivor condition.",
      "next_exact_step":"Count the full e208 current-source subpopulation in the containing b-shard by exact (t,qH,support,r) H refinement, then replay the same post-mass adversarial LP with all non-e208 capacities unchanged.",
      "firewalls":{"main_credit_changed":False,"main_bound_replacement_authorized":False,"full178_complete":False,"theorem_credit_changed":False,"endpoint_credit_changed":False,"merge":False},
    }
    print("ACTIVE_E208_STRICT_WITNESS_SUMMARY="+json.dumps({
        "active_e_floor":active_floor,
        "aggregate":[a,b,c,t],
        "qA":qA,"qH":qH,"qexc":qexc,
        "current_qs":len(current),"refined_qs":len(refined),
        "strict_x4":[x["x4"] for x in rejected],
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
