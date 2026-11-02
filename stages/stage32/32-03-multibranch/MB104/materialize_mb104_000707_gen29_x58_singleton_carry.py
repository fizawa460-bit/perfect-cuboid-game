#!/usr/bin/env python3
from __future__ import annotations
import argparse,base64,gzip,hashlib,json,os,subprocess,tempfile,zipfile
from pathlib import Path

PACKET_SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_SINGLETON_PACKET_V1'
AGG_SCHEMA='STAGE32_MB104_000707_FIBRATION_SHELL0_ADAPTIVE_X58_SINGLETON_AGGREGATE_V1'
HEAD='090cf1ce97819736f9be09a9a96fb6421349acad'
RUN_ID=36092356653
AGG_CANON='480052e0ae4b174ce60a751599ad7393847c428e0948ec9b090668d5286e8af0'

def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def gh(path): return json.loads(subprocess.check_output(['gh','api','--method','GET',path],text=True))
def fetch_zip(repo,aid,path):
 with path.open('wb') as f: subprocess.run(['gh','api','--method','GET',f'repos/{repo}/actions/artifacts/{int(aid)}/zip'],check=True,stdout=f)
def one_json(path):
 with zipfile.ZipFile(path) as z:
  names=z.namelist(); assert len(names)==1 and names[0].endswith('.json'),names
  return names[0],z.read(names[0])
