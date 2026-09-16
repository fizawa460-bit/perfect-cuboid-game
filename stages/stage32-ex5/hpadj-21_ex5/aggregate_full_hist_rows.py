#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKER = HERE / "run_full_hist_row.py"
WORKER_BLOB = "68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
EXPECTED_ROWS = 178
EXPECTED_HPADJ20_CELLWISE_FLOOR = 179119009547804181594


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def canonical(obj: dict) -> str:
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":")).encode()).hexdigest()


def load_worker():
    req(WORKER.is_file() and git_blob(WORKER)==WORKER_BLOB,"HPADJ21 row worker blob drift")
    spec=importlib.util.spec_from_file_location("hpadj21_row_locked_for_union",WORKER)
    req(spec is not None and spec.loader is not None,"cannot load HPADJ21 row worker")
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


def aggregate(paths: list[Path]) -> dict:
    w=load_worker(); p=w.load_pilot(); h20=p.load_parent(); h19=h20.load_parent(); h18=h19.load_parent(); h17=h18.load_parent(); h16=h17.load_parent()
    p15=h16.load_module(h16.PARENT,h16.PARENT_BLOB,"hpadj15_locked_for_hpadj21_union"); p14=p15.load_parent(); counter=p14.load_counter()
    manifest=counter.load_locked_json(p14.MANIFEST,p14.LOCKS["manifest_blob"],p14.LOCKS["manifest_canonical"],"FULL178 manifest")
    rows=counter.manifest_rows(manifest); req(len(rows)==EXPECTED_ROWS,"FULL178 manifest row count drift")

    by_index={}
    for path in paths:
        req(path.is_file(),f"missing input {path}")
        raw=json.loads(path.read_text()); idx=int(raw.get("row",{}).get("index",-1))
        req(0<=idx<EXPECTED_ROWS,f"row index out of range in {path}")
        req(idx not in by_index,f"duplicate row index {idx}")
        d=w.validate(path,idx)
        row_id,g,dv=rows[idx]
        req(d["row"]["row_id"]==row_id and int(d["row"]["g"])==int(g) and int(d["row"]["d"])==int(dv),f"manifest identity mismatch row {idx}")
        by_index[idx]=(path,d)
    req(set(by_index)==set(range(EXPECTED_ROWS)),f"FULL178 row coverage gap: have {len(by_index)}")

    h20_rat=Fraction(0,1); h21_rat=Fraction(0,1)
    h20_floor=h21_floor=pre=post=strict_cells=0
    row_stream=hashlib.sha256(); row_summaries=[]
    for idx in range(EXPECTED_ROWS):
        path,d=by_index[idx]; t=d["totals"]
        r20=Fraction(int(t["hpadj20_rational_num"]),int(t["hpadj20_rational_den"])); r21=Fraction(int(t["hpadj21_rational_num"]),int(t["hpadj21_rational_den"]))
        req(r21<=r20,f"row {idx} rational weakening")
        f20=int(t["hpadj20_cellwise_floor_sum"]); f21=int(t["hpadj21_cellwise_floor_sum"]); req(f21<=f20,f"row {idx} floor weakening")
        h20_rat+=r20; h21_rat+=r21; h20_floor+=f20; h21_floor+=f21; pre+=int(t["pre_mass"]); post+=int(t["post_mass"]); strict_cells+=int(t["strict_cell_count"])
        compact={"row_index":idx,"row_id":d["row"]["row_id"],"g":int(d["row"]["g"]),"d":int(d["row"]["d"]),"canonical":d["canonical_sha256_without_this_field"],"hpadj20_floor":f20,"hpadj21_floor":f21,"floor_improvement":f20-f21,"strict_cells":int(t["strict_cell_count"])}
        row_summaries.append(compact); row_stream.update(json.dumps(compact,sort_keys=True,separators=(",",":")).encode()+b"\n")

    req(h20_floor==EXPECTED_HPADJ20_CELLWISE_FLOOR,f"HPADJ20 aggregate replay drift {h20_floor}")
    req(h21_floor<=h20_floor,"HPADJ21 aggregate weakened HPADJ20")
    req(strict_cells>0 and h21_rat<h20_rat and h21_floor<h20_floor,"HPADJ21 full aggregate lacks strict gain")
    out={
      "schema":"STAGE32EX5_HPADJ21_FULL_QA_HISTOGRAM_FULL178_AGGREGATE_V1","route_id":"HPADJ-21_ex5","status":"EXACT_FULL178_FULL_QA_HISTOGRAM_CANDIDATE_HOSTILE_AUDIT_REQUIRED",
      "coverage":{"expected_rows":EXPECTED_ROWS,"received_rows":len(by_index),"row_gaps":0,"row_overlaps":0,"manifest_blob_sha1":p14.LOCKS["manifest_blob"],"row_certificate_stream_sha256":row_stream.hexdigest()},
      "source_locks":{"row_worker_git_blob":WORKER_BLOB,"hpadj20_parent_git_blob":p.PARENT_BLOB,"hpadj20_expected_cellwise_floor":EXPECTED_HPADJ20_CELLWISE_FLOOR},
      "totals":{"pre_mass":pre,"post_mass":post,"hpadj20_rational_num":h20_rat.numerator,"hpadj20_rational_den":h20_rat.denominator,"hpadj21_rational_num":h21_rat.numerator,"hpadj21_rational_den":h21_rat.denominator,"hpadj20_cellwise_floor_sum":h20_floor,"hpadj21_cellwise_floor_sum":h21_floor,"strict_cell_count":strict_cells,"improvement_vs_hpadj20":h20_floor-h21_floor},
      "composition":{"rule":"DIRECT_REFINEMENT_OF_SAME_POPULATION_LP__NO_ADDITIVE_SUBTRACTION","same_pre_domain_population":True,"same_post_mass_constraints":True,"exact_qA_histogram_multiplicity":True},
      "row_summaries":row_summaries,
      "firewalls":{"hostile_audit_required":True,"stage32_main_pruning_credit":False,"current_main_incremental_credit":False,"effectivity_credit":False,"receiver_credit":False,"theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_credit":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=canonical(out); return out


def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("inputs",nargs="+"); ap.add_argument("--output",type=Path); args=ap.parse_args()
    paths=[]
    for item in args.inputs:
        p=Path(item)
        if p.is_dir(): paths.extend(sorted(p.glob("*.json")))
        else: paths.append(p)
    out=aggregate(paths)
    text=json.dumps(out,sort_keys=True,separators=(",",":"))+"\n"
    if args.output: args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text)
    print(json.dumps({"rows":out["coverage"]["received_rows"],"hpadj20":out["totals"]["hpadj20_cellwise_floor_sum"],"hpadj21":out["totals"]["hpadj21_cellwise_floor_sum"],"improvement":out["totals"]["improvement_vs_hpadj20"],"strict_cells":out["totals"]["strict_cell_count"],"canonical":out["canonical_sha256_without_this_field"]},sort_keys=True))


if __name__=="__main__": main()
