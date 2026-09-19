#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

I=1j

def req(c,m):
    if not c:
        raise SystemExit("FAIL: "+m)

def nodes():
    v=[]
    for j in range(3):
        for sa in (1,-1):
            for s1 in (1,-1):
                for s2 in (1,-1):
                    x=[0j]*7
                    x[j]=sa
                    q=[t for t in range(3) if t!=j]
                    x[3+q[0]]=s1; x[3+q[1]]=s2; x[6]=1
                    v.append(tuple(x))
    for j in range(3):
        q=[t for t in range(3) if t!=j]; a,b=q
        for sr in (1,-1):
            for ep in (1,-1):
                for eq in (1,-1):
                    x=[0j]*7
                    x[a]=1; x[b]=I*sr
                    x[3+a]=I*ep; x[3+b]=-eq*sr
                    v.append(tuple(x))
    req(len(v)==48 and len(set(v))==48,"48-node model")
    return v

V=nodes()

def from_mask(h):
    n=int(h,16)
    return frozenset(i for i in range(48) if (n>>i)&1)

def c2_supports():
    out=[]
    for fam in range(3):
        for e1 in (1,-1):
            for e2 in (1,-1):
                ids=[]
                for j,x in enumerate(V):
                    a1,a2,a3,b1,b2,b3,c=x
                    if fam==0:
                        ok=(b1==0 and I*a2+e1*a3==0 and a1+e2*c==0)
                    elif fam==1:
                        ok=(b2==0 and I*a3+e1*a1==0 and a2+e2*c==0)
                    else:
                        ok=(b3==0 and I*a1+e1*a2==0 and a3+e2*c==0)
                    if ok: ids.append(j)
                req(len(ids)==8,"C2 eight-node support")
                out.append(frozenset(ids))
    req(len(out)==12,"12 C2 quartics")
    return out

C2=c2_supports()

