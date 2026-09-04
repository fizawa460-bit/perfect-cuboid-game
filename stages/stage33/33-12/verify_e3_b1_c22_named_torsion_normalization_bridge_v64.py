#!/usr/bin/env python3
"""Verify V64 C22 branch-point to named elliptic 2-torsion bridge."""
import hashlib, json
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
V61=HERE/"e3-b1-c22-pic0-2-basis-v61.json"
V63=HERE/"e3-b1-c22-kappa-a-literal-cech-lift-v63.json"
ORI=HERE/"j2-cv-d2-semantic-orientation.json"
ART=HERE/"e3-b1-c22-named-torsion-normalization-bridge-v64.json"

def canonical(o):
    return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def blob(path):
    b=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load(path,digest,sha):
    assert blob(path)==sha,path
    o=json.loads(path.read_text())
    assert o["canonical_sha256"]==digest,path
    b=dict(o); b.pop("canonical_sha256")
    assert canonical(b)==digest,path
    return o

v61=load(V61,"48ec6b2ffb91d549041ff5ec667ff88d493becf01d89e1bb5974134b3b0a53f6","e50bde0bd88f29ce4bbe16f8d48fe89a8c3ab4d9")
v63=load(V63,"7714c722f7f30cae1fac03edd34821d1e84372bf3d7663dc2c62a98fde6b186c","3a966544378e2302f5a591e2162c30dbb5a3732e")
ori=load(ORI,"0a5abe419c3bd2e4c523af50fd8f85858af6a0d957dcce1e3bdf2ff1430fed3e","140acdc9896d1d87a82a1807fd92ce276a620d75")
art=json.loads(ART.read_text())
claimed=art["canonical_sha256"]; body=dict(art); body.pop("canonical_sha256")
assert claimed=="55679ba16710e3b78ab46ab699ea73ecc3fc56faab4cb7edc5a02e487df3de38"
assert canonical(body)==claimed

roots=v61["component"]["roots"]
assert roots=={"r1":"1+sqrt(2)","r2":"-(1+sqrt(2))","r3":"sqrt(2)-1","r4":"1-sqrt(2)"}
basis=v61["ordered_c22_pic0_2_basis"]
assert basis[0]["half_divisor"]=="D_A=P_r1-P_r4"
assert basis[1]["half_divisor"]=="D=P_r2-P_r4"
assert v63["literal_symbol"]["branch_input"]=="kappa_A=[P_r1-P_r4]"
assert ori["source_locks"]["named_transport_rigidity_git_blob_sha1"]=="2095dbaca6341f65a29690fe6b373f3da1be745a"
assert art["source_locks"]["historical_named_cv_pairing_blob_sha1"]=="5ef1d0549cd0c2e48ae4ffd2af99b6b6577e5b27"

# Q(sqrt(2)) replay of x=(t-(1+s))/((1+s)t+1).
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
Z=Fraction(0); O=Fraction(1); one=(O,Z); a=(O,O)
rs=[(O,O),(-O,-O),(-O,O),(O,-O)]
nd=[(sub(t,a),add(mul(a,t),one)) for t in rs]
assert nd[0]==((Z,Z),(Fraction(4),Fraction(2)))
assert nd[1]==((Fraction(-2),Fraction(-2)),(Fraction(-2),Fraction(-2)))
assert nd[2]==((Fraction(-2),Z),(Fraction(2),Z))
assert nd[3]==((Z,Fraction(-2)),(Z,Z))
assert art["normalization"]["root_images"]=={"r1":"J1","r2":"J2","r3":"J1+J2","r4":"O"}

bridge=art["exact_bridge"]
assert bridge["kappa_A"]=={"half_divisor":"P_r1-P_r4","named_torsion":"J1"}
assert bridge["kappa_D"]=={"half_divisor":"P_r2-P_r4","named_torsion":"J2"}
assert ori["exact_conclusion"]["named_CV_J2_semantic_discriminant_label"]=="u1"
assert ori["exact_conclusion"]["named_CV_J2_fixed_marked_Kc_coordinate_f2"]==[1,0]
iface=art["marked_kc_interface"]
assert iface["kappa_D"]=={"named_torsion":"J2","semantic":"u1","coordinate_f2":[1,0],"proper14_mask_decimal":25}
assert iface["kappa_A"]["semantic_candidates"]==["u2","u1+u2"]
assert iface["kappa_A"]["coordinate_candidates_f2"]==[[0,1],[1,1]]
assert iface["kappa_A"]["selected"] is None
assert iface["kappa_A"]["proper14_mask_decimal"] is None
assert iface["remaining_ambiguity_bits"]==1
fw=art["credit_firewall"]
for k in ["basis_complement_used_as_orientation","symmetry_guess_used","new_marked_proper14_gysin_column_materialized","b1_14x4_matrix_materialized","e3_mask20_membership_computed","stage33_12_closed_exact","stage33_13_released","merge_allowed"]:
    assert fw[k] is False,k
assert fw["stage33_progress"]=="6/11"
assert art["status"]=="PASS_EXACT_C22_NAMED_TORSION_BRIDGE_KAPPA_A_EQUALS_J1_MARKED_ORIENTATION_ONE_BIT_OPEN"
print(json.dumps({"success":True,"kappa_A":"J1","kappa_D":"J2","remaining_candidates":["u2","u1+u2"],"proper14_column3":None,"merge_allowed":False},sort_keys=True))