def key(r): return (int(r['primary_value']),int(r['secondary_residue']),int(r['fixed_x61_value']),int(r['x60_residue']),int(r['fixed_x60_value']),int(r['fixed_x58_value']))

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--out-dir',type=Path,required=True); a=ap.parse_args()
 repo=os.environ.get('GITHUB_REPOSITORY'); assert repo and os.environ.get('GH_TOKEN')
 out=a.out_dir; out.mkdir(parents=True,exist_ok=True)
 run=gh(f'repos/{repo}/actions/runs/{RUN_ID}')
 assert run['head_sha']==HEAD and run['status']=='completed' and run['conclusion']=='success'
 arts=gh(f'repos/{repo}/actions/runs/{RUN_ID}/artifacts?per_page=100')
 assert int(arts['total_count'])==55
 packets=sorted([x for x in arts['artifacts'] if x['name'].startswith('stage32-mb-fib-x58-singleton-')],key=lambda x:x['name'])
 aggs=[x for x in arts['artifacts'] if x['name']=='stage32-mb-fib-shell0-x58-singleton-aggregate']
 assert len(packets)==54 and len(aggs)==1 and all(not x['expired'] for x in packets+aggs)
 assert all(x['workflow_run']['head_sha']==HEAD for x in packets+aggs)
 complete=[]; incomplete=[]; certs=[]; source_locks=None; canon={}; seen=set()
 with tempfile.TemporaryDirectory() as td0:
  td=Path(td0)
  for art in packets:
   digest=art.get('digest'); assert isinstance(digest,str) and digest.startswith('sha256:')
   zp=td/f"{int(art['id'])}.zip"; fetch_zip(repo,art['id'],zp)
   assert hashlib.sha256(zp.read_bytes()).hexdigest()==digest.split(':',1)[1]
   fname,raw=one_json(zp); d=json.loads(raw)
   assert d['schema']==PACKET_SCHEMA and d['provenance']['producing_generation']==29 and d['provenance']['producing_mode']=='RECOVERY'
   assert all(v is False for v in d['credit_firewall'].values())
   if source_locks is None: source_locks=d['semantic_source_locks']
   else: assert d['semantic_source_locks']==source_locks
   body=dict(d); claimed=body.pop('canonical_sha256_without_this_field'); assert csha(body)==claimed
   p=d['partition']; parent={k:int(p[k]) for k in ('primary_value','secondary_residue','fixed_x61_value','x60_residue','fixed_x60_value')}
   interval=[int(x) for x in p['parent_x58_interval']]; pk=tuple(parent.values())+tuple(interval)
   assert pk not in seen; seen.add(pk); canon[':'.join(map(str,pk))]=claimed
   cc=0
   for ch in d['children']:
    cb=dict(ch); chash=cb.pop('canonical_sha256_without_this_field'); assert csha(cb)==chash
    row={**parent,'fixed_x58_value':int(ch['x58_value']),'canonical_sha256':chash}
    assert ch['result']['integral_known140_nonnegative_solution_count']==0
    assert ch['result']['primitive_known140_nonnegative_candidate_count']==0 and ch['result']['primitive_known140_nonnegative_candidates']==[]
    if ch['result']['complete']:
     assert ch['status']=='COMPLETE_EXACT_X58_SINGLETON_ZERO_CREDIT' and ch['solver']['final_solver_result']=='unsat' and ch['solver']['reason'] is None
     complete.append(row); cc+=1
    else:
     assert ch['status']=='PARTIAL_UNKNOWN_NO_CREDIT' and ch['solver']['final_solver_result']=='unknown' and ch['solver']['reason']=='timeout'
     row.update({'solver_result':'unknown','reason':'timeout'}); incomplete.append(row)
   assert cc==int(d['result']['complete_child_count']) and d['result']['complete'] is (cc==len(d['children']))
   certs.append({'artifact_id':int(art['id']),'artifact_name':art['name'],'artifact_zip_digest_sha256':digest.split(':',1)[1],'certificate_filename':fname,'certificate_file_sha256':hashlib.sha256(raw).hexdigest(),'canonical_sha256':claimed,'base64':base64.b64encode(raw).decode('ascii')})
  ar=aggs[0]; digest=ar.get('digest'); assert isinstance(digest,str) and digest.startswith('sha256:')
  az=td/'aggregate.zip'; fetch_zip(repo,ar['id'],az); assert hashlib.sha256(az.read_bytes()).hexdigest()==digest.split(':',1)[1]
  afname,araw=one_json(az); ag=json.loads(araw); assert ag['schema']==AGG_SCHEMA
  ab=dict(ag); ac=ab.pop('canonical_sha256_without_this_field'); assert csha(ab)==ac==AGG_CANON
  assert ag['complete'] is False and ag['status']=='PARTIAL_X58_SINGLETON_RECOVERY_NO_CREDIT'
  cov=ag['coverage']; assert cov['observed_packet_count']==54 and cov['missing_packets']==[] and len(cov['incomplete_packets'])==49
  assert cov['expected_x58_singleton_child_count']==160 and cov['gen27_complete_x58_interval_count']==74
  assert cov['prior_complete_x60_singletons']==281 and cov['necessary_condition_empty_leaf_count']==14
  assert ag['packet_input_canonical_sha256']==canon and ag['result']['primitive_candidates']==[] and ag['result']['primitive_candidate_count'] is None
  assert all(v is False for v in ag['credit_firewall'].values())
  aggregate={'artifact_id':int(ar['id']),'artifact_name':ar['name'],'artifact_zip_digest_sha256':digest.split(':',1)[1],'certificate_filename':afname,'certificate_file_sha256':hashlib.sha256(araw).hexdigest(),'canonical_sha256':ac,'base64':base64.b64encode(araw).decode('ascii')}
 complete.sort(key=key); incomplete.sort(key=key); certs.sort(key=lambda r:r['artifact_name'])
 assert len(seen)==54 and len(complete)==111 and len(incomplete)==49 and len(complete)+len(incomplete)==160
 fire=ag['credit_firewall']
 source={'schema':'STAGE32_MB104_000707_GEN29_X58_SINGLETON_CARRY_SOURCE_V1','producing_generation':29,'producing_mode':'RECOVERY','producing_execution_head':HEAD,'producing_workflow_run_id':RUN_ID,'packet_count':54,'x58_singleton_child_count':160,'expected_complete_child_count':111,'expected_incomplete_child_count':49,'prior_carried_complete_x60_singleton_count':281,'prior_necessary_condition_empty_leaf_count':14,'prior_carried_complete_x58_interval_count':74,'aggregate_artifact_id':aggregate['artifact_id'],'aggregate_artifact_zip_digest_sha256':aggregate['artifact_zip_digest_sha256'],'aggregate_canonical_sha256':aggregate['canonical_sha256'],'packet_artifacts':[{k:r[k] for k in ('artifact_id','artifact_name','artifact_zip_digest_sha256','certificate_filename','certificate_file_sha256','canonical_sha256')} for r in certs],'credit_firewall':fire,'exact_bytes_not_regenerated':True}
 payload={'schema':'STAGE32_MB104_000707_GEN29_X58_SINGLETON_DURABLE_CARRY_PAYLOAD_V1','producing_generation':29,'producing_mode':'RECOVERY','producing_execution_head':HEAD,'producing_workflow_run_id':RUN_ID,'source_locks':source_locks,'packet_count':54,'x58_singleton_child_count':160,'complete_child_count':111,'incomplete_child_count':49,'prior_carried_complete_x60_singleton_count':281,'prior_necessary_condition_empty_leaf_count':14,'prior_carried_complete_x58_interval_count':74,'complete_children':complete,'incomplete_children':incomplete,'certificates':certs,'aggregate_certificate':aggregate,'credit_firewall':fire}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode(); packed=gzip.compress(raw,mtime=0); b64=base64.b64encode(packed).decode('ascii'); chunks=[b64[i:i+24000] for i in range(0,len(b64),24000)]
 for old in out.glob('MB104-000707-GEN29-X58-SINGLETON-CARRY-BUNDLE-PART-*.b64'): old.unlink()
 chunk_rows=[]
 for i,s in enumerate(chunks):
  fn=f'MB104-000707-GEN29-X58-SINGLETON-CARRY-BUNDLE-PART-{i:02d}.b64'; (out/fn).write_text(s+'\n'); chunk_rows.append({'order':i,'filename':fn,'char_count':len(s),'sha256':hashlib.sha256(s.encode()).hexdigest()})
 index={'schema':'STAGE32_MB104_000707_GEN29_X58_SINGLETON_DURABLE_CARRY_CHUNK_INDEX_V1','encoding':'gzip+base64-chunks','exact_bytes_not_regenerated':True,'producing_generation':29,'producing_mode':'RECOVERY','producing_execution_head':HEAD,'producing_workflow_run_id':RUN_ID,'packet_count':54,'x58_singleton_child_count':160,'complete_child_count':111,'incomplete_child_count':49,'prior_carried_complete_x60_singleton_count':281,'prior_necessary_condition_empty_leaf_count':14,'prior_carried_complete_x58_interval_count':74,'aggregate_canonical_sha256':aggregate['canonical_sha256'],'byte_length':len(raw),'compressed_byte_length':len(packed),'payload_sha256':hashlib.sha256(raw).hexdigest(),'gzip_sha256':hashlib.sha256(packed).hexdigest(),'chunks':chunk_rows,'credit_firewall':fire}
 residual={'schema':'STAGE32_MB104_000707_GEN30_X58_SINGLETON_RESIDUAL49_V1','source_generation':29,'source_execution_head':HEAD,'source_workflow_run_id':RUN_ID,'complete_singleton_child_count':111,'residual_timeout_singleton_count':49,'prior_carried_complete_x60_singleton_count':281,'prior_necessary_condition_empty_leaf_count':14,'prior_carried_complete_x58_interval_count':74,'residual_singletons':incomplete,'credit':False}
 (out/'MB104-000707-GEN29-X58-SINGLETON-CARRY-SOURCE.json').write_text(json.dumps(source,indent=2,sort_keys=True)+'\n')
 (out/'MB104-000707-GEN29-X58-SINGLETON-CARRY-INDEX.json').write_text(json.dumps(index,indent=2,sort_keys=True)+'\n')
 (out/'MB104-000707-GEN30-X58-SINGLETON-RESIDUAL49.json').write_text(json.dumps(residual,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'success':True,'packets':54,'x58_singletons':160,'complete_children':111,'residual_timeout_children':49,'payload_sha256':index['payload_sha256'],'gzip_sha256':index['gzip_sha256'],'chunks':len(chunks)},sort_keys=True))
if __name__=='__main__': main()
