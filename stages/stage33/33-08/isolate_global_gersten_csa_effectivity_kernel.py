#!/usr/bin/env python3
"""Freeze the smallest remaining Stage33-08 representative-effectivity kernel.

The audited Stage33-04/07 stack proves the relevant Gersten/Faddeev residue
modules, relations, exact orders, and exponent-preserving existence of lifts.
Stage33-08 now has an explicit saturated Q-unit basis, all 44 unit-symbol
quaternions, and the exact generic J2 corestriction CSA.  What remains is not a
class-survival problem: it is the constructive section problem from the
remaining residue presentations to evaluable global central simple algebras on
the surface function field.

This certificate deliberately does NOT infer an explicit CSA from Gersten
surjectivity.  It freezes the required input/output contract for a later exact
constructive adapter.
"""
import hashlib, io, json, os, urllib.parse, urllib.request, zipfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
REPO="fizawa460-bit/perfect-cuboid-game"
ART=9521076746
DIG="c9de08cff9ce04b0bfe1fd216e176996437d44fa7c841673f037400ad8e47dca"
KERNEL="R33-BR2B-GLOBAL-GERSTEN-CSA-SECTION-EFFECTIVITY"

class R(urllib.request.HTTPRedirectHandler):
 def redirect_request(self,req,fp,code,msg,h,newurl):
  n=super().redirect_request(req,fp,code,msg,h,newurl)
  if n is not None and urllib.parse.urlsplit(req.full_url).netloc!=urllib.parse.urlsplit(newurl).netloc:n.remove_header("Authorization")
  return n

