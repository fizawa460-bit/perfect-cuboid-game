#!/usr/bin/env python3
"""Replay immutable V80 facts while allowing later exact Stage33 frontiers."""
from __future__ import annotations

import hashlib, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
STAGE=HERE.parent
STATE=STAGE/'MAIN-STATE.json'
V79=HERE/'e3-b1-full-gysin-matrix-xalpha-correction-v79.json'
V80=HERE/'e3-b1-route-freeze-and-outside-cech-rewire-v80.json'
V79_SHA='29acced201721df4ad65bda071914bf71a4b5d7098dce86a541cdd41f2085921'
V80_SHA='d75a7bbe14f5194b91a1411a372ce4b64982331d04da23d044591422fb37ccbf'
V80_BLOB='978828a81d11c00e9a53244e2ee2334b4e527250'


def csha(o):
 b=dict(o); h=b.pop('canonical_sha256'); got=hashlib.sha256(json.dumps(b,sort_keys=True,separators=(',',':')).encode()).hexdigest(); assert h==got; return h

def blob(path):
 d=path.read_bytes(); return hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()

state=json.loads(STATE.read_text()); assert state['canonical_sha256']==csha(state)
v79=json.loads(V79.read_text()); assert csha(v79)==V79_SHA
assert blob(V80)==V80_BLOB
v80=json.loads(V80.read_text()); assert csha(v80)==V80_SHA
# Immutable V79/V80 mathematics.
assert v79['b1_matrix']['column_masks_decimal']==[0,25,0,25]
assert v79['b1_matrix']['image_masks_decimal']==[0,25]
assert v79['e3_membership']['target_mask_decimal']==20
assert v79['e3_membership']['in_image'] is False
assert v80['v79_promotion']['b1_route_status']=='FROZEN_EXACT_V79_MASK20_NOT_IN_IMAGE'
assert v80['v79_promotion']['global_H2_mu2_nonexistence_claim'] is False
assert v80['rewired_current_leaf']['genuine_full_surface_H2_mu2_lift_for_e3'] is False
# Successor-safe live-state requirements only.
assert state['stage33_progress']=='6/11'
assert state['authority_sync']['controller_global_authority_locked'] is True
assert state['authority_sync']['operational_routing_authority']=='V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP'
assert state['locked_facts']['v79']['sha256']==V79_SHA
assert state['locked_facts']['v80']['sha256']==V80_SHA
f=state['current_exact_frontier']
assert f['e3_b1_matrix_materialized'] is True
assert f['e3_b1_image_masks_decimal']==[0,25]
assert f['e3_b1_membership'] is False
assert f['e3_b1_route_frozen'] is True
assert f['e3_proper14_mask_decimal']==20
assert f['e3_genuine_full_surface_h2_mu2_lift_materialized'] is False
assert f['e3_global_H2_mu2_nonexistence_claim'] is False
assert state['anti_loop_policy']['do_not_reopen_b1_gysin_membership_after_v79'] is True
assert state['anti_loop_policy']['do_not_promote_b1_nonmembership_to_global_H2_mu2_nonexistence'] is True
assert state['execution_gate']['advance_allowed'] is True
assert state['firewalls']['stage33_12_closed_exact'] is False
assert state['firewalls']['stage33_13_released'] is False
assert state['firewalls']['merge_allowed'] is False
print(json.dumps({
 'success':True,
 'marker':'V81_HISTORICAL_V80_REPLAY_COMPLETE_LIVE_FRONTIER_UNPINNED',
 'v80_canonical_sha256':V80_SHA,
 'live_frontier':state['authority_sync']['frontier_authority'],
 'b1_route_frozen':True,
 'global_H2_mu2_nonexistence_claim':False,
 'merge_allowed':False,
},sort_keys=True))
