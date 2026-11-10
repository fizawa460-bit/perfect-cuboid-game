"""Extract a checkable principal-product witness for the one lost formal direction."""
import json,runpy
from pathlib import Path
if not __debug__:raise RuntimeError('Python -O is unsupported')
O=Path(__file__).resolve().parent;d=runpy.run_path(str(O/'analyse.py'))
old=json.loads((O.parent/'new394/certificate_candidate394.json').read_text())['remaining_formal_basis']
assert len(old)==181
small={};deps=[]
for i,a in enumerate(old):
    v,_=d['reduce'](1<<d['ix'][tuple(a[:2])],d['piv']);c=1<<i
    while v:
        k=v.bit_length()-1
        if k not in small:small[k]=(v,c);break
        w,e=small[k];v^=w;c^=e
    if not v:deps.append(c)
assert len(small)==180 and len(deps)==1
selected=[old[i] for i in range(181) if deps[0]>>i&1]
vector=sum(1<<d['ix'][tuple(a[:2])] for a in selected)
res,c=d['reduce'](vector,d['piv']);assert res==0
used=[i for i in range(len(d['rows'])) if c>>i&1]
vals={}
for i in used:
    for key,e in d['rows'][i].items():vals[key]=vals.get(key,0)+e
targets={tuple(a[:2]) for a in selected}
assert {key for key,e in vals.items() if e&1}==targets
witness=dict(dependent_previous_basis_direction=[2999,0],relation_mod2=selected,
    old_generator_indices=[i for i in used if i<len(d['old'])],
    rational_primes=[d['ps'][i-len(d['old'])] for i in used if len(d['old'])<=i<d['base_n']],
    new_generator_indices=[i-d['base_n'] for i in used if i>=d['base_n']],
    half_ideal_factors=[[p,j,(e-int((p,j) in targets))//2] for (p,j),e in sorted(vals.items()) if (e-int((p,j) in targets))//2],
    identity='Product of listed generators and rational primes = product of selected prime ideals times I^2 (as fractional ideals)')
(O/'dependency_witness.json').write_text(json.dumps(witness,indent=2)+'\n')
# Build a new formal dual, proving P827 still survives this finite presentation.
v,_=d['reduce'](1<<d['ix'][(827,0)],d['piv']);assert v
lam=1<<(v.bit_length()-1)
for k,(row,c) in sorted(d['piv'].items()):
    if (row&lam).bit_count()%2:lam^=1<<k
assert all((d['vec'](r)&lam).bit_count()%2==0 for r in d['rows'])
assert lam>>d['ix'][(827,0)]&1
(O/'dual_wave2.json').write_text(json.dumps(dict(nonzero_labels=[x for i,x in enumerate(d['labels']) if lam>>i&1],all_rows_annihilated=True,p827_value=1,scope='finite presentation only; not a true class-group character'),indent=2)+'\n')
print('DEPENDENCY',selected,'old generators',len(witness['old_generator_indices']),'new',len(witness['new_generator_indices']))
