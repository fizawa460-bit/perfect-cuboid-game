#!/usr/bin/env python3
"""Verify V91C1L finite 14-bit source-bound marked Brauer evaluation contract."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent
CERT=HERE/'e3-v91c1l-a2-02-cech-to-marked-discriminant-dual-evaluation-contract.json'
LOCKS={
 HERE/'e3-v91c-type-safe-cech-adapter-interface.json':'da156e8fcbd59743073b5a3d8ba5359c533b0b045adddc41877310974cdc1754',
 HERE/'e3-v91c1d-a2-02-purity-cech-cartier-assembly.json':'fafb639197f12b0570c9f63526a0020c8a543417043dc316f386c037f5938e14',
 HERE/'e3-proper14-dual-to-discriminant-quotient-bridge-v89.json':'26bf699fd92e261e1ae40066ad0fd5aece9cb896f28a385367786de1d0460639',
 HERE/'e3-retained-at-marked-picard-dual-source-v91.json':'729f296c1495d9ba600b085a6e9a5a0b53f8968a7997af4774fa11dc2d0215e9',
 HERE/'e3-v91c1k-a2-02-arsenal-applicability-matrix.json':'16ccf10acd65fd7101acd6a776771896cd3e3e91aa3a2bd49dba43e0d6cd11b3'}
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,e):
 o=json.loads(p.read_text()); b=dict(o); h=b.pop('canonical_sha256'); assert h==e and csha(b)==e; return o
for p,e in LOCKS.items(): load(p,e)
c=load(CERT,'6ae7e0464c2acd012c1c486e6a12fdb806d65049359c0c6c2440168be138e3dc')
e=c['evaluation_contract']; assert e['bit_count']==14 and len(e['bit_names'])==14
assert c['locked_types']['marked_target_dimension_f2']==14
assert c['locked_types']['target_e3_vector_f2']==[0,0,1,0,1,0,0,0,0,0,0,0,0,0]
assert c['acceptance']['source_evaluation_vector_materialized'] is False
assert e['each_bit_must_be_computed_from_literal_a2_02_seed'] is True
assert e['copying_target_mask20_bits_into_source_evaluation_forbidden'] is True
assert e['using_zero_absolute_localization_as_any_proper14_bit_forbidden'] is True
assert c['anti_inference']['contract_counts_as_computed_vector'] is False
assert c['exact_consequence']['a2_02_marked_brauer_image_computed'] is False
assert c['entry_chain']['combined_hostile_audit_pending'] is True
assert c['credit_firewall']['stage33_progress']=='6/11' and c['credit_firewall']['merge_allowed'] is False
print(json.dumps({'success':True,'certificate_sha256':c['canonical_sha256'],'evaluation_bits_required':14,'evaluation_bits_materialized':0,'stage33_progress':'6/11'},sort_keys=True))
