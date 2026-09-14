#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
STAGE=ROOT/"stages/stage32"
STATE=STAGE/"MAIN-STATE.json"
SNAP=STAGE/"management/MAIN-STATE-V21-BATCH-CUT-PRECONSUMPTION.json"
RECEIPT=STAGE/"management/post-cut193-cut197-cut198-current-v21-batch-composition-consumption-20260913.json"
V21_HEAD="62768270a39b23c358f11b3a75bccae5d7cea0f6"
V21_STATE_BLOB="64dc5523652f1bbe4f19456a6854a39cb3aec87a"
V21_STATE_CANON="739520f562fc445567969088bfea0dd9d87d85c11541d706e6f68748746e0fb7"
V22_STATE_BLOB="80fb35c79854bfdf775dc5b94c331f5f8a535ced"
V22_STATE_CANON="82ca200d81b0ce844b1756dc0c3205eec388a20cae312af5e0f3c55d959d491c"
RECEIPT_BLOB="84c1c37b5bf9ad5b42b566eeca032b631f4c4cdf"
RECEIPT_CANON="1ac16af0b323d28ad216fc3c2d2101782a14d9f8eebcd13f6128f5bb4e572121"
N357_COMP_HEAD="0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
N357_VERIFIER_BLOB="fdca9ad629983d8c31c7e6355540af3545910120"
POP_COUNT=7596
POP_STREAM="529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3"
WIDTH=113
PRE=47589703313957134886123
TOTAL=81925
POST=47589703313957134804198
CUTS={
"CUT193":{"head":"5b2ebb3f67805eddefef835878ba4b9744bfdbd9","path":"stages/stage32/full178-cut/CUT193-e8-common-adapter-wave1-result.json","blob":"ef72967a97e41287671f25647ad6fc24aef31ccb","canon":"161abe2cf9a00b95ce2b1acd422008bbb5c72929ea7a72e9892b94546abae2c1","offset":[1,255],"closed":227,"inc":25651},
"CUT197":{"head":"adce53dc9004c24bffb3ba9f88e9d5d6e51cf6a5","path":"stages/stage32/full178-cut/CUT197-e8-common-adapter-wave5-result.json","blob":"e98f33ef093003e724ff6574bfec546ab1221955","canon":"f99d0f051ce95e269658e0ec945d727db32a94687bfd8acde5ee354e00776fa0","offset":[1021,1275],"closed":250,"inc":28250},
"CUT198":{"head":"16e439bc65e723c9f2658c274d53fb839738dcd2","path":"stages/stage32/full178-cut/CUT198-e8-common-adapter-wave6-result.json","blob":"29a392b20d3f88519f5e8a6f3d2225ec5955bcb2","canon":"60f2d1d4d926d3f0c527a15fb2978d11dea7ca5dc9d02825c2671fc793618607","offset":[1276,1530],"closed":248,"inc":28024}}
OLD_RECEIPTS={
"CUT191":("stages/stage32/management/post-cut191-hostile-pass-consumption-20260911.json","8bea39e443d7996a8958c95005206d6ff349fa52","f1c59f708190f99ef87422eabc443a5c9df981438a5e647c93dc5052fc5fe6a2"),
"CUT194":("stages/stage32/management/post-cut194-hostile-pass-consumption-20260912.json","775c7853de989ee92167269bf3be774bd1e984f3","6e9711716358ff955fe3aac1fda9661a800f3f1e3d10286fa5127a4638efb568"),
"CUT195":("stages/stage32/management/post-cut195-current-v14-composition-consumption-20260912.json","148ea573bb1f618baac33c0d1f8cc91678fbbca2","e33fb30bef69ce3ef87f095b500ecd4a8a21b155a3d9c957836ed17c82ad6be9"),
"CUT196":("stages/stage32/management/post-cut196-current-v16-composition-consumption-20260912.json","a45f27611d6d274e7e7e3ff65e8a75089e996596","2c55ddd13f90068fc8383c755dcada07f265c40c6ff468709b0add12a390c0e2"),
"N358":("stages/stage32/management/post-n358-current-v18-composition-consumption-20260912.json","efa87a1b62cc698745f87814cd8f9eb9fe95dbd2","27c50848e19c242389298b6a23d7c5b6a8ea86afd97c36ced16905adc66a5bdc")}
def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)
def git_blob(p):
    r=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(r)).encode()+b"\0"+r).hexdigest()
