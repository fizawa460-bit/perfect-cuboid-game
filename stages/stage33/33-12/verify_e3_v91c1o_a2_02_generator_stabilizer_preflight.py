#!/usr/bin/env python3
"""Verify V91C1O generator-stabilizer preflight without promoting residue-level fixing to H2 fixing."""
from __future__ import annotations
import hashlib,json,runpy
from pathlib import Path
D=Path(__file__).resolve().parent
C=D/'e3-v91c1o-a2-02-generator-stabilizer-preflight.json'
DIAG=D/'diagnose_e3_v91c1o_a2_02_geometric_stabilizer.py'
C_SHA='e5da15ac7ff1d39f8f6b35922d626bbfef335425bc2765fc9b9969600f54d359'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
o=json.loads(C.read_text(encoding='utf-8')); b=dict(o); q=b.pop('canonical_sha256'); assert q==C_SHA==csha(b)
ns=runpy.run_path(str(DIAG)); r=ns['result']
assert r['source_generator_fixed_names']==['sign_a1','sign_a2','sign_a3','sign_b1','sign_b2','sign_b3','sign_c']
assert r['source_generator_fixed_count']==7
assert r['joint_v4_fixed_dimension_before']==10
assert r['candidate_dimension_if_full_seed_fixed_under_source_generator_stabilizers']==7
assert r['e3_mask20_fixed_by_source_generator_stabilizers'] is True
assert o['residue_source_stabilizer_generators']['generator_fixed_names']==r['source_generator_fixed_names']
assert o['target_preflight']['dimension_if_full_seed_fixed_under_all_seven_sign_generators']==7
assert o['target_preflight']['e3_mask20_fixed_by_all_seven_sign_generators'] is True
assert o['type_firewall']['residue_direction_fixed_implies_full_cech_seed_fixed'] is False
assert o['type_firewall']['seed_level_geometric_transport_materialized'] is False
assert o['exact_consequence']['a2_02_marked_brauer_image_computed'] is False
assert o['entry_chain']['audit_pass_credit_for_batch_candidates'] is False
assert o['credit_firewall']['merge_allowed'] is False
print(json.dumps({'success':True,'marker':'V91C1O_A2_02_GENERATOR_STABILIZER_PREFLIGHT','certificate_sha256':C_SHA,'conditional_dimension':7,'seed_level_transport':False},sort_keys=True))
