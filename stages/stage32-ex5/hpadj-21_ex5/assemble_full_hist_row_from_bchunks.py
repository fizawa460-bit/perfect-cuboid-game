#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, importlib.util, json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
DIRECT=HERE/"run_full_hist_row.py"; DIRECT_BLOB="68a3edcf5be71bb75ed97959fcc5f56a2fcecbd7"
BCHUNK=HERE/"run_full_hist_bchunk.py"


def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)

def git_blob(path):
    raw=path.read_bytes(); return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def canonical(obj):
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None); return hashlib.sha256(json.dumps(body,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path); req(spec is not None and spec.loader is not None,"cannot load "+name); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def add_caps(dst, records):
    for s,B,m in records: dst[(int(s),int(B))]+=int(m)

def assemble(row_index:int, paths:list[Path])->dict:
    req(DIRECT.is_file() and git_blob(DIRECT)==DIRECT_BLOB,"direct worker drift")
    direct=load(DIRECT,"hpadj21_direct_for_bchunk_assembler"); bc=load(BCHUNK,"hpadj21_bchunk_for_assembler")
    p=direct.load_pilot(); h20=p.load_parent(); h19=h20.load_parent(); h18=h19.load_parent(); h17=h18.load_parent(); h16=h17.load_parent()
    p15=h16.load_module(h16.PARENT,h16.PARENT_BLOB,"hpadj15_for_hpadj21_bchunk_assembler"); p14=p15.load_parent(); counter=p14.load_counter()
    manifest=counter.load_locked_json(p14.MANIFEST,p14.LOCKS["manifest_blob"],p14.LOCKS["manifest_canonical"],"FULL178 manifest"); rows=counter.manifest_rows(manifest)
    row_id,g0,d0=rows[row_index]; g,d=int(g0),int(d0); h=d//2
    chunks=[]
    for f in paths:
        x=json.loads(f.read_text()); chunks.append(bc.validate(f,row_index,int(x["b_range"]["start"]),int(x["b_range"]["stop"])))
    chunks.sort(key=lambda x:int(x["b_range"]["start"])); cursor=0
    two={i:defaultdict(int) for i in range(len(p15.PLANNED))}; full={i:defaultdict(int) for i in range(len(p15.PLANNED))}
    classes=tuples=None
    for x in chunks:
        a,b=int(x["b_range"]["start"]),int(x["b_range"]["stop"]); req(a==cursor,f"b coverage gap/overlap at {cursor}"); cursor=b+1
        req(x["row"]["row_id"]==row_id and int(x["row"]["g"])==g and int(x["row"]["d"])==d,"row identity drift")
        classes=int(x["profile"]["classes_with_more_than_two_qA_bins"]) if classes is None else classes; tuples=int(x["profile"]["tuples_above_second_qA_level"]) if tuples is None else tuples
        for rec in x["interval_records"]:
            i=int(rec["interval_position"]); add_caps(two[i],rec["two_caps"]); add_caps(full[i],rec["full_caps"])
    req(cursor==h+1,"b coverage incomplete")
    rejected=p15.load_certificate(p14)
    two_total=Fraction(0,1); full_total=Fraction(0,1); two_floor=full_floor=pre_total=post_total=strict_cells=0; records=[]
    for i,interval in enumerate(p15.PLANNED):
        P=sum(two[i].values()); req(sum(full[i].values())==P,f"full/two pre-mass mismatch {i}"); R=int(rejected[(interval,g,d)]); req(0<=R<=P,"rejected mass drift"); Mpost=P-R
        tobj,_,_,_=h18.optimize_cell_exact_predomain(two[i],Mpost); fobj,_,_,_=h18.optimize_cell_exact_predomain(full[i],Mpost); req(fobj<=tobj,"full histogram weakened direct")
        tf=tobj.numerator//tobj.denominator; ff=fobj.numerator//fobj.denominator; req(ff<=tf,"floor weakened direct")
        strict=fobj<tobj; strict_cells+=int(strict); two_total+=tobj; full_total+=fobj; two_floor+=tf; full_floor+=ff; pre_total+=P; post_total+=Mpost
        records.append({"interval_position":i,"b_interval":list(interval),"pre_mass":P,"post_mass":Mpost,"hpadj20_num":tobj.numerator,"hpadj20_den":tobj.denominator,"hpadj20_floor":tf,"hpadj21_num":fobj.numerator,"hpadj21_den":fobj.denominator,"hpadj21_floor":ff,"strict":strict})
    out={"schema":direct.SCHEMA,"route_id":"HPADJ-21_ex5","status":"EXACT_FULL_QA_ROW_COMPLETE_HOSTILE_AUDIT_REQUIRED","row":{"index":row_index,"row_id":row_id,"g":g,"d":d},
         "source_locks":{"bounded_pilot_git_blob":direct.PILOT_BLOB,"hpadj20_parent_git_blob":p.PARENT_BLOB,"full178_manifest_blob_sha1":p14.LOCKS["manifest_blob"],"hpadj10_counter_blob_sha1":p14.LOCKS["hpadj10_counter_blob"]},
         "profile":{"classes_with_more_than_two_qA_bins":classes,"tuples_above_second_qA_level":tuples,"exact_qA_multiplicity_preserved":True},
         "totals":{"pre_mass":pre_total,"post_mass":post_total,"hpadj20_rational_num":two_total.numerator,"hpadj20_rational_den":two_total.denominator,"hpadj21_rational_num":full_total.numerator,"hpadj21_rational_den":full_total.denominator,"hpadj20_cellwise_floor_sum":two_floor,"hpadj21_cellwise_floor_sum":full_floor,"strict_cell_count":strict_cells,"floor_improvement":two_floor-full_floor},
         "cell_records":records,"semantics":{"same_population_as_hpadj20":True,"same_post_mass_constraints_as_hpadj20":True,"full_qA_histogram_exact_multiplicity":True,"additive_subtraction_used":False,"statistical_independence_assumed":False},
         "credit_firewall":{"partial_output_credit":False,"stage32_main_credit":False,"full178_completion_credit":False,"theorem_credit":False,"effectivity_credit":False,"receiver_credit":False,"endpoint_credit":False,"perfect_cuboid_credit":False,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=canonical(out); direct.validate_obj = getattr(direct,"validate_obj",None); return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--row-index",type=int,required=True); ap.add_argument("--chunks-dir",type=Path,required=True); ap.add_argument("--output",type=Path,required=True); a=ap.parse_args()
    paths=sorted(a.chunks_dir.rglob(f"hpadj21-bchunk-{a.row_index}-*.json")); req(paths,"no chunk certificates"); d=assemble(a.row_index,paths); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(d,sort_keys=True,separators=(",",":"))+"\n")
    direct=load(DIRECT,"hpadj21_direct_validate_assembled"); direct.validate(a.output,a.row_index); print(json.dumps({"row":a.row_index,"chunks":len(paths),"canonical":d["canonical_sha256_without_this_field"]},sort_keys=True))

if __name__=="__main__": main()
