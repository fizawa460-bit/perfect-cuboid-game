#!/usr/bin/env python3
import hashlib
import io
import json
import os
import urllib.request
import urllib.parse
import zipfile
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE = Path(__file__).resolve().parent
REPO = "fizawa460-bit/perfect-cuboid-game"
ARTIFACTS = {
    "br0a": (9505735040, "75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87"),
    "br0b": (9513603089, "cf95be77ae227227f8f2f2b478a54a4c38d82cc242d6c4a293d63490eb533c07"),
    "br0g": (9513712470, "4ef12f7686e0b251bbfbcc3f0c3f0c44c61db0e0fca7dbb94afcdc5f0fbfb637"),
}

class StripCrossHostAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        newreq = super().redirect_request(req, fp, code, msg, headers, newurl)
        if newreq is not None and urllib.parse.urlsplit(req.full_url).netloc != urllib.parse.urlsplit(newurl).netloc:
            newreq.remove_header("Authorization")
        return newreq

def download_artifact(key):
    aid, expected = ARTIFACTS[key]
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN required")
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/actions/artifacts/{aid}/zip",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "perfect-cuboid-stage33/2.1",
        },
    )
    opener = urllib.request.build_opener(StripCrossHostAuthRedirect())
    with opener.open(req, timeout=90) as resp:
        raw = resp.read()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != expected:
        raise SystemExit(f"{key} artifact digest mismatch: {actual}")
    return zipfile.ZipFile(io.BytesIO(raw))

def jload(zf, name):
    return json.loads(zf.read(name))

with download_artifact("br0a") as z:
    br0a = jload(z, "br0a-artifact-certificate.json")
with download_artifact("br0b") as z:
    d2 = jload(z, "d2-01-image.json")
    br0b = jload(z, "br0b-all-primary-inventory.json")
with download_artifact("br0g") as z:
    bg = jload(z, "boundary-galois.json")

K = sp.Matrix(br0a["unit_divisor_relation_kernel_basis"])
if K.shape != (14,72) or K.rank() != 14:
    raise SystemExit("audited U_D regression")
cc = [int(x)-1 for x in bg["boundary_perm_cc_1based"]]
ct = [int(x)-1 for x in bg["boundary_perm_ct_1based"]]
if ct != list(range(72)):
    raise SystemExit("unexpected sqrt2 action on boundary")

seen=set(); orbits=[]
for i in range(72):
    if i in seen:
        continue
    orb=sorted({i,cc[i]})
    if any(cc[j] not in orb for j in orb):
        raise SystemExit("cc is not involutive on boundary")
    seen.update(orb); orbits.append(orb)
if len(orbits)!=60 or sum(len(o)==1 for o in orbits)!=48 or sum(len(o)==2 for o in orbits)!=12:
    raise SystemExit("arithmetic boundary orbit regression")

# U_D is pointwise Galois fixed, so conjugate geometric components have equal
# valuations for every unit basis vector.
for o in orbits:
    if len(o)==2 and any(K[r,o[0]] != K[r,o[1]] for r in range(14)):
        raise SystemExit("unit valuation is not constant on a Q(i) orbit")

V = sp.Matrix([[int(K[r,o[0]]) for o in orbits] for r in range(14)])
if V.rank()!=14:
    raise SystemExit("arithmetic-orbit coefficient map lost rank")
