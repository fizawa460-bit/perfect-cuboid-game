#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,gzip,hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
INDEX=HERE/'MB104-000707-GEN29-X58-SINGLETON-CARRY-INDEX.json'
SOURCE=HERE/'MB104-000707-GEN29-X58-SINGLETON-CARRY-SOURCE.json'
RESIDUAL=HERE/'MB104-000707-GEN30-X58-SINGLETON-RESIDUAL49.json'
PACKET_SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_SINGLETON_PACKET_V1'
AGG_SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_SINGLETON_AGGREGATE_V1'
PAYLOAD_SCHEMA='STAGE32_MB104_000707_GEN29_X58_SINGLETON_DURABLE_CARRY_PAYLOAD_V1'
HEAD='090cf1ce97819736f9be09a9a96fb6421349acad'
RUN_ID=36092356653
AGG_CANON='480052e0ae4b174ce60a751599ad7393847c428e0948ec9b090668d5286e8af0'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def key(r): return (int(r['primary_value']),int(r['secondary_residue']),int(r['fixed_x61_value']),int(r['x60_residue']),int(r['fixed_x60_value']),int(r['fixed_x58_value']))

def decode_carry(index_path=INDEX,source_path=SOURCE,residual_path=RESIDUAL,out_dir=None):
 idx=json.loads(Path(index_path).read_text()); src=json.loads(Path(source_path).read_text()); res=json.loads(Path(residual_path).read_text())
 assert idx['schema']=='STAGE32_MB104_000707_GEN29_X58_SINGLETON_DURABLE_CARRY_CHUNK_INDEX_V1'
 assert idx['encoding']=='gzip+base64-chunks' and idx['exact_bytes_not_regenerated'] is True
 assert idx['producing_generation']==29 and idx['producing_mode']=='RECOVERY'
 assert idx['producing_execution_head']==HEAD and idx['producing_workflow_run_id']==RUN_ID
 assert idx['packet_count']==54 and idx['x58_singleton_child_count']==160 and idx['complete_child_count']==111 and idx['incomplete_child_count']==49
 assert idx['prior_carried_complete_x60_singleton_count']==281 and idx['prior_necessary_condition_empty_leaf_count']==14 and idx['prior_carried_complete_x58_interval_count']==74
 assert idx['aggregate_canonical_sha256']==AGG_CANON and all(v is False for v in idx['credit_firewall'].values())
 parts=[]
 for i,row in enumerate(idx['chunks']):
  assert int(row['order'])==i
  s=(HERE/row['filename']).read_text().strip()
  assert len(s)==int(row['char_count']) and hashlib.sha256(s.encode()).hexdigest()==row['sha256']
  parts.append(s)
 packed=base64.b64decode(''.join(parts),validate=True)
 assert len(packed)==int(idx['compressed_byte_length']) and hashlib.sha256(packed).hexdigest()==idx['gzip_sha256']
 raw=gzip.decompress(packed)
 assert len(raw)==int(idx['byte_length']) and hashlib.sha256(raw).hexdigest()==idx['payload_sha256']
 p=json.loads(raw)
 assert p['schema']==PAYLOAD_SCHEMA and p['producing_generation']==29 and p['producing_mode']=='RECOVERY'
 assert p['producing_execution_head']==HEAD and p['producing_workflow_run_id']==RUN_ID
 assert p['packet_count']==54 and p['x58_singleton_child_count']==160 and p['complete_child_count']==111 and p['incomplete_child_count']==49
 assert p['prior_carried_complete_x60_singleton_count']==281 and p['prior_necessary_condition_empty_leaf_count']==14 and p['prior_carried_complete_x58_interval_count']==74
 assert all(v is False for v in p['credit_firewall'].values())
 complete=[]; incomplete=[]; canon={}; seen=set(); provenance=[]; locks=None
 for rec in p['certificates']:
  rawc=base64.b64decode(rec['base64'],validate=True)
  assert hashlib.sha256(rawc).hexdigest()==rec['certificate_file_sha256']
  d=json.loads(rawc)
  assert d['schema']==PACKET_SCHEMA and d['provenance']['producing_generation']==29 and d['provenance']['producing_mode']=='RECOVERY'
  assert all(v is False for v in d['credit_firewall'].values())
  if locks is None:
   locks=d['semantic_source_locks']; assert locks==p['source_locks']
  else:
   assert d['semantic_source_locks']==locks
  body=dict(d); claimed=body.pop('canonical_sha256_without_this_field'); assert csha(body)==claimed==rec['canonical_sha256']
  part=d['partition']
  parent={k:int(part[k]) for k in ('primary_value','secondary_residue','fixed_x61_value','x60_residue','fixed_x60_value')}
  interval=[int(x) for x in part['parent_x58_interval']]
  pk=tuple(parent.values())+tuple(interval); assert pk not in seen; seen.add(pk)
  canon[':'.join(map(str,pk))]=claimed
  assert part['coverage_is_exact_disjoint'] is True
  assert list(map(int,part['x58_singleton_values']))==list(range(interval[0],interval[1]+1))
  cc=0
  for child in d['children']:
   cb=dict(child); chash=cb.pop('canonical_sha256_without_this_field'); assert csha(cb)==chash
   row={**parent,'fixed_x58_value':int(child['x58_value']),'canonical_sha256':chash}
   assert child['result']['integral_known140_nonnegative_solution_count']==0
   assert child['result']['primitive_known140_nonnegative_candidate_count']==0 and child['result']['primitive_known140_nonnegative_candidates']==[]
   if child['result']['complete']:
    assert child['status']=='COMPLETE_EXACT_X58_SINGLETON_ZERO_CREDIT'
    assert child['solver']['final_solver_result']=='unsat' and child['solver']['reason'] is None
    complete.append(row); cc+=1
   else:
    assert child['status']=='PARTIAL_UNKNOWN_NO_CREDIT'
    assert child['solver']['final_solver_result']=='unknown' and child['solver']['reason']=='timeout'
    row.update({'solver_result':'unknown','reason':'timeout'}); incomplete.append(row)
  assert cc==int(d['result']['complete_child_count']) and d['result']['complete'] is (cc==len(d['children']))
  provenance.append({k:rec[k] for k in ('artifact_id','artifact_name','artifact_zip_digest_sha256','certificate_filename','certificate_file_sha256','canonical_sha256')})
  if out_dir is not None:
   out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); (out/rec['certificate_filename']).write_bytes(rawc)
 complete.sort(key=key); incomplete.sort(key=key)
 assert len(seen)==54 and len(complete)==111 and len(incomplete)==49 and len(complete)+len(incomplete)==160
 assert complete==p['complete_children'] and incomplete==p['incomplete_children']
 ar=p['aggregate_certificate']; araw=base64.b64decode(ar['base64'],validate=True)
 assert hashlib.sha256(araw).hexdigest()==ar['certificate_file_sha256']
 ag=json.loads(araw); body=dict(ag); ac=body.pop('canonical_sha256_without_this_field')
 assert ag['schema']==AGG_SCHEMA and csha(body)==ac==ar['canonical_sha256']==idx['aggregate_canonical_sha256']==AGG_CANON
 assert ag['complete'] is False and ag['status']=='PARTIAL_X58_SINGLETON_RECOVERY_NO_CREDIT'
 cov=ag['coverage']
 assert cov['expected_packet_count']==54 and cov['observed_packet_count']==54 and cov['missing_packets']==[] and len(cov['incomplete_packets'])==49
 assert cov['expected_x58_singleton_child_count']==160 and cov['gen27_complete_x58_interval_count']==74
 assert cov['prior_complete_x60_singletons']==281 and cov['necessary_condition_empty_leaf_count']==14
 assert ag['packet_input_canonical_sha256']==canon
 assert ag['result']['primitive_candidates']==[] and ag['result']['primitive_candidate_count'] is None
 assert all(v is False for v in ag['credit_firewall'].values())
 assert src['schema']=='STAGE32_MB104_000707_GEN29_X58_SINGLETON_CARRY_SOURCE_V1'
 assert src['producing_execution_head']==HEAD and src['producing_workflow_run_id']==RUN_ID and src['exact_bytes_not_regenerated'] is True
 assert src['packet_count']==54 and src['x58_singleton_child_count']==160 and src['expected_complete_child_count']==111 and src['expected_incomplete_child_count']==49
 assert src['prior_carried_complete_x60_singleton_count']==281 and src['prior_necessary_condition_empty_leaf_count']==14 and src['prior_carried_complete_x58_interval_count']==74
 assert src['aggregate_artifact_id']==ar['artifact_id'] and src['aggregate_artifact_zip_digest_sha256']==ar['artifact_zip_digest_sha256'] and src['aggregate_canonical_sha256']==AGG_CANON
 assert sorted(src['packet_artifacts'],key=lambda r:r['artifact_name'])==sorted(provenance,key=lambda r:r['artifact_name'])
 assert all(v is False for v in src['credit_firewall'].values())
 assert res['schema']=='STAGE32_MB104_000707_GEN30_X58_SINGLETON_RESIDUAL49_V1'
 assert res['source_generation']==29 and res['source_execution_head']==HEAD and res['source_workflow_run_id']==RUN_ID
 assert res['complete_singleton_child_count']==111 and res['residual_timeout_singleton_count']==49
 assert res['prior_carried_complete_x60_singleton_count']==281 and res['prior_necessary_condition_empty_leaf_count']==14 and res['prior_carried_complete_x58_interval_count']==74
 assert res['residual_singletons']==incomplete and res['credit'] is False
 if out_dir is not None: (Path(out_dir)/ar['certificate_filename']).write_bytes(araw)
 return idx,p

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--index',type=Path,default=INDEX); ap.add_argument('--source',type=Path,default=SOURCE); ap.add_argument('--residual',type=Path,default=RESIDUAL); ap.add_argument('--out-dir',type=Path)
 a=ap.parse_args(); idx,_=decode_carry(a.index,a.source,a.residual,a.out_dir)
 print(json.dumps({'success':True,'packets':54,'x58_singletons':160,'complete_children':111,'residual_timeout_children':49,'payload_sha256':idx['payload_sha256']},sort_keys=True))

if __name__=='__main__': main()
