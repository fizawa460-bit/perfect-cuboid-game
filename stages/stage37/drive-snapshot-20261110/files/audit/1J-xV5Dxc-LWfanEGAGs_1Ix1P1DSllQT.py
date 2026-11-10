"""Independent numerical checks; proofs in TI-005 are parameter uniform."""
from math import gcd,isqrt
from itertools import product
import json
from ti005_rank_bound import matrix,factors,sf

def annihilated(rows,cols,d):
    vec=[int(d%p==0) for p in cols]
    return all(sum(x*y for x,y in zip(row,vec))%2==0 for row in rows)

def fullcover(a,b,d,mod):
    squares={c*c%mod for c in range(mod)}
    return all((d*z**4+a*z*z*t*t+(b//d)*t**4)%mod not in squares
               for z in range(mod) for t in range(mod) if gcd(gcd(z,t),mod)==1)

rows=[matrix(m,n) for m,n in [(2,1),(6,1),(11,2),(8,5),(18,7),(4,1),(9,4)]]
for r in rows:
    cols=r['B_columns'];v,w=r['V'],r['W'];a=4*(v*v+w*w);b=16*v*v*w*w
    assert annihilated(r['B'],cols,sf(2*v)) and annihilated(r['B'],cols,sf(2*w))
    if r['forced_sfmn']!=1:
        assert r['forced_sfmn']!=r['forced_sf2W'] and r['forced_sf2W']!=1
        assert r['delta_old']>=1
    a_vectors=[x for x in product([0,1],repeat=len(r['A_columns'])) if all(sum(a*b for a,b in zip(x,row))%2==0 for row in r['A'])]
    for name in ['B','B_enhanced']:
        vectors=[x for x in product([0,1],repeat=len(cols)) if all(sum(a*b for a,b in zip(x,row))%2==0 for row in r[name])]
        assert len(vectors)>=2
        expected=r['delta_old'] if name=='B' else r['delta_new']
        assert len(a_vectors)*len(vectors)==2**(expected+1)
cover_checks=[]
for m,n,ds in [(2,1,[2,-2,10,-10]),(6,1,[6,-6]),(11,2,[22,-22])]:
    r=matrix(m,n);v,w=r['V'],r['W'];a=4*(v*v+w*w);b=16*v*v*w*w
    for d in ds:
        assert fullcover(a,b,d,512)
        cover_checks.append(dict(m=m,n=n,d=d,modulus=512,full_primitive_pair_nonsolubility=True))
# Known physical brick reconstruction; its cutoff remains R_phys, not maxedge.
p,q=matrix(11,2),matrix(8,5);g=gcd(p['U'],q['U'])
X,Y,Z=p['U']*q['U']//g,p['V']*q['U']//g,p['U']*q['V']//g
assert (X,Y,Z)==(117,44,240)
assert all(isqrt(a*a+b*b)**2==a*a+b*b for a,b in [(X,Y),(X,Z),(Y,Z)])
assert p['TI_CLOSED'] and not q['TI_CLOSED']
report=dict(status='PASS',forced_kernel_fixtures=7,two_adic_cover_checks=cover_checks,
            enhanced_certified_sources=[[r['m'],r['n']] for r in rows if r['TI_CLOSED']],
            physical_witness=dict(edges=[X,Y,Z],closed_source=[11,2],other_source=[8,5]),
            scope='Finite checks supplement uniform proofs. No physical weights or density evaluated.')
open('ti005_audit.json','w').write(json.dumps(report,indent=2));print(json.dumps(report))
