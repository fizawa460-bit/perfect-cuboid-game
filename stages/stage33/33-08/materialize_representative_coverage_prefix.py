#!/usr/bin/env python3
"""Stage33-08 first production leaf: exact representative coverage prefix.

This leaf does not claim BR2B closure. It source-locks the audited Stage33-07
class inventory, materializes the already-known exact J2 endpoint CSA, and
replays the audited BR0G artifact to identify which open-algebraic/unit
representatives are already explicit versus which global Gersten sections
still have to be constructed.
"""
import hashlib
import io
import json
import os
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

import sympy as sp

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
            "User-Agent": "perfect-cuboid-stage33/3.0",
        },
    )
    with urllib.request.build_opener(StripCrossHostAuthRedirect()).open(req, timeout=90) as resp:
        raw = resp.read()
    got = hashlib.sha256(raw).hexdigest()
    if got != BR0G_ARTIFACT_SHA256:
        raise SystemExit(f"BR0G artifact digest mismatch: {got}")
    return zipfile.ZipFile(io.BytesIO(raw))


controller = load(S33 / "controller.json")
s07 = load(S33 / "33-07" / "audit-state.json")
j2_source = (S33 / "33-05" / "j2_arithmetic_descent.py").read_text(encoding="utf-8")

assert controller["stage33_progress"] == "7/11"
assert controller["stage33_08_released"] is True
assert controller["stage33_08_release_allowed"] is True
assert s07["unit_status"] == "CLOSED" and s07["hostile_audit"] == "PASS"
assert s07["br2a"] == "DISCHARGED"
assert s07["unresolved_unknown_in_scope"] == 0
assert s07["global_inventory"]["complete_relevant_q_defined_class_list"] is True
assert s07["global_inventory"]["every_class_primary_order_and_provenance_exact"] is True

required_j2_fragments = [
    "L=Q(t)[alpha]/(t^2*(1-alpha^2)^2+alpha^2*(1-t^2)^2)",
    "ell_J2=4*(alpha^2*t^2+t^4-4*t^2+2)/",
    "((t^2-1)*(t^2-2*t-1))",
    "Cor_{L(C)/Q(t)(C)}((ell_J2, s-alpha)_2)",
]
for needle in required_j2_fragments:
    if needle not in j2_source:
        raise SystemExit(f"J2 representative source-lock missing: {needle}")

with download_br0g() as zf:
    linear = json.loads(zf.read("linear-factor-unit-lifts.json"))
    us = json.loads(zf.read("unit-symbol-residue-span.json"))
    tp = json.loads(zf.read("two-primary-prime-power-gersten-descent.json"))

assert linear["unit_lattice_rank"] == 14
assert len(linear["ratio_lifts"]) == 17
M = sp.Matrix([r["coordinates_in_audited_U_D_basis"] for r in linear["ratio_lifts"]])
assert M.shape == (17, 14)
explicit_linear_ratio_rank = int(M.rank())
assert explicit_linear_ratio_rank == 11
row_pivots = list(M.T.rref()[1])
assert len(row_pivots) == 11
explicit_linear_units = [linear["ratio_lifts"][i]["ratio"] for i in row_pivots]

assert us["unit_divisor_lattice_rank"] == 14
assert us["unit_symbol_secondary_residue_span_rank_f2"] == 44
assert us["explicit_q_rational_unit_functions_materialized"] is False
assert tp["full_two_primary_prime_power_gersten_character_descent_complete"] is True
assert tp["order4_generator_count"] == 12
assert tp["two_primary_ramified_crossing_module"] == "(Z/2)^49 direct_sum (Z/4)^12"

j2 = {
    "class_id": "J2",
    "primary_order": 2,
    "provenance": "BR2",
    "field_of_definition": "Q",
    "branch_algebra": "L=Q(t)[alpha]/(t^2*(1-alpha^2)^2+alpha^2*(1-t^2)^2)",
    "symbol_or_algebra_representative": (
        "Cor_{L(C)/Q(t)(C)}((ell_J2,s-alpha)_2), "
        "ell_J2=4*(alpha^2*t^2+t^4-4*t^2+2)/"
        "((t^2-1)*(t^2-2*t-1))"
    ),
    "endpoint_dense_chart": (
        "w^2=t^2*(1-s^2)^2+s^2*(1-t^2)^2; "
        "c^2=(1-t^2)^2*(1-s^2)^2+4*w^2"
    ),
    "second_slot_norm": "Norm_L/Q(t)(s-alpha)=w^2/t^2",
    "ramification_support": [],
    "denominator_support_direct_formula": [
        "t=0", "w=0", "t^2-1=0", "t^2-2*t-1=0"
    ],
    "direct_evaluation_domain": "t*w*(t^2-1)*(t^2-2*t-1) != 0",
    "proper_unramified_class": True,
    "endpoint_pullback_nonzero": True,
    "equivalence_independence_certificate": {
        "stage33_07_audit": "J2 exact order 2, proper transcendental, independent from constant-character and nonzero-boundary-residue blocks",
        "q2_evaluation_nonconstant": True,
        "q2_invariants_observed": ["0", "1/2"]
    },
    "exact_evaluable_representative_on_dense_chart": True,
    "physical_open_patch_cover_complete": False
}

