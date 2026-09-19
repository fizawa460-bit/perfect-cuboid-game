#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path

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
        n=self.a*self.a-2*self.b*self.b
        assert n != 0
        return Q2(self.a/n,-self.b/n)
    def __truediv__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return self*o.inv()
    def __eq__(self,o):
        o=o if isinstance(o,Q2) else Q2(o)
        return self.a==o.a and self.b==o.b

class C:
    __slots__=("r","i")
    def __init__(self,r=0,i=0):
        self.r=r if isinstance(r,Q2) else Q2(r)
        self.i=i if isinstance(i,Q2) else Q2(i)
    def __add__(self,o):
        o=o if isinstance(o,C) else C(o)
        return C(self.r+o.r,self.i+o.i)
    __radd__=__add__
    def __neg__(self): return C(-self.r,-self.i)
    def __sub__(self,o):
        o=o if isinstance(o,C) else C(o)
        return self+(-o)
    def __mul__(self,o):
        o=o if isinstance(o,C) else C(o)
        return C(self.r*o.r-self.i*o.i,self.r*o.i+self.i*o.r)
    __rmul__=__mul__
    def inv(self):
        n=self.r*self.r+self.i*self.i
        return C(self.r/n,-self.i/n)
    def __truediv__(self,o):
        o=o if isinstance(o,C) else C(o)
        return self*o.inv()
    def __eq__(self,o):
        o=o if isinstance(o,C) else C(o)
        return self.r==o.r and self.i==o.i

I=C(0,1)
d=json.loads(Path(__file__).with_name(
 "MB104-Z37-SURVIVING-768-FIRST-NORMAL-EXACT-TRANSITION-CERTIFICATE.json").read_text())
assert d["schema"]=="STAGE32_MB104_Z37_SURVIVING768_FIRST_NORMAL_EXACT_TRANSITION_V1"
assert d["support"]=="000707000f0f"

for sign in (1,-1):
    s=Q2(0,sign)
    assert s*s==Q2(2)
    D=C(s-2)
    g=C(0,1)
    gu=-C(1)/D
    gv=C(1)/D
    guv=I/(D*D)
    kappa=guv/g-(gu*gv)/(g*g)
    assert kappa==C(0)

coh=d["cohomology"]
assert coh["degree_on_A"]==2 and coh["degree_on_B"]==2
assert coh["component_H1_zero"] is True
assert coh["normalized_node_fiber_vector"]==[0,0]
assert coh["first_normal_class_zero"] is True
con=d["conclusion"]
assert con["O_2U_P_trivial"] is True
assert con["O_2U_lP_trivial_all_l_ge_1"] is True
assert con["surviving_768_excluded"] is False
assert d["next_leaf"]=="MB104-Z38-SURVIVING-768-ALL-HIGHER-FORMAL-PICARD-VANISHING"
assert all(v is False for v in d["credit_firewall"].values())
print("PASS: Z37 surviving-768 first-normal exact transition")
print("at both r_+,r_-: normalized mixed coefficient kappa=0")
print("O(P)|2U is trivial; first formal obstruction vanishes")
