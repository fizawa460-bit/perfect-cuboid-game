from pathlib import Path
import hashlib,json
p=Path(__file__).resolve().parent
d=json.loads((p/'MANIFEST_SHA256.json').read_text())
for name,r in d['files'].items():
 f=(p/name).resolve()
 if p.resolve()not in f.parents:raise RuntimeError('invalid manifest path')
 data=f.read_bytes()
 if len(data)!=r['bytes']or hashlib.sha256(data).hexdigest()!=r['sha256']:raise RuntimeError('integrity mismatch: '+name)
if len(d['files'])!=d['file_count']:raise RuntimeError('manifest count mismatch')
print(json.dumps({'integrity':'PASS','SHA256_files':len(d['files'])}))
