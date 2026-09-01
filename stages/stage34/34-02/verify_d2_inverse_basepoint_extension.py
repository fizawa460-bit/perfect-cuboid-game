#!/usr/bin/env python3
from fractions import Fraction
import json, pathlib

ROOT=pathlib.Path(__file__).resolve().parent
maps=json.loads((ROOT/"d2-quartic-map-certificate.json").read_text())
records=[]
for c in maps["cases"]:
    q=Fraction(c["q"])
    a1,a2,a3,a4,a6=[Fraction(x.strip()) for x in c["magma_elliptic_a_invariants"].strip()[1:-1].split(',')]
    assert a6==0
    assert a3!=0
    # On y^2+a1*x*y+a3*y=x^3+a2*x^2+a4*x at (0,0),
    # the implicit-function expansion is y=(a4/a3)x+O(x^2).
    # The inverse-map projective t-coordinate [T:S]=[y:2x+y]
    # therefore extends to t=a4/(2*a3+a4), provided the denominator is nonzero.
    den=2*a3+a4
    assert den!=0
    t=a4/den
    d=int(c["d"])
    if d==1:
        x=q*(t*t-1)/(2*t)
        assert t!=0
        assert x not in (q,-q)
    else:
        x=q*(2*t*t-4*t+1)/(2*t*t-1)
        assert t==1
        assert x==-q
    records.append({"q":c["q"],"d":d,"extended_t":str(t),"receiver_x":str(x),"a3":str(a3),"a4":str(a4)})

payload={
  "schema":"STAGE34_02_D2_INVERSE_BASEPOINT_LOCAL_EXTENSION_V1",
  "status":"PASS_EXACT_14_OF_14_T_COORDINATE_EXTENSIONS_AT_MAGMA_E_00",
  "source":"stages/stage34/34-02/d2-quartic-map-certificate.json",
  "derivation":"At the smooth Magma-E point (0,0), a3!=0 gives y=(a4/a3)x+O(x^2); since the inverse map has t=[y:2x+y], t extends to a4/(2a3+a4).",
  "cases":records,
  "d2_summary":"All seven d=2 extensions have t=1 and receiver x=-q, hence land on an already-audited order-4 receiver pole.",
  "d1_summary":"All seven d=1 extensions are finite non-pole receiver-x values and must be retained exactly in finite reduction rather than treated as wildcard.",
  "failed_conjugate_attempt":{"run":33505167479,"classification":"ASSUMPTION_REJECTED_NO_CLOSURE_CREDIT","fact":"For q=20/21,d=1 the conjugate selected base point maps to (0:-a3:1), not to an order-2 point; this is distinct from the inverse-coordinate base point (0,0)."},
  "firewalls":{"local_extension_is_matching_x_closure":False,"d2_pole_extension_is_non_torsion_receiver_survival":False,"receiver_closed":False}
}
(ROOT/"d2-inverse-basepoint-extension.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"cases":len(records)},sort_keys=True))
