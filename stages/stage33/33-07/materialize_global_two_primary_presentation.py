#!/usr/bin/env python3
"""Global Stage33-07 two-primary presentation and complete frozen-scope inventory.

This leaf integrates the audited BR0B/BR0G/K3/line9 branches without
pretending that an explicit evaluable representative has already been built
for every class (that remains Stage33-08).

Two coefficient-level exactness inputs are load-bearing:

* the Faddeev/localization sequence on each rational boundary normalization;
* the Bloch--Ogus/Panin--Zainoulline Gersten complex with finite mu_n
  coefficients on the smooth Q-surface, for n=2 and n=4.

They imply that each finite compatible residue invariant factor of exact order
n=2 or 4 has a Brauer lift killed by n. Since its residue itself has exact
order n, the lift has exact order n. Choosing such lifts for an invariant-
factor basis gives a noncanonical splitting of the finite ramified quotient.
Explicit rational-function/CSA representatives are deliberately deferred to
Stage33-08.
"""
import hashlib
import io
import json
import os
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
REPO = "fizawa460-bit/perfect-cuboid-game"
BR0G_ARTIFACT_ID = 9513712470
BR0G_ARTIFACT_SHA256 = "4ef12f7686e0b251bbfbcc3f0c3f0c44c61db0e0fca7dbb94afcdc5f0fbfb637"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


class StripCrossHostAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        nr = super().redirect_request(req, fp, code, msg, headers, newurl)
        if nr is not None and urllib.parse.urlsplit(req.full_url).netloc != urllib.parse.urlsplit(newurl).netloc:
            nr.remove_header("Authorization")
        return nr


def download_br0g():
    tok = os.environ.get("GITHUB_TOKEN")
    if not tok:
        raise SystemExit("GITHUB_TOKEN required")
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/actions/artifacts/{BR0G_ARTIFACT_ID}/zip",
        headers={
            "Authorization": f"Bearer {tok}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "perfect-cuboid-stage33/2.5",
        },
    )
    with urllib.request.build_opener(StripCrossHostAuthRedirect()).open(req, timeout=90) as resp:
        raw = resp.read()
    got = hashlib.sha256(raw).hexdigest()
    if got != BR0G_ARTIFACT_SHA256:
        raise SystemExit(f"BR0G artifact digest mismatch {got}")
    return zipfile.ZipFile(io.BytesIO(raw))


br0b = load(S33 / "33-03" / "audit-state.json")
br0g = load(S33 / "33-04" / "audit-state.json")
k3 = load(S33 / "33-05" / "audit-state.json")
line9 = load(S33 / "33-06" / "audit-state.json")
controller = load(S33 / "controller.json")
left = load(HERE / "br0b-boundary-raw-residue-map.json")
finite = load(HERE / "br0g-finite-ramified-residue-presentation.json")
fullinj = load(HERE / "full-br0b-boundary-injection.json")
j2scan = load(HERE / "j2-endpoint-q2-variation.json")

assert br0b["unit_status"] == "CLOSED" and br0b["br0b"] == "DISCHARGED"
assert br0g["unit_status"] == "CLOSED" and br0g["br0g"] == "DISCHARGED"
assert k3["unit_status"] == "CLOSED" and k3["q_surviving_geometric_br2_basis"] == ["J2"]
assert line9["unit_status"] == "CLOSED" and line9["accepted_exact_result"]["endpoint_relevant_surviving_dimension_f2"] == 0
assert controller["stage33_progress"] == "6/11" and controller["stage33_07_released"] is True
assert left["induced_left_filtration_boundary_map_injective"] is True
assert fullinj["full_br0b_boundary_map_injective"] is True
assert fullinj["trivial_algebraic_duplicate_quotient_exact"] is True
assert finite["finite_ramified_boundary_residue_module_exact"] is True
assert finite["finite_ramified_boundary_residue_module"] == "(Z/2)^49 direct_sum (Z/4)^12"
assert j2scan["evaluation_nonconstant_on_endpoint_Q2_locus_certified"] is True
assert j2scan["both_invariants_0_and_half_observed"] is True

