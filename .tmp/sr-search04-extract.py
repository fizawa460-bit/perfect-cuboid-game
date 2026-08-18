import json
from pathlib import Path
ids={f"SR-STR-{n:03d}" for n in [21,22,23,24,27,28,29,30]}
p=Path('docs/structure-radar/structure-registry.json')
reg=json.loads(p.read_text())
if isinstance(reg, dict):
    seq=reg.get('structures') or reg.get('cards') or reg.get('registry') or []
else:
    seq=reg
out=[x for x in seq if isinstance(x,dict) and x.get('structure_id') in ids]
Path('.tmp/sr-search04-cards.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('found',len(out),[x.get('structure_id') for x in out])
if len(out)!=8: raise SystemExit(2)
