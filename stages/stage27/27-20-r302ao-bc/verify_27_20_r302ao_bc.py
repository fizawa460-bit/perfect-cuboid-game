#!/usr/bin/env python3
import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
S27 = ROOT / "stages" / "stage27"

def read(path): return path.read_text(encoding="utf-8")
def req(text, marker): assert marker in text, f"missing marker: {marker}"
def divisors(n):
    out=[]
    for d in range(1,int(math.isqrt(n))+1):
        if n%d==0:
            out.append(d)
            if d*d!=n: out.append(n//d)
    return sorted(out)
def mobius(n):
    if n==1:return 1
    p=2; sign=1; x=n
    while p*p<=x:
        if x%p==0:
            x//=p; sign=-sign
            if x%p==0:return 0
            while x%p==0:x//=p
        p+=1
    if x>1:sign=-sign
    return sign
def ramanujan_sum(q,n): return sum(d*mobius(q//d) for d in divisors(math.gcd(q,n)))
def valuation_capped(n,p,cap):
    if n==0:return cap
    n=abs(n); v=0
    while v<cap and n%p==0:n//=p; v+=1
    return v
def factorization(n):
    out=[]; p=2; x=n
    while p*p<=x:
        if x%p==0:
            k=0
            while x%p==0:x//=p;k+=1
            out.append((p,k))
        p+=1
    if x>1:out.append((x,1))
    return out
def s_factor(C,q):
    ans=1
    for p,k in factorization(q):
        v=valuation_capped(C,p,k); ans*=p**min(k//2,v//2)
    return ans
def omega_odd(q): return sum(1 for p,_ in factorization(q) if p!=2)
def roots(C,q): return [x for x in range(q) if (x*x-C)%q==0]

parent=read(S27/"27-20-r302an"/"result.md"); req(parent,"NEXT_DERIVED_ROUTE=27-20-r302ao")
chain=["ao","ap","aq","ar","as","at","au","av","aw","ax","ay","az","ba","bb"]
for suffix in chain:
    text=read(S27/f"27-20-r302{suffix}"/"result.md")
    req(text,"CHECKPOINT=40"); req(text,"STRICT_SUB_SQRT_UPPER_PROVED=false")
bc=read(S27/"27-20-r302bc"/"result.md")
for marker in ["CHECKPOINT=40","STRICT_SUB_SQRT_UPPER_PROVED=false","FULL_ADDITIVE_FREQUENCY_RECOMBINATION_COMPLETE=true","ONE_WEIGHTED_FIXED_POWER_THEOREM_SUFFICIENT=true","SINGULARITY_WEIGHTED_RESIDUE_FOURTH_MOMENT_DEFICIT_PROVED=false","ADVANCE_TO_CHECKPOINT50=false","FREEZE_FOR_STRUCTURE_RADAR=true","NEXT_DERIVED_ROUTE=NONE_THEOREM_GATE_PAUSED","MERGE_ALLOWED=true"]: req(bc,marker)
reg=json.loads(read(S27/"27-20-r302ao-bc"/"batch-registry.json"))
assert reg["audit_status"]=="PASS_WITH_FREEZE_REPAIR"
assert reg["merge_allowed"] is True
assert reg["advance_allowed"] is False
assert reg["freeze_for_structure_radar"] is True
assert reg["next_derived_route"] is None
assert reg["claims"]["full_gcd_stratum_frequency_flat_diagonal_justified"] is False
assert reg["claims"]["full_gcd_stratum_ramanujan_recombination_proved"] is True
assert reg["claims"]["all_strata_root_projector_recombination_proved"] is True
assert reg["claims"]["generic_all_coefficient_local_fixed_power_contraction"] is False
assert reg["claims"]["singularity_weighted_residue_fourth_moment_deficit_proved"] is False

for q in range(1,49):
    for C in range(q):
        for f in range(q):
            n=f*f-C
            total=sum(ramanujan_sum(Q,n) for Q in divisors(q))
            assert total==(q if n%q==0 else 0)
            for d in divisors(q):
                Q=q//d
                direct=sum(cmath.exp(2j*math.pi*a*n/q) for a in range(q) if math.gcd(a,q)==d)
                assert abs(direct-ramanujan_sum(Q,n))<1e-8
for q in range(1,129):
    for C in range(q):
        R=len(roots(C,q)); bound=4*(2**omega_odd(q))*s_factor(C,q)
        assert R<=bound,(q,C,R,bound)
        if math.gcd(C,q)==1: assert s_factor(C,q)==1
for q in range(2,25):
    W=[complex((3*f+1)%5-2,(2*f+3)%3-1) for f in range(q)]
    E=sum(abs(w)**2 for w in W)
    if E==0: continue
    Lambda=sum(abs(w)**4 for w in W)/(E*E)
    nu=[abs(w)**2 for w in W]
    nuhat=[sum(nu[f]*cmath.exp(-2j*math.pi*h*f/q) for f in range(q)) for h in range(q)]
    assert abs(Lambda-sum(abs(z)**2 for z in nuhat)/(q*E*E))<1e-8
    for C in range(q):
        rr=roots(C,q); R=len(rr); Eroot=sum(abs(W[f])**2 for f in rr)
        lhs=R*Eroot/E; rhs=(R**1.5)*math.sqrt(Lambda) if R else 0.0
        assert lhs<=rhs+1e-8
print("Stage27-20-r302ao-bc verification: PASS (audited theorem-gate freeze)")
