#!/usr/bin/env python3
"""Fetch original Gen15 Actions ZIPs once and retain their exact proof bytes."""
from __future__ import annotations
import argparse,base64,gzip,hashlib,json,os,subprocess,zipfile
from pathlib import Path
import run_mb104_000707_fibration_shell_local_exact as engine

def main():
 p=argparse.ArgumentParser(); p.add_argument('--manifest',type=Path,required=True); p.add_argument('--bundle',type=Path,required=True); a=p.parse_args()
 repo=os.environ.get('GITHUB_REPOSITORY'); assert repo and os.environ.get('GH_TOKEN')
 m=json.loads(a.manifest.read_text()); g=m['generation15_singleton_carry']; rows=g['artifact_provenance']; assert len(rows)==29
 certs=[]
 for rec in rows:
  value=int(rec['value']); z=a.bundle.parent/f'.gen15-{value}.zip'
  with z.open('wb') as f: subprocess.run(['gh','api','--method','GET',f'repos/{repo}/actions/artifacts/{int(rec["artifact_id"])}'+'/zip'],check=True,stdout=f)
  assert 'sha256:'+hashlib.sha256(z.read_bytes()).hexdigest()==rec['zip_digest']
  with zipfile.ZipFile(z) as q:
   names=q.namelist(); assert len(names)==1 and names[0].endswith('.json')
   raw=q.read(names[0])
  z.unlink(); cert=json.loads(raw); body=dict(cert); claimed=body.pop('canonical_sha256_without_this_field')
  assert engine.csha(body)==claimed
  rec['certificate_file_sha256']=hashlib.sha256(raw).hexdigest(); rec['canonical']=claimed
  certs.append({'value':value,'certificate_file_sha256':rec['certificate_file_sha256'],'canonical':claimed,'base64':base64.b64encode(raw).decode('ascii')})
 payload={'schema':'STAGE32_MB104_000707_GEN15_COMPLETE_SINGLETON_CARRY_BUNDLE_V1','producing_workflow_run_id':g['producing_workflow_run_id'],'producing_execution_head':g['producing_execution_head'],'certificates':sorted(certs,key=lambda x:x['value'])}
 raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode(); packed=gzip.compress(raw,mtime=0)
 e={'schema':'STAGE32_MB104_000707_GEN15_DURABLE_CARRY_ENVELOPE_V1','encoding':'gzip+base64','gzip_sha256':hashlib.sha256(packed).hexdigest(),'payload_sha256':hashlib.sha256(raw).hexdigest(),'base64':base64.b64encode(packed).decode('ascii'),'exact_bytes_not_regenerated':True}
 a.bundle.write_text(json.dumps(e,sort_keys=True,indent=2)+'\n'); g['durable_bundle']={'path':str(a.bundle),'schema':e['schema'],'exact_bytes_not_regenerated':True,'materialized_from_original_actions_artifacts':True}; a.manifest.write_text(json.dumps(m,sort_keys=True,indent=2)+'\n')
if __name__=='__main__': main()
