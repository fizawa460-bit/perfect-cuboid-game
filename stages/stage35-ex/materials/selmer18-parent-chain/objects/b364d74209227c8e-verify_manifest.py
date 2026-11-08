from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
d=json.loads((R/'MANIFEST_SHA256.json').read_text())
for name,h in d.items():
 p=R/name
 if not p.is_file()or hashlib.sha256(p.read_bytes()).hexdigest()!=h:raise RuntimeError('SHA256 mismatch: '+name)
print('PASS',len(d),'files SHA256')
