#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
MANIFEST=Path(__file__).with_name("HPADJ21-TOP20-MASS-MANIFEST.json")
MANIFEST_BLOB="d4e38ed1e0b400ab8ca2ce54a0385092d3bb839c"
WORKER_BLOB="d4dfd574f988f941553b92b2a19dbbef19f7c942"
AUTH=157570677819451133507
SCHEMA="STAGE32_MAIN_GRF04_X4_SUPPORT_TOP20_AGGREGATE_V1"
def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)
def blob(p):
    raw=p.read_bytes();return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--input-dir",type=Path,required=True);ap.add_argument("--output",type=Path,required=True);a=ap.parse_args()
    req(blob(MANIFEST)==MANIFEST_BLOB,"manifest blob drift")
    mf=json.loads(MANIFEST.read_text()); expected={int(r["row_index"]):r for r in mf["rows"]}
    found={}
    for p in a.input_dir.rglob("*.json"):
        d=json.loads(p.read_text())
        if d.get("schema")!="STAGE32_MAIN_GRF04_X4_SUPPORT_HPADJ21_TOP20_ROW_V1": continue
        req(d.get("canonical_sha256_without_this_field")==canon(d),"row canonical drift")
        idx=int(d["target"]["row_index"]);req(idx in expected and idx not in found,"row coverage/duplicate drift")
        req(d["source_locks"]["top20_manifest_blob_sha1"]==MANIFEST_BLOB,"row manifest lock drift")
        req(d["source_locks"]["hpadj21_row_worker_blob_sha1"]=="68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7","row worker lock drift")
        req(d["result"]["old_hpadj21_row_floor"]==expected[idx]["old_hpadj21_floor"],"old floor drift")
        req(int(d["result"]["new_grf04_x4_row_floor"])<=int(d["result"]["old_hpadj21_row_floor"]),"row weakened")
        req(d["firewalls"]["main_pruning_credit"] is False,"row credit drift")
        found[idx]=d
    req(set(found)==set(expected),"top20 row coverage incomplete")
    old=sum(int(found[i]["result"]["old_hpadj21_row_floor"]) for i in found)
    new=sum(int(found[i]["result"]["new_grf04_x4_row_floor"]) for i in found)
    gain=old-new
    req(old==119686241435383494141,"top20 old mass drift")
    req(gain>=0,"negative top20 gain")
    stream=hashlib.sha256()
    rows=[]
    for idx in sorted(found):
        d=found[idx]
        s={"row_index":idx,"row_id":d["target"]["row_id"],"old":d["result"]["old_hpadj21_row_floor"],"new":d["result"]["new_grf04_x4_row_floor"],"improvement":d["result"]["improvement"],"canonical":d["canonical_sha256_without_this_field"]}
        rows.append(s);stream.update(json.dumps(s,sort_keys=True,separators=(",",":")).encode()+b"\n")
    out={"schema":SCHEMA,"stage":32,"status":"EXACT_TOP20_PARTIAL_FULL178_BOUND_REPLACEMENT_CANDIDATE_ZERO_CREDIT",
      "scope":{"row_count":20,"hpadj21_authority_coverage_num":str(old),"hpadj21_authority_coverage_den":str(AUTH)},
      "result":{"old_top20_floor_sum":str(old),"new_top20_floor_sum":str(new),"top20_improvement":str(gain),"candidate_global_upper_bound_if_promoted":str(AUTH-gain)},
      "row_stream_sha256":stream.hexdigest(),"rows":rows,
      "source_locks":{"top20_manifest_blob_sha1":MANIFEST_BLOB,"worker_blob_sha1":WORKER_BLOB,
        "hpadj21_aggregate_canonical_sha256":"82d9dcd44eca1ead942ee300d0a66f2aaf895184482b308691a5544240877769"},
      "composition":{"replace_only_selected_20_hpadj21_rows":True,"other_158_rows_left_at_hpadj21":True,"no_additive_stacking":True,"same_population":True},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"hostile_audit_required_before_promotion":True,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("GRF04_X4_TOP20_SUMMARY="+json.dumps(out["result"],sort_keys=True))
    print("GRF04_X4_TOP20_CANONICAL="+out["canonical_sha256_without_this_field"])
if __name__=="__main__":main()
