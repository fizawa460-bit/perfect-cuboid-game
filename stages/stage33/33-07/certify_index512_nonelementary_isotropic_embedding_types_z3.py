#!/usr/bin/env python3
"""Exact isotropic-embedding existence test for the 8 non-elementary H types.

The abstract LR filter leaves eight non-elementary order-512 group types.
For each type mu=(r_i), this script asks whether H=direct_sum Z/2^r_i embeds
injectively and totally isotropically into
  A0=(Z/8)^10 direct_sum (Z/16)^4
with q(x)=sum_X x_j^2/8 + sum_Y x_j^2/16 mod 2Z.

Write a generator of order 2^r in normalized coordinates u_j via
x_j=2^(e_j-r) u_j (e_j=3 or4), 0<=u_j<2^r. Injectivity is equivalent
to independence of the order-two multiples, hence to F2 independence of the
parity vectors u_i mod2. Total isotropy is equivalent to q(g_i)=0 and
b(g_i,g_j)=0 for all generator pairs. Thus the SMT problem is finite and exact.
SAT witnesses are independently checked with ordinary Python arithmetic.
"""
import hashlib,json
from pathlib import Path
from z3 import Int,Or,Solver,sat,unsat
HERE=Path(__file__).resolve().parent
LR=json.loads((HERE/'index512-abstract-glue-types-lr-retained.json').read_text())
LR_LOCK='dd14ecc255244db71a0a1fdcc8af7a5d9a8e957857dec7c879ed8c51d756746a'
if LR['canonical_sha256']!=LR_LOCK:raise SystemExit('LR source lock moved')
all_types=[tuple(x) for x in LR['abstract_H_types_after_two_exact_sequence_LR_filter']]
elementary=(1,)*9
TYPES=[x for x in all_types if x!=elementary]
if len(TYPES)!=8:raise SystemExit('non-elementary type census regression')
E=[3]*10+[4]*4

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
    if len(W)!=len(mu) or any(len(r)!=14 for r in W):return False
    for i,r in enumerate(mu):
        if any(not(0<=int(W[i][j])<2**r) for j in range(14)):return False
        if q32(W[i],r)!=0:return False
    if parity_rank(W)!=len(mu):return False
    for i in range(len(mu)):
        for k in range(i):
            if b16(W[i],mu[i],W[k],mu[k])!=0:return False
    # Convert normalized witness to actual A0 coordinates and verify exact
    # generator orders and all 512 subgroup elements are distinct/isotropic.
    actual=[]
    for row,r in zip(W,mu):actual.append([(2**(E[j]-r))*int(row[j]) for j in range(14)])
    seen=set()
    def add(coeffs):
        return tuple(sum(coeffs[i]*actual[i][j] for i in range(len(mu)))%(2**E[j]) for j in range(14))
    def q_actual(x):
        return (sum(2*x[j]*x[j] for j in range(10))+sum(x[j]*x[j] for j in range(10,14)))%32
    import itertools
    for coeffs in itertools.product(*[range(2**r) for r in mu]):
        x=add(coeffs)
        if x in seen:return False
        seen.add(x)
        if q_actual(x)!=0:return False
    return len(seen)==512

def decide(mu):
    k=len(mu);U=[[Int(f'u_{i}_{j}') for j in range(14)] for i in range(k)]
    s=Solver();s.set(timeout=180000);s.set(random_seed=0)
    for i,r in enumerate(mu):
        for j in range(14):s.add(U[i][j]>=0,U[i][j]<2**r)
        q=sum((2**(7-2*r))*U[i][j]*U[i][j] for j in range(10))+sum((2**(8-2*r))*U[i][j]*U[i][j] for j in range(10,14))
        s.add(q%32==0)
    for i in range(k):
        for h in range(i):
            ri,rh=mu[i],mu[h]
            b=sum((2**(7-ri-rh))*U[i][j]*U[h][j] for j in range(10))+sum((2**(8-ri-rh))*U[i][j]*U[h][j] for j in range(10,14))
            s.add(b%16==0)
    # F2 independence of parity vectors: every nonzero binary combination is nonzero.
    for mask in range(1,1<<k):
        s.add(Or(*[(sum(U[i][j] for i in range(k) if (mask>>i)&1)%2)!=0 for j in range(14)]))
    res=s.check()
    if res==unsat:return {'status':'UNSAT','witness':None,'witness_verified':True}
    if res!=sat:raise SystemExit(f'isotropic embedding solver non-decision for {mu}: {res}')
    m=s.model();W=[[m.eval(U[i][j],model_completion=True).as_long() for j in range(14)] for i in range(k)]
    if not verify(mu,W):raise SystemExit(f'independent witness verification failed for {mu}')
    return {'status':'SAT','witness':W,'witness_verified':True}

results={}
for mu in TYPES:
    z=decide(mu);results[','.join(map(str,mu))]=z
summary={'SAT':sum(v['status']=='SAT' for v in results.values()),'UNSAT':sum(v['status']=='UNSAT' for v in results.values())}
if summary['SAT']+summary['UNSAT']!=8:raise SystemExit('decision census regression')
cert={'schema':'STAGE33_07_INDEX512_NONELEMENTARY_ISOTROPIC_EMBEDDING_TYPES_Z3_V1','source_lr_sha256':LR_LOCK,'abstract_non_elementary_types_before':8,'decision_summary':summary,'results':results,'isotropic_embedding_type_survivors':[k for k,v in results.items() if v['status']=='SAT'],'quadratic_endpoint_match_certified':False,'V4_action_match_certified':False,'actual_index512_glue_identified':False,'next_exact_leaf':'L33-07-FILTER-NONELEMENTARY-ISOTROPIC-TYPE-SURVIVORS-BY-ENDPOINT-QUADRATIC-MODULE-AND-V4-ACTION','unit_status':'RUNNING_REPAIR','stage33_progress':'6/11','stage33_08_released':False,'theorem_credit':False,'endpoint_credit':False}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'index512-nonelementary-isotropic-embedding-types-z3.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'SAT_types':summary['SAT'],'UNSAT_types':summary['UNSAT'],'survivors':cert['isotropic_embedding_type_survivors'],'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
