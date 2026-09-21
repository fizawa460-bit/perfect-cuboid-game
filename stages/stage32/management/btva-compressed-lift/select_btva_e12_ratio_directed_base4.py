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

ROOT = Path(__file__).resolve().parents[4]
REF = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-V43-HPADJ21-ROW-REFERENCE.json"
REF_BLOB = "c7c01eb27c4e80598d32261cb498fdccc7264ba9"
REF_CANON = "53e9dd57501b4ed10cd1a60e172c7ac1e255eba46a7b4d592847ba5387a2341d"
QBIN_RETAINED = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-E12-HPADJ21-EXACT-QBIN-JOINT-RETAINED.json"
QBIN_RETAINED_BLOB = "35b94bf7aa6635130938327eb316e4cf6fc30495"
QBIN_RETAINED_CANON = "f264f0f57e0e566227928ce5359cf4698f951764423a88a60421571ebfa6f72e"
INDEXER = ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py"
INDEXER_BLOB = "4fb0a8dd34909494bd62646373e42877ed7a3c9e"
HPADJ21_HEAD = "33f63a4c0bb3dde9d56efd895f4e8eb19d9217e2"
ROW_WORKER_REL = Path("stages/stage32-ex5/hpadj-21_ex5/run_full_hist_row.py")
ROW_WORKER_BLOB = "68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"

ROW_INDEX=23
ROW_ID="g0-d008"
G=0
D=8
E=12
H=4
B=93
SELECT_COUNT=16
TOP16={
    (4,4,4,4),(4,5,3,5),(5,3,4,4),(5,4,3,5),
    (3,5,4,6),(3,4,5,5),(6,3,3,3),(6,4,2,4),
    (4,4,4,6),(4,3,5,3),(3,6,3,7),(3,3,6,4),
    (4,3,5,5),(4,6,2,6),(2,6,4,6),(2,5,5,5),
}
TOP16_SHA256="9df7cc14ed5eecf755ce7a6f9d30e7b392f19c2f2393054131b02a5a550e8f27"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: "+msg)


def blob(path: Path) -> str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def load_module(path: Path, name: str):
    spec=importlib.util.spec_from_file_location(name,path)
    req(spec is not None and spec.loader is not None,"cannot load "+str(path))
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod


def lock_json(path: Path, expected_blob: str, expected_canon: str) -> dict:
    req(blob(path)==expected_blob,path.name+" blob drift")
    obj=json.loads(path.read_text(encoding="utf-8"))
    stored=obj.get("canonical_sha256_without_this_field")
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    req(stored==expected_canon and csha(body)==expected_canon,path.name+" canonical drift")
    return obj


