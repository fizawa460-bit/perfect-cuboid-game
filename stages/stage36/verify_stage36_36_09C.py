#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
STATE=ROOT/'stages/stage36/MAIN-STATE.json'
CERT=ROOT/'stages/stage36/36-09C/single-place-direct-receiver-obstruction-preflight.json'
CERT_BLOB='67fd5cd61ef35582dce32811aac4bebdb9356138'
BASE='7b7971cc12bb0c9046a13a9ba956d73392178d72'
SCHEMA='STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V18_36_09C_PENDING_HOSTILE_AUDIT'
SOURCES={
 'stage29_exact_sign_cover_model':('stages/stage29/29-02ha/exact-sign-cover-model.md','fc2d5284a259750f45d2d756a952002671e3bccc'),
 'stage36_36_02_representatives':('stages/stage36/36-02/representative-inventory.json','88130b9380a677a191f91c24df87618e65be0a2f'),
 'stage36_36_03_physical_receiver':('stages/stage36/36-03/physical-open-boundary.json','fc1947b2de08f7d8a104bdc91902b20e88635349'),
 'stage36_36_04_torsor_class':('stages/stage36/36-04/h-torsor-lift-class.json','a06e201a9b554da71c5e75d8f8541e7284f8d020'),
 'stage36_36_09_breadth_gate':('stages/stage36/36-09/replacement-breadth-gate.json','0c6019d70346b531a9b703d6f74e346302273655'),
 'stage36_36_09B_preflight':('stages/stage36/36-09B/receiver-restricted-branch-intersection-preflight.json','da9143e587506522ed966d380d9980ff1875db0d'),
 'cycle_safety_protocol':('docs/research-os/policies/cycle-exploration-safety-protocol.md','4e911c4fc7e4ea7a2b5f96733a90b986ef8d9a37'),
}
ARSENAL={
 'router':('docs/arsenal/index.json','aa45d19c2f1d8970c7f142bf744c5c17e75abe5a'),
 'S30-WF02':('docs/arsenal/cards/workflows/S30-WF02.md','38e4625155eb079bbe3d50d663c6256559319886'),
 'S30-WF03':('docs/arsenal/cards/workflows/S30-WF03.md','12740198aba19ade18302819f8e890dbda4eb701'),
 'S34-WF01':('docs/arsenal/cards/workflows/S34-WF01.md','1ebba4ec402e14d536284a06c5ac32625c6b8cec'),
}

def blob_sha(p:Path)->str:
 b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def req(ok:bool,msg:str)->None:
 if not ok: raise SystemExit(msg)

