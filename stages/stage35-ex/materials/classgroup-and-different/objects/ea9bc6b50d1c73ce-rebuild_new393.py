#!/usr/bin/env python3
"""Rebuild all new number-field arithmetic (python-flint required).
Old profiles are inherited from byte-bound audited row392; not re-derived here.
"""
from pathlib import Path
if not __debug__: raise RuntimeError('Certification requires Python without -O')
import sys,json,time
from flint import fmpz_poly
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'parent392'/'parent391'/'parent390'/'parent389'/'parent388'/'parent381'))
import verify_units381 as v
from verify_row380 import prime_factors,unit_code,w_roots,local
read=lambda n:json.loads((HERE/n).read_text())
rows=read('new_relations393.json');start=time.perf_counter()
for i,row in enumerate(rows):
    out=v.full_profile(row);assert out is not None
    vals,code,positive_h=out;h=fmpz_poly(row['coefficients']);k=row['denominator_exponent']
    assert row['norm_sign']==(1 if positive_h==h else -1)
    assert abs(int(v.G.resultant(h)))==row['absolute_norm']*2**(105*k)
    for j,a in enumerate(h(v.X+1)):assert int(a)%2**max(0,k-j//3)==0
    for j in [0,1]:
        a=vals.get((2,j),0)-3*k;assert a>=0
        if a:vals[2,j]=a
        else:vals.pop((2,j),None)
    assert [[p,j,a] for (p,j),a in sorted(vals.items()) if a]==row['valuations']
    assert code==int(row['local_unit_code'],16)
    assert [[p,j] for (p,j),a in sorted(vals.items()) if p!=2 and a&1]==row['mod2_labels']
    if i%100==99:print('new exact profiles',i+1,'seconds',round(time.perf_counter()-start,1),flush=True)
old={int(p):d for p,d in json.loads((HERE/'parent392'/'factorizations392.json').read_text()).items()}
factors={int(p):d for p,d in read('factorizations393.json').items()}
for count,p in enumerate(sorted(factors.keys()-old.keys())):
    _,ff=prime_factors(p);ff=sorted(ff,key=lambda a:a[2])
    assert factors[p]==[[g.degree() for g,e,j in ff],[e for g,e,j in ff]]
    if count%200==199:print('new prime decompositions',count+1,flush=True)
roots=w_roots();uc=read('unit_kernel393.json')['rational_unit_codes_mod8']
for a in [1,3,5,7]:assert uc[str(a)]==hex(local.combine(unit_code(fmpz_poly([a]),0,0,roots)))
print('PASS all',len(rows),'new exact integral generators, norms, complete ideal valuations, local unit parts;',len(factors)-len(old),'additional prime decompositions;', 'four rational unit classes')
