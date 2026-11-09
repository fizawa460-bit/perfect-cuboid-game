import sys,json
from pathlib import Path
DATA=Path(__file__).resolve().parent
(DATA/'rerun').mkdir(exist_ok=True)
if not __debug__: raise RuntimeError("Run certification/discovery scripts without Python -O")
sys.path.insert(0,str((DATA.parent/'parent392'/'parent391'/'parent390'/'parent389'/'parent388'/'parent381')))
from verify_row380 import unit_code,w_roots,local
from flint import fmpz_poly
sys.path.insert(0,str((DATA.parent/'parent392'/'parent391'/'parent390'/'parent389'/'parent388')))
from verify_row388 import binary_basis,parity_mask
P=(DATA.parent/'parent392'/'parent391'/'parent390'/'parent389'/'parent388');O=(DATA/'rerun');profiles=json.loads((P/'profiles388.json').read_text())+json.loads(((DATA.parent/'parent392'/'parent391'/'parent390'/'parent389')/'new_relations389.json').read_text())+json.loads(((DATA.parent/'parent392'/'parent391'/'parent390')/'new_relations390.json').read_text())+json.loads(((DATA.parent/'parent392'/'parent391')/'new_relations391.json').read_text())+json.loads(((DATA.parent/'parent392')/'new_relations392.json').read_text());new=json.loads((O/'new_relations393.json').read_text());factors={int(p):v for p,v in json.loads((O/'all_factorizations393.json').read_text()).items()};cert=json.loads((O/'relation_certificate393.json').read_text())
roots=w_roots();rational_codes={str(r):hex(local.combine(unit_code(fmpz_poly([r]),0,0,roots))) for r in [1,3,5,7]}
codes=[int(r['local_unit_code'],16) for r in profiles]+[int(rational_codes[str(p%8)],16) for p in sorted(factors)]+[int(r['local_unit_code'],16) for r in new]
unit=[]
for k in cert['integer_kernel']:
 u=0
 for i,e in k:
  if e&1:u^=codes[i]
 unit.append(u)
piv,dependencies=binary_basis(unit);assert len(piv)==55
masks=[parity_mask(k) for k in cert['integer_kernel']];squares=[]
for dep in dependencies:
 c=0
 for i,m in enumerate(masks):
  if dep>>i&1:c^=m
 squares.append(c)
assert len(squares)==len(unit)-55 and len(binary_basis(squares)[0])==len(squares)
out={'rational_unit_codes_mod8':rational_codes,'integer_kernel_local_codes':[hex(u) for u in unit],
 'global_square_relations_as_generator_masks':[hex(c) for c in squares],'unit_local_rank':55,'global_square_relations_dimension':len(squares)}
(O/'unit_kernel393.json').write_text(json.dumps(out,separators=(',',':')))
print('integer unit relations',len(unit),'local rank',len(piv),'global square relation basis',len(squares))
