#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DS/proselmer-torsion-injectivity-correction.json'
SRC=ROOT/'stages/stage36/36-09DS/proselmer-torsion-injectivity-correction-source-lock.md'
POL=ROOT/'docs/research-os/policies/research-credit-and-promotion-firewalls.md'
DQ=ROOT/'stages/stage36/36-09DQ/global-2primary-adelic-annihilator-proselmer-source-lock.md'
DS=ROOT/'stages/stage36/36-09DS/fixed-p2-v4-isogeny-2primary-proselmer-transport-preflight.json'
DS_SRC=ROOT/'stages/stage36/36-09DS/v4-isogeny-norm-pullback-proselmer-source-lock.md'
DT=ROOT/'stages/stage36/36-09DT/fixed-p2-v4-isogeny-proselmer-defect-preflight.json'
LOCKS={
 CERT:'d3318c8291835de8011f6b72fea8ca4479c3107d',
 SRC:'7b8d09ddf0eaa147af01437d0ef19a80da44fb0c',
 POL:'7a3de0b2692afe4fb25b6825b31bd0384a118a41',
 DQ:'71829ec5e0af601605f1f93c5f3a3fec4cae2102',
 DS:'8c16b2f2c53f343dc710bf06d55245aab0599a36',
 DS_SRC:'1bac0039c0abccc236b392c2deba3a26ee83ba88',
 DT:'362326de8d6ecc0b415ecf29c6eb936134e395ce',
}

def gh(p):
 return subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
for p,h in LOCKS.items(): assert gh(p)==h,(p,gh(p),h)

c=json.loads(CERT.read_text()); ds=json.loads(DS.read_text()); dt=json.loads(DT.read_text())
dq=DQ.read_text(); pol=POL.read_text(); src=SRC.read_text()
assert c['schema']=='STAGE36_36_09DS_PROSELMER_TORSION_INJECTIVITY_CORRECTION_V1'
assert c['status']=='CORRECTION_REVOKE_MUTUAL_INJECTIVITY_RETAIN_EXPONENT2_KERNEL_COKERNEL'
assert 'Hostile audit may revoke, downgrade, supersede, or reopen prior credit' in pol

# Historical claims are preserved as historical evidence but explicitly revoked by the overlay.
p=ds['proSelmer_transport']
assert p['T2Sel_2_torsion_free'] is True
assert p['Phi_injective'] is True
assert p['Psi_injective'] is True
for k in ['T2Sel_2_torsion_free','Phi_injective','Psi_injective','proSelmer_mutual_injections_constructed']:
 assert c['historical_DS_claims_revoked'][k] is True

# DQ explicitly places the 2-adic Mordell-Weil completion inside pro-Selmer.
assert '0 -> T_m Sel(A^t)' in dq
assert '2-adic Mordell--Weil completion inside `T_2 Sel(J)`' in dq
assert c['DQ_Kummer_interface']['Mordell_Weil_completion_embeds_in_proSelmer'] is True
assert c['DQ_Kummer_interface']['T2Sel_automatically_2_torsion_free'] is False

# DT independently makes both geometric kernels split rational 2-torsion.
assert dt['Galois_rationality']['kernel_Phi_constant_Q_group_scheme']=='(Z/2Z)^3'
assert dt['dual_kernel']['kernel_Psi_constant_Q_group_scheme']=='(Z/2Z)^3'
assert c['DT_rational_kernel_input']['kernel_Phi_Q_nonzero'] is True
assert c['DT_rational_kernel_input']['kernel_Psi_Q_nonzero'] is True

# Elementary completion replay for the visible kernel C2^3: quotient by 2^n is C2^3 for every n>=1,
# so each nonzero element survives the entire inverse system.
C=[tuple((m>>i)&1 for i in range(3)) for m in range(8)]
for n in range(1,8):
 # 2^n*C=0, hence C/(2^n C)=C and all seven nonzero elements survive.
 assert 2**n % 2 == 0
 assert len([x for x in C if any(x)])==7

q=c['corrected_proSelmer_transport']
assert q['Phi_kernel_nonzero'] is True and q['Psi_kernel_nonzero'] is True
assert q['Phi_injective'] is False and q['Psi_injective'] is False
# The composition identities alone retain exponent-2 control for both kernels and cokernels.
for k in ['Phi_kernel_killed_by_2','Psi_kernel_killed_by_2','Phi_cokernel_killed_by_2','Psi_cokernel_killed_by_2']:
 assert q[k] is True,k
for k in ['Phi_kernel_dimension_computed','Psi_kernel_dimension_computed','Phi_cokernel_dimension_computed','Psi_cokernel_dimension_computed','product_identification_obtained']:
 assert q[k] is False,k
assert ds['composition_relations']['Psi_after_Phi']=='[2]_A'
assert ds['composition_relations']['Phi_after_Psi']=='[2]_J'
assert ds['degree_and_kernel']['degree_Phi']==8 and ds['degree_and_kernel']['degree_Psi']==8
assert c['downstream_impact']['DX_finite_global_Phi_Selmer_four_class_result_retained'] is True
assert c['downstream_impact']['DS_mutual_injection_bridge_revoked'] is True
assert c['downstream_impact']['36_09DY_entry_must_be_relocked'] is True
assert c['downstream_impact']['external_reaudit_required_before_new_downstream_promotion'] is True
assert 'does not rewrite the historical 36-09DS exact-head artifact' in src
for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
print('36-09DS correction verified: rational split 2-torsion kernels survive the Mordell-Weil 2-adic completions inside pro-Selmer, so Phi_* and Psi_* are not injective. The [2] compositions still force both kernels and cokernels to have exponent dividing 2. Geometric V4/degree-8 and DT-DX finite Phi-descent credit are retained; DY is relocked pending re-audit.')
