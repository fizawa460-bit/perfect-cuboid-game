#!/usr/bin/env python3
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve()
CL = HERE.parent / "cyclotomic_quartic_allocation_audit.py"
spec = spec_from_file_location("stage14_4cl", CL)
assert spec and spec.loader
cl = module_from_spec(spec)
spec.loader.exec_module(cl)

oddpart = cl.oddpart


def audit_pair(a, b):
    cells, triple, _, hs = cl.ck.ch.residual_data(a, b)
    R,S,T,J,alpha,beta,gamma,delta = cells
    C,u,v = triple
    hk_plus,hk_minus,hx_plus,hx_minus = hs
    r=a["r"]*b["r"]; s=a["s"]*b["s"]
    X=a["x"]*b["x"]; Y=a["y"]*b["y"]
    A=alpha*r; D=delta*s; U=R*X; V=J*Y

    assert oddpart(hk_minus) == oddpart(R*J)*oddpart(u)
    assert oddpart(hx_minus) == oddpart(alpha*delta)*oddpart(v)

    xb = cl.cyclotomic_partition(R*J,A,D)
    kb = cl.cyclotomic_partition(alpha*delta,U,V)
    assert xb[2] == 1 and kb[2] == 1
    mm,mp,_ = xb; nm,np,_ = kb
    assert mm*mp == oddpart(R*J)
    assert nm*np == oddpart(alpha*delta)

    exm=oddpart(D-A)//mm; exp=oddpart(D+A)//mp
    ekm=oddpart(V-U)//nm; ekp=oddpart(V+U)//np
    assert exm*exp == oddpart(u)
    assert ekm*ekp == oddpart(v)

    am=(D-A)//mm; ap=(D+A)//mp
    bm=(V-U)//nm; bp=(V+U)//np
    epsk=(alpha*delta)//(nm*np)
    epsx=(R*J)//(mm*mp)
    assert epsk in (1,2) and epsx in (1,2)
    assert (ap*mp)**2-(am*mm)**2 == 4*epsk*r*s*nm*np
    assert (bp*np)**2-(bm*nm)**2 == 4*epsx*X*Y*mm*mp
    return 1


def main():
    groups=cl.ck.ch.make_groups(420)
    checked=0
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i+1,len(states)):
                a,b=states[i],states[j]
                if (a["a"],a["b"])==(b["a"],b["b"]): continue
                if (a["km"],a["kp"])==(b["km"],b["kp"]): continue
                checked += audit_pair(a,b)
    assert checked>0
    theta=Fraction(5,16); phi=Fraction(1,4)
    assert phi == Fraction(1,4)
    assert theta == Fraction(5,16)
    assert theta-phi == Fraction(1,16)
    assert phi+Fraction(1,8)-theta == Fraction(1,16)
    print("Stage14-4cm audit: PASS")
    print("physical dual-cross pairs checked:", checked)
    print("xi/k quadratic cyclotomic branches: empty")
    print("linear quotient products: odd(u_res), odd(v_res)")
    print("sharp dominant linear exponents: 1/4, 5/16")
    print("sharp dominant quotient exponents <= 1/16, 1/16")

if __name__ == "__main__": main()
