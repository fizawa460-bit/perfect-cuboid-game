#!/usr/bin/env python3

def compose(a,b):
    return tuple(a[b[i]] for i in range(len(a)))

def ident(n):
    return tuple(range(n))

def inv_from_pairs(n,pairs):
    p=list(range(n))
    used=set()
    for a,b in pairs:
        assert a not in used and b not in used and a!=b
        used.add(a); used.add(b)
        p[a]=b; p[b]=a
    return tuple(p)

def transposition_count(p):
    seen=set(); c=0
    for i,j in enumerate(p):
        if i in seen: continue
        if j==i:
            seen.add(i)
        else:
            assert p[j]==i
            seen.add(i); seen.add(j); c+=1
    return c

def orbit_size(gs):
    seen={0}; todo=[0]
    for x in todo:
        for g in gs:
            y=g[x]
            if y not in seen:
                seen.add(y); todo.append(y)
    return len(seen)

def cycle_matching(base_pairs):
    # base_pairs are ordered two-vertex components (u_j,v_j).
    m=len(base_pairs)
    return [(base_pairs[j][1],base_pairs[(j+1)%m][0]) for j in range(m)]

def factor1(l):
    n=56*l
    p1=[(2*j,2*j+1) for j in range(12*l)]
    off=24*l
    p2=[(off+2*j,off+2*j+1) for j in range(16*l)]
    s1=inv_from_pairs(n,p1)
    s2=inv_from_pairs(n,p2)
    s3=ident(n)
    base=p1+p2
    T=inv_from_pairs(n,cycle_matching(base))
    s4=s5=T
    s6=compose(s1,s2)
    return [s1,s2,s3,s4,s5,s6]

def factor2(l):
    n=56*l
    p3=[(2*j,2*j+1) for j in range(16*l)]
    off=32*l
    p4=[(off+2*j,off+2*j+1) for j in range(12*l)]
    t1=ident(n)
    t3=inv_from_pairs(n,p3)
    t4=inv_from_pairs(n,p4)
    t2=compose(t3,t4)
    base=p3+p4
    T=inv_from_pairs(n,cycle_matching(base))
    t5=t6=T
    return [t1,t2,t3,t4,t5,t6]

def check(gs,expected,l):
    n=56*l
    assert [transposition_count(g) for g in gs]==[x*l for x in expected]
    p=ident(n)
    for g in gs:
        p=compose(p,g)
    assert p==ident(n)
    assert orbit_size(gs)==n
    assert sum(transposition_count(g) for g in gs)==112*l

for l in range(1,33):
    check(factor1(l),[12,16,0,28,28,28],l)
    check(factor2(l),[0,28,16,12,28,28],l)

print("PASS: 000707 e=4 individual six-value passports are Hurwitz-feasible")
print("verified explicit all-l construction pattern for l=1..32")
print("factor1 r=(12,16,0,28,28,28)l")
print("factor2 r=(0,28,16,12,28,28)l")
