from pathlib import Path
from math import gcd
import json,sys,hashlib
from flint import fmpz_poly
OUT=Path(__file__).resolve().parent;BASE=OUT.parent/'row393'
sys.path.insert(0,str(BASE/'parent392/parent391/parent390/parent389/parent388/parent381'))
from verify_row380 import G,prime_factors
if not __debug__:raise RuntimeError('Do not run with -O')
bs=json.loads((BASE/'discovery/scan_basis.json').read_text());zk=list(zip(bs['basis_numerators'],bs['basis_denominators']))
rows=json.loads((BASE/'new_relations393.json').read_text());results=[]
for name in ['pair_terms.jsonl','pair_wide_terms.jsonl']:
 lines=(OUT/name).read_text().splitlines();assert len(lines)==1
 data=json.loads(lines[0]);terms=data['terms'];den=max(zk[j][1] for j,e in terms)
 h=sum((e*(den//zk[j][1])*fmpz_poly(zk[j][0]) for j,e in terms),fmpz_poly());content=gcd(*map(int,h));h=h//content
 if h.leading_coefficient()<0:h=-h
 matches=[j for j,row in enumerate(rows) if list(map(int,h))==row['coefficients'] or list(map(int,-h))==row['coefficients']]
 assert matches==[0];old=rows[0];norm=abs(int(G.resultant(h)));assert norm==old['absolute_norm']*2**(105*old['denominator_exponent'])
 assert old['valuations']==[[827,0,1],[667801,3,1],[15849133,0,1]]
 results.append(dict(file=name,parent_generator_index=0,exact_absolute_norm=old['absolute_norm'],denominator_exponent=old['denominator_exponent'],new=False))
json.dump(results,open(OUT/'returned_candidate_checks.json','w'),indent=2);print(json.dumps(results,indent=2))