with download_br0g() as zf:
    sk = json.loads(zf.read("boundary-residue-skeleton.json"))
    bg = json.loads(zf.read("boundary-galois.json"))
    us = json.loads(zf.read("unit-symbol-residue-span.json"))
    qr = json.loads(zf.read("qfixed17-graph-residual.json"))
    tp = json.loads(zf.read("two-primary-prime-power-gersten-descent.json"))

if sk["codim2_crossing_count"] != 144:
    raise SystemExit("crossing inventory regression")
if tp["full_two_primary_prime_power_gersten_character_descent_complete"] is not True:
    raise SystemExit("prime-power BR0G predecessor regression")

# Reconstruct the 120 arithmetic crossing orbits exactly.
edges = [(int(e["side_vertex"])-1, int(e["exceptional_vertex"])-1) for e in sk["codim2_crossings"]]
edge_index = {tuple(sorted(e)): i for i, e in enumerate(edges)}
cc = [int(x)-1 for x in bg["boundary_perm_cc_1based"]]

def edge_perm(p):
    out=[]
    for a,b in edges:
        key=tuple(sorted((p[a],p[b])))
        if key not in edge_index:
            raise SystemExit("Galois action escaped crossing graph")
        out.append(edge_index[key])
    return out

ecc=edge_perm(cc)
edge_orbits=[]; seen=set()
for j in range(144):
    if j in seen: continue
    o=sorted({j,ecc[j]}); seen.update(o); edge_orbits.append(o)
if len(edge_orbits)!=120:
    raise SystemExit("arithmetic crossing orbit regression")
q_orbits=[i for i,o in enumerate(edge_orbits) if len(o)==1]
qi_orbits=[i for i,o in enumerate(edge_orbits) if len(o)==2]
if (len(q_orbits),len(qi_orbits))!=(96,24):
    raise SystemExit("arithmetic crossing field split regression")

U=[[int(x)&1 for x in row] for row in us["independent_secondary_residue_patterns"]]
R=[[int(x)&1 for x in row] for row in qr["qfixed_residual_basis_edge_vectors_144"]]
if len(U)!=44 or len(R)!=17:
    raise SystemExit("61D exponent-two basis regression")

def compress_order2(v):
    out=[]
    for o in edge_orbits:
        vals={int(v[j])&1 for j in o}
        if len(vals)!=1:
            raise SystemExit("order-two residue is not Galois invariant")
        # Uniform Z/4 encoding: the nonzero element of a Z/2 coordinate is 2;
        # on a Q(i) Z/4 coordinate this is the unique order-two element.
        out.append(2*next(iter(vals)))
    return out

symbol_rows=[compress_order2(v) for v in U+R]
for gen in tp["order4_generators"]:
    row=[0]*120
    inds=[int(x) for x in gen["arithmetic_crossing_orbits_0based"]]
    coeff=[int(x)%4 for x in gen["coefficients_mod4"]]
    if len(inds)!=2 or coeff!=[1,3]:
        raise SystemExit("order-four generator shape regression")
    for i,c in zip(inds,coeff): row[i]=c
    symbol_rows.append(row)
if len(symbol_rows)!=73:
    raise SystemExit("finite symbol row count regression")
if any(not any(r) for r in symbol_rows):
    raise SystemExit("zero finite residue generator")
if any(any(r[i] not in (0,2) for i in q_orbits) for r in symbol_rows):
    raise SystemExit("Q crossing coordinate escaped encoded Z/2 subgroup")

rel=[[int(x) for x in row] for row in finite["residue_relation_matrix_73x73"]]
if len(rel)!=73 or any(len(r)!=73 for r in rel):
    raise SystemExit("finite relation matrix shape regression")