coverage = [
    {
        "family_id": "BR0G_ODD_CONSTANT_CHARACTERS",
        "inventory_group": s07["global_inventory"]["odd_primary_complete_group"],
        "primary_orders": "all odd primary character orders",
        "provenance": "BR0G/MERGED_BR0B",
        "accounted": True,
        "exact_evaluable_representatives_complete": False,
        "missing_work": "global explicit Gersten/Faddeev section to endpoint CSA for all 60 boundary component-character coordinates"
    },
    {
        "family_id": "BR0G_TWO_PRIMARY_CONSTANT_CHARACTERS",
        "inventory_group": s07["global_inventory"]["two_primary_constant_character_group"],
        "primary_orders": "all 2-power character orders",
        "provenance": "BR0G/MERGED_BR0B",
        "accounted": True,
        "exact_evaluable_representatives_complete": False,
        "missing_work": "global explicit Gersten/Faddeev section to endpoint CSA for all 60 boundary component-character coordinates"
    },
    {
        "family_id": "BR0G_FINITE_RAMIFIED",
        "inventory_group": s07["br0g"]["finite_ramified_group"],
        "primary_orders": {"order_2_generators": 49, "order_4_generators": 12},
        "provenance": "BR0G",
        "accounted": True,
        "exact_evaluable_representatives_complete": False,
        "missing_work": "lift the exact 61 invariant-factor residue generators to explicit endpoint CSA/function representatives"
    },
    {
        "family_id": "BR2_K3_J2",
        "inventory_group": "Z/2",
        "primary_orders": [2],
        "provenance": "BR2",
        "accounted": True,
        "exact_evaluable_representatives_complete": True,
        "representative": j2
    },
    {
        "family_id": "BR2_LINE9",
        "inventory_group": "0",
        "primary_orders": [],
        "provenance": "BR2",
        "accounted": True,
        "exact_evaluable_representatives_complete": True,
        "representative": "EMPTY_EXACT_ZERO_SURVIVAL"
    }
]

residuals = [
    "R33-BR2B-REPLAY-FULL-RANK14-EXPLICIT-Q-UNIT-LATTICE",
    "R33-BR2B-GLOBAL-GERSTEN-SECTION-FOR-60-CONSTANT-CHARACTER-COORDINATES",
    "R33-BR2B-GLOBAL-GERSTEN-SECTION-FOR-61-FINITE-RAMIFIED-GENERATORS",
    "R33-BR2B-J2-PHYSICAL-OPEN-PATCH-COVER"
]

cert = {
    "schema": "STAGE33_08_REPRESENTATIVE_COVERAGE_PREFIX_V1",
    "stage33_unit": "33-08",
    "source_locks": {
        "stage33_07_audit_state": "stages/stage33/33-07/audit-state.json",
        "stage33_05_j2_source": "stages/stage33/33-05/j2_arithmetic_descent.py",
        "stage33_04_audited_artifact_id": BR0G_ARTIFACT_ID,
        "stage33_04_audited_artifact_sha256": BR0G_ARTIFACT_SHA256,
        "stage33_04_materialize_full_q_units": "stages/stage33/33-04/materialize_q_units.py"
    },
    "every_stage33_07_relevant_class_accounted": True,
    "every_surviving_class_has_primary_order_and_provenance": True,
    "j2_exact_evaluable_representative_materialized": True,
    "j2_physical_open_patch_cover_complete": False,
    "predecessor_explicit_linear_factor_ratio_count": 17,
    "predecessor_explicit_linear_factor_ratio_rank_in_U_D": explicit_linear_ratio_rank,
    "predecessor_independent_explicit_linear_units": explicit_linear_units,
    "full_unit_lattice_rank": 14,
    "full_rank14_explicit_q_unit_lattice_replay_required": True,
    "boundary_constant_character_representatives_complete": False,
    "finite_ramified_representatives_complete": False,
    "every_surviving_class_has_exact_evaluable_representative": False,
    "ramification_support_complete": False,
    "denominator_support_complete": False,
    "equivalence_independence_certificates_complete": False,
    "physical_open_domain_certified": False,
    "coverage": coverage,
    "residual_kernels": residuals,
    "unresolved_unknown_in_scope": len(residuals),
    "br2b": "RUNNING",
    "unit_status": "RUNNING",
    "unit_closed": False,
    "downstream_released": False,
    "stage33_progress": "7/11",
    "stage33_09_released": False,
    "next_exact_leaf": "L33-08-REPLAY-MATERIALIZE-Q-UNITS-THEN-BUILD-EXPLICIT-GERSTEN-SECTIONS",
    "next_expected_command": "Stage33-main-batch",
    "theorem_credit": False,
    "endpoint_credit": False,
    "brauer_manin_set_empty_proved": False,
    "perfect_cuboid_nonexistence_claim": False
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(HERE / "representative-coverage-prefix.json").write_text(
    json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "j2_exact_evaluable_representative": True,
    "stage33_07_families_accounted": len(coverage),
    "explicit_linear_unit_prefix_rank": explicit_linear_ratio_rank,
    "full_unit_rank": 14,
    "remaining_residual_count": len(residuals),
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"]
}, indent=2, sort_keys=True))
