#!/usr/bin/env python3
"""Record the all-72 ambient/blowup boundary-function milestone in handoff/result."""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
SIDE=HERE/'mixed-order-side-ambient-function-lifts.json'
EXC=HERE/'mixed-order-exceptional-ambient-tangent-function-lifts.json'
HAND=HERE/'handoff.json'
RESULT=HERE/'result.md'
SIDE_SHA='2f137842fffbabe7fa9f91879f379e0662803204d6753c342fc31f6dfe12fa6d'
EXC_SHA='a9d5ceb66625dfa561db61a3afc95388bf5a8371fb81905988991514a765d397'
NEXT_KERNEL='R33-BR2A-26-AMBIENT-BOUNDARY-FUNCTION-PACKAGES-GLOBAL-GERSTEN-OFF-BOUNDARY-RESIDUES'
NEXT_LEAF='L33-07-ASSEMBLE-26-AMBIENT-BOUNDARY-PACKAGES-AND-CERTIFY-OFF-BOUNDARY-CODIM1-RESIDUES'

def load(path,sha):
    x=json.load(open(path)); assert x['canonical_sha256']==sha
    return x
side=load(SIDE,SIDE_SHA); exc=load(EXC,EXC_SHA)
assert side['counts']['source_count']==26 and side['counts']['nontrivial_source_side_function_count']==120
assert exc['counts']['source_count']==26 and exc['counts']['exceptional_component_count']==48
assert exc['counts']['nontrivial_source_exceptional_function_count']==120
assert exc['constructive_progress']['all_72_boundary_component_function_packages_have_explicit_ambient_or_blowup_rational_lifts']

h=json.load(open(HAND))
h['schema']='STAGE33_07_REAUDIT_BLOCKED_HANDOFF_V10_ALL72_AMBIENT_BOUNDARY_GLOBAL_GERSTEN_GAP'
h['smallest_current_exact_kernel']=NEXT_KERNEL
h['next_item']=NEXT_LEAF
h['retained_exact_prefix']['all_24_side_component_first_residue_functions_have_ambient_surface_rational_lifts']=True
h['retained_exact_prefix']['all_48_exceptional_component_first_residue_functions_have_ambient_blowup_rational_lifts']=True
h['retained_exact_prefix']['all_72_boundary_component_function_packages_have_explicit_ambient_or_blowup_rational_lifts']=True
r=h['repair_exact_reduction']
r['side_ambient_function_lifts_materialized_nontrivial']=120
r['side_ambient_selected_crossing_factors']=240
r['exceptional_ambient_tangent_function_lifts_materialized_nontrivial']=120
r['exceptional_ambient_selected_crossing_factors']=240
r['all_72_boundary_component_function_packages_ambientized']=True
r['global_geometric_Gersten_lifts_materialized']=0
r['global_geometric_Gersten_lifts_required']=26
r['off_boundary_codimension1_residue_certificates_materialized']=0
h['ambient_boundary_function_lift_evidence']={
  'side':{'producer':'materialize_mixed_order_side_ambient_function_lifts.py','certificate_sha256':SIDE_SHA,'source_count':26,'nontrivial_functions':120,'selected_crossing_factors':240,'workflow_run':33057410798,'artifact_id':9640210685,'artifact_zip_sha256':'057c63d1f823d7a9bd1f23676f36f32606dfc8cf85a865ebdeeb67dd4953795e','actions_validation':'PASS'},
  'exceptional':{'producer':'materialize_mixed_order_exceptional_ambient_tangent_function_lifts.py','certificate_sha256':EXC_SHA,'source_count':26,'exceptional_models':48,'nontrivial_functions':120,'selected_crossing_factors':240,'workflow_run':33057660173,'artifact_id':9640318609,'artifact_zip_sha256':'3cb9271b729b37b975b9fbd5117d1e74335be816296a5461a3a13ddf589a52dd','actions_validation':'PASS'},
  'all_72_boundary_components_ambient_or_blowup_lifted':True,
}
m=h['order2_localization_missing_exact_inputs']
m['all_72_boundary_component_function_packages_ambientized']=True
m['off_boundary_codimension1_residue_certificates_for_26_global_lifts']=False
m['global_geometric_Gersten_lifts_for_all_26_sources']=False
assert h['stage33_progress']=='6/11' and not h['stage33_08_released']
assert not h['theorem_credit'] and not h['endpoint_credit']
HAND.write_text(json.dumps(h,indent=2,sort_keys=True)+'\n')

marker='<!-- STAGE33_07_ALL72_AMBIENT_BOUNDARY_PROGRESS -->'
section=f'''\n{marker}\n## All-72 ambient boundary-function milestone\n\nThe mixed-order first-residue packages now have explicit ambient rational-function lifts on **all 72 boundary components**.  The 24 physical side conics contribute 120 nontrivial source/component functions with 240 selected crossing factors (`{SIDE_SHA}`); the 48 exceptional tangent conics contribute another 120 nontrivial functions with 240 factors (`{EXC_SHA}`).  The exceptional constructor reproduces all 48 frozen tangent-conic commitments before forming deterministic ambient projection pairs.\n\nThis does **not** promote any source to a global geometric Gersten/Brauer lift.  The remaining exact kernel is `{NEXT_KERNEL}`: assemble the 26 ambient boundary packages and certify every off-boundary codimension-one residue (or an exact cancellation) before global-lift credit.\n\n```text\nALL_72_BOUNDARY_COMPONENT_PACKAGES_AMBIENTIZED=true\nGLOBAL_GEOMETRIC_GERSTEN_LIFTS_MATERIALIZED=0/26\nOFF_BOUNDARY_CODIM1_RESIDUE_CERTIFICATES=0/26\nPROJECT_14x26_L_SQUARECLASS_TENSOR_COMPUTED=false\nABSOLUTE_DELTA_LOC_COMPUTED=false\nARITHMETIC_HS_CLOSED=false\nSTAGE33_PROGRESS_EFFECTIVE=6/11\n```\n'''
text=RESULT.read_text()
if marker in text: text=text.split(marker)[0].rstrip()+section
else: text=text.rstrip()+section
RESULT.write_text(text.rstrip()+'\n')
print(json.dumps({'success':True,'schema':h['schema'],'all72':True,'global_Gersten_lifts':'0/26','next':NEXT_LEAF},indent=2))
