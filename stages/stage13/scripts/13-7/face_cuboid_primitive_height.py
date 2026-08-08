#!/usr/bin/env python3
"""Stage13-7je: primitive-height ledger for the coupled face-cuboid model."""
from __future__ import annotations
import json, math
from pathlib import Path

OUT=Path("stages/stage13/data/13-7/face_cuboid_primitive_height_report.json")

def audit(hmax=24):
    total=sol=fail=0; ratios={}; examples=[]
    for u in range(2,hmax+1):
      for v in range(1,u):
        if math.gcd(u,v)!=1: continue
        for m in range(2,hmax+1):
          for n in range(1,m):
            if math.gcd(m,n)!=1: continue
            total+=1
            q=(u*u*n*n-m*m*v*v)*(u*u*m*m-v*v*n*n)
            if q<=0: continue
            w=math.isqrt(q)
            if w*w!=q: continue
            sol+=1
            A=2*m*n*u*v
            B=abs(m*m-n*n)*u*v
            P=(m*m+n*n)*u*v
            H=m*n*abs(u*u-v*v)
            D=m*n*(u*u+v*v)
            if A*A+B*B!=P*P or B*B+w*w!=H*H or P*P+w*w!=D*D:
                fail+=1
            g=0
            for x in (A,B,w,P,H,D): g=math.gcd(g,x)
            G=math.gcd(u*v,m*n)
            if not (G<=g<=2*G): fail+=1
            ratios[str(g//G)]=ratios.get(str(g//G),0)+1
            if len(examples)<8: examples.append({"u":u,"v":v,"m":m,"n":n,"G":G,"g":g,"primitive_d":D//g})
    return {"H_parameter_max":hmax,"parameter_quadruples":total,"square_solutions":sol,"failures":fail,"g_over_G_histogram":ratios,"examples":examples}

def build():
    checks=audit()
    if checks["failures"]: raise ArithmeticError(checks)
    return {
      "metadata":{"stage":"13-7je","scope":"exact primitive common-factor and coupled-height ledger"},
      "cleared_face_cuboid":{
        "parameters":"s=u/v, t=m/n; gcd(u,v)=gcd(m,n)=1",
        "edges":["2mnuv","(m^2-n^2)uv","W"],
        "first_face_diagonal":"(m^2+n^2)uv",
        "second_face_diagonal":"mn(u^2-v^2)",
        "space_diagonal":"D0=mn(u^2+v^2)",
        "square_condition":"W^2=(un-mv)(un+mv)(um-vn)(um+vn)"
      },
      "primitive_gcd_ledger":{
        "G":"gcd(uv,mn)",
        "lower_bound":"G divides every cleared edge/diagonal, including W because G^2 divides W^2",
        "upper_bound_1":"the common gcd divides gcd(2mnuv,(m^2-n^2)uv,(m^2+n^2)uv), which divides 2uv",
        "upper_bound_2":"it also divides gcd(2mnuv,mn(u^2-v^2),mn(u^2+v^2)), which divides 2mn",
        "conclusion":"G <= g <= 2G"
      },
      "primitive_height":{
        "exact":"d=D0/g=mn(u^2+v^2)/g",
        "sandwich":"mn(u^2+v^2)/(2 gcd(uv,mn)) <= d <= mn(u^2+v^2)/gcd(uv,mn)",
        "necessary_cutoff":"d<=B implies mn(u^2+v^2)/gcd(uv,mn) <= 2B",
        "importance":"this couples the two Pythagorean parameter pairs and is strictly sharper for averaging than treating H(s),H(t)<=sqrt(B) independently"
      },
      "remaining_count":{
        "target":"count square-condition quadruples under mn(u^2+v^2)/gcd(uv,mn)<=2B by o(B(log B)^3)",
        "status":"not proved in 13-7je"
      },
      "finite_exact_checks":checks,
      "status":{"primitive_coupled_height_exact":True,"common_gcd_within_factor_2":True,"pair_overlap_lower_order_proved":False,"exact_one_directional_limit_identified":False,"next":"Stage13-7jf"}
    }

def main():
    r=build(); OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n"); print(json.dumps(r["status"],indent=2))
if __name__=="__main__": main()
