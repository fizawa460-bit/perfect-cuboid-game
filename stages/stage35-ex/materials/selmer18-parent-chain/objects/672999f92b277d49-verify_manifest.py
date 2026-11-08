import hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent
data=json.loads((P/'MANIFEST_SHA256.json').read_text())
for name,h in data.items():
 if hashlib.sha256((P/name).read_bytes()).hexdigest()!=h:raise ArithmeticError('hash mismatch: '+name)
print(json.dumps({'status':'MANIFEST_PASS','files':len(data)}))
