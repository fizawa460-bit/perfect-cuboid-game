#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
PARENT=ROOT/"stages/stage32/management/btva-compressed-lift/select_btva_e12_ratio_directed_base4_wave3.py"
PARENT_BLOB="9c26eb7bdff3f350848858189f0b3044433f91ed"
PARTIAL=ROOT/"stages/stage32/management/btva-compressed-lift/BTVA-D8-E12-RATIO-DIRECTED-WAVE3-PARTIAL-RETAINED.json"
PARTIAL_BLOB="3864c723d77fa4f8827ec999cb4743a8b0761961"
PARTIAL_CANON="b9bc11e5dbd9058c937656c24c0830acf62619cd3e3b639c06134a29f2b5f2d8"
PARTIAL_QBIN=ROOT/"stages/stage32/management/btva-compressed-lift/BTVA-D8-E12-WAVE3-PARTIAL-QBIN-RETAINED.json"
PARTIAL_QBIN_BLOB="fd6cdc5386bc8b3b30a20aa6c641d7e4a7cb54e7"
PARTIAL_QBIN_CANON="edbd101483a9dc08a28203847db11c48919550eb7fe3ea25c5fe5a30d48c188c"
SELECT_COUNT=32
BASE_FLOOR=425610
BASE_TIGHTENING=22821


def req(v: bool,msg: str)->None:
    if not v:
        raise SystemExit("FAIL: "+msg)


