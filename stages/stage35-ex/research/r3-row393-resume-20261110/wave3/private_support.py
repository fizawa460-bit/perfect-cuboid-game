"""Certify why these 55 new rows impose no relation on the old support."""
import json,sys
from collections import Counter
from pathlib import Path
if not __debug__:raise RuntimeError('Python -O is unsupported')
O=Path(__file__).resolve().parent;B=O.parent/'row393'
sys.path.insert(0,str(B/'parent392/parent391/parent390/parent389/parent388/parent381'))
sys.path.insert(0,str(O.parent/'wave2'))
import verify_units381 as units
import verify_row380 as parent
from arbitrary_precision import activate,polynomial
from prime_certificates import verify
proved=verify(json.loads((O/'prime_certificates.json').read_text()))
activate(units,parent,lambda p:p in proved)
rows=json.loads((O/'new_relations_wave3.json').read_text())
old={int(p) for p in json.loads((O.parent/'wave2/factorizations_wave2.json').read_text())}
occ=Counter(p for r in rows for p,e in r['odd_factorization'])
cert=[]
for i,r in enumerate(rows):
    large=[(p,e) for p,e in r['odd_factorization'] if p>=2**64]
    assert len(large)==1
    p,e=large[0];assert e==1 and occ[p]==1 and p not in old
    gn,gs=parent.prime_factors(p)
    assert all(m==1 for g,m,j in gs) and len(gs)>=2
    h=polynomial(r['coefficients'],p);common=gn.gcd(h)
    assert common.degree()==1
    hit=[j for g,m,j in gs if (common%g).is_zero()]
    assert len(hit)==1
    j=hit[0];assert [x for x in r['valuations'] if x[0]==p]==[[p,j,1]]
    other=min(k for g,m,k in gs if k!=j)
    cert.append(dict(generator_index=i,private_prime=p,hit_label=j,unhit_label=other,
        rho_root=-int(common[0])*pow(int(common[1]),-1,p)%p,
        local_two_column_matrix=[[1,0],[1,1]]))
assert len(cert)==55
out=dict(private_supports=cert,all_55_rows_checked=True,
    conclusion='New row span plus new rational-prime rows has zero intersection with the old coordinate space; old finite quotient embeds unchanged.',
    formal_dimension_before=180,formal_dimension_after=180,
    scope='This finite extension only; future relations sharing these primes can change the conclusion.')
(O/'private_support_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS 55 private prime supports; old finite quotient unchanged; no global impossibility claim')