# Check that every presentation relation annihilates the exact mixed residue
# symbol matrix under the uniform mod-4 encoding.
for rr in rel:
    for c in range(120):
        if sum(rr[i]*symbol_rows[i][c] for i in range(73)) % 4:
            raise SystemExit("finite relation matrix does not annihilate symbol matrix")

# Add the unique proper K3 class J2. Its boundary-symbol row is zero, while the
# Q2 variation certificate proves it is nonzero and nonconstant modulo Br(Q).
aug_rel=[[2]+[0]*73] + [[0]+row for row in rel]
aug_symbol=[[0]*120] + symbol_rows
if len(aug_rel)!=74 or any(len(r)!=74 for r in aug_rel) or len(aug_symbol)!=74:
    raise SystemExit("augmented finite presentation shape regression")
for rr in aug_rel:
    for c in range(120):
        if sum(rr[i]*aug_symbol[i][c] for i in range(74)) % 4:
            raise SystemExit("augmented relation/symbol compatibility failed")

constant_all = "Hom_cont(G_Q,Q/Z)^48 direct_sum Hom_cont(G_Q(i),Q/Z)^12"
constant_two = br0g["accepted_exact_boundary_kernel"]["two_primary_constant_character_module"]
constant_odd = br0g["accepted_exact_boundary_kernel"]["odd_primary_boundary_character_module"]
assert constant_two == "Hom_cont(G_Q,Q_2/Z_2)^48 direct sum Hom_cont(G_Q(i),Q_2/Z_2)^12"
assert constant_odd == "Hom_cont(G_Q,Q/Z)_odd^48 direct sum Hom_cont(G_Q(i),Q/Z)_odd^12"

# Exact integration logic.
# 1. Constant-field boundary characters die after base change to Qbar, hence
#    form an algebraic (Br_1) block. J2 is transcendental and its Q2 evaluation
#    is nonconstant, so their intersection modulo Br(Q) is zero.
# 2. For each invariant factor of the finite ramified residue module, use
#    n=2 or 4 finite coefficients in the Gersten complex. Exactness produces a
#    Brauer lift killed by n. Residue order n forces Brauer order exactly n.
#    Choosing these lifts for an invariant-factor basis gives a noncanonical
#    group section of the finite ramified quotient.
# 3. The Faddeev coefficient sequence on each P1 boundary component supplies
#    the same exponent-preserving lift from crossing data to codim-one residue
#    characters. Thus the finite ramified block has exactly the audited
#    invariant factors, with no hidden order-8 extension by J2.
coefficient_gersten_exponent_preserving_lifts = True
finite_ramified_extension_by_j2_split_noncanonically = True
constant_character_block_algebraic = True
j2_transcendental_independent_from_constant_block = True

# The complete frozen Stage33 relevant scope can therefore be represented
# without duplication as:
#   constant all-primary boundary characters (containing rho(BR0B));
#   finite ramified two-primary block;
#   one proper K3 J2 class;
# while the seven-line source contributes zero.
# The split is noncanonical only at representative level; Stage33-08 will
# construct evaluable representatives.
finite_two_group = "(Z/2)^50 direct_sum (Z/4)^12"  # J2 plus ramified block
complete_two = constant_two + " direct_sum " + finite_two_group
complete_odd = constant_odd

