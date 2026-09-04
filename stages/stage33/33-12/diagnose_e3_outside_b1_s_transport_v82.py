#!/usr/bin/env python3
"""Bounded exact-interface diagnostic for S:B1->B3 transport.

No Brauer/Gysin column is granted.  This probe identifies the exact retained
objects needed to descend S=swap13*sign(a2) from Picard64 to the ordered
proper14 discriminant basis.
"""
from __future__ import annotations

import hashlib, json, runpy, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
S07 = HERE.parent / "33-07"; S09 = HERE.parent / "33-09"
S32 = ROOT / "stages/stage32/residual-32-01-production"
sys.path.insert(0, str(S07))
from stage32_picard_marking_retained import load as load_marking  # type: ignore

ADAPTER=S32/"post1529-fsm-stoll-diagonal-action-source-lock.json"
BRIDGE=S09/"marked-picard-basis-bridge-certified.json"
SIGN=S07/"picard_coordinate_sign_rows_retained.py"
ADJOINT=HERE/"j2-picard-adjoint-proper-br2.json"
MARKING_SHA="e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
ADAPTER_SHA="5726289d8948beaaf3ed4e2dc260f49d1b3b3054642f3460b6b1e53c77ea23bc"
BRIDGE_BLOB="77b16e2ee80c33af27f7a5a04e1c465e9fc1acea"
ADJOINT_SHA="066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8"


def csha(o, field="canonical_sha256"):
    b=dict(o); claimed=b.pop(field); got=hashlib.sha256(json.dumps(b,sort_keys=True,separators=(",",":")).encode()).hexdigest(); assert claimed==got; return got

def blob(path):
    d=path.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()

def shape(x):
    if isinstance(x,list): return [len(x),len(x[0])] if x and isinstance(x[0],list) else [len(x)]
    if isinstance(x,dict): return {"keys":sorted(x)}
    return type(x).__name__

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

marking=load_marking(); assert marking["canonical_sha256"]==MARKING_SHA
adapter=json.loads(ADAPTER.read_text()); assert csha(adapter,"canonical_sha256_without_this_field")==ADAPTER_SHA
assert blob(BRIDGE)==BRIDGE_BLOB
bridge=json.loads(BRIDGE.read_text()); assert csha(bridge)==bridge["canonical_sha256"]
adj=json.loads(ADJOINT.read_text()); assert csha(adj)==ADJOINT_SHA
sign=runpy.run_path(str(SIGN))["load"]()
assert sign["canonical_sha256"]==bridge["source_locks"]["retained_old_picard_signs_sha256"]
assert sign["coordinate_order"]==["a1","a2","a3","b1","b2","b3","c"]
Sinfo=adapter["fsm_section2_actions"]["S"]
assert Sinfo["normalized_box_action"]==["a3","-a2","a1","b3","b2","b1","c"]
acs=bridge["actual_coordinate_swaps_in_historical_magma_picard_basis"]
S13=acs["swap13_action_64x64"]; A2=sign["picard_actions_64x64"]["a2"]
S64=mm(S13,A2)
I=[[int(i==j) for j in range(64)] for i in range(64)]
assert mm(S64,S64)==I
D=adj["degree2_picard_adjoint"]
dshapes={k:shape(v) for k,v in D.items()}
small={k:v for k,v in D.items() if isinstance(v,(str,bool,int,float)) or (isinstance(v,list) and len(v)<=20 and not(v and isinstance(v[0],list)))}

print(json.dumps({
 "success":True,
 "marker":"V82_BOUNDED_S_TRANSPORT_INTERFACE_DIAGNOSTIC",
 "marking_canonical_sha256":MARKING_SHA,
 "bridge_canonical_sha256":bridge["canonical_sha256"],
 "retained_sign_canonical_sha256":sign["canonical_sha256"],
 "adjoint_canonical_sha256":ADJOINT_SHA,
 "S_box_action":Sinfo["normalized_box_action"],
 "S_factorization_historical_picard64":"swap13_action_64x64 * sign(a2)_64x64",
 "S64_involution_exact":True,
 "S_maps_B1_to_B3":True,
 "adjoint_degree2_interface_shapes":dshapes,
 "adjoint_degree2_small_metadata":small,
 "proper14_action_materialized":False,
 "b3_gysin_image_materialized":False,
 "merge_allowed":False,
},sort_keys=True))
