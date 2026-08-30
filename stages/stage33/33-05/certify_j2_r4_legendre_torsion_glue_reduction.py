#!/usr/bin/env python3
"""Exact R4 Legendre/torsion-glue reduction for repaired J2.

Dependency-free. This proves a new structural reduction only: the relative
reducible-fiber component vector is already explained by rational 4-torsion
primitive glue, so the marked Brauer coordinate still requires horizontal
f2 ramification / monodromy (or an equivalent B-field/frame adapter).
"""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CERT=ROOT/"j2-r4-legendre-torsion-glue-reduction.json"

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b))
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)])

def scale(a,c):
    return trim([c*x for x in a])

def sub(a,b):
    return add(a,scale(b,-1))

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return trim(out)

def powp(a,n):
    out=[1]
    for _ in range(n):
        out=mul(out,a)
    return out

# Q(sqrt(2)): a+b*sqrt(2)
def qadd(x,y):
    return (x[0]+y[0],x[1]+y[1])

def qmul(x,y):
    return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])

def qeval(p,x):
    acc=(0,0)
    for c in reversed(p):
        acc=qadd(qmul(acc,x),(c,0))
    return acc

t=[0,1]
one=[1]
t2=mul(t,t)
A=sub(t2,one)
B=scale(t,2)
C=add(t2,one)
A2=mul(A,A)
B2=mul(B,B)
AB=mul(A,B)
a=add(A2,B2)
b=mul(A2,B2)
q=sub(A2,B2)
Dplus=sub(A,B)
Dminus=add(A,B)

assert sub(add(A2,B2),mul(C,C)) == [0]
assert sub(q,mul(Dplus,Dminus)) == [0]
assert sub(b,mul(AB,AB)) == [0]

# E: y^2=x*(x+A^2)*(x+B^2).
def curve_rhs(x):
    return mul(mul(x,add(x,A2)),add(x,B2))

xp=AB
yp=mul(AB,Dminus)
xm=scale(AB,-1)
ym=mul(AB,Dplus)
assert sub(mul(yp,yp),curve_rhs(xp)) == [0]
assert sub(mul(ym,ym),curve_rhs(xm)) == [0]

# Doubling on y^2=x^3+a*x^2+b*x:
# m=(3x^2+2ax+b)/(2y), x(2P)=m^2-a-2x.
# At Pplus, m=A+B; at Pminus, m=-(A-B). Verify without division.
num_p=add(add(scale(mul(xp,xp),3),scale(mul(a,xp),2)),b)
den_p=scale(yp,2)
assert sub(num_p,mul(den_p,Dminus)) == [0]
x2p=sub(sub(mul(Dminus,Dminus),a),scale(xp,2))
assert x2p == [0]
assert sub(scale(yp,-1),scale(mul(Dminus,xp),-1)) == [0]

minus_Dplus=scale(Dplus,-1)
num_m=add(add(scale(mul(xm,xm),3),scale(mul(a,xm),2)),b)
den_m=scale(ym,2)
assert sub(num_m,mul(den_m,minus_Dplus)) == [0]
x2m=sub(sub(mul(Dplus,Dplus),a),scale(xm,2))
assert x2m == [0]
assert add(scale(ym,-1),mul(minus_Dplus,xm)) == [0]
assert yp != [0] and ym != [0]

# Legendre parameter lambda=B^2/A^2. The deck symmetries -t and 1/t
# preserve lambda; verify by exact cross-multiplication.
B2_minus=mul(scale(t,-2),scale(t,-2))
A2_minus=powp(sub(mul(scale(t,-1),scale(t,-1)),one),2)
assert B2_minus==B2 and A2_minus==A2
u=[0,1]
u2=mul(u,u)
lhs_num=scale(u2,4)
lhs_den=powp(sub(one,u2),2)
rhs_num=scale(u2,4)
rhs_den=powp(sub(u2,one),2)
assert mul(lhs_num,rhs_den)==mul(rhs_num,lhs_den)

roots={
    "r1":(1,1),
    "r2":(-1,-1),
    "r3":(-1,1),
    "r4":(1,-1),
}
for x in roots.values():
    assert qeval(q,x)==(0,0)
assert qeval(Dplus,roots["r1"])==(0,0)
assert qeval(Dplus,roots["r4"])==(0,0)
assert qeval(Dminus,roots["r2"])==(0,0)
assert qeval(Dminus,roots["r3"])==(0,0)

# f2=(t-r2)/(t-r4). Verify the exact cross-factor companion identity
# f2*(A-B)/(A+B)=(t-r1)/(t-r3).
def lin(root):
    return [(-root[0],-root[1]),(1,0)]

