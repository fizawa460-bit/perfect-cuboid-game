#!/usr/bin/env python3
"""Fail-closed verifier for the Stage30-08 physical-endpoint adapter decision.

This verifier intentionally depends only on audited static stage artifacts and the
Stage30-08 manifest.  It does not SHA-pin mutable controller state.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def load_json(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def load_text(rel: str):
    return (ROOT / rel).read_text(encoding="utf-8")


ledger = load_json("stages/stage29/29-16/active-kernel-ledger.json")
mod1d = load_text("stages/stage29/29-15/bounded-execution.md")
qmod = load_text("stages/stage29/29-02g/exact-q-moduli-adapter.md")
a06c = load_json("stages/stage30/30-06C/audit-state.json")
a07 = load_json("stages/stage30/30-07/audit-state.json")
out = load_json("stages/stage30/30-08/physical-adapter.json")

kernels = {row["kernel"]: row for row in ledger["class2_kernels"]}
require("K16-C2-MODULAR-S4-ACTION" in kernels, "frozen modular kernel missing")
k = kernels["K16-C2-MODULAR-S4-ACTION"]
require(k["children"] == ["R29-KUM5"], "unexpected receiver mapping")
require(k["parent_routes"] == ["Q11-MODULAR"], "unexpected parent route")
require(
    k["exact_wall"] == "action-level arrangement-to-modular S4 identification compatible with the audited Q/Q(i) descent cocycles",
    "frozen exact wall changed",
)
require(
    k["completion_consequence"] == "attach the eight marked modular defects to the exact arrangement action",
    "frozen completion consequence changed",
)
require(k["endpoint_decisive_alone"] is False, "kernel endpoint-decisive firewall changed")

require("STATUS=AUDITED_PASS_ON_NONCUSP_FINE_MODULI_LOCUS" in qmod, "noncusp Q-moduli adapter missing")
require("R29-MOD1D=DISCHARGED_PHYSICAL_OPEN_NONCUSP_STABILIZER_FREE" in mod1d,
        "physical-open MOD1D discharge missing")
require("PHYSICAL_ENDPOINT_INTERSECTS_MODULAR_CUSP_LOCUS=false" in mod1d,
        "physical cusp exclusion missing")
require("PHYSICAL_ENDPOINT_MODULAR_G0_STABILIZER_TRIVIAL=true" in mod1d,
        "physical stabilizer statement missing")

f = a06c["finite_certificate"]
require(f["modular_group_order"] == 24, "wrong modular group order")
require(f["endpoint_projective_group_order"] == 24, "wrong endpoint group order")
require(f["theta_all24_verified"] is True, "theta not verified for all 24")
require(f["c_sigma"] == "delta_a3", "wrong coordinate cocycle")
require(f["c_sigma_cocycle_verified"] is True, "coordinate cocycle unverified")
require(f["semilinear_all24_verified"] is True, "semilinear identity not verified")
require(f["failed_element_count"] == 0, "semilinear failures present")

require(a07["k8_order"] == 8, "wrong K8 order")
require(a07["all_24x8_equivariance_verified"] is True, "24x8 defect transport unverified")
require(a07["ordinary_s4_orbit_sizes"] == [1, 3, 3, 1], "ordinary orbit sizes changed")
require(a07["sigma_action_on_k8"] == "TRIVIAL", "sigma action changed")
require(a07["marked_q_descent_class_count"] == 8, "wrong marked class count")
require(a07["marked_classes_are_singletons"] is True, "marked classes not singleton")
require(a07["defect_elimination_count"] == 0, "unexpected defect elimination")

require(out["roadmap_outcome"] == "B_R29_KUM5_DISCHARGED_ZERO_DEFECT_ELIMINATION", "wrong Stage30-08 outcome")
require(out["source_scope"]["physical_open_non_cusp"] is True, "physical noncusp scope not recorded")
require(out["source_scope"]["physical_open_g0_stabilizer_free"] is True, "physical stabilizer scope not recorded")
require(out["source_scope"]["compactified_boundary_extension_required_for_physical_open"] is False,
        "illegal compactification dependency")
require(out["receiver_decision"]["r29_kum5_discharged_if_audit_passes"] is True, "receiver not proposed discharged")
require(out["receiver_decision"]["smaller_residual_class2_leaf_created"] is False, "unexpected residual Class2 leaf")
require(out["receiver_decision"]["new_class3_theorem_gate_created"] is False, "unexpected Class3 gate")
require(out["route_decision"]["q11_modular_color_before"] == "AMBER", "wrong prior route color")
require(out["route_decision"]["q11_modular_color_after"] == "AMBER", "route color changed illegally")
require(out["route_decision"]["physical_endpoint_exclusion_proved"] is False, "illegal endpoint exclusion")
require(out["completed_adapter"]["defect_elimination_count"] == 0, "manifest elimination mismatch")
require(out["research_os_delta_if_audited"]["active_kernel_count_after"] == 12, "wrong prospective active kernel count")
require(out["research_os_delta_if_audited"]["class2_kernel_count_after"] == 3, "wrong prospective Class2 count")
require(out["research_os_delta_if_audited"]["class3_kernel_count_after"] == 9, "wrong prospective Class3 count")

for key, value in out["firewalls"].items():
    require(value is False, f"firewall must remain false: {key}")

print("FROZEN_R29_KUM5_WALL=PASS")
print("PHYSICAL_OPEN_NONCUSP_STABILIZER_FREE=PASS")
print("SEMILINEAR_ALL24=PASS")
print("K8_EIGHT_STATE_TRANSPORT=PASS")
print("DEFECT_ELIMINATION_COUNT=0")
print("ROADMAP_OUTCOME=B")
print("R29_KUM5_DISCHARGE_SUBMITTED_PENDING_AUDIT=true")
print("Q11_MODULAR_COLOR=AMBER")
print("PASS")
