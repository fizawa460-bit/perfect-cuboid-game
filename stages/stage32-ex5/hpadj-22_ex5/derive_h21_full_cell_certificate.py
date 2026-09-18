#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

EXPECTED_ROWS=178
EXPECTED_CELLS=1424
EXPECTED_TOTAL=157570677819451133507
MISSING={20,21,44,88,171}

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def canonical(d):
    x=dict(d); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def load_rows(root:Path):
    out={}
    for p in sorted(root.rglob("hpadj21-row-*.json")):
        d=json.loads(p.read_text())
        if d.get("schema")!="STAGE32EX5_HPADJ21_FULL_QA_ROW_CERT_V1": continue
        req(d.get("canonical_sha256_without_this_field")==canonical(d),f"canonical drift {p}")
        idx=int(d["row"]["index"]); req(idx not in out,f"duplicate row {idx}")
        req(len(d["cell_records"])==8,f"cell coverage row {idx}")
        req(all(v is False for v in d["credit_firewall"].values()),f"credit firewall row {idx}")
        out[idx]=d
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--carry-dir",type=Path,required=True)
    ap.add_argument("--missing-dir",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    carry=load_rows(a.carry_dir); missing=load_rows(a.missing_dir)
    req(set(carry)==set(range(EXPECTED_ROWS))-MISSING,"173-row carry identity drift")
    req(set(missing)==MISSING,"missing-row reconstruction identity drift")
    rows={**carry,**missing}; req(set(rows)==set(range(EXPECTED_ROWS)),"FULL178 row coverage")
    compact=[]
    total=0
    for idx in range(EXPECTED_ROWS):
        d=rows[idx]
        cells=[]
        for pos,c in enumerate(d["cell_records"]):
            req(int(c["interval_position"])==pos,f"interval position {idx}/{pos}")
            floor=int(c["hpadj21_floor"]); req(int(c["hpadj21_num"])//int(c["hpadj21_den"])==floor,f"floor arithmetic {idx}/{pos}")
            total+=floor
            cells.append([int(c["hpadj21_num"]),int(c["hpadj21_den"]),floor,int(c["pre_mass"]),int(c["post_mass"])])
        compact.append([idx,d["row"]["row_id"],cells,d["canonical_sha256_without_this_field"]])
    req(total==EXPECTED_TOTAL,f"HPADJ21 FULL178 total drift {total}")
    out={
      "schema":"STAGE32EX5_HPADJ21_FULL178_CELL_FLOOR_CERT_V1",
      "status":"SCRATCH_DERIVED_FROM_EXISTING_AUDITED_HPADJ21_EVIDENCE__ZERO_NEW_CREDIT",
      "source":{
        "carry_run_id":35275839413,
        "carry_artifact_id":10519913594,
        "carry_artifact_digest":"sha256:366e93ff132652d830e86ab4a46392a1e0fd90185110863a9805fa0ef97f4499",
        "recovery_run_id":35279651998,
        "missing_rows":sorted(MISSING)
      },
      "coverage":{"rows":178,"cells":1424},
      "hpadj21_full178_cellwise_floor_sum":total,
      "rows":compact,
      "credit":{"new_mathematical_credit":False,"stage32_main_credit":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canonical(out)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print(json.dumps({"rows":178,"cells":1424,"total":total,"bytes":a.output.stat().st_size,"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__": main()
