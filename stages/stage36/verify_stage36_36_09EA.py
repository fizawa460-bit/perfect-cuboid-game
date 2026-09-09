#!/usr/bin/env python3
import json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09EA/fixed-p2-defect-aware-retained-open-intersection-preflight.json'
SRC=ROOT/'stages/stage36/36-09EA/defect-aware-retained-open-intersection-source-lock.md'
DQ=ROOT/'stages/stage36/36-09DQ/global-2primary-adelic-annihilator-proselmer-source-lock.md'
DR=ROOT/'stages/stage36/36-09DR/fixed-p2-v4-elliptic-quotient-proselmer-reduction-preflight.json'
DS=ROOT/'stages/stage36/36-09DS/v4-isogeny-norm-pullback-proselmer-source-lock.md'
CORR=ROOT/'stages/stage36/36-09DS/proselmer-torsion-injectivity-correction.json'
DZ=ROOT/'stages/stage36/36-09DZ/fixed-p2-mw-phi-quotient-preflight.json'
DZV=ROOT/'stages/stage36/verify_stage36_36_09DZ.py'
LOCKS={
 CERT:'aea5c84bb2721a92759e4143f5199f607a31637d',
 SRC:'fe3fe4b5a8341159f347b6f8fc3d083aeccdf926',
 DQ:'71829ec5e0af601605f1f93c5f3a3fec4cae2102',
 DR:'c212f0430fb5b4d04ee0887e303a73fb303657c8',
 DS:'1bac0039c0abccc236b392c2deba3a26ee83ba88',
 CORR:'d3318c8291835de8011f6b72fea8ca4479c3107d',
 DZ:'5fb697e6d450ab46adde1a4a40cde9c415e4cd90',
 DZV:'c7a8edc23e7d1f3438ec658fd7d23c8b79587dad',
}
def gh(p): return subprocess.check_output(['git','hash-object',str(p)],cwd=ROOT,text=True).strip()
for p,h in LOCKS.items(): assert gh(p)==h,(p,gh(p),h)

c=json.loads(CERT.read_text()); dr=json.loads(DR.read_text()); corr=json.loads(CORR.read_text()); dz=json.loads(DZ.read_text()); dq=DQ.read_text(); ds=DS.read_text(); src=SRC.read_text()
assert c['schema']=='STAGE36_36_09EA_FIXED_P2_DEFECT_AWARE_RETAINED_OPEN_INTERSECTION_PREFLIGHT_V1'
assert c['status']=='PASS_EXACT_FOUR_COSET_PROSELMER_INTERSECTION_REPRESENTATIVES_NOT_MATERIALIZED'
assert c['base_main_sha']=='9346a1b0cfdb6f2e8abe93b4aef9987698eeeb47'
for key,item in c['source_locks'].items():
    p=ROOT/item['path']; assert gh(p)==item['blob_sha'],(key,gh(p),item['blob_sha'])

# DQ is the exact retained-open / full 2-primary Brauer interface.
assert 'iota_hat_2(U_ret(A_Q)) intersect image(T_2 Sel(J))' in dq
assert 'if and only if' in dq
assert c['retained_open_criterion']['DQ_Brauer_interface_consumed'] is True

# Retained V4 geometry defines the actual product A and pullback-sum Phi.
assert dr['isogeny_result']['Q_isogeny_constructed'] is True
assert 'A = E_tau x E_sigma x E_rho' in ds
assert 'Phi(a_tau,a_sigma,a_rho) = pi_tau^* a_tau + pi_sigma^* a_sigma + pi_rho^* a_rho' in ds
# Historical mutual injectivity remains revoked; EA must not reintroduce it.
for k in ['Phi_injective','Psi_injective','proSelmer_mutual_injections_constructed']:
    assert corr['historical_DS_claims_revoked'][k] is True

# DZ exact defect data: rational MW quotient exhausts the Phi pro-Selmer cokernel.
e=dz['exact_proSelmer_defect']; rq=dz['rational_isogeny_quotients']; sh=dz['finite_isogeny_Sha_kernels']
assert e['Phi_cokernel_F2_dimension']==2 and e['Phi_cokernel_cardinality']==4
assert rq['Phi_MW_quotient_F2_dimension']==2 and rq['Phi_MW_quotient_cardinality']==4
assert sh['Sha_A_Phi_trivial'] is True
assert c['exact_isogeny_defect_input']['Phi_cokernel_F2_dimension']==2
assert c['exact_isogeny_defect_input']['Phi_cokernel_cardinality']==4
assert c['exact_isogeny_defect_input']['JQ_mod_PhiAQ_F2_dimension']==2
assert c['exact_isogeny_defect_input']['JQ_mod_PhiAQ_cardinality']==4
assert c['exact_isogeny_defect_input']['T2Sha_cokernel_contribution_to_Phi_cokernel']==0
assert c['exact_isogeny_defect_input']['MW_quotient_maps_isomorphically_to_proSelmer_cokernel'] is True

# Abstract quotient replay: F2^2 has exactly four cosets/classes and admits zero as a representative.
Q=[(a,b) for a in (0,1) for b in (0,1)]
assert len(Q)==4 and (0,0) in Q
cd=c['coset_decomposition']
assert cd['representative_set_cardinality']==len(Q)
assert cd['representatives_exist_in_JQ'] is True
assert cd['zero_representative_may_be_chosen'] is True
assert cd['representatives_materialized'] is False
assert cd['abstract_identity']=='T2Sel(J)=union_{r in R}(r+Phi_*T2Sel(A))'
assert cd['prelocalization_cosets_distinct'] is True
assert cd['postlocalization_cosets_claimed_distinct'] is False

# Product identity is asserted only for the literal product A, never for J.
ep=c['elliptic_product_side']
assert ep['A_literal_product']=='E_tau x E_sigma x E_rho'
assert ep['finite_level_Selmer_product_identity'] is True
assert ep['proSelmer_product_identity_for_A'] is True
assert ep['T2Sel_A_identity']=='T2Sel(E_tau) x T2Sel(E_sigma) x T2Sel(E_rho)'
assert ep['T2Sel_J_identified_with_product'] is False
assert 'This is not an identification of `T_2 Sel(J)` with an elliptic product' in src

# Localization is functorial and retains all four translations.
ad=c['adelic_image_decomposition']; rc=c['retained_open_criterion']
assert ad['localization_functorial_for_Phi'] is True
assert ad['four_translated_images_exact'] is True
assert rc['number_of_global_defect_cosets']==4
assert rc['exact_four_coset_intersection_reduction'] is True
assert rc['individual_coset_intersections_decided'] is False
assert 'pi_tau^*loc(s_tau)' in rc['criterion']
assert c['route_result']['next_leaf']=='36-09EB_FIXED_P2_PHI_COSET_REPRESENTATIVE_PREFLIGHT'
for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
print('36-09EA verified: DZ coker(Phi_*)=J(Q)/Phi A(Q)=F2^2 yields an exact four-rational-coset decomposition of loc T2Sel(J); only the literal product A is decomposed into elliptic pro-Selmer factors. The retained-open Br(2) problem is exactly four translated intersections. Representatives and all downstream credit remain unresolved.')
