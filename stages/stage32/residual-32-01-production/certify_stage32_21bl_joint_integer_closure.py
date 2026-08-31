#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from z3 import Int, Solver, get_version_string, sat, unknown, unsat
from audit_stage32_21be_r51_endpoints import EXPECTED_TRIPLES, predicted_lo
from certify_stage32_21ba_r51_interval_census import prism_triples
from certify_stage32_21bc_pair_combination_projection import CANDIDATE_BOUNDS
from certify_stage32_21bf_r49_per_triple_projection import build_21bf_solver
from certify_stage32_21bg_r42_per_triple_projection import r49_hi
from certify_stage32_21bh_r54_per_triple_projection import r42_lo
from certify_stage32_21bj_r56_per_triple_projection import r57_hi
from certify_stage32_21bk_r20_final_single_coordinate import (
    EXPECTED_21BI_LOCK_SHA256, EXPECTED_21BJ_LOCK_SHA256, load_canonical_lock, r56_lo,
)
from direct_picard_reynolds_lattice_diagnostic import csha

RANK=59
SCHEMA_SHARD="STAGE32_21BL_EXACT_JOINT_INTEGER_CLOSURE_SHARD_V1"
SCHEMA_AGG="STAGE32_21BL_EXACT_JOINT_INTEGER_CLOSURE_AGGREGATE_V1"
EXPECTED_21BK_EVIDENCE_CANONICAL="c39ba719e648104cd62a8f87bd739f5933725fcd71cc0cca56397692f1036c57"
EXPECTED_21BH_LOCK_CANONICAL="23a732fd232cf025533cb9ef17c6ab482a5a50a860d163731a346faca7a11c6d"

def sha(path: Path)->str: return hashlib.sha256(path.read_bytes()).hexdigest()

def load_21bk_evidence(path: Path)->dict:
    x=json.loads(path.read_text()); claimed=x.pop("canonical_sha256_without_this_field")
    if claimed!=EXPECTED_21BK_EVIDENCE_CANONICAL or csha(x)!=claimed: raise ValueError("21bk evidence canonical regression")
    if x.get("status")!="PASS_EXACT_21BK_R20_FINAL_SINGLE_COORDINATE_PROJECTION" or x["result"]["open_triples"]!=EXPECTED_TRIPLES or x["result"]["unknown_triples"]!=0: raise ValueError("21bk evidence status regression")
    return x

def load_21bh_lock(path: Path):
    x=json.loads(path.read_text()); claimed=x.pop("canonical_sha256_without_this_field")
    if claimed!=EXPECTED_21BH_LOCK_CANONICAL or csha(x)!=claimed: raise ValueError("21bh lossless table canonical regression")
    if x.get("status")!="PASS_EXACT_21BH_R54_PER_TRIPLE_PROJECTION": raise ValueError("21bh lossless table is not exact PASS")
    cov=x.get("coverage",{})
    if cov.get("expected_triples")!=EXPECTED_TRIPLES or cov.get("open_triples")!=EXPECTED_TRIPLES or cov.get("unknown_triples")!=0 or cov.get("exact_integer_pruned_triples")!=0: raise ValueError("21bh lossless table coverage regression")
    table=x.get("lossless_r54_interval_table",{})
    if table.get("r27_start")!=-96 or table.get("r27_end")!=-48 or table.get("upper")!=-132 or not table.get("verified_against_all_3234_exact_21bh_rows"): raise ValueError("21bh lossless table metadata regression")
    return x,table

def r54_lo_from_table(table: dict, r50: int, r55: int, r27: int) -> int:
    delta=r50-r55-129
    if delta not in table.get("delta_values",[]): raise ValueError(f"21bh delta outside lock: {delta}")
    start=int(table["r27_start"]); end=int(table["r27_end"])
    if not start<=r27<=end: raise ValueError(f"r27 outside 21bh table: {r27}")
    offset=r27-start
    seen=0
    for value,count in table["lower_rle_by_delta"][str(delta)]:
        count=int(count)
        if offset < seen+count: return int(value)
        seen += count
    raise ValueError("21bh RLE did not cover r27")

