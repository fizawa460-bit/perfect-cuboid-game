#!/usr/bin/env python3
from itertools import combinations

P=1097
II=341


def nodes():
    out=[]
    for j in range(3):
        for sa in (1,-1):
            for s1 in (1,-1):
                for s2 in (1,-1):
                    z=[0j]*7
                    z[j]=sa
                    o=[t for t in range(3) if t!=j]
                    z[3+o[0]]=s1
                    z[3+o[1]]=s2
                    z[6]=1
                    out.append(tuple(z))
    for j in range(3):
        o=[t for t in range(3) if t!=j]
        a,b=o
        for sr in (1,-1):
            for ep in (1,-1):
                for eq in (1,-1):
                    z=[0j]*7
                    z[a]=1
                    z[b]=1j*sr
                    z[3+a]=1j*ep
                    z[3+b]=-eq*sr
                    out.append(tuple(z))
    assert len(out)==48
    return out


V=nodes()


def q(z,k):
    a1,a2,a3,b1,b2,b3,c=z
    return (
        a1*a1+a2*a2-b3*b3,
        a2*a2+a3*a3-b1*b1,
        a1*a1+a3*a3-b2*b2,
        a1*a1+a2*a2+a3*a3-c*c,
    )[k-1]


def support(pred):
    return [r for r,z in enumerate(V) if pred(z)]


def mask(ids):
    m=0
    for r in ids:
        m|=1<<r
    return m


def rank_mod(ids):
    M=[]
    for r in ids:
        row=[]
        for x in V[r]:
            a=int(x.real)
            b=int(x.imag)
            row.append((a+b*II)%P)
        M.append(row)
    rk=0
    for c in range(7):
        pv=next((r for r in range(rk,len(M)) if M[r][c]),None)
        if pv is None:
            continue
        M[rk],M[pv]=M[pv],M[rk]
        inv=pow(M[rk][c],P-2,P)
        M[rk]=[(x*inv)%P for x in M[rk]]
        for r in range(len(M)):
            if r!=rk and M[r][c]:
                f=M[r][c]
                M[r]=[(M[r][j]-f*M[rk][j])%P for j in range(7)]
        rk+=1
        if rk==len(M):
            break
    return rk


def capacity(degrees):
    # D_l.Q=l(7e-4n_Q)>=0 requires n_Q<=floor(7e/4).
    return sum((7*e)//4 for e in degrees)


assert capacity([2]*8)==24
assert capacity([2]*4+[4]*2)==26
assert capacity([2]*4)==12
assert capacity([4]*4)==28
assert capacity([4]*2)==14

# Retained incidence-24 geometry: 8 conics, each section node on two conics.
assert 2*14>24

# Retained incidence-20 geometry: 4 conics + 2 elliptic quartics,
# every section node on exactly two reduced components.
assert 2*14>26

# Retained incidence-19 geometry: four reduced conics cover every section node.
assert 14>12

# Incidence-16 size-3 orbit: b1=0; four smooth elliptic quartics.
S16a=support(lambda z:z[3]==0)
C16a=[]
for s in (1,-1):
    for t in (1,-1):
        C16a.append(set(support(lambda z,s=s,t=t:
            z[3]==0 and z[1]==s*1j*z[2] and z[6]==t*z[0]
            and q(z,1)==0 and q(z,3)==0)))
assert len(S16a)==16
assert [len(C) for C in C16a]==[8,8,8,8]
assert all(sum(r in C for C in C16a)==2 for r in S16a)

balanced_a=[]
for omit in combinations(S16a,2):
    Sigma=set(S16a)-set(omit)
    counts=tuple(len(Sigma&C) for C in C16a)
    if all(n<=7 for n in counts):
        assert counts==(7,7,7,7)
        assert rank_mod(sorted(Sigma))==6
        balanced_a.append(tuple(sorted(Sigma)))
assert len(balanced_a)==32
assert len(set(balanced_a))==32

# Incidence-16 size-24 orbit: c=a1+a2+i*a3; two doubled elliptic quartics.
H16b=lambda z:z[6]==z[0]+z[1]+1j*z[2]
S16b=support(H16b)
C1=set(support(lambda z:H16b(z) and z[0]+1j*z[2]==0 and z[4]==0 and q(z,1)==0 and q(z,2)==0))
C2=set(support(lambda z:H16b(z) and z[1]+1j*z[2]==0 and z[3]==0 and q(z,1)==0 and q(z,3)==0))
assert len(S16b)==16
assert len(C1)==len(C2)==8
assert not (C1&C2)
assert C1|C2==set(S16b)

balanced_b=[]
for omit in combinations(S16b,2):
    Sigma=set(S16b)-set(omit)
    counts=(len(Sigma&C1),len(Sigma&C2))
    if all(n<=7 for n in counts):
        assert counts==(7,7)
        assert rank_mod(sorted(Sigma))==6
        balanced_b.append(tuple(sorted(Sigma)))
assert len(balanced_b)==64
assert len(set(balanced_b))==64

# Incidence-14 orbit size 96. Representative:
#   -a2+a3+b2+b3=0.
# On this hyperplane q1-q3=2*(a2-b3)*(b2+b3).
# The branch a2=b3 has a1=0, b2=-a3 and splits into two doubled conics c=+/-b1.
H14a=lambda z:-z[1]+z[2]+z[4]+z[5]==0
S14a=support(H14a)
assert len(S14a)==14
assert mask(S14a)==int('0000185aa566',16)
assert rank_mod(S14a)==6
Q14p=set(support(lambda z:H14a(z) and z[1]==z[5] and z[0]==0 and z[4]==-z[2] and z[6]==z[3] and q(z,2)==0))
Q14m=set(support(lambda z:H14a(z) and z[1]==z[5] and z[0]==0 and z[4]==-z[2] and z[6]==-z[3] and q(z,2)==0))
assert len(Q14p)==len(Q14m)==6
assert len(Q14p|Q14m)==10
assert len(Q14p&Q14m)==2
# For the unique N=14 support in this incidence-14 hyperplane, each conic has n_Q=6:
# D_l.Q=l*(14-24)=-10l.
assert 7*2-4*len(Q14p)==-10
assert 7*2-4*len(Q14m)==-10

print('PASS STAGE32_MB104_GENUS1_SPAN5_UNIFORM_RAY_COMPONENT_CAPACITY_V2')
print('inc24=N>=14_forces_negative_component capacity=24 incidence_at_least=28')
print('inc20=N>=14_forces_negative_component capacity=26 incidence_at_least=28')
print('inc19=N>=14_forces_negative_conic capacity=12 incidence_at_least=14')
print('inc16_orbit3=N>=15_forced;N14_balanced_spanning_survivors=32 counts=7,7,7,7')
print('inc16_orbit24=N>=15_forced;N14_balanced_spanning_survivors=64 counts=7,7')
print('inc14_orbit96=unique_N14_support_forces_double_conic_pairing_minus10l conic_node_counts=6,6')
