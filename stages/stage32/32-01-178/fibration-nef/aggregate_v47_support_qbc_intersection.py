#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
MAN=HERE/"local-support-qbc/GENERATION4-COMPLETE.json"
PREF=HERE/"V47-SUPPORT-QBC-INTERSECTION-PREFLIGHT.json"
UNIT=HERE/"run_v47_support_qbc_intersection_unit.py"
OUTDIR=HERE/"v47-support-qbc-intersection"
EXPECTED_MAN_BLOB="a917f6a98e8f4db57d0ada5193fe263f52162732"
EXPECTED_MAN_CANON="3f1ebc76ef519949ef9d5c497a363f216159387d6857c081d7c1867319e3b242"
EXPECTED_UNIT_BLOB="af3026f5d7608181845e2ee0f9e0ab91feee60d1"
V47_TOTAL=128645575147764659235
def req(v,m):
 if not v: raise SystemExit("FAIL: "+m)
def blob(p):
 b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def canon(o):
 x=dict(o);x.pop("canonical_sha256_without_this_field",None)
 return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def main():
 req(blob(MAN)==EXPECTED_MAN_BLOB,"manifest blob drift");m=json.loads(MAN.read_text())
 req(canon(m)==EXPECTED_MAN_CANON==m["canonical_sha256_without_this_field"],"manifest canonical drift")
 req(blob(UNIT)==EXPECTED_UNIT_BLOB,"unit consumer drift")
 pf=json.loads(PREF.read_text());req(int(pf["v47_authority"]["same_population_joint_upper_bound"])==V47_TOTAL,"V47 total drift")
 expected={(int(x["verified"]["row_index"]),int(x["verified"]["b"])) for x in m["receipts"]}
 req(len(expected)==384,"expected coordinate count")
 files=sorted(OUTDIR.glob("row*-b*.json"));req(len(files)==384,f"receipt count {len(files)} != 384")
 seen=set();base=ref=0;stream=hashlib.sha256()
 for p in files:
  o=json.loads(p.read_text());req(canon(o)==o["canonical_sha256_without_this_field"],"canonical "+p.name)
  t=o["target"];k=(int(t["row_index"]),int(t["b"]));req(k in expected and k not in seen,"coordinate "+str(k));seen.add(k)
  req(o["status"]=="EXACT_UNIT_COMPLETE_ZERO_MAIN_CREDIT","status "+p.name)
  req(o["source_locks"]["v47_exact_head"]==pf["v47_authority"]["source_exact_head"],"V47 head "+p.name)
  req(o["source_locks"]["v47_helper_blob_sha1"]==pf["v47_authority"]["helper_blob_sha1"],"V47 helper "+p.name)
  req(o["source_locks"]["support_qbc_worker_blob_sha1"]==pf["support_qbc_producer"]["worker_blob_sha1"],"support worker "+p.name)
  req(o["source_locks"]["hpadj22_source_head"]==pf["v47_authority"]["hpadj22_source_head"],"source head "+p.name)
  r=o["result"];b=int(r["v47_joint_survivors"]);q=int(r["v47_support_qbc_joint_survivors"]);s=int(r["exact_incremental_saving_vs_v47"])
  req(0<=q<=b and s==b-q,"unit accounting "+p.name);base+=b;ref+=q
  stream.update((str(k)+":"+o["canonical_sha256_without_this_field"]+"\n").encode())
 req(seen==expected,"coverage mismatch");saving=base-ref;req(0<=saving<=V47_TOTAL,"global saving range")
 out={"schema":"STAGE32_32_01_178_V47_SUPPORT_QBC_INTERSECTION_AGGREGATE_V1","status":"EXACT_384_COORDINATE_AGGREGATE_ZERO_MAIN_CREDIT",
 "coverage":{"expected_coordinates":384,"completed_coordinates":384,"unique_coordinates":384,"uncomputed_v47_region_unchanged":True},
 "source_locks":{"generation4_manifest_blob_sha1":EXPECTED_MAN_BLOB,"generation4_manifest_canonical":EXPECTED_MAN_CANON,
 "unit_consumer_blob_sha1":EXPECTED_UNIT_BLOB,"v47_exact_head":pf["v47_authority"]["source_exact_head"],"v47_upper_bound":str(V47_TOTAL)},
 "result":{"covered_v47_joint_survivors":str(base),"covered_v47_support_qbc_joint_survivors":str(ref),
 "exact_incremental_saving_vs_v47":str(saving),"same_population_replacement_upper_bound":str(V47_TOTAL-saving)},
 "accounting":{"additive_subtraction_of_raw_hpadj22_saving":False,"no_double_charge":True,"statistical_independence":False,
 "replacement_formula":"V47_total - covered_V47 + covered_V47_support_qBC"},
 "receipt_stream_sha256":stream.hexdigest(),
 "firewalls":{"main_credit_changed":False,"theorem_credit_changed":False,"endpoint_credit_changed":False,"merge":False,"hostile_audit_required":True}}
 out["canonical_sha256_without_this_field"]=canon(out)
 path=HERE/"V47-SUPPORT-QBC-INTERSECTION-AGGREGATE.json";path.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n")
 print(json.dumps(out["result"],sort_keys=True))
if __name__=="__main__":main()
