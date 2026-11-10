"""Low-pivot replay and direct integer addition for all extracted witnesses."""
import json
from pathlib import Path
if not __debug__:raise RuntimeError('Python -O is unsupported')
O=Path(__file__).resolve().parent;B=O.parent/'row393';P=B/'parent392/parent391/parent390/parent389/parent388'
paths=[P/'profiles388.json',P.parent/'new_relations389.json',P.parent.parent/'new_relations390.json',P.parent.parent.parent/'new_relations391.json',B/'parent392/new_relations392.json',B/'new_relations393.json',O.parent/'new394/new_relations394.json',O.parent/'wave2/new_relations_wave2.json',O.parent/'wave3/new_relations_wave3.json',O.parent/'wave4/new_relations_wave4.json']
old=sum((json.loads(p.read_text()) for p in paths),[])
new=json.loads((O/'new_relations_wave5.json').read_text())
factors={int(p):v for p,v in json.loads((O/'factorizations_wave5.json').read_text()).items()}
expected=json.loads((O/'results_wave5.json').read_text())
labels=[(2,0),(2,1)]+[(p,j) for p,v in sorted(factors.items()) for j in range(len(v[0]))];ix={a:i for i,a in enumerate(labels)}
rats=[[(p,j,e) for j,e in enumerate(v[1])] for p,v in sorted(factors.items())]
rows=[r['valuations'] for r in old]+rats+[r['valuations'] for r in new]
def vector(row):
    v=0
    for p,j,e in row:
        if e%2:v^=1<<ix[p,j]
    return v
def reduce(b,v):
    while v:
        k=(v&-v).bit_length()-1
        if k not in b:return v
        v^=b[k]
    return 0
def add(b,v):
    v=reduce(b,v)
    if v:b[(v&-v).bit_length()-1]=v
def fb_dimension(b):
    copy=b.copy()
    for p,j,q in fb:add(copy,1<<ix[p,j])
    return len(copy)-len(b)
fb=[(2,0,128)]+[(p,j,p**d) for p,(ds,es) in factors.items() for j,d in enumerate(ds) if p**d<=6768];assert len(fb)==878
b={}
for row in rows[:len(old)+len(rats)]:add(b,vector(row))
baseline=len(b);assert baseline==expected['old_plus_new_rational_rank'] and fb_dimension(b)==178
assert sum(reduce(b,1<<ix[p,j])==0 for p,j,q in fb)==628
for r in new:add(b,vector(r['valuations']))
assert len(b)==expected['new_rank'] and fb_dimension(b)==expected['new_formal_dimension']
assert sum(reduce(b,1<<ix[p,j])==0 for p,j,q in fb)==expected['new_individually_zero']
assert (reduce(b,1<<ix[827,0])==0)==expected['p827_zero']
witnesses=json.loads((O/'dependency_witnesses.json').read_text())
zeros=json.loads((O/'certificate_wave5.json').read_text())['witnesses']
for w in witnesses+zeros:
    vals={};selected=[old[i]['valuations'] for i in w['old_generator_indices']]+[new[i]['valuations'] for i in w['new_generator_indices']]
    selected += [[(p,j,e) for j,e in enumerate(factors[p][1])] for p in w['rational_primes']]
    for row in selected:
        for p,j,e in row:vals[p,j]=vals.get((p,j),0)+e
    rhs={(p,j):2*e for p,j,e in w['half_ideal_factors']}
    for p,j,q in w.get('relation_mod2',[w.get('prime_ideal')]):rhs[p,j]=rhs.get((p,j),0)+1
    assert {k:v for k,v in vals.items() if v}=={k:v for k,v in rhs.items() if v}
dual=json.loads((O/'dual_wave5.json').read_text())
if not expected['p827_zero']:
    support=set(map(tuple,dual['nonzero_labels']));assert (827,0) in support
    assert all(sum(e for p,j,e in row if (p,j) in support)%2==0 for row in rows)
by_prime={tuple(w['prime_ideal'][:2]):w for w in zeros}
u,v=by_prime[(3313,2)],by_prime[(4957,0)]
assert u['new_generator_indices']==v['new_generator_indices']==[825]
assert u['rational_primes']==v['rational_primes']==[]
old_difference={}
for sign,w in [(1,u),(-1,v)]:
    for i in w['old_generator_indices']:
        for p,j,e in old[i]['valuations']:
            old_difference[p,j]=old_difference.get((p,j),0)+sign*e
rhs={(3313,2):1,(4957,0):-1}
for sign,w in [(1,u),(-1,v)]:
    for p,j,e in w['half_ideal_factors']:
        rhs[p,j]=rhs.get((p,j),0)+2*sign*e
assert {k:v for k,v in old_difference.items() if v}=={k:v for k,v in rhs.items() if v}
result=dict(method='low pivots and integer valuation witness sums',rows=len(rows),columns=len(labels),baseline_rank=baseline,final_rank=len(b),formal_dimension_before=178,formal_dimension_after=fb_dimension(b),dependency_witnesses_verified=len(witnesses),individual_zero_witnesses_verified=len(zeros),p827_zero=expected['p827_zero'])
result['old_3313_to_4957_bridge_verified_from_valuations']=True
(O/'linear_verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
