"""Exact principal-product witnesses for new dependencies in the old 180-space."""
import json,runpy
from pathlib import Path
if not __debug__:raise RuntimeError('Python -O is unsupported')
O=Path(__file__).resolve().parent;d=runpy.run_path(str(O/'analyse.py'))
old=json.loads((O.parent/'wave3/certificate_wave3.json').read_text())['remaining_formal_basis']
assert len(old)==180
small={};deps=[]
for i,a in enumerate(old):
    v,_=d['reduce'](1<<d['ix'][tuple(a[:2])],d['piv']);c=1<<i
    while v:
        k=v.bit_length()-1
        if k not in small:small[k]=(v,c);break
        w,e=small[k];v^=w;c^=e
    if not v:deps.append(c)
assert len(small)==d['results']['new_formal_dimension']
witnesses=[]
for dep in deps:
    selected=[old[i] for i in range(180) if dep>>i&1]
    vector=sum(1<<d['ix'][tuple(a[:2])] for a in selected)
    res,c=d['reduce'](vector,d['piv']);assert res==0
    used=[i for i in range(len(d['rows'])) if c>>i&1];vals={}
    for i in used:
        for key,e in d['rows'][i].items():vals[key]=vals.get(key,0)+e
    targets={tuple(a[:2]) for a in selected}
    assert {key for key,e in vals.items() if e&1}==targets
    witnesses.append(dict(relation_mod2=selected,
        old_generator_indices=[i for i in used if i<len(d['old'])],
        rational_primes=[d['ps'][i-len(d['old'])] for i in used if len(d['old'])<=i<d['base_n']],
        new_generator_indices=[i-d['base_n'] for i in used if i>=d['base_n']],
        half_ideal_factors=[[p,j,(e-int((p,j) in targets))//2] for (p,j),e in sorted(vals.items()) if (e-int((p,j) in targets))//2]))
(O/'dependency_witnesses.json').write_text(json.dumps(witnesses,indent=2)+'\n')
v,_=d['reduce'](1<<d['ix'][(827,0)],d['piv'])
if v:
    lam=1<<(v.bit_length()-1)
    for k,(row,c) in sorted(d['piv'].items()):
        if (row&lam).bit_count()%2:lam^=1<<k
    assert all((d['vec'](r)&lam).bit_count()%2==0 for r in d['rows'])
    assert lam>>d['ix'][(827,0)]&1
    dual=dict(nonzero_labels=[x for i,x in enumerate(d['labels']) if lam>>i&1],all_rows_annihilated=True,p827_value=1,scope='finite presentation only; not a true class-group character')
else:dual=dict(p827_zero=True)
(O/'dual_wave4.json').write_text(json.dumps(dual,indent=2)+'\n')
print('DEPENDENCIES',len(witnesses),[w['relation_mod2'] for w in witnesses])
