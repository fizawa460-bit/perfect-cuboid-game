#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

SCHEMA="STAGE32_CUT193_E8_COMMON_ADAPTER_WAVE1_AGGREGATE_V1"
SHARD_SCHEMA="STAGE32_CUT193_E8_COMMON_ADAPTER_WAVE1_SHARD_V1"
EXPECTED_RANGES=[(1,32),(33,64),(65,96),(97,128),(129,160),(161,192),(193,224),(225,255)]
MAIN_TERMINALS=65396964990500233636101

def csha(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",", ":")).encode()).hexdigest()
def req(ok,msg):
    if not ok: raise RuntimeError(msg)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input-dir',type=Path,required=True); ap.add_argument('--output',type=Path,required=True); args=ap.parse_args()
    files=sorted(args.input_dir.glob('cut193-shard-*.json'))
    req(len(files)==8,f'expected 8 shards, got {len(files)}')
    shards=[json.loads(p.read_text()) for p in files]
    ranges=sorted(tuple(s['target']['survivor_offset_range']) for s in shards)
    req(ranges==EXPECTED_RANGES,f'shard ranges drift: {ranges}')
    for s in shards:
        claimed=s.get('canonical_sha256_without_this_field'); q=dict(s); q.pop('canonical_sha256_without_this_field',None)
        req(s['schema']==SHARD_SCHEMA and claimed==csha(q),'shard canonical/schema drift')
        req(s['credit']['stage32_main_pruning_credit'] is False and s['firewalls']['main_authority_mutated'] is False,'shard credit leak')
        req(s['target']['cut191_block0_disjoint'] is True and s['target']['n356_preserved_all_wave_blocks'] is True,'current MAIN bridge drift')
    all_blocks=[]; closed=[]; recs=[]; method_counts={}
    for s in sorted(shards,key=lambda x:x['target']['survivor_offset_range'][0]):
        all_blocks.extend(s['target']['block_indices']); closed.extend(s['result']['candidate_closed_block_indices']); recs.extend(s['result']['blocks'])
        for k,v in s['result']['method_counts'].items(): method_counts[k]=method_counts.get(k,0)+int(v)
    req(len(all_blocks)==255 and len(set(all_blocks))==255 and 0 not in all_blocks,'wave block population drift')
    req(len(recs)==255 and sorted(r['block_index'] for r in recs)==sorted(all_blocks),'block record coverage drift')
    req(all(r['n356_lhs_b_minus_c']<=4 for r in recs),'N356 bridge regression')
    closed=sorted(closed); req(len(closed)==len(set(closed)),'duplicate closed block')
    h=hashlib.sha256(); ch=hashlib.sha256()
    for i in all_blocks:h.update(f'{i}\n'.encode())
    for i in closed:ch.update(f'{i}\n'.encode())
    candidate=113*len(closed)
    zero_hnf=sum(1 for r in recs if r['method']=='HNF_PARENT_POPULATION_EMPTY')
    whole=sum(1 for r in recs if r['method']=='WHOLE_BLOCK_FINITE_RING_UNSAT')
    parent_all=sum(1 for r in recs if r['method']=='ALL_HNF_PARENTS_FINITE_RING_UNSAT')
    residual=sum(1 for r in recs if not r['closed_candidate'])
    req(zero_hnf+whole+parent_all+residual==255,'method partition drift')
    body={"schema":SCHEMA,"stage":"32","surface":"full178-cut","node":"CUT193","status":"WAVE1_CANDIDATE_AUDIT_REQUIRED","source":{"main_parent_exact_head":"6d63d798adb50dd4efc5f0d5abc553b3dfa23060","main_parent_external_reaudit_review":5178420739,"ex5_producer_exact_head":"fd00531181228c9f367a49eb61ddc3af6ab84ab3","ex5_producer_ci_run":34598945799,"ex5_wave_artifact_id":10263148684,"ex5_wave_artifact_digest":"sha256:df48610fbf8d6cd11640f8f3feb534256b307e6ea803688267a33cb972cfba7f"},"target":{"row_id":"g1-d008","g":1,"d":8,"e":8,"survivor_offset_range":[1,255],"block_count":255,"terminal_count":28815,"block_indices":all_blocks,"block_index_stream_sha256":h.hexdigest(),"cut191_block0_disjoint":True,"n356_preserved_all_wave_blocks":True},"result":{"candidate_closed_block_indices":closed,"candidate_closed_block_count":len(closed),"candidate_closed_block_stream_sha256":ch.hexdigest(),"candidate_pruned_terminals":candidate,"candidate_post_cut_main_terminals":MAIN_TERMINALS-candidate,"remaining_nonclosed_block_count":residual,"method_counts":method_counts,"hnf_empty_block_count":zero_hnf,"whole_block_finite_ring_unsat_count":whole,"all_parent_finite_ring_unsat_block_count":parent_all},"credit":{"stage32_main_pruning_credit":False,"full178_complete":False,"theorem_credit":False,"endpoint_credit":False,"merge_authorized":False},"firewalls":{"hostile_audit_required":True,"main_authority_mutated":False,"cut191_double_counted":False,"n356_double_counted":False,"perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False}}
    body['canonical_sha256_without_this_field']=csha(body); args.output.write_text(json.dumps(body,sort_keys=True,indent=2)+'\n')
    print(json.dumps({"status":body['status'],"closed_blocks":len(closed),"candidate_pruned_terminals":candidate,"remaining_nonclosed_blocks":residual,"methods":method_counts,"canonical":body['canonical_sha256_without_this_field']},sort_keys=True))
if __name__=='__main__':main()
