#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
PARENT=HERE/"verify_hpadj21_g1d192_b36_47_cell_replay.py"
PARENT_BLOB="3cd275cef9412cce549235781a94e686d154c132"
GENERAL=HERE/"verify_fibration_nef_zero_center_general_caps.py"
GENERAL_BLOB="cc6e6aabace3bbe0d92a9cb32e659b3a7df76650"
FAST=HERE/"verify_fibration_nef_lowmass_parity_separable_picard_min.py"
FAST_BLOB="a4f7b35e52d01d36614c7f46a592fdb7cb54518b"
E192V2=HERE/"verify_fibration_nef_active_e192_strict_witness.py"
E192V2_BLOB="5b902ac35834b95a252b809e510900a252c2ceff"
CORRECTION=HERE/"CURRENT-SOURCE-DOMAIN-CORRECTION.json"
CORRECTION_BLOB="ff6192106a99cb89138fc3e659c09c9a2c021e35"

ROW_WORKER_BLOB="68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
HPADJ18_BLOB="09c3a97ca47f2602b547efc572a3ddfee1d3437f"
HPADJ16_BLOB="61805f8b6d661c29805b6966e2453ed411d73189"
HPADJ15_BLOB="99ac15d18c83da050107ac7e8b113ae795ff0629"
HPADJ10_BLOB="eebeb47f91df22461c33e9974d63aceca4da3b52"
ROW_CERT_CANON="ba356db05dfb3699c7a13b59698d30cad9599a32e3bf409f6e6d5de45c42ddca"

EXPECTED_PRE=207312456066801657003
EXPECTED_POST=85212642937627265785
EXPECTED_NUM=1824391732631330409367
EXPECTED_DEN=883
EXPECTED_FLOOR=2066128802526988006
TARGET_B=2689


def req(v:bool,msg:str)->None:
    if not v: raise SystemExit("FAIL: "+msg)