def blob(path: Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def csha(v: object)->str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def load_module(path: Path,name: str):
    spec=importlib.util.spec_from_file_location(name,path)
    req(spec is not None and spec.loader is not None,"cannot load "+str(path))
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod


def lock_json(path: Path, expected_blob: str, expected_canon: str)->dict:
    req(blob(path)==expected_blob,path.name+" blob drift")
    obj=json.loads(path.read_text(encoding="utf-8"))
    stored=obj.get("canonical_sha256_without_this_field")
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    req(stored==expected_canon and csha(body)==expected_canon,path.name+" canonical drift")
    return obj


def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--hpadj21-root",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()

    req(blob(PARENT)==PARENT_BLOB,"wave3 selector source drift")
    p3=load_module(PARENT,"stage32_main_btva_wave4_parent")
    partial=lock_json(PARTIAL,PARTIAL_BLOB,PARTIAL_CANON)
    partial_qbin=lock_json(PARTIAL_QBIN,PARTIAL_QBIN_BLOB,PARTIAL_QBIN_CANON)
    unsat3={tuple(int(v) for v in row) for row in partial["result"]["unsat_base4"]}
    unknown3={tuple(int(v) for v in row) for row in partial["result"]["unknown_base4"]}
    req(len(unsat3)==29 and len(unknown3)==3 and not (unsat3&unknown3),"wave3 partial key partition")
    req(partial_qbin["result"]["wave3_partial_exact_qbin_row_floor"]==BASE_FLOOR,"wave3 partial qbin floor")
    req(partial_qbin["result"]["total_tightening_vs_hpadj21_baseline"]==BASE_TIGHTENING,"wave3 partial tightening")

    req(p3.blob(p3.INDEXER)==p3.INDEXER_BLOB,"indexer drift")
    sys.path.insert(0,str(p3.INDEXER.parent))
    idxmod=p3.load_module(p3.INDEXER,"stage32_main_btva_wave4_indexer")
    indexer=idxmod.CompressedTerminalIndexer(p3.E,p3.D)
    req(indexer.normal_budget==92 and int(indexer.exceptional_count)==164282,"e12 census boundary")

    hp_root=args.hpadj21_root.resolve()
    row_worker=hp_root/p3.ROW_WORKER_REL
    req(row_worker.is_file() and p3.blob(row_worker)==p3.ROW_WORKER_BLOB,"HPADJ21 row worker drift")
    rw=p3.load_module(row_worker,"stage32_main_btva_wave4_row")
    p=rw.load_pilot(); h20=p.load_parent(); h19=h20.load_parent(); h18=h19.load_parent(); h17=h18.load_parent(); h16=h17.load_parent()
    p15=h16.load_module(h16.PARENT,h16.PARENT_BLOB,"stage32_main_btva_wave4_h15")
    p14=p15.load_parent(); counter=p14.load_counter()
    manifest=counter.load_locked_json(p14.MANIFEST,p14.LOCKS["manifest_blob"],p14.LOCKS["manifest_canonical"],"FULL178 manifest")
    rows=counter.manifest_rows(manifest)
    row_id,g,d=rows[p3.ROW_INDEX]
    req((row_id,int(g),int(d))==(p3.ROW_ID,p3.G,p3.D),"row identity")

    cells,BC=p.exact_pilot_cells(p15,p14,counter,[(p3.ROW_ID,p3.G,p3.D)])
    profiles,_,_=p.full_profiles(p3.H,counter,h19)
    A=[[sum(mult for _,mult in profiles[a][sa]) for sa in range(4)] for a in range(p3.H+1)]
    full_caps={interval:defaultdict(int) for interval in p15.PLANNED}
    K=counter.ceil_div(p3.D-16*p3.G+16,4)

    for b in range(p3.H+1):
        interval=p15.shard_for_b(b)
        for c in range(p3.H+1):
            bcv=BC[b][c]
            if not any(any(pair) for pair in bcv): continue
            c3=counter.component3(p3.D,b,c)
            if c3<0: continue
            exact_surv=p.full_survivors(h16,profiles,p3.H,p3.G,b,c)
            for a in range(p3.H+1):
                if not any(A[a]): continue
                M=a+b+c; ca=counter.component_a(p3.D,a)
                if ca<0: continue
                srem=min(16,p3.D)+ca+c3
                for sbc,pair in enumerate(bcv):
                    for r in (0,1):
                        left=int(pair[r])
                        if not left: continue
                        for sa,right in enumerate(A[a]):
                            if not right: continue
                            fi=exact_surv[a][sa]; req(fi is not None,"missing q profile")
                            support=sbc+sa; qneed=K-support
                            if qneed>0 and srem<qneed: continue
                            lower=max(8,K,p3.D-4*p3.G+4,M,M+max(0,qneed))
                            upper=min((19*p3.D)//5,3*p3.D,3*p3.D-(b-c))
                            if lower>upper: continue
                            excluded=set(); e_n358=3*p3.D-(b-c)
                            if b<=p3.H-5 and support+srem==K and e_n358-M>=srem: excluded.add(e_n358)
                            lo=lower if lower%2==0 else lower+1; hi=upper if upper%2==0 else upper-1
                            for e in range(lo,hi+1,2):
                                if e in excluded: continue
                                BB=19*p3.D-5*e+1
                                for s0,s1,mult in fi["tiers"]:
                                    ss=s0 if r==0 else s1
                                    full_caps[interval][(int(ss),BB)]+=left*int(mult)*BB
    for interval in p15.PLANNED:
        req(sum(full_caps[interval].values())==int(cells[(interval,p3.G,p3.D)]["pre_mass"]),"full caps replay")

    raw_blocks=Counter()
    pre_caps_by_key=defaultdict(lambda:defaultdict(Counter))
    support_by_key=defaultdict(Counter)
    for erank in range(int(indexer.exceptional_count)):
        x=tuple(int(v) for v in indexer.unrank(erank*p3.B))
        req(x[4]==0,"x4 stride")
        a,b,c,t,r,sa,qA,s=p3.block_coordinates(h16,x)
        key=(a,b,c,t)
        raw_blocks[key]+=1
        if s is None: continue
        c3=counter.component3(p3.D,b,c); ca=counter.component_a(p3.D,a)
        if c3<0 or ca<0: continue
        support=sum(1 for j,v in enumerate(x) if j!=4 and v>0)
        srem=min(16,p3.D)+ca+c3; qneed=K-support
        if qneed>0 and srem<qneed: continue
        M=a+b+c
        lower=max(8,K,p3.D-4*p3.G+4,M,M+max(0,qneed))
        upper=min((19*p3.D)//5,3*p3.D,3*p3.D-(b-c))
        if not (lower<=p3.E<=upper): continue
        e_n358=3*p3.D-(b-c)
        if b<=p3.H-5 and support+srem==K and e_n358-M>=srem and p3.E==e_n358: continue
        interval=p15.shard_for_b(b)
        pre_caps_by_key[key][interval][(int(s),p3.B)]+=p3.B
        support_by_key[key][support]+=1

    proved=p3.TOP16|p3.WAVE1|p3.WAVE2|unsat3
    attempted=proved|unknown3
    req(len(proved)==77 and len(attempted)==80,"wave4 proved/attempted key counts")

    proved_caps={i:Counter() for i in p15.PLANNED}
    for key in proved:
        for interval,caps in pre_caps_by_key.get(key,{}).items():
            proved_caps[interval].update(caps)
    caps_after_proved=p3.subtract_key(full_caps,proved_caps)
    base_obj,base_floor,_=p3.objective(h18,p15,cells,caps_after_proved)
    req(base_floor==BASE_FLOOR,"wave4 baseline floor replay")

    remaining={k for k in pre_caps_by_key if k not in attempted and sum(sum(c.values()) for c in pre_caps_by_key[k].values())>0}
    req(len(remaining)>=SELECT_COUNT,"insufficient fresh wave4 keys")
    selected=[]
    current_caps=caps_after_proved
    current_obj=base_obj
    current_floor=base_floor

    for step in range(SELECT_COUNT):
        best=None
        for key in remaining:
            test=p3.subtract_key(current_caps,pre_caps_by_key[key])
            obj,floor,post=p3.objective(h18,p15,cells,test)
            delta=current_obj-obj
            overlap=sum(sum(c.values()) for c in pre_caps_by_key[key].values())
            score=(delta,current_floor-floor,overlap,raw_blocks[key]*p3.B,tuple(-v for v in key))
            if best is None or score>best[0]:
                best=(score,key,test,obj,floor,post)
        req(best is not None,"wave4 selector exhausted")
        score,key,test,obj,floor,post=best
        delta=score[0]
        selected.append({
          "selection_order":step,
          "base4":list(key),
          "raw_exceptional_blocks":int(raw_blocks[key]),
          "raw_terminal_mass":int(raw_blocks[key])*p3.B,
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
        current_caps=test; current_obj=obj; current_floor=floor; remaining.remove(key)

    selected_keys={tuple(r["base4"]) for r in selected}
    req(len(selected_keys)==SELECT_COUNT and not (selected_keys&attempted),"wave4 selector overlap prior/unknown")
    out={
      "schema":"STAGE32_MAIN_BTVA_D8_E12_RATIO_DIRECTED_SELECTOR_WAVE4_V1",
      "stage":32,
      "status":"EXACT_HPADJ21_RATIO_DIRECTED_BTVA_WAVE4_SELECTOR_ZERO_CREDIT",
      "target":{"row_id":p3.ROW_ID,"row_index":p3.ROW_INDEX,"g":p3.G,"d":p3.D,"e":p3.E,"selected_count":SELECT_COUNT},
      "baseline":{
        "proved_base4_count":77,
        "reserved_timeout_base4_count":3,
        "wave3_partial_exact_qbin_row_floor":base_floor,
        "wave3_partial_tightening_candidate":BASE_TIGHTENING,
      },
      "selected":selected,
      "selected_base4_in_order":[r["base4"] for r in selected],
      "hypothetical_if_all_selected_unsat":{
        "row_floor":current_floor,
        "additional_tightening_beyond_wave3_partial":base_floor-current_floor,
        "total_tightening_vs_hpadj21_baseline":448431-current_floor,
        "selected_raw_terminal_mass":sum(r["raw_terminal_mass"] for r in selected),
        "selected_hpadj21_predomain_overlap_terminal_mass":sum(r["hpadj21_predomain_overlap_terminal_mass"] for r in selected),
      },
      "population":{
        "e12_base4_key_count":len(raw_blocks),
        "hpadj21_predomain_base4_key_count":len(pre_caps_by_key),
        "proved_key_count":77,
        "reserved_timeout_key_count":3,
      },
      "source_locks":{
        "parent_wave3_selector_blob_sha1":PARENT_BLOB,
        "wave3_partial_retained_blob_sha1":PARTIAL_BLOB,
        "wave3_partial_retained_canonical_sha256":PARTIAL_CANON,
        "wave3_partial_qbin_retained_blob_sha1":PARTIAL_QBIN_BLOB,
        "wave3_partial_qbin_retained_canonical_sha256":PARTIAL_QBIN_CANON,
        "compressed_terminal_indexer_blob_sha1":p3.INDEXER_BLOB,
        "hpadj21_head":p3.HPADJ21_HEAD,
        "hpadj21_row_worker_blob_sha1":p3.ROW_WORKER_BLOB,
      },
      "semantics":{
        "selector_is_not_unsat_proof":True,
        "hypothetical_floor_requires_all_selected_keys_to_later_prove_btva_unsat":True,
        "three_wave3_timeout_keys_reserved_and_not_reselected":True,
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
    print("BTVA_E12_RATIO_WAVE4_SELECTOR_SUMMARY="+json.dumps({
      "base_floor":base_floor,
      "hypothetical_floor":current_floor,
      "additional":base_floor-current_floor,
      "selected":[r["base4"] for r in selected],
      "canonical":out["canonical_sha256_without_this_field"],
    },sort_keys=True))


if __name__=="__main__":
    main()
