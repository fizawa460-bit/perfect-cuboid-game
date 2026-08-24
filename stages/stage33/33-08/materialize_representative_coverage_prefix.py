#!/usr/bin/env python3
"""Rebuild the Stage33-08 direct representative prefix after Stage33-07 re-audit.

Stage33-07 no longer supplies a complete Q-defined global BR0G class list.
This leaf therefore records only direct representatives and exact boundary
residue families whose arithmetic Q-lift remains the named HS-descent kernel.
"""
import hashlib, io, json, os, urllib.parse, urllib.request, zipfile
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
S33=HERE.parent
REPO="fizawa460-bit/perfect-cuboid-game"
BR0G_ARTIFACT_ID=9513712470
BR0G_ARTIFACT_SHA256="4ef12f7686e0b251bbfbcc3f0c3f0c44c61db0e0fca7dbb94afcdc5f0fbfb637"
KERNEL="R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT"

def load(p): return json.loads(p.read_text(encoding='utf-8'))
class R(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,h,newurl):
  n=super().redirect_request(req,fp,code,msg,h,newurl)
  if n is not None and urllib.parse.urlsplit(req.full_url).netloc!=urllib.parse.urlsplit(newurl).netloc:n.remove_header('Authorization')
  return n

def dl():
 t=os.environ.get('GITHUB_TOKEN')
 if not t: raise SystemExit('GITHUB_TOKEN required')
 req=urllib.request.Request(f'https://api.github.com/repos/{REPO}/actions/artifacts/{BR0G_ARTIFACT_ID}/zip',headers={'Authorization':f'Bearer {t}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'perfect-cuboid-stage33/5.0'})
 with urllib.request.build_opener(R()).open(req,timeout=90) as r:b=r.read()
 if hashlib.sha256(b).hexdigest()!=BR0G_ARTIFACT_SHA256: raise SystemExit('BR0G artifact digest mismatch')
 return zipfile.ZipFile(io.BytesIO(b))

ctl=load(S33/'controller.json')
s07=load(S33/'33-07'/'audit-state.json')
j2_source=(S33/'33-05'/'j2_arithmetic_descent.py').read_text(encoding='utf-8')
assert ctl['stage33_progress']=='6/11'
assert ctl['stage33_07']['unit_status']=='BLOCKED_NEW_KERNEL'
assert not ctl['stage33_08_released']
assert s07['unit_status']=='BLOCKED_NEW_KERNEL'
assert s07['new_kernel_id']==KERNEL
assert s07['j2']['q_defined'] and s07['j2']['endpoint_pullback_nonzero']

for needle in (
 'L=Q(t)[alpha]/(t^2*(1-alpha^2)^2+alpha^2*(1-t^2)^2)',
 'ell_J2=4*(alpha^2*t^2+t^4-4*t^2+2)/',
 'Cor_{L(C)/Q(t)(C)}((ell_J2, s-alpha)_2)'):
 if needle not in j2_source: raise SystemExit(f'J2 source-lock missing: {needle}')

with dl() as z:
 linear=json.loads(z.read('linear-factor-unit-lifts.json'))
 us=json.loads(z.read('unit-symbol-residue-span.json'))
 tp=json.loads(z.read('two-primary-prime-power-gersten-descent.json'))
 bg=json.loads(z.read('boundary-galois.json'))

M=sp.Matrix([r['coordinates_in_audited_U_D_basis'] for r in linear['ratio_lifts']])
assert M.shape==(17,14) and int(M.rank())==11
assert us['unit_divisor_lattice_rank']==14
assert us['unit_symbol_secondary_residue_span_rank_f2']==44
assert tp['order4_generator_count']==12
assert tp['two_primary_ramified_crossing_module']=='(Z/2)^49 direct_sum (Z/4)^12'
assert len(bg['arithmetic_component_orbits'])==60

j2={
 'class_id':'J2','primary_order':2,'provenance':'BR2_K3','field_of_definition':'Q',
 'symbol_or_algebra_representative':'Cor_{L(C)/Q(t)(C)}((ell_J2,s-alpha)_2), ell_J2=4*(alpha^2*t^2+t^4-4*t^2+2)/((t^2-1)*(t^2-2*t-1))',
 'proper_unramified_class':True,'endpoint_pullback_nonzero':True,
 'q2_evaluation_nonconstant':True,'q2_invariants_observed':['0','1/2'],
 'exact_evaluable_representative_on_dense_chart':True,'physical_open_patch_cover_complete':False
}

cert={
 'schema':'STAGE33_08_REPRESENTATIVE_COVERAGE_PREFIX_V2_REAUDIT_AWARE',
 'stage33_unit':'33-08',
 'source_locks':{
  'stage33_07_reaudit_state':'stages/stage33/33-07/audit-state.json',
  'stage33_05_j2_source':'stages/stage33/33-05/j2_arithmetic_descent.py',
  'stage33_04_audited_artifact_id':BR0G_ARTIFACT_ID,
  'stage33_04_audited_artifact_sha256':BR0G_ARTIFACT_SHA256,
 },
 'stage33_07_complete_q_defined_class_list_currently_authoritative':False,
 'stage33_07_effective_status':'BLOCKED_NEW_KERNEL',
 'new_kernel_id':KERNEL,
 'boundary_residue_data_retained':{
  'arithmetic_component_orbits':60,
  'unit_symbol_rank_f2':44,
  'finite_ramified_boundary_residue_module':'(Z/2)^49 direct_sum (Z/4)^12',
  'global_q_lifts_certified':False
 },
 'j2_exact_evaluable_representative_materialized':True,
 'j2':j2,
 'seven_line_endpoint_block':'0',
 'predecessor_explicit_linear_factor_ratio_count':17,
 'predecessor_explicit_linear_factor_ratio_rank_in_U_D':11,
 'full_unit_lattice_rank':14,
 'full_rank14_explicit_q_unit_lattice_replay_required':True,
 'direct_prefix_can_continue_independently':True,
 'every_stage33_07_relevant_class_accounted':False,
 'every_surviving_class_has_primary_order_and_provenance':False,
 'every_surviving_class_has_exact_evaluable_representative':False,
 'ramification_support_complete':False,
 'denominator_support_complete':False,
 'equivalence_independence_certificates_complete':False,
 'physical_open_domain_certified':False,
 'unresolved_unknown_in_scope':1,
 'br2b':'BLOCKED_NEW_KERNEL','unit_status':'BLOCKED_NEW_KERNEL','unit_closed':False,'downstream_released':False,
 'stage33_progress':'6/11','stage33_09_released':False,
 'next_exact_leaf':'L33-07-REPAIR-COMPUTE-ARITHMETIC-HS-DESCENT-OF-BR0G-RESIDUE-LIFTS',
 'next_expected_command':'Stage33-main-batch','theorem_credit':False,'endpoint_credit':False,
 'brauer_manin_set_empty_proved':False,'perfect_cuboid_nonexistence_claim':False
}
raw=json.dumps(cert,sort_keys=True,separators=(',',':')).encode();cert['canonical_sha256']=hashlib.sha256(raw).hexdigest()
(HERE/'representative-coverage-prefix.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
print(json.dumps({'success':True,'STAGE33_07_COMPLETE_Q_LIST':False,'J2_DIRECT_REPRESENTATIVE':True,'BOUNDARY_RESIDUE_DATA_RETAINED':True,'NEW_KERNEL':KERNEL,'STAGE33_PROGRESS':'6/11','certificate_sha256':cert['canonical_sha256']},indent=2,sort_keys=True))
