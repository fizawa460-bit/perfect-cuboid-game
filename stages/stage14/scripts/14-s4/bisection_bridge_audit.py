#!/usr/bin/env python3
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'stages/stage14/data/14-s4/bisection_bridge_audit.json'

# Explicit 14-4ai+ artifacts are intentionally detected rather than assumed.
candidates=[]
for p in (ROOT/'stages/stage14').rglob('*'):
    if not p.is_file():
        continue
    s=str(p.relative_to(ROOT))
    low=s.lower()
    if any(tag in low for tag in ('14-4ai','14-4aj','14-4ak','14-4al')):
        candidates.append(s)

report={
  'metadata':{'stage':'14-s4','title':'Arithmetic/Kummer bisection bridge readiness audit'},
  'frozen_bridge':{
    'main_4ah_contract':'physical rational curves have M.C>=4; extremal sqrt(B) target is a Q-rational M-degree-4 bisection with degree 2 over r',
    's1_descent_coordinate':'(Z,Z-S^2,Z+X^2) modulo squares',
    's3_height_gate':'physical d<=B implies a non-torsion point in canonical height O(log B+log H)',
    'extremal_curve_height_exponent':'2/(M.C)=1/2 for M.C=4'
  },
  'required_upstream_payload':[
    'normalization parameter z on C~=P1',
    'degree-two base map r(z)',
    'physical coordinates and M-height d(z)',
    'induced elliptic point P_C(z)',
    'proof of physical-open and non-torsion status'
  ],
  'detected_14_4ai_plus_files':sorted(candidates),
  'decision':{
    'STAGE14_S4':'BRIDGE_READY_WAITING_FOR_14_4AI' if not candidates else 'UPSTREAM_ARTIFACT_DETECTED_REQUIRES_CLASS_COMPARISON',
    'BISECTION_TO_SELMER_COMPARISON_INTERFACE_LOCKED':True,
    'M_DEGREE4_HEIGHT_EXPONENT_COMPATIBILITY_LOCKED':True,
    'EXPLICIT_M_DEGREE4_BISECTION_IMPORTED':bool(candidates),
    'FINITE_BISECTION_COVERAGE_MEASURED':False,
    'BISECTION_DOMINANCE_PROVED':False,
    'ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED':False
  }
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report['decision'],indent=2))
