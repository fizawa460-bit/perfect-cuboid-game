#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,importlib.util,json,sys
from pathlib import Path

AUTH=157570677819451133507
EXPECTED_REJECT=40886299509963924857401
DIRECT_BAND_REL=Path("stages/stage32/management/hpadj22-direct-full178/run_direct_band.py")
DIRECT_BAND_BLOB="26746a68dc53b53d4ed28aef7c65954759094ae7"
DIRECT_COUNT_BLOB="e965ab0a6ea51938006882ca2110016f48b3768e"
HPADJ22_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
OLD_REL=Path("stages/stage32-ex5/hpadj-22_ex5/run_full_bband.py")
OLD_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"
BAND7_CANON="b367b4ba2fda193a82d8eb925ee46423fe9218cb6ad8dca204b898455ffa256d"
SCHEMA="STAGE32_MAIN_HPADJ22_DIRECT_FULL178_AGGREGATE_V1"

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def blob(p):
    raw=p.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_old(root):
    p=root/OLD_REL
    req(p.is_file() and blob(p)==OLD_BLOB,"old HPADJ22 worker drift")
    spec=importlib.util.spec_from_file_location("hpadj22_old_for_direct_full_aggregate",p)
    req(spec and spec.loader,"cannot load old HPADJ22 worker")
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
    return m

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo-root",type=Path,required=True)
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--direct-root",type=Path,required=True)
    ap.add_argument("--band7-dir",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    req(blob(a.repo_root/DIRECT_BAND_REL)==DIRECT_BAND_BLOB,"direct band worker drift")

    bands={}
    for p in sorted(a.direct_root.rglob("band-*.json")):
        d=json.loads(p.read_text())
        if d.get("schema")!="STAGE32_MAIN_HPADJ22_DIRECT_BAND_V1": continue
        req(d.get("canonical_sha256_without_this_field")==canon(d),"direct band canonical drift")
        pos=int(d["band"]["position"])
        req(0<=pos<=6 and pos not in bands,"direct band coverage/duplicate drift")
        req(d["band"]["row_count"]==178,"direct band row coverage")
        req(d["validation"]["all_178_rows_replay_retained_hpadj08_rejected_mass"] is True,"retained reject replay missing")
        req(d["source_locks"]["direct_count_blob_sha1"]==DIRECT_COUNT_BLOB,"direct-count source drift")
        req(d["source_locks"]["hpadj22_source_head"]==HPADJ22_HEAD,"HPADJ22 source drift")
        req(d["firewalls"]["main_pruning_credit"] is False,"band credit drift")
        bands[pos]=d
    req(set(bands)==set(range(7)),f"direct bands incomplete {sorted(bands)}")

    old=load_old(a.source_root)
    ctx=old.source_context()
    marker,rows7=old.validate_complete_dir(a.band7_dir,7,ctx)
    req(marker["canonical_sha256_without_this_field"]==BAND7_CANON,"band7 retained canonical drift")
    req(len(rows7)==178,"band7 row coverage")

    pre=reject=post=h22=0
    summaries=[]
    for pos in range(7):
        d=bands[pos];t=d["totals"]
        p0=int(t["pre_mass"]);r0=int(t["rejected_mass"]);po=int(t["post_mass"]);h0=int(t["hpadj22_exact_survivor_sum"])
        req(p0-r0==po,f"direct band mass conservation {pos}")
        pre+=p0;reject+=r0;post+=po;h22+=h0
        summaries.append({"band_position":pos,"b_interval":d["band"]["b_interval"],"source":"NEW_DIRECT",
          "pre_mass":str(p0),"rejected_mass":str(r0),"post_mass":str(po),"hpadj22_exact":str(h0),
          "canonical":d["canonical_sha256_without_this_field"],
          "retained_crosschecked_rows":d["validation"]["retained_partial_crosschecked_rows"]})

    t7=marker["totals"]
    p7=int(t7["pre_mass"]);r7=int(t7["rejected_mass"]);po7=int(t7["post_mass"]);h7=int(t7["hpadj22_exact_survivor_sum"])
    req(p7-r7==po7,"band7 mass conservation")
    pre+=p7;reject+=r7;post+=po7;h22+=h7
    summaries.append({"band_position":7,"b_interval":marker["b_interval"],"source":"RETAINED_COMPLETE_BAND7",
      "pre_mass":str(p7),"rejected_mass":str(r7),"post_mass":str(po7),"hpadj22_exact":str(h7),
      "canonical":marker["canonical_sha256_without_this_field"],"retained_crosschecked_rows":178})

    req(pre-reject==post,"FULL178 mass conservation")
    req(reject==EXPECTED_REJECT,f"FULL178 retained HPADJ08 reject mismatch {reject} != {EXPECTED_REJECT}")
    candidate=min(AUTH,h22)
    gain=AUTH-candidate
    req(gain>=0,"candidate worsened authority")

    out={
      "schema":SCHEMA,"stage":32,
      "status":"EXACT_FULL178_DIRECT_HPADJ22_CANDIDATE_ZERO_CREDIT_HOSTILE_AUDIT_REQUIRED",
      "coverage":{"bands":8,"rows_per_band":178,"cells":1424,"gaps":0,"overlaps":0,
        "new_direct_bands":[0,1,2,3,4,5,6],"retained_complete_bands":[7]},
      "source_locks":{
        "direct_band_worker_blob_sha1":DIRECT_BAND_BLOB,
        "direct_count_blob_sha1":DIRECT_COUNT_BLOB,
        "hpadj22_source_head":HPADJ22_HEAD,
        "old_band_worker_blob_sha1":OLD_BLOB,
        "retained_band7_canonical":BAND7_CANON,
        "current_main_state_blob_sha1":"ca613fd51623ee8846369bb4f68507f7a85ba49f"
      },
      "totals":{"pre_mass":str(pre),"rejected_mass":str(reject),"post_mass":str(post),
        "hpadj22_exact_survivor_sum":str(h22)},
      "result":{"current_authority":str(AUTH),"direct_hpadj22_full178_upper_bound":str(h22),
        "candidate_global_upper_bound_if_promoted":str(candidate),"exact_tightening_if_promoted":str(gain)},
      "bands":summaries,
      "composition":{
        "rule":"MIN_CURRENT_HPADJ21_AUTHORITY_WITH_EXACT_FULL178_HPADJ22_DIRECT_SURVIVOR_COUNT",
        "same_pre_domain_population":True,"same_picard_qA_rule":True,
        "exact_hpadj08_deletion_location_retained":True,
        "all_1424_cells_covered_exactly_once":True,
        "additive_subtraction":False,"statistical_independence":False
      },
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,
        "hostile_audit_required_before_promotion":True,"theorem_credit":False,
        "effectivity_credit":False,"receiver_credit":False,"endpoint_credit":False,
        "stage32_closed":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("HPADJ22_DIRECT_FULL178="+json.dumps({
      "hpadj22":str(h22),"candidate":str(candidate),"gain":str(gain),
      "canonical":out["canonical_sha256_without_this_field"]
    },sort_keys=True))

if __name__=="__main__":main()