def main()->None:
 req(blob_sha(CERT)==CERT_BLOB,'36-09C certificate blob drift')
 c=json.loads(CERT.read_text())
 req(c.get('schema')=='STAGE36_36_09C_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION_PREFLIGHT_V1','36-09C schema moved')
 req(c.get('base_main_sha')==BASE,'36-09C base moved')
 entry=c.get('entry_authority',{})
 req(entry=={'stage36_36_09B_promotion_pr':1585,'promotion_exact_head':'1d29735f3f50c6918a32b2542de8364b86568396','promotion_exact_head_ci_run':33953819230,'promotion_exact_head_ci_job':101273378060,'promotion_merged_main_sha':BASE,'selected_route':'36-09C_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION_PREFLIGHT'},'36-09C entry authority moved')
 for k,(rel,sha) in SOURCES.items():
  req(c.get('source_locks',{}).get(k)=={'path':rel,'blob_sha':sha},f'36-09C source declaration moved: {k}')
  req(blob_sha(ROOT/rel)==sha,f'36-09C source blob drift: {k}')
 for k,(rel,sha) in ARSENAL.items():
  row=c.get('arsenal_locks',{}).get(k,{})
  req(row.get('path')==rel and row.get('blob_sha')==sha,f'36-09C Arsenal declaration moved: {k}')
  req(blob_sha(ROOT/rel)==sha,f'36-09C Arsenal blob drift: {k}')

 # Source model really is the seven simultaneous-square sign cover.
 sign=(ROOT/SOURCES['stage29_exact_sign_cover_model'][0]).read_text()
 for anchor in ['L_{a1}=x','L_{a2}=y','L_{a3}=z','L_{b3}=x+y','L_{b2}=x+z','L_{b1}=y+z','L_c=x+y+z','simultaneous square roots']:
  req(anchor in sign,f'sign-cover anchor moved: {anchor}')

 lemma=c.get('all_place_local_point_lemma',{})
 req(lemma.get('ALL_PLACES_ENDPOINT_OPEN_LOCALLY_SOLUBLE') is True,'all-place endpoint lemma lost')
 req(lemma.get('ALL_PLACES_EACH_AUDITED_RECEIVER_IMAGE_LOCALLY_NONEMPTY') is True,'all-place receiver lemma lost')
 # Real construction.
 real=lemma.get('real_place',{})
 req(real.get('base_point')==[1,1,1] and real.get('seven_line_values')==[1,1,1,2,2,2,3],'real local point moved')
 req(all(v>0 for v in real['seven_line_values']),'real local point lost positivity')
 # Odd-prime symbolic identities. x=p^4,y=p^2,z=1.
 odd=lemma.get('odd_prime_place',{})
 req(odd.get('base_point')=='[x:y:z]=[p^4:p^2:1]','odd-p base point moved')
 req(odd.get('remaining_line_values')=={'x+y':'p^2*(1+p^2)','x+z':'1+p^4','y+z':'1+p^2','x+y+z':'1+p^2+p^4'},'odd-p line identities moved')
 req(odd.get('unit_residues_mod_p')=={'1+p^2':1,'1+p^4':1,'1+p^2+p^4':1},'odd-p Hensel residues moved')
 req('f\'(1)=2' in odd.get('square_unit_lemma','') and 'Hensel' in odd.get('square_unit_lemma',''),'odd-p square lemma moved')
 req(odd.get('all_seven_values_nonzero') is True and odd.get('branch_free') is True,'odd-p branch-free scope moved')
 # p=2 explicit construction and square-unit residues.
 two=lemma.get('prime_2_place',{})
 req(two.get('base_point')==[256,16,1],'2-adic base point moved')
 req(two.get('remaining_line_values')=={'x+y':'16*17','x+z':257,'y+z':17,'x+y+z':273},'2-adic line identities moved')
 req(17%8==257%8==273%8==1,'internal mod-8 arithmetic failure')
 req(two.get('odd_unit_residues_mod_8')=={'17':1,'257':1,'273':1},'2-adic square residues moved')
 req('iff it is 1 mod 8' in two.get('square_unit_lemma',''),'2-adic square lemma moved')
 req(two.get('all_seven_values_nonzero') is True and two.get('branch_free') is True,'2-adic branch-free scope moved')

 phys=json.loads((ROOT/SOURCES['stage36_36_03_physical_receiver'][0]).read_text())
 q=phys.get('global_quotient_chain',{})
 req(q.get('Q_defined') is True and q.get('resolved_H_torsor_finite_etale') is True and q.get('rational_point_pushforward') is True,'36-03 quotient push moved')
 req(phys.get('restricted_receiver_preparation',{}).get('exact_restricted_open')=='U_H=q_H(U) for each audited representative','36-03 restricted receiver moved')
 dec=c.get('single_place_route_decision',{})
 req(dec.get('SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION_POSSIBLE') is False,'single-place route not closed')
 req(dec.get('legal_outcome')=='BLOCKED_SINGLE_PLACE_ROUTE_BY_EXPLICIT_ALL_PLACE_LOCAL_POINTS','36-09C legal outcome moved')
 fire=c.get('local_global_firewall',{})
 for k in ['ONE_GLOBAL_Q_POINT_CONSTRUCTED','SAME_RATIONAL_POINT_USED_AT_ALL_PLACES','BRAUER_MANIN_NONOBSTRUCTION_PROVED','ETALE_BRAUER_NONOBSTRUCTION_PROVED','QUOTIENT_Q_POINT_EXISTENCE_PROVED','ENDPOINT_Q_POINT_EXISTENCE_PROVED']:
  req(fire.get(k) is False,f'36-09C local-global credit leaked: {k}')

 # Three post-breadth distinct blocks force the cycle safety refresh.
 policy=(ROOT/SOURCES['cycle_safety_protocol'][0]).read_text()
 req('three or more materially different attempted routes since the last broad audit' in policy,'cycle breadth trigger moved')
 cyc=c.get('post_block_cycle_audit',{})
 req(cyc.get('EXHAUSTIVE_VIEW_AUDIT') is True and cyc.get('BLIND_REDISCOVERY') is True and cyc.get('blind_generation_before_arsenal_comparison') is True,'36-09C breadth refresh moved')
 req(cyc.get('selected_next_candidate')=='B6_FIBRATION_TO_CURVE_BASE','36-09C next candidate moved')
 led=cyc.get('ledger_after_refresh',{})
 req(led.get('B2_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION')=='BLOCKED_BY_EXPLICIT_ALL_PLACE_LOCAL_POINTS','B2 block moved')
 req(led.get('B6_FIBRATION_TO_CURVE_BASE')=='LIVE','B6 not live')
 req(led.get('B11_DIRECT_MULTIPLACE_ADELIC_RECIPROCITY')=='UNTESTED','new blind B11 silently discarded')
 req(led.get('counts')=={'live':1,'untested':4,'blocked':5,'dominated':1},'36-09C refreshed ledger counts moved')
 req(led.get('split_triggered') is False and led.get('parking_audit_complete') is False,'36-09C split/parking moved')
 req(cyc.get('next_route_after_hostile_audit')=='36-09D_Q_DEFINED_PENCIL_FIBRATION_PREFLIGHT','36-09C successor moved')
 req(all(v is False for v in c.get('claims',{}).values()),'36-09C higher claim leaked')

 s=json.loads(STATE.read_text())
 req(s.get('schema')==SCHEMA and s.get('status')=='ACTIVE_PENDING_HOSTILE_AUDIT' and s.get('base_main_sha')==BASE,'V18 lifecycle moved')
 legacy=s.get('legacy_authority_snapshot',{})
 req(legacy.get('commit')==BASE and legacy.get('blob_sha')=='a6b3c57ef9acd17125f7271a2bb409099618d3ab','V17 snapshot lock moved')
 p=s.get('authority_frontier',{}).get('36-09B-promotion',{})
 req(p.get('pr')==1585 and p.get('exact_head')=='1d29735f3f50c6918a32b2542de8364b86568396' and p.get('exact_head_ci_run')==33953819230 and p.get('exact_head_ci_job')==101273378060 and p.get('merged_main_sha')==BASE,'36-09B promotion provenance moved')
 u=s.get('authority_frontier',{}).get('36-09C',{})
 req(u.get('certificate_blob_sha')==CERT_BLOB and u.get('promotion_status')=='PROVISIONAL_NOT_AUDITED','36-09C provisional authority moved')
 req(u.get('ALL_PLACES_ENDPOINT_OPEN_LOCALLY_SOLUBLE') is True and u.get('SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION_POSSIBLE') is False,'36-09C state result moved')
 req(u.get('EXHAUSTIVE_VIEW_AUDIT') is True and u.get('BLIND_REDISCOVERY') is True,'36-09C state breadth audit moved')
 sc=s.get('cycle_ledger',{})
 req(sc.get('B6_FIBRATION_TO_CURVE_BASE')=='LIVE' and sc.get('B2_SINGLE_PLACE_DIRECT_RECEIVER_OBSTRUCTION')=='BLOCKED_BY_EXPLICIT_ALL_PLACE_LOCAL_POINTS','V18 cycle routing moved')
 req(sc.get('counts')=={'live':1,'untested':4,'blocked':5,'dominated':1},'V18 cycle counts moved')
 cur=s.get('current',{})
 req(cur.get('unit')=='36-09C' and cur.get('36_09D_entry_allowed') is False and cur.get('provisional_successor_after_hostile_audit')=='36-09D_Q_DEFINED_PENCIL_FIBRATION_PREFLIGHT','36-09C hostile boundary moved')
 req(s.get('anti_loop',{}).get('do_not_start_36_09D_before_36_09C_hostile_audit') is True,'36-09D anti-loop moved')
 g=s.get('promotion_gates',{})
 for k in ['uniform_finite_ramification_support_proved','finite_exhaustive_H_twist_family_proved','local_solubility_filter_exhaustive','all_global_survivors_closed','quotient_Q_point_emptiness_proved','receiver_matched_replacement_theorem_proved','R29_CAMP2_closed','Q11_CAMPEDELLI_closed','endpoint_closed','perfect_cuboid_existence_claim','perfect_cuboid_nonexistence_claim']:
  req(g.get(k) is False,f'V18 promotion credit leaked: {k}')
 req(all(v is False for v in s.get('claims',{}).values()),'V18 higher claim leaked')
 print('PASS STAGE36_36_09C_SINGLE_PLACE_DIRECT_RECEIVER_PREFLIGHT')
 print('all places: explicit U(Q_v) point -> every audited q_H(U(Q_v)) nonempty')
 print('single-place emptiness route impossible; no global Q-point/Brauer-Manin credit')
 print('post-three-block breadth refresh PASS; B6 Q-defined pencil fibration selected; 36-09D locked pending hostile audit')
if __name__=='__main__': main()
