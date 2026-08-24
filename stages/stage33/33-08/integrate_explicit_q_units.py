#!/usr/bin/env python3
"""Integrate the exact rank-14 Q-unit replay into Stage33-08 representatives."""
import hashlib, io, json, os, re, urllib.parse, urllib.request, zipfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
S33=HERE.parent
REPO="fizawa460-bit/perfect-cuboid-game"
BR0G_ARTIFACT_ID=9513712470
BR0G_ARTIFACT_SHA256="4ef12f7686e0b251bbfbcc3f0c3f0c44c61db0e0fca7dbb94afcdc5f0fbfb637"


def load(p): return json.loads(p.read_text(encoding="utf-8"))


class StripCrossHostAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        nr=super().redirect_request(req,fp,code,msg,headers,newurl)
        if nr is not None and urllib.parse.urlsplit(req.full_url).netloc != urllib.parse.urlsplit(newurl).netloc:
            nr.remove_header("Authorization")
        return nr


def download():
    tok=os.environ.get("GITHUB_TOKEN")
    if not tok: raise SystemExit("GITHUB_TOKEN required")
    req=urllib.request.Request(
      f"https://api.github.com/repos/{REPO}/actions/artifacts/{BR0G_ARTIFACT_ID}/zip",
      headers={"Authorization":f"Bearer {tok}","Accept":"application/vnd.github+json",
               "X-GitHub-Api-Version":"2022-11-28","User-Agent":"perfect-cuboid-stage33/3.1"})
    with urllib.request.build_opener(StripCrossHostAuthRedirect()).open(req,timeout=90) as r: raw=r.read()
    got=hashlib.sha256(raw).hexdigest()
    if got!=BR0G_ARTIFACT_SHA256: raise SystemExit(f"artifact digest mismatch {got}")
    return zipfile.ZipFile(io.BytesIO(raw))


prefix=load(HERE/"representative-coverage-prefix.json")
qu=load(S33/"33-04"/"explicit-q-units.json")
s03=load(S33/"33-03"/"audit-state.json")
s07=load(S33/"33-07"/"audit-state.json")
assert prefix["unit_status"]=="RUNNING"
assert qu["explicit_q_unit_count"]==14
assert qu["explicit_q_unit_divisor_lattice_rank"]==14
assert qu["explicit_q_unit_divisor_lattice_equals_audited_U_D"] is True
assert qu["all_units_defined_over_Q"] is True
assert s03["unit_status"]=="CLOSED" and s03["br0b"]=="DISCHARGED"
assert s07["unit_status"]=="CLOSED" and s07["br0b"]["full_boundary_map_injective"]

with download() as zf:
    sk=json.loads(zf.read("boundary-residue-skeleton.json"))
ids=[x["stable_id"] for x in sk["component_inventory"]]
assert len(ids)==72 and len(set(ids))==72

units=[]
for u in qu["explicit_q_units"]:
    div=[int(x) for x in u["divisor_vector_72"]]
    assert len(div)==72
    support=[ids[i] for i,v in enumerate(div) if v]
    fn=u["function"]
    m=re.fullmatch(r"\(([^()]+)\)/\(([^()]+)\)",fn)
    if not m: raise SystemExit(f"unexpected unit function {fn}")
    num,den=m.groups()
    denvec=next(x["divisor_vector_72"] for x in qu["factor_divisors_72"] if x["factor"]==den)
    units.append({
      "unit_id":u["unit_id"],
      "rational_function":fn,
      "numerator_factor":num,
      "denominator_factor":den,
      "divisor_vector_72":div,
      "ramification_support_boundary_ids":support,
      "denominator_support_boundary_ids":[ids[i] for i,v in enumerate(denvec) if v],
      "representative_template":"CUP(chi, "+fn+"); equivalently cyclic algebra attached to finite-order character chi and unit u",
      "character_parameter":"chi in Hom_cont(G_Q,Q/Z), specialized to any finite primary order",
      "primary_order_rule":"divides order(chi); exact class order determined by the audited Stage33-03/07 quotient relations",
      "field_of_definition":"Q",
      "physical_open_domain":"ALL_PHYSICAL_OPEN: numerator and denominator divisor support is contained in deleted boundary",
      "exact_evaluable_on_physical_open":True,
      "equivalence_independence_certificate":"Stage33-03 exact nonsplit filtration plus Stage33-07 injective boundary map/duplicate quotient"
    })

cert={
 "schema":"STAGE33_08_BR0B_LEFT_EXPLICIT_QUNIT_REPRESENTATIVES_V1",
 "source_locks":{
   "explicit_q_units":"runtime replay of stages/stage33/33-04/materialize_q_units.py",
   "stage33_03_audit":"stages/stage33/33-03/audit-state.json",
   "stage33_07_audit":"stages/stage33/33-07/audit-state.json",
   "stage33_04_artifact_id":BR0G_ARTIFACT_ID,
   "stage33_04_artifact_sha256":BR0G_ARTIFACT_SHA256
 },
 "explicit_q_unit_count":14,
 "explicit_q_unit_lattice_rank":14,
 "explicit_q_unit_lattice_equals_U_D":True,
 "all_14_unit_coordinate_representative_templates_evaluable":True,
 "all_unit_zero_pole_support_on_deleted_physical_boundary":True,
 "br0b_left_filtration_parametric_representatives_complete":True,
 "br0b_left_filtration_group":"X_Q^14/<KAPPA_1,KAPPA_2>",
 "internal_nonsplit_filtration_preserved":True,
 "unit_representatives":units,
 "residual_kernels":[
   "R33-BR2B-BR0B-RIGHT-FILTRATION-EXPLICIT-REPRESENTATIVES",
   "R33-BR2B-GLOBAL-GERSTEN-SECTION-FOR-BOUNDARY-CONSTANT-CHARACTER-COMPLEMENT",
   "R33-BR2B-GLOBAL-GERSTEN-SECTION-FOR-61-FINITE-RAMIFIED-GENERATORS",
   "R33-BR2B-J2-PHYSICAL-OPEN-PATCH-COVER"
 ],
 "unresolved_unknown_in_scope":4,
 "br2b":"RUNNING",
 "unit_status":"RUNNING",
 "unit_closed":False,
 "downstream_released":False,
 "stage33_09_released":False,
 "next_exact_leaf":"L33-08-MATERIALIZE-BR0B-RIGHT-FILTRATION-LIFTS-THEN-GERSTEN-SECTIONS",
 "theorem_credit":False,
 "endpoint_credit":False,
 "perfect_cuboid_nonexistence_claim":False
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
(HERE/"br0b-left-explicit-representatives.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n")
print(json.dumps({
 "success":True,
 "explicit_q_units":14,
 "br0b_left_representatives_complete":True,
 "remaining_residuals":4,
 "next_exact_leaf":cert["next_exact_leaf"],
 "certificate_sha256":cert["canonical_sha256"]
},indent=2,sort_keys=True))
