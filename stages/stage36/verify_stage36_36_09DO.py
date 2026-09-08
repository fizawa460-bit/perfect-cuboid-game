#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DO/fixed-p2-2primary-full-brauer-relevance-boundary-preflight.json'
SRC=ROOT/'stages/stage36/36-09DO/full-2primary-q2-formal-neighborhood-boundary-source-lock.md'
DN=ROOT/'stages/stage36/36-09DN/fixed-p2-full-br2-common-neighborhood-preflight.json'
DNSRC=ROOT/'stages/stage36/36-09DN/full-br2-local-common-neighborhood-source-lock.md'
BASE='e98b06455d34bf2f346d297d9370e82fc2a71970'
DN_GREEN='6d8d65b9215ef9eba148370342922092aa36a084'
DN_REPLAY='56b59e4d43529ecc77b2cd3e0ad30c1a9ea6d038'
LOCKS={
 CERT:'db5368da5162014e8fae767c778d6ddb0c2180e0',
 SRC:'4529177bbe39401ed93c0395cce66176bf451dc8',
 DN:'bffce7f0e27a9f92f12657bcca1b71cddce7ccaa',
 DNSRC:'60984a1f42b999e770219398690e833b54c8eb0f',
}

def git(*args:str)->str:
 return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
def blob(path:Path)->str:
 return git('hash-object',str(path.relative_to(ROOT)))

def main()->None:
 for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
 for h in [BASE,DN_GREEN,DN_REPLAY]:
  subprocess.check_call(['git','merge-base','--is-ancestor',h,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text()); dn=json.loads(DN.read_text()); src=SRC.read_text(); dns=DNSRC.read_text()
 assert c['base_main_sha']==BASE
 assert c['batch_parent']['36_09DN_exact_green_head']==DN_GREEN
 assert c['batch_parent']['36_09DN_exact_head_ci']=='34226894499/102063100388'
 assert c['batch_parent']['36_09DN_promotion_replay_head']==DN_REPLAY
 assert c['batch_parent']['36_09DN_promotion_replay_ci']=='34227100485/102063780519'
 assert c['source_locks']['stage36_36_09DN']['blob_sha']==LOCKS[DN]
 assert c['source_locks']['stage36_36_09DN_source']['blob_sha']==LOCKS[DNSRC]
 assert c['source_locks']['local_2primary_boundary']['blob_sha']==LOCKS[SRC]

 # DN parent remains exact-green only at exponent 2.
 assert dn['global_Br2_consequence']['full_Br2_Brauer_set_nonempty'] is True
 assert dn['local_constancy_uniformization']['uniform_for_all_2primary_classes'] is False
 assert 'finite-intersection argument' in dns
 assert 'does not intersect class-dependent neighborhoods over the full infinite Brauer group or over all `2^n`-primary torsion' in dns

 # Source theorem and structural locks.
 assert 'Lichtenbaum' in src and '10.1007/BF01389795' in src
 assert 'Mattuck' in src and '10.2307/2007101' in src and 'Theorem 7' in src
 assert 'Milne' in src and 'local duality for abelian varieties' in src
 assert 'M ~= Z_2^3' in src
 assert 'intersection_{n>=1} 2^n J(Q_2)' in src
 assert 'no punctured analytic neighborhood of P0' in src
 assert 'does **not** show that every separating local class is the localization of a global class' in src

 fc=c['fixed_curve']; ds=c['dyadic_local_structure']; fr=c['formal_neighborhood_result']; oc=c['odd_place_comparison']; gl=c['global_localization_firewall']
 assert fc['genus']==3 and fc['jacobian_dimension']==3
 assert fc['reference_point']=={'name':'P0','t':0,'z':1,'rational':True,'smooth':True,'retained_open':False}
 assert ds['field']=='Q_2'
 assert ds['all_2primary_annihilator']=='intersection_{n>=1} 2^n J(Q_2)'
 assert ds['all_2primary_annihilator_intersection_M']=='{0}'
 assert ds['every_nonzero_x_in_M_detected_by_some_2power_character'] is True
 assert fr['locally_injective_at_P0'] is True
 assert fr['punctured_common_neighborhood_for_all_local_2primary_classes_exists'] is False
 assert fr['DN_finite_intersection_method_extends_to_full_local_2primary_at_Q2'] is False
 assert oc['for_odd_p_open_formal_subgroup_is_pro_p'] is True
 assert oc['continuous_2primary_characters_kill_open_pro_p_subgroup'] is True
 assert oc['unique_structural_unbounded_exponent_place']=='Q_2'
 assert gl['local_separating_class_need_not_globalize'] is True
 assert gl['global_2primary_Brauer_set_nonempty'] is False
 assert gl['global_2primary_Brauer_set_empty'] is False
 assert gl['fixed_p2_exclusion_obtained'] is False
 assert gl['first_missing_obligation']=='GLOBAL_2PRIMARY_BRAUER_Q2_LOCALIZATION_IMAGE_BOUNDEDNESS_OR_SEPARATION'

 assert c['route_result']['next_leaf']=='36-09DP_FIXED_P2_GLOBAL_2PRIMARY_BRAUER_Q2_LOCALIZATION_IMAGE_PREFLIGHT'
 cb=c['current_credit_boundary']
 assert cb['full_Br2_Brauer_set_nonempty'] is True
 assert cb['full_Br2_Brauer_Manin_obstruction_disproved'] is True
 for k in ['full_2primary_Brauer_set_nonempty','full_2primary_Brauer_set_empty','full_Brauer_set_nonempty','full_Brauer_set_empty','Brauer_Manin_obstruction_obtained','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
  assert cb[k] is False,k
 for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
 print('36-09DO verified: the exponent-2 DN common-neighborhood method cannot extend to the entire local 2-primary Brauer group at Q2. Mattuck gives a torsion-free open Z_2^3 subgroup of J(Q2), and local Tate/Lichtenbaum duality separates every nonzero sufficiently small Abel-Jacobi displacement by some 2-power local character. This is only a local no-go: globalization of the separating characters is unresolved, so full 2-primary BM/fixed-p/receiver/endpoint credit remains closed.')

if __name__=='__main__': main()
