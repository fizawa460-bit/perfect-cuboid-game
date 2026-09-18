#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENERAL = HERE / "verify_fibration_nef_zero_center_general_caps.py"
GENERAL_BLOB = "cc6e6aabace3bbe0d92a9cb32e659b3a7df76650"
FAST = HERE / "verify_fibration_nef_lowmass_parity_separable_picard_min.py"
FAST_BLOB = "a4f7b35e52d01d36614c7f46a592fdb7cb54518b"
HPADJ16_BLOB = "61805f8b6d661c29805b6966e2453ed411d73189"
HPADJ15_BLOB = "99ac15d18c83da050107ac7e8b113ae795ff0629"
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


def stream_sha(rows) -> str:
    h=hashlib.sha256()
    for row in rows:
        h.update(json.dumps(row,sort_keys=True,separators=(",",":")).encode())
        h.update(b"\n")
    return h.hexdigest()


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--hpadj16",type=Path,required=True)
    ap.add_argument("--hpadj15",type=Path,required=True)
    ap.add_argument("--hpadj10",type=Path,required=True)
    args=ap.parse_args()

    req(GENERAL.is_file() and blob(GENERAL)==GENERAL_BLOB,"general-cap theorem drift")
    req(FAST.is_file() and blob(FAST)==FAST_BLOB,"Picard zero-center source drift")
    req(args.hpadj16.is_file() and blob(args.hpadj16)==HPADJ16_BLOB,"HPADJ16 drift")
    req(args.hpadj15.is_file() and blob(args.hpadj15)==HPADJ15_BLOB,"HPADJ15 drift")
    req(args.hpadj10.is_file() and blob(args.hpadj10)==HPADJ10_BLOB,"HPADJ10 drift")

    fast=load_module(FAST,"stage32_178_e208_subset_fast")
    h16=load_module(args.hpadj16,"stage32_178_e208_subset_h16")
    h15=load_module(args.hpadj15,"stage32_178_e208_subset_h15")
    h10=load_module(args.hpadj10,"stage32_178_e208_subset_h10")
    cert=fast.load_certificate()

    g,d,e,h=1,192,208,96
    a,b,c=91,75,4
    M=a+b+c
    R=e-M
    support=10
    K=h10.ceil_div(d-16*g+16,4)
    ca=h10.component_a(d,a); c3=h10.component3(d,b,c)
    srem=min(16,d)+ca+c3; qneed=K-support
    lower=max(4,K,d-4*g+4,M,M+max(0,qneed))
    upper=min((19*d)//5,3*d,3*d-(b-c))
    req((M,R,K,ca,c3,srem,qneed,lower,upper)==(170,38,48,13,9,38,38,208,505),
        "fixed source arithmetic drift")
    req(8*a*a+8*b*b+6*c*c > 3*d*d+96,"quadratic source predicate")
    req(e==lower and e<=upper,"e208 source membership")
    req(h15.shard_for_b(b)==(72,83),"b-shard drift")
    B=19*d-5*e+1
    req(B==2609,"normal block size")

    # Exact A histogram for support=3: all x2,x3,x7 are positive and sum to 91.
    Ah=Counter()
    for x2 in range(1,a-1):
        for x3 in range(1,a-x2):
            x7=a-x2-x3
            if x7<=0:
                continue
            Ah[x2*x2+x3*x3+x7*x7]+=1
    Acount=sum(Ah.values())
    req(Acount==h10.triple_free_count(a,3)==4005,"A support-3 population drift")

    # Exact canonical unequal H histogram at (b,c)=(75,4), support=7.
    # Since all seven H coordinates are positive and c=x0+x6+x8+x10=4,
    # necessarily x0=x6=x8=x10=1.  Canonical unequal means x1>1.
    Hh=Counter()
    for x1 in range(2,b-1):
        rem=b-x1
        for x9 in range(1,rem):
            x5=rem-x9
            if x5<=0:
                continue
            # retained terminal-family parity x1+x8+x9+x10 == 0 mod 2
            if (x1+1+x9+1)&1:
                continue
            t=1+x1+1+x9
            qH=1+x1*x1+x5*x5+1+1+x9*x9+1
            r=(1+1+1)&1
            req(r==1,"required x4 parity drift")
            Hh[(t,qH,r)]+=1
    Hcount=sum(Hh.values())
    req(Hcount>0,"H subset empty")

    # Independent replay against the retained unequal BC construction.
    D=h10.build_pair_triple_parity(h)
    expected_by_r=[0,0]
    x0=1
    g3=c-x0
    req(g3==3,"g3 drift")
    for x1 in range(2,b-1):
        g2=b-x1
        src=D[x1&1][g2][g3]
        for x9par in (0,1):
            value=int(src[5][x9par])
            if value:
                rr=(x0&1)^(x1&1)^x9par
                expected_by_r[rr]+=value
    req(expected_by_r[0]==0 and expected_by_r[1]==Hcount,
        f"unequal H population replay drift {expected_by_r} vs {Hcount}")

    # Picard parity and residual minimum are fixed throughout this subset:
    # retained parity forces t even; b and a are odd, hence p=(1,1,0,0,0)
    # and the exact zero-center residual penalty is 1/2+1/10=3/5.
    for t,_,_ in Hh:
        req(t%2==0,"retained H emitted odd t")
        p=fast.parity_witness((a,b,c,t,0,e,d))
        req(p==(1,1,0,0,0),f"Picard parity drift t={t}: {p}")
        req(fast.membership_ok(cert,(a,b,c,t,0,e,d)+p),f"Picard witness membership drift t={t}")
    minpen=Fraction(3,5)

    xr=h16.a0_interval(h,g,b,c)
    req(xr==(0,99),f"HPADJ x4 interval drift {xr}")
    current_cache={}
    def current_x4(qA:int):
        if qA not in current_cache:
            xs=[]
            for x4 in range(xr[0],xr[1]+1):
                if (x4&1)!=1:
                    continue
                room=-int(h16.f0(h,g,b,c,x4))
                if room>=0 and qA<=room//138:
                    xs.append(x4)
            current_cache[qA]=tuple(xs)
        return current_cache[qA]

    transition=Counter()
    current_capacity=0
    refined_capacity=0
    strict_prefix_multiplicity=0
    zero_current_prefix_multiplicity=0
    prefix_count=0
    sample=None
    genus_budget=Fraction(d*d,16)+d+2-2*g

    for qA,ma in Ah.items():
        cur=current_x4(int(qA))
        qcur=len(cur)
        for (t,qH,r),mh in Hh.items():
            req(r==1,"H required parity drift")
            mult=int(ma)*int(mh)
            prefix_count+=mult
            qexc=int(qA)+int(qH)
            qref=0
            for x4 in cur:
                rho=Fraction(qexc,2)+Fraction((d//2-2*x4-t)**2,12)
                if rho+minpen<=genus_budget:
                    qref+=1
            req(qref<=qcur,"refinement weakened current HPADJ survivor count")
            transition[(qcur,qref)]+=mult
            current_capacity+=mult*qcur
            refined_capacity+=mult*qref
            if qref<qcur:
                strict_prefix_multiplicity+=mult
                if sample is None:
                    sample={"qA":int(qA),"qH":int(qH),"t":int(t),"multiplicity":mult,
                            "current_qs":qcur,"refined_qs":qref}
            if qcur==0:
                zero_current_prefix_multiplicity+=mult

    req(prefix_count==Acount*Hcount,"factorized prefix population mismatch")
    req(current_capacity>refined_capacity,"subset produced no strict survivor-capacity gain")
    req(strict_prefix_multiplicity>0 and sample is not None,"subset strictness accounting")
    req((2761 in Ah) and Hh[(52,1879,1)]>0,"retained strict witness state missing")
    witness_cur=len(current_x4(2761))
    witness_ref=0
    for x4 in current_x4(2761):
        rho=Fraction(4640,2)+Fraction((96-2*x4-52)**2,12)
        if rho+minpen<=genus_budget:
            witness_ref+=1
    req((witness_cur,witness_ref)==(24,22),"e208 concrete witness no longer reproduced")

    rows=[
      {"current_qs":int(qc),"refined_qs":int(qr),"prefix_multiplicity":str(m)}
      for (qc,qr),m in sorted(transition.items())
    ]
    out={
      "schema":"STAGE32_32_01_178_ACTIVE_E208_B75_UNEQUAL_SUBSET_V1",
      "status":"EXACT_CURRENT_SOURCE_SUBSET_STRICT_REFINEMENT__ZERO_MAIN_CREDIT",
      "source":{
        "row_id":"g1-d192","g":g,"d":d,"e":e,
        "b_shard":[72,83],
        "aggregate":{"a":a,"b":b,"c":c},
        "canonical_branch":"x0<x1",
        "support":10,
        "normal_block_size":B,
      },
      "population":{
        "A_support3_ordered_triples":Acount,
        "H_support7_canonical_unequal_prefixes":Hcount,
        "factorized_exceptional_prefixes":prefix_count,
        "pre_domain_terminal_mass":str(prefix_count*B),
        "current_zero_survivor_prefix_multiplicity":zero_current_prefix_multiplicity,
      },
      "refinement":{
        "current_hpadj21_survivor_terminal_capacity":str(current_capacity),
        "zero_center_refined_survivor_terminal_capacity":str(refined_capacity),
        "strict_capacity_reduction":str(current_capacity-refined_capacity),
        "strict_prefix_multiplicity":str(strict_prefix_multiplicity),
        "transition_histogram":rows,
        "transition_stream_sha256":stream_sha(rows),
        "concrete_witness_reproduced":{"qA":2761,"qH":1879,"t":52,"current_qs":24,"refined_qs":22},
        "sample_strict_state":sample,
      },
      "semantics":{
        "same_current_source_population":True,
        "only_survivor_capacity_tightened":True,
        "post_mass_adversarial_lp_not_yet_replayed":True,
        "main_bound_improvement_claimed":False,
        "next_exact_step":"Replay the containing (g1-d192,b=72..83) HPADJ21 cell LP with only this exact subset's (q_s,B) capacities replaced by the refined transition histogram; all other capacities remain unchanged.",
      },
      "firewalls":{"main_credit_changed":False,"main_bound_replacement_authorized":False,"full178_complete":False,"theorem_credit_changed":False,"endpoint_credit_changed":False,"merge":False},
    }
    print("ACTIVE_E208_B75_SUBSET_SUMMARY="+json.dumps({
      "A":Acount,"H":Hcount,"prefixes":prefix_count,
      "pre_mass":str(prefix_count*B),
      "current_capacity":str(current_capacity),
      "refined_capacity":str(refined_capacity),
      "reduction":str(current_capacity-refined_capacity),
      "strict_prefix_multiplicity":str(strict_prefix_multiplicity),
      "transition_sha256":out["refinement"]["transition_stream_sha256"],
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