def blob(path:Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def canonical(obj:dict)->str:
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def load_module(path:Path,name:str):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None: raise RuntimeError(path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod


def stream_sha(rows)->str:
    h=hashlib.sha256()
    for row in rows:
        h.update(json.dumps(row,sort_keys=True,separators=(",",":")).encode());h.update(b"\n")
    return h.hexdigest()


def reconstruct_caps(parent,h16,h15,h10):
    g,d,h=1,192,96
    K=h10.ceil_div(d-16*g+16,4);legacy=4
    BC=h10.build_bc_exact_parity(h)
    A=parent.build_A(h,h10)
    diffs=defaultdict(Counter)
    for b in range(36,48):
      for c in range(h+1):
        bcv=BC[b][c]
        if not any(any(pair) for pair in bcv):continue
        c3=h10.component3(d,b,c)
        if c3<0:continue
        xr=h16.a0_interval(h,g,b,c)
        caps_r=[[],[]]
        if xr is not None:
            for x4 in range(xr[0],xr[1]+1):
                room=-int(h16.f0(h,g,b,c,x4))
                req(room>=0,"a0 interval contains negative room")
                caps_r[x4&1].append(room//138)
            caps_r[0].sort();caps_r[1].sort()
        for a in range(h+1):
            ca=h10.component_a(d,a)
            if ca<0:continue
            M=a+b+c;srem=min(16,d)+ca+c3
            qdist={}
            for sa in range(4):
              if not A[a][sa]:continue
              for r in (0,1):
                ctr=Counter();arr=caps_r[r]
                for qA,mult in A[a][sa].items():
                    qs=len(arr)-bisect.bisect_left(arr,int(qA))
                    ctr[qs]+=int(mult)
                qdist[(sa,r)]=ctr
            for sbc,pair in enumerate(bcv):
              for r in (0,1):
                left=int(pair[r])
                if not left:continue
                for sa in range(4):
                    ctr=qdist.get((sa,r))
                    if not ctr:continue
                    support=sbc+sa
                    qneed=K-support
                    if qneed>0 and srem<qneed:continue
                    lower=max(legacy,K,d-4*g+4,M,M+max(0,qneed))
                    upper=min((19*d)//5,3*d,3*d-(b-c))
                    if lower>upper:continue
                    excluded=set();e_n358=3*d-(b-c)
                    if b<=h-5 and support+srem==K and e_n358-M>=srem:
                        excluded.add(e_n358)
                    for qs,amult in ctr.items():
                        count=left*int(amult)
                        if count: parent.add_range(diffs[int(qs)],lower,upper,count,excluded)
    req(diffs,"empty target cell")
    caps=defaultdict(int)
    min_e=min(k for diff in diffs.values() for k in diff)
    max_e=max(k for diff in diffs.values() for k in diff)
    if min_e%2:min_e+=1
    if max_e%2:max_e-=1
    for qs,diff in diffs.items():
        running=0
        for e in range(min_e,max_e+1,2):
            running+=diff.get(e,0)
            if running:
                B=19*d-5*e+1
                req(B>0 and B%2==1,f"normal B drift e={e}")
                caps[(int(qs),B)]+=running*B
    req(sum(caps.values())==EXPECTED_PRE,"baseline pre mass drift")
    return caps


def positive_A_hist(a:int)->Counter[int]:
    out=Counter()
    for x2 in range(1,a-1):
        for x3 in range(1,a-x2):
            x7=a-x2-x3
            if x7>0: out[x2*x2+x3*x3+x7*x7]+=1
    return out


def unequal_positive_H_hist(*,b:int,c:int)->Counter[tuple[int,int,int]]:
    # Exact DP for canonical x0<x1 with all seven H coordinates positive.
    # State=(partial_b,partial_c,t,qH,r), where
    # r=(x0+x8+x10) mod 2 is the required normal-coordinate parity.
    states=Counter()
    for x0 in range(1,c):
        for x1 in range(x0+1,b):
            states[(x1,x0,x0+x1,x0*x0+x1*x1,x0&1)]+=1

    # x5,x6,x8,x9,x10: (db,dc,dt,toggle_r)
    specs=((1,0,0,0),(0,1,1,0),(0,1,0,1),(1,0,1,0),(0,1,0,1))
    for db,dc,dt,toggle in specs:
        nxt=Counter()
        for (pb,pc,t,q,r),mult in states.items():
            room=(b-pb) if db else (c-pc)
            for value in range(1,room+1):
                nb=pb+db*value
                nc=pc+dc*value
                if nb>b or nc>c: continue
                nxt[(nb,nc,t+dt*value,q+value*value,r^((value&1) if toggle else 0))]+=mult
        states=nxt

    out=Counter()
    for (pb,pc,t,q,r),mult in states.items():
        if pb==b and pc==c and ((c-t)&1)==0:
            out[(t,q,r)]+=mult
    return out

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--row-worker",type=Path,required=True)
    ap.add_argument("--hpadj18",type=Path,required=True)
    ap.add_argument("--hpadj16",type=Path,required=True)
    ap.add_argument("--hpadj15",type=Path,required=True)
    ap.add_argument("--hpadj10",type=Path,required=True)
    ap.add_argument("--row-cert",type=Path,required=True)
    args=ap.parse_args()

    for label,path,expected in (
      ("parent cell replay",PARENT,PARENT_BLOB),("general zero-center theorem",GENERAL,GENERAL_BLOB),
      ("Picard zero-center source",FAST,FAST_BLOB),("corrected e192 witness",E192V2,E192V2_BLOB),
      ("current-source correction",CORRECTION,CORRECTION_BLOB),
      ("row worker",args.row_worker,ROW_WORKER_BLOB),("HPADJ18",args.hpadj18,HPADJ18_BLOB),
      ("HPADJ16",args.hpadj16,HPADJ16_BLOB),("HPADJ15",args.hpadj15,HPADJ15_BLOB),
      ("HPADJ10",args.hpadj10,HPADJ10_BLOB)):
        req(path.is_file() and blob(path)==expected,f"{label} drift")

    corr=json.loads(CORRECTION.read_text())
    req(corr["corrected_authority"]["exact_active_even_e_floor"]==192,"current-source correction e floor drift")
    req(corr["corrected_authority"]["e192_current_source_nonempty"] is True,"e192 source correction drift")

    row=json.loads(args.row_cert.read_text())
    req(row.get("canonical_sha256_without_this_field")==ROW_CERT_CANON and canonical(row)==ROW_CERT_CANON,
        "row certificate canonical drift")
    rec=[x for x in row["cell_records"] if x["b_interval"]==[36,47]]
    req(len(rec)==1,"target row cell missing")
    rec=rec[0]
    req((rec["pre_mass"],rec["post_mass"],rec["hpadj21_num"],rec["hpadj21_den"],rec["hpadj21_floor"])==
        (EXPECTED_PRE,EXPECTED_POST,EXPECTED_NUM,EXPECTED_DEN,EXPECTED_FLOOR),"target cell receipt drift")

    parent=load_module(PARENT,"stage32_178_e192_ref_parent")
    h16=load_module(args.hpadj16,"stage32_178_e192_ref_h16")
    h15=load_module(args.hpadj15,"stage32_178_e192_ref_h15")
    h10=load_module(args.hpadj10,"stage32_178_e192_ref_h10")
    fast=load_module(FAST,"stage32_178_e192_ref_fast")
    cert=fast.load_certificate()

    caps=reconstruct_caps(parent,h16,h15,h10)
    old_obj,old_total,old_cutoff,old_trace,_=parent.greedy(caps,EXPECTED_POST)
    req(old_total==EXPECTED_PRE and old_obj==Fraction(EXPECTED_NUM,EXPECTED_DEN),"baseline LP drift")
    req(old_cutoff==Fraction(14,883),"baseline cutoff drift")

    g,d,e,h=1,192,192,96
    a,b,c=45,45,60
    supportA,supportH,support=3,7,10
    K=h10.ceil_div(d-16*g+16,4)
    ca=h10.component_a(d,a);c3=h10.component3(d,b,c)
    srem=min(16,d)+ca+c3;qneed=K-support;M=a+b+c
    lower=max(4,K,d-4*g+4,M,M+max(0,qneed))
    upper=min((19*d)//5,3*d,3*d-(b-c))
    excluded=set();e_n358=3*d-(b-c)
    if b<=h-5 and support+srem==K and e_n358-M>=srem:excluded.add(e_n358)
    req((K,ca,c3,srem,qneed,M,lower,upper)==(48,13,9,38,38,150,192,576),
        "e192 source arithmetic drift")
    req(e==lower and e not in excluded and h15.shard_for_b(b)==(36,47),"e192 source membership drift")
    B=19*d-5*e+1
    req(B==TARGET_B,"target normal block drift")

    Ah=positive_A_hist(a)
    req(sum(Ah.values())==h10.triple_free_count(a,supportA)==946,"A support-3 histogram population drift")
    Hh=unequal_positive_H_hist(b=b,c=c)
    Hcount=sum(Hh.values())
    req(all((t&1)==0 for (t,_qH,_r) in Hh),"H parity quotient drift")

    # Independently recover the same unequal H support population from HPADJ10 D.
    D=h10.build_pair_triple_parity(h)
    by_r=[0,0]
    for x0 in range(1,c-2):
      for x1 in range(x0+1,min(b-2,95)+1):
        g2=b-x1;g3=c-x0
        if g2<0 or g3<0 or g2>h or g3>h:continue
        src=D[x1&1][g2][g3]
        for x9par in (0,1):
            value=int(src[5][x9par])
            if value:
                r=(x0&1)^(x1&1)^x9par
                by_r[r]+=value
    hist_by_r=[sum(m for (t,q,r),m in Hh.items() if r==rr) for rr in (0,1)]
    req(by_r==hist_by_r,f"H D-replay drift {by_r} != {hist_by_r}")

    prefix_total=sum(Ah.values())*Hcount

    # For this fixed aggregate R=42 and all residual caps are 42. Retained
    # parity c==t mod2 gives t even; a,b odd therefore p=(1,1,0,0,0),
    # exact zero-center residual penalty = 1/2+1/10 = 3/5.
    R=e-M
    req(R==42,"remaining mass drift")
    for t,_qH,_r in Hh:
        p=fast.parity_witness((a,b,c,t,0,e,d))
        req(p==(1,1,0,0,0),f"Picard parity drift t={t}: {p}")
        req(fast.membership_ok(cert,(a,b,c,t,0,e,d)+p),f"Picard witness membership drift t={t}")
    minpen=Fraction(3,5)
    genus_budget=Fraction(d*d,16)+d+2-2*g

    xr=h16.a0_interval(h,g,b,c)
    req(xr is not None,"target b,c has no current q interval")
    current_cache={}
    def current_x4(qA:int,r:int):
        key=(qA,r)
        if key not in current_cache:
            xs=[]
            for x4 in range(xr[0],xr[1]+1):
                if (x4&1)!=r:continue
                room=-int(h16.f0(h,g,b,c,x4))
                req(room>=0,"a0 interval negative room")
                if qA<=room//138:xs.append(x4)
            current_cache[key]=tuple(xs)
        return current_cache[key]

    limit_cache={}
    def qh_limits(qA:int,t:int,r:int):
        key=(qA,t,r)
        if key not in limit_cache:
            vals=[]
            for x4 in current_x4(qA,r):
                static_rho=Fraction((d//2-2*x4-t)**2,12)
                exact_cut=2*(genus_budget-static_rho-minpen)
                vals.append(exact_cut.numerator//exact_cut.denominator-qA)
            vals.sort()
            limit_cache[key]=tuple(vals)
        return limit_cache[key]

    transition=Counter()
    current_survivor_capacity=0
    refined_survivor_capacity=0
    strict_prefix_multiplicity=0
    high_ratio_strict_prefix_multiplicity=0
    cutoff=Fraction(14,883)
    for qA,ma in Ah.items():
      for (t,qH,r),mh in Hh.items():
        mult=int(ma)*int(mh)
        qc=len(current_x4(int(qA),int(r)))
        limits=qh_limits(int(qA),int(t),int(r))
        qr=len(limits)-bisect.bisect_left(limits,int(qH))
        req(0<=qr<=qc,"zero-center refinement weakened current q survivor count")
        transition[(qc,qr)]+=mult
        current_survivor_capacity+=mult*qc
        refined_survivor_capacity+=mult*qr
        if qr<qc:
            strict_prefix_multiplicity+=mult
            if Fraction(qc,B)>=cutoff:
                high_ratio_strict_prefix_multiplicity+=mult

    req(sum(transition.values())==prefix_total,"transition prefix accounting drift")
    req(current_survivor_capacity>refined_survivor_capacity,"subset has no strict refinement")
    req(high_ratio_strict_prefix_multiplicity>0,"subset strictness does not touch selected LP ratios")

    newcaps=defaultdict(int,caps)
    moved_blocks=0
    rows=[]
    for (qc,qr),blocks in sorted(transition.items()):
        blocks=int(blocks)
        rows.append({"current_qs":int(qc),"refined_qs":int(qr),"prefix_blocks":str(blocks)})
        if qc==qr:continue
        delta=blocks*B
        req(newcaps[(qc,B)]>=delta,
            f"subset removal exceeds current bin {(qc,B)}: {delta}>{newcaps[(qc,B)]}")
        newcaps[(qc,B)]-=delta
        newcaps[(qr,B)]+=delta
        moved_blocks+=blocks

    req(sum(newcaps.values())==EXPECTED_PRE,"partial replacement changed pre-domain mass")
    req(all(v>=0 for v in newcaps.values()),"partial replacement produced negative capacity")

    new_obj,new_total,new_cutoff,new_trace,_=parent.greedy(newcaps,EXPECTED_POST)
    req(new_total==EXPECTED_PRE,"refined LP total capacity drift")
    req(new_obj<old_obj,"e192 zero-center partial replacement did not strictly improve LP rational objective")
    old_floor=old_obj.numerator//old_obj.denominator
    new_floor=new_obj.numerator//new_obj.denominator
    req(old_floor==EXPECTED_FLOOR,"old floor drift")
    req(new_floor<=old_floor,"refined floor weakened")
    floor_improvement=old_floor-new_floor

    out={
      "schema":"STAGE32_32_01_178_HPADJ21_G1D192_B36_47_E192_ZERO_CENTER_REFINEMENT_V1",
      "status":"EXACT_CURRENT_CELL_PARTIAL_REPLACEMENT_STRICT_CANDIDATE__ZERO_MAIN_CREDIT__HOSTILE_AUDIT_REQUIRED",
      "source":{
        "row_id":"g1-d192","g":g,"d":d,"b_interval":[36,47],"e":e,
        "aggregate":{"a":a,"b":b,"c":c},"canonical_branch":"x0<x1","support":support,
        "row_certificate_canonical":ROW_CERT_CANON,
        "parent_cell_replay_blob":PARENT_BLOB,"general_zero_center_blob":GENERAL_BLOB,
        "corrected_e192_witness_blob":E192V2_BLOB,"source_domain_correction_blob":CORRECTION_BLOB,
      },
      "subset_population":{
        "A_support3_prefixes":sum(Ah.values()),"H_unequal_support7_prefixes":Hcount,
        "exceptional_prefix_blocks":str(prefix_total),"normal_block_size":B,
        "pre_domain_terminal_mass":str(prefix_total*B),
        "transition_stream_sha256":stream_sha(rows),
      },
      "survivor_refinement":{
        "current_survivor_capacity":str(current_survivor_capacity),
        "refined_survivor_capacity":str(refined_survivor_capacity),
        "strict_survivor_capacity_reduction":str(current_survivor_capacity-refined_survivor_capacity),
        "strict_prefix_multiplicity":str(strict_prefix_multiplicity),
        "high_ratio_strict_prefix_multiplicity":str(high_ratio_strict_prefix_multiplicity),
        "moved_prefix_blocks":str(moved_blocks),
      },
      "cell_lp":{
        "pre_mass":str(EXPECTED_PRE),"post_mass":str(EXPECTED_POST),
        "old_objective_num":old_obj.numerator,"old_objective_den":old_obj.denominator,
        "old_floor":old_floor,"old_cutoff":str(old_cutoff),
        "new_objective_num":new_obj.numerator,"new_objective_den":new_obj.denominator,
        "new_floor":new_floor,"new_cutoff":str(new_cutoff),
        "floor_improvement":floor_improvement,
        "strict_rational_improvement":str(old_obj-new_obj),
      },
      "semantics":{
        "same_current_pre_domain_population":True,
        "same_certified_post_mass":True,
        "only_exact_e192_unequal_subset_survivor_capacity_replaced":True,
        "all_other_current_capacities_unchanged":True,
        "additive_cross_route_subtraction":False,
        "main_bound_replacement_performed":False,
        "hostile_audit_required_before_any_consumption":True,
      },
      "firewalls":{"main_credit_changed":False,"main_bound_replacement_authorized":False,
                   "full178_complete":False,"theorem_credit_changed":False,
                   "endpoint_credit_changed":False,"merge":False},
    }
    print("HPADJ21_E192_ZERO_CENTER_REFINEMENT_SUMMARY="+json.dumps({
      "prefix_blocks":str(prefix_total),
      "current_survivor_capacity":str(current_survivor_capacity),
      "refined_survivor_capacity":str(refined_survivor_capacity),
      "survivor_reduction":str(current_survivor_capacity-refined_survivor_capacity),
      "high_ratio_strict_prefixes":str(high_ratio_strict_prefix_multiplicity),
      "old_floor":old_floor,"new_floor":new_floor,"floor_improvement":floor_improvement,
      "old_cutoff":str(old_cutoff),"new_cutoff":str(new_cutoff),
      "transition_sha256":out["subset_population"]["transition_stream_sha256"],
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
