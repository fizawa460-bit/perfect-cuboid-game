#!/usr/bin/env python3
import hashlib
import io
import json
import os
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

import sympy as sp
from sympy import ZZ
from sympy.matrices.normalforms import smith_normal_decomp, smith_normal_form

HERE = Path(__file__).resolve().parent
REPO = "fizawa460-bit/perfect-cuboid-game"
ARTIFACTS = {
    "br0a": (9505735040, "75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87"),
    "br0b": (9513603089, "cf95be77ae227227f8f2f2b478a54a4c38d82cc242d6c4a293d63490eb533c07"),
    "br0g": (9513712470, "4ef12f7686e0b251bbfbcc3f0c3f0c44c61db0e0fca7dbb94afcdc5f0fbfb637"),
}
RETAINED = HERE / "br0b-boundary-raw-residue-map.json"
RETAINED_SHA256 = "44f03877c524a817e41036d89cf20ea971cc95c3d52adf53c2af6317a83d2324"

# Stage33 artifacts have short retention.  Once the exact result has been
# independently produced and source-locked, keep the compact certificate in
# git and validate it here.  Artifact download remains only the rebuild path.
if RETAINED.exists():
    retained = json.loads(RETAINED.read_text(encoding="utf-8"))
    claimed = retained.get("canonical_sha256")
    chk = dict(retained)
    chk.pop("canonical_sha256", None)
    actual = hashlib.sha256(json.dumps(chk, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if claimed != RETAINED_SHA256 or actual != RETAINED_SHA256:
        raise SystemExit(f"retained BR0B residue certificate hash regression: claimed={claimed} actual={actual}")
    if retained.get("schema") != "STAGE33_07_BR0B_TO_BOUNDARY_RESIDUE_MAP_V2":
        raise SystemExit("retained BR0B residue schema regression")
    if retained.get("induced_left_filtration_boundary_map_injective") is not True:
        raise SystemExit("retained BR0B residue injectivity regression")
    if retained.get("exact_kernel_statement") != "ker(X_Q^14 -> X_Q^48 direct_sum X_Q(i)^12 via unit valuations/restriction) = <KAPPA_1,KAPPA_2>":
        raise SystemExit("retained BR0B residue kernel regression")
    print(json.dumps({
        "success": True,
        "source": "RETAINED_EXACT_CERTIFICATE",
        "artifact_rebuild_required": False,
        "canonical_sha256": actual,
        "induced_left_filtration_boundary_map_injective": True,
        "stage33_progress": "6/11",
    }, indent=2, sort_keys=True))
    raise SystemExit(0)

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
        raise SystemExit("GITHUB_TOKEN required for artifact rebuild")
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/actions/artifacts/{aid}/zip",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "perfect-cuboid-stage33/2.2",
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

def gf2_rank(rows):
    a=[[int(x)&1 for x in row] for row in rows]
    if not a:
        return 0
    rank=0
    for c in range(len(a[0])):
        p=next((i for i in range(rank,len(a)) if a[i][c]),None)
        if p is None:
            continue
        a[rank],a[p]=a[p],a[rank]
        for i in range(len(a)):
            if i!=rank and a[i][c]:
                a[i]=[x^y for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a):
            break
    return rank

def left_nullspace_f2(A):
    B=[[int(A[r,c])&1 for r in range(A.rows)] for c in range(A.cols)]
    m=len(B); n=A.rows; rank=0; piv=[]
    for c in range(n):
        p=next((i for i in range(rank,m) if B[i][c]),None)
        if p is None:
            continue
        B[rank],B[p]=B[p],B[rank]
        for i in range(m):
            if i!=rank and B[i][c]:
                B[i]=[x^y for x,y in zip(B[i],B[rank])]
        piv.append(c); rank+=1
    free=[c for c in range(n) if c not in piv]
    out=[]
    for f in free:
        x=[0]*n; x[f]=1
        for rr,c in reversed(list(enumerate(piv))):
            x[c]=sum(B[rr][j]*x[j] for j in range(n))&1
        out.append(x)
    return out

with download_artifact("br0a") as z:
    br0a = jload(z, "br0a-artifact-certificate.json")
with download_artifact("br0b") as z:
    d2 = jload(z, "d2-01-image.json")
    br0b = jload(z, "br0b-all-primary-inventory.json")
with download_artifact("br0g") as z:
    bg = jload(z, "boundary-galois.json")

M=sp.Matrix(br0a["boundary_to_pic_matrix"])
if M.shape!=(72,64):
    raise SystemExit("boundary-to-Pic shape regression")
D,S,T=smith_normal_decomp(M,domain=ZZ)
if D != S*M*T:
    raise SystemExit("Smith decomposition regression")
diag_pic=[abs(int(D[i,i])) for i in range(58)]
if diag_pic != [1]*56+[2,2]:
    raise SystemExit("Pic(Ubar) Smith tail regression")
U=S[58:72,:]
if U.shape!=(14,72) or U.rank()!=14 or U*M != sp.zeros(14,64):
    raise SystemExit("Smith unit-kernel basis regression")

cc=[int(x)-1 for x in bg["boundary_perm_cc_1based"]]
ct=[int(x)-1 for x in bg["boundary_perm_ct_1based"]]
if ct != list(range(72)):
    raise SystemExit("unexpected sqrt2 action on boundary")
seen=set(); orbits=[]
for i in range(72):
    if i in seen:
        continue
    orb=sorted({i,cc[i]})
    if any(cc[j] not in orb for j in orb):
        raise SystemExit("cc boundary action not involutive")
    seen.update(orb); orbits.append(orb)
if len(orbits)!=60 or sum(len(o)==1 for o in orbits)!=48 or sum(len(o)==2 for o in orbits)!=12:
    raise SystemExit("arithmetic boundary orbit regression")
for o in orbits:
    if len(o)==2 and any(U[r,o[0]]!=U[r,o[1]] for r in range(14)):
        raise SystemExit("Smith unit basis lost absolute Galois invariance")

q_orbits=[o for o in orbits if len(o)==1]
qi_orbits=[o for o in orbits if len(o)==2]
V=sp.Matrix([[int(U[r,o[0]]) for o in orbits] for r in range(14)])
Vq=sp.Matrix([[int(U[r,o[0]]) for o in q_orbits] for r in range(14)])
Vqi=sp.Matrix([[int(U[r,o[0]]) for o in qi_orbits] for r in range(14)])
Dall=smith_normal_form(V,domain=ZZ)
Dq=smith_normal_form(Vq,domain=ZZ)
all_diag=[abs(int(Dall[i,i])) for i in range(14) if Dall[i,i]!=0]
q_diag=[abs(int(Dq[i,i])) for i in range(14) if Dq[i,i]!=0]
if all_diag != [1]*14:
    raise SystemExit(f"full coefficient lattice not primitive: {all_diag}")
if q_diag != [1]*12+[2,2]:
    raise SystemExit(f"Q-component coefficient Smith regression: {q_diag}")

null_q=left_nullspace_f2(Vq)
if len(null_q)!=2 or gf2_rank(null_q)!=2:
    raise SystemExit("Q-component mod2 kernel is not two-dimensional")
entries=d2["torsion_generator_images"]
if len(entries)!=2 or d2["image_f2_rank"]!=2:
    raise SystemExit("d2_01 rank regression")
kappas=[]
for e in entries:
    if any(int(x)&1 for x in e["ct_quadratic_character_coefficients_f2"]):
        raise SystemExit("audited KAPPA acquired ct-character component")
    kappas.append([int(x)&1 for x in e["cc_quadratic_character_coefficients_f2"]])
if gf2_rank(kappas)!=2 or gf2_rank(null_q+kappas)!=2:
    raise SystemExit("KAPPA span is not the Q-component mod2 kernel")

qi_patterns=[]
for n in null_q:
    qi_patterns.append([sum(n[r]*int(Vqi[r,c]) for r in range(14))&1 for c in range(12)])
if gf2_rank(qi_patterns)!=2:
    raise SystemExit("Q(i) restriction patterns do not separate the two Q-kernel directions")

kappa_q_patterns=[]
for k in kappas:
    kappa_q_patterns.append([sum(k[r]*int(Vq[r,c]) for r in range(14))&1 for c in range(48)])
if any(any(row) for row in kappa_q_patterns):
    raise SystemExit("audited KAPPA has nonzero Q-boundary residue")

out={
    "schema":"STAGE33_07_BR0B_TO_BOUNDARY_RESIDUE_MAP_V2",
    "source_locks":{
        "br0a_artifact_id":ARTIFACTS["br0a"][0],"br0a_artifact_sha256":ARTIFACTS["br0a"][1],
        "br0b_artifact_id":ARTIFACTS["br0b"][0],"br0b_artifact_sha256":ARTIFACTS["br0b"][1],
        "br0g_artifact_id":ARTIFACTS["br0g"][0],"br0g_artifact_sha256":ARTIFACTS["br0g"][1],
        "boundary_to_pic_matrix_sha256":hashlib.sha256(json.dumps(br0a["boundary_to_pic_matrix"],separators=(",",":")).encode()).hexdigest(),
        "d2_01_sha256":d2["canonical_sha256"],"br0b_inventory_sha256":br0b["canonical_sha256"],
        "boundary_galois_sha256":bg["canonical_sha256"],
    },
    "basis_correction":{"br0a_reported_kernel_basis_used_as_stage33_03_smith_basis":False,"stage33_03_smith_unit_basis_reconstructed":True,"reason":"Stage33-03 H2 coordinates are rows 59..72 of the Smith left transform S; the BR0A artifact kernel basis is an independently valid but different Z-basis."},
    "unit_rank":14,"arithmetic_boundary_orbits":60,"q_boundary_orbits":48,"qi_boundary_orbits":12,
    "unit_to_arithmetic_boundary_valuation_matrix_14x60":[[int(x) for x in V.row(r)] for r in range(14)],
    "full_coefficient_matrix_rank":V.rank(),"full_coefficient_matrix_smith_nonzero_diagonal":all_diag,"full_coefficient_lattice_primitive":True,
    "q_component_coefficient_matrix_smith_nonzero_diagonal":q_diag,"q_component_mod2_kernel_dimension":2,"q_component_mod2_kernel_basis":null_q,
    "kappa_f2_basis":kappas,"kappa_span_equals_q_component_mod2_kernel":True,"qi_patterns_of_q_kernel_basis":qi_patterns,"qi_pattern_rank_f2":2,
    "character_residue_rule":{"Q_component":"rho_D(chi,u)=v_D(u)*chi","Q_i_component":"rho_D(chi,u)=v_D(u)*Res_{G_Q(i)}(chi)","kernel_of_quadratic_restriction_Q_to_Qi":"<chi_-1>"},
    "kappa_residue_zero":{"both_q_component_patterns_zero":True,"both_qi_component_patterns_zero":True,"qi_zero_reason":"both KAPPA relations use chi_-1, whose restriction to G_Q(i) is zero"},
    "exact_kernel_statement":"ker(X_Q^14 -> X_Q^48 direct_sum X_Q(i)^12 via unit valuations/restriction) = <KAPPA_1,KAPPA_2>",
    "induced_domain":"X_Q^14/<KAPPA_1,KAPPA_2>","induced_left_filtration_boundary_map_injective":True,
    "odd_primary_submap_injective":"X_Q,odd^14 injects into the odd-primary BR0G constant-character module",
    "two_primary_left_submap_injective":"X_Q[2^infinity]^14/<KAPPA_1,KAPPA_2> injects into the two-primary BR0G constant-character module",
    "left_filtration_br0b_br0g_duplicate_overlap_exact":True,
    "exact_conclusion":"The complete Stage33-03 left filtration is exactly identified with its image inside the Stage33-04 constant-character boundary module; its only raw character-unit residue kernel is the already-quotiented KAPPA_1,KAPPA_2 image. No extra left-filtration class is deleted.",
    "symbol_matrix_exact_for_two_primary_branch":False,"relation_matrix_exact_for_two_primary_branch":False,"trivial_algebraic_duplicate_quotient_exact":False,
    "complete_relevant_q_defined_class_list_for_stage33_brauer_scope":False,
    "new_residual_kernel":"R33-BR2A-BR0B-RIGHT-FILTRATION-BOUNDARY-LIFT-AND-FINITE-RAMIFIED-INTEGRATION",
    "next_exact_leaf":"L33-07-MATERIALIZE-H1-PICU-FIVE-PLUS-QUADRATIC-LIFT-BOUNDARY-RESIDUES-AND-MATCH-RAMIFIED-MODULE",
    "unit_status":"RUNNING","unit_closed":False,"downstream_released":False,"stage33_progress":"6/11","stage33_08_released":False,"unresolved_unknown_in_scope":1,
    "theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_nonexistence_claim":False,
}
raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode(); out["canonical_sha256"]=hashlib.sha256(raw).hexdigest()
RETAINED.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({"success":True,"source":"ARTIFACT_REBUILD","canonical_sha256":out["canonical_sha256"],"induced_left_filtration_boundary_map_injective":True,"stage33_progress":"6/11"},indent=2,sort_keys=True))