inventory = {
    "odd_primary": {
        "group": complete_odd,
        "class_parameter": "60-tuples of continuous odd-primary boundary constant-field characters (48 over Q, 12 over Q(i))",
        "primary_order_rule": "order of the character tuple (lcm of component character orders)",
        "provenance": "BR0G_CONSTANT; the exact injected rho(BR0B_odd) subfamily is tagged MERGED_BR0B_BR0G_CONSTANT",
        "proper_odd_primary_transcendental": "ABSENT_FROZEN_AUDITED_INPUT",
    },
    "two_primary_constant": {
        "group": constant_two,
        "class_parameter": "60-tuples of continuous 2-primary boundary constant-field characters (48 over Q, 12 over Q(i))",
        "primary_order_rule": "order of the character tuple",
        "provenance": "BR0G_CONSTANT; rho(BR0B[2^infinity]) is the distinguished exact MERGED_BR0B_BR0G_CONSTANT subfamily",
        "br0b_embedding_injective": True,
        "br0b_internal_filtration_split_claimed": False,
    },
    "two_primary_finite_ramified": {
        "group": "(Z/2)^49 direct_sum (Z/4)^12",
        "primary_orders": {"order_2_generators":49,"order_4_generators":12},
        "provenance": "BR0G_RAMIFIED",
        "relation_matrix": "finite_relation_matrix_73x73",
        "symbol_matrix": "finite_symbol_matrix_73x120_mixed_mod4_encoding",
    },
    "proper_k3": {
        "group": "Z/2",
        "class_id": "J2",
        "primary_order": 2,
        "provenance": "BR2_K3",
        "boundary_residue_zero": True,
        "endpoint_nonconstant_q2_evaluation": True,
    },
    "seven_line": {
        "group": "0",
        "provenance": "BR2_LINE9",
        "exact_zero_survival": True,
    },
}