def dl():
 t=os.environ.get("GITHUB_TOKEN")
 if not t:raise SystemExit("GITHUB_TOKEN required")
 req=urllib.request.Request(f"https://api.github.com/repos/{REPO}/actions/artifacts/{ART}/zip",headers={"Authorization":f"Bearer {t}","Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"perfect-cuboid-stage33/4.3"})
 with urllib.request.build_opener(R()).open(req,timeout=90) as r:b=r.read()
 if hashlib.sha256(b).hexdigest()!=DIG:raise SystemExit("Stage33-07 artifact digest mismatch")
 return zipfile.ZipFile(io.BytesIO(b))

q=json.load(open(HERE/"saturated-q-unit-generators.json"))
left=json.load(open(HERE/"br0b-left-explicit-representatives.json"))
x=json.load(open(HERE/"u44-j2-explicit-representatives.json"))
if not q["full_rank14_saturated_unit_lattice_generated"]:raise SystemExit("U_D explicit basis regression")
if not left["br0b_left_filtration_parametric_representatives_complete"]:raise SystemExit("BR0B left representative regression")
if not x["u44_explicit_representatives_complete"] or x["u44_generator_count"]!=44:raise SystemExit("U44 regression")
if not x["j2_generic_exact_representative_complete"]:raise SystemExit("J2 generic representative regression")

with dl() as z:
 full=json.loads(z.read("full-br0b-boundary-injection.json"))
 finite=json.loads(z.read("br0g-finite-ramified-residue-presentation.json"))
 global2=json.loads(z.read("global-two-primary-presentation.json"))
 rawmap=json.loads(z.read("br0b-boundary-raw-residue-map.json"))

if not full["full_br0b_boundary_map_injective"]:raise SystemExit("full BR0B boundary injection regression")
if not global2["coefficient_gersten_exponent_preserving_lifts"]:raise SystemExit("Gersten lift existence regression")
if finite["residue_presentation_generators"]!={"U_order2":44,"R_order2":17,"O_nominal_order4":12}:raise SystemExit("finite generator split regression")
if global2["complete_inventory"]["seven_line"]["group"]!="0":raise SystemExit("line9 zero regression")

constant_all=full["boundary_constant_character_module_all_primary"]
constant_odd=full["boundary_constant_character_module_odd"]
constant_two=full["boundary_constant_character_module_two_primary"]
if rawmap["arithmetic_boundary_orbits"]!=60 or rawmap["q_boundary_orbits"]!=48 or rawmap["qi_boundary_orbits"]!=12:raise SystemExit("constant boundary orbit regression")

# Evidence firewall: the audited producers certify module-level residue data and
# existence/order of lifts.  They do not contain a per-class evaluable global
# CSA field.  Only U44 and J2 have now been upgraded to such representatives.
for obj,name in ((finite,"finite"),(global2,"global2"),(full,"full")):
 if "symbol_or_algebra_representative" in obj:
  raise SystemExit(f"unexpected global representative field appeared in {name}; update kernel analysis")

cert={
 "schema":"STAGE33_08_GLOBAL_GERSTEN_CSA_SECTION_EFFECTIVITY_KERNEL_V1",
 "stage33_unit":"33-08","pr":1375,
 "source_locks":{
  "stage33_07_artifact_id":ART,"stage33_07_artifact_sha256":DIG,
  "full_br0b_boundary_injection_sha256":full["canonical_sha256"],
  "br0g_finite_ramified_residue_presentation_sha256":finite["canonical_sha256"],
  "global_two_primary_presentation_sha256":global2["canonical_sha256"],
  "br0b_boundary_raw_residue_map_sha256":rawmap["canonical_sha256"],
  "saturated_q_unit_sha256":q["canonical_sha256"],
  "br0b_left_explicit_sha256":left["canonical_sha256"],
  "u44_j2_explicit_sha256":x["canonical_sha256"],
  "stage33_04_curve_lift_input":"Faddeev/localization exact sequence on each P1_K; surface Gersten compatibility",
 },
 "accepted_exact_prefix":{
  "every_stage33_07_relevant_class_accounted":True,
  "every_surviving_class_has_primary_order_and_provenance":True,
  "full_U_D_explicit_q_rational_basis_rank":14,
  "br0b_left_filtration_explicit_parametric_representatives_complete":True,
  "finite_ramified_U44_explicit_quaternion_representatives_complete":True,
  "finite_ramified_U44_physical_open_domain":"ALL_PHYSICAL_OPEN",
  "j2_q_defined_generic_corestriction_csa_complete":True,
  "j2_generic_dense_patch_evaluable":True,
  "seven_line_endpoint_block_zero":True
 },
 "remaining_input_modules":{
  "boundary_constant_character_block_all_primary":constant_all,
  "boundary_constant_character_block_odd":constant_odd,
  "boundary_constant_character_block_two_primary":constant_two,
  "boundary_constant_orbits":{"total":60,"Q":48,"Q_i":12},
  "finite_ramified_non_unit_symbol_generators":{"R_order2":17,"O_order4":12},
  "finite_ramified_residue_relation_matrix_exact":True,
  "finite_ramified_residue_symbol_matrix_exact":True,
  "gersten_faddeev_exponent_preserving_lift_existence_exact":True
 },
 "why_existing_exactness_is_not_stage33_08_representation_credit":(
  "Gersten/Faddeev exactness and the Stage33-07 residue matrices certify existence, residues, relations and exact orders, "
  "but do not provide an executable section assigning each remaining residue class a Q-defined global central simple algebra/crossed-product cocycle with explicit denominators and evaluation patches."
 ),
 "required_new_adapter":{
  "input":"60-orbit all-primary constant-character tuples plus R01..R17 and O01..O12 residue generators with audited relations",
  "output":"for every generator/parametric character tuple, an explicit Q-defined CSA or crossed-product cocycle in Br(Q(U))",
  "must_verify":[
   "exact residues equal the audited Stage33-07 vectors",
   "no extra ramification on the physical open",
   "primary order is preserved (including O01..O12 order four and arbitrary finite character orders)",
   "denominator support is explicit",
   "equivalence/independence against the audited relation matrix is explicit",
   "a certified physical-open evaluation domain/patch cover is supplied"
  ]
 },
 "current_source_locked_stack_has_constructive_global_section_adapter":False,
 "new_kernel_id":KERNEL,
 "new_kernel_exposed":True,
 "smallest_unresolved_dependency":"constructive global Gersten-to-CSA section for non-unit residue classes; class survival and residue modules are already exact",
 "j2_patch_cover_note":"J2 already has an exact Q-defined global Brauer class and generic CSA formula; its displayed formula patch can be completed alongside the constructive representative adapter and is not a class-survival unknown.",
 "closure_criteria_total":10,"closure_criteria_satisfied":2,
 "every_stage33_07_relevant_class_accounted":True,
 "every_surviving_class_has_primary_order_and_provenance":True,
 "every_surviving_class_has_exact_evaluable_representative":False,
 "ramification_support_complete":False,"denominator_support_complete":False,
 "equivalence_independence_certificates_complete":False,"physical_open_domain_certified":False,
 "br2b":"BLOCKED_NEW_KERNEL","unresolved_unknown_in_scope":1,
 "unit_status":"BLOCKED_NEW_KERNEL","unit_closed":False,"downstream_released":False,
 "stage33_progress":"7/11","stage33_09_released":False,
 "audit_verdict":"NOT_APPLICABLE_BLOCKED_NEW_KERNEL",
 "next_expected_command":"Stage33-main-batch",
 "theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_nonexistence_claim":False
}
raw=json.dumps(cert,sort_keys=True,separators=(",",":")).encode();cert["canonical_sha256"]=hashlib.sha256(raw).hexdigest();(HERE/"global-gersten-csa-effectivity-kernel.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({"success":True,"UNIT_STATUS":cert["unit_status"],"NEW_KERNEL_ID":KERNEL,"U44_EXPLICIT":44,"FINITE_REMAINING":"R17+O12","CONSTANT_ORBITS_REMAINING":60,"CLOSURE_CRITERIA":"2/10","STAGE33_PROGRESS":"7/11","STAGE33_09_RELEASED":False,"certificate_sha256":cert["canonical_sha256"]},indent=2,sort_keys=True))