def canonical(o):
    c=dict(o); c.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(c,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def locked(p,b,c):
    req(p.is_file(),f"missing {p}"); req(git_blob(p)==b,f"blob drift {p}")
    o=json.loads(p.read_text(encoding="utf-8")); req(o.get("canonical_sha256_without_this_field")==c,f"stored canonical drift {p}"); req(canonical(o)==c,f"canonical drift {p}"); return o
def head(p): return subprocess.check_output(["git","-C",str(p),"rev-parse","HEAD"],text=True).strip()
def stream_sha(vals):
    h=hashlib.sha256()
    for v in vals: h.update(f"{v}\n".encode())
    return h.hexdigest()
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--audited-main-v21-root",type=Path,required=True); ap.add_argument("--audited-cut193-root",type=Path,required=True); ap.add_argument("--audited-cut197-root",type=Path,required=True); ap.add_argument("--audited-cut198-root",type=Path,required=True); ap.add_argument("--audited-n357-composition-root",type=Path,required=True)
    a=ap.parse_args(); roots={"CUT193":a.audited_cut193_root.resolve(),"CUT197":a.audited_cut197_root.resolve(),"CUT198":a.audited_cut198_root.resolve()}; v21=a.audited_main_v21_root.resolve(); comp=a.audited_n357_composition_root.resolve()
    req(head(v21)==V21_HEAD,"V21 exact head drift")
    audited_v21=locked(v21/"stages/stage32/MAIN-STATE.json",V21_STATE_BLOB,V21_STATE_CANON); local_snap=locked(SNAP,V21_STATE_BLOB,V21_STATE_CANON); req(audited_v21==local_snap,"V21 snapshot differs from audited predecessor")
    vf=audited_v21["current_exact_frontier"]; req(vf["authoritative_remaining_terminals"]==PRE and vf["authoritative_remaining_strata"]==17128,"V21 authority drift"); req(vf["cut193_main_pruning_credit"] is False and vf["cut197_main_pruning_credit"] is False,"V21 already consumed new cuts"); req(vf.get("cut198_main_pruning_credit",False) is False,"V21 already consumed CUT198")
    old={}
    for name,(rel,b,c) in OLD_RECEIPTS.items(): old[name]=locked(v21/rel,b,c)
    req(old["CUT191"]["authority"]["cut191_main_pruning_credit"] is True,"CUT191 not consumed"); req(old["CUT194"]["authority"]["cut194_main_pruning_credit"] is True,"CUT194 not consumed"); req(old["CUT195"]["authority"]["cut195_main_pruning_credit"] is True,"CUT195 not consumed"); req(old["CUT196"]["authority"]["cut196_main_pruning_credit"] is True,"CUT196 not consumed")
    req(old["CUT194"]["cut194_external_audit"]["target"]["survivor_offset_range"]==[256,510],"CUT194 range drift"); req(old["CUT195"]["cut195_candidate"]["survivor_offset_range"]==[511,765],"CUT195 range drift"); req(old["CUT196"]["cut196_candidate"]["survivor_offset_range"]==[766,1020],"CUT196 range drift"); req(old["CUT191"]["cut191_external_audit"]["first_block_rank_range"]==[0,112],"CUT191 range drift")
    zr=old["N358"]["current_v18_composition_replay"]["zero_overlap_reason"]; req(zr["consumed_cut_d"]==8 and zr["consumed_cut_e"]==8 and zr["h"]==4 and zr["h_minus_5"]==-1,"N358 zero-overlap premise drift"); req(zr["equivalently_n358_incremental_domain_empty_on_g1_d008_e8"] is True,"N358 e8 empty-domain drift")
    cuts={}
    for name,spec in CUTS.items():
        req(head(roots[name])==spec["head"],f"{name} exact head drift"); cut=locked(roots[name]/spec["path"],spec["blob"],spec["canon"]); cuts[name]=cut
        req(cut["target"]["row_id"]=="g1-d008" and cut["target"]["d"]==8 and cut["target"]["e"]==8,f"{name} target row drift"); req(cut["target"]["survivor_offset_range"]==spec["offset"],f"{name} offset drift"); req(cut["target"]["block_count"]==255 and cut["target"]["terminal_count"]==28815,f"{name} population drift"); req(cut["result"]["candidate_closed_block_count"]==spec["closed"],f"{name} closed count drift"); req(cut["result"]["candidate_pruned_terminals"]==spec["inc"],f"{name} increment drift")
    req(head(comp)==N357_COMP_HEAD,"N357 composition exact head drift"); n357_path=comp/"stages/stage32/verify_n357_v13_current_authority_composition.py"; req(git_blob(n357_path)==N357_VERIFIER_BLOB,"N357 composition verifier blob drift"); subprocess.run([sys.executable,str(n357_path)],cwd=comp,check=True)
    ms=importlib.util.spec_from_file_location("n357_comp",n357_path); req(ms is not None and ms.loader is not None,"cannot import N357 composition"); mod=importlib.util.module_from_spec(ms); ms.loader.exec_module(mod)
    residual=comp/"stages/stage32/residual-32-01-production"; sys.path.insert(0,str(residual)); from compressed_terminal_indexer import CompressedTerminalIndexer
    idx=CompressedTerminalIndexer(8,8); req(idx.normal_budget+1==WIDTH,"block width drift"); survivors=[]
    for bi in range(idx.exceptional_count):
        base=tuple(int(v) for v in idx.unrank(bi*WIDTH))
        if mod.prefix_survives(base): survivors.append(bi)
    req(len(survivors)==POP_COUNT,"survivor count drift"); req(stream_sha(survivors)==POP_STREAM,"survivor stream drift")
    targets={}; closed={}
    for name,spec in CUTS.items():
        lo,hi=spec["offset"]; targets[name]=set(survivors[lo:hi+1]); req(list(cuts[name]["target"]["block_indices"])==survivors[lo:hi+1],f"{name} target != current survivor offsets"); closed[name]=set(int(v) for v in cuts[name]["result"]["candidate_closed_block_indices"]); req(closed[name].issubset(targets[name]),f"{name} closed set escapes target"); rejecting=[b for b in targets[name] if not mod.n357_accepts(tuple(int(v) for v in idx.unrank(b*WIDTH)))]; req(rejecting==[],f"N357 overlaps {name} target: {rejecting[:8]}")
    names=list(CUTS)
    for i in range(len(names)):
        for j in range(i+1,len(names)):
            req(targets[names[i]].isdisjoint(targets[names[j]]),f"new target overlap {names[i]}/{names[j]}"); req(closed[names[i]].isdisjoint(closed[names[j]]),f"new closed overlap {names[i]}/{names[j]}")
    consumed={"CUT191":{survivors[0]},"CUT194":set(survivors[256:511]),"CUT195":set(survivors[511:766]),"CUT196":set(survivors[766:1021])}
    for n,t in targets.items():
        for o,s in consumed.items(): req(t.isdisjoint(s),f"{n} overlaps consumed {o}")
    req(sum(CUTS[n]["inc"] for n in CUTS)==TOTAL,"batch increment arithmetic drift"); req(PRE-TOTAL==POST,"post authority arithmetic drift"); req(not (1<=797<=255 or 1021<=797<=1530),"N372 offset unexpectedly in new waves")
    receipt=locked(RECEIPT,RECEIPT_BLOB,RECEIPT_CANON); state=locked(STATE,V22_STATE_BLOB,V22_STATE_CANON); cr=receipt["composition"]; req(cr["double_charge"] is False and cr["incremental_rejected_terminals"]==TOTAL,"receipt batch composition drift"); req(cr["mutual_overlap_terminals"]==0 and cr["overlap_with_consumed_cuts_terminals"]==0,"receipt overlap drift"); req(cr["overlap_with_n357_terminals"]==0 and cr["overlap_with_n358_terminals"]==0,"receipt N overlap drift")
    sf=state["current_exact_frontier"]; req(sf["authoritative_remaining_terminals"]==POST and sf["authoritative_remaining_strata"]==17128,"V22 authority drift")
    for k in ("cut193_main_pruning_credit","cut197_main_pruning_credit","cut198_main_pruning_credit"): req(sf[k] is True,f"missing consumed credit {k}")
    req(sf["batch_cut_incremental_rejected_terminals"]==TOTAL,"V22 batch increment drift"); req(sf["n372_survives_batch_cut193_cut197_cut198"] is True,"N372 preservation drift"); req(sf["full178_numerical_census_complete"] is False and sf["stage32_closed"] is False,"unauthorized closure"); req(state["firewalls"]["merge_authorized"] is False,"merge authorized")
    print(json.dumps({"verdict":"PASS_CUT193_CUT197_CUT198_CURRENT_V21_BATCH_COMPOSITION_AND_MAIN_CONSUMPTION","incremental_rejected_terminals":TOTAL,"remaining_terminals":POST,"mutual_overlap_terminals":0,"overlap_with_consumed_cuts_terminals":0,"overlap_with_n357_terminals":0,"overlap_with_n358_terminals":0,"n372_preserved":True,"replacement_head_hostile_reaudit_required":True,"merge_authorized":False},sort_keys=True))
if __name__=="__main__": main()
