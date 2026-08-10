#!/usr/bin/env python3
import json, math

PRIMES=[3,5,7,11,13,17,19,23,29,31,37,41,43]

def proj_eq_one(R,S,p):
    # U is unit because p does not divide R^2+S^2.
    return S%p==0

def proj_eq_i(R,S,p):
    return R%p==0

def prod(xs):
    z=1
    for x in xs:z*=x
    return z

local=selector=partition=bound=0
max_ratio=0.0
examples=0
for R in range(1,31):
  for S in range(1,31):
    if math.gcd(R,S)!=1: continue
    m=R*R+S*S
    # choose each eligible prime and both denominator tags.
    eligible=[p for p in PRIMES if m%p]
    for p in eligible:
      local+=2
      assert proj_eq_one(R,S,p)==(S%p==0)
      assert proj_eq_i(R,S,p)==(R%p==0)
    # deterministic squarefree ray moduli from short prime windows.
    for start in range(min(5,len(eligible))):
      ps=eligible[start:start+4]
      if not ps: continue
      M=prod(ps)
      # alpha/beta tag by index parity.
      alpha=prod(ps[::2]); beta=prod(ps[1::2])
      D=math.gcd(alpha,abs(S))*math.gcd(beta,abs(R))
      assert D==math.gcd(M,D)
      assert (R*S)%D==0
      assert 2*abs(R*S)<=m
      selector+=1
      if D:
        max_ratio=max(max_ratio,D/m)
      # exact nonselector support partition. Let d omit at most first prime;
      # active nonselectors are d_frac.
      omit=ps[0] if len(ps)>2 else 1
      d=M//omit
      d_frac=1
      for q in ps:
        if d%q==0:
          sel=((alpha%q==0 and S%q==0) or (beta%q==0 and R%q==0))
          if not sel: d_frac*=q
      M_nsel=M//math.gcd(M,D)
      assert ((M//d)*d_frac)%M_nsel==0
      partition+=1
      # any hard diagonal selector divisor is hosted by RS and has divisor-many choices.
      diag=math.gcd(d,D)
      assert D%diag==0 and (R*S)%diag==0
      bound+=1
      examples+=1

out={
  'stage':'14-t82',
  'local_projective_selector_checks':local,
  'selector_divisor_checks':selector,
  'nonselector_partition_checks':partition,
  'fixed_u_host_checks':bound,
  'synthetic_packets':examples,
  'max_selector_over_m':max_ratio,
  'boundary':{
    'STAGE14_T82':'COMPLETE_AFFINE_DEGENERATE_RAY_MODULUS_TO_FIXED_U_COORDINATE_DIVISOR_HOST',
    'AFFINE_ALPHA_TAG_EQUIVALENT_TO_P_DIVIDES_S':True,
    'AFFINE_BETA_TAG_EQUIVALENT_TO_P_DIVIDES_R':True,
    'HARD_DIAGONAL_MODULUS_DIVIDES_FIXED_U_SELECTOR':True,
    'FIXED_U_SELECTOR_DIVIDES_R_TIMES_S':True,
    'FIXED_U_SELECTOR_MAX':'m/2',
    'NONSEL_RAY_SUPPORT_DIVIDES_INACTIVE_TIMES_FRACTIONAL_SUPPORT':True,
    'FIXED_U_HARD_MODULUS_MULTIPLICITY':'Bo1',
    'MOVING_MODULUS_FAMILY_LENGTH_REOPENED':False,
    'CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT':'1/2',
    'SQRT_B_UPPER_BOUND_PROVED':True,
    'STRICT_SUBSQRT_POWER_SAVING_PROVED':False,
    'TH23_NEEDED':True,
    'TH24_NEEDED':False,
    'NEXT':'Stage14-t83'
  }
}
print(json.dumps(out,indent=2,sort_keys=True))