def build_joint(args):
    load_21bk_evidence(args.tenth_lock)
    load_canonical_lock(args.eighth_lock,EXPECTED_21BI_LOCK_SHA256,"PASS_EXACT_21BI_R57_AFTER_TARGETED_UNKNOWN_RESCUE")
    load_canonical_lock(args.ninth_lock,EXPECTED_21BJ_LOCK_SHA256,"PASS_EXACT_21BJ_R56_PER_TRIPLE_PROJECTION")
    _,r54_table=load_21bh_lock(args.seventh_lock)
    lra,r,target=build_21bf_solver(args)
    if len(r)!=RANK: raise ValueError("rank regression")
    if CANDIDATE_BOUNDS.get(20)!=(86,132): raise ValueError("r20 bound regression")
    s=Solver(); s.set(timeout=args.per_check_timeout_ms); s.add(*lra.assertions())
    ri=[Int(f"ri_{j}") for j in range(RANK)]
    for j in range(RANK): s.add(r[j]==ri[j])
    return s,r,ri,target,r54_table

def bands_for(triple,table):
    r50,r55,r27=triple
    return {51:(predicted_lo(r50,r55,r27),-132),49:(132,r49_hi(r27)),42:(r42_lo(r50,r55,r27),79),54:(r54_lo_from_table(table,r50,r55,r27),-132),57:(0,r57_hi(r27)),56:(r56_lo(r50,r55,r27),60)}

def run_shard(args):
    triples=list(prism_triples())
    if len(triples)!=EXPECTED_TRIPLES: raise ValueError("prism count regression")
    start=EXPECTED_TRIPLES*args.shard_index//args.shard_count; end=EXPECTED_TRIPLES*(args.shard_index+1)//args.shard_count
    s,r,ri,target,table=build_joint(args)
    unsat_rows=[]; sat_rows=[]; unknown_rows=[]
    for ordinal in range(start,end):
        triple=triples[ordinal]; b=bands_for(triple,table); s.push()
        s.add(r[50]==triple[0],r[55]==triple[1],r[27]==triple[2])
        for j,(lo,hi) in b.items(): s.add(r[j]>=lo,r[j]<=hi)
        try:
            out=s.check()
            if out==unsat: unsat_rows.append(ordinal)
            elif out==unknown: unknown_rows.append({"ordinal":ordinal,"triple":list(triple),"reason":s.reason_unknown()})
            elif out==sat:
                m=s.model(); witness=[m.eval(ri[j],model_completion=True).as_long() for j in range(RANK)]
                sat_rows.append({"ordinal":ordinal,"triple":list(triple),"witness_r_reduced":witness})
            else: raise RuntimeError(out)
        finally: s.pop()
        if (ordinal-start+1)%50==0: print(json.dumps({"shard":args.shard_index,"processed":ordinal-start+1,"unsat":len(unsat_rows),"sat":len(sat_rows),"unknown":len(unknown_rows)}),flush=True)
    payload={"schema":SCHEMA_SHARD,"stage":32,"leaf":"32-21bl","mode":"EXACT_59D_JOINT_INTEGER_CLOSURE_PER_FIXED_TRIPLE","source_21bk_evidence_canonical_sha256":EXPECTED_21BK_EVIDENCE_CANONICAL,"z3_version":get_version_string(),"target":target,"partition":{"shard_index":args.shard_index,"shard_count":args.shard_count,"start_ordinal":start,"end_ordinal_exclusive":end,"expected_rows":end-start},"result":{"processed_rows":end-start,"integer_unsat_count":len(unsat_rows),"integer_sat_count":len(sat_rows),"unknown_count":len(unknown_rows),"unsat_ordinals":unsat_rows,"sat_witnesses":sat_rows,"unknown_rows":unknown_rows},"interpretation":{"all_59_unimodular_reduced_coordinates_are_constrained_integer_simultaneously":True,"six_prior_lossless_coordinate_bands_and_42_pair_cuts_are_sound_pruning_only":True,"sat_contains_exact_fixed_projection_integer_witness":True,"unsat_prunes_only_the_fixed_triple":True,"unknown_is_not_unsat":True,"fixed_projection_unsat_is_not_slice_unsat":True,"representative_sample_only":True,"not_full178_numerical_credit":True},"safety":{"heavy_run_key_used":True,"full178_production_run":False,"integer_solver_used":True,"theorem_credit":False,"receiver_credit":False,"route_credit":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False}}
    payload["canonical_sha256_without_this_field"]=csha(payload); args.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":"PASS_SHARD" if not unknown_rows else "SHARD_WITH_UNKNOWN","canonical":payload["canonical_sha256_without_this_field"],"unsat":len(unsat_rows),"sat":len(sat_rows),"unknown":len(unknown_rows)}),flush=True)

