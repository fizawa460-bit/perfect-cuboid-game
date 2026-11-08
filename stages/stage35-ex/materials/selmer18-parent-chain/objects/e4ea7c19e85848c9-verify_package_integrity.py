from pathlib import Path
import json,hashlib
p=Path(__file__).resolve().parent
m=json.loads((p/'SHA256SUMS.json').read_text())
for n,s in m.items():
 f=p/n
 if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=s:raise RuntimeError('missing or changed '+n)
print(json.dumps({'status':'HASHES_MATCH_NOT_MATH_AUDIT','files':len(m)}))
