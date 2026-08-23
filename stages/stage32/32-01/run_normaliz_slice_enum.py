#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib, sys, time
import PyNormaliz
from PyNormaliz import Cone

ROOT = pathlib.Path(__file__).resolve().parent
CORE = ROOT / 'picard-core.json'
OUT = ROOT / 'normaliz-slice-enum.json'
EXPECTED_BLOB = '0422b69847f2afb97cb7b3ed02ebef91279f61b1'

def qform(x, G):
    return sum(x[i]*G[i][j]*x[j] for i in range(64) for j in range(64))

def load_core():
    p=json.loads(CORE.read_text())
    assert p['schema']=='STAGE32_PICARD_CORE_INDLIST_V1'
    assert p['source']['git_blob_sha1']==EXPECTED_BLOB
    u=dict(p); claimed=u.pop('canonical_sha256_without_this_field')
    got=hashlib.sha256(json.dumps(u,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert got==claimed
    assert p['rank']==64 and p['known_class_count']==140 and p['h2']==16
    return p,got

def enumerate_degree(core, d):
    G=core['basis_gram']; h=core['hyperplane']; ineq=core['raw_cross_pairings_with_basis']
    hform=[sum(h[i]*G[i][j] for i in range(64)) for j in range(64)]
    # Normaliz inhomogeneous rows use [constant, x_1, ..., x_n].
    inh_ineq=[[0]+list(map(int,row)) for row in ineq]
    inh_eq=[[-int(d)]+list(map(int,hform))]
    t0=time.time()
    P=Cone(inhom_inequalities=inh_ineq, inhom_equations=inh_eq)
    pts=P.LatticePoints()
    elapsed=time.time()-t0
    # Normaliz may return homogenized points with a final/first denominator coordinate.
    vecs=[]
    for raw in pts:
        r=list(map(int,raw))
        if len(r)==64:
            x=r
        elif len(r)==65 and r[-1]==1:
            x=r[:-1]
        elif len(r)==65 and r[0]==1:
            x=r[1:]
        else:
            raise RuntimeError(f'unexpected lattice-point shape {len(r)}: {r[:4]}...{r[-4:]}')
        assert sum(hform[i]*x[i] for i in range(64))==d
        assert all(sum(ineq[k][i]*x[i] for i in range(64))>=0 for k in range(140))
        vecs.append(x)
    rows={}
    for g in (0,1):
        lower=-d-2+2*g
        kept=[x for x in vecs if qform(x,G)>=lower]
        rows[str(g)]={
            'self_intersection_lower_bound': lower,
            'candidate_count_after_adjunction_bound': len(kept),
            'self_intersections': sorted({qform(x,G) for x in kept}),
        }
    return {'degree':d,'slice_lattice_point_count':len(vecs),'elapsed_seconds':round(elapsed,3),'genus_filters':rows}

core,digest=load_core()
degrees=[int(a) for a in sys.argv[1:]] or [2]
results=[]
for d in degrees:
    if d<=0 or d%2: raise SystemExit('Stage32 audited window uses positive even degree')
    results.append(enumerate_degree(core,d))
payload={
 'schema':'STAGE32_NORMALIZ_FIXED_DEGREE_ENUM_V1',
 'upstream_blob':EXPECTED_BLOB,
 'picard_core_sha256':digest,
 'degrees':degrees,
 'results':results,
 'scope':'numerical necessary-condition enumeration only; no effectivity or receiver credit',
 'complete_census_claim':False,
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
print(json.dumps(payload,sort_keys=True))
