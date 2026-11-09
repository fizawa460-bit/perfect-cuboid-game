#!/usr/bin/env python3
"""Recompute all 4,143 exact principal ideal valuations and local unit parts.
Requires python-flint; uses only included, byte-bound audited parent arithmetic.
"""
import json,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'parent381'))
import verify_units381 as v
from verify_row380 import prime_factors,TABLE
read=lambda n:json.loads((HERE/'parent381'/n).read_text())
rows=[{'coefficients':[2],'odd_factorization':[]},{'coefficients':[-1,1],'odd_factorization':[]},
      {**read('dyadic_principal.json'),'odd_factorization':[]}]+read('principal_witnesses.json')+read('new_relations.json')
profiles=[];start=time.perf_counter()
for i,row in enumerate(rows):
    out=v.full_profile(row);assert out is not None
    vals,code,h=out
    profiles.append({'valuations':[[p,j,e] for (p,j),e in sorted(vals.items()) if e],
                     'local_unit_code':hex(code),
                     'norm_sign':1 if h==v.fmpz_poly(row['coefficients']) else -1})
    if i%400==0:print('exact profiles',i,round(time.perf_counter()-start,1),flush=True)
assert profiles==json.loads((HERE/'profiles388.json').read_text())
ps={p for row in rows for p,e in row['odd_factorization']}
factors={}
for p in sorted(ps):
    if p in TABLE:
        ds=[len(f)-1 for f in TABLE[p]['factors_ascending']]
        factors[p]=[ds,[1]*len(ds)]
    else:
        _,ff=prime_factors(p);ff=sorted(ff,key=lambda a:a[2])
        factors[p]=[[g.degree() for g,e,j in ff],[e for g,e,j in ff]]
assert factors=={int(p):d for p,d in json.loads((HERE/'factorizations388.json').read_text()).items()}
print('PASS: all 4143 profiles, all 4344 rational-prime factorizations equal')
frontier={int(p):d for p,d in json.loads((HERE/'frontier_factorizations388.json').read_text()).items()}
for p in sorted(frontier.keys()-factors.keys()):
    _,ff=prime_factors(p);ff=sorted(ff,key=lambda a:a[2])
    assert frontier[p]==[[g.degree() for g,e,j in ff],[e for g,e,j in ff]]
assert all(frontier[p]==d for p,d in factors.items())
print('PASS: all additional finite-frontier factorizations equal')
