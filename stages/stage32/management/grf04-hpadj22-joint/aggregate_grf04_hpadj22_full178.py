#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

WORKER_BLOB="c9fbf71242581f096718ebf0dbc9ac88878c91f1"
HELPER_BLOB="99eef03657b07eb5cf86be8d880050fd8aa2d13b"
SOURCE_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
PARENT_SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_PARENT_V1"
ROW_SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_ROW_CHUNK_V1"
SCHEMA="STAGE32_MAIN_V46_GRF04_HPADJ22_FULL178_AGGREGATE_V1"
BANDS=((0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96))
EXPECTED_BAND_BASELINES=(
  741770765552823405,
  7696074963214187236,
  22467171299110639029,
  35641966335542218797,
  36265487246132086252,
  24348355963238288318,
  10085548271692058832,
  1406364956168291625,
)
EXPECTED_GLOBAL_BASELINE=138652739800650593494

def req(v,m):
    if not v:raise SystemExit("FAIL: "+m)

def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def chunks_for_band(pos):
    lo,hi=BANDS[pos];n=hi-lo+1;q,r=divmod(n,4);out=[];cur=lo
    for i in range(4):
      w=q+(1 if i<r else 0);out.append((cur,cur+w-1));cur+=w
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--parents-root",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()

    parents={}
    row_seen=set()
    for p in sorted(a.parents_root.rglob("PARENT-COMPLETE.json")):
      d=json.loads(p.read_text())
      req(d.get("schema")==PARENT_SCHEMA,f"parent schema drift {p}")
      req(d.get("canonical_sha256_without_this_field")==canon(d),f"parent canonical drift {p}")
      s=d["source_locks"]
      req(s["production_worker_blob_sha1"]==WORKER_BLOB,"parent worker lock drift")
      req(s["helper_blob_sha1"]==HELPER_BLOB,"parent helper lock drift")
      req(s["hpadj22_source_head"]==SOURCE_HEAD,"parent source head drift")
      q=d["parent"];key=(int(q["band_position"]),int(q["chunk_position"]))
      req(key not in parents,f"duplicate parent {key}")
      b0,b1=chunks_for_band(key[0])[key[1]]
      req(q["b_chunk"]==[b0,b1],f"parent chunk interval drift {key}")
      cov=d["coverage"]
      req(cov["gaps"]==0 and cov["overlaps"]==0,f"parent coverage drift {key}")
      expected=set(int(x) for x in cov["expected_computed_rows"])
      implicit=set(int(x) for x in cov["implicit_zero_rows"])
      req(expected.isdisjoint(implicit) and expected|implicit==set(range(178)),f"row partition drift {key}")
      req(cov["computed_row_count"]==len(expected) and cov["implicit_zero_row_count"]==len(implicit),f"row counts drift {key}")
      parents[key]=d

      parent_dir=p.parent
      certs={}
      for rp in parent_dir.glob("row-*.json"):
        rd=json.loads(rp.read_text())
        if rd.get("schema")!=ROW_SCHEMA:continue
        req(rd.get("canonical_sha256_without_this_field")==canon(rd),f"row canonical drift {rp}")
        t=rd["target"];ri=int(t["row_index"])
        req((int(t["band_position"]),int(t["chunk_position"]))==key,f"row parent identity drift {rp}")
        req(t["b_chunk"]==[b0,b1],f"row b chunk drift {rp}")
        rs=rd["source_locks"]
        req(rs["production_worker_blob_sha1"]==WORKER_BLOB,f"row worker drift {rp}")
        req(rs["helper_blob_sha1"]==HELPER_BLOB,f"row helper drift {rp}")
        req(rs["hpadj22_source_head"]==SOURCE_HEAD,f"row source drift {rp}")
        req(ri in expected and ri not in certs,f"row coverage/duplicate drift {key} row={ri}")
        rr=rd["result"]
        req(int(rr["joint_exact_survivors"])<=int(rr["hpadj22_exact_survivors"]),f"row weakened baseline {key} row={ri}")
        certs[ri]=rd
        global_key=(key[0],key[1],ri)
        req(global_key not in row_seen,"global duplicate row-chunk")
        row_seen.add(global_key)
      req(set(certs)==expected,f"missing row certificates {key}: {sorted(expected-set(certs))[:8]}")
      pb=sum(int(certs[i]["result"]["hpadj22_exact_survivors"]) for i in expected)
      pj=sum(int(certs[i]["result"]["joint_exact_survivors"]) for i in expected)
      req(pb==int(d["result"]["hpadj22_exact_survivors"]),f"parent baseline replay drift {key}")
      req(pj==int(d["result"]["joint_exact_survivors"]),f"parent joint replay drift {key}")

    expected_parents={(b,c) for b in range(8) for c in range(4)}
    req(set(parents)==expected_parents,f"parent coverage incomplete missing={sorted(expected_parents-set(parents))}")
    req(len(row_seen)==sum(int(d["coverage"]["computed_row_count"]) for d in parents.values()),"row-chunk global coverage count drift")

    band_summaries=[];global_b=global_j=0
    for band in range(8):
      ps=[parents[(band,c)] for c in range(4)]
      b=sum(int(x["result"]["hpadj22_exact_survivors"]) for x in ps)
      j=sum(int(x["result"]["joint_exact_survivors"]) for x in ps)
      req(b==EXPECTED_BAND_BASELINES[band],f"band{band} HPADJ22 baseline mismatch {b}!={EXPECTED_BAND_BASELINES[band]}")
      req(j<=b,f"band{band} joint weakened baseline")
      global_b+=b;global_j+=j
      band_summaries.append({"band_position":band,"b_interval":list(BANDS[band]),
        "hpadj22_exact_survivors":str(b),"joint_exact_survivors":str(j),
        "exact_improvement":str(b-j),"strict":j<b,
        "parent_canonicals":[parents[(band,c)]["canonical_sha256_without_this_field"] for c in range(4)]})
    req(global_b==EXPECTED_GLOBAL_BASELINE,f"global HPADJ22 baseline mismatch {global_b}")
    req(global_j<=global_b,"global joint weakened baseline")

    out={
      "schema":SCHEMA,"stage":32,
      "status":"EXACT_FULL178_JOINT_AGGREGATE_ZERO_CREDIT_HOSTILE_AUDIT_REQUIRED",
      "coverage":{"bands":8,"chunks_per_band":4,"parents":32,"rows":178,
        "row_chunk_certificates":len(row_seen),"gaps":0,"overlaps":0},
      "source_locks":{"production_worker_blob_sha1":WORKER_BLOB,"helper_blob_sha1":HELPER_BLOB,
        "hpadj22_source_head":SOURCE_HEAD},
      "totals":{"hpadj22_exact_survivors":str(global_b),"joint_exact_survivors":str(global_j),
        "exact_improvement":str(global_b-global_j),"strict":global_j<global_b},
      "bands":band_summaries,
      "composition":{"same_population_exact_intersection":True,"additive_subtraction":False,
        "min_of_counts":False,"statistical_independence":False,
        "retained_hpadj22_band_totals_replayed_exactly":True},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,
        "hostile_audit_required_before_promotion":True,"theorem_credit":False,
        "effectivity_credit":False,"receiver_credit":False,"route_credit":False,
        "endpoint_credit":False,"stage32_closed":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("FULL178_AGG="+json.dumps({"baseline":str(global_b),"joint":str(global_j),
      "improvement":str(global_b-global_j),"strict":global_j<global_b,
      "row_chunk_certificates":len(row_seen),"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__":main()
