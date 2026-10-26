#!/usr/bin/env python3
"""Materialize exact Gen15 certificates only from the source-committed bundle."""
from __future__ import annotations
import argparse,base64,gzip,hashlib,json
from pathlib import Path

def main():
 p=argparse.ArgumentParser(); p.add_argument('--manifest',type=Path,required=True); p.add_argument('--bundle',type=Path,required=True); p.add_argument('--out-dir',type=Path,required=True); a=p.parse_args()
 m=json.loads(a.manifest.read_text()); g=m['generation15_singleton_carry']; e=json.loads(a.bundle.read_text())
 assert e['schema']=='STAGE32_MB104_000707_GEN15_DURABLE_CARRY_ENVELOPE_V1' and e['encoding']=='gzip+base64'
 packed=base64.b64decode(e['base64'],validate=True); assert hashlib.sha256(packed).hexdigest()==e['gzip_sha256']
 raw=gzip.decompress(packed); assert hashlib.sha256(raw).hexdigest()==e['payload_sha256']
 b=json.loads(raw); assert b['schema']=='STAGE32_MB104_000707_GEN15_COMPLETE_SINGLETON_CARRY_BUNDLE_V1'
 rows={int(x['value']):x for x in g['artifact_provenance']}; certs={int(x['value']):x for x in b['certificates']}
 expected=[int(x) for x in g['complete_values']]; assert sorted(rows)==expected==sorted(certs) and len(expected)==29
 a.out_dir.mkdir(parents=True,exist_ok=True)
 for value in expected:
  rec,entry=rows[value],certs[value]; data=base64.b64decode(entry['base64'],validate=True)
  assert hashlib.sha256(data).hexdigest()==entry['certificate_file_sha256']==rec['certificate_file_sha256']
  assert entry['canonical']==rec['canonical']
  (a.out_dir/f'{value}.json').write_bytes(data)
 print(json.dumps({'success':True,'rehydrated_values':expected,'count':len(expected)},sort_keys=True))
if __name__=='__main__': main()
