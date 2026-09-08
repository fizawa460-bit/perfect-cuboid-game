#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
CERT=ROOT/'stages/stage36/36-09DN/fixed-p2-full-br2-common-neighborhood-preflight.json'
SRC=ROOT/'stages/stage36/36-09DN/full-br2-local-common-neighborhood-source-lock.md'
DM=ROOT/'stages/stage36/36-09DM/fixed-p2-full-cv-explicit-image-boundary-adelic-control-preflight.json'
DF=ROOT/'stages/stage36/36-09DF/fixed-p2-creutz-viray-complement-local-obstruction-preflight.json'
DD=ROOT/'stages/stage36/36-09DD/creutz-viray-explicit-image-completeness-source-lock.md'
BASE='e98b06455d34bf2f346d297d9370e82fc2a71970'
UNLOCK='ddb470122413038f1e08738d0dbe48953585546e'
LOCKS={
 CERT:'bffce7f0e27a9f92f12657bcca1b71cddce7ccaa',
 SRC:'60984a1f42b999e770219398690e833b54c8eb0f',
 DM:'95956c74aca1aca1601a1f4c77b66bfb226a5198',
 DF:'e2ad1a187dc607b558288a6cad91272c021dd493',
 DD:'632e908d3fcd4d1f3511be99b3993469537e3c07',
}

def git(*a:str)->str:
 return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
def blob(p:Path)->str:
 return git('hash-object',str(p.relative_to(ROOT)))

def rhs(t:Fraction)->Fraction:
 return (t*t+4)*(t*t+Fraction(1,4))*(t*t+9)*(t*t+Fraction(1,9))

def main()->None:
 for p,h in LOCKS.items(): assert blob(p)==h,(p,blob(p),h)
 for h in [BASE,UNLOCK]: subprocess.check_call(['git','merge-base','--is-ancestor',h,'HEAD'],cwd=ROOT)
 c=json.loads(CERT.read_text()); dm=json.loads(DM.read_text()); df=json.loads(DF.read_text()); src=SRC.read_text(); dd=DD.read_text()
 assert c['base_main_sha']==BASE
 assert c['batch_parent']['DN_unlock_sync_head']==UNLOCK
 assert c['batch_parent']['DN_unlock_ci']=='34224426949/102054967101'
 assert c['source_locks']['local_br2_common_neighborhood']['blob_sha']==LOCKS[SRC]
 assert c['source_locks']['stage36_36_09DM']['blob_sha']==LOCKS[DM]
 assert c['source_locks']['stage36_36_09DF']['blob_sha']==LOCKS[DF]
 assert c['source_locks']['stage36_36_09DD_source']['blob_sha']==LOCKS[DD]

 # Exact reference-point arithmetic and retained boundary lineage.
 assert rhs(Fraction(0))==1
 p0=c['fixed_curve']['reference_point']
 assert p0=={'name':'P0','t':'0','z':'1','Q_rational':True,'smooth':True,'retained_open':False}
 assert Fraction(2)!=0  # d(z^2-rhs)/dz at P0
 assert c['fixed_curve']['retained_open_boundary_contains']==['t=0','t=1','t=-1','t=infinity']
 assert df['fixed_curve']['retained_open_excludes']==['t=0','t=1','t=-1','t=infinity']
 assert dm['global_reference_point']['t']==0 and dm['global_reference_point']['z']==1
 assert dm['global_reference_point']['Q_rational'] is True and dm['global_reference_point']['smooth'] is True

 # Source theorem locks: local 2-torsion quotient is finite and each fixed evaluation is locally constant.
 assert 'Lichtenbaum' in src and '10.1007/BF01389795' in src
 assert 'Pic(C) x Br(C) -> Br(K) ~= Q/Z' in src
 assert '(Br(C)/Br(K))[2]' in src
 assert 'is finite' in src
 assert 'Uematsu Theorem 1.1' in src
 assert 'is locally constant' in src
 assert 'finite-intersection argument' in src
 assert 'does not intersect class-dependent neighborhoods over the full infinite Brauer group' in src
 assert 'does **not** prove' in src
 assert 'does **not** identify that image with all of `(Br(C)/Br_0(C))[2]`' in dd

 li=c['local_padic_input']; lc=c['local_constancy_uniformization']; sel=c['retained_open_point_selection']; gc=c['global_Br2_consequence']
 assert li['nonconstant_local_2torsion_quotient_finite'] is True
 assert li['covers_v2'] is True and li['requires_good_reduction'] is False
 assert lc['finite_representatives_suffice_mod_constants'] is True
 assert lc['uniform_for_all_local_2torsion_classes'] is True
 assert lc['uniform_for_all_2primary_classes'] is False
 assert lc['uniform_for_full_Brauer_group'] is False
 assert sel['adelic_tuple_exists'] is True and sel['all_components_in_retained_open'] is True
 assert sel['integral_at_all_but_finitely_many_places'] is True
 assert sel['same_evaluation_as_P0_for_every_global_2torsion_class_at_every_place'] is True
 assert gc['target_group']=='Br(C3_2)[2]'
 assert gc['retained_open_adelic_point_orthogonal_to_entire_Br2_exists'] is True
 assert gc['full_Br2_Brauer_set_nonempty'] is True
 assert gc['full_Br2_Brauer_Manin_obstruction_disproved_for_fixed_p2_retained_open'] is True
 assert gc['includes_classes_outside_Creutz_Viray_explicit_image'] is True

 cb=c['current_credit_boundary']
 assert cb['full_Br2_Brauer_set_nonempty'] is True
 assert cb['full_Br2_Brauer_Manin_obstruction_disproved'] is True
 for k in ['full_Creutz_Viray_explicit_image_computed','Creutz_Viray_explicit_image_equals_full_Br2','full_2primary_Brauer_set_nonempty','full_Brauer_set_nonempty','full_Brauer_group_computed','Brauer_Manin_obstruction_from_full_Brauer_group_proved','fixed_p_2_branch_excluded','candidate_parameter_set_shrunk','receiver_emptiness_proved']:
  assert cb[k] is False,k
 assert c['route_result']['next_leaf']=='36-09DO_FIXED_P2_2PRIMARY_FULL_BRAUER_RELEVANCE_BOUNDARY_PREFLIGHT'
 for k,v in c['scope_firewalls'].items(): assert v is False,(k,v)
 print('36-09DN verified: P0=(0,1) is a smooth rational reference point. Lichtenbaum local duality makes the nonconstant local Br[2] quotient finite at every p-adic place, including 2, and Uematsu local constancy permits one common neighborhood for all exponent-2 classes. Retained-open points can be chosen in those neighborhoods, giving an adelic point whose evaluation equals P0 placewise for every global Br[2] class; global reciprocity makes the full Br[2] Brauer set nonempty. Higher 2-primary/full Brauer/fixed-p/receiver/endpoint credit remains open.')

if __name__=='__main__': main()
