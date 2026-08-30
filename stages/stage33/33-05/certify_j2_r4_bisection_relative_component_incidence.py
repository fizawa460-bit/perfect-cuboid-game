#!/usr/bin/env python3
"""Exact R4 local component-incidence verifier for the repaired J2 bisection.

Dependency-free. This does not select the marked Brauer coordinate. It computes
only the relative component pattern of the degree-2 bisection on the named
f2/Tr torsor and leaves the primitive NS glue/discriminant assembly open.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CERT = ROOT / "j2-r4-bisection-relative-component-incidence.json"


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


def deriv(a):
    return trim([i*a[i] for i in range(1,len(a))] or [0])


def evalz(a,x):
    acc=0
    for c in reversed(a):
        acc=acc*x+c
    return acc


# Q(sqrt(2)) arithmetic, represented by a+b*sqrt(2).
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
t2=mul(t,t)
one=[1]
r=powp(sub(t2,one),2)
a=powp(add(t2,one),2)
b=scale(mul(t2,r),4)
q=add(add(powp(t,4),scale(t2,-6)),one)

# Load-bearing identities on the named torsor. Multiplying the standard
# d=f2 equation by d gives
# d*N^2=(d U^2+r V^2)(d U^2+4 t^2 V^2).
assert sub(a,add(r,scale(t2,4))) == [0]
assert sub(b,scale(mul(t2,r),4)) == [0]
assert sub(sub(mul(a,a),scale(b,4)),mul(q,q)) == [0]

# I4 fibers: b has a double zero, q is a unit and a is nonzero. Therefore
# y^2=x*(x^2+a*x+b) specializes to y^2=x^2*(x+a), with Tr=(0,0)
# on the singular point.
db=deriv(b)
d2b=deriv(db)
for x,qv in [(0,1),(1,-4),(-1,-4)]:
    assert evalz(b,x)==0 and evalz(db,x)==0 and evalz(d2b,x)!=0
    assert evalz(q,x)==qv and evalz(a,x)!=0

# Infinity chart u=1/t after x=t^4*xbar, y=t^6*ybar.
u=[0,1]
u2=mul(u,u)
a_inf=powp(add(one,u2),2)
b_inf=scale(mul(u2,powp(sub(one,u2),2)),4)
q_inf=add(add(one,scale(u2,-6)),powp(u,4))
assert evalz(b_inf,0)==0
assert evalz(deriv(b_inf),0)==0
assert evalz(deriv(deriv(b_inf)),0)!=0
assert evalz(a_inf,0)==1 and evalz(q_inf,0)==1

# The four q-roots are simple. At q=0, a^2=4b and b!=0, hence the cubic is
# x*(x+a/2)^2. Its singular point is x=-a/2!=0, while Tr has x=0 and is
# smooth on the original irreducible nodal cubic.
roots={
    "r1=1+sqrt(2)":(1,1),
    "r2=-(1+sqrt(2))":(-1,-1),
    "r3=sqrt(2)-1":(-1,1),
    "r4=1-sqrt(2)":(1,-1),
}
dq=deriv(q)
for x in roots.values():
    assert qeval(q,x)==(0,0)
    assert qeval(dq,x)!=(0,0)
    assert qeval(b,x)!=(0,0)
    assert qeval(a,x)!=(0,0)

# f2=(t-r2)/(t-r4): exact horizontal branch divisor of w^2=f2.
def affine_linear_at(x,const_pair):
    return qadd(x,const_pair)

num_const=(1,1)    # t+1+sqrt(2)
den_const=(-1,1)   # t-1+sqrt(2)
r2=roots["r2=-(1+sqrt(2))"]
r4=roots["r4=1-sqrt(2)"]
assert affine_linear_at(r2,num_const)==(0,0)
assert affine_linear_at(r4,den_const)==(0,0)
for name in ("r1=1+sqrt(2)","r3=sqrt(2)-1"):
    x=roots[name]
    assert affine_linear_at(x,num_const)!=(0,0)
    assert affine_linear_at(x,den_const)!=(0,0)
for x in ((0,0),(1,0),(-1,0)):
    assert affine_linear_at(x,num_const)!=(0,0)
    assert affine_linear_at(x,den_const)!=(0,0)
# Both numerator and denominator are monic degree one, so f2 is a unit at infinity.

# Source-lock the repaired Tr-kernel route, never the revoked d=2/T0 route.
r4c=json.loads((ROOT/"j2-r4-tr-kernel-torsor-reduction.json").read_text())
assert r4c["canonical_sha256"]=="a2b13adf8bf186796058baf88de4853a10682577298f4c75f508ddd8a0c4b3ec"
assert r4c["named_repaired_J2_2cover"]["kernel"]=="<Tr>"
assert r4c["named_repaired_J2_2cover"]["bisection_base_double_cover"]=="w^2=f2"
assert r4c["tr_kernel_2isogenous_comparison_surface"]["is_named_J2_torsor"] is False
r3=json.loads((ROOT/"j2-corrected-cv-e2-cocycle.json").read_text())
assert r3["canonical_sha256"]=="8440400fd7eff183830bb16e991a6fb6f253b1774a76384ed2a3dc8adc951312"
assert r3["cv_lemma_4_6"]["xi_rho"]=="Tr"

c=json.loads(CERT.read_text())
assert c["attempt"]==2
assert c["exact_factorization"]["identities"][-1].startswith("d*N^2=")

# Standard Neron/Kodaira specialization: on I4, Tr is an order-2 section
# through the singular point, hence its nonidentity component class is the
# unique order-2 element 2 in Z/4. On I2, Tr is smooth on the original nodal
# cubic, hence it lies on the identity component (class 0 in Z/2).
for f in c["jacobian_fibers"]["I4"]:
    assert f["Tr_on_singular_point"] is True
    assert f["component_group"]=="Z/4" and f["Tr_component_class"]==2
i2=c["jacobian_fibers"]["I2"]
assert i2["Tr_is_smooth"] is True
assert i2["Tr_component_class"]==0 and i2["component_group"]=="Z/2"

# In the standard <Tr>-kernel even-quartic 2-cover the two bisection points
# over sqrt(d) differ by Tr. Thus the label-independent component difference
# is 2 mod 4 on I4 and 0 mod 2 on I2.
bi=c["bisection_component_incidence"]
assert bi["generic_two_points_difference"]=="Tr"
assert bi["I4_relative_pattern"]["component_difference_mod_4"]==2
assert bi["I4_relative_pattern"]["canonical_pair_up_to_rotation"]==[0,2]
assert bi["I2_relative_pattern"]["all_q_root_fibers_component_difference_mod_2"]==0
assert bi["I2_relative_pattern"]["ramified_roots"]==["r2=-(1+sqrt(2))","r4=1-sqrt(2)"]
assert bi["I2_relative_pattern"]["unramified_roots"]==["r1=1+sqrt(2)","r3=sqrt(2)-1"]

lat=c["lattice_reduction"]
assert lat["candidate_minimum_norms"]==[4,8,12]
assert lat["candidate_set_reduced"] is False
assert lat["minimum_norm_selected"] is False
assert lat["marked_brauer_coordinate_selected"] is False
assert c["firewalls"]["E2_basis_bits_equal_marked_brauer_bits"] is False
assert c["firewalls"]["stage33_05_reclosed"] is False
assert c["firewalls"]["stage33_12_closed_exact"] is False
assert c["firewalls"]["stage33_13_released"] is False

d=dict(c)
got=d.pop("canonical_sha256")
canonical=json.dumps(d,sort_keys=True,separators=(",",":")).encode()
assert got==hashlib.sha256(canonical).hexdigest()
print(json.dumps({
    "success":True,
    "status":c["status"],
    "canonical_sha256":got,
    "I4_component_difference":2,
    "I2_component_difference":0,
    "candidate_minimum_norms":[4,8,12],
    "next_exact_leaf":c["next_exact_leaf"],
},indent=2,sort_keys=True))
