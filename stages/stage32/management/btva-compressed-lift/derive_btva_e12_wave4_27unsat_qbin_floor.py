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
WAVE3_QBIN=ROOT/"stages/stage32/management/btva-compressed-lift/BTVA-D8-E12-WAVE3-PARTIAL-QBIN-RETAINED.json"
WAVE3_QBIN_BLOB="fd6cdc5386bc8b3b30a20aa6c641d7e4a7cb54e7"
WAVE3_QBIN_CANON="edbd101483a9dc08a28203847db11c48919550eb7fe3ea25c5fe5a30d48c188c"
WAVE4_PARTIAL=ROOT/"stages/stage32/management/btva-compressed-lift/BTVA-D8-E12-RATIO-DIRECTED-WAVE4-PARTIAL-RETAINED.json"
WAVE4_PARTIAL_BLOB="91c891e7e91f18713c5155b9b4e885ce0f88e1bd"
WAVE4_PARTIAL_CANON="de2e0507eb7242561493aaebe9b66fa4e0365d54cf8c3943dfffcb53afa6f0d1"
BASELINE_ROW_FLOOR=438674
HPADJ21_ROW_FLOOR=448431
V43_BOUND=157570677819451133507


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


def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--hpadj21-root",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()

    req(blob(PARENT)==PARENT_BLOB,"wave3 selector source drift")
    p3=load_module(PARENT,"stage32_main_btva_wave3_partial_parent")
    wave3_partial=p3.lock_json(PARTIAL,PARTIAL_BLOB,PARTIAL_CANON)
    wave3_unsat={tuple(int(v) for v in row) for row in wave3_partial["result"]["unsat_base4"]}
    wave3_unknown={tuple(int(v) for v in row) for row in wave3_partial["result"]["unknown_base4"]}
    req(len(wave3_unsat)==29 and len(wave3_unknown)==3 and not (wave3_unsat&wave3_unknown),"wave3 partial key partition drift")
    wave3sel=json.loads((ROOT/"stages/stage32/management/btva-compressed-lift/BTVA-D8-E12-RATIO-DIRECTED-WAVE3-SELECTOR-RETAINED.json").read_text())
    wave3keys={tuple(int(v) for v in row) for row in wave3sel["selected_base4_in_order"]}
    req(wave3_unsat|wave3_unknown==wave3keys,"wave3 partial keys do not partition retained selector")

    wave3_qbin=p3.lock_json(WAVE3_QBIN,WAVE3_QBIN_BLOB,WAVE3_QBIN_CANON)
    req(wave3_qbin["result"]["wave3_partial_exact_qbin_row_floor"]==425610,"wave3 exact qbin floor drift")
    wave4_partial=p3.lock_json(WAVE4_PARTIAL,WAVE4_PARTIAL_BLOB,WAVE4_PARTIAL_CANON)
    wave4_unsat={tuple(int(v) for v in row) for row in wave4_partial["result"]["unsat_base4"]}
    wave4_unknown={tuple(int(v) for v in row) for row in wave4_partial["result"]["unknown_base4"]}
    req(len(wave4_unsat)==27 and len(wave4_unknown)==5 and not (wave4_unsat&wave4_unknown),"wave4 partial key partition drift")
    req(wave4_partial["result"]["compatible_sat_base4_count"]==0,"wave4 compatible SAT drift")

    wave2=p3.lock_json(p3.WAVE2_RETAINED,p3.WAVE2_RETAINED_BLOB,p3.WAVE2_RETAINED_CANON)
    req(wave2["result"]["exact_wave2_joint_row_floor"]==BASELINE_ROW_FLOOR,"wave2 row floor drift")

    req(p3.blob(p3.INDEXER)==p3.INDEXER_BLOB,"indexer drift")
    sys.path.insert(0,str(p3.INDEXER.parent))
    idxmod=p3.load_module(p3.INDEXER,"stage32_main_btva_wave3_partial_indexer")
    indexer=idxmod.CompressedTerminalIndexer(p3.E,p3.D)
    req(indexer.normal_budget==92 and int(indexer.exceptional_count)==164282,"e12 census boundary")

    hp_root=args.hpadj21_root.resolve()
    row_worker=hp_root/p3.ROW_WORKER_REL
    req(row_worker.is_file() and p3.blob(row_worker)==p3.ROW_WORKER_BLOB,"HPADJ21 row worker drift")
    rw=p3.load_module(row_worker,"stage32_main_btva_wave3_partial_row")
    p=rw.load_pilot(); h20=p.load_parent(); h19=h20.load_parent(); h18=h19.load_parent(); h17=h18.load_parent(); h16=h17.load_parent()
    p15=h16.load_module(h16.PARENT,h16.PARENT_BLOB,"stage32_main_btva_wave3_partial_h15")
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

    pre_caps_by_key=defaultdict(lambda:defaultdict(Counter))
    raw_blocks=Counter()
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

    proved_wave2=p3.TOP16|p3.WAVE1|p3.WAVE2
    req(len(proved_wave2)==48,"wave2 proved-key count drift")
    req(not (proved_wave2 & wave3_unsat) and not (proved_wave2 & wave4_unsat),"new UNSAT key overlaps earlier proved set")
    req(not (wave3_unsat & wave4_unsat),"wave4 UNSAT overlaps wave3 UNSAT")

    wave2_caps={i:Counter() for i in p15.PLANNED}
    for key in proved_wave2:
        for interval,caps in pre_caps_by_key.get(key,{}).items():
            wave2_caps[interval].update(caps)
    caps_after_wave2=p3.subtract_key(full_caps,wave2_caps)
    _,wave2_floor,_=p3.objective(h18,p15,cells,caps_after_wave2)
    req(wave2_floor==BASELINE_ROW_FLOOR,"wave2 floor replay")

    wave3_caps={i:Counter() for i in p15.PLANNED}
    for key in wave3_unsat:
        for interval,caps in pre_caps_by_key.get(key,{}).items():
            wave3_caps[interval].update(caps)
    for key in wave3_unknown:
        req(sum(sum(c.values()) for c in pre_caps_by_key.get(key,{}).values())>0,"wave3 unknown key has no HPADJ21 overlap")
    caps_after_wave3=p3.subtract_key(caps_after_wave2,wave3_caps)
    _,wave3_floor,_=p3.objective(h18,p15,cells,caps_after_wave3)
    req(wave3_floor==425610,"wave3 partial floor replay")

    wave4_caps={i:Counter() for i in p15.PLANNED}
    for key in wave4_unsat:
        for interval,caps in pre_caps_by_key.get(key,{}).items():
            wave4_caps[interval].update(caps)
    for key in wave4_unknown:
        req(sum(sum(c.values()) for c in pre_caps_by_key.get(key,{}).values())>0,"wave4 unknown key has no HPADJ21 overlap")
    caps_after_wave4=p3.subtract_key(caps_after_wave3,wave4_caps)
    _,floor,_=p3.objective(h18,p15,cells,caps_after_wave4)
    req(floor<=wave3_floor,"wave4 exact UNSAT reoptimization weakened row bound")

    overlap=sum(sum(c.values()) for c in wave4_caps.values())
    raw=sum(int(raw_blocks[k])*p3.B for k in wave4_unsat)
    tightening=HPADJ21_ROW_FLOOR-floor
    out={
      "schema":"STAGE32_MAIN_BTVA_D8_E12_WAVE4_27UNSAT_EXACT_QBIN_FLOOR_V1",
      "stage":32,
      "status":"EXACT_WAVE4_27UNSAT_QBIN_ROW_TIGHTENING_CANDIDATE_ZERO_CREDIT",
      "target":{"row_id":p3.ROW_ID,"row_index":p3.ROW_INDEX,"g":p3.G,"d":p3.D,"e":p3.E},
      "proof_population":{
        "wave2_proved_base4_count":48,
        "wave3_exact_unsat_count":29,
        "wave3_unknown_count":3,
        "wave4_selected_count":32,
        "wave4_exact_unsat_count":27,
        "wave4_unknown_count":5,
        "wave4_unsat_raw_terminal_mass":raw,
        "wave4_unsat_hpadj21_predomain_overlap_terminal_mass":overlap,
        "wave4_unknown_base4":[list(k) for k in sorted(wave4_unknown)],
      },
      "result":{
        "baseline_hpadj21_row_floor":HPADJ21_ROW_FLOOR,
        "wave2_exact_qbin_row_floor":wave2_floor,
        "wave3_partial_exact_qbin_row_floor":wave3_floor,
        "wave4_27unsat_exact_qbin_row_floor":floor,
        "additional_tightening_beyond_wave3_partial":wave3_floor-floor,
        "total_tightening_vs_hpadj21_baseline":tightening,
      },
      "authority_candidate":{
        "current_v43_global_upper_bound":str(V43_BOUND),
        "candidate_global_upper_bound_if_promoted":str(V43_BOUND-tightening),
        "candidate_tightening":tightening,
        "authority_changed":False,
        "additional_main_pruning_credit":0,
      },
      "composition":{
        "same_hpadj21_row":True,
        "exact_qbin_reoptimization":True,
        "wave2_and_wave3_proved_keys_removed_before_wave4":True,
        "only_exact_unsat_wave4_keys_removed":True,
        "five_wave4_unknown_keys_left_adversarially_present":True,
        "no_additive_subtraction_used":True,
        "statistical_independence_assumed":False,
        "candidate_composition":f"REPLACE_G0_D008_HPADJ21_ROW_FLOOR_{HPADJ21_ROW_FLOOR}_WITH_{floor}_AFTER_HOSTILE_AUDIT_AND_MAIN_PROMOTION",
      },
      "source_locks":{
        "wave3_selector_script_blob_sha1":PARENT_BLOB,
        "wave3_partial_retained_blob_sha1":PARTIAL_BLOB,
        "wave3_partial_qbin_retained_blob_sha1":WAVE3_QBIN_BLOB,
        "wave4_partial_retained_blob_sha1":WAVE4_PARTIAL_BLOB,
        "wave4_partial_retained_canonical_sha256":WAVE4_PARTIAL_CANON,
        "hpadj21_head":p3.HPADJ21_HEAD,
        "hpadj21_row_worker_blob_sha1":p3.ROW_WORKER_BLOB,
        "compressed_terminal_indexer_blob_sha1":p3.INDEXER_BLOB,
      },
      "firewalls":{
        "main_pruning_credit":False,"receiver_credit":False,"effectivity_credit":False,
        "theorem_credit":False,"endpoint_credit":False,"full178_complete":False,
        "stage32_closed":False,"merge_authorized":False,"hostile_audit_required_before_promotion":True,
      },
    }
    out["canonical_sha256_without_this_field"]=csha(out)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("BTVA_E12_WAVE4_27UNSAT_QBIN_SUMMARY="+json.dumps(out["result"],sort_keys=True))
    print("BTVA_E12_WAVE4_27UNSAT_QBIN_AUTHORITY="+json.dumps(out["authority_candidate"],sort_keys=True))
    print("BTVA_E12_WAVE4_27UNSAT_QBIN_CANONICAL="+out["canonical_sha256_without_this_field"])


if __name__=="__main__":
    main()
