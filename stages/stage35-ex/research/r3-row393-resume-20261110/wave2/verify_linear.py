"""Second GF(2) implementation: low pivots and direct integer witness summation."""
import json
from pathlib import Path
if not __debug__:raise RuntimeError('Python -O is unsupported')
O=Path(__file__).resolve().parent;B=O.parent/'row393';P=B/'parent392/parent391/parent390/parent389/parent388'
paths=[P/'profiles388.json',P.parent/'new_relations389.json',P.parent.parent/'new_relations390.json',P.parent.parent.parent/'new_relations391.json',B/'parent392/new_relations392.json',B/'new_relations393.json',O.parent/'new394/new_relations394.json']
old=sum((json.loads(p.read_text()) for p in paths),[])
new=json.loads((O/'new_relations_wave2.json').read_text())
factors={int(p):v for p,v in json.loads((O/'factorizations_wave2.json').read_text()).items()}
labels=[(2,0),(2,1)]+[(p,j) for p,v in sorted(factors.items()) for j in range(len(v[0]))]
ix={a:i for i,a in enumerate(labels)}
rats=[[(p,j,e) for j,e in enumerate(v[1])] for p,v in sorted(factors.items())]
rows=[r['valuations'] for r in old]+rats+[r['valuations'] for r in new]
def vector(row):
    v=0
    for p,j,e in row:
        if e%2:v^=1<<ix[p,j]
    return v
def add(b,v):
    while v:
        k=(v&-v).bit_length()-1
        if k not in b:b[k]=v;return
        v^=b[k]
def fb_dimension(b):
    copy=b.copy()
    for p,j,q in fb:add(copy,1<<ix[p,j])
    return len(copy)-len(b)
fb=[(2,0,128)]+[(p,j,p**d) for p,(ds,es) in factors.items() for j,d in enumerate(ds) if p**d<=6768]
assert len(fb)==878
b={}
for row in rows[:len(old)+len(rats)]:add(b,vector(row))
baseline_rank=len(b);assert baseline_rank==14533 and fb_dimension(b)==181
for r in new:add(b,vector(r['valuations']))
assert len(b)==15121 and fb_dimension(b)==180
w=json.loads((O/'dependency_witness.json').read_text());vals={}
selected=[old[i]['valuations'] for i in w['old_generator_indices']]+[new[i]['valuations'] for i in w['new_generator_indices']]
selected += [[(p,j,e) for j,e in enumerate(factors[p][1])] for p in w['rational_primes']]
for row in selected:
    for p,j,e in row:vals[p,j]=vals.get((p,j),0)+e
rhs={(p,j):2*e for p,j,e in w['half_ideal_factors']}
for p,j,q in w['relation_mod2']:rhs[p,j]=rhs.get((p,j),0)+1
assert {k:v for k,v in vals.items() if v}=={k:v for k,v in rhs.items() if v}
dual=json.loads((O/'dual_wave2.json').read_text());support=set(map(tuple,dual['nonzero_labels']))
assert (827,0) in support
assert all(sum(e for p,j,e in row if (p,j) in support)%2==0 for row in rows)
result=dict(method='low pivots plus integer valuation witness; separate from high-pivot extraction',
    rows=len(rows),columns=len(labels),baseline_with_new_rational_rank=baseline_rank,
    final_rank=len(b),formal_dimension_before=181,formal_dimension_after=180,
    dependency_exact=True,p827_formal_dual_verified=True)
(O/'linear_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