def qpoly_mul(p,r):
    out=[(0,0)]*(len(p)+len(r)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(r):
            out[i+j]=qadd(out[i+j],qmul(x,y))
    while len(out)>1 and out[-1]==(0,0):
        out.pop()
    return out

def intpoly_to_q(p):
    return [(c,0) for c in p]

assert qpoly_mul(lin(roots["r1"]),lin(roots["r4"]))==intpoly_to_q(Dplus)
assert qpoly_mul(lin(roots["r2"]),lin(roots["r3"]))==intpoly_to_q(Dminus)
left=qpoly_mul(lin(roots["r2"]),intpoly_to_q(Dplus))
left=qpoly_mul(left,lin(roots["r3"]))
right=qpoly_mul(lin(roots["r1"]),intpoly_to_q(Dminus))
right=qpoly_mul(right,lin(roots["r4"]))
assert left==right

# At q=0 the singular x-coordinate is -A^2=-B^2. Pplus has x=AB:
# it is singular iff A=-B (Dminus=0), smooth iff A=B (Dplus=0).
for name in ("r2","r3"):
    x=roots[name]
    assert qeval(Dminus,x)==(0,0)
    assert qeval(add(AB,A2),x)==(0,0)
for name in ("r1","r4"):
    x=roots[name]
    assert qeval(Dplus,x)==(0,0)
    assert qeval(add(AB,A2),x)!=(0,0)

# Source-lock repaired inputs.
r3=json.loads((ROOT/"j2-corrected-cv-e2-cocycle.json").read_text())
assert r3["canonical_sha256"]=="8440400fd7eff183830bb16e991a6fb6f253b1774a76384ed2a3dc8adc951312"
assert r3["cv_lemma_4_6"]["xi_rho"]=="Tr"
r4=json.loads((ROOT/"j2-r4-tr-kernel-torsor-reduction.json").read_text())
assert r4["canonical_sha256"]=="a2b13adf8bf186796058baf88de4853a10682577298f4c75f508ddd8a0c4b3ec"
assert r4["named_repaired_J2_2cover"]["kernel"]=="<Tr>"
inc=json.loads((ROOT/"j2-r4-bisection-relative-component-incidence.json").read_text())
assert inc["canonical_sha256"]=="bae1bd41d89a994b87ad7649547d5045808ff28653df319fd6bbad470e758735"
assert inc["bisection_component_incidence"]["I4_relative_pattern"]["component_difference_mod_4"]==2
assert inc["bisection_component_incidence"]["I2_relative_pattern"]["all_q_root_fibers_component_difference_mod_2"]==0

c=json.loads(CERT.read_text())
assert c["attempt"]==3
assert c["rational_4torsion_halves_of_Tr"]["Pplus"]["double"]=="Tr"
assert c["rational_4torsion_halves_of_Tr"]["order4_exact"] is True
assert c["primitive_torsion_glue_reduction"]["component_only_route_can_select_marked_brauer_coordinate"] is False
assert c["f2_horizontal_character"]["ramified_q_roots"]==["r2","r4"]
assert c["f2_horizontal_character"]["ramification_meets_one_Pplus_singular_and_one_Pplus_smooth_I2"] is True
assert c["lattice_reduction"]["candidate_minimum_norms"]==[4,8,12]
assert c["lattice_reduction"]["candidate_set_reduced"] is False
assert c["lattice_reduction"]["minimum_norm_selected"] is False
assert c["lattice_reduction"]["marked_brauer_coordinate_selected"] is False

cy=c["cycle_protocol"]
assert cy["CYCLE_ROUTE_STATUS"]=="BLOCKED_NEW_PATTERN_ISOLATED"
assert cy["CYCLE_EXHAUSTIVE_VIEW_AUDIT"] is True
assert cy["CYCLE_BLIND_REDISCOVERY"] is True
assert cy["CYCLE_SPLIT_TRIGGERED"] is False
assert sum(x["status"]=="LIVE" for x in cy["candidate_ledger"])==2
assert sum(x["status"]=="UNTESTED" for x in cy["candidate_ledger"])==3
assert next(x for x in cy["candidate_ledger"] if x["route"]=="RELATIVE_COMPONENT_INCIDENCE_ALONE")["status"]=="BLOCKED"

for key in (
    "E2_basis_bits_equal_marked_brauer_bits",
    "Q_defined_descent_credit_restored",
    "comparison_2isogenous_curve_is_named_torsor",
    "class3_promoted",
    "stage33_05_reclosed",
    "stage33_12_closed_exact",
    "stage33_13_released",
    "theorem_credit",
    "receiver_credit",
    "endpoint_credit",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert c["firewalls"][key] is False

d=dict(c)
got=d.pop("canonical_sha256")
canonical=json.dumps(d,sort_keys=True,separators=(",",":")).encode()
assert got==hashlib.sha256(canonical).hexdigest()

print(json.dumps({
    "success":True,
    "status":c["status"],
    "canonical_sha256":got,
    "Tr_rationally_2_divisible":True,
    "component_only_route":"BLOCKED_BY_TORSION_PRIMITIVE_GLUE",
    "candidate_minimum_norms":[4,8,12],
    "next_exact_leaf":c["next_exact_leaf"],
},indent=2,sort_keys=True))
