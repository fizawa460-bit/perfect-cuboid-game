#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,gzip,hashlib,json,os,subprocess,tempfile,zipfile
from pathlib import Path

PACKET_SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_PACKET_V1'
AGG_SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_AGGREGATE_V1'
HEAD='1f69a43a49d05b3e8c5fa87c812efe974c9b20e5'
RUN_ID=36066791252
AGG_CANON='8990b5ddf23ec10a9f39502e3ee6ffb3edef8d517bfab7a3048aca30ae36cd93'


def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def gh(path): return json.loads(subprocess.check_output(['gh','api','--method','GET',path],text=True))
def fetch_zip(repo,aid,path):
 with path.open('wb') as f: subprocess.run(['gh','api','--method','GET',f'repos/{repo}/actions/artifacts/{int(aid)}/zip'],check=True,stdout=f)
def one_json(path):
 with zipfile.ZipFile(path) as z:
  names=z.namelist(); assert len(names)==1 and names[0].endswith('.json'),names
  return names[0],z.read(names[0])
def child_key(r): return (int(r['primary_value']),int(r['secondary_residue']),int(r['fixed_x61_value']),int(r['x60_residue']),int(r['fixed_x60_value']),int(r['x58_interval'][0]),int(r['x58_interval'][1]))


def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',type=Path,required=True); a=ap.parse_args()
 repo=os.environ.get('GITHUB_REPOSITORY'); assert repo and os.environ.get('GH_TOKEN')
 out=a.out_dir; out.mkdir(parents=True,exist_ok=True)
 run=gh(f'repos/{repo}/actions/runs/{RUN_ID}')
 assert run['head_sha']==HEAD and run['status']=='completed' and run['conclusion']=='success'
 arts=gh(f'repos/{repo}/actions/runs/{RUN_ID}/artifacts?per_page=100')
 assert int(arts['total_count'])==17
 packets=sorted([x for x in arts['artifacts'] if x['name'].startswith('stage32-mb-fib-adaptive-x58-')],key=lambda x:x['name'])
 aggs=[x for x in arts['artifacts'] if x['name']=='stage32-mb-fib-shell0-adaptive-x58-aggregate']
 assert len(packets)==16 and len(aggs)==1 and all(not x['expired'] for x in packets+aggs)
 assert all(x['workflow_run']['head_sha']==HEAD for x in packets+aggs)
 complete=[]; incomplete=[]; certs=[]; source_locks=None; canon={}; seen=set()
 with tempfile.TemporaryDirectory() as td0:
  td=Path(td0)
  for art in packets:
   digest=art.get('digest'); assert isinstance(digest,str) and digest.startswith('sha256:')
   zp=td/f"{int(art['id'])}.zip"; fetch_zip(repo,art['id'],zp)
   assert hashlib.sha256(zp.read_bytes()).hexdigest()==digest.split(':',1)[1]
   fname,raw=one_json(zp); d=json.loads(raw)
   assert d['schema']==PACKET_SCHEMA
   assert d['provenance']['producing_generation']==27 and d['provenance']['producing_mode']=='RECOVERY'
   assert isinstance(d['provenance'].get('gen25_cold_canonical_sha256'),str)
   assert all(v is False for v in d['credit_firewall'].values())
   if source_locks is None: source_locks=d['semantic_source_locks']
   else: assert d['semantic_source_locks']==source_locks
   claimed=d['canonical_sha256_without_this_field']; body=dict(d); body.pop('canonical_sha256_without_this_field'); assert csha(body)==claimed
   p=d['partition']; parent={k:int(p[k]) for k in ('primary_value','secondary_residue','fixed_x61_value','x60_residue','fixed_x60_value')}; pk=tuple(parent.values())
   assert pk not in seen; seen.add(pk); canon[':'.join(map(str,pk))]=claimed
   assert p['coverage_is_exact_disjoint'] is True and len(d['children'])==8 and int(d['result']['child_count'])==8
   cc=0
   for ch in d['children']:
    cb=dict(ch); chash=cb.pop('canonical_sha256_without_this_field'); assert csha(cb)==chash
    row={**parent,'x58_interval':[int(x) for x in ch['x58_interval']],'canonical_sha256':chash}
    assert ch['result']['integral_known140_nonnegative_solution_count']==0
    assert ch['result']['primitive_known140_nonnegative_candidate_count']==0 and ch['result']['primitive_known140_nonnegative_candidates']==[]
    if ch['result']['complete']:
     assert ch['status']=='COMPLETE_EXACT_ADAPTIVE_X58_INTERVAL_ZERO_CREDIT' and ch['solver']['final_solver_result']=='unsat' and ch['solver']['reason'] is None
     complete.append(row); cc+=1
    else:
     assert ch['status']=='PARTIAL_UNKNOWN_NO_CREDIT' and ch['solver']['final_solver_result']=='unknown' and ch['solver']['reason']=='timeout'
     row.update({'solver_result':'unknown','reason':'timeout'}); incomplete.append(row)
   assert cc==int(d['result']['complete_child_count']) and d['result']['complete'] is (cc==8)
   certs.append({'artifact_id':int(art['id']),'artifact_name':art['name'],'artifact_zip_digest_sha256':digest.split(':',1)[1],'certificate_filename':fname,'certificate_file_sha256':hashlib.sha256(raw).hexdigest(),'canonical_sha256':claimed,'base64':base64.b64encode(raw).decode('ascii')})
  ar=aggs[0]; digest=ar.get('digest'); assert isinstance(digest,str) and digest.startswith('sha256:')
  az=td/'aggregate.zip'; fetch_zip(repo,ar['id'],az); assert hashlib.sha256(az.read_bytes()).hexdigest()==digest.split(':',1)[1]
  afname,araw=one_json(az); ag=json.loads(araw); assert ag['schema']==AGG_SCHEMA
  ac=ag['canonical_sha256_without_this_field']; ab=dict(ag); ab.pop('canonical_sha256_without_this_field'); assert csha(ab)==ac==AGG_CANON
  assert ag['complete'] is False and ag['status']=='PARTIAL_ADAPTIVE_X58_RECOVERY_NO_CREDIT'
  assert ag['coverage']['observed_packet_count']==16 and ag['coverage']['missing_packets']==[] and len(ag['coverage']['incomplete_packets'])==16
  assert ag['coverage']['carried_complete_x60_singleton_child_count']==281 and ag['coverage']['necessary_condition_empty_leaf_count']==14 and ag['coverage']['expected_adaptive_x58_interval_child_count']==128
  assert ag['packet_input_canonical_sha256']==canon and ag['result']['primitive_candidates']==[] and ag['result']['primitive_candidate_count'] is None
  assert all(v is False for v in ag['credit_firewall'].values())
  aggregate={'artifact_id':int(ar['id']),'artifact_name':ar['name'],'artifact_zip_digest_sha256':digest.split(':',1)[1],'certificate_filename':afname,'certificate_file_sha256':hashlib.sha256(araw).hexdigest(),'canonical_sha256':ac,'base64':base64.b64encode(araw).decode('ascii')}
 complete.sort(key=child_key); incomplete.sort(key=child_key); certs.sort(key=lambda r:r['artifact_name'])
 assert len(seen)==16 and len(complete)==74 and len(incomplete)==54 and len(complete)+len(incomplete)==128
 fire=ag['credit_firewall']
 source={'schema':'STAGE32_MB104_000707_GEN27_ADAPTIVE_X58_CARRY_SOURCE_V1','producing_generation':27,'producing_mode':'RECOVERY','producing_execution_head':HEAD,'producing_workflow_run_id':RUN_ID,'packet_count':16,'adaptive_interval_child_count':128,'expected_complete_child_count':74,'expected_incomplete_child_count':54,'prior_carried_complete_x60_singleton_count':281,'prior_necessary_condition_empty_leaf_count':14,'aggregate_artifact_id':aggregate['artifact_id'],'aggregate_artifact_zip_digest_sha256':aggregate['artifact_zip_digest_sha256'],'aggregate_canonical_sha256':aggregate['canonical_sha256'],'packet_artifacts':[{k:r[k] for k in ('artifact_id','artifact_name','artifact_zip_digest_sha256','certificate_filename','certificate_file_sha256','canonical_sha256')} for r in certs],'credit_firewall':fire,'exact_bytes_not_regenerated':True}
 payload={'schema':'STAGE32_MB104_000707_GEN27_ADAPTIVE_X58_DURABLE_CARRY_PAYLOAD_V1','producing_generation':27,'producing_mode':'RECOVERY','producing_execution_head':HEAD,'producing_workflow_run_id':RUN_ID,'source_locks':source_locks,'packet_count':16,'adaptive_interval_child_count':128,'complete_child_count':74,'incomplete_child_count':54,'prior_carried_complete_x60_singleton_count':281,'prior_necessary_condition_empty_leaf_count':14,'complete_children':complete,'incomplete_children':incomplete,'certificates':certs,'aggregate_certificate':aggregate,'credit_firewall':fire}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode(); packed=gzip.compress(raw,mtime=0); b64=base64.b64encode(packed).decode('ascii'); chunks=[b64[i:i+24000] for i in range(0,len(b64),24000)]
 for old in out.glob('MB104-000707-GEN27-ADAPTIVE-X58-CARRY-BUNDLE-PART-*.b64'): old.unlink()
 chunk_rows=[]
 for i,s in enumerate(chunks):
  fn=f'MB104-000707-GEN27-ADAPTIVE-X58-CARRY-BUNDLE-PART-{i:02d}.b64'; (out/fn).write_text(s+'\n'); chunk_rows.append({'order':i,'filename':fn,'char_count':len(s),'sha256':hashlib.sha256(s.encode()).hexdigest()})
 index={'schema':'STAGE32_MB104_000707_GEN27_ADAPTIVE_X58_DURABLE_CARRY_CHUNK_INDEX_V1','encoding':'gzip+base64-chunks','exact_bytes_not_regenerated':True,'producing_generation':27,'producing_mode':'RECOVERY','producing_execution_head':HEAD,'producing_workflow_run_id':RUN_ID,'packet_count':16,'adaptive_interval_child_count':128,'complete_child_count':74,'incomplete_child_count':54,'prior_carried_complete_x60_singleton_count':281,'prior_necessary_condition_empty_leaf_count':14,'aggregate_canonical_sha256':aggregate['canonical_sha256'],'byte_length':len(raw),'compressed_byte_length':len(packed),'payload_sha256':hashlib.sha256(raw).hexdigest(),'gzip_sha256':hashlib.sha256(packed).hexdigest(),'chunks':chunk_rows,'credit_firewall':fire}
 residual={'schema':'STAGE32_MB104_000707_GEN28_ADAPTIVE_X58_RESIDUAL54_V1','source_generation':27,'source_execution_head':HEAD,'source_workflow_run_id':RUN_ID,'complete_child_count':74,'residual_timeout_child_count':54,'residual_children':incomplete,'credit':False}
 (out/'MB104-000707-GEN27-ADAPTIVE-X58-CARRY-SOURCE.json').write_text(json.dumps(source,indent=2,sort_keys=True)+'\n')
 (out/'MB104-000707-GEN27-ADAPTIVE-X58-CARRY-INDEX.json').write_text(json.dumps(index,indent=2,sort_keys=True)+'\n')
 (out/'MB104-000707-GEN28-ADAPTIVE-X58-RESIDUAL54.json').write_text(json.dumps(residual,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'success':True,'packets':16,'adaptive_children':128,'complete_children':74,'residual_timeout_children':54,'payload_sha256':index['payload_sha256'],'gzip_sha256':index['gzip_sha256'],'chunks':len(chunks)},sort_keys=True))

if __name__=='__main__': main()
