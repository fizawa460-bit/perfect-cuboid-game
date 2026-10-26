#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,gzip,hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
INDEX=HERE/'MB104-000707-GEN27-ADAPTIVE-X58-CARRY-INDEX.json'
SOURCE=HERE/'MB104-000707-GEN27-ADAPTIVE-X58-CARRY-SOURCE.json'
RESIDUAL=HERE/'MB104-000707-GEN28-ADAPTIVE-X58-RESIDUAL54.json'
PACKET_SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_PACKET_V1'
AGG_SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_AGGREGATE_V1'
PAYLOAD_SCHEMA='STAGE32_MB104_000707_GEN27_ADAPTIVE_X58_DURABLE_CARRY_PAYLOAD_V1'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def key(r): return (int(r['primary_value']),int(r['secondary_residue']),int(r['fixed_x61_value']),int(r['x60_residue']),int(r['fixed_x60_value']),int(r['x58_interval'][0]),int(r['x58_interval'][1]))
def identity(r): return {k:r[k] for k in ('primary_value','secondary_residue','fixed_x61_value','x60_residue','fixed_x60_value','x58_interval')}

def decode_carry(index_path=INDEX,source_path=SOURCE,residual_path=RESIDUAL,out_dir=None):
 idx=json.loads(Path(index_path).read_text()); src=json.loads(Path(source_path).read_text()); res=json.loads(Path(residual_path).read_text())
 assert idx['schema']=='STAGE32_MB104_000707_GEN27_ADAPTIVE_X58_DURABLE_CARRY_CHUNK_INDEX_V1'
 assert idx['encoding']=='gzip+base64-chunks' and idx['exact_bytes_not_regenerated'] is True
 assert idx['producing_generation']==27 and idx['producing_mode']=='RECOVERY'
 assert idx['producing_execution_head']=='1f69a43a49d05b3e8c5fa87c812efe974c9b20e5' and idx['producing_workflow_run_id']==36066791252
 assert idx['packet_count']==16 and idx['adaptive_interval_child_count']==128 and idx['complete_child_count']==74 and idx['incomplete_child_count']==54
 assert idx['prior_carried_complete_x60_singleton_count']==281 and idx['prior_necessary_condition_empty_leaf_count']==14
 assert all(v is False for v in idx['credit_firewall'].values())
 parts=[]
 for i,row in enumerate(idx['chunks']):
  assert int(row['order'])==i
  s=(HERE/row['filename']).read_text().strip(); assert len(s)==int(row['char_count']) and hashlib.sha256(s.encode()).hexdigest()==row['sha256']; parts.append(s)
 packed=base64.b64decode(''.join(parts),validate=True); assert len(packed)==int(idx['compressed_byte_length']) and hashlib.sha256(packed).hexdigest()==idx['gzip_sha256']
 raw=gzip.decompress(packed); assert len(raw)==int(idx['byte_length']) and hashlib.sha256(raw).hexdigest()==idx['payload_sha256']; p=json.loads(raw)
 assert p['schema']==PAYLOAD_SCHEMA and p['producing_generation']==27 and p['producing_mode']=='RECOVERY'
 assert p['producing_execution_head']==idx['producing_execution_head'] and p['producing_workflow_run_id']==idx['producing_workflow_run_id']
 assert p['packet_count']==16 and p['adaptive_interval_child_count']==128 and p['complete_child_count']==74 and p['incomplete_child_count']==54
 assert p['prior_carried_complete_x60_singleton_count']==281 and p['prior_necessary_condition_empty_leaf_count']==14
 assert all(v is False for v in p['credit_firewall'].values())
 complete=[]; incomplete=[]; canon={}; seen=set(); prov=[]; locks=None
 for rec in p['certificates']:
  rawc=base64.b64decode(rec['base64'],validate=True); assert hashlib.sha256(rawc).hexdigest()==rec['certificate_file_sha256']; d=json.loads(rawc)
  assert d['schema']==PACKET_SCHEMA and d['provenance']['producing_generation']==27 and d['provenance']['producing_mode']=='RECOVERY' and isinstance(d['provenance'].get('gen25_cold_canonical_sha256'),str)
  assert all(v is False for v in d['credit_firewall'].values())
  if locks is None: locks=d['semantic_source_locks']; assert locks==p['source_locks']
  else: assert d['semantic_source_locks']==locks
  cl=d['canonical_sha256_without_this_field']; b=dict(d); b.pop('canonical_sha256_without_this_field'); assert csha(b)==cl==rec['canonical_sha256']
  part=d['partition']; parent={k:int(part[k]) for k in ('primary_value','secondary_residue','fixed_x61_value','x60_residue','fixed_x60_value')}; pk=tuple(parent.values()); assert pk not in seen; seen.add(pk)
  canon[':'.join(map(str,pk))]=cl; assert part['coverage_is_exact_disjoint'] is True and len(d['children'])==8
  cc=0
  for child in d['children']:
   cb=dict(child); ch=cb.pop('canonical_sha256_without_this_field'); assert csha(cb)==ch
   row={**parent,'x58_interval':[int(x) for x in child['x58_interval']],'canonical_sha256':ch}
   if child['result']['complete']:
    assert child['status']=='COMPLETE_EXACT_ADAPTIVE_X58_INTERVAL_ZERO_CREDIT' and child['solver']['final_solver_result']=='unsat' and child['solver']['reason'] is None
    assert child['result']['integral_known140_nonnegative_solution_count']==0 and child['result']['primitive_known140_nonnegative_candidate_count']==0 and child['result']['primitive_known140_nonnegative_candidates']==[]
    complete.append(row); cc+=1
   else:
    assert child['status']=='PARTIAL_UNKNOWN_NO_CREDIT' and child['solver']['final_solver_result']=='unknown' and child['solver']['reason']=='timeout'
    assert child['result']['integral_known140_nonnegative_solution_count']==0 and child['result']['primitive_known140_nonnegative_candidate_count']==0 and child['result']['primitive_known140_nonnegative_candidates']==[]
    row.update({'solver_result':'unknown','reason':'timeout'}); incomplete.append(row)
  assert cc==int(d['result']['complete_child_count']) and d['result']['complete'] is (cc==8)
  prov.append({k:rec[k] for k in ('artifact_id','artifact_name','artifact_zip_digest_sha256','certificate_filename','certificate_file_sha256','canonical_sha256')})
  if out_dir is not None:
   out=Path(out_dir); out.mkdir(parents=True,exist_ok=True); (out/rec['certificate_filename']).write_bytes(rawc)
 complete.sort(key=key); incomplete.sort(key=key); assert len(seen)==16 and len(complete)==74 and len(incomplete)==54
 assert complete==p['complete_children'] and incomplete==p['incomplete_children']
 ar=p['aggregate_certificate']; araw=base64.b64decode(ar['base64'],validate=True); assert hashlib.sha256(araw).hexdigest()==ar['certificate_file_sha256']; ag=json.loads(araw)
 assert ag['schema']==AGG_SCHEMA and ag['complete'] is False and ag['status']=='PARTIAL_ADAPTIVE_X58_RECOVERY_NO_CREDIT'
 ac=ag['canonical_sha256_without_this_field']; ab=dict(ag); ab.pop('canonical_sha256_without_this_field'); assert csha(ab)==ac==ar['canonical_sha256']==idx['aggregate_canonical_sha256']==src['aggregate_canonical_sha256']
 assert ag['coverage']['observed_packet_count']==16 and ag['coverage']['missing_packets']==[] and len(ag['coverage']['incomplete_packets'])==16
 assert ag['coverage']['carried_complete_x60_singleton_child_count']==281 and ag['coverage']['necessary_condition_empty_leaf_count']==14 and ag['coverage']['expected_adaptive_x58_interval_child_count']==128
 assert ag['packet_input_canonical_sha256']==canon and ag['result']['primitive_candidates']==[] and ag['result']['primitive_candidate_count'] is None
 assert src['schema']=='STAGE32_MB104_000707_GEN27_ADAPTIVE_X58_CARRY_SOURCE_V1' and src['producing_execution_head']==idx['producing_execution_head'] and src['producing_workflow_run_id']==idx['producing_workflow_run_id']
 assert src['packet_count']==16 and src['adaptive_interval_child_count']==128 and src['expected_complete_child_count']==74 and src['expected_incomplete_child_count']==54
 assert src['prior_carried_complete_x60_singleton_count']==281 and src['prior_necessary_condition_empty_leaf_count']==14 and src['exact_bytes_not_regenerated'] is True and all(v is False for v in src['credit_firewall'].values())
 assert sorted(src['packet_artifacts'],key=lambda r:r['artifact_name'])==sorted(prov,key=lambda r:r['artifact_name'])
 assert src['aggregate_artifact_id']==ar['artifact_id'] and src['aggregate_artifact_zip_digest_sha256']==ar['artifact_zip_digest_sha256']
 assert res['schema']=='STAGE32_MB104_000707_GEN28_ADAPTIVE_X58_RESIDUAL54_V1' and res['source_generation']==27 and res['source_execution_head']==idx['producing_execution_head'] and res['source_workflow_run_id']==idx['producing_workflow_run_id']
 assert res['complete_child_count']==74 and res['residual_timeout_child_count']==54 and res['residual_children']==incomplete and res['credit'] is False
 if out_dir is not None: (Path(out_dir)/ar['certificate_filename']).write_bytes(araw)
 return idx,p

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--index',type=Path,default=INDEX); ap.add_argument('--source',type=Path,default=SOURCE); ap.add_argument('--residual',type=Path,default=RESIDUAL); ap.add_argument('--out-dir',type=Path); a=ap.parse_args(); idx,p=decode_carry(a.index,a.source,a.residual,a.out_dir); print(json.dumps({'success':True,'packets':16,'adaptive_children':128,'complete_children':74,'residual_timeout_children':54,'payload_sha256':idx['payload_sha256']},sort_keys=True))
if __name__=='__main__': main()