D = smith_normal_form(V, domain=ZZ)
diag=[abs(int(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i] != 0]
if diag != [1]*14:
    raise SystemExit(f"unit valuation coefficient lattice is not primitive: {diag}")

q_orbit_indices=[i for i,o in enumerate(orbits) if len(o)==1]
qi_orbit_indices=[i for i,o in enumerate(orbits) if len(o)==2]

# d2_01 relations are both supported on the cc quadratic character chi_-1.
# At Q-defined boundary components the raw cyclic-algebra residue is valuation
# parity times chi_-1.  At Q(i)-components it vanishes because
# chi_-1 restricted to G_Q(i) is zero.
def kappa_raw_boundary_pattern(entry):
    cc_coeff=[int(x)&1 for x in entry["cc_quadratic_character_coefficients_f2"]]
    ct_coeff=[int(x)&1 for x in entry["ct_quadratic_character_coefficients_f2"]]
    if any(ct_coeff):
        raise SystemExit("unexpected ct character in audited KAPPA relation")
    out=[]
    for oi,o in enumerate(orbits):
        if len(o)==2:
            out.append(0)
        else:
            out.append(sum(cc_coeff[r]*int(V[r,oi]) for r in range(14)) & 1)
    return out

entries=d2["torsion_generator_images"]
if len(entries)!=2 or d2["image_f2_rank"]!=2:
    raise SystemExit("d2_01 audit regression")
patterns=[kappa_raw_boundary_pattern(e) for e in entries]
weights=[sum(v) for v in patterns]
if weights != [20,20]:
    raise SystemExit(f"unexpected KAPPA raw-residue weights {weights}")
if patterns[0] != patterns[1]:
    raise SystemExit("KAPPA raw boundary patterns no longer coincide")
if not any(patterns[0]):
    raise SystemExit("expected nonzero raw KAPPA boundary pattern")
if any(patterns[0][i] for i in qi_orbit_indices):
    raise SystemExit("chi_-1 did not vanish on Q(i) boundary orbits")

support=[i+1 for i,b in enumerate(patterns[0]) if b]
cert={
    "schema":"STAGE33_07_BR0B_TO_BOUNDARY_RAW_RESIDUE_MAP_V1",
    "source_locks":{
        "br0a_artifact_id":ARTIFACTS["br0a"][0],
        "br0a_artifact_sha256":ARTIFACTS["br0a"][1],
        "br0b_artifact_id":ARTIFACTS["br0b"][0],
        "br0b_artifact_sha256":ARTIFACTS["br0b"][1],
        "br0g_artifact_id":ARTIFACTS["br0g"][0],
        "br0g_artifact_sha256":ARTIFACTS["br0g"][1],
        "unit_kernel_sha256":br0a["unit_divisor_relation_kernel_basis_sha256"],
        "boundary_galois_sha256":bg["canonical_sha256"],
        "d2_01_sha256":d2["canonical_sha256"],
        "br0b_inventory_sha256":br0b["canonical_sha256"],
    },
    "arithmetic_boundary_orbits":60,
    "q_boundary_orbits":48,
    "qi_boundary_orbits":12,
    "unit_rank":14,
    "unit_to_arithmetic_boundary_valuation_matrix_14x60":[[int(x) for x in V.row(r)] for r in range(14)],
    "coefficient_matrix_rank":14,
    "coefficient_matrix_smith_nonzero_diagonal":diag,
    "coefficient_lattice_primitive":True,
    "character_residue_rule":{
        "Q_component":"rho_D(chi,u)=v_D(u)*chi",
        "Q_i_component":"rho_D(chi,u)=v_D(u)*Res_{G_Q(i)}(chi)",
    },
    "kappa_raw_residue":{
        "relation_count":2,
        "raw_patterns_equal":True,
        "common_pattern_nonzero":True,
        "common_pattern_weight_on_60_orbits":20,
        "common_pattern_support_arithmetic_orbit_ids_1based":support,
        "support_on_q_orbits_only":True,
        "qi_zero_reason":"chi_-1 restricts trivially to G_Q(i)",
        "raw_map_descends_through_XQ14_mod_kappa_without_lift_correction":False,
    },
    "exact_conclusion":"The raw character-unit valuation map is exact and primitive at coefficient level, but it does not descend through the two d2_01 KAPPA relations by itself. Both KAPPA relations have the same nonzero Q-boundary quadratic residue pattern; the finite PicU/hypercohomology lift correction must be materialized and combined before the BR0B/BR0G duplicate quotient can be certified.",
    "new_residual_kernel":"R33-BR2A-KAPPA-BOUNDARY-RESIDUE-LIFT-CORRECTION",
    "next_exact_leaf":"L33-07-MATERIALIZE-PICU-TORSION-LIFT-BOUNDARY-CORRECTION-AND-CANCEL-KAPPA-PATTERN",
    "relation_matrix_exact_for_two_primary_branch":False,
    "symbol_matrix_exact_for_two_primary_branch":False,
    "trivial_algebraic_duplicate_quotient_exact":False,
    "complete_relevant_q_defined_class_list_for_stage33_brauer_scope":False,
    "unresolved_unknown_in_scope":1,
    "unit_status":"RUNNING",
    "unit_closed":False,
    "downstream_released":False,
    "stage33_progress":"6/11",
    "stage33_08_released":False,
    "theorem_credit":False,
    "endpoint_credit":False,
    "perfect_cuboid_nonexistence_claim":False,
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
(HERE/"br0b-boundary-raw-residue-map.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({
    "success":True,
    "coefficient_rank":14,
    "smith_diagonal":diag,
    "kappa_raw_pattern_weight":20,
    "kappa_raw_patterns_equal":True,
    "raw_map_descends_mod_kappa":False,
    "remaining_kernel":cert["new_residual_kernel"],
    "next_leaf":cert["next_exact_leaf"],
    "certificate_sha256":cert["canonical_sha256"],
},indent=2,sort_keys=True))