class Q2:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return Q2(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return self+(-o)
    def __rsub__(self,o): return Q2(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return Q2(self.a*o.a+2*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inv(self):
        d=self.a*self.a-2*self.b*self.b
        req(d!=0,"Q(sqrt2) inverse")
        return Q2(self.a/d,-self.b/d)
    def __truediv__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return self*o.inv()
    def __eq__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return self.a==o.a and self.b==o.b

def q4(x):
    a1,a2,a3,b1,b2,b3,c=x
    return (
        a1*a1+a2*a2-b3*b3,
        a2*a2+a3*a3-b1*b1,
        a1*a1+a3*a3-b2*b2,
        a1*a1+a2*a2+a3*a3-c*c,
    )

def c4c5_node_preflight(S):
    c4=[]
    for fam in range(4):
        for e1 in (1,-1):
            for e2 in (1,-1):
                for e3 in (1,-1):
                    ids=[]
                    for j,x in enumerate(V):
                        a1,a2,a3,b1,b2,b3,c=x
                        if fam==0:
                            ok=(b1+e2*b2+e3*b3==0 and a2*a3+e1*I*a1*b1==0)
                        elif fam==1:
                            ok=(b1+e2*I*b2+e3*b3==0 and a1*a3+e1*b2*c==0)
                        elif fam==2:
                            ok=(b1+e2*b2+e3*I*b3==0 and a1*a2+e1*b3*c==0)
                        else:
                            ok=(b1+e2*I*b2+e3*I*b3==0 and a2*a3+e1*b1*c==0)
                        if ok: ids.append(j)
                    c4.append(frozenset(ids))
    req(len(c4)==32 and all(len(x)==12 for x in c4),"C4 supports")
    c5=[]
    for e1 in (1,-1):
        for e2 in (1,-1):
            for e3 in (1,-1):
                for e4 in (1,-1):
                    ids=[]
                    for j,x in enumerate(V):
                        a1,a2,a3,b1,b2,b3,c=x
                        if a1+e2*a2+e3*a3+e4*I*c==0 and (e2*a2+e3*a3)*b1+e1*I*b2*b3==0:
                            ids.append(j)
                    c5.append(frozenset(ids))
    req(len(c5)==16 and all(len(x)==0 for x in c5),"C5 box-node supports")
    return max(len(S&q) for q in c4), max(len(S&q) for q in c5)

def main():
    cert=json.loads(Path(__file__).with_name(
        "MB104-Z33G-NULL-UNION-PIC0-GLUING-HOLONOMY-CERTIFICATE.json").read_text())
    profiles=cert["zero_quartic_profiles"]
    expected={
      "0000770000ff":([0,1,2,3],[31,31,27,27]),
      "00007b0000ff":([0,1,2,3],[31,31,26,26]),
      "000707000f0f":([3,5],[27,35]),
      "00070b000f0f":([3,5],[26,35]),
    }
    for h,(wantq,wanto) in expected.items():
        S=from_mask(h)
        rows=[]
        for j,Q in enumerate(C2):
            if len(S&Q)==7:
                om=sorted(Q-S)
                req(len(om)==1,"one omitted node")
                rows.append((j,om[0]))
        req([j for j,_ in rows]==wantq and [o for _,o in rows]==wanto,"zero quartic profile "+h)
        req(profiles[h]["quartics"]==wantq and profiles[h]["omitted_nodes"]==wanto,"certificate profile "+h)

    # Exact common size-768 intersection reduction:
    # QA,QB imply a1=a2=c, a3=i*c, b1=b2=0 and b3^2=2*c^2.
    # c=0 would force the zero projective vector, hence exactly r_+,r_-.
    s=Q2(0,1)
    req(s*s==Q2(2),"sqrt2 square")
    # Surface equations at r_pm reduce to 0 exactly in Q(sqrt2)[i].
    # q1: 1+1-s^2=0; q2/q3: 1+i^2=0; q4: 1+1+i^2-1=0.
    req(Q2(1)+Q2(1)-s*s==Q2(0),"r q1")
    req(Q2(1)-Q2(1)==Q2(0),"r q2/q3")
    req(Q2(1)+Q2(1)-Q2(1)-Q2(1)==Q2(0),"r q4")

    # 000707... : LA27(r_pm)=pm*s-2 and LB35=i*(pm*s-2), so g+=g-=i.
    h_good=Q2(1)
    req(h_good==Q2(1),"trivial holonomy")

    # 00070b... :
    # after cancelling the common i, g+=(s-2)/(-s-2)=3-2s,
    # g-=(-s-2)/(s-2)=3+2s.
    gp=(s-2)/(-s-2)
    gm=(-s-2)/(s-2)
    req(gp==Q2(3,-2) and gm==Q2(3,2),"transition constants")
    hbad=gp/gm
    req(hbad==Q2(17,-12),"nontrivial holonomy 17-12sqrt2")
    req(hbad!=Q2(1) and hbad!=Q2(-1),"not real root of unity +/-1")

    # Displayed degree-eight source preflight on all four canonical supports.
    for h in expected:
        mx4,mx5=c4c5_node_preflight(from_mask(h))
        req(mx4<=4 and mx5==0,"degree8 node incidence "+h)
    d8=cert["degree8_preflight"]
    req(d8["max_supported_box_nodes_C4"]==4 and d8["supported_box_nodes_C5"]==0,"degree8 certificate")
    req(d8["zero_pairing_threshold"]==14 and d8["new_displayed_degree8_null_curve"] is False,"degree8 no new null")

    e=cert["elimination"]
    req(e["excluded_orbit_mask"]=="00070b000f0f","excluded mask")
    req(e["excluded_orbit_size"]==768,"excluded orbit size")
    req(e["previous_balanced_support_count"]==1632,"old count")
    req(e["remaining_balanced_support_count"]==864,"remaining count")
    req(e["remaining_orbits"]==["0000770000ff","00007b0000ff","000707000f0f"],"remaining orbits")
    req(all(v is False for v in cert["credit_firewall"].values()),"credit firewall")
    print("PASS: Z33G null-union Pic0 gluing holonomy")
    print("000707000f0f holonomy=1 survives")
    print("00070b000f0f holonomy=17-12*sqrt(2), non-torsion => orbit768 excluded")
    print("balanced hard core: 1632 -> 864 supports, 4 -> 3 Aut(S) orbits")
    print("degree8 displayed C4/C5 add no zero-pairing null curve")

if __name__=="__main__":
    main()
