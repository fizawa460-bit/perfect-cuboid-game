#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as parent
import run_mb104_000707_fibration_shell0_adaptive_x58_packet as packet
import verify_mb104_000707_fibration_shell0_adaptive_x58_packet as pv
import aggregate_mb104_000707_fibration_shell0_adaptive_x58_packets as agg
import verify_mb104_000707_gen27_adaptive_x58_carry as carry

def union(input_dir):
 expected=set(packet.residual_rows()); obs={}; integral=0; prim=[]; sx=set(); sf=set()
 for path in sorted(Path(input_dir).glob('*.json')):
  raw=json.loads(path.read_text()); k=agg.pkey(raw); assert k in expected and k not in obs; d=pv.validate_certificate(path,*k); obs[k]=d; integral+=int(d['result']['integral_known140_nonnegative_solution_count'])
  for rec in d['result']['primitive_known140_nonnegative_candidates']:
   replay=parent.replay_solution(0,[int(v) for v in rec['x_hperp_coordinates']]); assert replay==rec and replay['primitive'] is True; xk=tuple(rec['x_hperp_coordinates']); fk=tuple(rec['picard_basis_coordinates']); assert xk not in sx and fk not in sf; sx.add(xk); sf.add(fk); prim.append(rec)
 prim.sort(key=lambda r:tuple(r['picard_basis_coordinates'])); missing=sorted([list(k) for k in expected-set(obs)]); incomplete=sorted([list(k) for k,d in obs.items() if not d['result']['complete']]); hashes={':'.join(map(str,k)):d['canonical_sha256_without_this_field'] for k,d in sorted(obs.items())}; return obs,integral,prim,missing,incomplete,hashes

def validate(path,input_dir,require_complete=False):
 d=json.loads(Path(path).read_text()); assert d['schema']==agg.SCHEMA; cl=d['canonical_sha256_without_this_field']; b=dict(d); b.pop('canonical_sha256_without_this_field'); assert parent.csha(b)==cl; assert d['provenance']['producing_execution_head']==subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(); assert d['provenance']['semantic_source_locks']==packet.semantic_source_locks(); idx,_=carry.decode_carry(); assert d['provenance']['gen27_carry_payload_sha256']==idx['payload_sha256'] and d['provenance']['gen27_carry_gzip_sha256']==idx['gzip_sha256'] and d['provenance']['gen27_producing_execution_head']==idx['producing_execution_head']
 c=d['coverage']; assert c['prior_complete_x60_singletons']==281 and c['necessary_condition_empty_leaf_count']==14 and c['gen27_complete_x58_interval_count']==74 and c['residual_timeout_x58_interval_count']==54 and c['expected_packet_count']==54 and c['expected_x58_singleton_child_count']==160 and c['refinement_coordinate_0based']==58 and c['refinement_is_exact_disjoint'] is True; obs,integral,prim,missing,incomplete,hashes=union(input_dir); assert c['observed_packet_count']==len(obs) and c['missing_packets']==missing and c['incomplete_packets']==incomplete and d['packet_input_canonical_sha256']==hashes; complete=not missing and not incomplete and len(obs)==54; assert d['complete'] is complete and all(v is False for v in d['credit_firewall'].values())
 if complete: assert d['status']=='COMPLETE_EXACT_SHELL0_ENUMERATION_ZERO_CREDIT' and d['result']['integral_known140_nonnegative_solution_count']==integral and d['result']['primitive_candidate_count']==len(prim) and d['result']['primitive_candidates']==prim
 else: assert d['status']=='PARTIAL_X58_SINGLETON_RECOVERY_NO_CREDIT' and d['result']['integral_known140_nonnegative_solution_count'] is None and d['result']['primitive_candidate_count'] is None and d['result']['primitive_candidates']==[]
 if require_complete: assert complete
 return d

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--certificate',type=Path,required=True); ap.add_argument('--input-dir',type=Path,required=True); ap.add_argument('--require-complete',action='store_true'); a=ap.parse_args(); d=validate(a.certificate,a.input_dir,a.require_complete); print(json.dumps({'success':True,'complete':d['complete'],'observed_packets':d['coverage']['observed_packet_count'],'primitive_candidates':d['result']['primitive_candidate_count'],'canonical':d['canonical_sha256_without_this_field']},sort_keys=True))
if __name__=='__main__': main()