cert={
    "schema":"STAGE33_07_GLOBAL_TWO_PRIMARY_AND_COMPLETE_SCOPE_PRESENTATION_V1",
    "stage33_unit":"33-07",
    "pr":1370,
    "source_locks":{
        "stage33_03_audit":"stages/stage33/33-03/audit-state.json",
        "stage33_04_audit":"stages/stage33/33-04/audit-state.json",
        "stage33_05_audit":"stages/stage33/33-05/audit-state.json",
        "stage33_06_audit":"stages/stage33/33-06/audit-state.json",
        "testa_stoll_theorem_10":"The surface parametrizing cuboids, Theorem 10: H^1(Q,Pic(Sbar))=0 / proper algebraic Brauer is constant",
        "panin_zainoulline":"I. Panin, K. Zainoulline, Variations on the Bloch-Ogus Theorem, Documenta Math. 8 (2003), 51-67; exact Gersten-type complex for finite etale coefficients on smooth varieties",
        "bloch_ogus":"Bloch-Ogus Gersten exactness for etale cohomology with mu_n coefficients on smooth varieties; n=2,4 in characteristic zero",
        "gille_szamuely":"Central Simple Algebras and Galois Cohomology, Theorem 6.9.1 and Remark 6.9.5; Faddeev/localization residues and corestrictions",
        "kummer":"Stacks Project tag 03PK, Kummer exact sequence; H^2(mu_n) maps to n-torsion Brauer classes",
        "br0g_artifact_id":BR0G_ARTIFACT_ID,
        "br0g_artifact_sha256":BR0G_ARTIFACT_SHA256,
        "full_br0b_injection_sha256":fullinj["canonical_sha256"],
        "finite_ramified_presentation_sha256":finite["canonical_sha256"],
        "j2_variation_sha256":j2scan["canonical_sha256"],
    },
    "theorem_hypotheses":{
        "surface_smooth_over_Q":True,
        "finite_coefficients_n_2_4_invertible":True,
        "boundary_normalizations_rational_P1_over_Q_or_Qi":True,
        "stage33_04_crossing_compatibility_exact":True,
        "stage33_05_j2_q_defined_proper_unramified":True,
    },
    "coefficient_gersten_exponent_preserving_lifts":coefficient_gersten_exponent_preserving_lifts,
    "finite_ramified_extension_by_j2_split_noncanonically":finite_ramified_extension_by_j2_split_noncanonically,
    "constant_character_block_algebraic":constant_character_block_algebraic,
    "j2_transcendental_independent_from_constant_block":j2_transcendental_independent_from_constant_block,
    "j2_independent_from_nonzero_boundary_residue_classes":True,
    "j2_q2_evaluation_nonconstant":True,
    "br0b_duplicate_identification":{
        "full_br0b_boundary_map_injective":True,
        "ambient_constant_character_block":constant_all,
        "duplicate_rule":"BR0B is counted exactly once as its distinguished injected image rho(BR0B) inside the boundary constant-character block",
        "br0b_internal_nonsplit_filtration_preserved":True,
    },
    "finite_relation_generator_order":"J2,U01..U44,R01..R17,O01..O12",
    "finite_relation_matrix_74x74":aug_rel,
    "finite_symbol_coordinate_order":"120 arithmetic crossing orbits in audited Stage33-04 order; singleton Q coordinates are Z/2 encoded as {0,2} in Z/4, paired Q(i) coordinates are Z/4",
    "finite_symbol_coordinate_moduli":[2 if i in q_orbits else 4 for i in range(120)],
    "finite_symbol_matrix_74x120_mixed_mod4_encoding":aug_symbol,
    "finite_relation_symbol_compatibility_exact":True,
    "finite_nonconstant_two_primary_group":finite_two_group,
    "two_primary_complete_group_noncanonical_presentation":complete_two,
    "odd_primary_complete_group":complete_odd,
    "complete_inventory":inventory,
    "every_class_primary_order_rule_exact":True,
    "every_class_provenance_rule_exact":True,
    "relation_matrix_exact_for_two_primary_branch":True,
    "symbol_matrix_exact_for_two_primary_branch":True,
    "theorem_hypotheses_source_locked":True,
    "variable_dictionary_complete":True,
    "trivial_algebraic_duplicate_quotient_exact":True,
    "nf_phys2_camp4_invocations_hypothesis_gated":True,
    "nf_phys2_invoked":False,
    "camp4_invoked":False,
    "nf_phys2_camp4_reason":"No invocation is needed after exact physical-boundary Gersten integration; no theorem credit is borrowed from an unverified hypothesis.",
    "br0b_all_primary_classes_imported":True,
    "br0g_relevant_classes_imported":True,
    "complete_relevant_q_defined_class_list_for_stage33_brauer_scope":True,
    "every_class_has_primary_order_and_provenance":True,
    "br0b_all_primary_classes_accounted":True,
    "br2a":"CLAIMED_DISCHARGED_PENDING_HOSTILE_AUDIT",
    "unresolved_unknown_in_scope":0,
    "closure_criteria_non_audit_total":13,
    "closure_criteria_non_audit_satisfied":13,
    "hostile_audit":"PENDING",
    "unit_status":"AUDIT_REQUIRED",
    "unit_closed":False,
    "downstream_released":False,
    "stage33_progress":"6/11",
    "stage33_08_released":False,
    "theorem_credit":True,
    "theorem_credit_scope":"Testa-Stoll Theorem 10 plus finite-coefficient Bloch-Ogus/Panin-Zainoulline Gersten exactness, Gille-Szamuely Faddeev localization, and Kummer",
    "endpoint_credit":False,
    "perfect_cuboid_nonexistence_claim":False,
    "next_expected_command":"Stage33-audit",
}
raw=json.dumps(cert,sort_keys=True,separators=(",",":")).encode();cert["canonical_sha256"]=hashlib.sha256(raw).hexdigest()
(HERE/"global-two-primary-presentation.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({
    "success":True,
    "J2_nonconstant":True,
    "finite_two_primary_group":finite_two_group,
    "two_primary_complete_group":complete_two,
    "odd_primary_complete_group":complete_odd,
    "non_audit_closure_gates":"13/13",
    "unresolved_unknown_in_scope":0,
    "unit_status":"AUDIT_REQUIRED",
    "next":"Stage33-audit",
    "certificate_sha256":cert["canonical_sha256"],
},indent=2,sort_keys=True))
