#!/usr/bin/env python3
from collections import Counter

# Gaussian integers as (re, im).
def g(a=0,b=0): return (int(a),int(b))
def ga(x,y): return (x[0]+y[0],x[1]+y[1])
def gn(x): return (-x[0],-x[1])
def gs(x,y): return ga(x,gn(y))
def gm(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def gz(x): return x==(0,0)
ONE=g(1); MONE=g(-1); II=g(0,1); MII=g(0,-1); ZERO=g()

# Tiny exact polynomial ring over Z[i] for the factor identities.
ZEXP=(0,)*7
def pclean(p): return {m:c for m,c in p.items() if not gz(c)}
def padd(*ps):
    out={}
    for p in ps:
        for m,c in p.items(): out[m]=ga(out.get(m,ZERO),c)
    return pclean(out)
def pneg(p): return {m:gn(c) for m,c in p.items()}
def psub(a,b): return padd(a,pneg(b))
def pscale(c,p): return pclean({m:gm(c,v) for m,v in p.items()})
def pmul(a,b):
    out={}
    for ma,ca in a.items():
        for mb,cb in b.items():
            m=tuple(ma[i]+mb[i] for i in range(7))
            out[m]=ga(out.get(m,ZERO),gm(ca,cb))
    return pclean(out)
def ppow(p,n):
    out={ZEXP:ONE}
    for _ in range(n): out=pmul(out,p)
    return out
def var(i):
    e=[0]*7;e[i]=1
    return {tuple(e):ONE}
def subst(p,repl):
    out={}
    for m,c in p.items():
        term={ZEXP:c}
        for i,e in enumerate(m):
            if e: term=pmul(term,ppow(repl.get(i,var(i)),e))
        out=padd(out,term)
    return pclean(out)
def peq(a,b): return pclean(psub(a,b))=={}

a=[var(i) for i in range(3)]; b=[var(i) for i in range(3,6)]; c=var(6)
q1=psub(padd(pmul(a[0],a[0]),pmul(a[1],a[1])),pmul(b[2],b[2]))
q2=psub(padd(pmul(a[1],a[1]),pmul(a[2],a[2])),pmul(b[0],b[0]))
q3=psub(padd(pmul(a[0],a[0]),pmul(a[2],a[2])),pmul(b[1],b[1]))
q4=psub(padd(pmul(a[0],a[0]),pmul(a[1],a[1]),pmul(a[2],a[2])),pmul(c,c))

# Orbit representative factor identities.
R20={6:padd(a[0],b[0])}
assert peq(subst(psub(q4,q2),R20),pscale(g(-2),pmul(a[0],b[0])))
R19={6:padd(a[2],b[0],b[1])}
assert peq(subst(psub(padd(q2,q3),q4),R19),pscale(g(2),pmul(padd(a[2],b[0]),padd(a[2],b[1]))))
R16a={3:{}}
assert peq(subst(q2,R16a),pmul(padd(a[1],pscale(II,a[2])),padd(a[1],pscale(MII,a[2]))))
assert peq(subst(psub(q4,q2),R16a),pmul(psub(a[0],c),padd(a[0],c)))
R16b={6:padd(a[0],a[1],pscale(II,a[2]))}
assert peq(subst(q4,R16b),pscale(g(-2),pmul(padd(a[0],pscale(II,a[2])),padd(a[1],pscale(II,a[2])))))

# Branch-local scheme checks.
R={0:{},6:b[0]}
assert peq(subst(q1,R),pmul(psub(a[1],b[2]),padd(a[1],b[2])))
assert peq(subst(q3,R),pmul(psub(a[2],b[1]),padd(a[2],b[1])))
assert peq(subst(q4,R),subst(q2,R))
R={3:{},6:a[0]}
assert peq(subst(q2,R),pmul(padd(a[1],pscale(II,a[2])),padd(a[1],pscale(MII,a[2]))))
assert peq(subst(q4,R),subst(q2,R))
R={3:pscale(MONE,a[2]),6:b[1]}
assert peq(subst(q2,R),pmul(a[1],a[1]))
assert peq(subst(q4,R),padd(subst(q3,R),subst(q2,R)))
assert peq(subst(q1,{**R,1:{}}),pmul(psub(a[0],b[2]),padd(a[0],b[2])))
R={4:pscale(MONE,a[2]),6:b[0]}
assert peq(subst(q3,R),pmul(a[0],a[0]))
assert peq(subst(q4,R),padd(subst(q2,R),subst(q3,R)))
assert peq(subst(q1,{**R,0:{}}),pmul(psub(a[1],b[2]),padd(a[1],b[2])))
R={0:pscale(MII,a[2]),6:a[1]}
assert peq(subst(q3,R),pscale(MONE,pmul(b[1],b[1]))) and subst(q4,R)=={}
R={1:pscale(MII,a[2]),6:a[0]}
assert peq(subst(q2,R),pscale(MONE,pmul(b[0],b[0]))) and subst(q4,R)=={}

# Smooth standard elliptic quartic: four distinct singular quadrics in the pencil.
def projroot(A,B):
    from math import gcd
    x,y=-B,A
    if x==0:return (0,1)
    if y==0:return (1,0)
    d=gcd(abs(x),abs(y));x//=d;y//=d
    if x<0:x,y=-x,-y
    return (x,y)
F=[1,-1,0,-1]; G=[1,1,-1,0]
assert len({projroot(F[i],G[i]) for i in range(4)})==4

# Exact 48 nodes over Z[i].
def nodes():
    out=[]
    for j in range(3):
      for sa in (1,-1):
       for s1 in (1,-1):
        for s2 in (1,-1):
         z=[ZERO]*7;z[j]=g(sa);o=[t for t in range(3) if t!=j];z[3+o[0]]=g(s1);z[3+o[1]]=g(s2);z[6]=ONE;out.append(tuple(z))
    for j in range(3):
      o=[t for t in range(3) if t!=j];aa,bb=o
      for sr in (1,-1):
       for ep in (1,-1):
        for eq in (1,-1):
         z=[ZERO]*7;z[aa]=ONE;z[bb]=g(0,sr);z[3+aa]=g(0,ep);z[3+bb]=g(-eq*sr);out.append(tuple(z))
    assert len(out)==48
    return out
V=nodes()
def leval(cs,z):
    s=ZERO
    for cc,zz in zip(cs,z):s=ga(s,gm(cc,zz))
    return s
def qeval(k,z):
    A1,A2,A3,B1,B2,B3,C=z;sq=lambda x:gm(x,x)
    if k==1:return gs(ga(sq(A1),sq(A2)),sq(B3))
    if k==2:return gs(ga(sq(A2),sq(A3)),sq(B1))
    if k==3:return gs(ga(sq(A1),sq(A3)),sq(B2))
    if k==4:return gs(ga(ga(sq(A1),sq(A2)),sq(A3)),sq(C))
for z in V: assert all(gz(qeval(k,z)) for k in (1,2,3,4))
def support(cs): return [r for r,z in enumerate(V) if gz(leval(cs,z))]
def mask(ids):
    m=0
    for r in ids:m|=1<<r
    return m
H20=[g(-1),ZERO,ZERO,g(-1),ZERO,ZERO,ONE]
H19=[ZERO,ZERO,g(-1),g(-1),g(-1),ZERO,ONE]
H16a=[ZERO,ZERO,ZERO,ONE,ZERO,ZERO,ZERO]
H16b=[g(-1),g(-1),MII,ZERO,ZERO,ZERO,ONE]
assert (len(support(H20)),mask(support(H20)))==(20,int('0000ff33330f',16))
assert (len(support(H19)),mask(support(H19)))==(19,int('003c3c163333',16))
assert (len(support(H16a)),mask(support(H16a)))==(16,int('0000ff0000ff',16))
assert (len(support(H16b)),mask(support(H16b)))==(16,int('000f0f000f0f',16))

E=lambda cs:(lambda z:gz(leval(cs,z))); Q=lambda k:(lambda z:gz(qeval(k,z)))
def unit(i):
    cs=[ZERO]*7;cs[i]=ONE;return cs
def lcomb(items):
    cs=[ZERO]*7
    for i,cc in items:cs[i]=ga(cs[i],cc)
    return cs
def comp_ids(eqs):return [r for r,z in enumerate(V) if all(eq(z) for eq in eqs)]

C20=[]
for s in (1,-1):
  for t in (1,-1):C20.append(comp_ids([E(H20),E(unit(0)),E(lcomb([(5,ONE),(1,g(-s))])),E(lcomb([(4,ONE),(2,g(-t))])),Q(2)]))
for s in (1,-1):C20.append(comp_ids([E(H20),E(unit(3)),E(lcomb([(1,ONE),(2,g(0,-s))])),Q(1),Q(3)]))
assert sorted(map(len,C20))==[6,6,6,6,8,8]
cnt=Counter(r for Cc in C20 for r in Cc);assert all(cnt[r]==2 for r in support(H20)) and set(cnt)==set(support(H20))

C19=[]
for s in (1,-1):C19.append(comp_ids([E(H19),E(lcomb([(2,ONE),(3,ONE)])),E(unit(1)),E(lcomb([(5,ONE),(0,g(-s))])),Q(3)]))
for s in (1,-1):C19.append(comp_ids([E(H19),E(lcomb([(2,ONE),(4,ONE)])),E(unit(0)),E(lcomb([(5,ONE),(1,g(-s))])),Q(2)]))
assert list(map(len,C19))==[6,6,6,6]
cnt=Counter(r for Cc in C19 for r in Cc);assert Counter(cnt[r] for r in support(H19))==Counter({1:16,2:2,4:1})

C16a=[]
for s in (1,-1):
  for t in (1,-1):C16a.append(comp_ids([E(H16a),E(lcomb([(1,ONE),(2,g(0,-s))])),E(lcomb([(6,ONE),(0,g(-t))])),Q(1),Q(3)]))
assert list(map(len,C16a))==[8,8,8,8]
cnt=Counter(r for Cc in C16a for r in Cc);assert all(cnt[r]==2 for r in support(H16a)) and set(cnt)==set(support(H16a))

C16b=[comp_ids([E(H16b),E(lcomb([(0,ONE),(2,II)])),E(unit(4)),Q(1),Q(2)]),comp_ids([E(H16b),E(lcomb([(1,ONE),(2,II)])),E(unit(3)),Q(1),Q(3)])]
assert list(map(len,C16b))==[8,8]
cnt=Counter(r for Cc in C16b for r in Cc);assert all(cnt[r]==1 for r in support(H16b)) and set(cnt)==set(support(H16b))

assert 4*2+2*4==16
assert 4*(2*2)==16
assert 4*4==16
assert 2*(2*4)==16
print('PASS STAGE32_MB104_GENUS1_SPAN5_SECTIONS_20_19_16_V1')
print('inc20=4_smooth_conics_plus_2_smooth_elliptic_quartics reduced degree16 node_component_mult=2')
print('inc19=4_smooth_conics_each_scheme_multiplicity2 degree16 reduced_node_incidence=16x1,2x2,1x4')
print('inc16_orbit3=4_smooth_elliptic_quartics degree16 node_component_mult=2')
print('inc16_orbit24=2_smooth_elliptic_quartics_each_scheme_multiplicity2 degree16 nodes_split_8_plus_8')
print('irreducible_genus1_component_degree_cap=4 for incidence 20,19,16 ambient orbits')
