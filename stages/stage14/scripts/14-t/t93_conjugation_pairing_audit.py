#!/usr/bin/env python3
import itertools, json

def walsh_coeff(vals,r,S):
    total=0.0
    for eps,v in vals.items():
        ch=1
        for i in S: ch*=eps[i]
        total += v*ch
    return total/(2**r)

checks=0
odd_cancel=0
principal_survival=0
max_r=8
for r in range(1,max_r+1):
    cube=list(itertools.product((-1,1), repeat=r))
    # nonnegative conjugation-invariant stress weight; mean is positive
    vals={e: 1 + int(sum(e)>=0) + int(sum(e)<=0) for e in cube}
    even={e:(vals[e]+vals[tuple(-x for x in e)])/2 for e in cube}
    odd={e:(vals[e]-vals[tuple(-x for x in e)])/2 for e in cube}
    assert abs(sum(odd.values()))<1e-12
    odd_cancel += 1
    mu=sum(vals.values())/(2**r)
    assert mu>0
    principal_survival += 1
    for mask in range(1<<r):
        S=[i for i in range(r) if mask>>i&1]
        ce=walsh_coeff(even,r,S)
        co=walsh_coeff(odd,r,S)
        if len(S)%2: assert abs(ce)<1e-12
        else: assert abs(co)<1e-12
        checks += 1
out={
 "stage":"14-t93",
 "walsh_parity_checks":checks,
 "odd_sector_cancellation_checks":odd_cancel,
 "positive_principal_mean_stress_checks":principal_survival,
 "max_cube_rank":max_r,
 "boundary":{
  "CONJUGATION_IS_GLOBAL_ORIENTATION_ANTIPODE":True,
  "WALSH_PARITY_SPLIT_EXACT":True,
  "ODD_WALSH_SECTOR_ANTIPODALLY_CENTERED":True,
  "PRINCIPAL_CUBE_MEAN_KILLED_BY_CONJUGATION":False,
  "CENTERED_EVEN_SPECTRUM_ELIMINATED":False,
  "TH27_NEEDED":False,
  "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT":"1/2",
  "STRICT_SUBSQRT_POWER_SAVING_PROVED":False,
  "NEXT":"Stage14-t94"
 }}
print(json.dumps(out,sort_keys=True))