def run_aggregate(args):
    files=sorted(args.input_dir.glob("**/stage32-21bl-joint-*.json"))
    if len(files)!=args.shard_count: raise ValueError(f"expected {args.shard_count} shards, got {len(files)}")
    shards=[]; sources=[]
    for p in files:
        x=json.loads(p.read_text()); claimed=x.pop("canonical_sha256_without_this_field")
        if x.get("schema")!=SCHEMA_SHARD or csha(x)!=claimed: raise ValueError(f"bad shard {p}")
        x["canonical_sha256_without_this_field"]=claimed; shards.append(x); sources.append({"file":p.name,"raw_sha256":sha(p),"canonical_sha256":claimed})
    shards.sort(key=lambda x:x["partition"]["shard_index"]); expected=0; uns=[]; sats=[]; unknowns=[]
    for idx,x in enumerate(shards):
        p=x["partition"]
        if p["shard_index"]!=idx or p["shard_count"]!=args.shard_count or p["start_ordinal"]!=expected: raise ValueError("partition regression")
        expected=p["end_ordinal_exclusive"]; rr=x["result"]; uns.extend(rr["unsat_ordinals"]); sats.extend(rr["sat_witnesses"]); unknowns.extend(rr["unknown_rows"])
    complete=expected==EXPECTED_TRIPLES and len(uns)+len(sats)+len(unknowns)==EXPECTED_TRIPLES and len(set(uns+[x["ordinal"] for x in sats]+[x["ordinal"] for x in unknowns]))==EXPECTED_TRIPLES
    if not complete: status="FAIL_INCOMPLETE_21BL"
    elif unknowns: status="UNKNOWN_REMAINS_21BL"
    elif sats: status="PASS_EXACT_21BL_INTEGER_SAT_WITNESS_FOUND"
    else: status="PASS_EXACT_21BL_FIXED_PROJECTION_INTEGER_UNSAT"
    payload={"schema":SCHEMA_AGG,"stage":32,"leaf":"32-21bl","status":status,"source_21bk_evidence_canonical_sha256":EXPECTED_21BK_EVIDENCE_CANONICAL,"coverage":{"expected_triples":EXPECTED_TRIPLES,"complete_partition":complete,"integer_unsat_triples":len(uns),"integer_sat_triples":len(sats),"unknown_triples":len(unknowns)},"unsat_ordinals":sorted(uns),"sat_witnesses":sorted(sats,key=lambda x:x["ordinal"]),"unknown_rows":sorted(unknowns,key=lambda x:x["ordinal"]),"shard_sources":sources,"interpretation":{"all_3234_fixed_triple_cases_checked_in_the_same_59d_integer_model":complete,"integer_sat_is_fixed_projection_only_not_perfect_cuboid":True,"all_unsat_and_unknown_zero_closes_only_this_fixed_projection":True,"fixed_projection_unsat_is_not_slice_unsat":True,"representative_sample_only":True,"not_full178_numerical_credit":True},"safety":{"theorem_credit":False,"receiver_credit":False,"route_credit":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False}}
    payload["canonical_sha256_without_this_field"]=csha(payload); args.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n"); print(json.dumps({"status":status,"canonical":payload["canonical_sha256_without_this_field"],**payload["coverage"]}),flush=True)

def common(p):
    p.add_argument("--source-lock",type=Path,required=True); p.add_argument("--formula-lock",type=Path,required=True); p.add_argument("--pair-lock",type=Path,required=True); p.add_argument("--audit-lock",type=Path,required=True); p.add_argument("--seventh-lock",type=Path,required=True); p.add_argument("--eighth-lock",type=Path,required=True); p.add_argument("--ninth-lock",type=Path,required=True); p.add_argument("--tenth-lock",type=Path,required=True); p.add_argument("--retained",type=Path,required=True); p.add_argument("--marking",type=Path,required=True); p.add_argument("--per-check-timeout-ms",type=int,default=5000)

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd",required=True); s=sub.add_parser("shard"); common(s); s.add_argument("--shard-index",type=int,required=True); s.add_argument("--shard-count",type=int,required=True); s.add_argument("--output",type=Path,required=True); a=sub.add_parser("aggregate"); a.add_argument("--input-dir",type=Path,required=True); a.add_argument("--shard-count",type=int,required=True); a.add_argument("--output",type=Path,required=True); args=ap.parse_args(); run_shard(args) if args.cmd=="shard" else run_aggregate(args)
if __name__=="__main__": main()
