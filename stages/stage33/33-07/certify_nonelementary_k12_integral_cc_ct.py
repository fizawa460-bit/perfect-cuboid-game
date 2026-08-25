#!/usr/bin/env python3
"""Certify the exact integral cc/ct affine reduction on compressed k=1,2 glue types."""
import hashlib, json, runpy
from pathlib import Path
HERE=Path(__file__).resolve().parent
SCOUT_SHA='04348ed4a491efd9481c303c0eb3e3b73d6d00de5f3c1122385477d03b7529c2'
K1_SOURCE='702758b2c085db70b48577531377b5c8dace827f3080f43486fbcf0fd0605cf2'
K2_SOURCE='cfa87933b595744811b8ea2e04bf71ea39b75b0c3a9255437c4bc507b3846a95'
ACTION_LOCK='a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20'
runpy.run_path(str(HERE/'profile_nonelementary_k12_integral_cc_ct.py'))
x=json.loads((HERE/'nonelementary-k12-integral-cc-ct-scout.json').read_text())
assert x['canonical_sha256']==SCOUT_SHA
assert x['source_k1_sha256']==K1_SOURCE and x['source_k2_sha256']==K2_SOURCE
assert x['source_actions_sha256']==ACTION_LOCK
assert x['raw_cc_choices']==1024 and x['distinct_normalized_cc_actions']==8
assert x['raw_ct_choices']==128 and x['distinct_normalized_ct_actions']==1
expected={
 'k1':{'orbits':4595,'before':6723136,'after':2928832,'dims':{'4':1499,'5':2503,'6':593}},
 'k2':{'orbits':427,'before':67641344,'after':11866112,'dims':{'8':13,'9':130,'10':36,'11':203,'12':3,'13':42}},
}
for key,e in expected.items():
    y=x[key]
    assert y['skeleton_orbits']==e['orbits']
    assert y['raw_structural_H_reconstructed']==e['before']
    assert y['weighted_H_after_common_cc_locus_if_applicable']==e['after']
    assert y['common_cc_dimension_histogram']==e['dims']
    assert y['all_cc_choices_common_locus']
    assert y['cc_locus_count_histogram']=={'1':e['orbits']}
    assert y['orbits_with_missing_or_inconsistent_cc']==0
    assert y['ct_neutral_on_base_fibre_every_orbit']
    rec=y['records']; assert len(rec)==e['orbits']
    assert sum(int(r['orbit_size'])*(1<<int(r['base_dim'])) for r in rec)==e['before']
    assert sum(int(r['orbit_size'])*(1<<int(r['chosen_cc_dim'])) for r in rec)==e['after']
cert={
 'schema':'STAGE33_07_NONELEMENTARY_K12_INTEGRAL_CC_CT_CERT_V1',
 'source_scout_sha256':SCOUT_SHA,
 'source_k1_sha256':K1_SOURCE,'source_k2_sha256':K2_SOURCE,'source_actions_sha256':ACTION_LOCK,
 'raw_cc_choices_checked':1024,'normalized_cc_actions':8,'raw_ct_choices_checked':128,'normalized_ct_actions':1,
 'k1':{'H_before':6723136,'H_after_integral_cc_ct':2928832,'skeleton_orbits':4595,'affine_dimension_histogram':expected['k1']['dims']},
 'k2':{'H_before':67641344,'H_after_integral_cc_ct':11866112,'skeleton_orbits':427,'affine_dimension_histogram':expected['k2']['dims']},
 'combined_H_before':74364480,'combined_H_after_integral_cc_ct':14794944,
 'all_raw_cc_choices_induce_same_normalized_affine_locus_on_every_orbit':True,
 'ct_adds_no_affine_equation_on_every_orbit':True,
 'integral_cc_ct_certified':True,
 'full_Q4_condition_certified':False,'endpoint_finite_q_certified':False,'endpoint_full_action_certified':False,
 'actual_index512_glue_identified':False,'arithmetic_HS_closed':False,
 'stage33_progress':'6/11','stage33_08_released':False,'stage33_09_released':False,
 'theorem_credit':False,'endpoint_credit':False,'perfect_cuboid_nonexistence_claim':False,
 'next':'L33-07-IMPOSE-FULL-Q4-IMAGE-ORDER-ON-14794944-K1K2-INTEGRAL-ACTION-SURVIVORS'
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode(); cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'nonelementary-k12-integral-cc-ct-certified.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'k1_after':2928832,'k2_after':11866112,'combined_after':14794944,'certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
