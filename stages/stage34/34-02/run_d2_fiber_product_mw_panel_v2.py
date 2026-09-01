#!/usr/bin/env python3
"""V2 exact matching-x panel: reuse V1 engine, but replace the single
inverse-coordinate [0:0] case by the exact local extension certified in
verify_d2_inverse_basepoint_extension.py.
"""
from fractions import Fraction
import json, pathlib

ROOT=pathlib.Path(__file__).resolve().parent
source=(ROOT/"run_d2_fiber_product_mw_panel.py").read_text(encoding="utf-8")
marker="maps=json.loads"
assert marker in source
prefix,suffix=source.split(marker,1)
ns={"__file__":str(ROOT/"run_d2_fiber_product_mw_panel.py"),"__name__":"stage34_d2_panel_v2_engine"}
exec(prefix,ns)

# Replace only the J_q -> receiver-x evaluator.  Magma IsomorphismData gives
# E_magma -> J_q as (x,y)->(u^2 x+r, u^3 y+s u^2 x+t).
def jq_xfunc_v2(name,d,p,case):
    a,b=ns["FIBERS"][name]["a"],ns["FIBERS"][name]["b"]
    rr,ss,tt,uu=ns["parse_iso"](case["isomorphism_data_to_common_Jq"])
    r,s,t,u=[ns["red"](z,p) for z in (rr,ss,tt,uu)]
    assert u%p
    invpol=case["inverse_polynomials"]
    assert invpol[0].replace(" ","")=="$.2*$.3"
    assert invpol[2].replace(" ","")=="2*$.1*$.3+$.2*$.3"
    ainv=[Fraction(x.strip()) for x in case["magma_elliptic_a_invariants"].strip()[1:-1].split(',')]
    a1,a2,a3,a4,a6=ainv
    assert a6==0 and a3!=0 and 2*a3+a4!=0
    t0=a4/(2*a3+a4)
    def f(Q):
        if Q is None:
            T,S=(1,1) if d==1 else (0,1)
        else:
            Xj,Yj=Q
            xe=(Xj-r)*ns["inv"](u*u,p)%p
            ye=(Yj-s*(Xj-r)-t)*ns["inv"](u*u*u,p)%p
            if xe==0 and ye==0:
                # Exact curve-level extension of [y:2x+y] at the Magma-E
                # inverse-coordinate base point (0,0).
                try:
                    T=ns["red"](t0,p); S=1
                except Exception:
                    return None
            else:
                T=ye; S=(2*xe+ye)%p
        if d==1:
            X=a*(T*T-S*S); Z=2*b*T*S
        else:
            X=a*(2*T*T-4*T*S+S*S); Z=b*(2*T*T-S*S)
        return ns["p1"](X,Z,p)
    return f

ns["jq_xfunc"]=jq_xfunc_v2
exec(marker+suffix,ns)

p=ROOT/"d2-fiber-product-mw-panel.json"
data=json.loads(p.read_text())
assert all(z["J_indeterminate_states"]==0 for c in data["cases"] for z in c["local"])
data["schema"]="STAGE34_02_D2_FIBER_PRODUCT_MW_PANEL_V2_NO_INDETERMINATE_J_STATES"
data["status"]="PASS_EXACT_FOUR_PRIME_MATCHING_X_PANEL_WITH_LOCAL_BASEPOINT_EXTENSION"
data["source_inverse_basepoint_extension"]="d2-inverse-basepoint-extension.json"
data["J_indeterminate_states_total"]=0
out=ROOT/"d2-fiber-product-mw-panel-v2.json"
out.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n")
p.unlink()
print(json.dumps({"status":data["status"],"cases":len(data["cases"]),"J_indeterminate_states_total":0},sort_keys=True))
