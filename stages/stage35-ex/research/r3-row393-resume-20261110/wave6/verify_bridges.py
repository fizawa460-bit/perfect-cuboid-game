"""Direct integer-valuation check of the two principal-product witnesses."""
import json
from collections import Counter
from pathlib import Path

if not __debug__:
    raise RuntimeError('Python -O is unsupported')
out = Path(__file__).resolve().parent
b = out.parent / 'row393'
p = b / 'parent392/parent391/parent390/parent389/parent388'
paths = [p/'profiles388.json',p.parent/'new_relations389.json',
    p.parent.parent/'new_relations390.json',p.parent.parent.parent/'new_relations391.json',
    b/'parent392/new_relations392.json',b/'new_relations393.json',
    out.parent/'new394/new_relations394.json',out.parent/'wave2/new_relations_wave2.json',
    out.parent/'wave3/new_relations_wave3.json',out.parent/'wave4/new_relations_wave4.json',
    out.parent/'wave5/new_relations_wave5.json']
old = sum((json.loads(path.read_text()) for path in paths), [])
new = json.loads((out/'new_relations_wave6.json').read_text())
witnesses = json.loads((out/'certificate_wave6.json').read_text())['witnesses']
by_target = {tuple(w['prime_ideal'][:2]):w for w in witnesses}
checks = []
for target,index in [((827,0),1156),((1277,3),210)]:
    w = by_target[target]
    assert w['new_generator_indices'] == [index] and not w['rational_primes']
    assert len(w['old_generator_indices']) == len(set(w['old_generator_indices']))
    a = Counter()
    for i in w['old_generator_indices']:
        a.update({(prime,j):e for prime,j,e in old[i]['valuations']})
    alpha = Counter({(prime,j):e for prime,j,e in new[index]['valuations']})
    actual = a.copy()
    actual.update(alpha)
    expected = Counter({(prime,j):2*e for prime,j,e in w['half_ideal_factors']})
    expected[target] += 1
    assert {k:v for k,v in actual.items() if v} == {k:v for k,v in expected.items() if v}
    odd_old = {label for label,e in a.items() if e % 2}
    odd_alpha = {label for label,e in alpha.items() if e % 2}
    assert odd_old == odd_alpha.symmetric_difference({target})
    checks.append({'target':list(target),'new_index':index,
        'old_generator_count':len(w['old_generator_indices']),
        'rational_prime_rows':0,'alpha_odd_support':sorted(map(list,odd_alpha)),
        'old_product_odd_support':sorted(map(list,odd_old)),
        'integer_valuation_equality':True})
assert checks[0]['old_product_odd_support'] == [[101,0],[673,2],[769,0]]
u = by_target[(1277,3)]
equivalent = [(2939,2),(2999,0),(6373,1),(6571,0)]
for target in equivalent:
    v = by_target[target]
    assert u['new_generator_indices'] == v['new_generator_indices'] == [210]
    assert not u['rational_primes'] and not v['rational_primes']
    difference = Counter()
    for sign,w in [(1,u),(-1,v)]:
        for i in w['old_generator_indices']:
            difference.update({(prime,j):sign*e for prime,j,e in old[i]['valuations']})
    expected = Counter({(1277,3):1,target:-1})
    for sign,w in [(1,u),(-1,v)]:
        expected.update({(prime,j):2*sign*e for prime,j,e in w['half_ideal_factors']})
    assert {k:v for k,v in difference.items() if v} == {k:v for k,v in expected.items() if v}
checks[1]['old_equivalent_targets'] = [list(x) for x in equivalent]
(out/'bridge_verification.json').write_text(json.dumps(checks,indent=2)+'\n')
print('PASS: two principal-product bridges, including the three-prime P827 complement')
