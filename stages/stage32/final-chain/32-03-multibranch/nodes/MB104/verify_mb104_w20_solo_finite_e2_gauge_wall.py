#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

CERT=Path(__file__).with_name("MB104-W20-SOLO-FINITE-E2-GAUGE-WALL-CERTIFICATE.json")

def req(x,m):
    if not x:
        raise SystemExit("FAIL: "+m)

def add(x,y):
    return ((x[0]^y[0]),(x[1]^y[1]))

def main():
    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_W20_SOLO_FINITE_E2_GAUGE_WALL_V1","schema")
    req(c["status"]=="W20_SOLO_FINITE_E2_BRIDGE_CLOSED_NEGATIVE_NO_CREDIT","status")
    req(c["gauge_symmetry"]["cardinality"]==4,"E2 cardinality")
    req(c["gauge_symmetry"]["tau_square_trivial"] is True,"2-torsion square")

    E2=[(0,0),(1,0),(0,1),(1,1)]
    for delta in E2:
        orbit={add(delta,tau) for tau in E2}
        req(orbit==set(E2),"gauge action transitive")

    preserved=set(c["gauge_symmetry"]["preserves"])
    for key in [
        "degree(M2)",
        "M2^2",
        "square-line relation",
        "both typewise ramification line-bundle relations",
        "Riemann-Hurwitz line identity",
        "all retained branch-count/saturation equations",
    ]:
        req(key in preserved,"preserved "+key)

    s=c["separation"]
    req(s["eta_not_selected_by_factor_line_data"] is True,"eta separation")
    req(s["delta_fac_equals_eta_not_proved"] is True,"no delta=eta claim")
    req(s["normalization_data_does_not_determine_kappa"] is True,"kappa separation")
    req(s["even_if_delta_fac_equals_eta_and_eta_zero_kappa_still_unresolved"] is True,"kappa remains")

    q=c["conclusion"]
    req(q["current_factor_line_interface_can_select_delta_fac"] is False,"cannot select delta")
    req(q["current_finite_E2_bridge_can_close_e2"] is False,"cannot close e2")
    req(q["current_finite_E2_bridge_can_bound_weighted_conductor_cut"] is False,"cannot bound cut")
    req(q["branch_specific_residual_lift_or_singular_carrier_descent_required"] is True,"branch-specific required")

    req(c["disposition"]=="CLOSED_NEGATIVE_AS_FINITE_E2_BRIDGE","disposition")
    req(c["remaining_user_selected_solo_routes"]==["W16"],"remaining route")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_W20_SOLO_FINITE_E2_GAUGE_WALL_V1")
    print("E2_twist_action=simply_transitive")
    print("delta_fac_not_selected; eta_and_kappa_separated")
    print("W20=closed_negative_as_finite_E2_bridge no_credit")

if __name__=="__main__":
    main()
