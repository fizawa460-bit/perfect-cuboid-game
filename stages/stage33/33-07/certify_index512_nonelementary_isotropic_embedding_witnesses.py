#!/usr/bin/env python3
"""Deterministic exact witnesses for all eight LR-surviving non-elementary H types."""
import hashlib,itertools,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
LR=json.loads((HERE/'index512-abstract-glue-types-lr-retained.json').read_text())
LOCK='dd14ecc255244db71a0a1fdcc8af7a5d9a8e957857dec7c879ed8c51d756746a'
if LR['canonical_sha256']!=LOCK: raise SystemExit('LR source lock moved')
TYPES=[tuple(x) for x in LR['abstract_H_types_after_two_exact_sequence_LR_filter'] if tuple(x)!=(1,)*9]
if TYPES!=[(3,3,1,1,1),(3,2,2,1,1),(3,2,1,1,1,1),(3,1,1,1,1,1,1),(2,2,2,2,1),(2,2,2,1,1,1),(2,2,1,1,1,1,1),(2,1,1,1,1,1,1,1)]:
    raise SystemExit('non-elementary type order regression')
E=[3]*10+[4]*4
WIT={
'3,3,1,1,1':[[0,1,1,0,0,1,0,1,0,0,0,7,3,6],[0,1,2,7,2,0,0,5,7,0,2,1,7,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,1,0,1,0,0,0,0,0,1,0]],
'3,2,2,1,1':[[5,0,6,0,0,0,0,0,0,7,3,0,0,0],[2,0,0,1,1,0,2,0,0,0,3,1,3,0],[0,0,0,3,1,0,0,0,0,0,0,2,0,3],[0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0]],
'3,2,1,1,1,1':[[7,4,0,0,0,4,0,0,3,0,0,3,7,3],[0,3,1,0,2,2,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,0,0,1,0,0,1,0],[0,1,1,1,1,1,0,0,0,0,0,1,0,0]],
'3,1,1,1,1,1,1':[[7,4,0,2,4,6,7,0,6,0,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,1,0,0,0,1,0,0,0,0,1,0],[0,0,0,0,0,1,0,1,1,1,0,1,0,1],[0,1,0,1,0,0,0,1,1,0,1,0,0,0],[1,0,0,0,0,0,1,0,1,0,0,0,0,0]],
'2,2,2,2,1':[[0,2,3,0,1,0,0,0,3,1,0,0,0,0],[3,0,0,0,3,0,0,3,0,1,0,0,0,0],[0,0,0,2,2,0,0,2,0,0,0,1,0,1],[0,0,0,3,0,3,2,2,0,0,0,0,3,2],[0,1,1,0,0,0,0,0,0,0,0,1,0,0]],
'2,2,2,1,1,1':[[0,0,0,0,0,0,0,0,0,0,0,0,3,3],[0,0,2,0,0,0,0,0,0,0,3,0,0,1],[0,0,0,2,0,0,1,0,0,1,2,0,2,1],[0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,0,0,0,0,1,1,0,0,0,0,0,0,0]],
'2,2,1,1,1,1,1':[[0,3,1,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0,1,0,2,0,0,3],[0,0,0,0,1,0,0,1,0,0,0,1,0,0],[0,0,0,0,1,0,0,0,0,1,0,0,1,0],[0,0,1,0,0,1,0,0,0,1,0,0,0,0],[1,0,0,0,1,1,0,1,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,1,1,0,0,0,1]],
'2,1,1,1,1,1,1,1':[[0,0,1,0,0,0,0,1,0,0,0,0,0,3],[0,0,0,0,0,1,0,0,0,0,0,0,1,1],[0,0,0,1,0,0,0,0,0,0,1,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,1,0,1,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0]],
}
def parity_rank(rows):
    piv={}
    for row in rows:
        x=sum((int(v)&1)<<j for j,v in enumerate(row))
        while x:
            p=x.bit_length()-1
            if p in piv:x^=piv[p]
            else:piv[p]=x;break
    return len(piv)
def q32(row,r):
    return (sum((2**(7-2*r))*row[j]*row[j] for j in range(10))+sum((2**(8-2*r))*row[j]*row[j] for j in range(10,14)))%32
def b16(a,ra,b,rb):
    return (sum((2**(7-ra-rb))*a[j]*b[j] for j in range(10))+sum((2**(8-ra-rb))*a[j]*b[j] for j in range(10,14)))%16
def verify(mu,W):
    if len(W)!=len(mu) or any(len(row)!=14 for row in W): return False
    for row,r in zip(W,mu):
        if any(not 0<=int(v)<2**r for v in row) or q32(row,r): return False
    if parity_rank(W)!=len(mu): return False
    for i in range(len(mu)):
        for j in range(i):
            if b16(W[i],mu[i],W[j],mu[j]): return False
    actual=[[(2**(E[j]-r))*int(row[j]) for j in range(14)] for row,r in zip(W,mu)]
    seen=set()
    for coeffs in itertools.product(*[range(2**r) for r in mu]):
        x=tuple(sum(coeffs[i]*actual[i][j] for i in range(len(mu)))%(2**E[j]) for j in range(14))
        if x in seen: return False
        seen.add(x)
        if (sum(2*x[j]*x[j] for j in range(10))+sum(x[j]*x[j] for j in range(10,14)))%32: return False
    return len(seen)==512
results={}
for mu in TYPES:
    k=','.join(map(str,mu)); W=WIT[k]
    if not verify(mu,W): raise SystemExit('witness verification failed '+k)
    results[k]={'status':'SAT','witness':W,'all_512_elements_distinct_and_isotropic_verified':True}
cert={'schema':'STAGE33_07_INDEX512_NONELEMENTARY_ISOTROPIC_WITNESSES_V1','source_lr_sha256':LOCK,'abstract_non_elementary_types_before':8,'SAT_types':8,'UNSAT_types':0,'isotropic_embedding_type_survivors':list(results),'results':results,'quadratic_endpoint_match_certified':False,'V4_action_match_certified':False,'actual_index512_glue_identified':False,'next_exact_leaf':'L33-07-FILTER-8-NONELEMENTARY-ISOTROPIC-TYPES-BY-ENDPOINT-QUADRATIC-MODULE-AND-V4-ACTION','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,'theorem_credit':False,'endpoint_credit':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'index512-nonelementary-isotropic-embedding-witnesses.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'SAT_types':8,'UNSAT_types':0,'survivors':list(results),'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
