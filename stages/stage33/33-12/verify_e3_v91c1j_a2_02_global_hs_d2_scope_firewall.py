#!/usr/bin/env python3
"""Verify V91C1J: Stage33-05 zero K3 Br2 Q-survival is not an A2_02 proper14 marking."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
HERE=Path(__file__).resolve().parent; S33=HERE.parent
CERT=HERE/'e3-v91c1j-a2-02-global-hs-d2-scope-firewall.json'
I=HERE/'e3-v91c1i-a2-02-audited-localization-zero-fingerprint.json'
Z=S33/'33-05'/'stage33-05-br2-zero-q-survival-hostile-replay.json'
STATE=S33/'33-05'/'j2-representative-repair-state.json'
def csha(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def load(p,expected=None,canonical=True):
    o=json.loads(p.read_text())
    if canonical:
        b=dict(o); claimed=b.pop('canonical_sha256'); assert csha(b)==claimed
        if expected: assert claimed==expected
    return o
z=load(Z,'4e9f20c1f753bb63134207422b097c1985ce3edd6be87f7f41ba8afa316e7dc9')
i=load(I,'241112a8dceaae61027b803438f3dd5b34f3f85387b95c02b6d490666011213c')
s=load(STATE,canonical=False)
c=load(CERT,'8b415428c34464515d6c77c36f01575b93a414734d6b887697afda404ffc38e0')
h=z['hostile_checks']; assert h['domain_dimension_f2']==2 and h['domain_basis']==['J2','q1']
assert h['global_kernel_dimension_f2']==0 and h['exact_zero_survival'] is True
assert z['verdict']['K3_BR2_Q_surviving_class_list']==[]
assert s['arithmetic_classification']['Q_relevant_surviving_dimension']==0
assert c['current_a2_02_problem_type']['desired_quotient']=='marked proper geometric Br(Sbar)[2] coordinate in dimension 14'
assert c['current_a2_02_problem_type']['v91c1g_joint_v4_fixed_subspace_dimension_f2']==10
assert c['type_firewall']['a2_02_unknown_marked_image_identified_with_stage33_05_J2_q1_domain'] is False
assert c['type_firewall']['global_hs_d2_result_can_select_mask20_for_a2_02'] is False
assert c['exact_consequence']['a2_02_marked_brauer_image_computed'] is False
assert c['entry_chain']['combined_hostile_audit_pending'] is True
assert c['credit_firewall']['stage33_progress']=='6/11' and c['credit_firewall']['merge_allowed'] is False
print(json.dumps({'success':True,'certificate_sha256':c['canonical_sha256'],'stage33_05_global_kernel_dim':0,'a2_02_marked_image_computed':False,'stage33_progress':'6/11'},sort_keys=True))
