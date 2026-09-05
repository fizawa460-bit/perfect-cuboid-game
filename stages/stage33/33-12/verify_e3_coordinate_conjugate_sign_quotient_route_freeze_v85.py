#!/usr/bin/env python3
"""Replay V85: all coordinate-conjugate B1/B2/B3 sign-quotient routes miss mask20."""
from __future__ import annotations

import hashlib, json, runpy, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
CERT=HERE/'e3-coordinate-conjugate-sign-quotient-route-freeze-v85.json'
V84=HERE/'diagnose_e3_coordinate_automorphism_orbit_v84.py'
V79=HERE/'e3-b1-full-gysin-matrix-xalpha-correction-v79.json'
S09=HERE.parent/'33-09'; S07=HERE.parent/'33-07'
BRIDGE=S09/'marked-picard-basis-bridge-certified.json'
ADJ=HERE/'j2-picard-adjoint-proper-br2.json'
SIGN=S07/'picard_coordinate_sign_rows_retained.py'
CERT_SHA='6f63d8814d87d1e9ae4810fb9a5a3d09c9f37f0d3bd2875ddf7f4dce43c82159'
V84_BLOB='e9c7e81cc59fb5203482071208d25ff1447edeb2'
V79_SHA='29acced201721df4ad65bda071914bf71a4b5d7098dce86a541cdd41f2085921'
BRIDGE_SHA='039e3792e950ac5bf94adf6538c229640da231000a5e1b159a80e2323a812a92'
ADJ_SHA='066e6b039eb7b67c6dfc44a7af1459254c190ebfa5376e89b8e97fad1c8cb9f8'
SIGN_SHA='5cd64ca89ee9f3ec76d275bc4082349764ac8a5cb4647a9bb9a4eaf267b76ab9'


def csha(o):
 b=dict(o); h=b.pop('canonical_sha256'); got=hashlib.sha256(json.dumps(b,sort_keys=True,separators=(',',':')).encode()).hexdigest(); assert h==got; return h

def blob(path):
 d=path.read_bytes(); return hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()

c=json.loads(CERT.read_text()); assert csha(c)==CERT_SHA
v79=json.loads(V79.read_text()); assert csha(v79)==V79_SHA
bridge=json.loads(BRIDGE.read_text()); assert csha(bridge)==BRIDGE_SHA
adj=json.loads(ADJ.read_text()); assert csha(adj)==ADJ_SHA
sign=runpy.run_path(str(SIGN))['load'](); assert sign['canonical_sha256']==SIGN_SHA
assert blob(V84)==V84_BLOB
p=subprocess.run([sys.executable,str(V84)],check=True,capture_output=True,text=True)
r=json.loads(p.stdout.strip().splitlines()[-1])
assert r['success'] is True
assert r['generator_count']==9
assert r['all_generators_involutive_on_proper14'] is True
assert r['orbit_size_from_mask25']==1
assert r['orbit_masks_decimal']==[25]
assert r['target_mask']==20
assert r['target_in_coordinate_automorphism_orbit'] is False
assert r['shortest_word_to_target'] is None
assert c['finite_group_replay']['mask25_orbit_size']==1
assert c['finite_group_replay']['mask25_orbit_masks_decimal']==[25]
assert c['sign_quotient_consequence']['b1_exact_image_masks_decimal']==[0,25]
assert c['sign_quotient_consequence']['swap12_maps_B1_to_B2'] is True
assert c['sign_quotient_consequence']['swap13_maps_B1_to_B3'] is True
assert c['sign_quotient_consequence']['coordinate_conjugate_B1_B2_B3_image_masks_decimal']==[0,25]
assert c['sign_quotient_consequence']['e3_target_mask_decimal']==20
assert c['sign_quotient_consequence']['e3_in_any_coordinate_conjugate_sign_quotient_image'] is False
assert c['exact_boundary']['global_H2_mu2_nonexistence_claim'] is False
assert c['exact_boundary']['non_coordinate_conjugate_full_surface_realization_still_open'] is True
assert c['credit_firewall']['stage33_progress']=='6/11'
assert c['credit_firewall']['stage33_12_closed_exact'] is False
assert c['credit_firewall']['stage33_13_released'] is False
assert c['credit_firewall']['merge_allowed'] is False
print(json.dumps({
 'success':True,
 'marker':'V85_COORDINATE_CONJUGATE_SIGN_QUOTIENT_ROUTE_FREEZE_COMPLETE',
 'canonical_sha256':CERT_SHA,
 'coordinate_automorphism_orbit_masks':[25],
 'coordinate_conjugate_sign_quotient_image_masks':[0,25],
 'e3_target_mask':20,
 'global_H2_mu2_nonexistence_claim':False,
 'next_exact_leaf':c['next_exact_leaf'],
 'merge_allowed':False,
},sort_keys=True))
