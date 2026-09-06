#!/usr/bin/env python3
"""Verify V91C1P frozen preflight by replaying the full residue-stabilizer diagnostic."""
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path
D=Path(__file__).resolve().parent
C=D/'e3-v91c1p-a2-02-full-residue-stabilizer-preflight.json'
DIAG=D/'diagnose_e3_v91c1p_a2_02_full_residue_stabilizer.py'
C_SHA='7e1455f071c36d8e79651f5d0aa70d6f5e0a2ab7406e2fbe2e492d7b43f94545'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
o=json.loads(C.read_text()); b=dict(o); q=b.pop('canonical_sha256'); assert q==C_SHA==csha(b)
r=runpy.run_path(str(DIAG))['result']
assert r['source_orbit_size']==3
assert r['joint_v4_fixed_dimension_before']==10
assert r['conditional_dimension_if_full_seed_stabilized_by_full_residue_stabilizer']==5
assert r['e3_mask20_fixed_by_full_residue_stabilizer_target_actions'] is False
p=o['full_residue_stabilizer_preflight']
assert p['a2_02_source_residue_orbit_size']==3
assert p['conditional_fixed_subspace_dimension_f2']==5
assert p['conditional_fixed_subspace_cardinality']==32
assert p['e3_mask20_fixed_by_full_residue_stabilizer_target_actions'] is False
assert o['type_firewall']['seed_level_stabilizer_transport_materialized'] is False
assert o['anti_inference']['mask20_excluded_as_a2_02_image'] is False
assert o['credit_firewall']['a2_02_marked_brauer_image_computed'] is False
assert o['entry_chain']['audit_pass_credit_for_batch_candidates'] is False
print(json.dumps({'success':True,'marker':'V91C1P_FULL_RESIDUE_STABILIZER_PREFLIGHT','certificate_sha256':C_SHA,'source_orbit_size':3,'conditional_dimension':5,'mask20_full_residue_stabilizer_fixed':False,'seed_level_transport':False},sort_keys=True))
