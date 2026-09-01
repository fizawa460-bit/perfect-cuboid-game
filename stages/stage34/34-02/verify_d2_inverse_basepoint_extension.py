#!/usr/bin/env python3
from fractions import Fraction
import json, pathlib

ROOT=pathlib.Path(__file__).resolve().parent
maps=json.loads((ROOT/"d2-quartic-map-certificate.json").read_text())
records=[]
classes={"finite_nonpole":0,"pole_plus":0,"pole_minus":0,"infinity":0}
for c in maps["cases"]:
    q=Fraction(c["q"])
    a,b=q.numerator,q.denominator
    a1,a2,a3,a4,a6=[Fraction(x.strip()) for x in c["magma_elliptic_a_invariants"].strip()[1:-1].split(',')]
    assert a6==0
    assert a3!=0
    # On y^2+a1*x*y+a3*y=x^3+a2*x^2+a4*x at (0,0),
    # the implicit-function expansion is y=(a4/a3)x+O(x^2).
    # Since the persisted inverse map has [T:S]=[y:2x+y], the
    # curve-level parameter extends to [a4 : 2*a3+a4].
    T=a4; S=2*a3+a4
    assert not (T==0 and S==0)
    d=int(c["d"])
    if d==1:
        X=Fraction(a)*(T*T-S*S)
        Z=Fraction(2*b)*T*S
    else:
        X=Fraction(a)*(2*T*T-4*T*S+S*S)
        Z=Fraction(b)*(2*T*T-S*S)
    assert not (X==0 and Z==0)
    if Z==0:
        kind="infinity"; x=None
    else:
        x=X/Z
        if x==q: kind="pole_plus"
        elif x==-q: kind="pole_minus"
        else: kind="finite_nonpole"
    classes[kind]+=1
    records.append({
        "q":c["q"],"d":d,
        "extended_t_projective":[str(T),str(S)],
        "extended_t_affine":None if S==0 else str(T/S),
        "receiver_x_projective":[str(X),str(Z)],
        "receiver_x":None if x is None else str(x),
        "classification":kind,
        "a3":str(a3),"a4":str(a4)
    })

assert len(records)==14
payload={
  "schema":"STAGE34_02_D2_INVERSE_BASEPOINT_LOCAL_EXTENSION_V2",
  "status":"PASS_EXACT_14_OF_14_PROJECTIVE_T_AND_RECEIVER_X_EXTENSIONS_AT_MAGMA_E_00",
  "source":"stages/stage34/34-02/d2-quartic-map-certificate.json",
  "derivation":"At the smooth Magma-E point (0,0), a3!=0 gives y=(a4/a3)x+O(x^2); the inverse-map t=[y:2x+y] therefore extends projectively to [a4:2*a3+a4]. The locked d=1/d=2 projective x maps are then evaluated without any extra assumption on the image.",
  "cases":records,
  "classification_counts":classes,
  "failed_conjugate_attempt":{"run":33505167479,"classification":"ASSUMPTION_REJECTED_NO_CLOSURE_CREDIT","fact":"The hyperelliptic conjugate of the selected base point is not generally order-2 on Magma E; it is distinct from the inverse-coordinate base point (0,0)."},
  "removed_false_assumption":"No assertion that d=2 has t=1 or x=-q is retained. The exact projective extension decides the image case by case.",
  "firewalls":{"local_extension_is_matching_x_closure":False,"pole_or_infinity_classification_is_non_torsion_receiver_survival":False,"receiver_closed":False}
}
(ROOT/"d2-inverse-basepoint-extension.json").write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"cases":len(records),"classification_counts":classes},sort_keys=True))