def block_coordinates(h16, x: tuple[int,...]):
    a=x[2]+x[3]+x[7]
    b=x[1]+x[5]+x[9]
    c=x[0]+x[6]+x[8]+x[10]
    t=x[0]+x[1]+x[6]+x[9]
    r=(x[0]+x[8]+x[10])&1
    sa=int(x[2]>0)+int(x[3]>0)+int(x[7]>0)
    qA=x[2]*x[2]+x[3]*x[3]+x[7]*x[7]
    if not (0<=a<=H and 0<=b<=H and 0<=c<=H):
        return a,b,c,t,r,sa,qA,None
    xr=h16.a0_interval(H,G,b,c)
    if xr is None:
        return a,b,c,t,r,sa,qA,None
    caps=[[],[]]
    left,right=xr
    for xx4 in range(left,right+1):
        room=-h16.f0(H,G,b,c,xx4)
        req(room>=0,"q interval construction")
        caps[xx4&1].append(room//138)
    caps[0].sort();caps[1].sort()
    s=len(caps[r])-bisect.bisect_left(caps[r],qA)
    return a,b,c,t,r,sa,qA,s


def objective(h18, p15, cells, caps_by_interval):
    total=Fraction(0,1)
    floors=0
    post={}
    for interval in p15.PLANNED:
        P=sum(caps_by_interval[interval].values())
        M0=int(cells[(interval,G,D)]["post_mass"])
        M=min(M0,P)
        obj,_,_,_=h18.optimize_cell_exact_predomain(caps_by_interval[interval],M)
        total+=obj
        floors+=obj.numerator//obj.denominator
        post[interval]=M
    return total,floors,post


def subtract_key(caps_by_interval, key_caps):
    out={i:dict(v) for i,v in caps_by_interval.items()}
    for interval,rem in key_caps.items():
        for k,v in rem.items():
            req(k in out[interval] and out[interval][k]>=v,f"removal exceeds cap {(interval,k,v)}")
            out[interval][k]-=v
            if out[interval][k]==0:
                del out[interval][k]
    return out


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--hpadj21-root",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()

    ref=lock_json(REF,REF_BLOB,REF_CANON)
    retained=lock_json(QBIN_RETAINED,QBIN_RETAINED_BLOB,QBIN_RETAINED_CANON)
    req(retained["result"]["joint_exact_qbin_conservative_row_floor"]==448261,"retained qbin floor")
    req(retained["result"]["row_floor_tightening_candidate"]==170,"retained qbin tightening")
    req(csha(sorted([list(x) for x in TOP16]))==TOP16_SHA256,"top16 digest")

    req(blob(INDEXER)==INDEXER_BLOB,"indexer drift")
    sys.path.insert(0,str(INDEXER.parent))
    idxmod=load_module(INDEXER,"s32_e12_ratio_selector_indexer")
    indexer=idxmod.CompressedTerminalIndexer(E,D)
    req(indexer.normal_budget==92 and int(indexer.exceptional_count)==164282,"e12 census boundary")

    hp_root=args.hpadj21_root.resolve()
    row_worker=hp_root/ROW_WORKER_REL
    req(row_worker.is_file() and blob(row_worker)==ROW_WORKER_BLOB,"HPADJ21 row worker drift")
    rw=load_module(row_worker,"s32_e12_ratio_selector_row")
    p=rw.load_pilot();h20=p.load_parent();h19=h20.load_parent();h18=h19.load_parent();h17=h18.load_parent();h16=h17.load_parent()
    p15=h16.load_module(h16.PARENT,h16.PARENT_BLOB,"s32_e12_ratio_selector_h15")
    p14=p15.load_parent();counter=p14.load_counter()
    manifest=counter.load_locked_json(p14.MANIFEST,p14.LOCKS["manifest_blob"],p14.LOCKS["manifest_canonical"],"FULL178 manifest")
    rows=counter.manifest_rows(manifest)
    row_id,g,d=rows[ROW_INDEX]
    req((row_id,int(g),int(d))==(ROW_ID,G,D),"row identity")

    cells,BC=p.exact_pilot_cells(p15,p14,counter,[(ROW_ID,G,D)])
    profiles,_,_=p.full_profiles(H,counter,h19)
    A=[[sum(mult for _,mult in profiles[a][sa]) for sa in range(4)] for a in range(H+1)]
    full_caps={interval:defaultdict(int) for interval in p15.PLANNED}
    K=counter.ceil_div(D-16*G+16,4)

    for b in range(H+1):
        interval=p15.shard_for_b(b)
        for c in range(H+1):
            bcv=BC[b][c]
            if not any(any(pair) for pair in bcv): continue
            c3=counter.component3(D,b,c)
            if c3<0: continue
            exact_surv=p.full_survivors(h16,profiles,H,G,b,c)
            for a in range(H+1):
                if not any(A[a]): continue
                M=a+b+c;ca=counter.component_a(D,a)
                if ca<0: continue
                srem=min(16,D)+ca+c3
                for sbc,pair in enumerate(bcv):
                    for r in (0,1):
                        left=int(pair[r])
                        if not left: continue
                        for sa,right in enumerate(A[a]):
                            if not right: continue
                            fi=exact_surv[a][sa];req(fi is not None,"missing q profile")
                            support=sbc+sa;qneed=K-support
                            if qneed>0 and srem<qneed: continue
                            lower=max(8,K,D-4*G+4,M,M+max(0,qneed))
                            upper=min((19*D)//5,3*D,3*D-(b-c))
                            if lower>upper: continue
                            excluded=set();e_n358=3*D-(b-c)
                            if b<=H-5 and support+srem==K and e_n358-M>=srem: excluded.add(e_n358)
                            lo=lower if lower%2==0 else lower+1;hi=upper if upper%2==0 else upper-1
                            for e in range(lo,hi+1,2):
                                if e in excluded: continue
                                BB=19*D-5*e+1
                                for s0,s1,mult in fi["tiers"]:
                                    ss=s0 if r==0 else s1
                                    full_caps[interval][(int(ss),BB)]+=left*int(mult)*BB

    for interval in p15.PLANNED:
        req(sum(full_caps[interval].values())==int(cells[(interval,G,D)]["pre_mass"]),"full caps replay")

    raw_blocks=Counter()
    pre_caps_by_key=defaultdict(lambda:defaultdict(Counter))
    support_by_key=defaultdict(Counter)
    for erank in range(int(indexer.exceptional_count)):
        x=tuple(int(v) for v in indexer.unrank(erank*B))
        req(x[4]==0,"x4 stride")
        a,b,c,t,r,sa,qA,s=block_coordinates(h16,x)
        key=(a,b,c,t)
        raw_blocks[key]+=1
        if s is None: continue
        c3=counter.component3(D,b,c);ca=counter.component_a(D,a)
        if c3<0 or ca<0: continue
        support=sum(1 for j,v in enumerate(x) if j!=4 and v>0)
        srem=min(16,D)+ca+c3;qneed=K-support
        if qneed>0 and srem<qneed: continue
        M=a+b+c
        lower=max(8,K,D-4*G+4,M,M+max(0,qneed))
        upper=min((19*D)//5,3*D,3*D-(b-c))
        if not (lower<=E<=upper): continue
        e_n358=3*D-(b-c)
        if b<=H-5 and support+srem==K and e_n358-M>=srem and E==e_n358: continue
        interval=p15.shard_for_b(b)
        pre_caps_by_key[key][interval][(int(s),B)]+=B
        support_by_key[key][support]+=1

    top_caps={i:Counter() for i in p15.PLANNED}
    for key in TOP16:
        for interval,caps in pre_caps_by_key.get(key,{}).items():
            top_caps[interval].update(caps)
    req(sum(sum(v.values()) for v in top_caps.values())==129177,"top16 overlap replay")

    caps_after_top=subtract_key(full_caps,top_caps)
    base_obj,base_floor,base_post=objective(h18,p15,cells,caps_after_top)
    req(base_floor==448261,"post-top16 exact qbin floor replay")

    remaining={k for k in pre_caps_by_key if k not in TOP16 and sum(sum(c.values()) for c in pre_caps_by_key[k].values())>0}
    selected=[]
    current_caps=caps_after_top
    current_obj=base_obj
    current_floor=base_floor

    for step in range(SELECT_COUNT):
        best=None
        for key in remaining:
            test=subtract_key(current_caps,pre_caps_by_key[key])
            obj,floor,post=objective(h18,p15,cells,test)
            delta=current_obj-obj
            overlap=sum(sum(c.values()) for c in pre_caps_by_key[key].values())
            score=(delta, current_floor-floor, overlap, raw_blocks[key]*B, tuple(-v for v in key))
            if best is None or score>best[0]:
                best=(score,key,test,obj,floor,post)
        req(best is not None,"selector exhausted")
        score,key,test,obj,floor,post=best
        delta=score[0]
        selected.append({
            "selection_order":step,
            "base4":list(key),
            "raw_exceptional_blocks":int(raw_blocks[key]),
            "raw_terminal_mass":int(raw_blocks[key])*B,
            "hpadj21_predomain_overlap_terminal_mass":int(score[2]),
            "marginal_rational_improvement_num":delta.numerator,
            "marginal_rational_improvement_den":delta.denominator,
            "marginal_cellwise_floor_improvement":current_floor-floor,
            "cumulative_hypothetical_row_floor_if_all_selected_unsat":floor,
            "removed_qbin_terminal_mass":[
                {"b_interval":list(interval),"bins":[{"s":int(k[0]),"B":int(k[1]),"terminals":int(v)} for k,v in sorted(caps.items())]}
                for interval,caps in sorted(pre_caps_by_key[key].items())
            ],
            "support_histogram":[{"support":int(s),"blocks":int(n)} for s,n in sorted(support_by_key[key].items())],
        })
        current_caps=test;current_obj=obj;current_floor=floor;remaining.remove(key)

    selected_keys=[tuple(r["base4"]) for r in selected]
    req(len(selected_keys)==SELECT_COUNT and not (set(selected_keys)&TOP16),"selector overlap top16")
    out={
      "schema":"STAGE32_MAIN_BTVA_D8_E12_RATIO_DIRECTED_SELECTOR_V1",
      "stage":32,
      "status":"EXACT_HPADJ21_RATIO_DIRECTED_BTVA_SELECTOR_ZERO_CREDIT",
      "target":{"row_id":ROW_ID,"row_index":ROW_INDEX,"g":G,"d":D,"e":E,"selected_count":SELECT_COUNT},
      "baseline":{"top16_already_unsat":True,"top16_exact_qbin_row_floor":base_floor,"top16_row_tightening_candidate":170},
      "selection_rule":"Greedy maximize exact rational HPADJ21 objective decrease after top16 exact-qbin removal; tie by integer floor decrease, exact HPADJ predomain overlap mass, raw e12 mass, then base4.",
      "selected":selected,
      "hypothetical_if_all_selected_unsat":{
        "row_floor":current_floor,
        "additional_tightening_beyond_top16":base_floor-current_floor,
        "total_tightening_vs_hpadj21_baseline":448431-current_floor,
        "selected_raw_terminal_mass":sum(r["raw_terminal_mass"] for r in selected),
        "selected_hpadj21_predomain_overlap_terminal_mass":sum(r["hpadj21_predomain_overlap_terminal_mass"] for r in selected),
      },
      "population":{"e12_base4_key_count":len(raw_blocks),"hpadj21_predomain_base4_key_count":len(pre_caps_by_key),"top16_key_count":16},
      "source_locks":{
        "e12_reference_blob_sha1":REF_BLOB,"e12_reference_canonical_sha256":REF_CANON,
        "qbin_retained_blob_sha1":QBIN_RETAINED_BLOB,"qbin_retained_canonical_sha256":QBIN_RETAINED_CANON,
        "compressed_terminal_indexer_blob_sha1":INDEXER_BLOB,
        "hpadj21_head":HPADJ21_HEAD,"hpadj21_row_worker_blob_sha1":ROW_WORKER_BLOB,
        "top16_key_stream_sha256":TOP16_SHA256,
      },
      "semantics":{
        "selector_is_not_unsat_proof":True,
        "hypothetical_floor_assumes_selected_keys_later_prove_btva_unsat":True,
        "prior_hpadj08_removed_identity_handled_adversarially":True,
        "no_statistical_independence_assumed":True,
        "no_additive_subtraction_used":True,
      },
      "firewalls":{
        "main_pruning_credit":False,"receiver_credit":False,"effectivity_credit":False,
        "theorem_credit":False,"endpoint_credit":False,"full178_complete":False,
        "stage32_closed":False,"merge_authorized":False,
      },
    }
    out["canonical_sha256_without_this_field"]=csha(out)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("BTVA_E12_RATIO_SELECTOR_SUMMARY="+json.dumps({
        "base_floor":base_floor,"hypothetical_floor":current_floor,
        "additional":base_floor-current_floor,
        "selected":[r["base4"] for r in selected],
        "canonical":out["canonical_sha256_without_this_field"],
    },sort_keys=True))


if __name__=="__main__":
    main()
