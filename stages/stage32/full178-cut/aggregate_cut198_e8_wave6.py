#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path

SCHEMA = "STAGE32_CUT198_E8_COMMON_ADAPTER_WAVE6_AGGREGATE_V1"
SHARD_SCHEMA = "STAGE32_CUT198_E8_COMMON_ADAPTER_WAVE6_SHARD_V1"
EXPECTED_RANGES = [(1276,1307),(1308,1339),(1340,1371),(1372,1403),(1404,1435),(1436,1467),(1468,1499),(1500,1530)]
MAIN_V12_TERMINALS = 65396964990500233636101
PRIOR = {"cut193":25651,"cut194":26442,"cut195":26216,"cut196":27346,"cut197":28250}

def csha(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def req(ok,msg):
    if not ok: raise RuntimeError(msg)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--input-dir",type=Path,required=True); ap.add_argument("--output",type=Path,required=True); args=ap.parse_args()
    files=sorted(args.input_dir.glob("cut198-shard-*.json")); req(len(files)==8,f"expected 8 shards, got {len(files)}")
    shards=[json.loads(p.read_text()) for p in files]
    ranges=sorted(tuple(s["target"]["survivor_offset_range"]) for s in shards); req(ranges==EXPECTED_RANGES,f"shard ranges drift: {ranges}")
    for s in shards:
        q=dict(s); claimed=q.pop("canonical_sha256_without_this_field",None)
        req(s["schema"]==SHARD_SCHEMA and claimed==csha(q),"shard canonical/schema drift")
        req(s["credit"]["stage32_main_pruning_credit"] is False,"shard MAIN credit leak")
        req(s["firewalls"]["main_authority_mutated"] is False,"shard MAIN mutation leak")
        for k in ["cut191_block0_disjoint","cut193_wave1_disjoint","cut194_wave2_disjoint","cut195_wave3_disjoint","cut196_wave4_disjoint","cut197_wave5_disjoint","n356_preserved_all_wave_blocks"]:
            req(s["target"][k] is True,f"target firewall drift: {k}")
    ordered=sorted(shards,key=lambda x:x["target"]["survivor_offset_range"][0]); all_blocks=[]; closed=[]; recs=[]; methods={}
    for s in ordered:
        all_blocks += s["target"]["block_indices"]; closed += s["result"]["candidate_closed_block_indices"]; recs += s["result"]["blocks"]
        for k,v in s["result"]["method_counts"].items(): methods[k]=methods.get(k,0)+int(v)
    req(len(all_blocks)==255 and len(set(all_blocks))==255,"wave6 block population drift")
    req(len(recs)==255 and sorted(r["block_index"] for r in recs)==sorted(all_blocks),"block record coverage drift")
    req(all(r["n356_lhs_b_minus_c"]<=4 for r in recs),"N356 bridge regression")
    closed=sorted(int(v) for v in closed); req(len(closed)==len(set(closed)),"duplicate closed block")
    h=hashlib.sha256(); ch=hashlib.sha256()
    for i in all_blocks: h.update(f"{i}\n".encode())
    for i in closed: ch.update(f"{i}\n".encode())
    candidate=113*len(closed); zero_hnf=sum(r["method"]=="HNF_PARENT_POPULATION_EMPTY" for r in recs); whole=sum(r["method"]=="WHOLE_BLOCK_FINITE_RING_UNSAT" for r in recs); parent_all=sum(r["method"]=="ALL_HNF_PARENTS_FINITE_RING_UNSAT" for r in recs); residual=sum(not r["closed_candidate"] for r in recs)
    req(zero_hnf+whole+parent_all+residual==255,"method partition drift")
    body={
      "schema":SCHEMA,"stage":"32","surface":"full178-cut","node":"CUT198","status":"WAVE6_CANDIDATE_AUDIT_REQUIRED",
      "source":{"cut197_pr":1798,"cut197_audited_exact_head":"adce53dc9004c24bffb3ba9f88e9d5d6e51cf6a5","cut197_exact_head_ci":34694659965,"cut197_hostile_audit_review":5186601376,"cut197_audited_candidate_pruned_terminals":PRIOR["cut197"],"cut196_audited_candidate_pruned_terminals":PRIOR["cut196"],"cut195_audited_candidate_pruned_terminals":PRIOR["cut195"],"cut194_audited_candidate_pruned_terminals":PRIOR["cut194"],"cut193_audited_candidate_pruned_terminals":PRIOR["cut193"],"main_v12_exact_head":"6d63d798adb50dd4efc5f0d5abc553b3dfa23060","ex5_producer_exact_head":"fd00531181228c9f367a49eb61ddc3af6ab84ab3","ex5_producer_ci_run":34598945799},
      "target":{"row_id":"g1-d008","g":1,"d":8,"e":8,"survivor_offset_range":[1276,1530],"block_count":255,"terminal_count":28815,"block_indices":all_blocks,"block_index_stream_sha256":h.hexdigest(),"cut191_block0_disjoint":True,"cut193_wave1_disjoint":True,"cut194_wave2_disjoint":True,"cut195_wave3_disjoint":True,"cut196_wave4_disjoint":True,"cut197_wave5_disjoint":True,"n356_preserved_all_wave_blocks":True},
      "result":{"candidate_closed_block_indices":closed,"candidate_closed_block_count":len(closed),"candidate_closed_block_stream_sha256":ch.hexdigest(),"candidate_pruned_terminals":candidate,"candidate_post_wave6_from_main_v12_terminals":MAIN_V12_TERMINALS-candidate,"candidate_post_cut193_cut194_cut195_cut196_cut197_cut198_from_main_v12_terminals":MAIN_V12_TERMINALS-sum(PRIOR.values())-candidate,"remaining_nonclosed_block_count":residual,"method_counts":methods,"hnf_empty_block_count":zero_hnf,"whole_block_finite_ring_unsat_count":whole,"all_parent_finite_ring_unsat_block_count":parent_all},
      "credit":{"stage32_main_pruning_credit":False,"cut198_pruning_credit":False,"full178_complete":False,"theorem_credit":False,"endpoint_credit":False,"merge_authorized":False},
      "firewalls":{"hostile_audit_required":True,"main_authority_mutated":False,"cut191_double_counted":False,"cut193_wave1_double_counted":False,"cut194_wave2_double_counted":False,"cut195_wave3_double_counted":False,"cut196_wave4_double_counted":False,"cut197_wave5_double_counted":False,"n356_double_counted":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False}}
    body["canonical_sha256_without_this_field"]=csha(body); args.output.write_text(json.dumps(body,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"status":body["status"],"closed_blocks":len(closed),"candidate_pruned_terminals":candidate,"remaining_nonclosed_blocks":residual,"methods":methods,"canonical":body["canonical_sha256_without_this_field"]},sort_keys=True))
if __name__=="__main__": main()
